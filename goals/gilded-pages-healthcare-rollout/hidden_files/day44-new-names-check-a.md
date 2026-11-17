# Day 44 — New-Names Check (Step 14), Part A
Date: 2026-11-16
Towns covered: Payson, Star Valley, Pine/Strawberry, Camp Verde (Arizona)
Method: browser.search per town for hospitals, urgent care, clinics, dental, pharmacies, vision, mental health and recovery, home health, hospice, physical therapy, medical equipment, hearing, nursing/rehab, labs, imaging, dialysis. Every candidate name was checked with grep -i against ~/workspace/gilded-pages/healthcare-inventory-draft.md and ~/workspace/gilded-pages/healthcare-progress.md. Only names with 0 hits in both files count as new finds. No deep verification, no phone calls, nothing published.

Total new finds in this part: 3
- Payson: 2
- Star Valley: 0
- Pine/Strawberry: 0
- Camp Verde: 1

## Payson — 2 new finds

### 1. Privia Medical Group of Arizona
- Town: Payson
- Address: 111 W Cedar Ln Ste A, Payson, AZ 85541
- Kind: Clinic / medical group (family medicine providers listed: Morgan Gonzalez, NP; Joshua Lyon, PA)
- Phone: 1-623-433-0202 (Optum directory listing for this Payson facility; this number appears as a shared Privia directory number at several Arizona locations — verify at batch time)
- Source: Optum facility listing found in Payson searches.
- Check: grep "Privia Medical" / "Privia Medical Group" = 0 hits in inventory draft and progress file.
- Flag: Co-located at the exact address of the already-published Integrated Medical Services (IMS), 111 W Cedar Ln Ste A, (928) 472-4675. Identity — rebrand, successor, or network listing for the same practice — to settle at batch time, as with prior co-located finds.

### 2. Mogollon Residential - Payson West
- Town: Payson
- Address: 300 E Wade Ln, Payson, AZ, US
- Kind: Mental health and recovery — addiction treatment center / residential recovery
- Phone: (928) 478-7173
- Source: mogollontreatmentcenter.com/mogollon-residential-payson-west/ listing in Payson mental-health searches.
- Check: grep "Mogollon Residential - Payson West" = 0 hits in inventory draft and progress file. The parent names "Mogollon Residential" (212 W Wade Ln) and "Mogollon Treatment Center" (306 W Aero Dr) are already listed/published — this is a distinct second residential location/address under a distinct name, counted as a new-location find in line with prior days' practice (e.g., Genoa, NextCare new locations).

## Star Valley — 0 new finds
Searches for Star Valley, AZ 85541 healthcare, clinic, dental, pharmacy, physical therapy returned no business with a Star Valley address in the covered kinds. Results were Payson businesses 3–5 miles away (all already on the list) and out-of-area Phoenix/Scottsdale/Mesa businesses, plus Star Valley Veterinary Clinic (veterinary — outside the covered kinds, excluded).

## Pine/Strawberry — 0 new finds
Searches returned only:
- Banner Health Clinic – Pine (Family Medicine), 6152 Hardscrabble Mesa Rd, Pine, (928) 596-4848 — already in inventory as #183 "Banner Health Clinic – Pine (Family Medicine)" (en-dash spelling; a hyphen-spelling grep initially missed it) and already published as big-banner-pine.
- Dr. Donald L. Smith, DDS, Pine — already in inventory and published.
All other results were out-of-town (Payson, Flagstaff, Prescott, Phoenix, etc.).

## Camp Verde — 1 new find

### 1. Verde Valley Medical Clinic Orthopedics
- Town: Camp Verde
- Address: 1298 Finnie Flat Rd, Camp Verde, AZ, US
- Kind: Clinic — orthopedics / surgeon (orthopedist)
- Phone: (928) 649-7960
- Source: Verde Valley Medical Clinic Orthopedics listing (weence.com directory) in Camp Verde searches.
- Check: grep "Verde Valley Medical Clinic Orthopedics" = 0 hits in inventory draft and progress file; no Camp Verde orthopedics entry stands in the inventory's orthopedics listings.
- Flag: Co-located at 1298 Finnie Flat Rd, the building of the already-published Northern Arizona Healthcare Medical Group – Camp Verde (big-nah-camp-verde, (928) 639-5555, primary care / Immediate Care / lab). This orthopedics name and phone are distinct — identity as a separate specialty clinic at that site to settle at batch time.

## Candidates checked and rejected (already on the standing list)
Payson: Payson Walk-In Clinic, Banner Same-Day Care, Genoa Healthcare, Anderson Dental Group, Ponderosa Family Care, Lone Tooth, Bonanza Square Dentistry, Gabbert Medical, Payson Premier Dental, North Country HealthCare – Payson, Arizona Care Hospice, Payson Eye Care Center, Valley Hospice of Arizona, Banner Physical Therapy – Payson, Hospice of Payson, Risser Thomas Eye Clinic, Compassus – Payson, Payson Physical Therapy, Comfort Keepers Home Care, Preferred Homecare, Banner Home Care, Mogollon Treatment Center, Mogollon Residential (original location), Southwest Behavioral & Health Services, U-Turn For Christ, Fitz Ilias, Psych Assist, Payson Christian Clinic, Sonora Quest Laboratories, Miracle-Ear Hearing Aid Center, Banner Payson Imaging Center, Patient's Choice Lab Testing & Blood Draw Services, Rim Country Dialysis (the generic "Dialysis Center" place record at its phone (928) 474-7000), Integrated Medical Services (IMS — the "Amalia Pineres" place record is its provider/address), Hospice Rta Operations (added 2026-11-10).
Pine/Strawberry: Banner Health Clinic – Pine, Dr. Donald L. Smith DDS.
Camp Verde: Northern Arizona Healthcare Medical Group / Immediate Care – Camp Verde, Walgreens – Camp Verde, CVS Pharmacy – Camp Verde, Copper Canyon Family Dental, Verde Dental Care, Verde Smiles, Diamond D Rehab, Central Arizona Sports and Physical Therapy, Caring Hearts In-Home Care, Haven of Camp Verde / Haven Health Camp Verde, Polara Health – Camp Verde, Spectrum Healthcare Group – Camp Verde (inventory #97, skipped as unverified), Camp Verde Eye Care, Creative Dental Designs, Black Canyon Community Health Center, Yavapai-Apache Nation Health Center, EntireCare Rehab and Sports Medicine – Camp Verde (inventory new find 2026-11-08, at the same 1298 Finnie Flat Rd address).

Also excluded as not separate businesses: individual provider names at already-listed practices (Mattern Thomas DDS and Wilson Gustavo DDS at Payson Premier Dental's address/phone; Joanna Linn at North Country HealthCare's address/phone), and "Ketamine Evaluations" (a garbled place record sharing Fitz Ilias's phone, with a non-Payson street address).
