# Day 48 (2026-11-20) — New-Names Check, Part B

Towns covered (this part only): Sedona, Cottonwood, Show Low, Prescott, Prescott Valley.
Kinds searched: hospitals, urgent care, clinics, dental, pharmacies, vision, mental health and recovery, home health, hospice, physical therapy, medical equipment.
Chiropractic-only practices excluded per standing precedent.
Method: 10 browser.search queries (2 per town — a clinic/dental/pharmacy/urgent-care query and a vision/pharmacy/PT/mental-health/home-health/hospice query). Every candidate name was checked with grep against BOTH ~/workspace/gilded-pages/healthcare-inventory-draft.md and ~/workspace/gilded-pages/healthcare-progress.md, and the finalists were also checked against the published working copy ~/workspace/BACKUP-github-websites-only/gilded-pages/index.html.

## NEW NAMES — NOT on either list: 3

### Cottonwood (2)
1. **Bella Vita Healthcare** — Cottonwood — clinic (women's health: "providing the highest level of care to the women of the Verde Valley") — 18 E Beech St, Cottonwood, AZ — (928) 634-0391 — bellavitahealthcareaz.com. Grep: no match in inventory, progress, or published page.
2. **HOPE Inc** — Cottonwood — mental health and recovery (addiction service; also listed as mental health service / community organization) — 8 E Cottonwood St Bldg A Room A-16, Cottonwood, AZ — (928) 642-4057 — hopearizona.org. Grep: no match in inventory, progress, or published page. Note: the address is the Spectrum Healthcare campus (Spectrum's main Cottonwood site is 8 E Cottonwood St, already published as big-spectrum-cottonwood, and Genoa Healthcare Cottonwood stands in Building C of the same campus) — HOPE Inc is a distinct organisation/name at that campus, not a Spectrum entry.

### Show Low (1)
3. **Navajo County Health Department** — Show Low — clinic / public health services — 600 N 9th Pl, Show Low, AZ — (928) 532-6050 — navajocountyaz.gov/309/Public-Health-Services. Grep: no match in inventory, progress, or published page ("Navajo County" appears only inside the Savior Hospice entry's service-area note). FLAG: a county government public-health office, not a commercial practice — whether it belongs in the directory as a clinic entry is to be settled at batch time, the same way earlier flagged finds were handled.

### Sedona (0), Prescott (0), Prescott Valley (0)
No new names. Every candidate found in these towns was already on the standing list (see checked-and-excluded below).

**TOTAL NEW NAMES (Part B): 3**

## Checked and excluded — already on the list (name, town — where it stands)
- NextCare Urgent Care — Sedona (2530 AZ-89A, (928) 203-4813): inventory NEW FIND 2026-11-09; published as big-nextcare-sedona.
- Smith Dental LLC / William P. Smith Jr. DDS — Sedona (1785 W State Rte 89A, (928) 282-2077): inventory NEW FIND 2026-11-07.
- Sleep Better Southwest — Sedona (80 Soldiers Pass Rd Ste C, (928) 227-3024): inventory NEW FIND 2026-11-09; published as big-sleep-better-southwest-sedona. Its Prescott Valley hall (8841 E Florentine Rd, (928) 778-4555) is the original NEW FIND 2026-11-07.
- Arizona Biological Dentistry — Sedona (105 Roadrunner Dr, (928) 282-2482): inventory NEW FIND 2026-11-07.
- Red Rock Dental — Sedona (1120 AZ-89A, (928) 282-1282): inventory #24.
- The Eye Clinic (Dr. Farshid Paydar; search listing domain arizonaeyeclinic.com) — Sedona (2155 W State Rte 89A Ste 106, (928) 203-9600): inventory NEW FIND 2026-11-09 as "The Eye Clinic – Sedona location"; the Cottonwood hall is published as big-eye-clinic-cottonwood.
- Arizona Elder Care — Sedona (150 Dry Creek Rd, (928) 639-1583): inventory #132. (A distinct Prescott office is a NEW FIND 2026-11-08.)
- Home Instead Senior Care — Sedona ((928) 202-4679): inventory #131.
- Heartfelt of Sedona — Sedona ((928) 284-3750): inventory NEW FIND 2026-11-14.
- NextCare Urgent Care — Cottonwood (450 S Willard St #120, (928) 634-2574) and Prescott Valley (3051 N Windsong Dr, (928) 772-3336): NOT new — both stand as locations[] inside the published big-nextcare entry in the working copy (checked directly in index.html), alongside Prescott.
- Optima Medical — Cottonwood (450 S Willard St #103, (928) 634-9573): inventory #194.
- Arizona Smile Designers — Cottonwood (350 S Willard St, (928) 634-8610): inventory #28.
- Spectrum Healthcare Group — Cottonwood (search listing at its main site, 8 E Cottonwood St; (877) 634-7333 central line): inventory #102; published as big-spectrum-cottonwood, whose entry itself notes 8 E Cottonwood St as the main site.
- Arizona Family Dental — Cottonwood (658 E Mingus Ave, (928) 634-6192): inventory #34.
- VIP Dentistry AZ (incl. the Dr. Massoud Eftekhari listing, same address/phone) — Cottonwood (830 S Main St, (928) 634-5566): inventory NEW FIND 2026-11-07.
- Banner Same-Day Care — Show Low (680 E Deuce of Clubs Ste B, (928) 596-4580): already recorded in the inventory (Day 44, 2026-11-16) as a not-counted note — the name is published (Payson hall, big-banner-sameday) and this Show Low address was expressly noted as not on the list and not counted; not re-reported as new.
- Summit Healthcare Urgent Care — Show Low (4951 S White Mountain Rd Bldg A, (928) 537-6743): NOT new — it already stands as a Show Low location inside a published entry in the working copy (index.html line 1066, with the same address and phone).
- Elk Ridge Community Health – Show Low Dental Clinic — Show Low (2650 E Show Low Lake Rd; search phone (928) 251-3158): the clinic is published as big-elk-ridge-show-low (2650 E Show Low Lake Rd Ste 1, (928) 537-4300), whose record states it is an FQHC primary care + dental clinic at that address — same entry, not a new name. The differing dental phone is a batch-time note only.
- Akos Med Clinic — Show Low (900 W Deuce of Clubs, (928) 222-0402; listing says possibly temporarily closed): inventory NEW FIND 2026-11-09; stands in the Day 48 next-batch leads in the progress file.
- Advanced Dental Care — Show Low (301 N Central Ave, (928) 537-4363): inventory #38; published as big-advanced-dental-show-low.
- Halls Advanced Dentistry & Implant Center — Show Low (308 N White Mountain Rd, (928) 532-5550): inventory #40; published as big-halls-advanced-dentistry.
- ComfortFit Dentures — Show Low (301 N Central Ave, (928) 888-0002): inventory #36; published as big-comfortfit-dentures.
- CVS — Show Low (60 E Deuce of Clubs, (928) 532-3200): inventory NEW FIND 2026-11-07.
- AccentCare — Show Low (60 S White Mountain Rd Ste B, (928) 532-5400): inventory NEW FIND 2026-11-08. Its Prescott Valley hall (3050 N Navajo Dr #100, (928) 632-5219) is a NEW FIND 2026-11-10.
- Savior Hospice and Palliative Care — Show Low (1801 W Deuce of Clubs #310, (928) 892-3990): inventory NEW FIND 2026-11-08; published as big-savior-hospice.
- Sentry Home Health — Show Low (5171 Cub Lake Rd Ste 290 Bldg B, (928) 532-7719): inventory #149 (Regency Medical Equipment / Sentry Home Health); published as big-sentry-home-health.
- Preferred Homecare — Show Low (3051 S White Mountain Rd Ste B, (928) 532-1088): inventory #147. Its Prescott Valley hall (8067 Florentine Rd, (928) 445-0477) is a NEW FIND 2026-11-08.
- Prescott Complete Care — Prescott (1947 Commerce Center Cir Ste A, (928) 458-5723): inventory NEW FIND 2026-11-10.
- Tony Dalton, DDS (search: Dalton Tony J DDS) — Prescott (1055 Ruth St Ste 7, (928) 445-5600): inventory NEW FIND 2026-11-07.
- Altius Healthcare — Prescott (1151 W Iron Springs Rd, (928) 708-0025): inventory NEW FIND 2026-11-07.
- McKinney Physical Therapy — Prescott (250 S McCormick St, (928) 777-8050): inventory NEW FIND 2026-11-10 (flagged co-location with Backway's).
- Grand Canyon Dental — Prescott (172 Merritt Ave, (928) 443-1200): inventory NEW FIND 2026-11-07.
- Mangum Dental — Prescott (1229 Willow Creek Rd, (928) 778-4110): inventory NEW FIND 2026-11-09.
- Hicks Dental Group — Prescott (108 Whipple St, (928) 445-6030): inventory #42; published as big-hicks-dental.
- Bradshaw Family Dental — the search listing at 172 E Merritt St, Prescott, (928) 443-1200 is the Prescott hall of the practice whose Prescott Valley hall (7136 E Pav Way) is inventory #56 and published as big-bradshaw-family-dental, whose entry already notes the second Prescott hall; the Merritt St phone matches Grand Canyon Dental at the same address. Not a new name.
- Prescott Dental Arts — Prescott (1787 Willow Creek Rd, (928) 445-8980): inventory #49; published as big-prescott-dental-arts.
- "Family Dentistry" (generic place record) — Prescott (1231 Willow Creek Rd A, (928) 778-5518): same address as the published Joseph A. Savoini, DMD hall (big-savoini-dmd, 1231 Willow Creek Rd Ste A) — treated as an alternate/generic record for that premises, not a new name; the phone conflict is a batch-time note only.
- Good Samaritan Hospice — Prescott (1065 Ruth St, (928) 778-5655): inventory NEW FIND 2026-11-08.
- Assisteo North Hospice — Prescott (919 12th Pl #6, (928) 277-1345): named in the inventory's Cottonwood extras line and recorded in the progress file as a Prescott entry, publishable with flags.
- Arizona Life Hospice — Prescott (3177 Clearwater Dr Ste B, (928) 379-3391): inventory #155; published as big-arizona-life-hospice.
- Maggie's Hospice — Prescott (801 Miller Valley Rd, (928) 775-2290): inventory NEW FIND 2026-11-08.
- Angels Care Hospice — Prescott (1000 Willow Creek Rd, (928) 379-2887): inventory NEW FIND 2026-11-08 (distinct from the published Sedona hall).
- Family First Convenient Care (search name; family1stcc.com) — Prescott Valley (3075 N Windsong Dr, (928) 350-8780): same business/address/phone as inventory #208 Family First Primary Care, published as big-family-first-primary-care and corrected in the progress file to "Family 1st Convenient Care / Family 1st Primary Care" — a name variant of a published entry, not new.
- Horizon Dental Group — Prescott Valley (7890 E Florentine Rd, (928) 772-9860): inventory NEW FIND 2026-11-07.
- Aspen Dental — Prescott Valley (7584 E State Rte 69, (928) 499-3061; search listing under practitioner John Snee): inventory #51; published as big-aspen-dental.
- Lyon Orthodontics Lab — Prescott Valley (3550 N Mountain View Dr, (928) 772-9314): inventory NEW FIND 2026-11-15.
- Stillwater Dental — Prescott Valley (3253 N Windsong Dr): inventory NEW FIND 2026-11-07.
- Prescott Valley Dental Group — Prescott Valley (3264 Glassford Hill Rd, (928) 759-8000): inventory #50; published as big-prescott-valley-dental-group.
- Billet Health – Prescott — Prescott Valley (8508 E State Rte 69, (833) 224-5538): inventory NEW FIND 2026-11-10.
- All Ways Caring HomeCare — Prescott Valley (3100 N Navajo Dr, (928) 275-6722): inventory #165.
- Haven Home Health and Hospice — Prescott Valley (7750 E Florentine Rd, (928) 420-8880): inventory #158; published as big-haven-home-health-hospice.
- Nurses Network Home Health — Prescott Valley (3085 N Windsong Dr, (928) 772-8707): inventory #164; published as big-nurses-network-pv.
- Angels On Duty — Prescott Valley (2852 N Navajo Dr, (928) 759-7145): inventory NEW FIND 2026-11-08.

## Excluded by kind / record quality (not counted, not on the list either)
- PROHEALTH Chiropractic & Rehab Center — Show Low: chiropractic-primary listing, excluded per the task's chiropractic-only rule (it also already stands in the inventory as a NEW FIND 2026-11-10).
- Aspen Ridge Animal Hospital — Lakeside (veterinary, out of scope and outside the five towns).
- SPIRITSKiN — Sedona; Prime Vitality LLC — Cottonwood; Mastery of Self Healing — Cottonwood; Younger You by Cat Dale — Cottonwood; Elemental Integration LLC — Show Low: vague "medical service" / wellness listings with no directory kind established in the listing — not counted, per the searches-and-name-matching-only scope of this step.
- Individual-practitioner listings that are the same business as a listed practice (Dr. Massoud Eftekhari = VIP Dentistry AZ; Kaia Kordosky-Herrera = Prescott Complete Care; Dr Richard L D'Armand = NextCare Prescott Valley; John Snee = Aspen Dental Prescott Valley) — counted under their practice names above.
