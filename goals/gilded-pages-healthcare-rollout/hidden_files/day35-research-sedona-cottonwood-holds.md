# Day 35 Research — Sedona / Cottonwood Holds — 2026-11-07

Research only. Nothing published, no images generated, index.html / healthcare-progress.md not edited.
Method: fresh `browser.search` / `browser.open` only on 2026-11-07 (pages opened were crawled less than a minute before opening, ~10:31–10:32 UTC / 03:31 MST), against official sites, place listings, and directories. No live browser, no phone calls — a call cannot be made from here, which is exactly what each hold still needs.
Prior state:
- Task brief for Day 35: #24 Red Rock Dental (Sedona), #72 Pacific Clear Vision (Cottonwood), #141 Alliance Homecare / Valley Respiratory (Cottonwood) — holds only.
- `~/workspace/goals/gilded-pages-healthcare-rollout/hidden_files/day34-research-sedona-cottonwood-holds.md` — Day 34 verdicts, all three still held, with the full prior evidence chain.

**Summary verdict: all three remain HELD, needing a phone call. None is publishable with fully verified data today, and none is decisively closed/skippable on today's fresh evidence. No material change from Day 34 — the same three single-source gaps survive a fresh check on 2026-11-07.**

One fetch note: an attempt today to open `https://www.redrockdental.net` failed in the fetch tool with "requires a resolvable public HTTP(S) URL" / no source HTTP status. That is a fetch gap, not proof the domain is dead, and it was not retried. It is consistent with prior days: no live first-party Sedona Red Rock site has ever been retrieved.

---

## 1. #24 Red Rock Dental — Sedona

- Inventoried: Red Rock Dental — Sedona — 1120 W SR 89A — phone in inventory (888) 217-4023 (call-tracking, do not use) — local candidate (928) 282-1282 — General dentistry.
- Prior hold: Westervelt Family Dentistry claims the same building, suite A-3; redrockdental.net dead / unretrievable; no suite, no website for Red Rock.
- Task question: is Red Rock still open and distinct, which suite, hours, website?

### What was checked today (2026-11-07)

- Place data via search, 2026-11-07 (identical across the searches run today — "Red Rock Dental Sedona AZ 1120 W SR 89A", `"Red Rock Dental" Sedona 928-282-1282`, `"Michael Hughes" DDS Sedona Red Rock Dental 1120`, `"9282821282" Sedona dentist`, `"Red Rock Dental" Sedona Yelp reviews`):
  - Red Rock Dental — Address: 1120 AZ-89A, Sedona, AZ, US — Operating Status: Active — Phone: +19282821282 — Hours (America/Phoenix): Monday–Thursday 8:30 AM–4:30 PM (no Friday–Sunday listed) — Rating 4.8, based on 19 reviews — Primary Category: Dental Clinic; Secondary: General Dentist, Dentist & Dental Office — place_id 801090907572152 — Exact Location: 34.863163, -111.779394.
  - **No suite number and no website in the place record.** This is still the only source for the phone and the hours.
- Exact-phone check: searching the local number today returned only Red Rock Dental's own place record for (928) 282-1282 — no directory, insurer list, NPI record, or practice page corroborates it today.
- Opencare — https://www.opencare.com/dentists/sedona-az/red-rock-dental-24630218973c/
  - Opened 2026-11-07, page crawled less than a minute before opening.
  - Live profile: "Red Rock Dental - Sedona, AZ 86336 - Request Appointment"; text: "When you visit our office, your health and happiness are our top priorities. Our team is dedicated to providing you with the personalized, comprehensive care that you deserve."; confirms teeth whitening and regular check-up and cleaning services.
  - The fetched page gives **no address, no phone, no hours, no suite, no dentist name, and no official website**. It confirms the name still takes appointment requests in Sedona — nothing more.
- Westervelt Family Dentistry official site — http://www.westerveltfamilydentistry.com/
  - Opened 2026-11-07, page crawled less than a minute before opening.
  - Body: "Sedona Office — 1120 West State Route 89A, Ste A, Sedona, AZ 86336 — 928 204-2062 — Hours 8:00AM – 4:00PM, Tuesday thru Friday."
  - Footer: "(928) 204-2062 — 1120 West State Rte 89A, Suite A-3 Sedona, AZ."
  - So Westervelt's own site is internally inconsistent (Ste A in the body, Suite A-3 in the footer) but unambiguously claims a suite at **1120** W SR 89A today, with a different phone ((928) 204-2062) and different hours (Tue–Fri 8:00 AM–4:00 PM) from Red Rock's place record. Westervelt is already published in the Gilded Pages.
  - Directory inconsistency noted, not resolved: Westervelt's place record and its NPI record (Kirk Westervelt Dmd, PC, NPI 1386833382) still list **1146** W HWY 89A STE A, Sedona, AZ 86336, phone (928) 204-2062; a directory copy (smyleee.com, "Website Updated Nov 5, 2026") lists Westervelt at "#A-3, 1120, West State Route 89A". Either way, Westervelt is a separate practice from Red Rock on every source — different name, phone, hours, and place_id (2620673628068859).
- The rest of the 1120 building, from sources checked today:
  - Sedona Dental Arts official site — https://www.sedonadentalarts.com/ — opened 2026-11-07: "1120 W. State Route 89A, Ste. D-1 Sedona, AZ 86336 — 928-282-1514 — Hours: Monday 8:00 a.m.–4:00 p.m., Tuesday 9:00 a.m.–4:00 p.m., Wednesday 8:00 a.m.–4:00 p.m., Thursday 8:00 a.m.–4:00 p.m., Friday Closed." So **Suite D-1 is Sedona Dental Arts** (Dr. Austin Babcock / Dr. David Bill, (928) 282-1514).
  - WebMD dentist lists for Sedona (crawls up to ~88 days old — stale copies, background only): individual dentists tied to 1120 suites A2, A3 (Dr. Michael Thomas Hughes; Dr. Farpour Namiranian), B4 (endodontics), and D1. No source, old or new, assigns any suite to Red Rock Dental.
  - Pin collision: Red Rock Dental's coordinates (34.863163, -111.779394) are effectively identical to Dr. David H. Bill's place record (34.863166, -111.779396) and very close to Sedona Dental Arts' place record (34.863119, -111.779391) — the same pin cluster at 1120. That is consistent with a multi-suite building pin, and equally consistent with a stale/duplicate listing; today's evidence cannot separate the two.
- Historical evidence only: the Keep Sedona Beautiful Spring 2016 newsletter (keepsedonabeautiful.org PDF, in today's searches) lists "Red Rock Dental… www.RedRockDental.net" as a sponsor. That proves the practice traded under that name and domain in 2016 — it does not prove it trades today.
- `RedRockDental.net` today: a search for `redrockdental.net Sedona` returned **no Sedona official site** — only the Opencare profile and unrelated same-name practices (Las Vegas/Summerlin NV, Medicine Hat AB, Carson City NV, Redmond OR, Swampscott MA). The direct fetch attempt failed as noted at the top (a gap, not proof of death). No first-party Red Rock Dental Sedona website was found today.

### Verdict: HELD — needs a phone call (not publishable, not decisively closed)

- **Call (928) 282-1282 — question: "Is Red Rock Dental still open and distinct from Westervelt Family Dentistry and Sedona Dental Arts in the same building at 1120 W SR 89A in Sedona, which suite is it in, what are its current hours, and what is its official website?"**
  - Do NOT call the inventoried (888) 217-4023 — prior work identified it as a call-tracking number, and no dental source ties it to Red Rock.
- Why not publishable: no suite (both candidate suites at 1120 are claimed by others — Ste A / A-3 by Westervelt's own site, Ste D-1 by Sedona Dental Arts' own site); no official website; the phone, hours, and Active status rest on a single place record with no second corroborating source found today; publishing it at the bare 1120 address beside the already-published Westervelt entry risks listing one practice twice or a dead name once.
- Why not decisively closed: the place record said Active today with 19 reviews at 4.8 stars, and Opencare still takes appointment requests for a Sedona Red Rock Dental as of 2026-11-07. No closure, move, or succession statement was found in any source today.
- Directory-only candidate data (DO NOT publish until the call confirms):
  - Red Rock Dental — 1120 W SR 89A, Sedona, AZ 86336 (suite unverified — do not use A-3 or D-1; both are other practices' suites) — (928) 282-1282 — Mon–Thu 8:30 AM–4:30 PM (place data only, hours not confirmed) — website: none verified (omit website).

---

## 2. #72 Pacific Clear Vision — Cottonwood

- Inventoried: Pacific Clear Vision — Cottonwood — 294 W State Route 89A — (928) 634-2905 — Optometry.
- Prior hold: single place record Active only, no hours/website/suite; pcvi.com is Oregon only.
- Task question: current status — is there a real, verifiable Cottonwood optometrist here, with hours and website?

### What was checked today (2026-11-07)

- Place data via search, 2026-11-07 (identical across the searches run today — "Pacific Clear Vision Cottonwood AZ 294 W State Route 89A", `"Pacific Clear Vision" Cottonwood Arizona optometrist`, `"Pacific Clear Vision" 928 634 2905`):
  - Pacific Clear Vision — Address: 294 AZ-89A, Cottonwood, AZ, US — Operating Status: Active — Primary Category: Optometrist — Phone: +19286342905 — place_id 574934901272462 — Exact Location: 34.733833, -112.02963.
  - **No hours, no website, no suite, no rating/reviews, and no practitioner name in the returned record** — the thinnest of the three holds, unchanged.
- Exact-phone check: a search for `"928-634-2905"` today returned **no result tying that number to Pacific Clear Vision or to any eye business** — the hits were unrelated Cottonwood businesses. The number is corroborated nowhere except the place record itself.
- Address check: 294 W State Route 89A is a multi-suite medical building in today's directory results — e.g. suites 107, 110, 114, 203, 208/208A, 209 are tied to named Verde Valley / Northern Arizona Healthcare practices (cardiology, pain, urology, OB/GYN) in Healthgrades/WebMD copies. **No source today places Pacific Clear Vision in any suite at 294, and no second source places any optometrist at 294.** Every other practice found at that address carries a suite; Pacific Clear Vision carries none.
- Pacific ClearVision Institute official site — locations page opened today: https://pcvi.com/our-locations/eugene-location/
  - Opened 2026-11-07, page crawled less than a minute before opening. The page lists the institute's locations in full:
    - Eugene — 360 S Garden Way #250, Eugene, OR 97401 — Phone: 541-343-5000 — Mon 8:30am–5pm; Tue–Thu 7:30am–5pm; Fri 7:30am–4:30pm.
    - Cottage Grove — 257 N 8th St, Cottage Grove, OR 97424 — Phone: 541-942-5000 — Mon–Thu 8:30 am–5:00 pm; Fri 8:30 am–4:30 pm; Sat–Sun Closed.
  - **No Cottonwood, no Arizona location of any kind, and no (928) number anywhere on the official locations page.** Its NPI record (Pacific Clear Vision Institute, PC, NPI 1699812719) is likewise Eugene, OR only, last updated 06/07/2024. This confirms again today, from the official source, that pcvi.com is NOT the Cottonwood business and must never be used as its website.
- Cottonwood round-up checked today: Optix-now "Best Optometrists & Eye Exams in Cottonwood, AZ" (crawled less than an hour before today's search) lists 2003 E Rodeo Dr ((928) 634-4530), 401 Calvary Way – Ste D ((928) 634-5082), and 199 South Candy Lane Suite 2A ((928) 634-2883) — **Pacific Clear Vision at 294 AZ-89A does not appear**. Absence from a round-up is weak evidence only; it is not a closure notice. Southwestern Eye Center — Cottonwood (official sweye.com, in today's results) is a separate, already-known practice at 270 S. Candy Lane, (928) 634-4202, Mon–Fri 8:00 AM–5:00 PM — no source ties it to Pacific Clear Vision.
- No official website, no BBB profile, no Arizona NPI record, and no hours source for a Cottonwood Pacific Clear Vision were found today. No first-party Cottonwood source exists in today's check.

### Verdict: HELD — needs a phone call (not publishable, not decisively closed)

- **Call (928) 634-2905 — question: "Is Pacific Clear Vision still open at 294 W State Route 89A in Cottonwood as an optometrist, which suite, what are your hours, who is the practitioner, and do you have an official website? Are you affiliated with Pacific ClearVision Institute in Oregon or with Southwestern Eye Center?"**
- Why not publishable: the only verification today is a single place record (address + phone, Active). No hours (none found at all), no website, no practitioner name, no suite, and no second independent source corroborating 294 W SR 89A. Publishing on place data alone would repeat exactly the conflation risk that held it on Day 12.
- Why not decisively closed: the place record still said Active in today's searches, and no source says closed, moved, or succeeded. The Oregon PCVI evidence only disproves the *website/name conflation* — it does not disprove a small, unrelated Cottonwood optometrist trading as "Pacific Clear Vision."
- Directory-only candidate data (DO NOT publish until the call confirms):
  - Pacific Clear Vision — 294 W State Route 89A, Cottonwood, AZ 86326 — (928) 634-2905 — hours: not confirmed / none found — website: none (omit; never pcvi.com).

---

## 3. #141 Alliance Homecare / Valley Respiratory — Cottonwood

- Inventoried: Alliance Homecare / Valley Respiratory — Cottonwood — 1756 E Villa Dr Ste C-9 — (928) 852-0880 — "Home health plus medical equipment."
- Prior hold: official valleyrespiratory.com confirms DME/respiratory only in general, no Cottonwood location/phone listed; place record lists Mon–Thu hours only.
- Task question: does the official site confirm a Cottonwood location, phone, and services today, and what are the real hours?

### What was checked today (2026-11-07)

- Place data via search, 2026-11-07 (identical across the searches run today — "Alliance Homecare Valley Respiratory Cottonwood 1756 E Villa Dr", `"928-852-0880" Alliance Homecare Cottonwood`, `"Alliance Homecare" Cottonwood Arizona Villa Drive reviews`):
  - Alliance Homecare — Address: 1756 E Villa Dr C-9, Cottonwood, AZ, US — Operating Status: Active — Primary Category: Home Health Care Service; Secondary: Medical Equipment Supplier, Medical & Health — Phone: +19288520880 — Website: https://valleyrespiratory.com/ — Hours (America/Phoenix): **Monday–Thursday 9:00 AM–5:00 PM only (no Friday, Saturday, or Sunday listed)** — place_id 581616808342012 — Exact Location: 34.726684, -112.005882.
  - Sibling place record, same searches: Alliance Homecare, Prescott — 3194 Willow Creek Rd, Prescott, AZ, US — Phone: +19287171560 — same website https://valleyrespiratory.com/ — Hours: Monday–Friday 8:30 AM–5:00 PM — description begins "At Valley Healthcare Group, we envision a comprehensive approach to the treatment of respiratory disorders by offering a range of respiratory equipment…" The Cottonwood Mon–Thu pattern is therefore location-specific in place data, not a generic template — **Friday for Cottonwood remains specifically unconfirmed**, and it conflicts with the Mon–Fri pattern of every sibling record found today.
  - Company place records, same day: Valley Respiratory Services, Sun City — 13203 N 103rd Ave, Sun City, AZ — (623) 930-1225 — Mon–Fri 8:30 AM–5:00 PM; Valley Respiratory Services, Mesa — 2330 W Broadway Rd, Mesa, AZ — (480) 830-7700 — Mon–Fri 8:30 AM–5:00 PM. Both use https://valleyrespiratory.com/.
  - No source other than the place record itself ties (928) 852-0880, Ste C-9, or the Mon–Thu hours to this business today — exact-phone and exact-address searches returned the place record and unrelated building tenants only.
- Official site homepage — https://valleyrespiratory.com/
  - Opened 2026-11-07, page crawled less than a minute before opening.
  - Verbatim substance: "Founded in 2006 as a respiratory focused company, we have grown to add other companies to our family – bringing with it diversity in products to a full service DME provider, greater service area and continued excellent service throughout Maricopa, Yavapai, Pima and Pinal counties."
  - "Who We Are: Our licensed respiratory therapists deliver professional setup, patient education, and 24/7 on-call emergency support for a comprehensive range of home medical equipment, including CPAP and BiPAP, oxygen systems, ventilators, nebulizers, airway clearance devices, and continuous glucose monitoring…"
  - **The homepage names no locations, no Cottonwood address, no Ste C-9, and no (928) 852-0880.** Yavapai County (which contains Cottonwood and Prescott) is named as a service county — consistent with a Cottonwood presence, but it is not a location confirmation.
  - Services confirmed first-party today: **DME / respiratory only** — CPAP/BiPAP, oxygen, ventilators, nebulizers, airway clearance, continuous glucose monitoring, licensed respiratory therapists, 24/7 on-call emergency support. No skilled nursing / home-health service is described anywhere on the official homepage.
  - Answering the task question directly: **valleyrespiratory.com does NOT confirm a Cottonwood location, phone, or location-specific services today** — it confirms only that the company is a DME/respiratory provider serving Yavapai County in general. Targeted searches for a valleyrespiratory.com locations/contact page today returned no Cottonwood location page, address, or phone.
- Building check: 1756 E Villa Dr is a real multi-suite complex — today's searches found Aviant Hospice at Ste C-17 ((928) 634-1073; already published in the Gilded Pages), Lavish Body Lounge at Suite C15, Southwest Desert Associates / Thrivent at Suite C12, KPPV Radio at Suite 2C, and Aristocats Studio at Ste B1. **No business other than Alliance Homecare was found claiming Ste C-9, and no source other than Alliance's own place record confirms Alliance in C-9.**

### Verdict: HELD — needs a phone call (not publishable, not decisively closed)

- **Call (928) 852-0880 — question: "Is Alliance Homecare / Valley Respiratory still operating at 1756 E Villa Dr Ste C-9 in Cottonwood, is this the correct phone for that office, are you open Fridays or Monday–Thursday only, and do you provide DME/respiratory equipment only, or also skilled home-health nursing?"**
- Why not publishable: address, suite, phone, and hours are still place-data-only; the official site — the Gilded Pages standard for verification — does not list Cottonwood, C-9, or that phone today. The one piece of data most in doubt (Friday hours) is precisely the piece no source confirms: place says Mon–Thu only while the Prescott sibling and both Valley Respiratory offices list Mon–Fri.
- Why not decisively closed: place data said Active today, the official company is live and explicitly serves Yavapai County, and a Prescott sibling office shows the same Alliance Homecare branding still in use. No closure, move, or succession notice was found.
- Category correction stands: everything official supports **DME / respiratory equipment**, not the inventory's "home health plus medical equipment." If this ever publishes, it belongs as a medical-equipment / respiratory entry (name: Valley Respiratory Services / Alliance Homecare), with no skilled-home-health claim.
- Directory-only candidate data (DO NOT publish until the call / an official location listing confirms):
  - Alliance Homecare (Valley Respiratory Services) — 1756 E Villa Dr Ste C-9, Cottonwood, AZ 86326 — (928) 852-0880 — Mon–Thu 9:00 AM–5:00 PM (Friday: not confirmed — do not state Mon–Fri) — website: https://valleyrespiratory.com/ — category: Medical Equipment / respiratory DME (not Home Health) — services first-party in general (not location-confirmed): CPAP/BiPAP, oxygen, ventilators, nebulizers, airway clearance, continuous glucose monitoring.

---

## Bottom line for Day 35 batch planning

- All three holds survive today's fresh 2026-11-07 check unchanged in kind — each still needs exactly one phone call: **(928) 282-1282** (#24), **(928) 634-2905** (#72), **(928) 852-0880** (#141), with the exact questions stated in each verdict above. No call can be made from this run.
- Do not publish any of the three from directory/place data alone, and do not close/skip any of the three — today's evidence contains no closure, move, or succession statement for any of them.
- Standing cautions, re-confirmed today: do not use (888) 217-4023 for #24; do not use Suite A-3 or D-1 for #24 (Westervelt's and Sedona Dental Arts' suites respectively); do not use pcvi.com for #72; do not state Friday hours for #141; do not describe #141 as skilled home health.
