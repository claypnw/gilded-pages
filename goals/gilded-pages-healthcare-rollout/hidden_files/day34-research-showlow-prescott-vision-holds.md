# Day 34 — Re-check of Show Low / Prescott vision holds — 2026-11-06

Method: `browser.search` and `browser.open` only. No live browser, no phone calls, nothing published.
Task holds: #146 Apria Healthcare, Show Low; #81 Summit Eye Surgeons, Prescott.
Prior context supplied in the task brief was treated as a starting hypothesis, not as evidence. Every finding below rests on a fresh search or page open in this run, with the source URL copied verbatim from the tool result.

Verdicts in one line:
- **#146 Apria Healthcare, Show Low — HELD (leaning closed, NOT decisively closed, NOT publishable).** 7th consecutive check with the same shape.
- **#81 Summit Eye Surgeons, Prescott — HELD (leaning opening-soon / not yet open, NOT publishable, NOT closed).** July 2026 tenant-improvement permit for the exact address is now confirmed from the City of Prescott's own July 2026 permit list; no opening, hours, or official listing for Prescott was found.

---

## 1. #146 — Apria Healthcare, Show Low

### Inventoried data (from task brief)
- Address: 4551 S White Mountain Rd, Show Low, AZ
- Inventoried local phone: (928) 537-7330
- National phone: (888) 492-7742
- Prior (6 straight checks): leaning closed; AZ branches listed elsewhere; no Show Low branch; address now other businesses; no source states closure.

### Fresh searches run 2026-11-06
1. `Apria Healthcare Show Low Arizona 4551 S White Mountain Rd`
2. `Apria Healthcare locations Arizona Show Low`
3. `"4551 S White Mountain Rd" Show Low businesses`
4. `"Apria Healthcare" "537-7330" OR "Show Low" closed`
5. `site apria.com locations Arizona`
6. `Apria Healthcare branch locator Arizona zip 85901 Show Low`
7. `"Apria Healthcare" Show Low NPI 85901`

### Fresh page opens
- Apria homepage: https://www.apria.com/ — crawled 2026-11-06 10:31 UTC in this run. Shows national phone (888) 492-7742 and a "Locations" link; no town list on the homepage.
- Apria Locations page: https://www.apria.com/locations — opened via the homepage Locations link in this run. The text fetch returned only site navigation / app promo, no branch list at all (the locator is interactive / script-driven and does not render as text). That is a fetch limitation, **not** proof of any branch's presence or absence. It is recorded as a gap, not as evidence.
- CareArizona Arizona State List — Medical Equipment and Disability Aid Providers: https://www.carearizona.org/list08_az_home_medical_equipment.htm — opened in this run, crawled 2026-11-06 10:31 UTC.

### What the fresh evidence shows

**a) No Show Low branch appears in any Apria place / directory result returned for Arizona.**
Every Apria result returned across the seven searches above was for a different Arizona town, repeatedly the same set:
- Peoria — 8550 / 89 N 91st Ave Bldg H, Ste 85, Peoria, AZ, phone +1 623-872-1392, Mon–Fri 8:00 AM–5:00 PM, Operating Status: Active. Source (search result, apria.com place data): http://www.apria.com/
- Gilbert — 2085 S Bluejay Dr, Gilbert, AZ, phone +1 602-313-6826, Mon–Fri 8:00 AM–5:00 PM, Active, 3.4 stars / 5 reviews. Source: http://www.apria.com/
- Bullhead City — 2580 Landon Dr Ste H, Bullhead City, AZ, phone +1 928-763-7787, split hours Mon–Fri 9:00 AM–12:00 PM and 1:00–4:00 PM, Active. Source: http://www.apria.com/
- Chandler — 2700 W Frye Rd 3rd Floor, Chandler, AZ, phone +1 888-492-7742, Operating Status: **Permanently Closed** in one search result — that closure label is for **Chandler**, not Show Low, and must not be transferred. Source: https://www.apria.com/

No search in this run returned an Apria place record for Show Low, for 4551 S White Mountain Rd, or for phone (928) 537-7330. The inventoried local phone did not surface in any fresh result.

**b) The inventoried address is now occupied by other, unrelated businesses.**
Search `"4551 S White Mountain Rd" Show Low businesses` returned, for the exact address:
- It's A Ruff Life Grooming & Spa — 4551 S White Mountain Rd, Show Low, AZ, phone +1 928-251-2178, pet groomer, Active, Tue–Sat 8:00 AM–3:00 PM. Source: http://showlowpetgrooming.com/
- Acute Head Spa — 4551 S White Mountain Rd #1, Show Low, AZ, phone +1 928-242-4786, day spa, Active, Mon–Sat 9:30 AM–6:00 PM. Source: https://acuteheadspa.com/

No Apria listing was returned for that address. This matches the prior checks' "address now other businesses" finding, with two named current occupants in this run.

**c) Historical presence in Show Low is real — which is why "never existed" would be wrong.**
Arizona Enterprise Zone Program annual reports list Apria Healthcare, Inc. in Show Low in the late 2000s, at a neighbouring White Mountain Rd address:
- FY2010 report: "Apria Healthcare, Inc. 4481 S White Mtn  Show Low 85901" (2009 data). Source: https://azmemory.azlibrary.gov/assets/displaypdf/136017
- FY2008 report: "Apria Healthcare Inc. 4481 S. White Mountain Rd., E-1  Show Low 85901  Navajo" (2007 data). Source: https://lincolninst.edu/app/uploads/legacy-files/gwipp/upload/sources/Arizona/2008/AZ_sourcedoc_FY2008_Enteprise%20Zone%20Program%20Annual%20Report.pdf

Note the historical address is 4481, not the inventoried 4551. That difference is recorded, not smoothed over: the inventory address may be a later move, a neighbouring suite in the same centre, or an inventory error. Web evidence in this run does not settle which.

**d) The one list that still names a Show Low Apria is undated / stale in character.**
CareArizona's state list, opened in this run, contains at line 486:
> "Show Low, AZ | Apria Healthcare Inc, Navajo County | Click to request assistance"

The same page also lists "Peoria, AZ | Apria Healthcare Inc" and "Phoenix, AZ | Apria Healthcare Inc". Source: https://www.carearizona.org/list08_az_home_medical_equipment.htm
This page gives no address, no phone, and no hours for the Show Low entry, carries no visible last-updated date in the fetched text, and reads as a compiled provider list rather than a current branch locator. It is the **only** fresh source in this run that still names a Show Low Apria at all, and it is not strong enough to publish from, and not current enough to outweigh (a) and (b).

**e) No source found in this run states that the Show Low branch closed.**
Targeted closure searches returned closures for other Apria sites (Chandler above; Oklahoma / Kansas / Arkansas pharmacy facility records for other states, e.g. https://lv.pharmacy.ok.gov/FacilityDetail.asp?CountyTypeLic=88-D-3664) and generic / unrelated "going out of business" content. None names Show Low, AZ. The national company itself is plainly still operating — its homepage was crawled live in this run, promoting sleep / respiratory / wound / pharmacy services and the (888) 492-7742 line: https://www.apria.com/

### Verdict — #146: HELD
- **Not publishable:** no verified current Show Low address in use by Apria, no verified local phone, no hours from an official or reliable current source. Publishing the inventoried 4551 address / (928) 537-7330 would be publishing unverified data — two other businesses are listed at that exact address today.
- **Not decisively closed:** no source states a Show Low closure, and one compiled state list still names Apria in Show Low. "Decisively closed" on this record would overstate the evidence, exactly as in the six prior checks.
- **What would settle it:** a phone check — (928) 537-7330 (does it answer as Apria / is it disconnected / has it been reassigned?) and (888) 492-7742 (does Apria's national line list a Show Low branch / a serving branch for ZIP 85901?). Web-only re-checks have now returned the same shape seven times; another web-only pass is unlikely to change the verdict.

---

## 2. #81 — Summit Eye Surgeons, Prescott

### Inventoried data (from task brief)
- Address: 131 W Navajo Dr, Prescott, AZ
- Phone: (623) 249-7589 — chain-central number (same number is used for all other locations; see below)
- Prior: leaning closed as a Prescott entry; official site lists Scottsdale / Peoria / Chandler / Surprise only; Prescott place record Active with no hours; possible opening-soon permit July 2026.

### Fresh searches run 2026-11-06
1. `Summit Eye Surgeons Prescott Arizona 131 W Navajo Dr`
2. `Summit Eye Surgeons locations Scottsdale Peoria Chandler Surprise Prescott`
3. `"Summit Eye Surgeons" Prescott opening permit 2026`
4. `"131 W Navajo Dr" Prescott`
5. `"Summit Eye Surgeons" Prescott reviews hours`
6. `Prescott Arizona permits issued July 2026 Navajo Summit Eye`

### Fresh page opens
- Summit Eye Surgeons homepage: https://www.summiteyesurgeons.com/ — page crawled 2026-11-05 12:22 UTC, opened in this run.
- Summit Eye Surgeons — Our Doctors: https://www.summiteyesurgeons.com/our-doctors/ — page crawled 2026-11-06 09:36 UTC in this run.
- Summit Eye Surgeons — FAQs: https://www.summiteyesurgeons.com/faqs/ — page crawled 2026-11-05 16:25 UTC, opened in this run.
- City of Prescott, Permits Issued with Fees and Values, 7/1/2026–7/31/2026 (44 pages): https://prescott-az.gov/wp-content/uploads/2026/07/REC-JULY-2026-Permits-Issued-with-Fees-and-Values.pdf — opened in this run and searched in-page for "Navajo" (2 matches only; see below).

### What the fresh evidence shows

**a) The official site still lists four locations only — Prescott is not among them.**
Identical location blocks appear in the footer of the homepage, Our Doctors, and FAQs pages, opened in this run:
- Scottsdale — 14256 N. Northsight Blvd Unit #120
- Peoria — 8256 W. Cactus Rd. D130, Peoria, AZ 85381
- Chandler — 595 N. Dobson Rd. Suite A-15
- Surprise — 12647 W. Smokey Dr. Building F, Suite 115
- Phone on all pages: 623-249-7589

The homepage body section headed "Locations & Offices" / "Serving the Valley" likewise lists only Northsight (Scottsdale), Chandler, and Peoria.
Sources: https://www.summiteyesurgeons.com/ , https://www.summiteyesurgeons.com/our-doctors/ , https://www.summiteyesurgeons.com/faqs/
No Prescott address, Prescott hours, or Prescott announcement appears on any official page opened.

An independent review aggregator agrees: Trustindex's Summit Eye Surgeons locations list names North Scottsdale (14256 N Northsight Blvd Ste 120), Surprise (12647 W Smokey Dr Building F), and Chandler (595 N Dobson Rd) — no Prescott. Source: https://www.trustindex.io/reviews/www.summiteyesurgeons.com

**b) A Prescott place record exists, but it is thin — Active, no hours, chain phone only.**
Search results returned a place record:
- Summit Eye Surgeons — 131 W Navajo Dr, Prescott, AZ, US, Operating Status: Active, Primary Category: Ophthalmologist, phone +1 623-249-7589, website https://www.summiteyesurgeons.com/ — **with no Hours block**, unlike the chain's other locations. Source: https://www.summiteyesurgeons.com/

By contrast, the same search system returned full hours for the established locations, all Mon–Fri 8:00 AM–4:30 PM:
- Scottsdale — 14256 N Northsight Blvd Ste 120
- Peoria — 8256 W Cactus Rd Ste D130
- Chandler — 595 N Dobson Rd Ste A-15
Sources: https://www.summiteyesurgeons.com/ , http://www.summiteyesurgeons.com/

That contrast — hours present for Scottsdale / Peoria / Chandler, hours absent for Prescott — is consistent with a location that is planned / in set-up rather than trading. It is **not** proof by itself. No Prescott-specific reviews, Prescott hours, or Prescott opening announcement were found in the reviews/hours search in this run.

**c) NEW in this run — the July 2026 permit for the exact address is confirmed from the City's own list.**
City of Prescott, Permits Issued, date range 7/1/2026–7/31/2026, Commercial / Tenant Improvement and Remodel section:
> **B2606-080 — COMMERCIAL — 131 W NAVAJO DR UNIT A — $80,000.00**
> **7/21/2026 — TENANT IMPROVEMENT AND REMODEL — Parcel 113-03-021L — $1,144.05**
> **6/16/2026 — ISSUED — DAMERON PARK ADD — $1,144.05**
> **Owner Name: BKS PROPERTY DEVELOPMENT LLC — Contractor Name: Con Ker Enterprises Inc**

Source: https://prescott-az.gov/wp-content/uploads/2026/07/REC-JULY-2026-Permits-Issued-with-Fees-and-Values.pdf (page 5 of 44 in the PDF as fetched; in-page find for "Navajo" returns this entry and one unrelated grading permit for 199 W Navajo Dr, ENG2606-013 — no other Navajo Dr commercial permit, and no Certificate of Occupancy for 131 W Navajo Dr appears in the July list as fetched).

Notes on this permit, stated carefully:
- It confirms a real, paid, issued $80,000 tenant-improvement at the inventoried address in July 2026. That upgrades the prior brief's "possible opening-soon permit" from possible to **confirmed permit, confirmed address, confirmed date**.
- The permit text as fetched does **not** name "Summit Eye Surgeons" as owner, tenant, or contractor. The owner is BKS PROPERTY DEVELOPMENT LLC. The initials "BKS" coincide with the initials of Summit's founder/CEO, named on the official Our Doctors page as "Brandon Suedekum, M.D. … founder and CEO of Summit Eye Surgeons" (https://www.summiteyesurgeons.com/our-doctors/). That coincidence is noted as a **lead, not as proof** — no source opened in this run states that BKS Property Development LLC is Dr Suedekum's company or that this fit-out is for Summit Eye Surgeons.
- A tenant-improvement permit is not an opening. This run found no Certificate of Occupancy, no opening date, no "now open" announcement, and no addition of Prescott to the official locations list in the roughly three months since the permit issued.

**d) No closure evidence either.**
No source in this run states that a Prescott Summit Eye Surgeons opened and closed, or that a Prescott opening was cancelled. The chain itself is active: its homepage in this run carries patient reviews dated 22 October–3 November 2026.

### Verdict — #81: HELD
- **Not publishable:** the business's own site does not list Prescott; there are no verified Prescott hours, no verified opening, and the only phone is the chain-central (623) 249-7589. Publishing a Prescott entry now would present a not-yet-listed location as open.
- **Not decisively closed:** "closed" is the wrong frame on this evidence — a July 2026 fit-out permit at the exact address points the other way, toward a location in preparation. The prior brief's "leaning closed as a Prescott entry" should be **revised to "leaning opening-soon / not yet open"** on the strength of the confirmed permit.
- **What would settle it:** (1) a phone check to (623) 249-7589 asking directly whether the Prescott (131 W Navajo Dr) office has opened and, if so, its hours; (2) a check of City of Prescott permit lists for August–October 2026 for a Certificate of Occupancy at 131 W Navajo Dr Unit A — not done in this run (only the July 2026 list was opened), and recorded here as an open gap, not as a negative finding; (3) re-checking the official locations footer — Prescott appearing there, with hours, would make this entry publishable at once.

---

## Summary table

| Hold | Town | Verdict 2026-11-06 | Publishable data in hand? | Decisive closure proof? | Next step that would settle it |
|---|---|---|---|---|---|
| #146 Apria Healthcare — 4551 S White Mountain Rd, (928) 537-7330 inventoried | Show Low | **HELD — leaning closed** (7th check, unchanged shape) | No — address now lists It's A Ruff Life Grooming & Spa and Acute Head Spa; no Show Low branch / phone / hours in any fresh Apria result | No — no source states a Show Low closure; CareArizona compiled list still names Show Low | Phone: (928) 537-7330 and (888) 492-7742 |
| #81 Summit Eye Surgeons — 131 W Navajo Dr, (623) 249-7589 chain-central | Prescott | **HELD — leaning opening-soon / not yet open** (revised from "leaning closed") | No — official site lists Scottsdale / Peoria / Chandler / Surprise only; Prescott record has no hours | No — and a confirmed $80,000 tenant-improvement permit B2606-080, issued 7/21/2026 for 131 W Navajo Dr Unit A, points toward preparation, not closure | Phone: (623) 249-7589; plus Aug–Oct 2026 Prescott permit lists for a Certificate of Occupancy (gap in this run) |

## Gaps and limits of this run
- Apria's official Locations page (https://www.apria.com/locations) did not render a branch list as text; its locator could not be interrogated for ZIP 85901 by text fetch. Recorded as a fetch gap, not as evidence for either side.
- Only the City of Prescott **July 2026** permit list was opened for Summit. August–October 2026 lists were not checked in this run.
- No phone calls were made (web-only task). Both holds now sit at the point where a phone call, not another web pass, is the step that can move them.
- Nothing was published, and no progress-file or index.html changes were made in this research pass.

## Sources used (all opened or returned in this run, 2026-11-06)
- https://www.apria.com/
- https://www.apria.com/locations
- http://www.apria.com/
- https://www.carearizona.org/list08_az_home_medical_equipment.htm
- http://showlowpetgrooming.com/
- https://acuteheadspa.com/
- https://azmemory.azlibrary.gov/assets/displaypdf/136017
- https://lincolninst.edu/app/uploads/legacy-files/gwipp/upload/sources/Arizona/2008/AZ_sourcedoc_FY2008_Enteprise%20Zone%20Program%20Annual%20Report.pdf
- https://www.summiteyesurgeons.com/
- https://www.summiteyesurgeons.com/our-doctors/
- https://www.summiteyesurgeons.com/faqs/
- http://www.summiteyesurgeons.com/
- https://www.trustindex.io/reviews/www.summiteyesurgeons.com
- https://prescott-az.gov/wp-content/uploads/2026/07/REC-JULY-2026-Permits-Issued-with-Fees-and-Values.pdf
