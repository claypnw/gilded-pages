# Day 41 — Step-14 New-Names Check, PART A — 2026-11-13
Towns covered: Payson, Star Valley, Pine/Strawberry, Camp Verde, Sedona.
Method: narrow browser.search searches per town across the directory's kinds (hospitals, urgent care, clinics, dental, pharmacies, vision, mental health and recovery, home health, hospice, physical therapy, medical equipment, hearing, nursing/rehab, labs, imaging). Every name found was checked by grep against BOTH standing records: ~/workspace/gilded-pages/healthcare-inventory-draft.md (480 entries through Day 40) and ~/workspace/gilded-pages/healthcare-progress.md (published + held entries). A name in either file is NOT new. Searches and name-matching only — no verification, no phone calls, nothing published.
PART A RESULT: 8 new names (Payson 4, Star Valley 0, Pine/Strawberry 0, Camp Verde 1, Sedona 3).

---

## PAYSON — 4 new

### Searches run
1. "Payson Arizona new clinic dental pharmacy opened 2026"
2. "Payson AZ physical therapy hearing home health hospice medical"
3. "Payson Arizona mental health counseling therapy clinic"
4. "Payson AZ vision eye care optometrist hearing aid medical equipment lab"
5. "Payson Arizona assisted living nursing home senior care"

### NEW names
- **Navis-Schmidt Penny (Penny Navis-Schmidt)** — Payson — 700 W Main St — mental health (counselor) — (928) 474-8628. [NEW FIND 2026-11-13] Solo counselor place record; no match in either standing file (name or phone).
- **Martinez Lori A (Lori A. Martinez)** — Payson — 700 W Main St — mental health (counselor) — (928) 970-1967. [NEW FIND 2026-11-13] Solo counselor at the same address as the Navis-Schmidt record, different person and phone; no match in either standing file.
- **Southwest Behavioral & Health Services – Stageline Rd location** — Payson — 8985 Stageline Rd — mental health — (928) 468-2399. [NEW FIND 2026-11-13] New location of a published name: the published entries cover Aero Outpatient (404 W Aero Dr) and the Prescott Valley outpatient office only; no Stageline Rd address or this phone stands in either file. FLAG: the listing's website points to the Aero Outpatient page — the service type at this address (residential vs outpatient) is to settle at batch time.
- **The Beehive Villa** — Payson — 1409 E Graham Rnch Trl — nursing / assisted living — (480) 234-4389. [NEW FIND 2026-11-13] FLAG: place record only; its listed website is Vrbo, which suggests a possible vacation-rental mislabel — verify at batch time whether it is a public-facing assisted-living home.

### Found and rejected as already listed
- Anderson Dental Group (712 N Beeline Hwy) — inventory #1; Day 1 emergency-dental entry.
- Payson Premier Dental (409 W Main St) — inventory #2; published big-payson-premier-dental.
- Bonanza Square Dentistry (200 W Frontier St #5) — inventory #9; published big-bonanza-dental.
- Lone Tooth — inventory #11; held unverifiable in the progress file (no street address).
- Mattern Thomas DDS and Wilson Gustavo DDS (both 409 W Main St A, (928) 472-8400) — individual dentists at Payson Premier Dental's own address and phone; the practice is already published, providers are not separate entries.
- Genoa Healthcare (404 W Aero Dr) — NEW FIND 2026-11-07; published big-genoa-healthcare.
- **Qol Meds (404 W Aero Dr, (928) 468-6703)** — REJECTED: the published Genoa Healthcare entry (progress file) names Qol Meds as its predecessor at this site and flags this exact listing as the stale one. Not a separate business.
- Arizona Care Hospice (1100 N Beeline Hwy) — inventory #122; published big-arizona-care-hospice.
- Valley Hospice of Arizona (126 E Main St) — inventory #123; held unverified in the progress file.
- Hospice of Payson (900 N Beeline Hwy) — inventory #121; published big-hospice-of-payson.
- Compassus – Payson (511 S Mud Springs Rd) — inventory #120; published big-compassus.
- Hospice Rta Operations (107 E Frontier St) — NEW FIND 2026-11-10.
- Banner Physical Therapy – Payson Medical Center (126 E Main St Ste C) — inventory #210; published big-banner-physical-therapy.
- Payson Physical Therapy (405 W Main St), incl. its provider records Tenney Jared / Tiffany Deborah / Foote Stacey at Ste D — inventory #211; published big-payson-physical-therapy.
- Banner Home Care (708 E Route 260 Ste A1) — NEW FIND 2026-11-07.
- Comfort Keepers Home Care (200 W Frontier St Ste K) — NEW FIND 2026-11-07.
- Preferred Homecare (119 W Aero Dr) — inventory #124; published big-preferred-homecare.
- AccentCare Personal Care Services (200 W Frontier St Ste G) — inventory #125; published big-accentcare.
- SYNERGY HomeCare of Payson — NEW FIND 2026-11-07.
- Southwest Behavioral & Health Services – Aero Outpatient and Empowerment Center (404 W Aero Dr) — inventory #91; published big-southwest-behavioral.
- Psych Assist (405 W Main St Ste B), incl. provider record Carissa J Higgins at the same address/phone — inventory #94; published big-psych-assist.
- Fitz Ilias (600 AZ-260 #2) — NEW FIND 2026-11-07.
- Caring Connections For Special Needs / CCSN (708 E AZ-260) — NEW FIND 2026-11-08.
- Steckal Donna PHD (616 S Beeline Hwy #107) — NEW FIND 2026-11-11.
- Gabbert Medical (120 E Main St Ste B) — NEW FIND 2026-11-07.
- Joanna Linn (126 E Main St B, (928) 468-8610) — REJECTED: that address and phone are the published Elk Ridge Community Health hall (big-elk-ridge-health, formerly North Country HealthCare); a provider inside an already-published practice, not a separate entry.
- Ketamine Evaluations (listing address garbled — 9375 E Shea Blvd is a Scottsdale address placed in Payson; phone (480) 788-6070 matches Fitz Ilias's line) — REJECTED: no verifiable Payson storefront in the snippet; record too corrupt to join the list.
- Payson Eye Care Center / Dr. Jonathan Beeson (411 S Beeline Hwy) — inventory #58; published big-payson-eye-care.
- Risser Thomas Eye Clinic (302 W Main St) — inventory #59; published big-risser-thomas-eye.
- Alpine Optical / Arizona Optical Disp (302 W Main St) — inventory #60; published big-alpine-optical.
- Walmart Vision & Glasses (300 N Beeline Hwy) — inventory #61; published big-walmart-vision.
- Apple Valley Vision — NEW FIND 2026-11-08.
- Miracle-Ear Hearing Aid Center (1107 S Beeline Hwy Ste 3) — NEW FIND 2026-11-08; published big-miracle-ear.
- Sonora Quest Laboratories (117 E Main St Bldg C) — inventory #126; published big-sonora-quest.
- Patient's Choice Lab Testing & Blood Draw Services (708 S Coeur D Alene Ln Ste A) — NEW FIND 2026-11-09.
- Payson Care Center (107 E Lone Pine Dr) — NEW FIND 2026-11-09.
- Rim Country Health & Rehabilitation (807 W Longhorn Rd) — NEW FIND 2026-11-09.
- Majestic Rim Retirement Living (310 E Tyler Pkwy) — NEW FIND 2026-11-12.
- Avista Senior Living Payson (806 W Longhorn Rd) — NEW FIND 2026-11-12.
- Ordinary Lifestyles (205 W Bonita St) — NEW FIND 2026-11-12.
- Gila Social Services (807 W Longhorn Rd, (928) 468-0546) — REJECTED: a county senior/social service co-located inside the already-listed Rim Country Health campus, not a healthcare provider of a kind this directory lists.
- The Payson Senior Center (514 W Main St) — REJECTED: community senior center, not a healthcare business of a listed kind (same treatment as prior days).

---

## STAR VALLEY — 0 new

### Searches run
1. "Star Valley Arizona healthcare clinic pharmacy"
2. "Star Valley AZ dentist doctor pharmacy health"

### NEW names
- None.

### Found and rejected
- Star Valley Veterinary Clinic (103 Walters Ln) — veterinary, out of scope (appears in every Star Valley search; never a human-healthcare entry).
- All other hits were Payson businesses 4–5 miles away, already listed there: Genoa Healthcare, Qol Meds (see Payson), Amalia Pineres / IMS (111 W Cedar Ln — the IMS practice, inventory #174, published big-integrated-medical-services; the admin-held Alma Medical Clinic is a different record), Wilson Gustavo DDS and Diquattro Ryan DDS (Payson Premier / published big-diquattro-dental), Dr. Flaherty / Center Point Dental (Day 1 entry), Walgreens Payson (Day 1 pharmacy entry), Bonanza Square Dentistry, Lone Tooth.
- Standing position unchanged: Star Valley has zero human-healthcare businesses on the list, and tonight's searches found none.

---

## PINE / STRAWBERRY — 0 new

### Searches run
1. "Pine Strawberry Arizona clinic dental medical healthcare"
2. "\"Pine\" Arizona dentist doctor clinic Fossil Creek"

### NEW names
- None.

### Found and rejected
- Banner Health Clinic – Pine (6152 Hardscrabble Mesa Rd) — inventory #183; published big-banner-pine.
- Dr. Donald L. Smith, DDS (Pine) — inventory #14; published big-donald-smith-dds. (Tonight's searches did not surface him by name, but he stands published; no second Pine dental practice appeared.)
- Angulo Dental "Pine, AZ" page — REJECTED: SEO lead-gen page with an Alabama (205) phone number and no Pine storefront; not a real Pine business record.
- Pine Dental & Aesthetics — REJECTED: a United Kingdom practice (CQC-registered, Dr. Zara Adnan Malik) matched on the word "Pine" only; not in Arizona.
- Remaining hits were out-of-area (Phoenix, Scottsdale, Flagstaff, Prescott, Pinetop) or veterinary (Pine Country Animal Clinic — Payson address, veterinary, out of scope).

---

## CAMP VERDE — 1 new

### Searches run
1. "Camp Verde Arizona clinic dental pharmacy urgent care healthcare"
2. "Camp Verde AZ physical therapy home health mental health medical"
3. "Camp Verde AZ eye care vision hearing aid clinic"

### NEW names
- **Hope Women's Center** — Camp Verde — 77 W General Crook Trail — clinic (women's health / pregnancy care center) — (928) 651-9266. [NEW FIND 2026-11-13] Nonprofit women's health clinic; no match in either standing file (name or phone). Note: 77 W General Crook Trail is also Copper Canyon Family Dental's stale inventory address — the dental practice has since moved (published at 26 W Salt Mine Rd), so no address conflict with a current entry.

### Found and rejected as already listed
- Northern Arizona Healthcare Medical Group – Camp Verde / NAH Urgent Care & Immediate Care (1298 Finnie Flat Rd, (928) 639-5555) — inventory #184; published big-nah-camp-verde, whose entry already notes the Lab + Immediate Care housed in the same building. The urgent-care listing is the same hall, not a separate entry.
- Copper Canyon Family Dental — inventory #16; published big-copper-canyon-dental.
- Walgreens – Camp Verde (475 W Finnie Flat Rd) — NEW FIND 2026-11-07.
- CVS Pharmacy – Camp Verde (522 W Finnie Flat Rd) — NEW FIND 2026-11-07.
- Haven of Camp Verde (86 W Salt Mine Rd) — NEW FIND 2026-11-08; published big-haven-camp-verde.
- Haven Health Camp Verde Assisted Living (86 W Salt Mine Rd Ste A, (928) 567-5777) — REJECTED: the published big-haven-camp-verde entry already notes the separate assisted-living service at the same address; covered, not a new name.
- EntireCare Rehab and Sports Medicine – Camp Verde (1298 Finnie Flat Rd) — NEW FIND 2026-11-08; published big-entirecare-camp-verde.
- Diamond D Rehab, Fitness and Wellness (27 W General Crook Trail) — inventory #213; published big-diamond-d-rehab.
- Central Arizona Sports and Physical Therapy (155 S Montezuma Castle Hwy Ste 2) — inventory #212; published big-central-arizona-pt.
- Polara Health – Camp Verde Clinic (434 S Main St #3) — inventory #98; published big-polara-camp-verde.
- Caring Hearts In-Home Care (976 Esther Pkwy) — NEW FIND 2026-11-09.
- Camp Verde Eye Care (452 W Finnie Flat Rd) — inventory #63; published big-camp-verde-eye-care.
- Dr. David Sherman Deutch, MD (1298 W Finnie Flat Rd Ste 101, WebMD ophthalmology listing) — REJECTED: an individual physician listing inside the already-published NAH Camp Verde building; no separate practice name, address, or phone in the snippet.
- "Camp Verde Health Center" — REJECTED as unverified: the name appears only as a passing mention in a Sofia Health listicle with no address, phone, or place record in any search tonight; nothing solid enough to join the list.
- Veterinary hits (Anasazi Animal Clinic, Montezuma Veterinary Services, Complete Pet Care) — out of scope.

---

## SEDONA — 3 new

### Searches run
1. "Sedona Arizona new clinic dental pharmacy opened healthcare"
2. "Sedona AZ physical therapy vision hearing home health hospice mental health"
3. "Sedona Arizona urgent care medical clinic Village of Oak Creek"
4. "Sedona Arizona counseling therapy recovery treatment center"

### NEW names
- **Village of Oak Creek Health** — Sedona (Village of Oak Creek) — 61 Bell Rock Plaza #B — clinic (medical center, Verde Valley Medical Center) — (928) 204-4933. [NEW FIND 2026-11-13] Distinct name and phone from the listed North Country HealthCare – Sedona at 61 Bell Rock Plaza Ste A ((928) 204-4999); no match in either standing file.
- **Tim Mullins LPC (Wild Recovery)** — Sedona — no street address in the listing — mental health (counselor / psychotherapist) — (928) 300-0071. [NEW FIND 2026-11-13] Solo counselor practice (wildrecovery.net); no match in either standing file.
- **Smoking Cessation Wellness Quit Retreat** — Sedona — 160 Portal Ln — mental health / recovery (tobacco cessation treatment center) — (720) 230-2028. [NEW FIND 2026-11-13] FLAG: retreat-model listing with an out-of-state phone; patient-facing status to settle at batch time.

### Found and rejected as already listed
- Arizona Biological Dentistry (105 Roadrunner Dr) — NEW FIND 2026-11-07.
- Village Dentistry (6446 AZ-179 Unit 201) — NEW FIND 2026-11-09.
- Sleep Better Southwest – Sedona (80 Soldiers Pass Rd Ste C) — NEW FIND 2026-11-09.
- Smith Dental LLC / William P. Smith Jr. DDS (1785 W State Rte 89A) — NEW FIND 2026-11-07.
- Westervelt Family Dentistry — inventory #21; published big-westervelt-dental.
- Sedona Dental Arts (1120 W State Route 89A), incl. provider record Maritza E. Sanchez-Salaza, DDS at the same address/phone — inventory #20; published big-sedona-dental-arts.
- Dr. Raegan A. St. Denis / Sedona Family Dentistry (1146 W State Route 89A Ste C1) — inventory #22; published big-sedona-family-dentistry.
- Red Rock Dental (1120 AZ-89A, (928) 282-1282) — inventory #24; HELD in the progress file pending a phone check — already on the list, not new.
- CVS Pharmacy – Sedona (20 Airport Rd) — NEW FIND 2026-11-07.
- NextCare Urgent Care – Sedona (2530 AZ-89A) — NEW FIND 2026-11-09 (new location of the Day 1 NextCare name).
- Village Clinic (56 W Cortez Dr) — inventory #187; published big-village-clinic-sedona.
- Matsuoka MFR Physical Therapy (40 Soldiers Pass Rd #5) — inventory #215; published big-matsuoka-mfr.
- Ascension Therapy Spa (2030 W State Route 89A) — NEW FIND 2026-11-09.
- Sedona Physical Therapy / Lebec Physical Therapy (100 Posse Ground Rd) — inventory #214; published big-sedona-physical-therapy.
- Sedona Physical Therapy – Jody Hendryx (55 Manzanita Dr) — NEW FIND 2026-11-08.
- Myofascial Release Treatment (676 N State Rte 89A) — NEW FIND 2026-11-10; published as big-therapy-on-the-rocks.
- Therapy on the Rocks Myofascial Release Treatment Center (676 N State Rte 89A, (928) 282-3002) — REJECTED: same address and phone as the line above; it is the published big-therapy-on-the-rocks entry under its full name, already on the list.
- Accord Hospice of Sedona (2155 W State Route 89A) — inventory #127; published big-accord-hospice.
- Angels Care Hospice – Sedona (31 Bell Rock Plaza A) — inventory #128; published big-angels-care-hospice.
- Compassus – Sedona (7000 AZ-179 Ste D100) — inventory #129; published big-compassus-sedona.
- Echoes of Bell Rock (31 Bell Rock Blvd Ste D) — NEW FIND 2026-11-09.
- Brio Wellness Helpline (450 Jordan Rd #138) — NEW FIND 2026-11-09.
- Alternative to Meds Center / ATMC (185 Roadrunner Dr) — NEW FIND 2026-11-08.
- AudioNova – Sedona (100 Verde Valley School Rd #105) — NEW FIND 2026-11-09 (surfaced in the Camp Verde hearing search; Sedona address).
- The Sanctuary at Sedona (2605 Cactus Rd) — REJECTED as out of area: despite the name, its address is in Cornville, which is not one of the rollout towns; not added to the Sedona list.
- Wellness/retreat hits that are not healthcare businesses of a listed kind (Sedona Healing Arts, Quantum Resonance Institute, Biocybernaut Institute, Peaceful Body Experience) — REJECTED: retail/retreat centers, no clinical service of a listed kind.
- Out-of-area hits in Sedona searches (StoneRidge Centers – Prescott Valley, Steps to Recovery Homes – Cottonwood, Echo Cliffs Health Center – Coppermine/Tuba City, Sunset Health – Somerton) — not Sedona; the Prescott Valley and Cottonwood names stand in Part B's towns / already-listed records.

---

## PART A TOTAL: 8 new names
- Payson: 4 (Navis-Schmidt Penny; Martinez Lori A; Southwest Behavioral & Health Services – Stageline Rd location; The Beehive Villa)
- Star Valley: 0
- Pine/Strawberry: 0
- Camp Verde: 1 (Hope Women's Center)
- Sedona: 3 (Village of Oak Creek Health; Tim Mullins LPC / Wild Recovery; Smoking Cessation Wellness Quit Retreat)
