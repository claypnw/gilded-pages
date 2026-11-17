# Day 44 — New-Names Check (Step 14) — Part B
Date: 2026-11-16
Towns covered in this part: Sedona, Cottonwood, Show Low, Prescott / Prescott Valley (Arizona)
Method: browser.search for healthcare businesses in the kinds the directory lists (hospitals, urgent care, clinics, dental, pharmacies, vision, mental health and recovery, home health, hospice, physical therapy, medical equipment, hearing, nursing/rehab, labs, imaging, dialysis), then name-matching every candidate against:
- ~/workspace/gilded-pages/healthcare-inventory-draft.md
- ~/workspace/gilded-pages/healthcare-progress.md
Only names NOT on either list are reported as new finds. No deep verification, no phone calls, nothing published by this check.
Excluded per instruction: Cottonwood candidates just published today — Haven Health Cottonwood, Southwest Kidney Institute Cottonwood, Best of Europe, Sedona Regenerative Medicine, Revive IV, Great American Hearing, Paradise Hearing — not reported as new.

## Summary count
- Sedona: 0 new finds
- Cottonwood: 2 new finds
- Show Low: 0 new finds
- Prescott / Prescott Valley: 4 new finds
- Total for this part: 6 new finds

---

## Sedona — none

All candidates found in searches were already on the standing list (inventory and/or progress), including:
NextCare Urgent Care Sedona, Sleep Better Southwest – Sedona location, Arizona Biological Dentistry, Red Rock Dental, Dr. Raegan A. St. Denis, Westervelt Family Dentistry, Sedona Dental Arts, CVS Pharmacy Sedona, My Family Dentist, Smith Dental, Matsuoka MFR Physical Therapy, Accord Hospice of Sedona, Angels Care Hospice Sedona, Compassus Sedona Hospice, Sedona Physical Therapy / Lebec Physical Therapy, Brio Wellness Helpline, Sedona Eye Care, Southwestern Eye Center / Barnet Dulaney Perkins Sedona, Myofascial Release Treatment, Ascension Therapy Spa.

Note on a near-match: "Arizona Eye Clinic" / arizonaeyeclinic.com, Dr. Farshid Paydar, 2155 W State Rte 89A Ste 106, Sedona, (928) 203-9600 — this is the same practice already on the list as "The Eye Clinic – Sedona location (Dr. Farshid Paydar)" in the inventory (new find 2026-11-09) and held in progress. Not counted as new.

New finds: none.

---

## Cottonwood — 2 new finds

### 1. Seaside Serenity
- Town: Cottonwood
- Address: 1750 E Villa Dr, Cottonwood, AZ, US (place listing; no suite shown)
- Kind: Mental health service
- Phone: (928) 222-4752
- Source: place listing in Cottonwood mental-health search, listed Active / Open Now.
- List check: grep "Seaside Serenity" — 0 hits in healthcare-inventory-draft.md, 0 hits in healthcare-progress.md.
- Note: 1750 E Villa Dr is also the address in the inventory for Miracle-Ear Hearing Aid Center – Cottonwood location (Ste E) — a different business name at the same building; verify suite / status at batch time.

### 2. Bearing Detox Solution
- Town: Cottonwood
- Address: 830 S Main St, Cottonwood, AZ, US (place listing; no suite shown)
- Kind: Mental health service / detox
- Phone: (928) 328-1440
- Source: place listing in Cottonwood mental-health search, listed Active / Open Now.
- List check: grep "Bearing Detox" — 0 hits in healthcare-inventory-draft.md, 0 hits in healthcare-progress.md.
- Note: 830 S Main St is also the address in the inventory for VIP Dentistry AZ — a different business name at the same address; verify suite / status at batch time. Record is a place listing only in this check — no deep verification done.

All other Cottonwood candidates were already on the list, including: NextCare Urgent Care Cottonwood, Alpha Medical, Mingus Medical Care, VIP Dentistry AZ, Arizona Family Dental, Walgreens Cottonwood, Yavapai County Community Health Services – Cottonwood, Legacy Home Health Care, Safeway Pharmacy Cottonwood, Beltone Hearing Aid Center, Precision Physical Therapy, The Function Room, Verde Valley Physical Therapy, DaVita Cottonwood Dialysis, All-Med Equipment and Services, Cottonwood VA Clinic, Fornara Eye Center, Sedona Integrative Therapy (Cottonwood address), NAZCARE – Serenity Circle Wellness Center, The Eye Clinic (Cottonwood), Tribe Wellness Group, Red Rock Family Services, Southwestern Eye Center Cottonwood, CenterWell Home Health Cottonwood, All Ways Caring HomeCare Cottonwood.

---

## Show Low — none

All candidates found in searches were already on the standing list, including:
Summit Healthcare Urgent Care – Show Low, Genoa Pharmacy, ComfortFit Dentures, Halls Advanced Dentistry & Implant Center, Advanced Dental Care, CVS Show Low, North Country HealthCare – Show Low (published as successor Elk Ridge Community Health – Show Low), Accord Hospice of the White Mountains, Savior Hospice and Palliative Care, AccentCare, Fresenius Kidney Care, Alpha and Omega Physical Therapy, NAZCARE – Discovery Wellness Center, Sentry Home Health / Rotech, ChangePoint Integrated Health – Show Low, White Mountain Counseling, Windmill Pines Ranch.

Note on a near-match, NOT counted per the name rule: Banner Same-Day Care – Show Low, 680 E Deuce of Clubs Ste B, Show Low, (928) 596-4580, urgent care / same-day clinic. The name "Banner Same-Day Care" is already on the progress list (published Day 1 as big-banner-sameday, the Payson hall), so it is not counted as a new name here. Its Show Low address and phone do not appear in the inventory or progress files — the parent may wish to check whether a distinct Show Low location listing is wanted.

New finds: none.

---

## Prescott / Prescott Valley — 4 new finds

### 1. Eden Hospice Care (Eden Hospice Care Inc)
- Town: Prescott
- Address: 1129 Ironsprings Road, #109, Prescott, AZ 86305 (spelled "Ironsprings" on its own site; also rendered Iron Springs Rd)
- Kind: Hospice / palliative care
- Phone: (928) 482-2490
- Source: its own site edenhospicecareinc.com, Prescott hospice page — "Phone: 928-482-2490", location as above, office hours Mon–Fri 9 AM–5 PM.
- List check: grep "Eden Hospice" — 0 hits in healthcare-inventory-draft.md, 0 hits in healthcare-progress.md.

### 2. Pronghorn Clinic (StoneRidge Centers)
- Town: Prescott Valley
- Address: 7791 E State Rte 69, Prescott Valley, AZ, US (place listing; full route number / suite not shown in listing, listed as "7791 E State Rte")
- Kind: Mental health service / addiction treatment center / medical clinic
- Phone: (928) 583-7799
- Source: place listing, website stoneridgecenters.com.
- List check: grep "Pronghorn Clinic" — 0 hits in healthcare-inventory-draft.md, 0 hits in healthcare-progress.md.
- Note: the phone (928) 583-7799 matches the already-published Pronghorn Psychiatry (StoneRidge Centers), 5940 E Copper Hill Dr Ste B & E, Prescott Valley (inventory #117, big-pronghorn-psychiatry). This appears to be a different address / location for the same StoneRidge organization under the name "Pronghorn Clinic" — verify at batch time whether it is a second location, a move, or a duplicate listing before adding as a separate entry.

### 3. Sun Integrated Health
- Town: Prescott Valley
- Address: 8046 E Yavapai Rd, Prescott Valley, AZ, US
- Kind: Mental health service
- Phone: (602) 671-1700
- Source: place listing, website sunintegratedhealth.com, hours Mon–Fri 7:30 AM–4:30 PM in listing.
- List check: grep "Sun Integrated Health" — 0 hits in healthcare-inventory-draft.md, 0 hits in healthcare-progress.md.
- Note: 8046 E Yavapai Rd is also the address in the inventory for Family Healthcare Clinic (David R. Briant), (928) 772-6707, a 2026-11-11 new find — a different name and phone at the same address; may be co-located or a successor. Verify at batch time.

### 4. Terros Health
- Town: Prescott Valley
- Address: 8128 AZ-69 Ste 111, Prescott Valley, AZ, US
- Kind: Mental health service
- Phone: (877) 756-4090 (place listing; central number)
- Source: place listing, listed Active / Open Now.
- List check: grep "Terros" — 0 hits in healthcare-inventory-draft.md, 0 hits in healthcare-progress.md.

All other Prescott / Prescott Valley candidates were already on the list, including: Prescott Complete Care, Altius Healthcare, Grand Canyon Dental, Prescott Sleep Solutions, Tri-City Men's Health, Hicks Dental Group, Mile High Family Dentistry, Walgreens Prescott, Aqualizer, Central Dental Lab, Higgins Dental Lab, Encompass Physical Therapy, Horizons Healing Center, Northern Arizona Trauma Institute, Circle of Life Alzheimer Homes, Helping Hands In-Home Care, Angela Seesholtz Counseling and Neurofeedback, Arizona Elder Care, Prileo Home Care, Cornerstone Family Counseling, DJC Rock Home Care, NextCare Prescott Valley, Sleep Better Southwest – Prescott Valley, Prescott Valley Dental Group, Aspen Dental Prescott Valley, Bradshaw Family Dental, Horizon Dental Group, Stillwater Dental, Haven Home Health and Hospice, Hospice of the West, Arizona Care Hospice, Compassus Prescott Valley, Nurses Network Home Health, SYNERGY HomeCare, Polara Health – Windhaven, All Ways Caring HomeCare Prescott Valley.

Note on a near-match: "Family First Convenient Care", 3075 N Windsong Dr, Prescott Valley, (928) 350-8780 — this is the same practice already on the list as Family First Primary Care / Family 1st Convenient Care (inventory #208; published as big-family-first-primary-care, corrected in progress to Family 1st Convenient Care / Family 1st Primary Care, 3075 N Windsong Dr Ste A, same phone, site family1stcc.com). Not counted as new.

---

## Searches run (this part)
- Sedona: healthcare clinics / urgent care / hospital / dental / pharmacy; physical therapy / vision / mental health / home health / hospice; vision / eye care / hearing / labs / imaging / dialysis / mental health / recovery
- Cottonwood: healthcare clinics / urgent care / dental / pharmacy / hospital; physical therapy / vision / hearing / dialysis / medical equipment; mental health / recovery / home health / hospice / vision / eye care / labs
- Show Low: healthcare clinics / urgent care / hospital / dental / pharmacy; physical therapy / vision / hearing / hospice / home health / dialysis / labs / imaging; mental health / recovery / nursing / rehab / medical equipment
- Prescott: healthcare clinics / urgent care / hospital / dental / pharmacy; physical therapy / vision / hearing / hospice / home health / dialysis / labs / imaging / mental health
- Prescott Valley: healthcare clinics / urgent care / dental / pharmacy / physical therapy; vision / hearing / hospice / home health / dialysis / labs / imaging / mental health / nursing / rehab
- Follow-up name searches: Eden Hospice Care Prescott phone; Terros Health Prescott Valley; Sun Integrated Health Prescott Valley
