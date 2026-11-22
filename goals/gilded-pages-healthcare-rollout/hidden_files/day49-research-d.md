# Day 49 — Research D — Show Low, AZ
## Three healthcare businesses for the Gilded Pages directory

Research date: 2026-11-21 (Arizona time)
Researcher: subagent, batch D
Method: `browser.search` and `browser.open` on official sites and reliable directories only. No data invented. All conflicts listed. Official-site values flagged as preferred where an official site exists.

Inventory inputs given for this batch:
1. White Mountain Pharmacy — Show Low — 4461 S White Mountain Rd — pharmacy — (928) 537-8555
2. Summit Healthcare Pharmacy — Show Low — 4951 S White Mountain Rd Building A — pharmacy — (928) 537-6336
3. Ally Cove Counseling — Show Low — 141 N 6th St — mental health / counseling — (928) 251-1200 — backup pick

---

## 1. White Mountain Pharmacy — Show Low

### Exact name
- **White Mountain Pharmacy** — matches inventory exactly in every source found.
- Sources: Places listing (returned via Instagram / Meta place pages, place_id 1216207742492698); BCBSNM Medicaid Pharmacy Network Directory; RxLess nearby-pharmacy list.

### Address
- Inventory: 4461 S White Mountain Rd, Show Low (no suite, no ZIP given in the task input)
- Places listing: **4461 S White Mountain Rd, Show Low, AZ, US** — no suite, no ZIP shown
- RxLess (nearby list on the Summit Healthcare Pharmacy page, crawled ~2026-11-20): **4461 S White Mountain Rd Ste D2**
- BCBSNM Medicaid Pharmacy Network Directory (Prime Therapeutics, directory page dated 10/31/2026, crawled 2 days before research): **4461 S WHITE MOUNTAIN RD STE E1, SHOW LOW, AZ 85901**
- **CONFLICT — suite:** Ste D2 (RxLess) vs. Ste E1 (BCBSNM, most recently dated directory) vs. no suite (Places). Unresolved. The street address, town, and ZIP 85901 agree in all sources that give them.
- **Publishable address used:** 4461 S White Mountain Rd, Show Low, AZ 85901 — suite omitted because the two suite values conflict. Do not publish either suite without a phone check.

### Phone
- **(928) 537-8555** — confirmed, no conflict.
- Places: +1 928-537-8555. BCBSNM directory: 9285378555. Matches inventory.
- Note: a second location exists in Heber-Overgaard / Overgaard at 2841 AZ-260, phone (928) 535-4300, hours Mon–Fri 9:00 AM–5:00 PM. That is a different location — do not use its phone or hours for the Show Low entry.

### Hours
- Places listing (Show Low): **Monday–Friday 8:30 AM – 5:30 PM**. Saturday and Sunday are not listed — treat as closed / not confirmed, do not invent weekend hours.
- **CONFLICT — opening time (weak, narrative source):** a long-form article on rural pharmacy deserts (IPM United / AZiPRx, "Pharmacy deserts and the cost to rural America") says "When White Mountain Pharmacy opens at 9 a.m." That is narrative prose, not a directory hours table, and may be rounded or older. The Places hours table (8:30 AM) is preferred for publication, with this conflict noted here.
- No official-site hours were available to check, because no official website was found (see Website).

### Website
- **None found / not verified.**
- The Places listing for this business carries no website field in any search return.
- Repeated searches for an official site, including Good Neighbor Pharmacy network searches, returned no official White Mountain Pharmacy (Show Low) website URL. The pharmacy is described in the article above as "part of the Good Neighbor Pharmacy Network," but no store-specific official page URL was returned by search, so **no URL is published** — a guessed mygnp.com / network URL must not be used.
- Status: website = none confirmed. Publish with website omitted / empty.

### Services
From the Places self-description (the business's own description as carried in the listing):
- Fast and friendly service, low wait times
- No-wait refills with MedSync (medication synchronization)
- Multi-dose packaging
- Next-day compounds / compounding
- Delivery
- Mail service
- Immunizations
- Extensive over-the-counter section, including homeopathic medicine and essential oils

Corroboration: the rural-pharmacy article confirms compounding of custom prescriptions at the Show Low location (bioidentical hormones, shingles creams, nerve-pain gels named as examples) and flu-shot clinics in October, and states the pharmacy cares for about 8,000 patients between its Show Low and Heber-Overgaard locations, opened in Show Low in 2017 by pharmacist Nick Bryce.

### Category
- Places primary category: Pharmacy / Drugstore. Secondary: Pharmaceuticals, Medical & Health.
- Gilded Pages category: **pharmacy** (Apothecaries in the directory's category naming).

### Closed / open evidence
- **OPEN.** Places operating status: "Active."
- Listed as a current network pharmacy in the BCBSNM Medicaid Pharmacy Network Directory dated 10/31/2026.
- No closure notice found in any source searched.

### Conflicts — summary
1. Suite: Ste D2 (RxLess) vs. Ste E1 (BCBSNM 10/31/2026) vs. none (Places) — unresolved, suite omitted from publishable form.
2. Opening time: 8:30 AM (Places hours table, preferred) vs. "opens at 9 a.m." (narrative article) — Places preferred.
3. Weekend hours: not listed anywhere found — not confirmed, not invented.

### Verdict: PUBLISHABLE (with cautions above)
Publishable form:
```
name:     White Mountain Pharmacy
slug:     white-mountain-pharmacy
category: pharmacy / Apothecaries
address:  4461 S White Mountain Rd, Show Low, AZ 85901
phone:    (928) 537-8555
hours:    Mon–Fri 8:30 AM – 5:30 PM
website:  (none confirmed — omit)
services: Prescription filling, compounding (next-day compounds), MedSync refills,
          multi-dose packaging, delivery, mail service, immunizations, over-the-counter
note:     Suite number conflicts in directories (Ste D2 vs Ste E1) — omitted pending phone check.
          Weekend hours not confirmed.
```

---

## 2. Summit Healthcare Pharmacy — Show Low

### Exact name
- **Summit Healthcare Pharmacy** — matches inventory.
- Official site page title / heading context: Summit Healthcare "On-site Retail Pharmacy" / "Retail Pharmacy" at the Summit Healthcare Outpatient Pavilion.
- Note the spelling in RxLess: "SUMMIT HEALTCARE PHARMACY" is an RxLess typo — do not use it.

### Address
- Inventory: 4951 S White Mountain Rd Building A, Show Low
- **Official site (PREFERRED): 4951 S White Mountain Road, Building A, Show Low, AZ 85901**
  - Source: https://summithealthcare.net/on-site-retail-pharmacy/ — fetched with `browser.open` on 2026-11-21, page crawled 2026-11-21 09:33 UTC, loads successfully.
- Places listing: 4951 S White Mountain Rd Building A, Show Low, AZ, US — matches official.
- RxLess: 4951 S White Mountain Rd Bldg A, Show Low, AZ 85901 — matches official. NPI 1811468804, NCPDP 0360468.
- **No address conflict.**

### Phone
- **(928) 537-6336** — confirmed on the official site, no conflict.
- Official site, verbatim: "Call Us Today at 928-537-6336 or text RXLOCAL to 64890 for any questions or concerns."
- Places: +1 928-537-6336. Matches inventory.
- **Do-not-confuse numbers at the same building / organisation:** (928) 537-6700 is the Summit Healthcare Outpatient Pavilion / Family Medicine number for Building A, and (928) 537-4375 is Summit Healthcare's main line / main campus. Neither is the pharmacy number. The pharmacy-specific 537-6336 is the correct, official value.

### Hours
- **Official site lists NO hours** for the pharmacy on the page fetched 2026-11-21 — hours are therefore not official-site confirmed.
- Places listing: **Monday–Thursday 8:00 AM – 5:00 PM, Friday 8:00 AM – 12:00 PM**. Saturday and Sunday not listed.
- Corroboration for that pattern: Summit Healthcare's own Family Medicine page lists the Summit Healthcare Outpatient Pavilion, 4951 S White Mountain Road, Building A, with hours "Monday – Thursday | 8 AM – 5 PM, Friday | 8 AM – 12 PM" — the same building pattern, from the official domain, though for the clinic, not the pharmacy counter itself.
- **CONFLICT — RxLess hours:** RxLess lists "Mon–Sun: 7:00am–5:00pm," which conflicts with the Places hours on every day (opening time, Friday closing, and weekend opening). RxLess is the weaker source — its Summit text is generic ("may include") boilerplate — so **Places hours are preferred and RxLess hours are rejected for publication**, with the conflict recorded here.
- Publishable hours: Mon–Thu 8:00 AM – 5:00 PM, Fri 8:00 AM – 12:00 PM, with the note "hours not confirmed on official site."

### Website
- **https://summithealthcare.net/on-site-retail-pharmacy/**
- **Verified: loads.** `browser.open` succeeded on 2026-11-21 (crawl timestamp 2026-11-21 09:33 UTC), returning the pharmacy page with the Building A address and the 537-6336 phone number.
- Places listing gives the identical URL as the business website — official and directory agree.

### Services
- Official site (as fetched): on-site retail pharmacy at the Outpatient Pavilion; phone contact and text contact (RXLOCAL to 64890) for questions. The fetched official page text does not enumerate further services — do not add services on official-site authority.
- RxLess (secondary, unverified, worded as "may include"): traditional prescription filling, medication therapy management, immunization services, medication synchronization, online prescription refills, personalized medication packaging; and service flags: No drive-up, No delivery, Not open 24 hours. Treat these as directory claims only, not official-site confirmed.
- Summit Healthcare organisational material lists "On-site Retail Pharmacy" among its services — corroborates that the retail pharmacy exists as a standing service.

### Category
- Places primary category: Pharmacy / Drugstore.
- Gilded Pages category: **pharmacy** (Apothecaries in the directory's category naming).

### Closed / open evidence
- **OPEN.** Places operating status: "Active."
- Official pharmacy page is live on summithealthcare.net as of 2026-11-21.
- No closure notice found.

### Conflicts — summary
1. Hours: Places Mon–Thu 8–5 / Fri 8–12 (preferred, corroborated by the Building A clinic pattern on the official domain) vs. RxLess Mon–Sun 7–5 (rejected, generic directory) vs. official pharmacy page, which lists no hours at all.
2. Phone look-alikes: 537-6700 (pavilion / family medicine) and 537-4375 (main line) are NOT the pharmacy — pharmacy is 537-6336, official.

### Verdict: PUBLISHABLE
Publishable form:
```
name:     Summit Healthcare Pharmacy
slug:     summit-healthcare-pharmacy
category: pharmacy / Apothecaries
address:  4951 S White Mountain Rd, Building A, Show Low, AZ 85901
phone:    (928) 537-6336
hours:    Mon–Thu 8:00 AM – 5:00 PM; Fri 8:00 AM – 12:00 PM
          (hours from directory listing; official site lists no pharmacy hours)
website:  https://summithealthcare.net/on-site-retail-pharmacy/  — verified loading 2026-11-21
services: On-site retail pharmacy at Summit Healthcare Outpatient Pavilion —
          prescription filling; call or text RXLOCAL to 64890 for questions
note:     RxLess hours (Mon–Sun 7 AM–5 PM) conflict and were not used.
```

---

## 3. Ally Cove Counseling — Show Low — BACKUP PICK

### Exact name
- **Ally Cove Counseling** — as given in inventory, and as carried in the single listing found (see below). No second source confirms the name.
- **Do-not-confuse names found in searching, none of which are this business:** allcove (a California youth-centre network, ages 12–25 — different name spelling and concept), Ally Schulz MS, LPC / Frisco Counseling and Wellness (Texas), Ally Christian Counseling, Alva Counseling LLC (Oregon, NPI listing), Cove Therapy / THE COVE (a different practice). None of these may be used as sources for this entry.

### Address
- Inventory / single listing: **141 N 6th St, Show Low, AZ, US** — no ZIP in the listing (Show Low ZIP 85901 is the town ZIP, but the listing itself does not state it for this business).
- Only source: Places listing returned via Meta, place_id 191097177278322, coordinates 34.251085, -110.035842.
- No second directory, official site, licensing listing, or NPI listing confirming this address was found.

### Phone
- **(928) 251-1200** — single source only: Places listing, +1 928-251-1200. Matches inventory.
- No second source confirms this number for this business. Repeated exact searches on the name, the phone number, and the street address returned only the same single Places listing.

### Hours
- Places listing, **incomplete: Monday 8:00 AM – 5:00 PM, Tuesday 8:00 AM – 5:00 PM only.** Wednesday–Sunday are missing from the listing entirely — not stated as closed, simply absent.
- No other hours source exists. Full-week hours cannot be published from this evidence.

### Website
- **None found.** The single Places listing carries no website field, and no official site for "Ally Cove Counseling" in Show Low was returned by any search performed. Status: no website verified, none to publish.

### Services
- **None evidenced beyond the category word "Counselor."** The single listing gives no description, no services list, no practitioner name, and no specialties. No services may be stated for this entry without further verification — inventing counselling specialties would be fabrication.

### Category
- Places primary category: Counselor.
- Gilded Pages category (proposed, if it later verifies): **mental health / counseling** — as given in inventory.

### Closed / open evidence
- The single Places listing says Operating Status: "Active." That is the ONLY open evidence, and it is uncorroborated by any second source, official site, review, licensing record, or directory found in this research.

### Conflicts — summary
- No internal conflicts, because there is only one source. The problem is absence, not disagreement:
  1. Single-source for name, address, and phone — no corroboration anywhere else searched (general web, Psychology Today, NPI registry returns, Arizona treatment locators).
  2. Hours incomplete — only Monday and Tuesday are listed.
  3. No website, no services, no practitioner, no description in any source found.

### Verdict: HELD — do not publish yet
Reason: single uncorroborated directory listing with incomplete hours and no website, services, or second source. This entry needs a phone check first — call (928) 251-1200 to confirm the business exists at 141 N 6th St, Show Low, and to obtain full hours, services, practitioner name, and any website — before it can be published. It remains usable as the backup pick only after that check passes.

Held form (for the call sheet, NOT for publication):
```
name:     Ally Cove Counseling              [HELD — phone check required]
category: mental health / counseling (proposed)
address:  141 N 6th St, Show Low, AZ        [single source]
phone:    (928) 251-1200                    [single source]
hours:    Mon–Tue 8:00 AM – 5:00 PM only in listing; Wed–Sun unknown
website:  none found
services: none evidenced
```

---

## Batch summary

| # | Business | Verdict | Website status |
|---|----------|---------|----------------|
| 1 | White Mountain Pharmacy | PUBLISHABLE — suite omitted (D2 vs E1 conflict), no website | None found — omit |
| 2 | Summit Healthcare Pharmacy | PUBLISHABLE — official address/phone/website confirmed; hours from directory, official site lists none | https://summithealthcare.net/on-site-retail-pharmacy/ — loads, verified 2026-11-21 |
| 3 | Ally Cove Counseling | HELD — single source, incomplete hours, no website/services | None found |

Sources used in this report (all accessed 2026-11-21):
- Official: summithealthcare.net/on-site-retail-pharmacy/ (browser.open, crawled 2026-11-21 09:33 UTC); summithealthcare.net Family Medicine / Outpatient Pavilion page (Building A hours pattern)
- Directories / listings: Places listings for all three businesses (via Meta / Instagram place pages, with place_ids cited per entry); RxLess pharmacy page for Summit Healthcare Pharmacy, NPI 1811468804 (browser.open); BCBSNM Medicaid Pharmacy Network Directory, Prime Therapeutics, dated 10/31/2026 (White Mountain Pharmacy Ste E1 listing)
- Narrative corroboration (White Mountain only): "Pharmacy deserts and the cost to rural America," IPM United / AZiPRx — compounding, flu clinics, 2017 opening, ~8,000 patients across two locations
