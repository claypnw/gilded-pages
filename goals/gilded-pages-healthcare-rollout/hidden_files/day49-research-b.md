# Day 49 — Research B: Two Show Low Laboratories
Researched: 2026-11-21 (America/Phoenix date in task header; page fetches timestamped 2026-11-21 09:30 UTC)
Method: browser.search + browser.open on official sites and reliable directories only. No data invented. Official-site values are flagged PREFERRED. All conflicts are listed, not hidden.

Town: Show Low, AZ — Category for both: labs (medical / clinical laboratory, Patient Service Center)

---

## 1. Labcorp — Show Low

### Verdict: PUBLISHABLE — no material conflict

### Exact name
- **Labcorp** — location identifier on official site: "Labcorp #20361 Show Low, AZ"
- Source (official, PREFERRED): Labcorp location page, https://locations.labcorp.com/az/show-low/20361/

### Address
- **5171 S Cub Lake Rd, Ste 250, Show Low, AZ 85901**
- Official site (PREFERRED): "5171 S Cub Lake Rd , Ste 250 Show Low, AZ 85901" — browser.open, 2026-11-21 09:30 UTC.
- Corroborated: Mito Health listing (crawled 1 day / 8 hours ago) — same address, suite, ZIP.
- Matches the inventory address given in the task exactly. No conflict.
- Note: the same street address, different suites, also houses the Show Low VA Clinic (Suite C380, va.gov) — a different business; do not confuse them.

### Phone
- **(928) 532-0431** — official site (PREFERRED): "+1 928-532-0431", fax +1 928-532-0445.
- Corroborated: Mito Health — 928-532-0431. No conflicting phone found anywhere.
- Matches the inventory phone given in the task.

### Hours
- **Mon–Fri 7:00 AM – 3:00 PM; Sat–Sun Closed** (regular hours)
- Official site (PREFERRED): General Hours list shows Mon 2026-11-16 through Fri 2026-11-20 at 7:00 AM–3:00 PM, Sat/Sun closed; summary line "Mon: 07:00-15:00, Tue: 07:00-15:00, Wed: 07:00-15:00, Thu: 07:00-15:00, Fri: 07:00-15:00, Sat: Closed, Sun: Closed".
- Corroborated: Mito Health — "Mon to Fri, 7:00 AM-3:00 PM, Sat to Sun, Closed".
- Minor note (not a regular-hours conflict): date-specific closures vary — the live page fetched 2026-11-21 showed Thu 2026-11-19 as Closed and Thanksgiving week Thu 2026-11-26 / Fri 2026-11-27 Closed, while a search crawl from 1 day earlier showed Thu 2026-11-19 open. Publish only the regular Mon–Fri hours, not date-specific closures.

### Website — verified loads
- **https://locations.labcorp.com/az/show-low/20361/**
- Status: LOADED successfully via browser.open on 2026-11-21 (crawled <1 minute before reading) — full location content returned: address, phone, hours, services, appointment link. This is the location-specific official page; use it as the published website.

### Services (official site list, verbatim categories)
Routine lab work; Pediatric collection; Hair collection; Saliva alcohol testing; H. pylori breath test; Finger Printing; Employee Wellness with Body Measurement.
Official page headline also names: "Laboratory Testing, Drug Testing, and Routine Labwork."
Walk-ins welcome; appointments encouraged (per official FAQ on the same page).
- Secondary-only note, NOT official and NOT published: eNational Testing listed drug-screen sub-hours Mon–Fri 9:00 AM–12:00 PM and 1:00–2:00 PM. Not confirmed on Labcorp's own page — omit from the entry.

### Category
labs — Primary category in directory data: "Medical Lab".

### Open / closed evidence — OPEN
- Official location page is live with current November 2026 hours and an active appointment link.
- Directory data snippet for the same official URL: "Operating Status: Active".
- No closure notice found in any source searched.

### Conflicts
None material. Only the date-specific closure wobble noted under Hours, and the unconfirmed drug-screen sub-hours from a third party (omitted).

### Publishable form
```
Name:     Labcorp
Category: labs
Address:  5171 S Cub Lake Rd, Ste 250, Show Low, AZ 85901
Phone:    (928) 532-0431
Hours:    Mon–Fri 7:00 AM – 3:00 PM; Sat–Sun Closed
Website:  https://locations.labcorp.com/az/show-low/20361/
Services: Routine lab work, pediatric collection, hair collection, saliva alcohol testing, H. pylori breath test, fingerprinting, employee wellness with body measurement; laboratory testing and drug testing. Walk-ins welcome, appointments encouraged.
Note:     Location #20361 on official site.
```

---

## 2. Sonora Quest Laboratories – Show Low

### Verdict: PUBLISHABLE with preferred phone (928) 532-1745 — conflict settled below, alternate number documented. A phone check would remove the last doubt, but the live official location system is consistent and current; do NOT publish 1752 as the main number.

### Exact name
- **Sonora Quest Laboratories** — live location system styles it "Sonora Quest Laboratories - Show Low-24th St & Show Low Lake Rd"
- Sources: Quest Diagnostics official location detail (PREFERRED for location data, see Phone); Sonora Quest's own site, https://www.sonoraquest.com/patients/appointments/

### Address
- **2450 E Show Low Lake Rd, Ste 3B, Show Low, AZ 85901**
- Official location detail (PREFERRED): "2450 E SHOW LOW LAKE RD, STE 3B, SHOW LOW, AZ, 85901" — Quest Diagnostics detail page, browser.open 2026-11-21 09:30 UTC. Landmark given there: "24TH ST AND SHOW LOW LAKE RD". Coordinates on that page: 34.202442, -110.015059.
- Corroborated: Mito Health (crawled 1 day ago) — same address/suite/ZIP. Sonora Quest Client Gram, July 15, 2026 (official, sonoraquest.com PDF) — "Show Low: 2450 Show Low Lake Rd. Suite 3B" (omits the "E" directional; same building/road).
- Matches the inventory address given in the task. No conflict except the minor "E" omission in the Client Gram, noted above.

### Phone — CONFLICT, SETTLED
Conflict as assigned: (928) 532-1752 vs (928) 532-1745.

**Publish (928) 532-1745 — PREFERRED, live official location page.**
Evidence for 1745:
- Quest Diagnostics official location detail page for this exact Sonora Quest location — browser.open 2026-11-21 09:30 UTC, crawled <1 minute earlier: "2450 E SHOW LOW LAKE RD, STE 3B, SHOW LOW, AZ, 85901, 928-532-1745, 928-227-3703" and repeated "Phone, 928-532-1745, Fax, 928-227-3703".
  URL: https://www.questdiagnostics.com/locations/detail.html/ZPT/85901/75/1
- Quest Diagnostics location search — same number, crawls 2 hours ago, 1 day ago, 3 hours ago (multiple independent crawls, all 1745, none 1752).
  URL: https://www.questdiagnostics.com/locations/search.html/87829/75/2
- Mito Health (feeds Quest booking data), crawled 1 day ago: 928-532-1745.
- Sonora Quest directs patients to book through this same Quest system: its appointments page (sonoraquest.com/patients/appointments/, loaded 2026-11-21) is the booking entry, and its printed PSC lists state "Schedule appointments … at SonoraQuest.com" / "for our most current listings visit SonoraQuest.com" — i.e. Sonora Quest itself defers to the live online listing, which today says 1745.

Evidence for 1752 (documented, NOT preferred):
- Sonora Quest's own printed Patient Service Centers lists, February 2026, March 2026, and May 2026 editions (PDFs hosted at files.constantcontact.com, footer "for our most current listings visit SonoraQuest.com"): "Show Low — 2450 Show Low Lake Rd., #3B, Show Low, AZ 85901 — 928-532-1752, Fax: 928-227-3703". Opened and read directly for the March 2026 edition on 2026-11-21.
- Google-Places-derived data shown under a sonoraquest.com search snippet: "Phone: +19285321752", "Operating Status: Active" — aggregator data, no crawl date.
- Honeywell Biometrics collection list (undated/older, with clearly outdated split hours for Show Low): 928-532-1752.
- EasySTD and similar aggregators: 928‑532‑1752 (crawls 4–96 days ago, hours inconsistent between their own pages).

Why 1745 wins:
1. Recency: the 1745 sources are live pages crawled hours ago (Nov 2026); every 1752 source is a dated print list from Feb–May 2026 or an undated aggregator scrape.
2. Authority for a location listing: the live location detail page is the system of record patients book through today, and Sonora Quest's own print lists explicitly defer to the online listing as "most current".
3. Consistency: 1745 is identical across the detail page, the search page, and the booking-fed Mito listing, with the same fax (928-227-3703) as the 1752 lists — same office, updated main number, not a different business.
4. Supporting pattern: other PSC numbers also differ between the 2026 print lists and the live Quest system (e.g. Payson: print 928-474-6136 vs live Quest 928-474-3451), consistent with the live system carrying newer numbers than the print lists.
- Residual uncertainty, stated plainly: no source proves 1752 is disconnected; it may still ring as a secondary/former line. If the directory ever does a phone-check round, this is the one number to test first. That residual doubt does not justify holding the entry — address, hours, name, and existence are all firmly confirmed, and 1745 rests on the current official location page.

### Hours
- **Mon–Fri 7:00 AM – 4:00 PM; Sat–Sun Closed** (PREFERRED)
- Official location detail (Quest, fetched 2026-11-21): Mon–Fri 7:00 am–4:00 pm, Sat Closed, Sun Closed — no midday closure shown.
- Corroborated: Sonora Quest Client Gram, July 15, 2026 (official): "Show Low … Monday – Friday, 7:00 a.m. – 4:00 p.m. Effective 8/1/2026". Mito Health (1 day ago): same.
- Conflict (documented): Sonora Quest's Feb/Mar/May 2026 printed PSC lists add "Closed 12:00–1:00" for lunch. The live official page and the Aug 2026 Client Gram update do not show a lunch closure — publish 7:00–4:00 without a lunch break, and note the print-list lunch closure as superseded/unconfirmed.
- Stale source rejected: Solv Health pages (data ~1,193 days old) show Mon–Fri 7:00 AM–12:00 PM only — outdated, do not use.

### Website — verified loads
- **https://www.sonoraquest.com/patients/appointments/**
- Status: LOADED via browser.open on 2026-11-21 — page title returned: "Schedule an Appointment | Sonora Quest Laboratories - Sonora Quest Laboratories". Text extraction was minimal (2 lines; the page is an appointment-type picker), but the page responded and is the website URL attached to this location in directory data.
- Location-specific official page (also loads, full content): https://www.questdiagnostics.com/locations/detail.html/ZPT/85901/75/1 — fetched in full on 2026-11-21. Recommend publishing the Sonora Quest URL above as the entry website (brand site for this business) and keeping the Quest detail URL in the research record as the source for address/phone/hours.

### Services
No location-specific service list is published on the official location detail page. Confirmed, sourced services only:
- Clinical / diagnostic laboratory testing through a Patient Service Center (specimen collection) — Quest detail: "We offer broad access to clinical testing services through our national network of laboratories … approximately 2,000 patient locations."
- Blood tests / lab testing — Mito Health and Solv Health describe this location for blood testing (directory descriptions, not official).
- Business's own description in directory data: "Visit our medical lab located near the Summit Healthcare Regional Medical Center here in Show Low."
Do NOT add specific tests (drug screens, biometrics, etc.) to this entry — none were confirmed for this location on an official page. (A Honeywell document confirms Sonora Quest provides Biometrics (BFW) collection services in Arizona generally, but it is not location-specific proof for Show Low's current offering.)

### Category
labs — Primary category in directory data: "Medical Lab".

### Open / closed evidence — OPEN
- Quest live location detail and search pages are current (crawls hours old, Nov 2026) with full weekly hours.
- Directory data: "Operating Status: Active", "Open Now: Yes".
- Sonora Quest Client Gram, July 15, 2026 (official): announces Show Low hours effective 8/1/2026 — an operating location being updated, not closed.
- No closure notice found in any source searched.

### Conflicts — summary
1. Phone: 1745 (live official, Nov 2026) vs 1752 (Sonora Quest print lists Feb–May 2026 + aggregators) — settled for 1745, see above.
2. Lunch closure: print lists "Closed 12:00–1:00" vs live page / Client Gram showing continuous 7:00–4:00 — publish continuous, note the print version.
3. Hours (stale): Solv Health 7:00 AM–12:00 PM — rejected as ~3-year-old data.
4. Address form: "2450 E Show Low Lake Rd" (live, PREFERRED) vs "2450 Show Low Lake Rd" without "E" in the Client Gram — same location, use the "E" form.
5. Fax is consistent everywhere it appears: 928-227-3703 (not part of the published entry form, recorded here for verification value).

### Publishable form
```
Name:     Sonora Quest Laboratories
Category: labs
Address:  2450 E Show Low Lake Rd, Ste 3B, Show Low, AZ 85901
Phone:    (928) 532-1745
Hours:    Mon–Fri 7:00 AM – 4:00 PM; Sat–Sun Closed
Website:  https://www.sonoraquest.com/patients/appointments/
Services: Clinical laboratory testing / patient service center specimen collection; medical lab near Summit Healthcare Regional Medical Center.
Note:     Phone settled from the live official location page (Quest Diagnostics detail for this Sonora Quest location, fetched 2026-11-21). Alternate number (928) 532-1752 appears in Sonora Quest's Feb–May 2026 printed PSC lists and aggregators — do not publish as the main number; flag for a future phone check.
```

---

## Sources used (all accessed 2026-11-21)
Official (PREFERRED):
- Labcorp Show Low location — https://locations.labcorp.com/az/show-low/20361/ (browser.open, full page)
- Quest Diagnostics — Sonora Quest Show Low detail — https://www.questdiagnostics.com/locations/detail.html/ZPT/85901/75/1 (browser.open, full page)
- Quest Diagnostics location search — https://www.questdiagnostics.com/locations/search.html/87829/75/2 (search crawls, 2 hours–1 day old)
- Sonora Quest appointments — https://www.sonoraquest.com/patients/appointments/ (browser.open, loads; minimal text)
- Sonora Quest Client Gram Vol. 40, July 15, 2026 — https://www.sonoraquest.com/media/dialyh10/client-gram_vol_40_71526.pdf (browser.open, full text)
- Sonora Quest Patient Service Centers lists, Feb / Mar / May 2026 editions — files.constantcontact.com PDFs (March 2026 edition opened in full; Feb and May editions read in search extracts; all list Show Low as 928-532-1752, 7:00–4:00 M-F, closed 12:00–1:00)

Reliable directories / corroboration:
- Mito Health — Labcorp Show Low and Sonora Quest Show Low location pages (crawled 1 day / 8 hours ago)
- eNational Testing — Labcorp Show Low address/hours corroboration (drug-screen sub-hours NOT used)
- Solv Health — Sonora Quest Show Low (used only as evidence of staleness; its 7 AM–12 PM hours rejected)
- EasySTD aggregator pages — 1752 sightings, documented as aggregator evidence only
- Honeywell Biometrics document — older Sonora Quest collection list, 1752 sighting, documented only
- VA.gov Show Low VA Clinic page — used only to distinguish the VA Clinic (Suite C380) from Labcorp (Ste 250) at the same street address
