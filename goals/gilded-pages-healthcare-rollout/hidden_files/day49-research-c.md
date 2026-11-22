# Day 49 — Research C — Show Low (2 entries)
Researched: 2026-11-21 (Arizona time), via browser.search / browser.open
Rule applied: Do not invent data. Official site preferred over directories. All conflicts listed.

Sources key:
- [VA-OFFICIAL] https://www.va.gov/phoenix-health-care/locations/show-low-va-clinic/ — opened 2026-11-21, loads successfully
- [VA-MARKET] https://marketplace.va.gov/facilities/show-low — VA Diffusion Marketplace, opened 2026-11-21, loads successfully
- [WM-OFFICIAL] https://www.whitemountainperiodontics.com/ — opened 2026-11-21, loads successfully
- [WM-CONTACT] https://www.whitemountainperiodontics.com/contact/ — opened 2026-11-21
- [WM-TINGEY] https://www.whitemountainperiodontics.com/meet-dr-tingey/ — opened 2026-11-21
- [PROGRESS] ~/workspace/gilded-pages/healthcare-progress.md and ~/workspace/BACKUP-github-websites-only/gilded-pages/index.html — published Chet Adams entry

---

## 1. Show Low VA Clinic — Show Low

### Verdict: PUBLISHABLE

### Exact name
- **Show Low VA Clinic** [VA-OFFICIAL, VA-MARKET]
- Variants in directories: "Show Low VA Health Care Clinic" / "Show Low VA Healthcare Clinic" (LongTermCareLink, CountyOffice) — same facility, longer descriptive form. Use the official short form.

### Address
- **5171 Cub Lake Road, Suite C380, Show Low, AZ 85901-7850** [VA-OFFICIAL]
- Corroborated without ZIP+4 / suite punctuation variants: 5171 Cub Lake Road, Suite C380, Show Low, AZ 85901 [VA-MARKET, UA Cooperative Extension (checked Oct 2026), LongTermCareLink]
- Matches inventory: 5171 Cub Lake Rd Ste C380. No conflict on street, suite, city, or ZIP.

### Phone — CONFLICT SETTLED
- **Publish: (928) 532-1069**
  - VA Diffusion Marketplace (official VA): "Main number: 928-532-1069" [VA-MARKET]
  - UA Cooperative Extension resource hub, "Last checked: October 2026": 928-532-1069, same address/suite
  - LongTermCareLink national VA list: 928-532-1069
  - Google/Meta place listing: +1 928-532-1069, Operating Status: Active
  - RecordMaps: "Main phone, 928-532-1069"
- **Do NOT publish: (928) 537-2044**
  - Sole source found for the clinic under that number: CountyOffice.org page for the clinic, crawled ~332 days ago — a low-reliability aggregator. No VA source uses it for this clinic.
  - A separate old Navajo/Apache resource directory lists (928) 537-2044 as "Veterans Assistance" in a Linden-area table — a different veterans-assistance contact, not the Show Low VA Clinic main number. That is the likely origin of the confusion.
  - Conclusion: 537-2044 is stale / mis-attributed. 532-1069 wins on official VA source + multiple independent corroborations.
- Note on [VA-OFFICIAL]: the va.gov page's phone fields rendered blank in text extraction (tel: links stripped by the fetcher — shown as "Main phone: ,"). That is a fetch artefact, not evidence the clinic has no phone. The other official VA source [VA-MARKET] supplies the number explicitly.

### Hours
- **Mon–Fri 7:30 AM – 4:00 PM; Sat–Sun Closed** [VA-OFFICIAL facility hours]
- Corroborated: Google/Meta listing Mon–Fri 7:30 AM–4:00 PM.
- Service-specific variance (do not publish as facility hours): Laboratory service hours on va.gov are Mon–Fri 7:30 AM–noon, walk-in 7:30–8:00 AM, appointments 8:00 AM–noon. Other services state "same as facility hours."

### Website
- **https://www.va.gov/phoenix-health-care/locations/show-low-va-clinic/**
- Status: LOADS — opened successfully 2026-11-21, full content returned. Part of VA Phoenix Health Care System.

### Services [VA-OFFICIAL]
Primary care and specialty health services, including: laboratory and pathology, pharmacy, podiatry, telehealth, plus primary-care coordination of mental health care, women's health care, radiology, social services, labs/blood work. Telehealth specialties listed include mental health, retinal care, dermatology, rehabilitation, primary care, audiology.

### Category (Gilded Pages)
- **medical** — matches precedent: published Cottonwood VA Clinic was placed in Medical Offices / category "medical" (progress file, Day 45).

### Closed / open evidence
- OPEN / ACTIVE: va.gov page live with current facility hours; Google/Meta listing "Operating Status: Active"; VA Marketplace listing live. No closure notice found.

### Conflicts summary
1. Phone 532-1069 vs 537-2044 — SETTLED to 532-1069 (see above).
2. Name long vs short form — use official short form.
3. Lab hours (to noon) vs facility hours (to 4 PM) — publish facility hours; lab variance may be noted.

### Publishable form
```
slug: "big-show-low-va-clinic"
name: "Show Low VA Clinic"
category: "medical"
website: "https://www.va.gov/phoenix-health-care/locations/show-low-va-clinic/"
address: "5171 Cub Lake Road, Suite C380, Show Low, AZ 85901-7850"
  — directory display form used elsewhere: "5171 Cub Lake Rd, Suite C380, Show Low"
phone: "(928) 532-1069"
hours: "Mon–Fri 7:30 AM–4:00 PM; Sat–Sun closed"
note/services: Veterans outpatient clinic of the VA Phoenix Health Care System: primary care, laboratory and pathology, pharmacy, podiatry, and telehealth.
```

---

## 2. White Mountain Periodontal Care — Show Low

### Verdict: PUBLISHABLE — CONFIRMED DISTINCT from Chet Adams DMD

### Exact name
- Inventory / Google place name: **White Mountain Periodontal Care**
- Official site branding: **White Mountain Periodontics** — footer: "White Mountain Periodontics / Benjamin Tingey, DMD / Specializing in Dental Implants and Periodontics" [WM-OFFICIAL, WM-CONTACT]
- Same practice, two name forms. Publish under the inventory name "White Mountain Periodontal Care" and note the site calls itself White Mountain Periodontics. Do not treat them as two businesses.

### Practitioner
- **Benjamin T. Tingey, DMD** [WM-TINGEY: "Benjamin T. Tingey, DMD"; periodontal residency, University of Iowa; private practice in periodontics and implant dentistry since 2012; grew up in Arizona]
- Corroborated: Google place description "Benjamin Tingey DMD is a Periodontist with over 12 years of experience."

### Address
- **51 South White Mountain Road, Suite B, Show Low, AZ 85901** [WM-CONTACT — official contact page, with Suite B]
- Homepage / footer form omits the suite: 51 South White Mountain Road, Show Low, AZ 85901 [WM-OFFICIAL]
- Matches inventory: 51 S White Mountain Rd (suite not in inventory). Publish with Suite B — it is also a distinguisher from co-located practices (see Distinctness).

### Phone
- **(928) 532-3040** [WM-OFFICIAL homepage, WM-CONTACT, Google listing +19285323040] — no conflict.
- Fax (not for directory phone field): (928) 537-4775 [WM-CONTACT]
- Email on site: info@whitemountainperiodontics.com

### Hours — CONFLICT, official wins
- **Publish: Mon–Thu 9:00 AM – 5:00 PM** [WM-CONTACT official "Business Hours: Monday 9:00 AM–5:00 PM, Tuesday 9:00 AM–5:00 PM, Wednesday 9:00 AM–5:00 PM, Thursday 9:00 AM–5:00 PM" — no Friday/weekend hours listed]
- Corroborated: Google listing Mon–Thu 9:00 AM–5:00 PM.
- Conflict: Opencare says "sees patients on Tue, Wed, Thu, Fri" — no times, contradicts official Mon–Thu on both ends (adds Fri, drops Mon). REJECT Opencare; official site + Google agree.
- Friday–Sunday: not listed on official site — treat as closed / not stated, do not invent Friday hours.

### Website
- **https://www.whitemountainperiodontics.com/**
- Status: LOADS — homepage, /contact/, and /meet-dr-tingey/ all opened successfully 2026-11-21, full content returned.

### Services [WM-OFFICIAL homepage list]
Periodontics and dental implants: bone grafting, crown lengthening, dental implants, laser treatment, oral cancer screening, periodontal scaling & root planing, pocket reduction surgery, perio maintenance (cleanings), ridge modification, root amputation, sinus augmentation, soft tissue grafting.

### Category (Gilded Pages)
- **dental** — same category as the published Chet Adams entry; specialty is periodontics within dental.

### Closed / open evidence
- OPEN / ACTIVE: official site live with contact/appointment-request pages; Google listing "Operating Status: Active", Primary Category: Periodontist; Opencare accepting appointment requests. No closure notice found.

### Distinctness from published Chet Adams entry — CONFIRMED DISTINCT
Published entry [PROGRESS / index.html]: slug big-chet-adams-dmd, "Chet Adams DMD", 51 S White Mountain Rd, Show Low, phone (928) 537-2525, website chetadamsdmd.com, general / restorative / cosmetic dentistry (exams, cleanings, X-rays, fluoride, implants, whitening, veneers, crowns); successor practice to Dr. C. Trent Adams (opened 1983, died July 2025), now kept by his son Dr. Chet Adams, DMD (joined 2016).

White Mountain differs on every identifier except street address:
| Field | Chet Adams DMD (published) | White Mountain Periodontal Care |
|---|---|---|
| Doctor | Dr. Chet Adams, DMD | Dr. Benjamin T. Tingey, DMD |
| Phone | (928) 537-2525 | (928) 532-3040 |
| Website | chetadamsdmd.com | whitemountainperiodontics.com |
| Suite | Ste 1 in directory listings for Adams | Suite B [WM-CONTACT] |
| Specialty | General dentistry | Periodontics / dental implants (specialist) |
| Hours | Directory Mon–Thu 8 AM–5 PM (unconfirmed in published entry) | Mon–Thu 9 AM–5 PM (official) |

Same building (51 S White Mountain Rd is a multi-practice dental building — WebMD/Delta listings also place other dentists there, e.g. at the same street address), different practice, different doctor, different phone, different website. NOT a duplicate. Safe to publish as a separate entry; note co-location in the entry note to prevent future de-duplication error.
Historical note: the periodontics site links one procedure page to sheltonperio.com and WebMD lists a Dr. Steven K. Shelton at the same address for periodontal needs — suggesting a predecessor periodontist at this address. That does not affect Tingey's current practice, which the live official site names throughout. Flagged for awareness only; no action needed.

### Conflicts summary
1. Name: Periodontal Care (place/inventory) vs Periodontics (site branding) — same practice; publish inventory name, note site name.
2. Hours: official Mon–Thu 9–5 vs Opencare Tue–Fri (no times) — official wins.
3. Address suite: homepage omits suite, contact page gives Suite B — publish Suite B form.

### Publishable form
```
slug: "big-white-mountain-periodontal-care"
name: "White Mountain Periodontal Care"
category: "dental"
website: "https://www.whitemountainperiodontics.com/"
address: "51 South White Mountain Road, Suite B, Show Low, AZ 85901"
  — directory display form: "51 S White Mountain Rd, Suite B, Show Low"
phone: "(928) 532-3040"
hours: "Mon–Thu 9:00 AM–5:00 PM"
note/services: Periodontics and dental implants practice of Dr. Benjamin Tingey, DMD (site name: White Mountain Periodontics): bone grafting, crown lengthening, dental implants, laser treatment, scaling & root planing, pocket reduction, soft tissue grafting, sinus augmentation. Co-located at 51 S White Mountain Rd with Chet Adams DMD — a different practice, doctor, phone, and website.
```
