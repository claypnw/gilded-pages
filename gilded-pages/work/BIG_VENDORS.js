var BIG_VENDORS = [
/* ---------------- LARDERS & PROVISIONS ---------------- */
{
  slug: "big-walmart", name: "Walmart Supercenter", category: "larders", big: true,
  img: "big-walmart.webp",
  website: "https://www.walmart.com",
  alt: "Engraving of a grand provisioning hall — Nord shoppers with baskets, a clerk handing a parcel to a family, dragon carving over the door",
  intro: "The grand provisioning — fill thy wagon once and the whole of the Holds becomes thy larder: Rim picnics, fire-pit firewood, and not a mid-week run back to town.",
  locations: [
    { hold: "Payson", address: "300 N Beeline Hwy, Payson", phone: "(928) 474-0029", hours: "Open daily 6 AM–11 PM", note: "Pharmacy (928) 474-0034: Mon–Sat 9 AM–7 PM, Sun 10 AM–6 PM." },
    { hold: "Show Low", address: "5401 S White Mountain Rd, Show Low", phone: "(928) 537-3141", hours: "Open daily 6 AM–11 PM", note: "Auto Care Center on site." },
    { hold: "Prescott", address: "3050 E State Route 69, Prescott", phone: "(928) 445-1113", hours: "Open daily 6 AM–11 PM", note: "" },
    { hold: "Prescott", address: "1280 Gail Gardner Way, Prescott", phone: "(928) 541-0071", hours: "Open daily 6 AM–11 PM", note: "Second Prescott store, west side." }
  ]
},
{
  slug: "big-safeway", name: "Safeway", category: "larders", big: true,
  img: "big-safeway.webp",
  website: "https://www.safeway.com",
  alt: "Engraving of a friendly grocery hall — cheese wheels, bread loaves and salmon on ice, a Khajiit shopper sniffing a cheese wheel",
  intro: "The neighborhood larder — cheese wheels, fresh-baked bread, and a proper deli counter; many a Hearth supper has been saved by this hall.",
  locations: [
    { hold: "Payson", address: "401 State Route 260, Payson", phone: "(928) 472-8208", hours: "Open daily 6 AM–10 PM", note: "Pharmacy (928) 472-8242. Fuel station at 201 E Hwy 260, daily 4 AM–10 PM. In-store Starbucks." },
    { hold: "Sedona", address: "2300 W Hwy 89A, Sedona", phone: "(928) 282-0118", hours: "Open daily 6 AM–10 PM", note: "Pharmacy (928) 282-1712. Only Safeway in Sedona." },
    { hold: "Show Low", address: "900 W Deuce Of Clubs, Show Low", phone: "(928) 532-5656", hours: "Open daily 6 AM–10 PM", note: "Pharmacy (928) 532-5659. Bakery, deli, floral, sushi, Starbucks; DriveUp & Go pickup." },
    { hold: "Prescott", address: "450 White Spar Rd, Prescott", phone: "(928) 778-3086", hours: "Open daily 6 AM–10 PM", note: "Pharmacy, bakery, deli, Starbucks, DriveUp & Go." },
    { hold: "Prescott", address: "1044 Willow Creek Rd, Prescott", phone: "(928) 445-4550", hours: "Open daily 6 AM–10 PM", note: "Second Prescott store — same larder, north side." }
  ]
},
{
  slug: "big-costco", name: "Costco", category: "larders", big: true,
  img: "big-costco.webp",
  website: "https://www.costco.com/warehouse-locations/prescott-az-466.html",
  alt: "Engraving of a grand timber warehouse — bulk barrels of mead and grain, shoppers with carts, a clerk handing out samples",
  intro: "The warehouse of wonders — cheese wheels by the cartload and mead by the barrel; a membership token is required at the door, and the samples are free.",
  locations: [
    { hold: "Prescott", address: "3911 E State Route 69, Prescott", phone: "(928) 541-2203", hours: "Mon–Fri 10 AM–8:30 PM; Sat 9:30 AM–7 PM; Sun 10 AM–6 PM", note: "Membership required. Gas station, food court, pharmacy (928) 541-2218, Tire Center (928) 541-2213, Optical (928) 541-2214." }
  ]
},
{
  slug: "big-target", name: "Target", category: "larders", big: true,
  img: "big-target.webp",
  website: "https://www.target.com/sl/prescott/884",
  alt: "Engraving of a cheerful general store — clothing racks, a delighted shopper holding up a lantern, shelves of provisions and candles",
  intro: "The cheerful general store — tunics, lanterns, and everything betwixt; pop in for one thing and leave with a cart of treasures.",
  locations: [
    { hold: "Prescott", address: "1851 E Highway 69, Prescott", phone: "(928) 771-8400", hours: "Mon–Sat 8 AM–10 PM; Sun 8 AM–9 PM", note: "Order Pickup and Drive Up available; wine & beer sold." }
  ]
},
{
  slug: "big-ross", name: "Ross Dress for Less", category: "larders", big: true,
  img: "big-ross.webp",
  website: "https://www.rossstores.com/",
  alt: "Engraving of a discount clothing hall — racks of tunics and cloaks with septim bargain tags, shoppers happily hunting",
  intro: "The bargain hunter's dungeon — racks of tunics, cloaks, and boots at prices that make even a miser smile; the treasure changes daily, so strike when thou seest.",
  locations: [
    { hold: "Show Low", address: "4441 S White Mountain Rd, Show Low", phone: "(928) 532-1160", hours: "Mon–Thu 9 AM–9 PM; Fri–Sat 8:30 AM–10 PM; Sun 9:30 AM–8:30 PM", note: "Same center as Big 5." },
    { hold: "Prescott", address: "1931 E State Route 69, Prescott", phone: "(928) 445-4604", hours: "Mon–Thu 9 AM–8:30 PM; Fri–Sat 9 AM–10:30 PM; Sun 9 AM–9:30 PM", note: "" }
  ]
},
{
  slug: "big-big5", name: "Big 5 Sporting Goods", category: "larders", big: true,
  img: "big-big5.webp",
  website: "https://www.big5sportinggoods.com/",
  alt: "Engraving of a sporting goods outfitter — boots, fishing rods, packs and tents, a Nord family picking packs for a Rim trip",
  intro: "The outfitter's hall — packs, rods, and boots for thy Rim adventures; gear up here and the trails are thine.",
  locations: [
    { hold: "Show Low", address: "4441 S White Mountain Rd #101, Show Low", phone: "(928) 537-5551", hours: "Mon–Thu 9:30 AM–8:30 PM; Fri 9:30 AM–9 PM; Sat 9 AM–8:30 PM; Sun 9:30 AM–8 PM", note: "Camping, fishing, and hunting gear; same center as Ross." }
  ]
},
{
  slug: "big-staples", name: "Staples", category: "larders", big: true,
  img: "big-staples.webp",
  website: "https://stores.staples.com/az/prescott/186-e.-sheldon-st.",
  alt: "Engraving of a Nord stationer's — paper stacks, quills, ink bottles and scrolls, a clerk helping a traveler at a great press",
  intro: "The scribe's supply — paper, quills, and inkpots by the ream; print thy maps and post thy parcels.",
  locations: [
    { hold: "Prescott", address: "186 E Sheldon St, Prescott", phone: "(928) 776-0041", hours: "Mon–Fri 8 AM–7 PM; Sat 9 AM–6 PM; Sun 11 AM–6 PM", note: "Print & marketing services, passport photos, shipping services." }
  ]
},
{
  slug: "big-officedepot", name: "Office Depot", category: "larders", big: true,
  img: "big-officedepot.webp",
  website: "https://www.officedepot.com",
  alt: "Engraving of a post and supplies counter — a clerk weighing a parcel on a brass scale, ledgers and ink, parcels addressed to Riverwood and Solitude",
  intro: "The clerk's counter — ledgers, ink, and parcels weighed true; the FedEx raven-post inside flies thy packages afar.",
  locations: [
    { hold: "Prescott", address: "1931 E Highway 69 (Frontier Village III), Prescott", phone: "(928) 777-8123", hours: "Mon 10 AM–6 PM; Tue–Fri 9 AM–8 PM; Sat 10 AM–7 PM; Sun 10 AM–6 PM", note: "Hours as last listed — call ahead to confirm. FedEx drop-off and pickup counter inside." }
  ]
},
{
  slug: "big-bestbuy", name: "Best Buy", category: "larders", big: true,
  img: "big-bestbuy.webp",
  website: "https://stores.bestbuy.com/az/prescott/3085-gateway-blvd-377.html",
  alt: "Engraving of a marvels-of-the-age gadget shop — a clerk demonstrating a sparking contraption, soul gems in jars, clockwork and gears",
  intro: "The hall of marvels — strange glowing devices and clockwork wonders; the Geek Squad sages mend what ails thy contraptions.",
  locations: [
    { hold: "Prescott", address: "3085 Gateway Blvd, Prescott", phone: "(928) 776-7099", hours: "Mon–Sat 10 AM–9 PM; Sun 10 AM–8 PM", note: "Geek Squad services, Apple Shop in-store, trade-in program." }
  ]
},
/* ---------------- INNS & LODGING ---------------- */
{
  slug: "big-holidayinnexpress", name: "Holiday Inn Express", category: "inns", big: true,
  img: "big-holiday-inn-express.webp",
  website: "https://www.ihg.com/holidayinnexpress/hotels/us/en/sedona/sdoaz/hoteldetail",
  alt: "Engraving of a tidy timber-and-stone inn at dawn — a Nord traveler greeted at the door, dragon-head gables",
  intro: "A tidy roadside inn — hot breakfast at dawn and a warm bed by dusk; the reliable rest on any road.",
  locations: [
    { hold: "Sedona", address: "6176 Highway 179, Sedona", phone: "(928) 284-0711", hours: "Check-in 3 PM; check-out 11 AM", note: "By Bell Rock; outdoor pool, hot tub, free hot breakfast, pet-friendly." },
    { hold: "Payson", address: "206 S Beeline Hwy, Payson", phone: "(928) 472-7484", hours: "Check-in 3 PM; check-out 11 AM", note: "This address now appears to trade as a Comfort Inn — call ahead to confirm the banner." }
  ]
},
{
  slug: "big-comfortinn", name: "Comfort Inn", category: "inns", big: true,
  img: "big-comfort-inn.webp",
  website: "https://www.choicehotels.com/arizona/payson/comfort-inn-hotels",
  alt: "Engraving of a cozy inn — a traveler in Nord tunic sinking into a chair by the stone hearth, breakfast trays coming out",
  intro: "The cozy hearth — plump beds, hot breakfast, and a pool to soak road-weary feet.",
  locations: [
    { hold: "Payson", address: "206 S Beeline Hwy, Payson", phone: "(928) 472-7484", hours: "Check-in 3 PM; check-out 11 AM", note: "Indoor heated pool, hot breakfast; no pets (service animals only)." },
    { hold: "Camp Verde", address: "340 N Goswick Way, Camp Verde", phone: "(928) 567-9000", hours: "Check-in 3 PM; check-out 11 AM", note: "Free hot breakfast, pet-friendly, truck parking, fitness center; near Fort Verde." }
  ]
},
{
  slug: "big-daysinn", name: "Days Inn", category: "inns", big: true,
  img: "big-days-inn.webp",
  website: "https://www.wyndhamhotels.com/days-inn/camp-verde-arizona/days-inn-camp-verde-arizona/overview",
  alt: "Engraving of a sunny motor inn — horse-drawn carriages out front, a Nord family unloading, a glinting pool",
  intro: "The sunny motor inn — a clean bed, a fair price, and the road at thy door.",
  locations: [
    { hold: "Camp Verde", address: "1640 W State Route 260, Camp Verde", phone: "(928) 852-0124", hours: "Check-in 3 PM; check-out 11 AM", note: "Free guest laundry, seasonal pool and hot tub; discount at the Denny's next door." },
    { hold: "Payson", address: "1005 S Beeline Hwy, Payson", phone: "(928) 851-3075", hours: "Call ahead for check-in times", note: "Listing appears active — call ahead to confirm before setting out." }
  ]
},
{
  slug: "big-bestwestern", name: "Best Western Inn of Payson", category: "inns", big: true,
  img: "big-best-western.webp",
  website: "https://www.bestwestern.com",
  alt: "Engraving of a classic western inn — wooden porch with rocking chair, a clerk handing an iron key to cloaked travelers",
  intro: "The classic western inn — hot breakfast, a steaming pool, and a porch made for evening tales.",
  locations: [
    { hold: "Payson", address: "301 S Beeline Hwy Ste A, Payson", phone: "(928) 474-9800", hours: "24-hour front desk", note: "Hot breakfast, indoor pool and hot tub, fitness room." }
  ]
},
{
  slug: "big-qualityinn", name: "Quality Inn", category: "inns", big: true,
  img: "big-quality-inn.webp",
  website: "https://www.choicehotels.com",
  alt: "Engraving of a comfortable lodge inn — an Argonian innkeeper serving bread and cheese, a dog asleep by the door",
  intro: "The comfortable lodge — a stone hearth in the lobby and a dog asleep by the door; four-legged travelers welcome.",
  locations: [
    { hold: "Payson", address: "801 N Beeline Hwy, Payson", phone: "(928) 474-3241", hours: "Check-in 4 PM; check-out 11 AM", note: "Pet-friendly ($20/night fee)." }
  ]
},
{
  slug: "big-super8", name: "Super 8", category: "inns", big: true,
  img: "big-super-8.webp",
  website: "https://www.wyndhamhotels.com/super8",
  alt: "Engraving of a simple log-cabin roadside motel — painted wooden sign, a weary cloaked traveler resting on the porch",
  intro: "The simple rest — clean, honest, and easy on the coin purse; a weary traveler's friend.",
  locations: [
    { hold: "Payson", address: "809 E Hwy 260, Payson", phone: "(928) 478-7465", hours: "Call ahead for check-in times", note: "" }
  ]
},
{
  slug: "big-knightsinn", name: "Knights Inn", category: "inns", big: true,
  img: "big-knights-inn.webp",
  website: "https://www.knightsinn.com",
  alt: "Engraving of a small budget inn — horned-helm painted sign, a traveler smiling while counting coins",
  intro: "The budget keep — a fair price and a smile; count thy coins and rest easy near downtown.",
  locations: [
    { hold: "Payson", address: "101 W Phoenix St, Payson", phone: "(928) 474-4526", hours: "Check-in 3 PM; check-out 11 AM; 24-hour front desk", note: "Pet-friendly; budget rooms near downtown Payson." }
  ]
},
{
  slug: "big-hamptoninn", name: "Hampton Inn", category: "inns", big: true,
  img: "big-hampton-inn.webp",
  website: "https://www.hilton.com/en/hotels/prchhhx-hampton-prescott/",
  alt: "Engraving of a handsome inn — steaming hot-springs pool, travelers in robes, a servant with mead tankards",
  intro: "The handsome modern inn — a steaming hot-springs pool and mountain views; even the monthly Altmer patrol beds down here, though none will admit to waving.",
  locations: [
    { hold: "Prescott", address: "3453 Ranch Drive, Prescott", phone: "(928) 443-5500", hours: "Check-in 4 PM; check-out 11 AM; 24-hour front desk", note: "Heated indoor pool, hot tub, free hot breakfast; off AZ-69 near the mall." }
  ]
},
{
  slug: "big-hilton", name: "Hilton", category: "inns", big: true,
  img: "big-hilton.webp",
  website: "https://www.hilton.com",
  alt: "Engraving of a grand resort hall — an Orc porter with trunk and bedroll, a dragon fountain, iron keys on wall hooks",
  intro: "The grand resort — dragon-fountain halls and red-rock views; for when the quest deserves a feast of a stay.",
  locations: [
    { hold: "Sedona", address: "Hilton Sedona Resort at Bell Rock, 90 Ridge Trail Drive, Sedona", phone: "(928) 284-4040", hours: "Check-in 4 PM; check-out 11 AM", note: "Spa, 18-hole golf, SaltRock restaurant; suites with balconies; pet-friendly." },
    { hold: "Prescott", address: "Hilton Garden Inn Prescott Downtown, 300 N Montezuma St, Prescott", phone: "(928) 515-3422", hours: "Check-in 3 PM; check-out 11 AM; 24-hour front desk", note: "On-site restaurant, outdoor pool, EV charging; two blocks from Whiskey Row." }
  ]
},
{
  slug: "big-enchantment", name: "Enchantment Resort", category: "inns", big: true,
  img: "big-enchantment.webp",
  website: "https://www.enchantmentresort.com/",
  alt: "Engraving of a canyon resort — timber-and-stone lodges beneath red-rock walls, guests on a guided trail walk, a steaming bathhouse",
  intro: "The canyon sanctuary — adobe casitas in red-rock Boynton Canyon, a destination spa, and a hundred guided adventures.",
  locations: [
    { hold: "Sedona", address: "525 Boynton Canyon Rd, Sedona", phone: "(928) 282-2900", hours: "Check-in 4 PM; check-out noon", note: "Mii amo destination spa, fine dining, golf, 100+ weekly guided activities; direct trail access." }
  ]
},
{
  slug: "big-lauberge", name: "L'Auberge de Sedona", category: "inns", big: true,
  img: "big-lauberge.webp",
  website: "https://www.lauberge.com/",
  alt: "Engraving of a creekside inn — timber cottages along a babbling creek, a Nord couple on a footbridge, lanterns at dusk",
  intro: "The creekside dream — cottages on Oak Creek, lanterns at dusk, and dinners worth writing home about.",
  locations: [
    { hold: "Sedona", address: "301 L'Auberge Lane, Sedona", phone: "(928) 282-1661", hours: "Check-in 4 PM; check-out 11 AM", note: "Creekside cottages, spa, fine dining; yoga, stargazing; pet-friendly." }
  ]
},
{
  slug: "big-amara", name: "Amara Resort and Spa", category: "inns", big: true,
  img: "big-amara.webp",
  website: "https://www.amararesort.com/",
  alt: "Engraving of a sleek resort — stone bathhouse with steaming pools, furs and braziers, the creek below",
  intro: "The sleek hideaway — an infinity pool above Oak Creek and red rocks beyond; Uptown's galleries at thy doorstep.",
  locations: [
    { hold: "Sedona", address: "100 Amara Lane, Sedona", phone: "(928) 282-4828", hours: "Check-in 4 PM; check-out 11 AM", note: "Infinity pool over Oak Creek, spa, SaltRock restaurant; pet-friendly." }
  ]
},
{
  slug: "big-hyattpinonpointe", name: "Hyatt Vacation Club at Piñon Pointe", category: "inns", big: true,
  img: "big-hyatt-pinon-pointe.webp",
  website: "https://www.hyatt.com/hyatt-vacation-club/en-US/sedsh-hyatt-vacation-club-at-pinon-pointe",
  alt: "Engraving of villa lodgings — a family cooking a roast on a spit, stew cauldron, fire pit with furs outside",
  intro: "The villa homestead — full kitchens and room to spread out; cook thy own roast over the fire pit.",
  locations: [
    { hold: "Sedona", address: "1 N AZ-89-ALT, Sedona", phone: "(928) 204-8820", hours: "Check-in from 4 PM; check-out until 10 AM", note: "Residential-style villas with full kitchens; pool, hot tubs, fire pit; no pets; $45/day resort fee." }
  ]
},
{
  slug: "big-element", name: "Element Sedona", category: "inns", big: true,
  img: "big-element.webp",
  website: "https://www.marriott.com/en-us/hotels/flgel-element-sedona/overview/",
  alt: "Engraving of an eco-friendly lodge — windmill, herb garden, woven baskets, a hot-spring bathhouse among pines",
  intro: "The green lodge — an eco-minded stay with kitchens and a saline pool; light on the land, easy on the traveler.",
  locations: [
    { hold: "Sedona", address: "6601 State Route 179, Sedona", phone: "(928) 862-3000", hours: "Check-in from 4 PM; check-out until 11 AM", note: "Extended-stay lodge; full in-room kitchens, free breakfast; pet-friendly." }
  ]
},
{
  slug: "big-wranch", name: "W Ranch Resort", category: "inns", big: true,
  img: "big-w-ranch.webp",
  alt: "Engraving of an RV resort — neat rows of canvas-topped wagons, neighbors chatting over a fence, a paddle-ball game",
  intro: "The wagon-circle community — full-hookup sites for thy rolling home, with pickleball and good neighbors.",
  locations: [
    { hold: "Star Valley", address: "16 N Star Vale Dr, Star Valley", phone: "(928) 474-4242", hours: "Call ahead for office hours", note: "55+ community with RV sites (full hookups): about $75/day, $275/week, $705/mo + electric. Clubhouse, dog park." }
  ]
},
{
  slug: "big-hunterslodge", name: "Hunters Lodge RV and Cabin Resort", category: "inns", big: true,
  img: "big-hunters-lodge.webp",
  alt: "Engraving of a rustic cabin resort — log cabins, an Orc tending the fire pit, a dog groomed in a tub on the porch",
  intro: "The rustic camp — cabins, RV sites, and a porch made for whittling; all ages welcome at this fire.",
  locations: [
    { hold: "Star Valley", address: "3758 E AZ Hwy 260, Star Valley", phone: "(928) 474-5182", hours: "Call ahead for office hours", note: "RV sites, rental cabins, laundry, dog grooming; all-ages." }
  ]
},
{
  slug: "big-lamplighter", name: "Lamplighter RV Resort", category: "inns", big: true,
  img: "big-lamplighter.webp",
  website: "https://lamplighterrvresort.com",
  alt: "Engraving of a big friendly RV community — timber hall with billiards and card tables, elders playing cards, lantern-lit trails",
  intro: "The great hall of wagons — 286 lots, a timber clubhouse with billiards and cards, and lantern-lit evening strolls.",
  locations: [
    { hold: "Star Valley", address: "3933 E AZ Hwy 260, Star Valley", phone: "(928) 474-5048", hours: "Call ahead for office hours", note: "55+ resort; nightly, weekly, monthly, and annual rates. Big clubhouse, dog park, walking trails." }
  ]
},
/* ---------------- WHEELS & ROAD SERVICES ---------------- */
{
  slug: "big-autozone", name: "AutoZone", category: "wheels", big: true,
  img: "big-autozone.webp",
  website: "https://www.autozone.com",
  alt: "Engraving of an auto-parts counter — a Nord clerk pouring dwarven oil into a traveler's lantern, shelves of oil and fittings",
  intro: "The parts counter — dwarven oil, lantern oil, and iron fittings; free battery testing and tools to borrow.",
  locations: [
    { hold: "Payson", address: "109 E Hwy 260, Payson", phone: "(928) 472-8810", hours: "Mon–Sat 7 AM–9 PM; Sun 7:30 AM–8 PM", note: "Free battery and check-engine-light testing; Loan-A-Tool program." }
  ]
},
{
  slug: "big-oreilly", name: "O'Reilly Auto Parts", category: "wheels", big: true,
  img: "big-oreilly.webp",
  website: "https://www.oreillyauto.com",
  alt: "Engraving of an auto-parts shop — a Khajiit mechanic fitting a lantern onto an iron motor-wagon, a Nord driver watching",
  intro: "The wrench-wrights — a Khajiit mechanic will fit thy lantern while thou watchest; wiper blades installed free.",
  locations: [
    { hold: "Payson", address: "210 S Beeline Hwy, Payson", phone: "(928) 472-6227", hours: "Mon–Sat 7 AM–9 PM; Sun 7:30 AM–8 PM", note: "Free battery testing, wiper-blade installation, loaner tools." }
  ]
},
{
  slug: "big-stevecouryford", name: "Steve Coury Ford", category: "wheels", big: true,
  img: "big-steve-coury-ford.webp",
  website: "https://www.stevecouryford.com",
  alt: "Engraving of a Ford dealer's yard — rows of iron motor-wagons, a Nord salesman handing keys to a happy family",
  intro: "The iron-wagon yard — rows of fine Ford wagons, a service bay, and a parts counter; the Quick Lube across the road keeps thee rolling.",
  locations: [
    { hold: "Star Valley", address: "4397 E AZ Hwy 260, Star Valley", phone: "Sales (928) 267-5129 · Service (928) 267-5133 · Parts (928) 267-5128", hours: "Sales Mon–Sat 8 AM–6 PM, closed Sun", note: "New and used Ford dealership with service center and parts counter." },
    { hold: "Star Valley", address: "Steve Coury Quick Lube & Tire, 4402 E AZ Hwy 260, Star Valley", phone: "(928) 363-4113", hours: "Mon–Fri 8 AM–5 PM; Sat 8 AM–4 PM", note: "Quick lube and tire service, just across the highway from the dealership." }
  ]
},
{
  slug: "big-carlstowing", name: "Carl's Towing", category: "wheels", big: true,
  img: "big-carls-towing.webp",
  alt: "Engraving of a tow wagon to the rescue — an iron tow rig winching a stuck wagon from a ditch, the driver waving thanks",
  intro: "The rescue wagon — winch-outs, lockouts, and heavy hauls at any hour; when the ditch claims thy wagon, Carl answers.",
  locations: [
    { hold: "Star Valley", address: "3650 E Hwy 260, Star Valley", phone: "(928) 474-9868", hours: "Open 24 hours, 7 days", note: "Light, medium, and heavy-duty towing; mobile repair, winch-outs, lockouts." }
  ]
},
{
  slug: "big-paysonrideshare", name: "Payson Rideshare Taxi Service", category: "wheels", big: true,
  img: "big-payson-rideshare.webp",
  website: "https://paysonrideshare.business.site",
  alt: "Engraving of a friendly taxi — a Nord driver tipping his cap as cloaked travelers board a roomy motor-cab",
  intro: "The hired cab — a veteran driver tips his cap and takes thee anywhere in the county, day or night, up to six travelers.",
  locations: [
    { hold: "Payson", address: "Service-area business — no street address; serves Gila County", phone: "(602) 350-1105", hours: "Listed 24 hours, 7 days", note: "Veteran-owned taxi and rideshare; single riders or groups up to 6." }
  ]
},
/* ---------------- TOWN SERVICES ---------------- */
{
  slug: "big-scrvstorage", name: "SC RV & Mini Storage", category: "town", big: true,
  img: "big-sc-rv-storage.webp",
  website: "https://rvandministorage.com",
  alt: "Engraving of a tidy storage yard — rows of wagons and storage houses, a Nord keeper with a big key ring",
  intro: "The keeper of wagons — tidy storage for thy rolling home and thy overflow treasures; a big ring of keys and an honest rate.",
  locations: [
    { hold: "Star Valley", address: "4397 Arizona Highway 260, Star Valley", phone: "(928) 300-9816", hours: "Mon–Fri 9 AM–5 PM; Sat–Sun closed", note: "Part of the Steve Coury Automotive Family; RV parking and self-storage units." }
  ]
},
{
  slug: "big-starvalleyvet", name: "Star Valley Veterinary Clinic", category: "town", big: true,
  img: "big-star-valley-vet.webp",
  website: "https://starvalleyvet.com",
  alt: "Engraving of a beast-healer's clinic — a kind Nord vet examining a happy dog, cats watching from a sunny shelf",
  intro: "The beast-healers — potions, bandages, and kind hands for thy four-legged companions; boarding when thou must roam.",
  locations: [
    { hold: "Star Valley", address: "103 S Walters Lane, Star Valley", phone: "(928) 474-9605", hours: "Mon–Thu 8 AM–5:30 PM", note: "Small-animal clinic: wellness exams, surgery, lab, boarding; appointments by reservation." }
  ]
},
{
  slug: "big-laceysgrooming", name: "Lacey's Dog Gone Grooming Salon", category: "town", big: true,
  img: "big-laceys-grooming.webp",
  website: "https://dogonegroomn.base44.app",
  alt: "Engraving of a dog-grooming parlor — a Nord groomer trimming a fluffy dog, bubbles, bows, a proud prancing pup",
  intro: "The pampering parlor — bubbles, bows, and a proud prancing pup; all breeds, all temperaments welcome.",
  locations: [
    { hold: "Star Valley", address: "3700 E AZ Highway 260, Star Valley", phone: "(602) 423-0421", hours: "Mon–Sat 8 AM–5 PM (call to confirm)", note: "Full-service dog grooming with online booking." }
  ]
},
/* ---------------- SMITHS, HARDWARE & MAKER SUPPLY ---------------- */
{
  slug: "big-homedepot", name: "The Home Depot", category: "smiths", big: true,
  img: "big-home-depot.webp",
  website: "https://www.homedepot.com",
  alt: "Engraving of a giant hardware hall — an Orc blacksmith loading planks onto a cart, lumber racks and iron ingots",
  intro: "The giant's hardware hall — lumber by the rack, iron by the ingot, and tools to rent; an Orc blacksmith loads thy cart.",
  locations: [
    { hold: "Payson", address: "2000 N Beeline Hwy, Payson", phone: "(928) 468-0339", hours: "Mon–Sat 6 AM–9 PM; Sun 7 AM–8 PM", note: "Garden center; tool rental desk (928) 468-5168; Pro desk (928) 468-5162." },
    { hold: "Show Low", address: "5601 S White Mountain Rd, Show Low", phone: "(928) 532-1552", hours: "Mon–Sat 6 AM–9 PM; Sun 7 AM–8 PM", note: "Tool and truck rental, garden center." },
    { hold: "Prescott", address: "1941 E State Route 69, Prescott", phone: "(928) 771-8467", hours: "Mon–Sat 6 AM–9 PM; Sun 7 AM–8 PM", note: "Tool and truck rental, key cutting, propane exchange, garden center." }
  ]
},
{
  slug: "big-lowes", name: "Lowe's", category: "smiths", big: true,
  img: "big-lowes.webp",
  website: "https://www.lowes.com",
  alt: "Engraving of a home-improvement store — a clerk explaining a cast-iron hearthstove to a Nord couple, a dog dozing by the door",
  intro: "The home-improver's hall — hearthstoves explained with patience and a dog dozing by the door; dog-friendly, naturally.",
  locations: [
    { hold: "Show Low", address: "5800 S White Mountain Rd, Show Low", phone: "(928) 532-2620", hours: "Mon–Sat 6 AM–9 PM; Sun 8 AM–8 PM", note: "Garden center; appliance delivery. Sunday hours vary by listing — call ahead." },
    { hold: "Prescott", address: "2300 E State Route 69, Prescott", phone: "(928) 541-8640", hours: "Mon–Sat 6 AM–9 PM; Sun 7 AM–8 PM", note: "Garden center, truck delivery, dog-friendly store." }
  ]
},
{
  slug: "big-tractorsupply", name: "Tractor Supply Co.", category: "smiths", big: true,
  img: "big-tractor-supply.webp",
  website: "https://www.tractorsupply.com",
  alt: "Engraving of a ranch supply store — feed sacks, a soapy dog in a pet-wash tub, chicks in a warming pen, ranchers browsing",
  intro: "The rancher's supply — feed sacks, tack, and a soapy dog in the pet-wash tub; the PetVet clinic tends thy beasts.",
  locations: [
    { hold: "Payson", address: "510 E State Hwy 260, Payson", phone: "(928) 474-2829", hours: "Mon–Sat 8 AM–9 PM; Sun 9 AM–7 PM", note: "Pet supplies, PetVet veterinary clinic, propane refill station." },
    { hold: "Show Low", address: "3801 S White Mountain Rd, Show Low", phone: "(928) 532-5232", hours: "Mon–Sat 8 AM–9 PM; Sun 9 AM–7 PM", note: "Pet wash, PetVet clinic, propane refill, trailer rental." }
  ]
},
/* ---------------- HOSPITALS ---------------- */
{
  slug: "big-banner-payson", name: "Banner Payson Medical Center", category: "hospitals", big: true,
  img: "big-banner-health.webp",
  website: "https://www.bannerhealth.com/locations/payson/banner-payson-medical-center",
  alt: "Engraving of a stone house of healing \u2014 a healer in robes tending a patient, a red cross banner over the door, pines behind",
  intro: "The Hold's own house of healing \u2014 Payson's full hospital with a day-and-night emergency door, the closest to the Hearth.",
  locations: [
    { hold: "Payson", address: "807 S Ponderosa St, Payson", phone: "(928) 471-3222", hours: "Emergency open 24 hours, every day", note: "44-bed hospital; Arizona-designated Level IV Trauma Center." }
  ]
},
{
  slug: "big-summit-hospital", name: "Summit Healthcare Regional Medical Center", category: "hospitals", big: true,
  img: "big-summit-healthcare.webp",
  website: "http://summithealthcare.net/",
  alt: "Engraving of a mountain-view hospital \u2014 tall windows, a healer carrying a lantern toward the emergency door at dusk",
  intro: "The White Mountains' house of healing \u2014 Show Low's full hospital with a day-and-night emergency door.",
  locations: [
    { hold: "Show Low", address: "2200 E Show Low Lake Rd, Show Low", phone: "(928) 537-4375", hours: "Emergency open 24 hours, every day", note: "89-bed hospital with ICU, surgical services, and cardiac cath lab." },
    { hold: "Show Low", address: "Summit Healthcare Urgent Care, 4951 S White Mountain Rd, Bldg A, Show Low", phone: "(928) 537-6743", hours: "Daily 8 AM\u20138 PM", note: "Call ahead \u2014 this site has had temporary closures; the hospital emergency door stays open regardless." }
  ]
},
{
  slug: "big-vvmc", name: "Verde Valley Medical Center", category: "hospitals", big: true,
  img: "big-nah.webp",
  website: "https://www.nahealth.com/emergency-department",
  alt: "Engraving of a red-rock country infirmary \u2014 healers crossing a courtyard between sandstone walls, a banner with a white cross",
  intro: "The Verde Valley's healers \u2014 a full hospital in Cottonwood and a day-and-night emergency door in Sedona.",
  locations: [
    { hold: "Cottonwood", address: "269 S Candy Ln, Cottonwood", phone: "(928) 634-2251", hours: "Emergency open 24 hours, every day", note: "Level IV Trauma Center. Nearest full hospital to Camp Verde (~20 min)." },
    { hold: "Sedona", address: "VVMC Sedona Campus, 3700 W State Route 89A, Sedona", phone: "(928) 204-4100", hours: "Emergency open 24 hours, every day", note: "Freestanding emergency department." },
    { hold: "Camp Verde", address: "NAH Urgent Care, 1298 Finnie Flat Rd, Camp Verde", phone: "(928) 639-5555", hours: "Daily 8 AM\u20136 PM", note: "Camp Verde's urgent care." }
  ]
},
{
  slug: "big-yrmc", name: "Dignity Health, Yavapai Regional Medical Center", category: "hospitals", big: true,
  img: "big-yrmc.webp",
  website: "http://www.yrmc.org/services/emergency-services",
  alt: "Engraving of a grand western hospital \u2014 many windows, wagons at the entrance, a healer directing travelers to the emergency door",
  intro: "The western Holds' great hospital \u2014 Prescott's full regional hospital with a day-and-night emergency door, and a second campus in Prescott Valley.",
  locations: [
    { hold: "Prescott", address: "West Campus, 1003 Willow Creek Rd, Prescott", phone: "(928) 445-2700", hours: "Emergency open 24 hours, every day", note: "206-bed regional hospital." },
    { hold: "Prescott Valley", address: "East Campus, 7700 E Florentine Rd, Prescott Valley", phone: "(928) 771-5676", hours: "Emergency open 24 hours, every day", note: "" }
  ]
},
/* ---------------- URGENT CARE ---------------- */
{
  slug: "big-banner-sameday", name: "Banner Same-Day Care", category: "urgent", big: true,
  img: "big-banner-sameday.webp",
  website: "https://www.bannerhealth.com/locations/payson/banner-same-day-care-beeline",
  alt: "Engraving of a bright same-day healer's clinic \u2014 a healer greeting a traveler with a bandaged arm, lantern over the entrance, pines behind",
  intro: "The quick healer's door \u2014 same-day care with labs and X-ray on site, for the sprains and fevers that can't wait for morning.",
  locations: [
    { hold: "Payson", address: "101 AZ-260, Suite G, Payson", phone: "(928) 596-4570", hours: "Mon\u2013Thu 8 AM\u20136 PM", note: "On-site labs and X-ray." },
    { hold: "Show Low", address: "680 E Deuce of Clubs, Ste B, Show Low", phone: "(928) 596-4580", hours: "Mon\u2013Sat 8 AM\u20136 PM", note: "" }
  ]
},
{
  slug: "big-payson-walkin", name: "Payson Walk-In Clinic", category: "urgent", big: true,
  img: "big-payson-walkin.webp",
  website: "http://www.paysonclinic.com/",
  alt: "Engraving of a cozy Main Street clinic \u2014 a friendly healer at the door, flower boxes in the windows, pines on the ridge behind",
  intro: "Payson's own neighborhood healer \u2014 a locally owned walk-in clinic on Main Street for same-day care.",
  locations: [
    { hold: "Payson", address: "615 W Main St, Payson", phone: "(928) 363-1603", hours: "Mon\u2013Thu 8 AM\u20134 PM", note: "Locally owned." }
  ]
},
{
  slug: "big-nextcare", name: "NextCare Urgent Care", category: "urgent", big: true,
  img: "big-nextcare.webp",
  website: "https://nextcare.com/locations/az/cottonwood/",
  alt: "Engraving of a small urgent-care cottage \u2014 a healer waving a traveler in from the road, a lantern lit over the door",
  intro: "The quick healer's door across the western Holds \u2014 walk-in urgent care for the hurts that can't wait.",
  locations: [
    { hold: "Cottonwood", address: "450 S Willard St #120, Cottonwood", phone: "(928) 634-2574", hours: "Daily 8 AM\u20136 PM", note: "" },
    { hold: "Prescott", address: "2062 Willow Creek Rd, Prescott", phone: "(928) 443-5103", hours: "Mon\u2013Fri 8 AM\u20137 PM; Sat\u2013Sun 8 AM\u20134 PM", note: "" },
    { hold: "Prescott Valley", address: "3051 N Windsong Dr, Prescott Valley", phone: "(928) 772-3336", hours: "Mon\u2013Fri 7 AM\u20136 PM; Sat\u2013Sun 7 AM\u20133 PM", note: "" }
  ]
},
/* ---------------- DENTAL ---------------- */
{
  slug: "big-emergency-dental", name: "Emergency Dental Care, Payson", category: "dental", big: true,
  img: "big-emergency-dental.webp",
  website: "https://andersondentalonline.com/emergency-dental-services/",
  alt: "Engraving of a tooth-healer's workshop \u2014 a healer holding a carved wooden tooth, shelves of bottles, a patient in a wooden chair, lamplight",
  intro: "The tooth-healers \u2014 Payson's dentists who take emergencies and same-day urgent visits, for the toothache that ruins a vacation.",
  locations: [
    { hold: "Payson", address: "Anderson Dental Group, 712 N Beeline Hwy, Payson", phone: "(928) 474-4581", hours: "Mon\u2013Thu 8 AM\u20135 PM; Fri 8 AM\u20131 PM", note: "Dedicated emergency dentistry; severe toothache, broken teeth, lost crowns. Call ahead to confirm Friday hours." },
    { hold: "Payson", address: "Center Point Dental, 906 S Beeline Hwy, Payson", phone: "(928) 472-2500", hours: "Mon\u2013Thu 8 AM\u20135 PM", note: "Emergency dental care; often accommodates same-day urgent visits." }
  ]
},
/* ---------------- APOTHECARIES ---------------- */
{
  slug: "big-pharmacy", name: "Pharmacies, Payson", category: "pharmacy", big: true,
  img: "big-pharmacy.webp",
  website: "https://www.walgreens.com/locator/walgreens-100+s+beeline+hwy-payson-az-85541/id=6533",
  alt: "Engraving of an apothecary shop \u2014 shelves of jars and bottles, an apothecary handing a parcel to a traveler, mortar and pestle over the door",
  intro: "The apothecaries \u2014 where to fill a prescription in Payson. No 24-hour pharmacy in town; Walgreens keeps the latest hours.",
  locations: [
    { hold: "Payson", address: "Walgreens, 100 S Beeline Hwy, Payson", phone: "(928) 474-1599", hours: "Daily 7 AM\u201310 PM", note: "Latest pharmacy hours in Payson; most central." },
    { hold: "Payson", address: "Walmart Pharmacy, 300 N Beeline Hwy, Payson", phone: "(928) 474-0034", hours: "Mon\u2013Sat 9 AM\u20137 PM; Sun 10 AM\u20136 PM", note: "" },
    { hold: "Payson", address: "Safeway Pharmacy, 401 AZ-260, Payson", phone: "(928) 472-8242", hours: "Mon\u2013Sat 9 AM\u20136 PM (lunch 1:30\u20132 PM); Sun 10 AM\u20136 PM", note: "" },
    { hold: "Payson", address: "Bashas' Pharmacy, 142 AZ-260, Payson", phone: "(928) 474-7039", hours: "Mon\u2013Fri 10 AM\u20137 PM; Sat 9 AM\u20135:30 PM; closed Sunday", note: "" }
  ]
}
];