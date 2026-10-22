#!/usr/bin/env python3
"""Post-publish verification for the Gilded Pages healthcare rollout.

Batch job (fixed instructions; do not change without the admin's say-so).

Checks, after a daily healthcare rollout batch has been published:
  1. Index check: the live index.html md5 vs the working-copy index.html md5.
  2. Per slug: (a) the slug string appears in the LIVE index text, and
     (b) the live big-<slug>.webp md5 vs the local images file md5.

Prints the full output to stdout AND writes the same output to a dated log:
  ~/workspace/batch-logs/gilded-pages-healthcare-rollout/YYYY-MM-DD.log
(America/Phoenix date, unless --date is given.)

Last line is exactly:
  VERDICT: PASS
or
  VERDICT: FAIL -- <reason>   (with an em dash before the reason)

Exit code: 0 on PASS, 1 on FAIL.

Downloads go to a temporary directory that is removed on exit.
Python 3 standard library only.
"""

import argparse
import contextlib
import hashlib
import http.client
import io
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

JOB_DIR = "gilded-pages-healthcare-rollout"
LIVE_BASE = "https://claypnw.github.io/gilded-pages"
LIVE_INDEX_URL = LIVE_BASE + "/index.html"
WORKING_INDEX = Path.home() / "workspace" / "BACKUP-github-websites-only" / "gilded-pages" / "index.html"
LOCAL_IMAGES_DIR = Path.home() / "workspace" / "gilded-pages" / "images"
LOG_ROOT = Path.home() / "workspace" / "batch-logs" / JOB_DIR
TZ = ZoneInfo("America/Phoenix")
USER_AGENT = "gilded_verify/1.0 (batch post-publish verification)"
DOWNLOAD_TIMEOUT = 60  # seconds

# --- Rule log (Clay's design, 2026-10-18) ---------------------------------
# This program writes its own rule-log marks via ~/workspace/batch/rulelog.py
# (design: ~/workspace/morning-post/RULE-LOG-DESIGN.md). Marks are decided by
# values this program itself computed — never by exit code alone and never
# by a default evidence string. Rule logging is additive only: it must never
# change this program's output or exit code, so every call is guarded and
# the writer's own prints are captured, not shown.
try:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import rulelog as _rulelog
except Exception:  # rule log unavailable — the program runs as before
    _rulelog = None

_RL_PATH = None
_RL_TOTAL = 0
_RL_LABELS = {}
_RL_ZERO = set()


def _rl_begin(batch, labels):
    global _RL_PATH, _RL_TOTAL, _RL_LABELS
    _RL_LABELS = dict(labels)
    _RL_TOTAL = len(labels)
    if _rulelog is None:
        return
    try:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            _rulelog.cmd_begin(batch, _rulelog.now().strftime("%Y-%m-%d"), _RL_TOTAL)
        _RL_PATH = buf.getvalue().strip().splitlines()[-1]
    except Exception:
        _RL_PATH = None


def _rl(kind, n, evidence=""):
    if _rulelog is None or _RL_PATH is None:
        return
    try:
        _rulelog.mark(_RL_PATH, n, _RL_LABELS.get(n, f"step_{n}"), kind, evidence)
        if kind == "FAIL":
            _RL_ZERO.add(n)
    except Exception:
        pass


def _rl_finish(failed):
    """Close the rule log. If the program failed but no step stands at 0,
    put the last step at 0 with a generic reason — the program's own
    output carries the detail."""
    if _rulelog is None or _RL_PATH is None:
        return
    try:
        if failed and not _RL_ZERO and _RL_TOTAL:
            _rl("FAIL", _RL_TOTAL,
                "program reported failure at exit — see program output for the reason")
        with contextlib.redirect_stdout(io.StringIO()):
            _rulelog.cmd_close(_RL_PATH)
    except Exception:
        pass


# --- Shared error program (standards wiring step A, 2026-10-21) -------------
# The one shared error program is shared_error.py in this same
# directory (~/workspace/batch/). A failed verdict and any unforeseen
# error are reported to it, so an error record opens in the one place.
# The standard processing — write the error down in full in the dated
# error record, open an ERROR line in the completion pile, hand back
# STOP — happens in that one program, never in code copied here. This
# block is only the call. If the shared error program cannot be loaded
# or cannot record, the report prints a loud line on stderr and this
# program's own output, dated log, verdict line, and exit code are
# unchanged.
def _load_shared_error():
    for parent in Path(__file__).resolve().parents:
        for candidate in (parent / "shared_error.py",
                          parent / "batch" / "shared_error.py"):
            if candidate.is_file():
                try:
                    if str(candidate.parent) not in sys.path:
                        sys.path.insert(0, str(candidate.parent))
                    from shared_error import report_error
                    return report_error
                except Exception:
                    # A shared error program that is present but
                    # fails to load is treated the same as one
                    # that cannot be found: fall back, never
                    # raise at startup.
                    continue
    return None


_shared_report_error = _load_shared_error()


def _report_to_shared_error(step, error, kind="foreseen"):
    """Send one error to the one shared error program. Never raises."""
    if _shared_report_error is None:
        print(f"SHARED ERROR PROGRAM UNAVAILABLE — error not recorded: {error}",
              file=sys.stderr)
        return None
    try:
        return _shared_report_error(
            program=Path(__file__).name, step=step, error=error, kind=kind,
            error_type="FailedVerdict" if kind == "check_failed" else None)
    except Exception as exc:
        print(f"SHARED ERROR PROGRAM FAILED — error not recorded: {exc}",
              file=sys.stderr)
        return None


def md5_of_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


DOWNLOAD_ATTEMPTS = 5  # whole-file re-reads when a download comes up short


class IncompleteDownloadError(OSError):
    """A download never arrived complete, so nothing from it may be
    hashed or compared. An OSError subclass, so the callers' existing
    download-failed handling takes it — a short download is reported
    as a failed download, never as an md5 mismatch against the site.
    (Fix 2026-10-22, OPEN-WORK item 10: downloads through this machine's
    connection are sometimes cut short; the program used to hash the
    cut-off file and print VERDICT: FAIL against a correct site.)"""


def download(url, dest):
    """Download url to dest (a file inside the temp dir). Returns dest.

    When the server states a length (Content-Length), the bytes on
    disk are counted against it. A download that falls short — or one
    cut mid-transfer — is re-read from the start, up to
    DOWNLOAD_ATTEMPTS times. Only a complete file is returned; if no
    attempt arrives complete, IncompleteDownloadError is raised.
    A response with no stated length is accepted as before: there is
    no stated length to check it against.
    """
    last_short = None
    for _attempt in range(DOWNLOAD_ATTEMPTS):
        expected = None
        got = 0
        cut = False
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=DOWNLOAD_TIMEOUT) as resp:
                length = resp.headers.get("Content-Length")
                if length is not None:
                    try:
                        expected = int(length)
                    except ValueError:
                        expected = None
                with open(dest, "wb") as out:
                    while True:
                        chunk = resp.read(1024 * 1024)
                        if not chunk:
                            break
                        out.write(chunk)
                        got += len(chunk)
        except (http.client.IncompleteRead, ConnectionError) as e:
            # Cut mid-transfer: retry from the start, whatever the
            # stated length — a cut transfer is never a complete file.
            cut = True
            got = dest.stat().st_size if dest.exists() else 0
            last_short = f"{e} (got {got} bytes)"
        if not cut and (expected is None or got >= expected):
            return dest
        if not cut:
            last_short = f"got {got} of {expected} bytes"
    raise IncompleteDownloadError(
        f"download incomplete after {DOWNLOAD_ATTEMPTS} attempts: "
        f"{last_short} from {url}")


def normalize_slug(raw):
    """Accept a slug with or without the 'big-' prefix; return the bare slug."""
    s = raw.strip()
    if s.startswith("big-"):
        s = s[len("big-"):]
    # Tolerate a full filename being listed instead of a bare slug.
    if s.endswith(".webp"):
        s = s[: -len(".webp")]
    return s


# --- Start and finish records (standards wiring step B, 2026-10-21) --------
# This program writes a start line when it begins and a finish line
# when it ends well, both through the one shared finish-line writer,
# ~/workspace/work-launcher/write_finish_line.py — the same writer the
# morning jobs write their finish lines through, called the same way.
# A run that fails writes no finish line: its error goes to the one
# shared error program (the block above), and the pile carries the
# ERROR line instead. These calls are records only: they never change
# this program's own output, dated log, verdict line, or exit code,
# and a failed record write prints a loud line on stderr.
import subprocess as _subprocess
from datetime import datetime as _datetime
from pathlib import Path as _Path
from zoneinfo import ZoneInfo as _ZoneInfo


def _finish_writer_path():
    for parent in _Path(__file__).resolve().parents:
        candidate = parent / "work-launcher" / "write_finish_line.py"
        if candidate.is_file():
            return candidate
    return None


_FINISH_WRITER = _finish_writer_path()


def _write_pile_line(mode, result, rests_on):
    """Write one start or finish line through the shared writer."""
    if _FINISH_WRITER is None:
        print("FINISH-LINE WRITER UNAVAILABLE — record line not written",
              file=sys.stderr)
        return
    try:
        proc = _subprocess.run(
            [sys.executable, str(_FINISH_WRITER), mode,
             _Path(__file__).name,
             _datetime.now(_ZoneInfo("America/Phoenix")).strftime("%Y-%m-%d"),
             result, rests_on],
            check=False, capture_output=True, text=True)
    except Exception as exc:
        print(f"FINISH-LINE WRITER FAILED — record line not written: {exc}",
              file=sys.stderr)
        return
    if proc.returncode != 0:
        detail = (proc.stdout or "").strip() or (proc.stderr or "").strip()
        print(f"FINISH-LINE WRITER STOPPED — record line not written: {detail}",
              file=sys.stderr)


def _write_start_line():
    _write_pile_line("start", "run started", "this run's own output")


def _write_finish_line(result, rests_on):
    _write_pile_line("finish", result, rests_on)


def _main(argv=None):
    _write_start_line()
    parser = argparse.ArgumentParser(
        description="Post-publish verification for the Gilded Pages healthcare rollout."
    )
    parser.add_argument("--slugs", required=True, help="Path to a text file, one slug per line.")
    parser.add_argument(
        "--date",
        default=None,
        help="Log date YYYY-MM-DD (America/Phoenix). Default: today in America/Phoenix.",
    )
    args = parser.parse_args(argv)

    _rl_begin("gilded", {
        1: "read_slugs",
        2: "index_check",
        3: "slug_checks",
    })
    _rl("START", 1)

    if args.date:
        try:
            datetime.strptime(args.date, "%Y-%m-%d")
        except ValueError:
            _rl("FAIL", 1, f"--date must be YYYY-MM-DD, got: {args.date}")
            print(f"ERROR: --date must be YYYY-MM-DD, got: {args.date}", file=sys.stderr)
            return 2
        log_date = args.date
    else:
        log_date = datetime.now(TZ).strftime("%Y-%m-%d")

    lines = []

    def out(text=""):
        lines.append(text)

    failures = []  # short reason fragments for the verdict line

    out("Gilded Pages healthcare rollout — post-publish verification")
    out(f"Date (America/Phoenix): {log_date}")
    out(f"Live site: {LIVE_BASE}/")
    out(f"Slugs file: {args.slugs}")
    out(f"Working copy index: {WORKING_INDEX}")
    out(f"Local images dir: {LOCAL_IMAGES_DIR}")
    out("")

    # --- Read the slug list -------------------------------------------------
    slugs = []
    slugs_path = Path(args.slugs)
    if not slugs_path.is_file():
        out(f"Slugs file: NOT FOUND — {slugs_path}")
        failures.append(f"slugs file not found: {slugs_path}")
    else:
        for raw in slugs_path.read_text(encoding="utf-8").splitlines():
            if not raw.strip() or raw.strip().startswith("#"):
                continue
            slug = normalize_slug(raw)
            if slug:
                slugs.append(slug)
        out(f"Slugs to check: {len(slugs)}")
        for slug in slugs:
            out(f"  - {slug}")
        if not slugs:
            failures.append("no slugs in slugs file")
    out("")

    if not slugs_path.is_file():
        _rl("FAIL", 1, f"slugs file not found: {slugs_path}")
    elif not slugs:
        _rl("FAIL", 1, f"no slugs in slugs file: {slugs_path}")
    else:
        _rl("OK", 1, f"{len(slugs)} slugs read from {slugs_path}")
    _rl("START", 2)
    index_failures_before = len(failures)

    with tempfile.TemporaryDirectory(prefix="gilded_verify_") as tmp:
        tmpdir = Path(tmp)

        # --- 1. Index check -------------------------------------------------
        out("Index check:")
        live_index_path = tmpdir / "live-index.html"
        live_index_text = None
        live_index_md5 = None
        index_match = False
        try:
            download(LIVE_INDEX_URL, live_index_path)
            live_index_md5 = md5_of_file(live_index_path)
            live_index_text = live_index_path.read_text(encoding="utf-8", errors="replace")
            out(f"  Live index:    {LIVE_INDEX_URL}")
            out(f"  Live md5:      {live_index_md5}")
        except (urllib.error.URLError, OSError) as e:
            out(f"  Live index:    DOWNLOAD FAILED — {e}")
            failures.append(f"live index download failed: {e}")

        working_md5 = None
        if WORKING_INDEX.is_file():
            working_md5 = md5_of_file(WORKING_INDEX)
            out(f"  Working copy:  {WORKING_INDEX}")
            out(f"  Working md5:   {working_md5}")
        else:
            out(f"  Working copy:  NOT FOUND — {WORKING_INDEX}")
            failures.append("working copy index not found")

        if live_index_md5 is not None and working_md5 is not None:
            if live_index_md5 == working_md5:
                index_match = True
                out("  Result: MATCH")
            else:
                out("  Result: FAIL — md5 mismatch")
                out(
                    "  Note: Pages deploy lag is possible; the program reports "
                    "honestly either way — a mismatch may clear once the deploy finishes."
                )
                failures.append("index md5 mismatch")
        else:
            out("  Result: FAIL — could not compare (see above)")
            if "index md5 mismatch" not in failures:
                failures.append("index check could not be completed")
        out("")

        index_failures = failures[index_failures_before:]
        if index_match:
            _rl("OK", 2, f"live index md5={live_index_md5} == working copy md5={working_md5}")
        else:
            _rl("FAIL", 2, "; ".join(index_failures) if index_failures else "index check did not match")
        _rl("START", 3)
        slug_failures_before = len(failures)
        slug_pass_count = 0

        # --- 2. Per-slug checks ---------------------------------------------
        out("Per-slug checks:")
        if not slugs:
            out("  (no slugs to check)")
        for slug in slugs:
            in_live = None
            if live_index_text is not None:
                in_live = slug in live_index_text
            in_live_str = "YES" if in_live else ("NO" if in_live is not None else "UNKNOWN (no live index)")

            filename = f"big-{slug}.webp"
            live_url = f"{LIVE_BASE}/{filename}"
            local_path = LOCAL_IMAGES_DIR / filename

            live_md5 = None
            live_err = None
            try:
                live_file = download(live_url, tmpdir / filename)
                live_md5 = md5_of_file(live_file)
            except (urllib.error.URLError, OSError) as e:
                live_err = str(e)

            local_md5 = None
            if local_path.is_file():
                local_md5 = md5_of_file(local_path)

            if live_md5 is not None and local_md5 is not None:
                image_match = live_md5 == local_md5
                image_str = "MATCH" if image_match else "FAIL (md5 mismatch)"
            elif local_md5 is None:
                image_match = False
                image_str = f"FAIL (local file not found: {local_path})"
            else:
                image_match = False
                image_str = f"FAIL (live download failed: {live_err})"

            slug_pass = bool(in_live) and image_match
            if slug_pass:
                slug_pass_count += 1
            if not slug_pass:
                reasons = []
                if not in_live:
                    reasons.append("not in live index")
                if not image_match:
                    reasons.append("image md5 mismatch/failed")
                failures.append(f"slug {slug}: {', '.join(reasons)}")

            out(
                f"  {slug}: in_live_index={in_live_str} "
                f"image={filename} live_md5={live_md5 or 'NONE'} "
                f"local_md5={local_md5 or 'NONE'} image_md5={image_str} "
                f"— {'PASS' if slug_pass else 'FAIL'}"
            )
        out("")

        slug_failures = failures[slug_failures_before:]
        if not slugs:
            _rl("FAIL", 3, "no slugs to check (see step 1)")
        elif slug_failures:
            _rl("FAIL", 3, "; ".join(slug_failures))
        else:
            _rl("OK", 3, f"{slug_pass_count} of {len(slugs)} slugs in live index, all image md5s match")

    # --- 3. Overall verdict ---------------------------------------------------
    overall_pass = index_match and not failures
    if overall_pass:
        verdict_line = "VERDICT: PASS"
        exit_code = 0
    else:
        reason = "; ".join(failures) if failures else "index check did not match"
        # Keep the verdict a single line.
        reason = " ".join(reason.split())
        verdict_line = f"VERDICT: FAIL — {reason}"
        exit_code = 1
    out(verdict_line)

    output = "\n".join(lines) + "\n"
    sys.stdout.write(output)
    sys.stdout.flush()

    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    log_path = LOG_ROOT / f"{log_date}.log"
    log_path.write_text(output, encoding="utf-8")

    if exit_code != 0:
        # A failed verdict opens an error record in the one shared
        # error program. The dated log and the verdict line above are
        # unchanged — they are the evidence reports quote.
        _report_to_shared_error("verdict", verdict_line, kind="check_failed")

    if exit_code == 0:
        _write_finish_line(verdict_line, str(log_path))

    return exit_code


def main(argv=None):
    code = None
    try:
        code = _main(argv)
    except SystemExit:
        raise
    except BaseException as exc:
        # Catch-all: an error this program did not foresee goes to the
        # one shared error program, then the program stops as it would
        # have — the traceback still prints.
        _report_to_shared_error("main", exc, kind="unforeseen")
        raise
    finally:
        _rl_finish(failed=(code != 0))
    return code


if __name__ == "__main__":
    sys.exit(main())
