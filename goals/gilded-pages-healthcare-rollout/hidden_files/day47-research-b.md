# Gilded Pages Healthcare Rollout — Day 47 Research B
## Cottonwood, AZ — 3 businesses
Research date: 2026-11-19 (Arizona time, scheduled run 02:30 MST)
Method: browser.search / browser.open only. No live browser, no phone calls.
Sources are named with URLs for every fact below. "Place listing" means the
Meta / place_id listing returned by search (e.g. https://meta.ai?place_id=…)
— that is a single-source, auto-aggregated listing type, not an official site,
and is treated in this report as weak evidence on its own.

---

## 1. Seaside Serenity — Cottonwood
### Supplied in the task
- Address: 1750 E Villa Dr, Cottonwood, AZ
- Phone: (928) 222-4752
- Category: mental health

### Verdict: HELD — do NOT publish. Probable lead-generation / phantom place pin.
No website, no hours, no second source of any kind was found. The only source
for the business existing at this address, with this phone, in this category,
is one place listing. Everything else at 1750 E Villa Dr is a different,
well-documented business.

### What was found, fact by fact

**Existence / address / phone / category — ONLY source:**
- Place listing "Seaside Serenity", place_id 1676354937199822:
  Address: 1750 E Villa Dr, Cottonwood, AZ, US; Operating Status: Active;
  Open Now: Yes; Primary Category: Mental Health Service;
  Exact Location: 34.726606, -112.00664; Phone: +19282224752;
  Hours: (blank — no hours listed); Website: (none listed).
  Source: browser.search "Seaside Serenity Cottonwood Arizona 1750 E Villa Dr
  mental health", result 0 — https://meta.ai?place_id=1676354937199822
- The identical listing was returned again, unchanged, on a second search
  ("Seaside Serenity Arizona mental health rehab detox", result 0, same
  place_id, same address/phone, hours blank).

**No corroboration anywhere else:**
- Exact-name search `"Seaside Serenity" Cottonwood` returned NO Cottonwood
  mental-health business at all — only unrelated vacation rentals / spas of
  the same name in other places (Marriott Homes & Villas Dunsborough,
  OuterBanks.com Kill Devil Hills NC, Crystal Beach TX, Kahana Reef HI,
  Dubai, Seagrove Beach FL, Koh Samui, Kerikeri NZ, and a day spa booking page).
  Source: browser.search `"Seaside Serenity" Cottonwood`, results 0–9.
- Exact-phone search `"928-222-4752"` returned NO business listing for that
  number — only generic 928 area-code / reverse-lookup spam directories.
  One such directory notes the 928-222 prefix is a Flagstaff (Coconino County)
  rate centre and that "no business listings are currently on file … for
  Flagstaff, AZ" for that prefix — i.e. 928-222 is not a Cottonwood exchange
  on that record.
  Sources: browser.search `"928-222-4752"`, results 0–11; prefix note:
  411FCC, https://www.411fcc.com/az/Flagstaff_6.pdf
- No official website was found. No website is listed in the place listing,
  and no domain, SAMHSA / rehab-directory, Psychology Today, Yelp, BBB,
  Chamber, or licensing record for a Cottonwood "Seaside Serenity" appeared
  in any search run. Website live-status check: not applicable — there is
  no website to check.

**What actually stands at 1750 E Villa Dr — a multi-tenant plaza, and
Seaside Serenity is not among its documented tenants:**
- EDEN (restaurant) — "1750 E Villa Dr, Cottonwood, AZ 86326",
  phone +1 928-649-2675, website http://www.edencottonwood.com/,
  hours Tue–Sat 11 AM–8:30 PM, Sun/Mon closed; "Opened in July of 2023".
  Sources: Tripadvisor, https://Www.tripadvisor.in/Restaurant_Review-g31204-d27264279-Reviews-Eden-Cottonwood_Arizona.html ;
  Wanderlog, https://wanderlog.com/place/details/875311/eden
- Miracle-Ear Hearing Aid Center — "1750 E Villa Dr, Ste E, Cottonwood, AZ
  86326", phone (928) 634-5122 on its official store page, hours
  Mon–Fri 8:00 AM–4:30 PM.
  Source (official): Miracle-Ear,
  https://www.miracle-ear.com/stores-near-me/hearing-aids-cottonwood-az/miracle-ear-hearing-aid-center-e-villa-dr-s10435?source=yelp
  Note a secondary aggregator (findhealthclinics.org) gives a different
  phone, +19287231623, for the same Miracle-Ear suite — a conflict in that
  other business's aggregator data, noted here only to show aggregator
  phone data at this plaza is unreliable.
  Source: https://www.findhealthclinics.org/US/Cottonwood/255017437687304/Miracle-Ear-Hearing-Aid-Center
- Desert Botanical Skin and Wax — "1750 E Villa Dr Ste g, Cottonwood, AZ",
  phone +19283011230, website http://www.desertbotanicalskin.com/,
  with full weekday hours listed.
  Source: place listing returned in browser.search `"1760 E Villa Dr"
  Cottonwood …`, result 2 — http://www.desertbotanicalskin.com/
- At the neighbouring address 1760 E Villa Dr:
  - Desert Foothills Counseling – Cottonwood Clinic, Suite A,
    (928) 646-0347, https://www.desertfoothillscounseling.com —
    described as a state-licensed / ADHS-certified outpatient psychotherapy
    and substance-use clinic. This is the real, documented mental-health
    tenant on Villa Dr, and it is a different business.
    Source: University of Arizona Center for Rural Health,
    https://crh.arizona.edu/desert-foothills-counseling-cottonwood-clinic
  - ABRiO Care formerly listed at "1760 E Villa Dr. Suite F", Cottonwood,
    phone 928-634-6758 (2018 employment listing) — see Business 3 below;
    Abrio is now listed at 830 S Main St. So the Villa Dr plaza has had a
    genuine care tenant, but it was Abrio / Desert Foothills, not Seaside.
    Source: AnyFlip / The Employment Network Magazine, May 18–June 1, 2018,
    https://anyflip.com/nrzr/btyv/basic

**Lead-generation pattern flag — same name, many states, same listing shape:**
- "Seaside Serenity", 817 N Stratford Rd, Moses Lake, WA — Addiction Service /
  Drug Addiction Treatment Center / Rehabilitation Center / Mental Health
  Service, phone +15094924843, no website, no hours. place_id 926427885119349.
- "Seaside Serenity", 1411 NW Valley View Dr, Roseburg, OR — Alcohol
  Addiction Treatment Center, phone +15418978030, no website, no hours.
  place_id 225687387100206.
  Source for both: browser.search `"Seaside Serenity" Arizona mental health
  rehab detox`, results 1–2 — https://meta.ai?place_id=926427885119349 and
  https://meta.ai?place_id=225687387100206
- Pattern: an identical, evocative rehab-style name pinned in unrelated
  towns in at least three states, each with a different local-looking phone,
  no website, no hours, no reviews, no licensing or directory record. That is
  the classic shape of auto-generated / lead-generation place pins, not of a
  real multi-state chain (a real chain would have a website and a shared
  admissions number — compare Serenity Mental Health Centers and Serenity
  Lane, both of which have official sites, shared numbers and directory
  records, and neither of which lists a Cottonwood "Seaside Serenity").

**Services:** None verifiable. The place listing gives only the category
"Mental Health Service". No service list, staff, licence, or programme
description exists in any source found. Do not invent services for this entry.

**Hours:** None in any source. Place listing hours field is blank.

### Recommendation for Business 1
- **HELD (phone check + existence check required before any publication).**
  Do not publish address, phone, hours or website — none is verified.
- If a phone check is made, it must first establish that a business of this
  exact name answers at (928) 222-4752 and physically operates at
  1750 E Villa Dr, Cottonwood — and which suite. Without that, this should
  be closed as unverifiable / probable phantom listing, in line with the
  rollout rule to skip unverifiable entries.
- Recommended publishable data: **none at this time.**

---

## 2. Bearing Detox Solution — Cottonwood
### Supplied in the task
- Address: 830 S Main St, Cottonwood, AZ
- Phone: (928) 328-1440
- Category: mental health / detox
- Task note: 830 S Main St is also given for VIP Dentistry AZ and Abrio
  Home Care — check what actually stands there. (Answered below: 830 S Main
  St is a multi-tenant office building; VIP Dentistry Suite 1D and Abrio
  Suite 2C are documented there. Bearing Detox is not documented there by
  any source except its own single place pin.)

### Verdict: HELD — do NOT publish. Probable lead-generation place pin
### belonging to the "Bearing" rehab lead-gen family.
Same evidentiary problem as Business 1, plus a direct link-by-pattern to a
generic rehab lead-generation website (bearinginstitute.org).

### What was found, fact by fact

**Existence / address / phone / category — ONLY source:**
- Place listing "Bearing Detox Solution", place_id 3021365748201669:
  Address: 830 S Main St, Cottonwood, AZ, US; Operating Status: Active;
  Open Now: Yes; Primary Category: Mental Health Service;
  Exact Location: 34.724389, -112.007165; Phone: +19283281440;
  Hours: (blank); Website: (none listed).
  Source: browser.search "Bearing Detox Solution Cottonwood 830 S Main St",
  result 0 — https://meta.ai?place_id=3021365748201669
  (returned identically on the `"Bearing Detox" Arizona rehab` search.)

**No corroboration anywhere else:**
- Exact-name search `"Bearing Detox Solution"` returned NO business result
  at all — only patents and forum posts about purging grease from mechanical
  bearings. A real, operating detox facility would be expected to appear in
  at least one rehab directory, licensing list, review site or its own site.
  Source: browser.search `"Bearing Detox Solution"`, results 0–4.
- Exact-phone search `"928-328-1440"` returned NO business listing for that
  number — only generic 928 reverse-lookup spam directories.
  Source: browser.search `"928-328-1440"`, results 0–11.
- No official website for "Bearing Detox Solution" was found, and none is
  listed in its place pin. Website live-status check: not applicable for
  this business itself. The related lead-gen site bearinginstitute.org WAS
  checked live — see below.

**The "Bearing" family — the lead-generation pattern, documented:**
- "Bearing Detox Support", 7424 Bridgeport Way SW, Lakewood, WA —
  Mental Health Service, phone +12532705197,
  Website: https://www.bearinginstitute.org/, hours blank.
- "Bearing Detox Information", 405 Londonderry Dr, Waco, TX —
  Mental Health Service, phone +12542276170,
  Website: https://www.bearinginstitute.org/, hours blank.
  Source for both: browser.search `"Bearing Detox" Arizona rehab`,
  results 2–3 — https://www.bearinginstitute.org/
- The Cottonwood pin follows the same template exactly (Bearing Detox +
  a generic third word — Solution / Support / Information — a local-looking
  phone, a pin dropped on a real building in a new town, no hours), except
  the Cottonwood pin does not even carry the bearinginstitute.org website.
- bearinginstitute.org checked live by browser.open on 2026-11-19:
  https://www.bearinginstitute.org/ — the site is live and is a generic
  drug-rehab content / lead-generation site: boilerplate addiction-treatment
  text ("While you are going through the throes of drug addiction…"),
  sections headed DETOX / DUAL DIAGNOSIS / ALCOHOL, stock images dated
  2016 in its image paths, and a single call-to-action number,
  **(877) 448-7406** — which is NOT (928) 328-1440. The homepage names no
  Cottonwood facility, no Arizona address, and no "Bearing Detox Solution".
  Source: browser.open https://www.bearinginstitute.org/ (crawled
  2026-11-19 09:31 UTC).

**What actually stands at 830 S Main St, Cottonwood — a multi-tenant
office building ("Cottonwood Financial Center"):**
- Building name: "Cottonwood Financial Center", 830 S Main St, Cottonwood,
  AZ — Primary Category: Business Center, place_id 1280752847196649,
  Exact Location 34.724578, -112.007223 (essentially the same coordinates
  as the Abrio and VIP pins — one building, many suites).
  Source: browser.search `"830 S Main St" Cottonwood AZ businesses`,
  result 1 — https://meta.ai?place_id=1280752847196649
- VIP Dentistry AZ / VIP Family and Sedation Dentistry — **Suite 1D**
  (documented tenant, see detail below).
- Abrio Home Care Cottonwood — **Suite 2C** (documented tenant, Business 3).
- Vacte (Valley Academy for Career and Technology Education) — 830 S Main St,
  phone +19286347131, website http://www.vacte.com/, category Trade School.
  Source: browser.search `"830 S Main St" Cottonwood AZ businesses`, result 2.
- Art Paint Draw — 830 S Main St **#2A**, phone +19282121363,
  website http://artpaintdraw.com/, hours Tue–Sat 11:30 AM–4:00 PM.
  Source: same search, result 0 — http://artpaintdraw.com/
- Other suite tenants evidenced at the same street address in other
  listings: SunCore Power, 830 South Main Street, Unit 2E, (602) 422-6142
  (Manta); CBM Marketing Solutions, 830 South Main Street, Suite 2i
  (press release, 2025 — that release also garbles the town as "Clarkdale",
  a further sign of sloppy aggregator data at this address).
  Sources: Manta, https://www.manta.com/mb_44_E51B1_03/heating_equipment_except_electric_and_warm_air_furnaces/arizona ;
  PressAdvantage, https://pressadvantage.com/pdf/81183-cbm-marketing-solutions-launches-nationwide-with-free-marketing-suite-pioneers-aibpo-to-level-the-pl/
- Long-standing dental use of the building: NPI registry record for
  COTTONWOOD DENTAL ASSOCIATES PLLC lists both mailing and location address
  as 830 S MAIN ST, COTTONWOOD, AZ 86326-4620, phone 928-634-5566,
  record last updated 02/04/2016 — the same phone VIP Dentistry uses today.
  Source: datalabs.health NPI 1043678055,
  https://www.datalabs.health/medical_billing/coding/national_provider_identifier/codes/npi_1043678055.pdf
- **No source other than its own place pin places Bearing Detox Solution
  in this building — no suite number, no signage/directory listing, no
  licence, no directory entry.** A detox / mental-health facility is a
  licensed, high-footprint use; its total absence from every rehab
  directory searched (Rehab.com, Recovery.com, DetoxLocal, SAMHSA-derived
  listings all returned other Arizona facilities, never this one) is
  material negative evidence.
  Sources: browser.search `"Bearing Detox" Arizona rehab` and
  "Bearing Detox Solution Cottonwood 830 S Main St" — results reviewed in
  full; no rehab-directory hit names this business.

**VIP Dentistry AZ — verified, for the address-conflict record:**
- Place listing: VIP Dentistry AZ, 830 S Main St, Cottonwood, AZ, Active,
  phone +19286345566, website https://www.vipdentistryaz.com/,
  hours Mon–Thu 8:00 AM–4:00 PM, Fri 8:00 AM–3:00 PM,
  "Family, cosmetic & implant dentistry … Accepting new patients …
  Hablamos español!"
  Source: browser.search "VIP Dentistry AZ Cottonwood 830 S Main St",
  result 0 — https://www.vipdentistryaz.com/
- Official site checked live by browser.open on 2026-11-19:
  https://www.vipdentistryaz.com/ — live; title "VIP Family and Sedation
  Dentistry"; states "830 S Main St, Suite 1D Cottonwood AZ United States
  86326", "PHONE: (928) 634-5566", "FAX: (928)634-1363",
  "OPENING HOURS Mon - Fri: 8am - 5pm, Sat: By Appointment Only, Sun: Closed",
  services: sedation & sleep dentistry / IV sedation, dental surgery
  (wisdom tooth removal, bone grafts, complicated extractions, root canals),
  accepts AHCCCS, Health Choice, Care 1st, United Health Care; "Serving
  Patients Since 2010".
  Note the small hours conflict: the place listing says Mon–Thu to 4 PM /
  Fri to 3 PM, the official site says Mon–Fri 8 AM–5 PM. The official site
  governs for VIP's own entry (a separate rollout entry, not this one).
  Independent corroboration of Suite 1D: WebMD lists Dr. Massoud Eftekhari
  at "830 S Main St Ste 1D, Cottonwood, AZ, 86326".
  Source: https://doctor.webmd.com/providers/specialty/dentistry/arizona/cottonwood

**Services (Bearing Detox):** None verifiable. Only the place-pin category
"Mental Health Service" and the word "Detox" in the name. No detox level,
no licence type, no programme description exists in any source.

**Hours (Bearing Detox):** None in any source. Place listing hours blank.
Do NOT infer 24-hour detox hours — nothing supports that.

### Recommendation for Business 2
- **HELD (existence / phone check required; strong lead-generation flags).**
  Do not publish. If the phone check to (928) 328-1440 does not reach a
  facility of this exact name physically operating at 830 S Main St with a
  suite number and an Arizona licence, close it as a phantom / lead-gen pin.
- Recommended publishable data: **none at this time.**
- Address note for the rollout record: 830 S Main St is NOT a single-business
  address. Any entry using it must carry its suite (VIP = Suite 1D,
  Abrio = Suite 2C) to be accurate.

---

## 3. Abrio Home Care Cottonwood (ABRiO Care / Abrio Home Care)
### Supplied in the task
- Address: 830 S Main St, Cottonwood, AZ
- Phone: (928) 634-6758
- Category: home health

### Verdict: PUBLISHABLE — with the suite added and one wording correction.
Real, long-established Arizona company; Cottonwood office corroborated by
two independent sources giving the same address and the same local phone;
official website live and checked. Correction: it is **non-medical home
care**, not skilled "home health" — publish under home care, with services
worded as the company words them.

### What was found, fact by fact

**Existence / status — corroborated, long-running:**
- Place listing "Abrio Home Care Cottonwood", place_id 5710933458919095:
  Address: 830 S Main St, Cottonwood, AZ, US; Operating Status: Active;
  Primary Category: Home Health Care Service; Secondary: Local Service,
  In-Home Service; Exact Location: 34.724609, -112.007321;
  Phone: +19286346758; Website: https://abriohomecare.com/;
  Hours: Mon–Fri 8:00 AM–5:00 PM (America/Phoenix).
  Description (company's own words, carried in the listing): "Woman- and
  veteran-owned, Abrio Home Care is deeply rooted in the communities we
  serve and has been meeting the needs of Arizona families for over 25
  years. We have earned an A+ rating with the Better Business Bureau and
  are members of the Home Care Association of America… seven local offices
  located around the state… 24/7 access to quality in-home care services…"
  Source: browser.search "Abrio Home Care Cottonwood Arizona 830 S Main St",
  result 0 — https://abriohomecare.com/
- Independent corroboration of the exact Cottonwood address, suite AND phone:
  Prism Network resource / employment listing (source noted on the page:
  Yavapai College Job Fairs), crawled 1 day before this research:
  "ABRiO Care Home Care — Hiring: Caregivers — 830 S. Main Street,
  Suite 2C, Cottonwood, AZ 86326 — Call 928-634-6758".
  Source: https://www.prismaz.net/blog-posts/resources-and-employment-opportunities
- Historical continuity of the same Cottonwood office and the same phone:
  a May 2018 employment listing gives ABRiO Care Cottonwood at the OLD
  address "1760 E Villa Dr. Suite F" with phone 928-634-6758, alongside
  Prescott Valley (2485 Great Western, Suite G-2, 928-772-8866) and
  Flagstaff offices. Read together with the current listings, this shows
  the Cottonwood office **moved from 1760 E Villa Dr Suite F to
  830 S Main St Suite 2C, keeping its local number** — it is a relocation,
  not a closure, and it explains why older directories still show Villa Dr.
  Source: AnyFlip / The Employment Network Magazine, May 18–June 1, 2018,
  https://anyflip.com/nrzr/btyv/basic

**Address — recommended form:**
- **830 S Main St, Suite 2C, Cottonwood, AZ 86326**
- Base address + phone from the place listing (above); suite 2C from Prism
  Network (above). ZIP 86326 from the Prism listing and from the NPI /
  WebMD records for the same building.
- Conflict / stale addresses to NOT use, with reasons:
  - 1760 E Villa Dr, Cottonwood, AZ 86326 — OLD Cottonwood office address.
    Sources still carrying it: AgingCare "Abrio Home Care of AZ",
    https://www.agingcare.com/local/abrio-home-care-of-az-cottonwood-in-home-care-az ;
    Caring.com "Abrio Care – Cottonwood" (its review on that page is dated
    May 2, 2013), https://www.caring.com/senior-care/arizona/cottonwood/abrio-care-cottonwood .
    Superseded by the 830 S Main St / Suite 2C records above.
  - 821 N Main St Ste A, Cottonwood, AZ 86326 — appears in an AI-generated
    company profile for a differently-named entity ("Abri Health Care",
    described as home health / hospice / palliative, CHAP-accredited).
    That is a conflation with a different company and does NOT match
    Abrio Home Care's own site, phone or history. Do not use.
    Source: https://www.highperformr.ai/company/abrihealthcare
  - Prescott Valley is the nearby sister office, not the Cottonwood office:
    "Abrio Home Care, 2485 N Great Western Dr, Prescott Valley, AZ",
    phone +19287728866, hours Mon–Fri 8 AM–5 PM; recent company posts give
    a Yavapai County team number 928-772-1711 serving "Cottonwood,
    Prescott Valley, Sedona, and surrounding communities". These Prescott
    numbers must not be substituted for the Cottonwood number
    (928) 634-6758, which is the number tied to the Cottonwood address by
    both the place listing and Prism.
    Sources: place listing in browser.search "Abrio Home Care locations
    Cottonwood Prescott Valley official site", result 1 —
    https://abriohomecare.com/ ; findhealthclinics.org ABRiO pages,
    https://www.findhealthclinics.org/US/Kingman/104443718911468/ABRiO-Care

**Phone — recommended:**
- **(928) 634-6758** (Cottonwood office) — place listing + Prism Network,
  two independent sources, and the same number the office used at its old
  Villa Dr address in 2018.
- Company-wide number on the official site: 877-71-ABRIO / 877-712-2746.
  Source: browser.open https://abriohomecare.com/ (below). Publish the
  local Cottonwood number as the entry phone; the toll-free number may be
  noted as the company's central number.

**Website — live, checked:**
- https://abriohomecare.com/ — opened by browser.open on 2026-11-19
  (crawled 2026-11-19 09:31 UTC): live, current (blog posts dated
  Nov 03, Sep 02, Jul 07, 2026 on the homepage), states "Woman- and
  veteran-owned… meeting the needs of families in Phoenix, Yuma, Mesa,
  Kingman, Prescott, and communities throughout Arizona for over 25
  years… compassionate, reliable, and customized home care services for
  older adults and people with developmental disabilities", carries BBB
  A+ and Home Care Association of America marks, and gives HQ as
  "Abrio Home Care, 4736 N 12th St, Phoenix, AZ 85014", phone 877-712-2746.
  Source: browser.open https://abriohomecare.com/
- Note: the official site's homepage / service pages do NOT list the
  Cottonwood street address or the local 928-634-6758 number — they route
  enquiries through the toll-free number and list service towns (Phoenix,
  Mesa, Kingman, Yuma, Prescott / Prescott Valley, Tucson, Flagstaff
  "and throughout Arizona"). The Cottonwood office address therefore rests
  on the place listing + Prism, not on the official site. That is enough
  to publish (two independent sources, same address, same phone), and the
  limitation is recorded here plainly.
  Source: browser.open https://abriohomecare.com/ and
  https://abriohomecare.com/services/personal-care/ (both 2026-11-19).

**Hours — recommended:**
- **Monday–Friday 8:00 AM–5:00 PM** (office hours) — place listing for the
  Cottonwood office; the same Mon–Fri 8–5 pattern is listed for Abrio's
  Phoenix and Prescott Valley offices, which supports it as the company's
  standard office hours.
  Sources: Cottonwood, Phoenix and Prescott Valley place listings in
  browser.search "Abrio Home Care Cottonwood Arizona 830 S Main St" and
  "Abrio Home Care locations Cottonwood Prescott Valley official site" —
  https://abriohomecare.com/
- Care itself is described by the company as available 24/7 ("we offer
  24/7 access to quality in-home care services") — if the entry mentions
  this, word it as 24/7 access to care, NOT as office hours.
  Source: company description in the Cottonwood place listing (above).

**Services — from the company's own words:**
- From the Cottonwood place-listing description: personal care, meal prep
  and housekeeping, companionship, transportation, medication management,
  habilitation and life skills development, and respite care; care team of
  home health aides, certified nursing assistants, care managers and home
  care experts, bonded, insured, certified under the Arizona Direct Care
  Worker certification; for aging adults and people with developmental
  disabilities.
  Source: browser.search "Abrio Home Care Cottonwood Arizona 830 S Main St",
  result 0 — https://abriohomecare.com/
- From the official site, Personal Care page (opened 2026-11-19):
  support with bathing, personal hygiene, dressing and safety supervision;
  meal planning/preparation and help with eating; doctor-approved exercise
  plans; light housekeeping, bed-making, linens and laundry; transportation
  to appointments and social outings; errands, grocery shopping and
  prescription pickups; companionship; medication reminders. The page
  expressly distinguishes this from medical care: "Unlike medical care,
  which focuses on treating health conditions, personal care focuses on
  helping with the activities of daily living…"
  Source: browser.open https://abriohomecare.com/services/personal-care/
- Category correction for the Gilded Pages entry: list as **home care
  (non-medical in-home care)**. The supplied category "home health" and the
  place listing's "Home Health Care Service" label overstate it — Abrio's
  own site describes non-medical personal / companion care, transportation
  and respite, not skilled nursing / therapy home health. Do not claim
  skilled medical home-health services for this entry.
- Other directory presence (existence support only, no new facts relied on):
  AgingCare lists "Abrio Home Care of AZ" as a Cottonwood in-home care
  provider, https://www.agingcare.com/local/in-home-care/cottonwood-az ;
  Caring.com carries Abrio reviews for Cottonwood (old address, see above).

**Closed / moved status:** Not closed. **Moved within Cottonwood** —
from 1760 E Villa Dr Suite F (2018 and earlier) to 830 S Main St Suite 2C
(current). Publish only the current address.

### Recommendation for Business 3
- **PUBLISHABLE.**
- Publish as: **Abrio Home Care Cottonwood — 830 S Main St, Suite 2C,
  Cottonwood, AZ 86326 — (928) 634-6758 — Mon–Fri 8:00 AM–5:00 PM —
  https://abriohomecare.com/** — category: home care.
- Note in the entry, if a note field is used, that care/access is offered
  24/7 by the company while the office hours above are Mon–Fri 8–5, and
  that the central company number is 877-712-2746.

---

## Cross-cutting findings for the Day 47 batch

1. **830 S Main St is one multi-tenant office building** (Cottonwood
   Financial Center / Business Center). Documented healthcare tenants:
   VIP Family and Sedation Dentistry, Suite 1D, (928) 634-5566,
   https://www.vipdentistryaz.com/ (official site live, checked
   2026-11-19); Abrio Home Care, Suite 2C, (928) 634-6758. Other documented
   tenants include VACTE, Art Paint Draw (#2A), SunCore Power (Unit 2E).
   Any Gilded Pages entry at this address without a suite is incomplete.
2. **1750 / 1760 E Villa Dr is another multi-tenant plaza.** Documented
   tenants: EDEN restaurant (1750), Miracle-Ear Ste E (1750),
   Desert Botanical Skin and Wax Ste G (1750), Desert Foothills Counseling
   Ste A (1760), and formerly Abrio Ste F (1760, moved out). Neither
   "Seaside Serenity" nor any other new mental-health business is
   documented there.
3. **A repeated phantom-pin pattern affects this batch:** two of the three
   names (Seaside Serenity, Bearing Detox Solution) exist ONLY as single
   place pins with a local-looking phone, no website, no hours, no reviews,
   no licence and no directory record — and each name has sibling pins of
   the identical template in other states (Seaside Serenity in WA and OR;
   Bearing Detox Support in WA and Bearing Detox Information in TX, the
   latter two pointing at the generic lead-gen site bearinginstitute.org,
   whose own phone is (877) 448-7406 and which names no local facility).
   Treat any further Day-batch names with this exact profile (place pin
   only, blank hours, no website) as held pending a phone/existence check,
   not as publishable finds.
4. **Aggregator phone/address data at both plazas is demonstrably sloppy**
   (e.g. a second, conflicting phone for Miracle-Ear in one aggregator; a
   press release garbling 830 S Main St's town as Clarkdale; an AI profile
   inventing an 821 N Main St address for a conflated "Abri Health Care").
   For these two addresses, only facts carried by an official site or by
   two independent sources were treated as verified in this report.

## Sources index (URLs as returned by search / open — verbatim)
- Seaside Serenity place listing: https://meta.ai?place_id=1676354937199822
- Bearing Detox Solution place listing: https://meta.ai?place_id=3021365748201669
- Bearing Institute (live, opened): https://www.bearinginstitute.org/
- Abrio Home Care Cottonwood place listing / official site: https://abriohomecare.com/
- Abrio Personal Care (official, opened): https://abriohomecare.com/services/personal-care/
- Prism Network (Abrio Suite 2C + phone): https://www.prismaz.net/blog-posts/resources-and-employment-opportunities
- 2018 Abrio Cottonwood (old address, same phone): https://anyflip.com/nrzr/btyv/basic
- VIP Dentistry (official, opened): https://www.vipdentistryaz.com/
- VIP Suite 1D corroboration: https://doctor.webmd.com/providers/specialty/dentistry/arizona/cottonwood
- NPI record, 830 S Main dental history: https://www.datalabs.health/medical_billing/coding/national_provider_identifier/codes/npi_1043678055.pdf
- Desert Foothills Counseling, 1760 E Villa Dr Ste A: https://crh.arizona.edu/desert-foothills-counseling-cottonwood-clinic
- Miracle-Ear Cottonwood (official): https://www.miracle-ear.com/stores-near-me/hearing-aids-cottonwood-az/miracle-ear-hearing-aid-center-e-villa-dr-s10435?source=yelp
- EDEN, 1750 E Villa Dr: https://wanderlog.com/place/details/875311/eden and https://Www.tripadvisor.in/Restaurant_Review-g31204-d27264279-Reviews-Eden-Cottonwood_Arizona.html
- AgingCare (old Abrio address): https://www.agingcare.com/local/abrio-home-care-of-az-cottonwood-in-home-care-az
- Caring.com (old Abrio address): https://www.caring.com/senior-care/arizona/cottonwood/abrio-care-cottonwood
