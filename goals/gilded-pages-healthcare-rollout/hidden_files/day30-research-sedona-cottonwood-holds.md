# Day 30 Research — Sedona / Cottonwood Held Entries (RESEARCH ONLY)

Date of research: 2026-11-02 (Arizona time)
Scope: re-check of 4 held entries only. No publishing, no index edits, no images.
Method: official business sites read directly with browser.open on 2026-11-02, plus
place/directory records and NPI (NPPES-derived) records returned by browser.search.
Every fact below names its source. A fetch failure is recorded as a gap, not as proof.

Precedents used for the verdicts (from ~/workspace/gilded-pages/healthcare-progress.md):
- SUCCESSOR PUBLISHED: Day 9 — The Smiles Movement published as successor to inventory
  #19 Onsite Dental (same address/phone), with the successor fact stated plainly.
  Day 11 correction — #32 published as Northern Arizona Periodontics, successor to
  Dr. Michael R. Robertson at the same address/phone. Day 13 — CenterWell Home Health
  published as successor to Kindred at Home at the same address/phone. Day 6 — Elk
  Ridge rebrand published in the same way.
- HELD FOR A PHONE CALL: Day 9 — Red Rock #24 held ("needs a live phone call to
  (928) 282-1282 before publishing — do NOT publish both Westervelt and Red Rock at
  A-3"). Day 12 — Mahanti #70 and Pacific Clear Vision #72 held on the same rule.
  Day 13 — Alliance #141 held ("needs official locations-page confirmation or a
  phone call to (928) 852-0880").
- WEBSITE OMITTED IS NOT A BLOCKER by itself: Day 2 Plets, Day 5 Ponderosa /
  High Country, Day 9 Parfitt — entries published with the website field omitted
  when the rest was verified. A missing website never held an entry on its own;
  a missing/conflicting address, phone, or occupant did.

---

## 1. Inventory #24 — Red Rock Dental, Sedona

### Inventory / held record
- Inventory: "1120 AZ-89A — (888) 217-4023 — General dentistry."
  The (888) 217-4023 number was already established on Day 9 as a Google-only
  call-tracking number; the real local number in directories is (928) 282-1282.
- Day 9 hold reason: Westervelt's official site claims the suite directories gave
  Red Rock; hours conflict; redrockdental.net fetch failed.

### What was found in this pass
- PLACE RECORD (search place record, place_id 801090907572152):
  "Red Rock Dental — 1120 AZ-89A, Sedona, AZ — Operating Status: Active —
  Phone: +1 928-282-1282 — Hours: Monday 8:00 AM–4:00 PM, Tuesday 9:00 AM–4:00 PM,
  Wednesday 8:00 AM–4:00 PM, Thursday 8:00 AM–4:00 PM — Rating 4.8, 19 reviews —
  Primary Category: Dental Clinic." No suite, no Friday/weekend hours, no website
  in the record.
- OPENCARE (read directly, https://www.opencare.com/dentists/sedona-az/red-rock-dental-24630218973c/,
  crawled ~18 hours before this pass): a live profile headed "Red Rock Dental —
  Sedona, AZ 86336 — Request Appointment," generic text ("When you visit our
  office, your health and happiness are our top priorities…"), teeth whitening and
  check-up/cleaning listed. The fetched text carried NO address, phone, dentist
  name, or hours — it proves a profile exists, not who or where exactly.
- OFFICIAL SITE: redrockdental.net could NOT be read in this pass — the fetch
  failed without an HTTP status. That is a gap, exactly as on Day 9. It is NOT
  proof the domain is dead, and no official-site address/phone/hours exist to cite.
- WESTERVELT — OFFICIAL SITE READ DIRECTLY (https://westerveltfamilydentistry.com/,
  crawled 2026-11-02): body text: "Sedona Office — 1120 West State Route 89A,
  Ste A — Sedona, AZ 86336 — 928 204-2062 — Hours 8:00AM–4:00PM, Tuesday thru
  Friday." Page footer: "1120 West State Rte 89A, Suite A-3 Sedona, AZ" with the
  same (928) 204-2062. Westervelt is already published (Day 9, big-westervelt-dental)
  at Ste A-3, Tue–Fri 8 AM–4 PM.
- BUILDING CONTEXT at 1120 W SR 89A (WebMD directory, crawled ~83 days ago):
  Ste D-1 = Sedona Dental Arts (published Day 9, (928) 282-1514);
  Ste A3 = "Dr. Michael Thomas Hughes, DDS"; Ste B4 = Dr. Jeffery P. Hreha
  (endodontics); Ste A2 = Dr. George Lee Moore, DDS. This is a multi-suite dental
  building — a bare "1120" address with no suite cannot separate its occupants.
- HUGHES NPI CHECK: Michael Thomas Hughes, DDS — NPI 1154414142, certification
  2024-08-19 (NPPES record read directly). His NPI practice location is NOT Sedona:
  it is 522 W Finnie Flat Rd Ste J, Camp Verde, AZ 86322, phone (928) 567-5249 —
  that is Verde Dental Care, Camp Verde (already published Day 8). So the WebMD
  "Hughes at 1120 Ste A3" listing is stale; Hughes does not currently support a
  Red Rock identity at A-3.
- NO NPI record for an organisation named "Red Rock Dental" in Sedona was found
  in this pass, and no current source ties a named dentist to (928) 282-1282.

### Conflicts
1. Suite conflict, unresolved: directories/place record give Red Rock no suite;
   the only suite ever associated with it (A-3) is now claimed in TWO places on
   Westervelt's own official site (Ste A in the body, Suite A-3 in the footer).
   Publishing Red Rock at A-3 would duplicate the published Westervelt entry.
2. Hours suspicion (flagged, not proven): the Red Rock place hours
   (Mon 8–4, Tue 9–4, Wed–Thu 8–4, nothing Fri–Sun) are IDENTICAL to the published
   official hours of Sedona Dental Arts in Ste D-1 of the same building. That is
   the pattern of place-record contamination between co-located practices seen
   before in this rollout (Day 9: Sedona Family Dentistry's Google description
   copying Westervelt's history). It may also be coincidence — it cannot be
   settled from directories.
3. Phone: inventory (888) 217-4023 (call-tracking, do not use) vs local
   (928) 282-1282 (place record + Day 9 WebMD/Vitals/denTEL). Use 282-1282 only.
4. A same-name practice in Moab, UT (Red Rock Dental, LLC, (435) 259-4059, BBB)
   and a Las Vegas "Red Rock Dental" are unrelated — do not import their data.

### Verdict: HELD — not publishable, not proven closed
The name, a local phone, an "Active" place status, and an Opencare profile keep
this from being closed as dead. But there is still no official site, no suite,
no named dentist, and no hours that can be trusted as Red Rock's own — and the
one candidate suite belongs to an already-published practice.

### Still needs a phone call — (928) 282-1282, and only this settles it
Ask: (1) Is this Red Rock Dental, still seeing patients? (2) Which suite at
1120 W SR 89A? (3) Which dentist(s) practise there now? (4) Hours, including
Friday? (5) Is there a working website?
- If the call confirms a distinct suite/dentist: publishable as a normal Sedona
  dental entry with the call-confirmed data, website omitted if none works.
- If the number rings Westervelt or Sedona Dental Arts, or is disconnected:
  close #24 as succeeded/closed and note which.

---

## 2. Inventory #70 — Dr. Robert Mahanti / The Eye & Laser Center, Cottonwood

### Inventory / held record
- Inventory: "401 S Calvary Way #D — (928) 779-7000 — Ophthalmology / LASIK surgeon."
- Day 12 hold reason: azlaser.com's Cottonwood page (~5 years stale) claims the
  same Suite D that The Eye Clinic — Dr. Farshid Paydar claims on a live official
  site ((928) 649-2600, NPI updated 2026-06). Needs a call to (928) 779-7000.

### What was found in this pass
- MAHANTI OFFICIAL SITE READ DIRECTLY (https://www.azlaser.com/, crawled
  2026-11-02): the homepage now shows ONLY "900 N San Francisco St, Flagstaff,
  AZ 86001 | 928.779.7000" with Dr. Mahanti's biography (Wayne State, University
  of Minnesota residency, refractive-surgery fellowship, ABO certified, in
  Arizona practice since 1992). No Cottonwood address appears in the fetched
  homepage. Site service pages carry "Last Updated" stamps ~1,021–1,025 days
  before this pass — an old, lightly maintained site.
- MAHANTI PLACE RECORDS (stale layer): place records for "The Eye & Laser Center"
  and "Dr Robert Mahanti" still claim 401 S Calvary Way #D, Cottonwood,
  (928) 779-7000, Mon–Fri 8 AM–5 PM / Fri to 3 PM, with copy saying "three
  convenient Arizona offices, located in Flagstaff, Cottonwood, and Winslow."
  The same hours/address pattern is attached to the Flagstaff flagship record —
  directory copy carried across locations, not a Cottonwood confirmation.
- MAHANTI NPI: Robert L. Mahanti, MD — NPI 1730146499 (WebMD / HIPAASpace /
  NPPES-derived records). Practice location: 900 N SAN FRANCISCO ST, FLAGSTAFF,
  AZ 86001 ONLY, phone 928-779-7000. Last NPI update: 2008-04-25. No Cottonwood
  location in the NPI record at all. Current directories (WebMD, Healthgrades)
  list him in Flagstaff (Northern Arizona Eye Associates, 900 N San Francisco
  St) and as accepting patients there — the Flagstaff practice is active; only
  the Cottonwood claim is unsupported.
- SUCCESSOR — THE EYE CLINIC, OFFICIAL SITE READ DIRECTLY
  (https://arizonaeyeclinic.com/, crawled 2026-11-02):
  "The Eye Clinic, 401 S Calvary Way Suite D, Cottonwood, AZ 86326 —
  Hours: Mon, Tue, Wed, Thu, Fri: 08:00-17:00, Sat, Sun: Closed —
  Cottonwood: (928) 649-2600 — Sedona: (928) 203-9600."
  Same suite, current official site, full address/phone/hours.
- SUCCESSOR — PAYDAR NPI: Farshid Paydar, MD — individual NPI 1376538678,
  primary practice 401 S CALVARY WAY STE D, COTTONWOOD, AZ 86326-4165, phone
  (928) 649-2600, fax (928) 649-7847, last individual update 2022-12-28.
  Organisation NPI for FARSHID PAYDAR MD PC (1609039056; also 1558431866) at
  the same Ste D address shows Last Update Date 2026-06-09 — fresh federal
  corroboration that Paydar's organisation is the current Ste D occupant.
- SUCCESSOR — CORROBORATION: WebMD lists Dr. Paydar at The Eye Clinic,
  401 S Calvary Way Ste D, Mon–Fri 8:00 AM–5:00 PM, accepting new patients.
  The Eye Clinic's own patient-paperwork PDF (hosted on its site) heads all
  locations "Farshid Paydar, MD — Board Certified Ophthalmologist; Joshua
  Miller, OD — Optometrist" and lists Cottonwood 401 S. Calvary Way Ste. D,
  PH (928) 649-2600, FAX (928) 634-7847, alongside Sedona, Village of Oak Creek,
  and Camp Verde offices.
- BUILDING NOTE: Vue Optical, 401 S Calvary Way Ste B (published Day 12,
  big-vue-optical, (928) 300-7310), is a different suite in the same building —
  no conflict with a Ste D entry.

### Conflicts
1. Two official claims to Suite D: azlaser.com's old Cottonwood copy vs
   arizonaeyeclinic.com's current footer. Resolved in The Eye Clinic's favour by:
   azlaser.com's own current homepage dropping Cottonwood entirely, Mahanti's
   NPI naming Flagstaff only, and Paydar's organisation NPI updated 2026-06-09
   at Ste D.
2. One directory (Optix-now) lists Ste D with a third phone, (928) 634-5082.
   No other source supports it; official site + NPI agree on (928) 649-2600.
   Treat 634-5082 as directory noise, do not publish it.
3. Do NOT describe Mahanti as "closed." His Flagstaff practice is demonstrably
   active. What ended/unconfirmed is only his Cottonwood presence at Ste D.

### Verdict: PUBLISHABLE — as the successor entry, not as Mahanti
Publish: **The Eye Clinic — Dr. Farshid Paydar** (successor to inventory #70 at
the same suite), on the Smiles Movement / Northern Arizona Periodontics /
CenterWell successor precedent, with the entry stating plainly that The Eye
Clinic now practises at the suite formerly listed for The Eye & Laser Center.
Close #70 itself as SUCCEEDED at Cottonwood (not "Mahanti closed").
Exact publishable data (official site, read 2026-11-02):
- Name: The Eye Clinic (Dr. Farshid Paydar, MD; Joshua Miller, OD also named
  in the practice's own paperwork)
- Address: 401 S Calvary Way Ste D, Cottonwood, AZ 86326
- Phone: (928) 649-2600
- Hours: Mon–Fri 8:00 AM–5:00 PM; Sat–Sun closed
- Website: https://arizonaeyeclinic.com/
- Category: vision (ophthalmology / comprehensive eye care, surgical care)

### Still needs a phone call?
No call blocks the successor entry — official site + fresh organisation NPI
meet the rollout's publish standard. One OPTIONAL call remains for the record:
(928) 779-7000 (Mahanti, Flagstaff) — "Do you still see patients in Cottonwood
at 401 S Calvary Way?" — to close #70's file wording. If that call is never made,
the entry note should say Mahanti's Cottonwood presence is "no longer listed,"
not "confirmed ended by phone."

---

## 3. Inventory #72 — Pacific Clear Vision, Cottonwood

### Inventory / held record
- Inventory: "294 AZ-89A — (928) 634-2905 — Optometry."
- Day 12 hold reason: two clusters at 294 W SR 89A — Pacific Clear Vision
  (928) 634-2905 vs "Pacific Clearvision Institute, Suite 114, (928) 634-4200
  (BBB)"; pcvi.com is an Oregon practice with no Cottonwood location; no
  website, no hours verified. Needs a call to (928) 634-2905.

### What was found in this pass — the Ste 114 cluster is now identified
- PACIFIC CLEAR VISION PLACE RECORD (place_id 574934901272462): "294 AZ-89A,
  Cottonwood, AZ — Operating Status: Active — Primary Category: Optometrist —
  Phone: +1 928-634-2905." NO hours, NO website, NO suite, NO doctor name.
  That single record is the whole evidence for the name/phone pairing.
- STE 114 = DR. RENEE McCOY (NPI, NPPES-derived record read in this pass):
  organisation RENEE MCCOY, M.D., PLLC — NPI 1053627745 — mailing AND practice
  address 294 W HWY 89A STE 114, COTTONWOOD, AZ, phone 928-634-4200.
  Individual: Renee McCoy, MD — NPI 1700813433.
  Place record agrees: "Dr Renee McCoy — 294 AZ-89A #114, Cottonwood —
  Ophthalmologist — Phone: +1 928-634-4200."
  So Suite 114 / (928) 634-4200 is a distinct, federally registered ophthalmology
  practice — Dr. Renee McCoy — not "Pacific Clearvision Institute."
- NO COTTONWOOD "PACIFIC CLEARVISION INSTITUTE" WAS FOUND in this pass: BBB and
  general searches returned only the Oregon institute and unrelated BBB pages.
  The Day 12 "(BBB)" attribution for a Cottonwood Ste 114 PCVI listing could not
  be reproduced and should be treated as part of the original conflation.
- OREGON INSTITUTE CONFIRMED SEPARATE (pcvi.com location records): Pacific
  ClearVision Institute — Eugene, OR (360 S Garden Way, (541) 343-5000) and
  Cottage Grove, OR (257 N 8th St, (541) 942-5000). No Arizona location on its
  own site. Its data must never be used for the Cottonwood entry.
- PHONE CORRECTION to the Day 12 note: (928) 634-4200 (McCoy, Ste 114) is NOT
  Southwestern Eye Center's number. Southwestern Eye Center — Cottonwood's
  official page (sweye.com/locations/cottonwood/, already published Day 11 as
  big-southwestern-eye-cottonwood) gives (928) 634-4202, 270 S Candy Ln,
  Mon–Fri 8 AM–5 PM. 4200 and 4202 are two different numbers, one digit apart —
  an easy conflation, and the likely root of part of this hold.
- NO source in this pass ties any doctor name, NPI, hours, or website to the
  name "Pacific Clear Vision" or to (928) 634-2905, beyond the place record.

### Conflicts
1. Name conflation, partly resolved: "Pacific Clear Vision" (no suite,
   634-2905, optometrist) vs the Ste 114 ophthalmologist (McCoy, 634-4200).
   They share a building address (294 W SR 89A) and nothing else that is
   documented. They may be neighbours, or Pacific Clear Vision may be a former
   name / DBA connected with the Ste 114 practice — no source says either.
2. Category conflict inside the hold itself: inventory says optometry for
   #72; the only verified practice at the address is ophthalmology (McCoy).
   Publishing #72 as optometry at Ste 114 would misstate McCoy; publishing it
   with no suite repeats the bare-address problem from Red Rock #24.

### Verdict: HELD — not publishable, not proven closed
One place record (Active, right phone) is not enough: no doctor, no suite, no
hours, no website, no NPI. It also cannot be closed — nothing says it shut.

### Still needs a phone call — (928) 634-2905, and only this settles it
Ask: (1) What business name answers — Pacific Clear Vision, or another name?
(2) Which suite at 294 W SR 89A? (3) Which doctor(s) — and is there any link to
Dr. McCoy's Ste 114 practice? (4) Hours? (5) Website?
- If a distinct practice confirms itself: publishable on the call data
  (website omitted if none).
- If Ste 114 / McCoy's office answers on this number: re-file #72 as the same
  practice as McCoy and publish ONE entry for 294 W SR 89A under the verified
  name, not two.
- Separate lead created by this pass (not #72, do not merge without the call):
  Dr. Renee McCoy, MD, PLLC — 294 W SR 89A Ste 114, Cottonwood, (928) 634-4200 —
  NPI-verified address/phone, but no hours or website found; it would need its
  own verification (same phone call can cover it) before any listing.

---

## 4. Inventory #141 — Alliance Homecare / Valley Respiratory, Cottonwood

### Inventory / held record
- Inventory: "1756 E Villa Dr, C-9 — (928) 852-0880 — Home health plus medical
  equipment."
- Day 13 hold reason: Cottonwood location, phone, and Friday hours are
  directory-only and not confirmed on valleyrespiratory.com; the official site
  supports DME/respiratory, not the skilled home health the inventory described.
  Needs official locations-page confirmation or a call to (928) 852-0880.

### What was found in this pass
- OFFICIAL SITE READ DIRECTLY (https://valleyrespiratory.com/, crawled
  2026-11-02): "Founded in 2006 as a respiratory focused company, we have grown
  to… a full service DME provider… throughout Maricopa, Yavapai, Pima and Pinal
  counties." "Our licensed respiratory therapists deliver professional setup,
  patient education, and 24/7 on-call emergency support for… CPAP and BiPAP,
  oxygen systems, ventilators, nebulizers, airway clearance devices, and
  continuous glucose monitoring." The fetched homepage names NO locations, NO
  Cottonwood address, and NO (928) 852-0880 — there is still no official
  locations-page confirmation for Cottonwood. Yavapai County service area on
  the official site is consistent with a Cottonwood office, but does not prove
  the C-9 storefront.
- PLACE RECORD (place_id 581616808342012): "Alliance Homecare — 1756 E Villa
  Dr C-9, Cottonwood, AZ — Operating Status: Active — Primary Category: Medical
  Equipment Supplier — Phone: +1 928-852-0880 — Website:
  https://valleyrespiratory.com/ — Hours: Monday 9:00 AM–5:00 PM, Tuesday
  9:00 AM–5:00 PM, Wednesday 9:00 AM–5:00 PM, Thursday 9:00 AM–5:00 PM."
  Friday, Saturday, and Sunday are simply absent from the record — Friday is
  unlisted, NOT stated closed. This is the same directory-only pattern as Day 13,
  now with Mon–Thu hours attached.
- SISTER OFFICE (same place system): "Alliance Homecare — 3194 Willow Creek Rd,
  Prescott, AZ — (928) 717-1560 — Mon–Fri 8:30 AM–5:00 PM — Home Health Care
  Service / Medical Equipment Supplier," with Valley Healthcare Group copy
  about respiratory equipment. It shows the Alliance name is a live Valley
  Respiratory family brand in the region — and that its hours/phones are
  location-specific, so Prescott's Mon–Fri pattern must NOT be copied onto
  Cottonwood's missing Friday.
- OTHER VALLEY RESPIRATORY PLACE RECORDS (same system): Mesa HQ 2330 W
  Broadway Rd, (480) 830-7700, Mon–Fri 8:30–5; Casa Grande 1275 E Florence Blvd
  #4, (520) 836-9300; Tucson 3400 E Speedway Blvd, (520) 722-3210 — all
  Mon–Fri 8:30–5. Cottonwood's 9–5 / Mon–Thu-only pattern differs from every
  sister office, which is exactly why it needs voice confirmation.
- BUILDING CONTEXT: 1756 E Villa Dr is a multi-suite medical building — Aviant
  Hospice is at Ste C-17 (published Day 13, big-aviant-hospice, (928) 634-1073)
  and CenterWell Home Health is next door at 1760 E Villa Dr Ste E & F
  (published Day 13). No source places any other business in Ste C-9 — there is
  no suite conflict of the Red Rock / Mahanti kind.
- NO NPI record for a Cottonwood Alliance Homecare / Valley Respiratory
  organisation at 1756 E Villa Dr was found in this pass (recorded as a gap).

### Conflicts
1. Service description: inventory "home health plus medical equipment" vs the
   official site, which describes a DME / respiratory-equipment provider and
   does not claim skilled home-health nursing. If published, the entry must be
   a Medical Equipment entry (the All-Med Equipment precedent, Day 13), NOT a
   Home Health entry, and must not repeat the inventory's home-health claim.
2. Friday: place record lists Mon–Thu only; every sister office lists Mon–Fri.
   Either Cottonwood is genuinely closed Fridays, or the record is incomplete.
   Directories cannot settle it.
3. Name form: "Alliance Homecare" (place record / inventory) is the local
   storefront name; valleyrespiratory.com is the parent/website. Both names
   belong in any future entry, as the inventory already pairs them.

### Verdict: HELD — one phone call short of publishable
This is the closest of the three true holds: address, suite, phone, category,
website, and Mon–Thu hours all agree across the inventory and the place record,
there is no competing occupant for C-9, and the parent company's official site
confirms the business type and the county. It stays held only because, under
the rollout's own Day 13 ruling, Cottonwood confirmation must come from the
official locations page (still absent) or a phone call — and neither has
happened yet. Do not publish on directory data alone after that ruling.

### Still needs a phone call — (928) 852-0880
Ask: (1) Is this Alliance Homecare / Valley Respiratory at 1756 E Villa Dr
Ste C-9, Cottonwood? (2) Are you open Fridays — if so, what hours? (3) Is C-9 a
walk-in equipment storefront or an office patients phone first? (4) Confirm the
service list (oxygen, CPAP/BiPAP, ventilators, nebulizers, other DME).
- If the call confirms the above: publishable immediately as —
  Name: Alliance Homecare / Valley Respiratory; Address: 1756 E Villa Dr
  Ste C-9, Cottonwood, AZ 86326; Phone: (928) 852-0880; Hours: Mon–Thu
  9:00 AM–5:00 PM plus whatever Friday answer the call gives (if Friday stays
  unconfirmed, publish Mon–Thu and note "ring ahead for Friday");
  Website: https://valleyrespiratory.com/; Category: equipment (Medical
  Equipment), described as respiratory / home medical equipment — not home
  health.
- If the number is disconnected or denies the C-9 location: keep held and note
  the call result; do not close on directory silence alone.

---

## Summary table

| # | Entry | Verdict | Publishable data in hand | Blocking item |
|---|-------|---------|--------------------------|---------------|
| 24 | Red Rock Dental, Sedona | HELD | Name, 1120 W SR 89A (no suite), (928) 282-1282 | Suite/dentist/hours unverified; A-3 claimed by published Westervelt; call (928) 282-1282 |
| 70 | Mahanti / Eye & Laser, Cottonwood | PUBLISHABLE AS SUCCESSOR — The Eye Clinic, Dr. Farshid Paydar | 401 S Calvary Way Ste D, (928) 649-2600, Mon–Fri 8–5, arizonaeyeclinic.com (official site read 2026-11-02; org NPI updated 2026-06-09) | None for the successor entry; optional call to (928) 779-7000 to word #70's closure |
| 72 | Pacific Clear Vision, Cottonwood | HELD | Name, 294 W SR 89A (no suite), (928) 634-2905, optometrist (place record only) | No doctor/suite/hours/site/NPI; Ste 114 is Dr. Renee McCoy (NPI 1053627745 / 1700813433, (928) 634-4200); call (928) 634-2905 |
| 141 | Alliance Homecare / Valley Respiratory, Cottonwood | HELD — one call short | 1756 E Villa Dr Ste C-9, (928) 852-0880, Mon–Thu 9–5, valleyrespiratory.com, DME category | No official locations-page confirmation; Friday unknown; inventory's "home health" claim must be dropped; call (928) 852-0880 |

Corrections this pass makes to the standing record:
1. #72: Ste 114 / (928) 634-4200 is Dr. Renee McCoy, MD, PLLC (NPI-verified) —
   not a Cottonwood "Pacific Clearvision Institute," and 634-4200 is not
   Southwestern Eye's number (theirs is 634-4202).
2. #70: Mahanti's NPI lists Flagstaff only and azlaser.com's current homepage
   lists Flagstaff only — the Cottonwood Ste D claim survives only in stale
   place copy. The Eye Clinic's Ste D claim is official and current.
3. #24: the WebMD "Hughes at Ste A3" lead is stale — Hughes's current NPI
   practice address is Verde Dental Care, Camp Verde.
4. #141: the place record now supplies Mon–Thu 9–5 for C-9 (Friday absent, not
   stated closed); sister offices' Mon–Fri 8:30–5 must not be copied onto it.
