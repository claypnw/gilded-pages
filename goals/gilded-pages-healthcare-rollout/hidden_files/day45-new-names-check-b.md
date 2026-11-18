# Day 45 — New-Names Check (Step 14) — Part B
Date: 2026-11-17
Towns covered in this part: Cottonwood, Show Low, Prescott, Prescott Valley (Arizona)
Method: browser.search for healthcare businesses of the kinds the directory lists (hospitals, urgent care, clinics, dental, pharmacies, vision, mental health and recovery, home health, hospice, physical therapy, medical equipment, hearing, labs, imaging, nursing), then name-matching every candidate against all three standing records:
- ~/workspace/gilded-pages/healthcare-inventory-draft.md
- ~/workspace/gilded-pages/healthcare-progress.md
- ~/workspace/BACKUP-github-websites-only/gilded-pages/index.html (working copy)

Strict rule applied, per the brief: a name is NEW only if it appears in NONE of those three files. Same business under a slightly different name, a new location of an already-listed name, and a business outside the town do NOT count — those are listed as rejected, with the reason, and where a rejected location's address is in fact in none of the files that is said plainly so the parent can decide whether a separate location entry is wanted.
No deep verification, no phone calls, nothing published by this check.

Published today (2026-11-17) and NOT new, verified in the working copy: Cottonwood VA Clinic, Verde Valley Orthodontics, Maggie's Hospice Cottonwood, Miracle-Ear Cottonwood, Labcorp Cottonwood, EntireCare Cottonwood, NAH Recovery Clinic Cottonwood.

## Summary count (strict name rule)
- Cottonwood: 2 new names
- Show Low: 0 new names
- Prescott: 2 new names
- Prescott Valley: 1 new name
- Total for this part: 5 new entries (4 distinct organisations — Abrio Home Care has a separate office in each of Cottonwood and Prescott Valley)

---

## Cottonwood — 2 new names

### 1. Abrio Home Care Cottonwood
- Town: Cottonwood
- Kind: Home health / home care
- Address: 830 S Main St, Cottonwood, AZ
- Phone: (928) 634-6758
- Source: place listing, website abriohomecare.com — woman- and veteran-owned, in-home care (personal care, meal prep, companionship, transportation, medication management, respite), listed Active.
- List check: grep "Abrio" — 0 hits in healthcare-inventory-draft.md, 0 hits in healthcare-progress.md, 0 hits in the working-copy index.html.
- Note: 830 S Main St is also the address in the inventory for VIP Dentistry AZ and for yesterday's Bearing Detox Solution find — a different business name at the same building; verify suite at batch time.

### 2. Angel's Touch Inc — FLAG: thin record
- Town: Cottonwood
- Kind: Home health (Medicare-certified home health agency: nursing, speech / occupational / physical therapy, home health aides, medical social work, wound care, IV infusion)
- Address: US-89 ALT, Cottonwood, AZ 86326 — no street number in the listing found
- Phone: not found for the business itself — the SeniorAdvisor listing gives only its own central number, 1-866-344-9690, which is NOT the business's phone and must not be used as such
- Source: SeniorAdvisor home-care directory listing (crawled 2 days ago) naming "Angel's Touch Inc - Cottonwood, AZ"; a 2021 U.S. District Court opinion (Angel's Touch Inc. v. Becerra, No. CV-21-08026) describes it as a Medicare-certified home health agency providing services to approximately 312 patients in Cottonwood, Arizona.
- List check: grep "Angel's Touch" / "Angels Touch" — 0 hits in all three files.
- FLAG: thin record — no street number and no direct phone in this check, and the court record is from 2021. Verify current status, address and phone at batch time before any entry is built.

### Rejected — Cottonwood
- Helping Hands In-Home Care — Cottonwood, 203 S Candy Ln, (928) 639-8450 (a second listing gives 14 S Main St, Cottonwood): REJECTED per strict name rule — the name is already on the list (inventory: Helping Hands In-Home Care — Prescott, 371 Garden St Ste H, (928) 238-1506, NEW FIND 2026-11-11). Note for the parent: the Cottonwood address and phone appear in none of the three files, so this is an uncovered Cottonwood office of a listed name if a separate location entry is wanted.
- SYNERGY HomeCare — Cottonwood, 3800 E Western Dr Ste C, (928) 515-3318 (its own site: "SYNERGY HomeCare of Northeast Arizona", Cottonwood office): REJECTED per strict name rule — SYNERGY HomeCare is already listed (Prescott Valley office, inventory #166, published; Payson office, NEW FIND 2026-11-07). Note: the Cottonwood address appears in none of the three files; the phone is the same as the Prescott Valley office's.
- Preferred Homecare — Cottonwood, 295 S Willard St Ste 101, (928) 634-7528: REJECTED per strict name rule — Preferred Homecare is already listed (Payson #124, Show Low #147, Prescott Valley NEW FIND 2026-11-08). Note: the Cottonwood address and phone appear in none of the three files.
- Angels Care Home Health — Cottonwood, 1756 E Villa Dr C-17, (928) 649-8890: REJECTED per strict name rule — Angels Care Home Health is already listed (Prescott Valley, inventory #163, published). Note: the Cottonwood address appears in none of the three files; suite C-17 is the address in the inventory for Aviant Healthcare — Cottonwood (hospice), a different name/phone, so a successor or co-location question stands if the parent takes this up.
- CVS Pharmacy — Cottonwood, 1179 S Highway 260, (928) 634-2147: REJECTED per strict name rule — CVS Pharmacy is already listed for Camp Verde, Sedona, Prescott and Prescott Valley. Note: no Cottonwood CVS entry stands in any of the three files, so this store is uncovered if a separate location entry is wanted.
- Fry's Pharmacy — Cottonwood, 1100 AZ-260, (928) 634-9338: REJECTED per strict name rule — Fry's Pharmacy is already listed (Prescott Valley, NEW FIND 2026-11-08). Note: the Cottonwood store appears in none of the three files.
- Yavapai County Community WIC Services — Cottonwood, 10 S 6th St, (928) 639-8134: REJECTED — a WIC program of the already-listed Yavapai County Community Health Services / Community Health Center of Yavapai (Cottonwood, 51 Brian Mickelsen Pkwy); same organisation under a program name, per the slightly-different-name rule. Its 10 S 6th St address is not in the files.
- Dr. Massoud Eftekhari / Kaia-type individual listings, Dr. David Frausto-type listings: individual practitioners at already-listed practices (VIP Dentistry AZ), not separate businesses.
- All other Cottonwood candidates found were already on the list, including: Arizona Family Dental, VIP Dentistry AZ, NextCare Urgent Care Cottonwood, Walgreens Cottonwood, Nurses Network by Quality Home Health Cottonwood, Alpha Medical, Legacy Home Health Care, CenterWell Home Health Cottonwood, Alliance Homecare Cottonwood, All Ways Caring HomeCare Cottonwood, Northern Arizona Home Health Cottonwood, Southwestern Eye Center Cottonwood, Ameritone Beltone Hearing / Beltone Hearing Aid Center Cottonwood, Fornara Eye Center, The Eye Clinic Cottonwood, Miracle-Ear Cottonwood (published today), Great American Hearing Aid Company, Paradise Hearing Cottonwood, Vue Optical, Tribe Wellness Group, NAZCARE – Serenity Circle Wellness Center, Mingus Center Adult Behavioral, Polara Health Cottonwood Clinic, Spectrum Healthcare Group Cottonwood, Community Health Center of Yavapai Cottonwood, Verde Valley Medical Center Retail Pharmacy (NEW FIND 2026-11-14), Cottonwood Dental Laboratory, Safeway Pharmacy Cottonwood, Verde River Dental, Cottonwood VA Clinic (published today), Verde Valley Orthodontics (published today), Maggie's Hospice Cottonwood (published today), Labcorp Cottonwood (published today), EntireCare Cottonwood (published today).

---

## Show Low — 0 new names

New finds: none.

### Rejected — Show Low
- Banner Same-Day Care — Show Low, 680 E Deuce of Clubs Ste B, (928) 596-4580: REJECTED per strict name rule — the name "Banner Same-Day Care" is already published (Payson hall, big-banner-sameday, Day 1). Note, as yesterday: its Show Low address and phone do not appear in the inventory or progress files.
- Factor II, Inc. — 5642 White Mountain Ave, Lakeside, AZ, (928) 537-8387, medical equipment / prosthetic supplies: REJECTED — outside the town; the address is in Lakeside, not Show Low. Name itself is in none of the three files.
- White Mountain Hearing Service, Powered By Beltone — 5658 AZ-260 Ste 4, Lakeside, AZ, (928) 582-9370: REJECTED — outside the town (Lakeside address).
- Olson Eric V — 680 E Deuce of Clubs B, Show Low, (928) 537-2777, listed as "Nursing Agency": REJECTED — an individual person's name at the Banner Same-Day Care suite, not a business name; no business listing found.
- Aspen Ridge Animal Hospital — Lakeside: REJECTED — veterinary, and outside the town.
- All other Show Low candidates found were already on the list, including: Summit Healthcare Urgent Care – Show Low, ComfortFit Dentures, Halls Advanced Dentistry & Implant Center, Advanced Dental Care, Akos Med Clinic, CVS Show Low, North Country HealthCare – Show Low, Savior Hospice and Palliative Care, PROHEALTH Chiropractic & Rehab Center, AccentCare Show Low, Sentry Home Health / Rotech, Preferred Homecare Show Low, Genoa Pharmacy Show Low, Audiology (Audiology Inc) Show Low, Miracle-Ear Show Low, Barnet Dulaney Perkins Eye Center Show Low, Windmill Pines Ranch, ChangePoint Integrated Health – Show Low, White Mountain Counseling.

---

## Prescott — 2 new names

### 1. Western Medical Services — FLAG: place listing only
- Town: Prescott
- Kind: Home health care service
- Address: 805 Miller Valley Rd, Prescott, AZ
- Phone: (928) 708-9411
- Source: place listing only, listed Active, primary category Home Health Care Service; no website in the listing.
- List check: grep "Western Medical" — 0 hits in all three files.
- FLAG: place listing only in this check, and general web history for a company of this name is old (a national home-health company of this name was sold in 1999). Verify at batch time whether a current Prescott home-health office stands at this address under this name. 805 Miller Valley Rd is also the street address in the inventory for Maggie's Hospice — Prescott (801 Miller Valley Rd is the listed number; close but not identical).

### 2. The Pines Home Health & Hospice
- Town: Prescott
- Kind: Home health and hospice
- Address: 804 Ainsworth Dr, Suites 102 A and B, Prescott, AZ
- Phone: (928) 632-0111
- Source: place listing, listed Active / Open Now — "supporting the people of Yavapai County since 2005… throughout Prescott, Chino Valley, Prescott Valley, Dewey-Humboldt, Camp Verde, Cottonwood, Sedona"; also in the Prescott Parkinson's Support Group resource list ("The Pines Home Health & Hospice, 928-632-0111, thepineshealthcare.com").
- List check: grep "Pines Home Health" — 0 hits in all three files. (The word "Pines" alone hits other, different businesses — Recovery in the Pines and Windmill Pines Ranch — not this one.)
- Note: a NACOG directory feed gives a "The Pines - Home Health & Hospice" address of 6719 E. 2nd St. Ste A, Prescott Valley — a possible second office or a conflicting address; settle at batch time. The Prescott place listing above is the one counted here.

### Rejected — Prescott
- Southwest Kidney Institute — Prescott, 1000 Willow Creek Rd Ste F, (480) 610-6100: REJECTED per strict name rule — Southwest Kidney Institute is already listed (Cottonwood, published; Prescott Valley location, NEW FIND 2026-11-15). Note: the Prescott address appears in none of the three files.
- AKDHC Prescott / Arizona Kidney Disease and Hypertension Center — Prescott, 3122 Willow Creek Rd, (928) 445-7632, nephrology: REJECTED per strict name rule — the full name is already on the list (Arizona Kidney Disease And Hypertension Centers — Show Low, NEW FIND 2026-11-15). The acronym "AKDHC" alone is in none of the files, and the Prescott address is in none of the files.
- Renal Care Group — Prescott, 980 Willow Creek Rd #101, (928) 776-8061, dialysis: REJECTED — the address is exactly the already-listed DaVita Prescott Dialysis hall (inventory #150, same suite); no independent website, and the name is a predecessor operator at that site in older records. Treated as a stale / duplicate listing for the same dialysis site, not a separate business. Name itself is in none of the three files, so the parent may wish to confirm.
- Atlantis Home Health, Inc. / Atlantis Home Care — Prescott: NOT COUNTED — insufficient record. It appears only as a cross-reference in a senior-care directory ("Atlantis Home Care, Prescott, AZ, < 1 mile", no address or phone) and in a CMS CY2026 home-health list ("ATLANTIS HOME HEALTH, INC, PRESCOTT, AZ", CCN 037467, on an excluded-from-APU list). No current place listing, address, or phone was found in this check.
- Arizona Home Health Specialists of Prescott / Hassayampa Home Health — Prescott: NOT COUNTED — names appear only in CMS excluded/terminated home-health lists, with no current listing, address, or phone found.
- Caring Presence In Home Care — Prescott, 805 Whipple St, (928) 771-0701: already on the list (Caring Presence — Prescott, 805 Whipple St Ste D, NEW FIND 2026-11-15).
- Amedisys Home Health — Prescott, 2971 Willow Creek Rd Ste 2a-c, (928) 443-7663: already on the list (NEW FIND 2026-11-11, named inside the published BAYADA Prescott entry's note).
- All other Prescott candidates found were already on the list, including: Prescott Complete Care, Community Health Center of Yavapai – Prescott, Altius Healthcare, Prescott Sleep Solutions, Grand Canyon Dental, Aqualizer, Tri-City Men's Health, Polara Health – Cortez Clinic, Circle of Life Alzheimer Homes, Helping Hands In-Home Care Prescott, Arizona Elder Care, Prileo Home Care, DJC Rock Home Care – Prescott, DaVita Prescott Dialysis, Fresenius / M&M Eye Institute (successor to Prescott Eye Care, published), Premier Eye Center Prescott, Williams Eye Care Group / LensCrafters Prescott, Bob Stump Department of Veterans Affairs Medical Center (NEW FIND 2026-11-12), Arizona Life Hospice, Embark Recovery, Prescott House, AZ MediQuip (Prescott Valley location listed).

---

## Prescott Valley — 1 new name

### 1. Abrio Home Care — Prescott Valley office
- Town: Prescott Valley
- Kind: Home health / home care
- Address: 2485 N Great Western Dr, Prescott Valley, AZ (a directory listing gives "2485 Great Western, Suite G2, Prescott Valley, AZ 86314")
- Phone: (928) 772-8866
- Source: place listing, website abriohomecare.com, listed Active; also in the AZNHA agency member list ("ABRiO Care, Prescott Valley, 2485 Great Western #G2, 928-772-8866").
- List check: grep "Abrio" — 0 hits in all three files.
- Note: same organisation as the Cottonwood new find above, at a distinct Prescott Valley office with its own address and phone; counted once for this town, as with earlier multi-town finds.

### Rejected — Prescott Valley
- AKDHC Prescott Valley / Arizona Kidney Disease and Hypertension Center — Prescott Valley, 3194 N Windsong Dr (phone via the Prescott office, (928) 445-7632): REJECTED per strict name rule — the full name is already on the list for Show Low (NEW FIND 2026-11-15). Note: the Prescott Valley address appears in none of the three files; the listing evidence is provider-directory pages only, no place listing was found in this check.
- Consumer Direct Care Network — Prescott Valley, 8182 E. Florentine Rd Ste. C, (928) 445-3135: NOT COUNTED — the only record found is a 2023 AZNHA member-list PDF; no current place listing, website record, or current directory entry was found in this check.
- Cardinal Home Care — Prescott: NOT COUNTED — only a garbled entry in the same 2023 AZNHA list, with a Phoenix-area address attached; no Prescott / Prescott Valley listing found.
- Genoa Healthcare — Prescott Valley, 3347 N Windsong Dr, (928) 499-6908: already on the list (Genoa Healthcare – Prescott Valley location, NEW FIND 2026-11-15).
- Paul B. Smith — 3345 N Windsong Dr, Prescott Valley, category Pharmacy, phone (928) 445-5211: REJECTED — an individual person's name at the Polara Health Windhaven address/phone, not a business.
- John Snee / Heidi S. Alessi / Dr David Frausto Jr listings: individual practitioners at already-listed practices (Aspen Dental Prescott Valley, NextCare Prescott Valley, Bradshaw Family Dental), not separate businesses.
- All other Prescott Valley candidates found were already on the list, including: NextCare Urgent Care Prescott Valley, Family First Convenient Care / Family 1st Convenient Care, Community Health Center of Yavapai – Prescott Valley, Sleep Better Southwest – Prescott Valley, Prescott Valley Dental Group, Aspen Dental Prescott Valley, Bradshaw Family Dental, Horizon Dental Group, Haven Home Health and Hospice Prescott Valley, Angels Care Home Health Prescott Valley, SYNERGY HomeCare Prescott Valley, Nurses Network Home Health Prescott Valley, Angels On Duty, All Ways Caring HomeCare Prescott Valley, Child and Family Support Services (NEW FIND 2026-11-09), Preferred Homecare Prescott Valley, AccentCare Personal Care Prescott Valley, Billet Health – Prescott (Prescott Valley address, NEW FIND 2026-11-10), M&M Eye Institute – Prescott Valley location (NEW FIND 2026-11-13), Fresenius Kidney Care Prescott Valley East (NEW FIND 2026-11-11), Fry's Pharmacy Prescott Valley, CVS Prescott Valley, Walgreens Prescott Valley, Southwest Kidney Institute – Prescott Valley location (NEW FIND 2026-11-15), Terros Health / Sun Integrated Health / Pronghorn Clinic (all NEW FIND 2026-11-16).

---

## Searches run (this part)
- Cottonwood: healthcare clinics / urgent care / dental / pharmacy / hospital; physical therapy / vision / hearing / hospice / home health / labs / imaging; mental health / recovery / medical equipment / nursing; eye care / vision / optometry / hearing aids; dental clinic / orthodontics / pharmacy list; follow-up name searches for Abrio Home Care, SYNERGY HomeCare Cottonwood, Preferred Homecare Cottonwood, Angels Care Home Health Cottonwood, Angel's Touch Cottonwood
- Show Low: healthcare clinics / urgent care / hospital / dental / pharmacy; physical therapy / vision / hearing / hospice / home health / mental health; mental health / recovery / labs / imaging / medical equipment / nursing; eye care / vision / hearing / dental / pharmacy
- Prescott: healthcare clinics / urgent care / hospital / dental / pharmacy; physical therapy / vision / hearing / hospice / home health / labs / imaging / mental health; eye care / vision / hearing aids / labs / imaging / dialysis; mental health / counseling / recovery; follow-up name searches for Western Medical Services, The Pines Home Health & Hospice, Atlantis Home Care, Renal Care Group, AKDHC, Southwest Kidney Institute Prescott
- Prescott Valley: healthcare clinics / urgent care / dental / pharmacy / physical therapy; vision / hearing / hospice / home health / mental health / recovery / labs; eye care / vision / hearing / dental; dialysis / Fresenius / DaVita / pharmacy; follow-up name search for Abrio Home Care Prescott Valley
