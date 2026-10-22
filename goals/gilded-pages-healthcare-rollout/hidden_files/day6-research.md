# Day 6 research — Gilded Pages healthcare rollout (2026-10-10)

All 7 Payson businesses researched by three parallel research subagents via browser.search / browser.open text fetches and curl HTTP checks. No details invented; caveats noted per standing rules.

---

## 1. Peak Health Medical Group
- **Status:** Open/active. Google listing Active; official site live and current; NPI registry (PEAK HEALTH MEDICAL GROUP LLC) current at the address.
- **Address:** 127 E Main St Ste A, Payson, AZ 85541 (ZIP+4 85541-5646) — confirmed by NPI registry + official site.
- **Phone:** (928) 492-9222 — confirmed by official site + NPI registry.
- **Hours:** Mon–Fri 8 AM–5 PM; Sat/Sun closed (source: peakhealthmedicalgroup.com "Our Office" block; Google agrees).
- **Website:** https://peakhealthmedicalgroup.com/ — confirmed live-loading (browser.open fetch succeeded AND curl -sL → HTTP 200).
- **Services per site:** primary care / family medicine (nurse practitioners); dermatology explicitly referred to the sister practice.
- **Caveat:** "Peak Health Medical Group" appears to be a rebrand; older NPI records show a PEAK HEALTH MEDICAL GROUP INC (last updated ~5+ years ago), now superseded by PEAK HEALTH MEDICAL GROUP LLC. peakheart.com is unrelated (a Phoenix cardiology group) — do not confuse.

## 2. Arizona Institute of Dermatology / Peak Dermatology
- **Status:** Open/active. NPI registry (ARIZONA INSTITUTE OF DERMATOLOGY PAYSON LLC, dba Peak Dermatology) active, certified 2026; CLIA certificate valid through May 11, 2027; ~105 Google reviews at 4.9. No closure signals.
- **Address:** 127 E Main St Ste A, Payson, AZ 85541-5646 — confirmed by NPI registry + official site.
- **Phone:** (928) 951-0395 — confirmed by NPI registry + official site (also 833-739-3376 toll-free "1-833-REX-DERM").
- **Hours:** Mon–Fri 8 AM–5 PM; Sat/Sun closed (source: peakdermcare.com official Payson office listing; Google and healthcare4ppl agree).
- **Website:** https://www.peakdermcare.com/ — confirmed live-loading (curl -sL → HTTP 200, www→non-www redirect followed).
- **Provider:** Dr. Christopher Ugorji Rex, MD — board-certified dermatologist, Mohs surgeon (per NPI authorized official).
- **Relationship with Peak Health (same suite):** Same practice family, affiliated — not two independent tenants. Both are Dr. Rex's enterprises operating out of Suite A. The Peak Health homepage carries a "looking for dermatology care in Payson? visit the link below" callout pointing to the dermatology arm and uses the info-az@peakdermcare.com email (the derm brand's domain). NPI: "ARIZONA INSTITUTE OF DERMATOLOGY PAYSON LLC" dba "Peak Dermatology"; Peak Health Medical Group LLC is a separate legal group but lists the same providers (e.g., Cami Lynn Alexander appears under both orgs per healthcare4ppl), and medicarelist.com lists Dr. Rex as a member of Peak Health Medical Group LLC. **Directory-safe framing:** two separate entries is fine — distinct phones, distinct services — but cross-reference them so readers aren't confused by the identical address. Directory copy: "Peak Health Medical Group (primary/family care) and its affiliated Peak Dermatology practice (Dr. Christopher Rex, board-certified dermatologist/Mohs surgeon) share Suite A at 127 E Main St."

## 3. North Country HealthCare – Payson  ⚠️ REBRAND
- **Status:** Open/active — **but rebranded.** As of the April 1, 2026 transition, North Country HealthCare's northern-Arizona operations (including Payson) were taken over by El Rio Health and now operate as **Elk Ridge Community Health** (a division of El Rio Health). The old domain northcountryhealthcare.org now serves Elk Ridge branding. The Payson clinic remains open at the same address under the new name. **Directory listing should read "Elk Ridge Community Health (formerly North Country HealthCare)."**
- **Address:** 126 E Main St, Ste B, Payson, AZ 85541 — confirmed (https://elkridge.org/locations/payson/, fetched live via curl → HTTP 200).
- **Phone:** (928) 468-8610 — same official page. Fax (928) 468-8605.
- **Hours:** Mon–Tue 7am–5pm; Wed 8am–6pm; Thu 9am–6pm — from the official Elk Ridge Payson location page. **Friday not listed** (likely closed Fridays; phone-check suggested). No Sat/Sun listing.
- **Website:** https://elkridge.org/locations/payson/ — confirmed live-loading (curl -sL → HTTP 200). Use this location page, not the old brand URL.
- **Services at Payson:** Adult Medicine, Behavioral Health, Dental, Family Medicine, Pediatrics. FQHC heritage confirmed by NPI taxonomy (261QF0400X, Federally Qualified Health Center) and multiple directory sources.

## 4. Integrated Medical Services (IMS)
- **Status:** Open/active. Multiple current listings (Google place data, BestProsInTown, Loc8NearMe, Birdeye) show Active, not closed. Recent patient reviews dated August 2026.
- **Address:** 111 W Cedar Ln, Ste A, Payson, AZ 85541 — confirmed (Google place data, Zocdoc, BestProsInTown). Matches inventory.
- **Phone:** (928) 472-4675 — **confirmed as IMS's number** by four independent sources: Google place data (phone field), BestProsInTown, Loc8NearMe, and IMS's own newspaper ad in the Payson Roundup ("IMS Primary Care, 111 W Cedar Lane, Payson, 928-472-4675"). Matches inventory.
- **Hours:** Mon–Fri 7:00 AM–5:00 PM; Sat/Sun closed (Google place data, America/Phoenix; corroborated by BestProsInTown and Loc8NearMe).
- **Website:** https://www.imsaz.com/ — confirmed live-loading (curl -sL -o /dev/null -w "%{http_code}" → 200).
- **IMS/Alma phone question RESOLVED:** The inventory appears to have assigned IMS's number to Alma Medical Clinic in error. **Alma Medical Clinic is a separate, unrelated business** — 1106 N Beeline Hwy, Payson, AZ 85541, phone **(928) 474-8901** (WebMD, Vitals, NPI registry record 1750449427, namesandnumbers.com). Google lists Alma as "Possibly Temporarily Closed" — flag before including Alma in the directory. No IMS/Alma relationship found anywhere. (Side note: the same (928) 472-4675 also appears on the NPI registry for "Payson Healthcare Management Inc" at 126 E Main St Ste B — likely an IMS-related management entity, not Alma.)

## 5. Eagle Springs Family Medicine
- **Status:** Open/active. NPI registry record (1164482337, established 2006, active Medicare listing on medicarelist.com with current address/phone). No closure signals.
- **Address:** 903 E Highway 260, Suite 4, Payson, AZ 85541 — confirmed (NPPES/NPI registry, multiple directory mirrors). Matches inventory.
- **Phone:** (928) 468-7700 — confirmed (NPI registry; fax (928) 468-7703). Matches inventory.
- **Hours:** Not confirmed — no reliable source (official site, Google listing, or directory) published office hours for this practice.
- **Website:** None found / omitted. Searches surfaced only unrelated out-of-state practices named "Eagle Family Medicine" (PA, NC, ID). No own website identified — per standing rule the website field is omitted entirely.

## 6. Banner Physical Therapy – Payson Medical Center
- **Status:** Open/active. Current job postings (Monster, ~8 days old) hiring for this exact location; 186 recent patient reviews. No closure indicators.
- **Address:** 126 E Main St Ste C, Payson, AZ 85541 — confirmed (official Banner Health location page).
- **Phone:** (928) 468-8907 — same official page. Fax (928) 468-8912 (mylocalservices.com directory, secondary source).
- **Hours:** Mon–Fri 8:00am–5:00pm; Sat–Sun closed (official Banner Health location page).
- **Website:** https://www.bannerhealth.com/locations/payson/banner-physical-therapy-main — confirmed live-loading via browser.open (full page text retrieved, incl. address, phone, hours). Note: curl to this URL failed (bot-blocked, HTTP 000); alternate banner-pt.com location URL returned 403 via curl — omitted per standing rule.

## 7. Payson Physical Therapy
- **Status:** Open/active. Google place data Active; 4.9 stars on 14 reviews; NPI registry active (1194943423, dba "Payson Physical Therapy" under Nossek Rehab LLC).
- **Address:** 405 W Main St, **Suite D**, Payson, AZ 85541 — confirmed (NPI registry, namesandnumbers.com). Inventory address correct; NPI adds Suite D — use "405 W Main St Ste D".
- **Phone:** (928) 474-0429 — confirmed (Google place data, NPI registry). Matches inventory. Fax: (928) 474-0199.
- **Hours:** Mon–Fri 8:00 AM–4:00 PM (Google place data, America/Phoenix).
- **Website:** http://www.paysonphysicaltherapy.com/ — confirmed live-loading (curl -sL -o /dev/null -w "%{http_code}" → 200).

---

## Flags and corrections for the directory build
1. **North Country HealthCare → Elk Ridge Community Health.** List under the NEW brand: "Elk Ridge Community Health (formerly North Country HealthCare)".
2. **Alma Medical Clinic is NOT (928) 472-4675** — that is IMS's number. Alma's real number is (928) 474-8901, 1106 N Beeline Hwy; Google says "Possibly Temporarily Closed" — needs a decision before listing.
3. **Peak Health / Peak Dermatology are affiliated** (same suite, same owner). Two entries OK; cross-reference them.
4. **Payson Physical Therapy** — add Suite D to the address.
5. **Eagle Springs Family Medicine** — hours unconfirmed; no website to include.
6. **New categories needed:** Vision not needed today. Physical therapy category will be needed for Banner PT and Payson PT (check whether it exists; add "Physical Therapy" to BIG_CATEGORIES if not).

## Alma follow-up — 2026-10-10 20:25 UTC (proactive research)
- Re-checked Alma Medical Clinic's status for the next batch. Phone (928) 474-8901 re-confirmed across Healthgrades, WebMD, Vitals, NPI 1750449427, Manta — unanimous.
- NEW signal vs. Google's "Possibly Temporarily Closed" flag: Birdeye's live directory profile lists regular hours (Mon–Fri 9:00 AM–6:00 PM, closed Sat/Sun) and, checked on Saturday Oct 10, shows "Opens 9:00 a.m. tomorrow" — i.e., the business behaves as normally operating; the Google flag looks stale/unverified.
- Recommendation: list Alma with the verified phone; pending Clay's decision (asked 2026-10-10) — default hold if he doesn't answer before the 2026-10-11 03:30 batch.
- **DECISION (Clay, 2026-10-10 ~3:25 PM AZ): HOLD Alma out of the directory for now.** Do NOT list Alma in the 2026-10-11 03:30 batch or any later batch until he says otherwise. Revisit only if the Google closure flag clears or he asks.
