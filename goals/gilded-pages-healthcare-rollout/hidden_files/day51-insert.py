#!/usr/bin/env python3
import pathlib
p = pathlib.Path.home() / "workspace/BACKUP-github-websites-only/gilded-pages/index.html"
t = p.read_text()

entries = """,
{
  slug: "big-distinctive-dental-care", name: "Distinctive Dental Care", category: "dental", big: true, lastChecked: "November 23, 2026",
  img: "big-distinctive-dental-care.webp",
  website: "https://wulffdmd.com/",
  alt: "Engraving of a tooth-healer's hall in Prescott with pine trees behind it - a man dentist in his fifties with a round face, light-brown skin, short dark-brown hair with a receding hairline and a stocky build, holding a small mirror tool, examining the teeth of a seated woman in her forties with a long oval face, pale skin, red hair in a single braid and a slender build",
  intro: "The Stillwater Drive tooth-healers - family dentistry in Prescott by the Drs. Wulff, father and son.",
  locations: [
    { hold: "Prescott", address: "3140 Stillwater Dr Ste B, Prescott", phone: "(928) 445-3181", hours: "Mon-Thu 8 AM-5 PM; Fri 8 AM-3 PM; Sat-Sun closed", note: "Per its official site, checked live this run (the site blocks this machine's plain fetch, but opened live in research): general, cosmetic and surgical dentistry by Dr. Paul Wulff and Dr. Aaron Wulff - exams, cleanings, whitening, veneers, root canals, implants, extractions, dentures, CEREC same-day crowns and emergency care; accepting new patients. A place record lists a different phone, (928) 275-8561 - the official site's (928) 445-3181 is the number printed here." }
  ]
},
{
  slug: "big-prescott-periodontics", name: "Prescott Periodontics and Implant Dentistry", category: "dental", big: true, lastChecked: "November 23, 2026",
  img: "big-prescott-periodontics.webp",
  website: "https://www.prescottperio.com/",
  alt: "Engraving of a gum-healer's hall in Prescott, a stone building among pines - an older man healer in his late sixties with a square jaw, fair skin, a full white beard and thinning grey hair, tall and broad build, placing a tiny carved tooth implant, watched by a younger woman assistant in her twenties with a heart-shaped face, olive skin, black hair tied in a high knot and a petite build",
  intro: "The Stillwater Drive gum and implant hall - periodontics in Prescott by Dr. Jirsa and his partners.",
  locations: [
    { hold: "Prescott", address: "3124 Stillwater Dr, Prescott", phone: "(928) 778-2340", hours: "Mon-Fri 8 AM-5 PM; Sat-Sun closed", note: "Per its official site, checked live this run: gum disease treatment, dental implants, extractions, sinus and bone grafting, crown lengthening, soft tissue grafting and LANAP laser care, by Dr. Richard C. Jirsa, DDS, MS, Dr. Todd Walker and Dr. Rishi Guha. Dr. Jirsa retires at the end of 2026 (last day December 23, 2026, per the site's own notice); his partners continue care and records stay with the practice. A second hall of the same practice stands in Prescott Valley." }
  ]
},
{
  slug: "big-now-mens-health", name: "NOW Men's Health", category: "medical", big: true, lastChecked: "November 23, 2026",
  img: "big-now-mens-health.webp",
  website: "http://www.nowmenshealth.care/",
  alt: "Engraving of a men's health clinic hall in old Prescott, a wooden storefront on a historic street - a muscular man patient in his thirties with a chiselled face, tan skin, short black hair and a short boxed beard, athletic build, talking with a woman healer in her fifties with a narrow face, fair freckled skin, shoulder-length silver-streaked auburn hair and a medium build, holding a vial of tonic",
  intro: "The McCormick Street men's health hall - hormone and wellness care in Prescott, formerly Tri-City Men's Health.",
  locations: [
    { hold: "Prescott", address: "215 N McCormick St, Prescott", phone: "(928) 212-2772", hours: "Mon 1-6 PM; Tue-Fri 9 AM-6 PM; Sat 9 AM-1 PM; Sun closed, by appointment only", note: "Per its official site, checked live this run: testosterone and hormone therapy, sexual health and ED care, medical weight loss, and IV hydration and vitamin therapy. This hall was listed before as Tri-City Men's Health - the same clinic under its new name, not a second practice. Its site names no single doctor. NOW Mental Health stands at the same address on a different phone - a different service." }
  ]
},
{
  slug: "big-azopt-prescott", name: "AzOPT - Arizona Orthopedic Physical Therapy, Prescott", category: "physical", big: true, lastChecked: "November 23, 2026",
  img: "big-azopt-prescott.webp",
  website: "https://azopt.net/azopt-prescott-physical-therapy/",
  alt: "Engraving of a bone-setter's therapy hall in Prescott - a woman therapist in her thirties with a diamond-shaped face, medium-brown skin, curly dark hair pulled back in a low ponytail and a lean athletic build, guiding a man patient in his sixties with a long face, pale skin, a bald head with a grey fringe and a heavy build, stretching his arm with a wooden pulley rope",
  intro: "The Stillwater Drive bone-setters - orthopedic physical therapy in Prescott by licensed therapists only.",
  locations: [
    { hold: "Prescott", address: "3180 Stillwater Dr Ste B, Prescott", phone: "(928) 515-3118", hours: "Mon-Thu 7 AM-7 PM; Fri 7 AM-3:30 PM; Sat-Sun closed", note: "Per its official Prescott page, checked live this run (the site blocks this machine's plain fetch, but opened live in research): orthopedic physical therapy, dry needling, joint replacement and pre- and post-surgical rehabilitation, sports therapy, balance and gait work, blood flow restriction and vestibular care, at this address since July 20, 2026. The number printed is this hall's own direct line; the chain's central number is different. Kids Place North, the chain's children's arm, shares this suite and phone." }
  ]
},
{
  slug: "big-peterson-physical-therapy", name: "Peterson Physical Therapy", category: "physical", big: true, lastChecked: "November 23, 2026",
  img: "big-peterson-physical-therapy.webp",
  website: "https://petersonpt.com/",
  alt: "Engraving of a therapy hall in Prescott with a wooden water-wheel pool for healing exercise - a man therapist in his forties with a broad forehead, light skin, wavy blond hair to his shoulders and a wiry build, helping a woman patient in her seventies with a round wrinkled face, warm brown skin, short white curly hair and a small frail build, walk in the shallow pool",
  intro: "The Iron Springs Road therapy hall - physical therapy in Prescott since 1999, with a HydroWorx pool.",
  locations: [
    { hold: "Prescott", address: "1320 W Iron Springs Rd, Prescott", phone: "(928) 771-2977", hours: "Mon-Thu 8 AM-5 PM; Fri 8 AM-12 PM; Sat-Sun closed (directory - hours not confirmed on its official site)", note: "Per its official site, checked live this run, and directories for the hours: aquatic therapy in a HydroWorx pool, land-based and manual therapy, exercise therapy, balance work, work hardening, traction and taping. An older form stands on its legacy domain - this entry's site is its current one." }
  ]
},
{
  slug: "big-chain-reaction-pt", name: "Chain Reaction Physical Therapy", category: "physical", big: true, lastChecked: "November 23, 2026",
  img: "big-chain-reaction-pt.webp",
  website: "https://www.chainreactionpt.com/",
  alt: "Engraving of a sports-healing hall in Prescott with a wooden riding frame shaped like a horse - a woman therapist in her thirties with an angular face, pale skin, straight black hair in a bob cut and a tall slender build, coaching a young man athlete in his twenties with a boyish round face, deep-brown skin, short coiled hair and a compact muscular build, lifting a stone weight",
  intro: "The Miller Valley Road sports-healing hall - one-on-one physical therapy in Prescott by Dr. Duppler.",
  locations: [
    { hold: "Prescott", address: "621 Miller Valley Rd Ste A, Prescott", phone: "(928) 379-6390", hours: "Mon-Thu 9 AM-5 PM; Fri 9 AM-3 PM", note: "Per its official site, checked live this run: one-on-one physical therapy, sports rehabilitation, telehealth visits and bike fitting, by owner Jessie Duppler, PT, DPT. Care is out-of-network, per its site. Directory hours disagree with the official site's - the official hours are the ones printed here; Saturday and Sunday hours are not listed, so ring ahead for weekends." }
  ]
},
{
  slug: "big-walgreens-prescott", name: "Walgreens - Prescott", category: "pharmacy", big: true, lastChecked: "November 23, 2026",
  img: "big-walgreens-prescott.webp",
  website: "https://www.walgreens.com/locator/walgreens-178+e+sheldon+st-prescott-az-86301/id=2555",
  alt: "Engraving of an apothecary shop in old Prescott, shelves of glass tonic bottles and herb bundles - an apothecary man in his forties with a long narrow face, olive skin, dark hair in a low tail and a medium build, handing a small bottle to an older woman customer in her sixties with a square face, fair skin, grey hair in a bun and a stout build",
  intro: "The Prescott apothecaries - Walgreens' two Prescott stores, on Sheldon Street and Willow Creek Road.",
  locations: [
    { hold: "Prescott", address: "178 E Sheldon St, Prescott", phone: "(928) 776-1936", hours: "Store: Mon-Sat 7 AM-11 PM; Sun 8 AM-10 PM", note: "Store hours per Walgreens' official locator page, checked live this run. Pharmacy hours were not confirmed this run - ring ahead for the pharmacy counter. This is store #2555." },
    { hold: "Prescott", address: "1310 Willow Creek Rd, Prescott", phone: "(928) 227-9965", hours: "Store: daily 7 AM-10 PM", note: "Store hours per Walgreens' official locator page, checked live this run. Pharmacy hours were not confirmed this run - ring ahead for the pharmacy counter. This is store #9292. The Prescott Valley Walgreens is a separate store in a different town." }
  ]
}
"""

anchor = "\n\n\n];\n    CATEGORIES = CATEGORIES.concat(BIG_CATEGORIES);"
assert anchor in t, "BIG_VENDORS closing anchor not found"
assert "big-distinctive-dental-care" not in t
t = t.replace(anchor, entries + anchor, 1)
p.write_text(t)
print("inserted 7 entries")
