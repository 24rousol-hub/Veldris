# Roads of the centre: R10, R11, R12, R18, R19, R20, R21

Status: **PROPOSED.** Written 2026-10-01 from the author's sketch ([../region-sketch.md](../region-sketch.md)), the numbering table in [README.md](README.md), and the Palladium renders in `Team-Aquas-Asset-Repo/Maps/Project Palladium/` (sizes below were measured: `(px - 1) / 17` for grid images, `px / 16` otherwise). Format: the road card template in the README. Style matches [../route1.md](../route1.md) and [../route2.md](../route2.md). Nothing is built. Species were checked against `src/data/pokemon/species_info/` (all exist except where noted). Trainer lists give class, team and level only: ids reuse vanilla entries later ([README.md](README.md)). No IVs and no EVs on any trainer.

Linked cards: [towns/cragdale.md](towns/cragdale.md), [towns/lingmoor.md](towns/lingmoor.md), [towns/waymeet.md](towns/waymeet.md), [towns/gildhaven.md](towns/gildhaven.md), [landmarks-centre.md](landmarks-centre.md) (The Pinnacle). Hoarfell and Hemlock Reach cards come from the other agents.

## Summary

| Route | Between | Kind | Render (tiles) | Levels | Section id (from [../region-sketch.md](../region-sketch.md)) |
|---|---|---|---|---|---|
| R10 | Hoarfell, Cragdale | land | Palladium Route 42 (64 x 23) | 34 to 38 | `MAPSEC_ROUTE_113` |
| R11 | Cragdale, Lingmoor | land | Palladium Route 44 (67 x 25) | 36 to 40 | `MAPSEC_ROUTE_117` |
| R12 | Lingmoor, Waymeet | land | Palladium Route 39 (24 x 40) | 38 to 42 | `MAPSEC_ROUTE_118` |
| R18 | Hoarfell, Gildhaven | land | Palladium Route 35 (28 x 32) | 36 to 41 | `MAPSEC_ROUTE_128` |
| R19 | Waymeet, Gildhaven | water | vanilla Route 129 (80 x 40) | 38 to 42 | `MAPSEC_ROUTE_129` |
| R20 | Gildhaven, The Pinnacle | land and cave | Palladium Route 45 (22 x 91) plus vanilla Victory Road (3 floors) | 56 to 62 | `MAPSEC_ROUTE_130` |
| R21 | The Pinnacle, Vesperhaven | land, post-league | Palladium Route 46 (22 x 36) | 62 to 68 | `MAPSEC_ROUTE_131` |

Level logic ([README.md](README.md)): gym aces are 12, 19, 25, 31, 37, 42, 48, 55, 60. Hoarfell is gym 5 (ace 37), Gildhaven is gym 6 (ace 42). R10 to R12 and R19 can be walked either way round, so they run a little above 'ace minus 3'. R20 is walked **after all nine badges** (see R20), so it runs 56 to 62 ahead of the Elite Four at 65. R21 is post-league: 62 to 68.

**Common wild rate tables.** Land: 12 slots at 20/20/10/10/10/10/5/5/4/4/1/1. Surf: 5 slots at 60/30/5/4/1. Old Rod: 2 slots at 70/30. Good Rod: 3 slots at 60/20/20. Super Rod: 5 slots at 40/40/15/4/1. Rock Smash is not used on these roads.

**Walking order (the sketch's arrows).** Hoarfell (gym 5) goes by R10, Cragdale, R11, Lingmoor, R12 to Waymeet. From Waymeet, R19 (Surf) leads to Gildhaven (gym 6). R13 from Waymeet goes on to Hemlock Reach (gym 7). R18 is the thin line between Hoarfell and Gildhaven: a shortcut, not part of the main walk. R20 and R21 are the League road and the post-league road.

**Words.** Pokémon only. No real animals, even in jokes. Trainer classes below avoid animal words (the vanilla class 'Bird Keeper' is not used).

---

## R10: Hoarfell to Cragdale (land, sketch 10)

**Length and shape.** Palladium **Route 42.png** (1089 x 392 px, **64 x 23 tiles**, 1 px grid). A long east-west mountain pass: a wooded strip along the south-west, two small ponds with rock islets in the middle, a high cliff wall along the north, a step of ledges and a sandy track descending to the east. Mood: cold, open, the first of the clear-sky roads after the snow city. Size check: `(64+15)*(23+14) = 2923`, fine. Section `MAPSEC_ROUTE_113`.

**Edges.** **West edge** connects to Hoarfell's east edge (the render's grey gatehouse at the far left is dressed as a closed toll hut, scenery only, or a one-room gate with two warps if the author likes). **East edge** connects to Cragdale's west edge, lower half. No side exits. One ledge at the eastern end drops into the road (one-way, only from the Cragdale side).

**Wild table, land (levels 34 to 38).** Species checked.

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | BOLDORE | 34 to 35 |
| 2 | 20% | RHYHORN | 34 to 35 |
| 3 | 10% | SNEASEL | 35 to 36 |
| 4 | 10% | GRAVELER | 35 to 36 |
| 5 | 10% | MACHOKE | 36 |
| 6 | 10% | PILOSWINE | 36 to 37 |
| 7 | 5% | RHYHORN | 37 |
| 8 | 5% | BOLDORE | 37 |
| 9 | 4% | SKARMORY | 37 to 38 |
| 10 | 4% | SNEASEL | 38 |
| 11 | 1% | ABSOL | 38 |
| 12 | 1% | HAWLUCHA | 38 |

**Wild table, ponds (the two ponds in the middle).**

| Method | Rates | Species and levels |
|---|---|---|
| Surf | 60/30/5/4/1 | GOLDUCK 34 to 38, POLIWHIRL 34 to 38, QUAGSIRE 35 to 38, WHISCASH 36 to 38, SLOWBRO 37 to 38 |
| Old Rod | 70/30 | MAGIKARP 20 to 25, POLIWAG 20 to 25 |
| Good Rod | 60/20/20 | BARBOACH 28 to 32, GOLDEEN 28 to 32, POLIWHIRL 30 to 34 |
| Super Rod | 40/40/15/4/1 | WHISCASH 34 to 38, SEAKING 34 to 38, GOLDUCK 34 to 38, QUAGSIRE 36 to 38, GYARADOS 36 to 38 |

**Trainers (8).** 'Cold-weather trainers.'

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Hiker | GRAVELER 34, RHYHORN 35 | west end, ledge |
| 2 | Hiker | BOLDORE 35, MACHOKE 36 | middle |
| 3 | Black Belt | HITMONLEE 36, HITMONCHAN 36 | north track |
| 4 | Battle Girl | MEDICHAM 37, MACHOKE 36 | on the sandy slope |
| 5 | Cooltrainer | SNEASEL 36, PILOSWINE 37 | a Hoarfell graduate, sulking |
| 6 | Pokémon Ranger | FEAROW 36, SKARMORY 38 | on the ledges, east |
| 7 | Fisherman | SEAKING 36, WHISCASH 37, QUAGSIRE 36 | by the first pond |
| 8 | Picnicker | POLIWHIRL 35, GOLDUCK 36 | by the second pond |

**NPCs (5).** Hut attendant (a tired man in a closed hut, 'closed since forever'); a walker with a thermos (Hoarfell's cold joke); a weather watcher with a notebook (points at Cragdale's station); a sleeping Hiker on the ledge (blocks the path until woken, optional); a signpost reader. Signs: 'HOARFELL, snow city' (west), 'CRAGDALE, ridge town' (east), a mid-road sign 'Ponds: Surf to the islets'.

**Items.** Visible: Hyper Potion (north track), Super Repel (sandy slope), Great Ball (ledge). Hidden: Ether (by the first pond), Full Heal (cliff foot). Pond islets (Surf, badge 5): PP Up on the first islet, Rare Candy on the second (a rare treat).

**Gate.** None (Surf only for the islets). **Goldsworth beat:** none.

**Flags (not claimed).** `FLAG_ITEM_R10_*` (3 visible), `FLAG_HIDDEN_ITEM_R10_*` (2), `FLAG_ITEM_R10_ISLET_1/2`, `FLAG_R10_HIKER_WOKEN` (optional).

**Build effort.** **Medium.** Long, with ledges and two ponds. A close trace of a known layout.

**Open questions.** The render's west gatehouse: scenery, or a real two-warp gate? Is the 'wake the Hiker' optional beat wanted?

---

## R11: Cragdale to Lingmoor (land, sketch 11)

**Length and shape.** Palladium **Route 44.png** (1140 x 426 px, **67 x 25 tiles**, grid). A broad high basin: a rock wall along the north and south, a wide heather moor in between, a pond with a small inlet, trees in the west, a fenced enclosure and a ledge in the east. Mood: open, windy, a lot of sky. Size check: `(67+15)*(25+14) = 3198`, fine. Section `MAPSEC_ROUTE_117`.

**Edges.** **West edge** to Cragdale's east edge (lower half, the notch in the ridge wall). **East edge** to Lingmoor's west edge (upper half). A one-way ledge at the western end can be hopped down from Cragdale's drop (see [towns/cragdale.md](towns/cragdale.md)).

**Wild table, land (levels 36 to 40).**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | FLAAFFY | 36 to 37 |
| 2 | 20% | GOTHORITA | 36 to 37 |
| 3 | 10% | SKUNTANK | 37 |
| 4 | 10% | MIGHTYENA | 37 |
| 5 | 10% | TAUROS | 38 |
| 6 | 10% | GIRAFARIG | 38 |
| 7 | 5% | GOTHORITA | 39 |
| 8 | 5% | FLAAFFY | 39 |
| 9 | 4% | BANETTE | 39 to 40 |
| 10 | 4% | SWANNA | 39 to 40 |
| 11 | 1% | SABLEYE | 40 |
| 12 | 1% | ROTOM | 40 |

**Wild table, ponds.**

| Method | Rates | Species and levels |
|---|---|---|
| Surf | 60/30/5/4/1 | DUCKLETT 36 to 40, SWANNA 38 to 41, POLIWHIRL 36 to 40, POLITOED 40, GYARADOS 40 |
| Old Rod | 70/30 | MAGIKARP 20 to 25, POLIWAG 20 to 25 |
| Good Rod | 60/20/20 | BARBOACH 28 to 32, GOLDEEN 28 to 32, DUCKLETT 30 to 34 |
| Super Rod | 40/40/15/4/1 | SEAKING 36 to 40, WHISCASH 36 to 40, POLITOED 38 to 40, SWANNA 38 to 40, GYARADOS 38 to 40 |

**Trainers (7).** 'Heather folk.'

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Pokéfan | DELCATTY 37, AMPHAROS 38 | on the path |
| 2 | Hex Maniac | GOTHORITA 37, BANETTE 39 | at the cairn |
| 3 | Psychic | GIRAFARIG 38, GOTHORITA 38 | on the open moor |
| 4 | Gentleman | MIGHTYENA 38, GRANBULL 39 | by the enclosure |
| 5 | Guitarist | MANECTRIC 39, AMPHAROS 39 | on a rock, east |
| 6 | Lass | LOMBRE 37, SWANNA 38 | by the pond |
| 7 | Pokémon Breeder | MILTANK 38, TAUROS 39 | at the east enclosure, toughest |

**NPCs (5).** A cairn-builder (stacks stones for fun, tells the player which way the wind is blowing); a lost walker (asks for Lingmoor); a photographer taking pictures of 'nothing at all, in a very good light'; a gatekeeper at the enclosure (it is closed, the sign says so, twice); a heather-picker. Signs: 'CRAGDALE' (west), 'LINGMOOR' (east), 'Mind the ledges'.

**Items.** Visible: Super Potion, Full Heal, Revive (behind the enclosure fence, reached from the east). Hidden: Max Ether (the cairn), Pecha Berry (heather clump). Pond islet (Surf): Star Piece.

**Gate.** None. **Goldsworth beat:** none.

**Flags (not claimed).** `FLAG_ITEM_R11_*` (3), `FLAG_HIDDEN_ITEM_R11_*` (2), `FLAG_ITEM_R11_ISLET`.

**Build effort.** **Medium.** Long, mostly open ground, two big features (the pond, the enclosure).

**Open questions.** What is in the fenced enclosure? (Empty scenery, a post-game gift, or a Breeder's pen?) The card leaves it as scenery with a Breeder beside it.

---

## R12: Lingmoor to Waymeet (land, sketch 12)

**Length and shape.** Palladium **Route 39.png** (409 x 681 px, **24 x 40 tiles**, grid). A tall farm road: a fenced farm yard with a house and a barn at the top, a big pen in the middle, a track and tall-grass ledges below, a line of trees on both sides. Mood: pastoral, the first sight of crossroads country. Size check: `(24+15)*(40+14) = 2106`, fine. Section `MAPSEC_ROUTE_118`.

**Edges.** **North edge** to Lingmoor's south edge (a stone gate). **South edge** to Waymeet's north edge (a farm gate). The railway runs beside the road on the east and is scenery (the Station is in Waymeet).

**Wild table, land (levels 38 to 42).**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | MILTANK | 38 to 39 |
| 2 | 20% | BOUFFALANT | 38 to 39 |
| 3 | 10% | MUDSDALE | 39 |
| 4 | 10% | GOGOAT | 39 |
| 5 | 10% | DUBWOOL | 39 to 40 |
| 6 | 10% | TAUROS | 40 |
| 7 | 5% | MILTANK | 41 |
| 8 | 5% | BOUFFALANT | 41 |
| 9 | 4% | KANGASKHAN | 41 |
| 10 | 4% | GOGOAT | 42 |
| 11 | 1% | SLAKING | 42 |
| 12 | 1% | AUDINO | 42 |

No water here (the pen is a fenced yard, decoration).

**Trainers (6).** 'Farm hands.'

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Pokémon Breeder | MILTANK 38, GOGOAT 39 | at the farm yard gate |
| 2 | Camper | MUDSDALE 39, BOUFFALANT 38 | on the track |
| 3 | Picnicker | DUBWOOL 38, DELCATTY 39 | by the pen |
| 4 | Youngster | LINOONE 38, FURRET 38 | in the long grass |
| 5 | Pokéfan | GRANBULL 38, MILTANK 39 | by the barn |
| 6 | Bug Maniac | HERACROSS 39, PINSIR 40 | at the southern ledges |

**NPCs (5).** The farmer (in the yard, talks about the way the railway shakes the barn), his wife (inside the farmhouse, `LAYOUT_HOUSE2`, gives **Moomoo Milk** x2 once), a barn hand (the barn is `LAYOUT_HOUSE1`, a Miltank in it you can look at), a rail inspector (walks the line, says the timetable is 'under review'), a rail-watching child. Signs: 'LINGMOOR' (north), 'WAYMEET' (south), farm sign 'Lowbarrow Farm' (PROPOSED name).

**Items.** Visible: Super Repel, Hyper Potion, Revive. Hidden: Max Repel (hay), Moomoo Milk (barn side), Full Heal (fence post). Item behind a Cut tree at the yard's corner: Max Elixir.

**Gate.** None (Cut tree optional). **Goldsworth beat:** none; but a Goldsworth-livery crate sits on the siding by the railway, labelled 'Estates, urgent', rusting (a single deadpan object).

**Flags (not claimed).** `FLAG_RECEIVED_MOOMOO_MILK_R12`, `FLAG_ITEM_R12_*` (3), `FLAG_HIDDEN_ITEM_R12_*` (3).

**Build effort.** **Easy.** Small, vertical, straight, two simple interiors.

**Open questions.** Is Moomoo Milk wanted as a freebie (it exists in the item list)? Farm name PROPOSED.

---

## R18: Hoarfell to Gildhaven (land, no sketch number, thin line)

**Length and shape.** Palladium **Route 35.png** (477 x 545 px, **28 x 32 tiles**, grid). A tree-lined avenue: a wide fenced road with a long pond in the lower middle, a pair of grey gatehouses at the north and south ends, flower beds, tall grass behind the fences, forest on both sides. Mood: tidy, expensive, slightly too clean: a road under construction. Size check: `(28+15)*(32+14) = 1978`, fine. Section `MAPSEC_ROUTE_128`. Alternative render if the author wants a shorter hop: Route 37 (28 x 23).

**Edges.** **North edge** to Hoarfell's south edge, through the north gatehouse (a door warp pair, or a connection with the gatehouse as scenery). **South edge** to Gildhaven's north gate (the south gatehouse in the render is the town's North Gate). The sketch draws R18 as a thin line: a secondary road, **under construction** (author, 2026-10-01: not a toll road).

**Gate (PROPOSED).** The north gatehouse is **closed for construction** when the player comes from Hoarfell: the guard says it is 'closed for resurfacing, courtesy of Goldsworth Estates'. The works finish (the road opens) once the player holds the Feather Badge (confirmed by the author, 2026-10-01) (`FLAG_BADGE06_GET`, which already exists). Walking the other way, from Gildhaven to Hoarfell, is always allowed (the Gildhaven end is open and the guard at the north end waves you out). So the road is a shortcut for later, not a wall on the main walk. Goldsworth beat: the works sign 'GOLDSWORTH ESTATES: building a better you, eventually' and a foreman who says the contract was awarded 'to someone who asked who'.

**Wild table, land (levels 36 to 41).**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | STARAVIA | 36 to 37 |
| 2 | 20% | TRANQUILL | 36 to 37 |
| 3 | 10% | FEAROW | 37 |
| 4 | 10% | DODRIO | 37 to 38 |
| 5 | 10% | NOCTOWL | 38 |
| 6 | 10% | BEAUTIFLY | 38 |
| 7 | 5% | MASQUERAIN | 39 |
| 8 | 5% | SUDOWOODO | 39 |
| 9 | 4% | SWANNA | 39 |
| 10 | 4% | CHATOT | 40 |
| 11 | 1% | PELIPPER | 40 |
| 12 | 1% | ALTARIA | 41 |

**Wild table, the long pond.**

| Method | Rates | Species and levels |
|---|---|---|
| Surf | 60/30/5/4/1 | DUCKLETT 36 to 40, MASQUERAIN 38 to 41, POLIWHIRL 36 to 40, GOLDUCK 38 to 41, SWANNA 40 to 41 |
| Old Rod | 70/30 | MAGIKARP 20 to 25, GOLDEEN 20 to 25 |
| Good Rod | 60/20/20 | BARBOACH 28 to 32, GOLDEEN 28 to 32, CORPHISH 30 to 34 |
| Super Rod | 40/40/15/4/1 | SEAKING 36 to 40, CRAWDAUNT 36 to 40, WHISCASH 36 to 40, GYARADOS 38 to 41, GOLDUCK 38 to 41 |

**Trainers (5).** 'Posh road.'

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Rich Boy | DELCATTY 37, CLEFABLE 38 | north gate, bored |
| 2 | Lady | GRANBULL 38, WIGGLYTUFF 38 | on the lawn |
| 3 | Parasol Lady | MASQUERAIN 38, BEAUTIFLY 39 | by the pond |
| 4 | Cooltrainer | STARAPTOR 39, ALTARIA 40 | south end, a Gildhaven preview |
| 5 | Pokémon Ranger | DODRIO 38, CHATOT 38, PELIPPER 39 | near the south gate |

**NPCs (5).** Two gate guards (north gate, south gate); a gardener (waters the flower beds, the same bed, again); a jogger who has been through the tower three times; a signpost board. Signs: 'GILDHAVEN, 1 mile of lawn' (south), 'HOARFELL' (north), 'ROAD WORKS, residents only'.

**Items.** Visible: Super Potion, Revive. Hidden: Rare Candy (by the pond edge, a rarer reward for the long walk), Escape Rope. Pond islet (Surf): Pearl.

**Flags (not claimed).** `FLAG_R18_GATE_OPEN` (optional: or test `FLAG_BADGE06_GET`), `FLAG_ITEM_R18_*` (2), `FLAG_HIDDEN_ITEM_R18_*` (2), `FLAG_ITEM_R18_ISLET`.

**Build effort.** **Easy.** The render already is a straight road with two gatehouses, and the scenery is simple.

**Open questions.** None: the author confirmed 'under construction, not a toll road' (2026-10-01). The player at 5 badges goes round by R10 to R12 and the water road R19; R18 opens later as a shortcut.

---

## R19: Waymeet to Gildhaven (water, sketch 32)

**Length and shape.** Vanilla **Route 129** (`Route129_Layout`, **80 x 40**, tileset `gTileset_General` + `gTileset_Mossdeep`). No Palladium water road fits a long east-west run (Route 40 is vertical, 20 x 34). A long, sheltered stretch of open water between two shores: reed islets, a rail viaduct crossing overhead near Waymeet, a few rocky skerries, a lighthouse-less coast, sandbanks with a single grass tuft each. Mood: calm, wide, a place to take a break from the cliffs. Size check: `(80+15)*(40+14) = 5130`, fine. Section `MAPSEC_ROUTE_129`.

**Edges.** **East edge** connects to Waymeet's west pier. **West edge** connects to Gildhaven's east harbour. The sketch arrow runs towards Gildhaven. Both ends are open water; the player starts on land and surfs in. No side exits. The viaduct is scenery.

**Wild table, water only (levels 38 to 42).** No land encounters (the sandbanks have no tall grass).

| Method | Rates | Species and levels |
|---|---|---|
| Surf | 60/30/5/4/1 | TENTACRUEL 38 to 42, PELIPPER 38 to 41, MANTINE 40 to 42, LUMINEON 40 to 42, LAPRAS 41 to 42 |
| Old Rod | 70/30 | MAGIKARP 20 to 25, TENTACOOL 20 to 25 |
| Good Rod | 60/20/20 | CORPHISH 28 to 32, STARYU 28 to 32, CHINCHOU 28 to 32 |
| Super Rod | 40/40/15/4/1 | STARMIE 38 to 42, CRAWDAUNT 38 to 42, GYARADOS 38 to 42, SEADRA 40 to 42, WAILORD 41 to 42 |

**Trainers (7).** 'Waterside crew.'

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Swimmer (male) | TENTACRUEL 38, STARMIE 39 | east, near Waymeet |
| 2 | Swimmer (female) | LUMINEON 38, MANTINE 39 | middle |
| 3 | Sailor | MACHAMP 39, PELIPPER 38 | on a sandbank |
| 4 | Fisherman | GYARADOS 37, SEAKING 38, WHISCASH 39 | by the viaduct |
| 5 | Fisherman | CRAWDAUNT 38, QWILFISH 39 | west end |
| 6 | Sailor | KINGLER 38, OCTILLERY 39 | at a skerry |
| 7 | Swimmer (male) | SHARPEDO 39, STARMIE 40 | just before Gildhaven, toughest |

**NPCs (5).** A ferryman asleep in a moored boat (decor and a one-line hint that Waymeet's ferries 'are theoretical'); a lookout on a skerry who points out Gildhaven's tower; a pier-sitter ('the tower can be seen from here, and nothing else can'); two sandbank islanders (item holders). Signs: 'GILDHAVEN HARBOUR' (west), 'WAYMEET PIER' (east).

**Items.** Visible on sandbanks: Max Revive, Ultra Ball, TM Rain Dance (rare find). Hidden (Surf): Pearl, Heart Scale, Stardust. Dive spots (Dive, badge 9): hidden underwater items, noted for the post-game, not listed here.

**Gate.** **Surf (badge 5).** There is no walking path. **Goldsworth beat:** a Goldsworth-branded buoy line 'for guests of the Estate' and the tower visible from the middle: no scheme.

**Flags (not claimed).** `FLAG_ITEM_R19_*` (3 visible), `FLAG_HIDDEN_ITEM_R19_*` (3).

**Build effort.** **Medium.** Large (80 x 40) but mostly water: sandbanks and skerries are quick; the viaduct is a decoration piece. The vanilla base Route 129 makes it easy.

**Open questions.** Is a water-only road the author's intent? In the sketch the Gildhaven to Waymeet line is blue with no brown line beside it, so I read it as water only. Does the author want Waymeet's piers to feel like the start of a ferry?

---

## R20: Gildhaven to The Pinnacle (land, sketch 33): the Victory Road gauntlet

**Length and shape.** A two-part gauntlet. (a) **Surface climb:** Palladium **Route 45.png** (375 x 1548 px, **22 x 91 tiles**, grid). A very long, narrow mountain track with ledges, rock outcrops, a few small tree stands and a muddy pocket at the foot. Size check: `(22+15)*(91+14) = 3885`, fine. (b) **The cave ('the Long Climb', PROPOSED name):** the three vanilla **Victory Road** floors (`VictoryRoad_1F` **46 x 45**, `_B1F` **46 x 31**, `_B2F` **46 x 31**, tileset `gTileset_General`/`gTileset_Cave`), with Strength boulders, Rock Smash rocks and optional Flash. Mood: severe, steep, silent. Every trainer on it is overqualified and rude about it politely.

**Why a gauntlet.** The player walks R20 **after all nine badges** ([../troglodyte-arc.md](../troglodyte-arc.md): fight 7 is 'Victory Road', behind ace 60; [../postgame.md](../postgame.md): the Elite Four starts at 65). So this road is where the level curve climbs from 56 to 62 before the League, and it has more trainers and fewer free healing points than any other road. The Pokémon Center is in the Pinnacle's lobby, not on the road.

**Sections.** The surface uses `MAPSEC_ROUTE_130`. The three cave floors can share it, or take a new section if the author wants a separate popup name (open question).

**Edges.** **Surface north end** connects to Gildhaven through the **Pinnacle Gate** (a gatehouse that checks for all nine badges, [towns/gildhaven.md](towns/gildhaven.md)). The surface climbs south-east. At its south end a **cave mouth** (one door warp) leads into the cave. The cave's last floor exits to a short summit stair that arrives at **The Pinnacle's** north edge ([landmarks-centre.md](landmarks-centre.md)). The road is one way in design: there is nowhere to go but forward, but backtracking is allowed.

**Wild tables.** All 12 slots, rates 20/20/10/10/10/10/5/5/4/4/1/1. No water.

*Surface (levels 56 to 60).*

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | RHYDON | 56 to 57 |
| 2 | 20% | GOLEM | 56 to 57 |
| 3 | 10% | MACHAMP | 57 |
| 4 | 10% | GIGALITH | 57 |
| 5 | 10% | STEELIX | 57 to 58 |
| 6 | 10% | SKARMORY | 58 |
| 7 | 5% | MANDIBUZZ | 58 |
| 8 | 5% | RAMPARDOS | 58 to 59 |
| 9 | 4% | BASTIODON | 59 |
| 10 | 4% | HIPPOWDON | 59 |
| 11 | 1% | AGGRON | 60 |
| 12 | 1% | ABSOL | 60 |

*Cave 1F (levels 57 to 60).*

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | CROBAT | 58 to 59 |
| 2 | 20% | MEDICHAM | 58 to 59 |
| 3 | 10% | HARIYAMA | 58 to 59 |
| 4 | 10% | GOLEM | 58 to 59 |
| 5 | 10% | GIGALITH | 59 |
| 6 | 10% | STEELIX | 59 |
| 7 | 5% | CLAYDOL | 59 to 60 |
| 8 | 5% | AGGRON | 60 |
| 9 | 4% | PROBOPASS | 60 |
| 10 | 4% | BISHARP | 60 |
| 11 | 1% | MAWILE | 60 |
| 12 | 1% | SABLEYE | 60 |

*Cave B1F (levels 58 to 61).*

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | RHYDON | 58 to 59 |
| 2 | 20% | MACHAMP | 58 to 59 |
| 3 | 10% | CLAYDOL | 59 |
| 4 | 10% | CROBAT | 59 to 60 |
| 5 | 10% | MEDICHAM | 59 to 60 |
| 6 | 10% | HARIYAMA | 60 |
| 7 | 5% | AGGRON | 60 to 61 |
| 8 | 5% | PROBOPASS | 60 to 61 |
| 9 | 4% | BISHARP | 61 |
| 10 | 4% | MAWILE | 60 to 61 |
| 11 | 1% | SOLROCK | 61 |
| 12 | 1% | LUNATONE | 61 |

*Cave B2F (levels 59 to 62).*

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | STEELIX | 59 to 60 |
| 2 | 20% | GOLEM | 59 to 60 |
| 3 | 10% | CLAYDOL | 60 |
| 4 | 10% | AGGRON | 60 to 61 |
| 5 | 10% | PROBOPASS | 61 |
| 6 | 10% | RHYDON | 60 to 61 |
| 7 | 5% | BISHARP | 61 to 62 |
| 8 | 5% | DUSKNOIR | 61 to 62 |
| 9 | 4% | MAWILE | 61 |
| 10 | 4% | SABLEYE | 61 |
| 11 | 1% | GLISCOR | 62 |
| 12 | 1% | RHYPERIOR | 62 |

**Trainers.** All reuse vanilla ids, no IVs. 7 on the surface, 9 in the cave, plus **Troglodyte fight 7**.

*Surface (7), levels 56 to 58.*

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Hiker | GOLEM 56, STEELIX 57 | at the foot, first ledge |
| 2 | Black Belt | MACHAMP 56, HARIYAMA 57 | on a ledge |
| 3 | Cooltrainer | ALTARIA 56, GLISCOR 57 | mid-climb |
| 4 | Battle Girl | MEDICHAM 57, HITMONLEE 57 | the narrowest ledge |
| 5 | Ruin Maniac | CLAYDOL 56, RAMPARDOS 57 | by an outcrop |
| 6 | Dragon Tamer | FLYGON 57, ALTARIA 57 | at the cave mouth |
| 7 | Psychic | ALAKAZAM 57, GOTHITELLE 57 | beside the cave door |

*Cave 1F (3), levels 58 to 59.*

| # | Class | Team | Notes |
|---|---|---|---|
| 8 | Cooltrainer | AGGRON 58, CROBAT 58, MEDICHAM 59 | boulder corridor |
| 9 | Expert | HARIYAMA 58, MACHAMP 59 | past the first Strength boulder |
| 10 | Hex Maniac | DUSKNOIR 58, SABLEYE 59 | dark side room |

*Cave B1F (3), levels 59 to 60.*

| # | Class | Team | Notes |
|---|---|---|---|
| 11 | Dragon Tamer | HAXORUS 59, FLYGON 59 | on a pit-edge path |
| 12 | Psychic | CLAYDOL 59, ALAKAZAM 60 | in a Flash room |
| 13 | Cooltrainer | BISHARP 59, PROBOPASS 60, MAWILE 59 | at the stair |

*Cave B2F (3), levels 60 to 61.*

| # | Class | Team | Notes |
|---|---|---|---|
| 14 | Black Belt | HARIYAMA 60, MACHAMP 60 | on the exit stair |
| 15 | Expert | RHYPERIOR 60, STEELIX 60 | corridor |
| 16 | Ruin Maniac | GOLEM 60, PROBOPASS 61, CLAYDOL 61 | the toughest trainer here |

*Troglodyte, fight 7 (the Work phase).* In the **cave's final chamber, just before the stair that exits to The Pinnacle**. Arrives on a `coord_event` trigger. Party Size 6, `Pool Prune: Rival Starter`. Team ([../troglodyte-arc.md](../troglodyte-arc.md), fixed 2026-10-01, no Garchomp): **Stoutland 'Sir Biscuit' 55, Vaporeon 55, Gardevoir 56, Pyroar 56, Tyranitar 56, plus one stage-3 starter at 57** (levels 55 to 57, 'behind ace 60'). His line: 'Fight me. Properly. Please.' (the arc table). He has stopped making jokes and stopped pet jokes; he is stiff.

**NPCs (6).** A gate guard at the Pinnacle Gate (nine badges), a cave guide (a Hiker with a spare torch, gives a Repel once and recommends Flash), two resting trainers on a bench (non-battlers, a Cooltrainer who has lost for the third time and a Black Belt who is stretching), a child pushing a small boulder up the slope ('this is Strength practice'), a sign painter touching up 'THE PINNACLE: 1 MILE'. Signs: 'GILDHAVEN' (north), 'THE PINNACLE, nine badges required' (south).

**Items.** Visible: Max Revive, Full Restore, Rare Candy, PP Max (cave B1F, behind a Strength boulder), Max Elixir (surface ledge). Hidden: Ultra Ball, Max Ether, Elixir. TM: **TM Brick Break** (on the surface, behind a Rock Smash rock, optional). No Rock Smash encounters.

**Gate.** All nine badges (checked at the Pinnacle Gate through the badge table). HMs: **Strength** (badge 4, boulders, mandatory in the cave), **Rock Smash** (optional items), **Flash** (optional dark rooms). **Goldsworth beat:** Troglodyte fight 7.

**Flags (not claimed).** `FLAG_R20_CAVE_BOULDER_*` (vanilla uses temp flags for boulder resets, check), `FLAG_ITEM_R20_*` (6), `FLAG_HIDDEN_ITEM_R20_*` (3), `FLAG_RECEIVED_TM_BRICK_BREAK`, `TRAINER_TROGLODYTE_VICTORY_ROAD` (alias, reuses a vanilla id), `TRAINER_R20_*` (16 aliases).

**Build effort.** **Hard.** A 22 x 91 outdoor map plus three large vanilla cave floors to duplicate and retrim, 16 trainers and a coord-event scene. The vanilla Victory Road (1F, B1F, B2F) can be duplicated unchanged and then the trainers placed; that is the cheap route. A full redraw is not expected.

**Open questions.**
1. Is the cave **in** R20 (this card) or should the road be surface only (shorter, 22 x 91)? Without the cave the gauntlet has 7 trainers.
2. Section for the cave floors: reuse `MAPSEC_ROUTE_130` or take a new id?
3. ~~Troglodyte fight 7 species.~~ Resolved (author, 2026-10-01): fights 7 and 8 share the postgame core, no Garchomp.
4. ~~Badges for the gate.~~ **All nine** (author, 2026-10-01). Vanilla's guards only test one flag, so the gate script tests the ninth badge flag.

---

## R21: The Pinnacle to Vesperhaven (land, post-league, sketch 34)

**Length and shape.** Palladium **Route 46.png** (375 x 613 px, **22 x 36 tiles**, grid). A cliff-top descent: a patchwork of grassy shelves separated by rock ledges, a small stand of trees at the foot, a sandy landing at the bottom, a dark doorway at the top (the render's Dark Cave door, here a locked cellar). Mood: wind and open sea air, the world after the League. Size check: `(22+15)*(36+14) = 1850`, fine. Section `MAPSEC_ROUTE_131`.

**Edges.** **North edge** to The Pinnacle's south edge (a gap in a stone wall that is **barred until the game is cleared**, `FLAG_SYS_GAME_CLEAR`). **South edge** to Vesperhaven's north edge. Vesperhaven is post-game only ([../region-names.md](../region-names.md)), so the road is too.

**Wild table, land (levels 62 to 68, post-league).**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | BRAVIARY | 62 to 63 |
| 2 | 20% | MANDIBUZZ | 62 to 63 |
| 3 | 10% | SKARMORY | 63 to 64 |
| 4 | 10% | ALTARIA | 63 to 64 |
| 5 | 10% | GLISCOR | 64 to 65 |
| 6 | 10% | PELIPPER | 64 to 65 |
| 7 | 5% | STARAPTOR | 65 |
| 8 | 5% | DRAPION | 65 to 66 |
| 9 | 4% | RHYPERIOR | 66 |
| 10 | 4% | CROBAT | 66 |
| 11 | 1% | ABSOL | 67 |
| 12 | 1% | BISHARP | 68 |

No water on this road.

**Trainers (6).** All reuse vanilla ids, no IVs, 'League graduates.'

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Cooltrainer | FLYGON 64, HAXORUS 65, ALTARIA 64 | top shelf |
| 2 | Cooltrainer | ALAKAZAM 65, GALLADE 65, REUNICLUS 64 | mid shelf |
| 3 | Expert | METAGROSS 66, AGGRON 65, PROBOPASS 64 | on a ledge |
| 4 | Black Belt | CONKELDURR 65, HARIYAMA 64, MACHAMP 65 | the rocky stretch |
| 5 | Pokémon Ranger | PELIPPER 63, GLISCOR 64, STARAPTOR 65, SKARMORY 64 | sandy slope |
| 6 | Dragon Tamer | HAXORUS 66, HYDREIGON 66, NOIVERN 65 | toughest, near the foot |

**NPCs (5).** A League guard (lets you through once the Hall of Fame is done), a sign painter who has already updated 'THE PINNACLE: champions of the region' (gently out of date), a retired Elite Four fan with a flag, a surveyor with an orange stake (a Goldsworth nod: 'Estates are still thinking about this one'), a rest-bench trainer. Signs: 'THE PINNACLE' (north), 'VESPERHAVEN, hidden coast' (south).

**Items.** Visible: Max Revive, Full Restore, Rare Candy x2 (post-game gifts). Hidden: Max Elixir, PP Max. The locked cellar door at the top: opens after a late post-game flag (PROPOSED, a gift cache of Rare Candies, optional).

**Gate.** `FLAG_SYS_GAME_CLEAR` (the League is beaten). **Goldsworth beat:** the surveyor stake (a joke only).

**Flags (not claimed).** `FLAG_R21_OPEN` (or reuse `FLAG_SYS_GAME_CLEAR`), `FLAG_ITEM_R21_*` (3), `FLAG_HIDDEN_ITEM_R21_*` (2), `FLAG_R21_CELLAR_OPEN` (optional).

**Build effort.** **Medium.** Medium size, cliffs, one dead-end cellar door left decorative.

**Open questions.**
1. The render's dark doorway: decoration, a locked cellar with gifts, or a real cave? PROPOSED: a locked cellar.
2. R21 and Vesperhaven are post-game only. Should the Pinnacle's south gate also be open from the start as a scenic dead end (no, closed until `FLAG_SYS_GAME_CLEAR`)?

---

## Open questions for the author (centre group)

1. ~~R18 and the thin line.~~ Resolved (author, 2026-10-01): under construction, not a toll road.
2. **R19 is water only** (no brown beside the blue line in the sketch). Confirmed? Waymeet's piers and Gildhaven's harbour both need Surf (badge 5).
3. **R20 walking order.** The card assumes all nine badges before R20 ([../troglodyte-arc.md](../troglodyte-arc.md): fight 7 behind ace 60). If the Elite Four is open at eight badges, the cave levels (56 to 62) need lowering by about 4 and fight 7's team too.
4. **Palladium Route 40, Route 43 and others** are unassigned by this group; other agents may want them. This group uses Routes 35, 39, 42, 44, 45, 46 and vanilla Route 129.
5. The **three vanilla Victory Road floors** are Hoenn maps named 'VICTORY ROAD'. They need a Veldris name and section (PROPOSED 'the Long Climb').
