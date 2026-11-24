# Day 51 Research A — Prescott, AZ (dental)
Researched: 2026-11-23 (Arizona time) via browser.search / browser.open only. No phone calls, no live-browser browse.
Sources key: [META] = Meta place record returned by search; [OFFICIAL] = business's own website (fetched); [WEBMD], [REALTY], etc. as named.

---

## 1) Mile High Family Dentistry — Prescott — ⚠️ THIN / DIRECTORY-ONLY — HOLD recommended for phone check

- **Confirmed name:** Mile High Family Dentistry — matches inventory exactly. [META]
- **Address:** 715 W Hillside Ave, Prescott, AZ — **ZIP not stated in any source found** (do not assume; nearby 701 W Hillside Ave is 86301 per WebMD, but that is a different practice — Dr. Peter J. Bower — and was NOT used to fill this field). [META; WEBMD for the neighbour]
- **Phone:** (928) 445-2161 (+19284452161) — **directory-only, single source** [META]. No second source corroborates it.
- **Hours:** **Not found / not confirmed** in any source searched. No hours listed on the place record; no official site found to check.
- **Website:** **None found.** Multiple targeted searches ("Mile High Family Dentistry" Prescott + hours/phone/website; exact address + phone) returned no official website for this practice. Similar-name results are unrelated out-of-state businesses and must NOT be used: Mile High Dental Anesthesia (milehighda.com, Colorado), Mile High Dentistry (BBB, Aurora, CO), Mile High Smiles (Lakewood, CO), Comfort Dental Mile High (Denver, CO).
- **Website loads (200)?** N/A — no URL identified.
- **Services / doctors:** Category only: Dental Clinic / General Dentist / Dentist & Dental Office [META]. No named dentist, no service list found anywhere.
- **Status flags:** Operating Status: **Active** [META]. No closed flag found. No successor found.
- **Duplicate flags:** None found under this exact name in Prescott.
- **Conflicts / cautions:**
  - Single-source verification only — name, address, phone, and active status all rest on ONE Meta place record (place_id 606419938522229). No official site, no WebMD/Yelp/BBB listing, no second directory corroboration found after 3 separate searches.
  - Address is 2 doors from a different, well-documented practice at 701 W Hillside Ave (Dr. Peter Bower) — risk of place-record confusion cannot be ruled out.
  - **Recommendation: HOLD for phone check before publishing.** Publishable fields if the parent proceeds anyway: name, 715 W Hillside Ave, Prescott, AZ (no ZIP), phone (928) 445-2161 with "hours not confirmed" and website omitted.

## 2) Stillwater Dental — Prescott — ⚠️ CONFLICTED ADDRESS — HOLD recommended for phone check

- **Confirmed name:** Stillwater Dental — matches inventory. [META]
- **Address:** 3773 Crossings Dr Ste C, Prescott, AZ 86305 — ZIP 86305 corroborated by WebMD/Healthgrades listings for the same suite (see conflict below). [META; WEBMD]
- **Phone:** (928) 717-2400 (+19287172400) — **directory-only, single source** [META]. No second source corroborates it; the practice's web page (below) lists no phone.
- **Hours:** **Not found / not confirmed.** No hours on the place record, none on the web page found.
- **Website:** The only site found naming this practice is https://www.hellolocalwebsites.com/websites/stillwater-dental — "Stillwater Dental | Dentistry with a smile." It **loads (HTTP 200, verified 2026-11-23 via curl and browser.open)** BUT: it is hosted on a web-designer's domain (page meta: "Website built by Hello Local Websites", robots "noindex, follow"), reads as a portfolio/demo build, and contains **no address, no phone, and no hours** — it does not corroborate any directory field. Treat as **no confirmed official website**.
- **Services / doctors:** Site copy is generic only: family and cosmetic dentistry, checkups / "everyday care", first-visit exams and personal treatment plans. **No named dentist found in any source.**
- **Status flags:** Operating Status: **Active** [META]. No closed flag.
- **Conflicts — significant:**
  1. **Same suite, different business:** WebMD and Healthgrades list **Arizona Grand Medical Center PLLC** at the identical address, 3773 Crossings Dr Ste C, Prescott, AZ 86305 (providers Claudia Angulo, NP — Tel (928) 277-8316 per WebMD; Dr. Nirav Mehta — (602) 698-7325 per Healthgrades). Either the suite changed tenants, is shared, or one listing is stale.
  2. **Building sale:** A Realty.com listing for 3773 Crossings Dr (closed sale, $550,000) describes a "fully improved office/medical building" with co-tenants "including: Stillwater Dental, American Family Insurance & Wait Stuff" — confirms Stillwater Dental was a tenant at this address at listing time, but the building has since sold, so current tenancy is not proven by it. [REALTY]
  3. **Second place record:** A second "Stillwater Dental" Meta place exists at 3253 N Windsong Dr, Prescott Valley, AZ (place_id 2673952942962913, Active, no phone) — but that address is documented elsewhere as **Highland Dental** (Prescott Valley) [dental.page]. This looks like stale/confused place data, not a verified second location. Do NOT list it as a second location.
  4. **Name-similarity caution:** Not to be confused with Distinctive Dental Care on Stillwater **Drive** (entry 3 below) — different business, different street.
- **Recommendation: HOLD for phone check.** The (928) 717-2400 number and current tenancy at Ste C both need voice confirmation before publishing; the Arizona Grand Medical Center overlap is unresolved.

## 3) Distinctive Dental Care — Prescott — ✅ FULLY VERIFIED (official site)

- **Confirmed name:** Distinctive Dental Care. [OFFICIAL]
- **Address:** 3140 Stillwater Drive, Suite B, Prescott, AZ 86305 — exact match to inventory, stated repeatedly on the official site. [OFFICIAL]
- **Phone:** **(928) 445-3181** (shown as 928.445.3181) — official site, on every page; corroborated by Intake.Dental (Aaron Wulff listing, same number) and MapQuest. [OFFICIAL]
  - ⚠️ Conflict (minor): the Meta place record for this business lists a different phone, +1 928-275-8561. The official-site number (928) 445-3181 is multiply corroborated — **use 928-445-3181** and disregard the place-record number.
- **Hours (official site, confirmed — not directory-only):** Mon 8am–5pm, Tue 8am–5pm, Wed 8am–5pm, Thu 8am–5pm, Fri 8am–3pm, Sat Closed, Sun Closed. [OFFICIAL — homepage and services page, identical]
- **Website:** https://wulffdmd.com/ — **loads, HTTP 200** (verified 2026-11-23 via curl -L and browser.open; homepage and /services/ both fetched successfully).
- **Doctors:** Father-and-son team **Dr. Paul Wulff and Dr. Aaron Wulff** — "For over 30 years, the father-and-son team of Dr. Paul and Dr. Aaron Wulff has proudly served … Prescott, Prescott Valley, Chino Valley, and Dewey." [OFFICIAL] Matches the inventory note "Drs. Paul & Aaron Wulff" exactly. (WebMD also lists a Dr. Kimberly W. Fee, DDS, at this same address — she does not appear on the official homepage fetched today; note only, do not add her to the entry without further checking.)
- **Services (official site):** Cosmetic dentistry (teeth whitening, bonding, veneers), general dentistry (oral exams, cleanings, restorative work), complete dentistry, surgical dentistry (root canal, dental implants, tooth extraction), emergency dental treatment, dentures (partial and complete), tooth-colored fillings/restorations, crowns — including same-day CEREC crowns. Accepts most dental PPO plans (site names Cigna PPO, Aetna, Delta Dental); accepting new patients. In-office comforts noted on site: paraffin wax, neck pillows, refreshment bar. [OFFICIAL]
- **Status flags:** Active — official site live and current (crawled <1 hour before this research; appointment scheduling via NexHealth active). No closed/successor flags.
- **Duplicate flags:** None. Note only the street-name similarity to "Stillwater Dental" (entry 2) — different business.
- **Conflicts:** Only the Meta place-record phone noted above. Name, address, hours, doctors all consistent across official site, WebMD, Intake.Dental, and MapQuest.
- **Recommendation: Publish-ready** with phone (928) 445-3181, hours as above, website https://wulffdmd.com/.

---

## Summary table

| Business | Address | Phone | Hours | Website | Verdict |
|---|---|---|---|---|---|
| Mile High Family Dentistry | 715 W Hillside Ave, Prescott, AZ (ZIP unconfirmed) | (928) 445-2161 — directory-only, 1 source | Not confirmed | None found | HOLD — phone check |
| Stillwater Dental | 3773 Crossings Dr Ste C, Prescott, AZ 86305 | (928) 717-2400 — directory-only, 1 source | Not confirmed | Designer demo page only (200, no contact data) — no confirmed official site | HOLD — phone check; suite also listed for Arizona Grand Medical Center |
| Distinctive Dental Care | 3140 Stillwater Dr Ste B, Prescott, AZ 86305 | (928) 445-3181 — official | Mon–Thu 8–5, Fri 8–3, Sat/Sun closed — official | https://wulffdmd.com/ — 200 | Publish-ready |
