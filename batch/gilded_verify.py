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
import base64
import contextlib
import hashlib
import http.client
import io
import os
import socket
import ssl
import sys
import tempfile
import time
import urllib.error
import urllib.parse
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

# --- Rule log (the admin's design, 2026-10-18) ---------------------------------
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


DOWNLOAD_ATTEMPTS = 5  # tries down the step-down ladder (see download())
DOWNLOAD_WAITS = (10, 20, 40, 80)  # seconds before tries 2 to 5
DOWNLOAD_TIMEOUTS = (DOWNLOAD_TIMEOUT, DOWNLOAD_TIMEOUT, 120, 120, 120)  # per-try answer limit, seconds


class IncompleteDownloadError(OSError):
    """A download never arrived complete, so nothing from it may be
    hashed or compared. An OSError subclass, so the callers' existing
    download-failed handling takes it — a short download is reported
    as a failed download, never as an md5 mismatch against the site.
    (Fix 2026-10-22, OPEN-WORK item 10: downloads through this machine's
    connection are sometimes cut short; the program used to hash the
    cut-off file and print VERDICT: FAIL against a correct site.)"""


def _content_range(value):
    """'bytes 100-199/500' -> (100, 199, 500); a total of '*' -> None
    total; 'bytes */500' (the 416 form) -> (None, None, 500)."""
    if not value:
        return None, None, None
    try:
        unit, rest = value.split(None, 1)
        range_part, _, total_part = rest.partition("/")
        total = None if total_part in ("", "*") else int(total_part)
        if range_part == "*":
            return None, None, total
        start_s, _, end_s = range_part.partition("-")
        return int(start_s), int(end_s), total
    except (ValueError, AttributeError):
        return None, None, None


def _unfixable_transport(exc):
    """A transport failure no later try can fix: the name cannot be
    resolved, or the secure connection cannot be made. Those raise
    at once with their original error, as before this change; the
    cut, reset, refused, and timed-out kinds climb the ladder."""
    reason = getattr(exc, "reason", exc)
    return isinstance(reason, (socket.gaierror, ssl.SSLError))


class _EngineResponse:
    """A response read through the connection engine (http.client)
    directly, wearing the shape download() already judges: status,
    headers, read(n), and the with-statement. An error answer raises
    urllib.error.HTTPError, exactly as the urllib road raised, so
    the judging in download() does not change by one word.

    Why the engine directly (2026-10-27; the same record as the
    Scroll verify fix of 2026-10-26): the urllib layer over this
    engine was cut on fetch after fetch from the live sites, while
    the engine driven directly brought the same files down whole.
    The ladder, the judging, and the verdicts are unchanged; only
    the road under them moved."""

    def __init__(self, url, headers, timeout):
        parts = urllib.parse.urlsplit(url)
        host = parts.hostname
        port = parts.port or 443
        path = parts.path or "/"
        if parts.query:
            path += "?" + parts.query
        proxy = os.environ.get("https_proxy") or os.environ.get(
            "HTTPS_PROXY")
        ctx = ssl.create_default_context()
        if proxy:
            pp = urllib.parse.urlsplit(
                proxy if "//" in proxy else "//" + proxy)
            self._conn = http.client.HTTPSConnection(
                pp.hostname, pp.port or 3128, timeout=timeout,
                context=ctx)
            tunnel_headers = {}
            if pp.username:
                raw = (f"{urllib.parse.unquote(pp.username)}:"
                       f"{urllib.parse.unquote(pp.password or '')}")
                tunnel_headers["Proxy-Authorization"] = (
                    "Basic " + base64.b64encode(raw.encode()).decode())
            self._conn.set_tunnel(host, port, headers=tunnel_headers)
        else:
            self._conn = http.client.HTTPSConnection(
                host, port, timeout=timeout, context=ctx)
        self._conn.request("GET", path, headers=headers)
        self._resp = self._conn.getresponse()
        self.status = self._resp.status
        self.headers = self._resp.headers
        if self.status >= 400:
            hdrs = self._resp.headers
            self.close()
            raise urllib.error.HTTPError(
                url, self.status, f"HTTP {self.status}", hdrs, None)

    def read(self, n=-1):
        return self._resp.read(n)

    def close(self):
        try:
            self._conn.close()
        except Exception:
            pass

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
        return False


def _open_engine(url, headers, timeout):
    return _EngineResponse(url, headers, timeout)


def download(url, dest):
    """Download url to dest (a file inside the temp dir). Returns dest.

    The tries climb a step-down ladder (2026-10-26; before, a short
    download was re-read FROM THE START up to DOWNLOAD_ATTEMPTS times —
    the same whole request repeated):
      Try 1: the whole read, as before, at the standing 60-second
      limit (DOWNLOAD_TIMEOUT).
      Tries 2 to 5: RESUME — the bytes already on disk are kept, and
      the request asks only for the missing tail (a Range request
      from the byte reached), so each try asks for less than the one
      before. The waits between tries step up (10, 20, 40, 80
      seconds) and the allowed answer time steps up to 120 seconds
      from try 3 (DOWNLOAD_TIMEOUTS).

    How a resumed answer is judged (second form, after the fresh-eyes
    review proved the first form could return wrong bytes as a
    complete file):
      - A 206 (part) answer is checked BEFORE a byte of it is
        appended: its Content-Range must start exactly at the byte
        asked for, its stated total must match any total already
        learned, and its stated length must match its stated range.
        Anything else — the partial is cleared and the next try
        starts the file over; pieces are never joined on a server's
        say-so alone, and pieces of two versions are never joined
        at all (a total that changes mid-download clears and
        restarts the same way). A part is also judged AFTER it is
        read against its own stated range: more bytes than the
        range clears and restarts; FEWER bytes than the range —
        even ending cleanly, even when no total was ever stated —
        is a cut try, never a complete file (the bytes stay and
        the next try resumes from them). A fully delivered part
        whose size was never stated is also not proof of
        completeness: a server may answer an open-ended ask with
        a bounded piece, so the part's own end — and likewise the
        end reckoned from the part's stated length — proves
        nothing about the file's size. Completeness is proven
        only by a stated total being reached, a whole-file 200
        answer, or a 416 whose stated total equals the bytes on
        disk.
      - Only a 200 is a whole-file answer to a resume request, and
        it is written from the start. Any other status (a bodyless
        204, an odd success) is a failed try and the bytes on disk
        are not touched.
      - A 416 ("no such range") is judged by the total its own
        Content-Range states, against the bytes on disk: equal
        (and the bytes are the file's) — the file is complete;
        anything else — the file changed under the download (it
        shrank, or was replaced) — the partial is cleared and the
        next try starts over. A 416 never proves completeness by
        itself.
      - An HTTP answer no retry can fix (a missing file, a refused
        request) is raised at once, as before; a busy (408/429) or
        server-error answer joins the ladder. A transport failure
        no retry can fix (the name does not resolve, the secure
        connection cannot be made) is raised at once with its
        original error; cuts, resets, refusals, and time-outs join
        the ladder, the bytes on disk kept for the resume.
    Only a complete file is returned; if no try arrives complete,
    IncompleteDownloadError is raised. A response with no stated
    length is accepted as before: there is no stated length to
    check it against.
    """
    last_short = None
    expected = None

    def on_disk():
        return dest.stat().st_size if dest.exists() else 0

    for attempt in range(DOWNLOAD_ATTEMPTS):
        if attempt:
            time.sleep(DOWNLOAD_WAITS[attempt - 1])
        start = on_disk() if attempt else 0
        headers = {"User-Agent": USER_AGENT}
        if start:
            headers["Range"] = f"bytes={start}-"
        got = start
        cut = False
        try:
            with _open_engine(
                    url, headers, DOWNLOAD_TIMEOUTS[attempt]) as resp:
                status = getattr(resp, "status", 200)
                if start and status not in (200, 206):
                    # Not a whole file and not the tail: a failed
                    # try; the bytes on disk are not touched.
                    cut = True
                    last_short = (f"answer {status} to a resume request "
                                  f"(got {got} bytes)")
                elif status == 206:
                    p_start, p_end, p_total = _content_range(
                        resp.headers.get("Content-Range"))
                    length = resp.headers.get("Content-Length")
                    length_n = None
                    if length is not None:
                        try:
                            length_n = int(length)
                        except ValueError:
                            length_n = None
                    span = None
                    if p_start is not None and p_end is not None:
                        span = p_end - p_start + 1
                    problem = None
                    if p_start != start:
                        problem = (f"a part began at byte {p_start}; "
                                   f"byte {start} was asked for")
                    elif p_total is not None and expected is not None \
                            and p_total != expected:
                        problem = ("the file changed size during the "
                                   "download")
                    elif length_n is not None and span is not None \
                            and length_n != span:
                        problem = ("a part's stated length does not "
                                   "match its stated range")
                    if problem is not None:
                        # Never append: clear the partial and let
                        # the next try start the file over.
                        dest.write_bytes(b"")
                        expected = None
                        got = 0
                        cut = True
                        last_short = f"{problem} (partial cleared; will start over)"
                    else:
                        if p_total is not None:
                            expected = p_total
                        with open(dest, "ab") as out:
                            while True:
                                chunk = resp.read(1024 * 1024)
                                if not chunk:
                                    break
                                out.write(chunk)
                                got += len(chunk)
                        if span is not None and got - start > span:
                            dest.write_bytes(b"")
                            expected = None
                            cut = True
                            last_short = ("a part carried more bytes than "
                                          "its stated range (partial "
                                          "cleared; will start over)")
                            got = 0
                        elif span is not None and got - start < span:
                            # The part delivered fewer bytes than
                            # its own stated range and ended
                            # cleanly. The bytes stay (they are in
                            # order) and the next try resumes from
                            # them, but the try counts as a cut: a
                            # short part is never a complete file,
                            # even when no total was ever stated.
                            cut = True
                            last_short = (f"a part delivered "
                                          f"{got - start} of its stated "
                                          f"{span} bytes (got {got} bytes)")
                        elif expected is None:
                            # The part was delivered in full, but
                            # no answer has ever stated the file's
                            # size, and a part's own end is not
                            # proof of it: a server may answer an
                            # open-ended ask with a bounded piece
                            # (the range standard says the client
                            # must check whether more is needed).
                            # The bytes stay and the next try
                            # resumes from them; completeness is
                            # proven only by a stated total being
                            # reached, a whole-file 200 answer, or
                            # a 416 whose stated total equals the
                            # bytes on disk.
                            cut = True
                            last_short = (f"a part was delivered in "
                                          f"full, but no answer has "
                                          f"stated the file's size "
                                          f"(got {got} bytes)")
                else:
                    # A whole-file answer: written from the start and
                    # judged on its own stated length.
                    length = resp.headers.get("Content-Length")
                    if length is not None:
                        try:
                            expected = int(length)
                        except ValueError:
                            pass  # keep any length learned on an earlier try
                    got = 0
                    with open(dest, "wb") as out:
                        while True:
                            chunk = resp.read(1024 * 1024)
                            if not chunk:
                                break
                            out.write(chunk)
                            got += len(chunk)
        except urllib.error.HTTPError as e:
            if start and e.code == 416:
                _, _, stated_total = _content_range(
                    e.headers.get("Content-Range") if e.headers else None)
                have = on_disk()
                if have > 0 and (stated_total == have or expected == have):
                    # The bytes on disk are the whole file: the
                    # range was refused because nothing is missing.
                    return dest
                # Not proven complete — the file changed under the
                # download. Clear the partial; the next try starts
                # the file over.
                dest.write_bytes(b"")
                expected = None
                cut = True
                got = 0
                last_short = f"{e} (partial cleared; will start over)"
            elif not (e.code in (408, 429) or 500 <= e.code <= 599):
                raise
            else:
                cut = True
                got = on_disk()
                last_short = f"{e} (got {got} bytes)"
        except (http.client.IncompleteRead, ConnectionError,
                TimeoutError) as e:
            # Cut mid-transfer: the bytes on disk stay; the next try
            # resumes from them — a cut transfer is never a complete
            # file, and it is never started over either.
            cut = True
            got = on_disk()
            last_short = f"{e} (got {got} bytes)"
        except urllib.error.URLError as e:
            if _unfixable_transport(e):
                raise
            cut = True
            got = on_disk()
            last_short = f"{e} (got {got} bytes)"
        except OSError as e:
            # The engine road raises its transport failures bare,
            # with no URLError wrap: the unfixable kinds (the name
            # does not resolve, the secure connection cannot be
            # made) raise at once, as on the old road; the rest join
            # the ladder with the bytes on disk kept.
            if isinstance(e, (socket.gaierror, ssl.SSLError)):
                raise
            cut = True
            got = on_disk()
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
