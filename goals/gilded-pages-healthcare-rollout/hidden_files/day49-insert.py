#!/usr/bin/env python3
import pathlib
p = pathlib.Path.home() / "workspace/BACKUP-github-websites-only/gilded-pages/index.html"
t = p.read_text()

entries = """,
{
  slug: "big-audiology-inc-show-low", name: "Audiology, Inc. - Show Low", category: "hearing", big: true, lastChecked: "November 21, 2026",
  img: "big-audiology-inc-show-low.webp",
  website: "https://www.audiologyinc.net/",
  alt: "Engraving of a hearing clinic in Show Low - a woman audiologist in her sixties with a round face, olive skin, long silver-grey hair in a braid and a slight build, fitting a brass ear trumpet for a tall thin young man in his twenties with a narrow face, dark brown skin, short black curly hair and a beard",
  intro: "The White Mountain Road ear-healers - a family-owned audiology hall in Show Low since 2006.",
  locations: [
    { hold: "Show Low", address: "2600 S White Mountain Rd, Show Low", phone: "(928) 251-4614", hours: "Mon, Tue, Thu 8:30 AM-5 PM; Wed 9 AM-5 PM; Fri 8:30 AM-12 PM", note: "Per its official site, checked live this run: hearing evaluations, hearing aids fitted and programmed with real-ear measurement, cleaning and repairs, tinnitus care and balance testing, by Doctors of Audiology. PHONE NOTE: the published number is its official site's current Show Low number; the inventory number (928) 358-5604 and an older (928) 537-3456 stand superseded. A place listing also shows a midday closure the official site does not print." }
  ]
},
{
  slug: "big-labcorp-show-low", name: "Labcorp - Show Low", category: "labs", big: true, lastChecked: "November 21, 2026",
  img: "big-labcorp-show-low.webp",
  website: "https://locations.labcorp.com/az/show-low/20361/",
  alt: "Engraving of a laboratory hall in Show Low - a man laboratory keeper in his forties with a square jaw, pale skin, a bald head with a fringe of blond hair and a stocky build, holding glass vials, beside a woman assistant in her thirties with an oval face, light brown skin, dark hair in a tight bun and a medium build",
  intro: "The Cub Lake Road testing hall - Labcorp's Show Low patient service center.",
  locations: [
    { hold: "Show Low", address: "5171 S Cub Lake Rd Ste 250, Show Low", phone: "(928) 532-0431", hours: "Mon-Fri 7 AM-3 PM; Sat-Sun closed", note: "Per its official location page, checked live this run: routine lab work, pediatric collection, hair collection, saliva alcohol testing, H. pylori breath test, fingerprinting and employee wellness screening; walk-ins welcome. The VA Clinic stands in the same building at Suite C380 on a different phone - a different hall." }
  ]
},
{
  slug: "big-sonora-quest-show-low", name: "Sonora Quest Laboratories - Show Low", category: "labs", big: true, lastChecked: "November 21, 2026",
  img: "big-sonora-quest-show-low.webp",
  website: "https://www.sonoraquest.com/patients/appointments/",
  alt: "Engraving of a blood-testing laboratory in Show Low - an elderly man in his seventies with a long weathered face, tan skin, a white moustache and wispy white hair, lean build, tended by a young woman in her twenties with a heart-shaped face, fair freckled skin, red hair in two plaits and a petite build",
  intro: "The Show Low Lake Road testing hall - Sonora Quest's Show Low patient service center.",
  locations: [
    { hold: "Show Low", address: "2450 E Show Low Lake Rd Ste 3B, Show Low", phone: "(928) 532-1745", hours: "Mon-Fri 7 AM-4 PM; Sat-Sun closed", note: "Clinical and diagnostic laboratory testing and specimen collection, per its official location listing, checked live this run. PHONE NOTE: the published number is the one on the live official location page; printed lists from early 2026 give (928) 532-1752 - ring ahead if the first number does not answer. Older printed lists also show a midday closure the live page does not print. Distinct from the Payson and Cottonwood halls of the same name." }
  ]
},
{
  slug: "big-show-low-va-clinic", name: "Show Low VA Clinic", category: "medical", big: true, lastChecked: "November 21, 2026",
  img: "big-show-low-va-clinic.webp",
  website: "https://www.va.gov/phoenix-health-care/locations/show-low-va-clinic/",
  alt: "Engraving of a veterans healing hall in Show Low - a veteran man in his fifties with a broad face, medium brown skin, greying buzz-cut hair and a heavy muscular build, tended by a woman healer in her forties with a long face, deep brown skin, black hair worn loose past her shoulders and a tall slender build",
  intro: "The Cub Lake Road hall for veterans - the VA Phoenix system's Show Low clinic.",
  locations: [
    { hold: "Show Low", address: "5171 Cub Lake Rd Ste C380, Show Low", phone: "(928) 532-1069", hours: "Mon-Fri 7:30 AM-4 PM; Sat-Sun closed", note: "Per the VA's official pages, checked live this run: primary care, laboratory and pathology, pharmacy, podiatry and telehealth for enrolled veterans. PHONE NOTE: the published number is the VA's own main number for this clinic; an older directory's (928) 537-2044 is a separate veterans assistance contact, not this clinic. Labcorp stands in the same building at Suite 250 on a different phone." }
  ]
},
{
  slug: "big-white-mountain-periodontal-care", name: "White Mountain Periodontal Care", category: "dental", big: true, lastChecked: "November 21, 2026",
  img: "big-white-mountain-periodontal-care.webp",
  website: "https://www.whitemountainperiodontics.com/",
  alt: "Engraving of a gum-healers dental hall in Show Low - a man dentist in his thirties with a triangular face, fair skin, wavy chestnut hair to his shoulders and a wiry build, examining the teeth of an elderly woman in her eighties with a small round face, pale skin, short white bobbed hair and a frail build",
  intro: "The gum and implant hall on White Mountain Road - periodontics by Dr. Tingey.",
  locations: [
    { hold: "Show Low", address: "51 S White Mountain Rd Ste B, Show Low", phone: "(928) 532-3040", hours: "Mon-Thu 9 AM-5 PM", note: "Per its official site, checked live this run: periodontics and implants by Dr. Benjamin T. Tingey, DMD - bone grafting, crown lengthening, dental implants, laser treatment, scaling and root planing, pocket reduction and soft tissue grafting. It stands in the same building as the Chet Adams dental hall - a different practice, doctor, phone and suite." }
  ]
},
{
  slug: "big-white-mountain-pharmacy", name: "White Mountain Pharmacy", category: "pharmacy", big: true, lastChecked: "November 21, 2026",
  img: "big-white-mountain-pharmacy.webp",
  alt: "Engraving of an apothecary shop in Show Low - a woman apothecary in her fifties with a wide face, golden-brown skin, dark hair streaked with grey in a low ponytail and a plump build, grinding herbs with a pestle, serving a young father in his thirties with a chiselled face, fair skin, short sandy hair and an athletic build holding a small child",
  intro: "The White Mountain Road apothecary - an independent Show Low pharmacy opened in 2017.",
  locations: [
    { hold: "Show Low", address: "4461 S White Mountain Rd, Show Low", phone: "(928) 537-8555", hours: "Mon-Fri 8:30 AM-5:30 PM", note: "Directory entry: no official website was found, so no website is printed. Per its place listing and a current insurer directory, checked this run: MedSync refills, multi-dose packaging, next-day compounding, delivery, mail service and immunizations. Its suite is given differently across directories, so no suite is printed - ring ahead. A second hall stands in Heber-Overgaard." }
  ]
},
{
  slug: "big-summit-healthcare-pharmacy", name: "Summit Healthcare Pharmacy", category: "pharmacy", big: true, lastChecked: "November 21, 2026",
  img: "big-summit-healthcare-pharmacy.webp",
  website: "https://summithealthcare.net/on-site-retail-pharmacy/",
  alt: "Engraving of a hospital apothecary counter in Show Low - a man apothecary in his sixties with a gaunt face, light skin, a long grey beard and thinning grey hair, tall and stooped, handing a small bottle to a woman in her forties with a diamond-shaped face, olive skin, black hair in a crown braid and a medium build",
  intro: "The hospital's own apothecary - Summit Healthcare's retail pharmacy in Building A.",
  locations: [
    { hold: "Show Low", address: "4951 S White Mountain Rd Building A, Show Low", phone: "(928) 537-6336", hours: "Mon-Thu 8 AM-5 PM; Fri 8 AM-12 PM", note: "Per its official pharmacy page, checked live this run: the on-site retail pharmacy of Summit Healthcare Regional Medical Center, in Building A. Hours rest on place listings and the hospital's own Building A hours pattern - its pharmacy page prints no hours, so ring ahead. The pharmacy number is its own; the hospital's main and clinic lines are different numbers." }
  ]
}
"""

anchor = '  slug: "big-miracle-ear-show-low"'
i = t.find(anchor)
assert i != -1, "anchor slug not found"
# find the end of that entry: the first occurrence of "\n}\n" after the anchor, followed by the array close
end_marker = "\n}\n"
j = t.find(end_marker, i)
assert j != -1
insert_at = j + len("\n}")
# what follows must be the BIG_VENDORS array close
following = t[insert_at:insert_at+20]
assert "]" in following.split(";")[0] or following.strip().startswith("]"), repr(following)
new = t[:insert_at] + entries + t[insert_at:]
p.write_text(new)
print("inserted; following was:", repr(following))
print("new length", len(new))
