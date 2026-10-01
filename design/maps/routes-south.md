# Road cards, south group: R22 to R31 (PROPOSED, started 2026-10-01)

> **Open question (author, 2026-10-01): the Palladium route renders named in this file are NOT decided.** The author doubts that reusing Palladium route images will give a quality hack, so every 'source render' for a road below is a **mood and shape reference only** until the author decides how each road gets built (traced, redrawn or designed fresh). Lengths, edges, trainers, items and encounters stay as written.


Status: **PROPOSED.** Ten road cards written from the author's sketch and the README table ([README.md](README.md)). Nothing is built. Routes are numbered in walking order; the sketch's paired numbers are one road drawn with an arrow each way (README). Settlement cards: [towns/ebbsworth.md](towns/ebbsworth.md), [kingsquay.md](towns/kingsquay.md), [driftsands.md](towns/driftsands.md), [beaconmouth.md](towns/beaconmouth.md), [aldermere.md](towns/aldermere.md), [vesperhaven.md](towns/vesperhaven.md). Landmarks: [landmarks-south.md](landmarks-south.md).

## How to read these cards

- **Levels follow the README curve.** Gym aces 12, 19, 25, 31, 37, 42, 48, 55, 60. The south chain R22 to R25 sits between gym 8 (ace 55) and gym 9 (ace 60): wild levels **52 to 58**, trainers 50 to 58. The post-game roads (R26 to R31) run **60 to 85**: wilds 60 to 74 on the roads, up to 85 only on Argent Peak ([landmarks-south.md](landmarks-south.md)).
- **Gates.** Surf from badge 5 opens every water road. **Waterfall (badge 8) is the hard gate on R22**: it keeps the whole south chain behind gym 8. Dive (badge 9, from Mizzle) opens underwater spots on R26 and R29 and the drowned city. R26 to R31 open after `FLAG_SYS_GAME_CLEAR`.
- **Wild tables.** Land: 12 grass slots, rates 20/20/10/10/10/10/5/5/4/4/1/1. Water (Surf): 5 slots, rates 60/30/5/4/1. Fishing: Old Rod 2 slots (70/30), Good Rod 3 slots (60/20/20), Super Rod 5 slots (40/40/15/4/1). **Old Rod and Good Rod levels are PROPOSED low**, as in vanilla: Old Rod 25 to 30, Good Rod 40 to 50, Super Rod at the road's band. All species were grepped in `include/constants/species.h` and exist in this tree. Porymap writes them to `wild_encounters.json`.
- **Trainers** list class, species and levels only. They reuse vanilla Hoenn ids (a later job), carry no IVs (explicit `IVs: 0` lines when built), no EVs, and are Pokémon only. Maps hold at most 15 live objects.
- **Palladium pictures** live in `Team-Aquas-Asset-Repo/Maps/Project Palladium/`. Sizes below are measured from the PNGs: `(px - 1) / 17` for the gridded ones, `px / 16` for the rest. They are images, not map files: the author traces them in Porymap. Credit 'Project Palladium team' with the file name in `CREDITS.md` in the first commit that traces one (map-plan.md). Edges follow the sketch's compass where the render allows it, and the author may flip or rotate a picture. **Other groups may also pick these pictures** (the index will have to reconcile): I checked the other groups' cards on 2026-10-01 and avoided the pictures they use (Route 32, 35, 36, 39, 40, 42, 43, 44, 45, 46 and vanilla 105, 107, 129). I use Palladium Route 33 and Route 38, and vanilla Routes 106, 109, 115, 121, 122, 126, 128 and 134. Route 128 is the only one I could not confirm is free.
- **Section ids.** Each road needs one new section: `MAPSEC_VELDRIS_ROUTE_22` to `_31` (name `ROUTE 22` and so on, 8 characters). With the six settlements, Aldermere and Vesperhaven that is 19 to 21 of the 37 free ids; the three landmarks can borrow Hoenn cave or ruin section entries instead of new ones ([../region-sketch.md](../region-sketch.md), 'Map section budget').
- **Water roads and the Dive map.** Each Dive spot needs a second underwater map and a dive connection in Porymap. Vanilla `Underwater_Route124` to `_134` show the pattern.

| Road | Between | Render or base | Size (tiles) | Band | Kind |
|---|---|---|---|---|---|
| R22 | Waymeet, Ebbsworth | vanilla `Route122` | 40 x 40 | 52 to 55 | water (Waterfall weir) |
| R23 | Ebbsworth, Kingsquay | vanilla `Route109` | 40 x 63 | 53 to 56 | water with land path |
| R24 | Kingsquay, Driftsands | Palladium `Route 38.png` | 40 x 28 | 54 to 57 | land |
| R25 | Driftsands, Beaconmouth | vanilla `Route121`, trimmed | 80 x 20 base, about 64 x 20 built | 56 to 58 | land (two ponds) |
| R26 | Beaconmouth, Aldermere | vanilla `Route134` | 80 x 40 | 62 to 68 | water, post-game |
| R27 | Vesperhaven, Wendlebury | vanilla `Route128`, trimmed | 120 x 40 base, about 80 x 40 built | 60 to 66 | water, post-game |
| R28 | Vesperhaven, Ebbsworth | vanilla `Route106`, trimmed | 80 x 20 base, 60 x 20 built | 62 to 68 | water, post-game |
| R29 | Vesperhaven, Silverstrand | vanilla `Route126`, trimmed | 80 x 80 base, about 48 x 80 built | 64 to 70 | water, post-game |
| R30 | Vesperhaven, Echo Hollow | Palladium `Route 33.png`, extended | 22 x 18 render, about 22 x 30 built | 66 to 72 | land, post-game |
| R31 | Hollowbrook, Argent Peak | vanilla `Route115`, trimmed | 40 x 80 base, about 40 x 70 built | 68 to 74 | land, post-game |

---

## R22: Waymeet to Ebbsworth (water, sketch 21 and 30)

**Length and shape.** A sea channel, mostly water, 40 x 40 built (`(40 + 15) * (40 + 14) = 2970`). Mood: broad brown tide, reed banks, then a stepped stone weir. Source: vanilla **`Route122`** (`Route122_Layout`, 40 x 40), a sea route with a long bridge across it. Use the bridge as Waymeet's **south dock gate** at the top and ignore Mt Pyre. Add the weir by hand at the south end. (The one Palladium sea route, `Route 40.png`, 20 x 34, is already used by the east group for R14.) Section id `MAPSEC_VELDRIS_ROUTE_22`.

**Edges.** North end enters Waymeet's south dock (water, via the gate). South end enters Ebbsworth's north quay (water). No side exits. A sandbar beach under the gate has one NPC. The weir is the last thing before the town: a dog-leg so the cascade is climbed northwards on the screen (Waterfall tiles go up), with the town beyond the top.

**Wild table (PROPOSED), levels 52 to 55.** No tall grass.

Surf (60/30/5/4/1):

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 60% | TENTACRUEL | 52 to 55 |
| 2 | 30% | PELIPPER | 52 to 55 |
| 3 | 5% | WAILORD | 53 to 55 |
| 4 | 4% | MANTINE | 52 to 55 |
| 5 | 1% | KINGDRA | 54 to 55 |

Old Rod (70/30): MAGIKARP 25 to 30, TENTACOOL 25 to 30. Good Rod (60/20/20): BARBOACH 40 to 45, BUIZEL 40 to 45, CARVANHA 40 to 45. Super Rod (40/40/15/4/1): SEAKING 52 to 55, QWILFISH 52 to 55, WHISCASH 53 to 55, SHARPEDO 54 to 55, GYARADOS 55.

**Trainers (6, all on the water or the sandbar; levels 50 to 54).**

| Class | Team |
|---|---|
| Swimmer male | Starmie 52, Seadra 52, Floatzel 53 |
| Swimmer female | Mantine 52, Lanturn 53, Jellicent 53 |
| Fisherman | Gyarados 52, Whiscash 53, Qwilfish 53 |
| Sailor | Pelipper 52, Tentacruel 53, Dewgong 53 |
| Tuber female | Azumarill 52, Poliwrath 53 |
| Swimmer female (at the weir) | Kingdra 54, Seaking 53, Milotic 54 |

**NPCs.** The Waymeet dock-gate guard (reminds the player that the weir 'climbs, it does not carry'); a fisher on the sandbar who sells a rumour about the Ebbsworth barge; a barge hand on a floating pontoon (ambient, Scheme 9 seed: 'Four hundred. Counted twice.'); a child watching the Wailord. 4 NPCs.

**Items.** Visible: Max Potion on a rock outcrop, Revive on the sandbar, Dive Ball at the weir foot. Hidden: Heart Scale and Pearl on the sandbar. (Post-game: a Big Pearl Dive spot beneath the weir, optional.)

**Gate: Waterfall (badge 8) at the weir.** The first thing the south chain asks. Without it the player is stopped at the foot of the cascade: a sign says 'LOCK BEYOND' and the Waymeet gate guard explains. This is the hard gate behind gym 8.

**Goldsworth beat.** None. The barge is the only seed (see Ebbsworth).

**Flags (not claimed).** `FLAG_R22_BARGE_HAND_SEEN`, `FLAG_HIDDEN_ITEM_R22_HEART_SCALE`, `_PEARL`, `FLAG_ITEM_R22_MAX_POTION`, `FLAG_ITEM_R22_REVIVE`, `FLAG_ITEM_R22_DIVE_BALL`, trainer flags are the reused ids.

**Build effort.** Medium. A water road with the weir to design by hand.

**Open questions.** Is the weir the right gate, or should Waterfall be needed later (R23)?

---

## R23: Ebbsworth to Kingsquay (water, with a land path, sketch 22 and 29)

**Length and shape.** A coast road with sea on one side and a sand-and-pine path on the other, 40 x 63 (`(40 + 15) * (63 + 14) = 4235`). Mood: tidy coastline, a wooden pier into the water, a rest house in the pines. Source: vanilla **`Route109`** (`Route109_Layout`, 40 x 63), the beach road with the Seashore House and a jetty. It already has the sea beside a land path. (Palladium `Route 32.png`, 28 x 94, has the pier and sea but the west group has taken it for a lakeside road.) Section id `MAPSEC_VELDRIS_ROUTE_23`.

**Edges.** North: **Ebbsworth** (the east gate for the land path, the lock gate for the water path, both at the north end). South: **Kingsquay** north gate (land) and the slipway at the north-west coast (water). The pier in the middle is a side walkway into the sea, no exit.

**Wild table (PROPOSED), levels 53 to 56.**

Grass (land path), standard rates:

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | KINGLER | 53 to 54 |
| 2 | 20% | PELIPPER | 53 to 54 |
| 3 | 10% | SANDSLASH | 54 |
| 4 | 10% | SLOWBRO | 54 to 55 |
| 5 | 10% | STARAVIA | 54 to 55 |
| 6 | 10% | CRAWDAUNT | 54 to 55 |
| 7 | 5% | WYRDEER | 55 |
| 8 | 5% | DONPHAN | 55 |
| 9 | 4% | CLOYSTER | 55 to 56 |
| 10 | 4% | STARMIE | 55 to 56 |
| 11 | 1% | CLEFABLE | 56 |
| 12 | 1% | ABSOL | 56 |

Surf (60/30/5/4/1): TENTACRUEL 53 to 56, PELIPPER 53 to 56, STARMIE 54 to 56, MANTINE 54 to 56, LAPRAS 55.
Old Rod (70/30): MAGIKARP 25 to 30, TENTACOOL 25 to 30. Good Rod (60/20/20): SHELLDER 40 to 45, CORSOLA 40 to 45, STARYU 40 to 45. Super Rod (40/40/15/4/1): SEADRA 53 to 56, OCTILLERY 53 to 56, CLOYSTER 54 to 56, KINGDRA 55 to 56, GYARADOS 56.

**Trainers (7; levels 53 to 55).**

| Class | Where | Team |
|---|---|---|
| Bird Keeper | Forest path | Pelipper 53, Skarmory 54, Staraptor 54 |
| Camper | Forest path | Sandslash 53, Crawdaunt 54, Donphan 54 |
| Parasol Lady | Beach strip | Masquerain 53, Roserade 54 |
| Pokémon Ranger | Rest stop | Heracross 54, Scizor 54, Wyrdeer 55 |
| Fisherman | Pier end | Seaking 53, Whiscash 54, Gyarados 54 |
| Swimmer male | Water | Starmie 54, Kingdra 54 |
| Sailor | Pier | Tentacruel 53, Pelipper 54, Cloyster 55 |

**NPCs.** A **rest house** in the pines (Route 109's Seashore House idea, `LAYOUT_HOUSE1`; a free drink, no healing); a pier fisherman who gives a hint about Super Rod spots; a barge hand arguing with a clerk over a manifest (Scheme 9 seed: 'It says "permits (400)". It does not say whose.'); a walker with a map; a picnic couple. 5 NPCs.

**Items.** Visible: Super Repel, Max Ether. Hidden: Pearl on the pier, Heart Scale under a pine, Star Piece in the dunes. A Net Ball on a stump.

**Gate.** Surf (badge 5) and Waterfall (R22) get the player here. The land path needs nothing.

**Goldsworth beat.** None (the barge hands from R22 continue the seed).

**Flags (not claimed).** `FLAG_R23_BARGE_ARGUMENT_SEEN`, `FLAG_ITEM_R23_SUPER_REPEL`, `FLAG_ITEM_R23_MAX_ETHER`, `FLAG_ITEM_R23_NET_BALL`, `FLAG_HIDDEN_ITEM_R23_PEARL`, `_HEART_SCALE`, `_STAR_PIECE`.

**Build effort.** Medium (a long map with a pier and a rest house).

**Open questions.** Route 109 is mostly sand and sea in Hoenn; the pines on the path side are an add. Does the author want a Pokémon Center halfway (it would need a heal location)? I left it out.

---

## R24: Kingsquay to Driftsands (land, sketch 23 and 28)

**Length and shape.** A fenced land road through windbreak woods and a tall-grass patch, 40 x 28 (`(40 + 15) * (28 + 14) = 2310`). Mood: sandy, windy, tidy, hedges and a gate at the far end. Source: Palladium **`Route 38.png`**, 681 x 477 px gridded, **40 x 28 tiles**: a fenced lane with a long sandy path, a small tall-grass patch, a ledge, a signpost and a gatehouse on its east edge. Use a plain map connection at the gatehouse (Hoenn has no standard gate layout). (Palladium `Route 36.png`, 52 x 22, was my first pick but the west group has it.) Section id `MAPSEC_VELDRIS_ROUTE_24`.

**Edges.** West end enters Kingsquay's east gate (the lane's west end). East end (the gatehouse tile) enters Driftsands' west boardwalk. No side exits. A sandy loop to a lookout in the middle.

**Wild table (PROPOSED), levels 54 to 57.** Land only (the render has no pond).

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | PELIPPER | 54 to 55 |
| 2 | 20% | SANDSLASH | 54 to 55 |
| 3 | 10% | MACHOKE | 55 |
| 4 | 10% | SANDACONDA | 55 |
| 5 | 10% | CRABOMINABLE | 55 to 56 |
| 6 | 10% | STARAPTOR | 55 to 56 |
| 7 | 5% | CRUSTLE | 56 |
| 8 | 5% | DONPHAN | 56 |
| 9 | 4% | KINGLER | 56 to 57 |
| 10 | 4% | HERACROSS | 56 to 57 |
| 11 | 1% | SCIZOR | 57 |
| 12 | 1% | ABSOL | 57 |

**Trainers (7; levels 54 to 57).**

| Class | Team |
|---|---|
| Bug Maniac | Heracross 55, Scizor 55, Kleavor 56 |
| Camper | Sandslash 54, Crustle 55, Golem 55 |
| Picnicker | Kingler 55, Crabominable 55, Ludicolo 56 |
| Collector | Probopass 55, Magnezone 56, Bronzong 56 |
| Cooltrainer female | Wyrdeer 56, Gallade 56, Roserade 56 |
| Bird Keeper | Skarmory 56, Corviknight 56, Staraptor 56 |
| Beauty | Lapras 55, Milotic 56, Gardevoir 56 |

**NPCs.** A tourist heading for Driftsands; a gatekeeper-style old man at the Kingsquay end ('the road with sand in its shoes'); a child chasing a Starly that keeps stealing his hat; a flower-seller at the red beds who sells Pecha and Cheri berries; a lost clerk (Pip, PROPOSED, from Kingsquay) walking the wrong way. 4 NPCs.

**Items.** Visible: Rare Candy under a tree in the flower bed, Max Repel, PP Up on the lookout. Hidden: Revive, Heart Scale, Big Mushroom.

**Gate.** None.

**Goldsworth beat.** Optional: a solicitor's clerk pushes a hand-cart of boxes, and the wheel has come off (Scheme 9 seed; ties to R25).

**Flags (not claimed).** `FLAG_ITEM_R24_RARE_CANDY`, `FLAG_ITEM_R24_MAX_REPEL`, `FLAG_ITEM_R24_PP_UP`, `FLAG_HIDDEN_ITEM_R24_REVIVE`, `_HEART_SCALE`, `_BIG_MUSHROOM`.

**Build effort.** Easy to medium (a flat road with fences and flower beds).

**Open questions.** None specific. Is a no-water road here (the render has none) fine, given the sketch draws R24 as brown only?

---

## R25: Driftsands to Beaconmouth (land, sketch 24 and 27)

**Length and shape.** A cliff road to the last city, about 64 x 20 built (`(64 + 15) * (20 + 14) = 2686`). Mood: sea cliffs on the south, a grassy shelf, boulders, a stream across the road. Source: vanilla **`Route121`** (`Route121_Layout`, **80 x 20**) trimmed to 64 x 20: Lilycove's coastal road with cliffs and a grassy shelf. Add two ponds fed by a stream by hand. (Palladium `Route 42.png` fits this mood best but two other groups have it.) Section id `MAPSEC_VELDRIS_ROUTE_25`.

**Edges.** West end enters from Driftsands' north stair; east end enters Beaconmouth's south gate (offset: Beaconmouth's south edge, left). The stream under the road at the east end runs into Beaconmouth's harbour.

**Wild table (PROPOSED), levels 56 to 58.**

Grass:

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | GOLEM | 56 to 57 |
| 2 | 20% | MAGCARGO | 56 to 57 |
| 3 | 10% | SKARMORY | 57 |
| 4 | 10% | HARIYAMA | 57 |
| 5 | 10% | DONPHAN | 57 |
| 6 | 10% | PELIPPER | 57 |
| 7 | 5% | STEELIX | 57 to 58 |
| 8 | 5% | RHYDON | 57 to 58 |
| 9 | 4% | MAWILE | 58 |
| 10 | 4% | GLISCOR | 58 |
| 11 | 1% | TYRANITAR | 58 |
| 12 | 1% | DRAGONAIR | 58 |

Ponds, Surf (60/30/5/4/1): WHISCASH 56 to 58, SEAKING 56 to 58, GOLDUCK 57 to 58, AZUMARILL 57 to 58, GYARADOS 58.
Old Rod (70/30): MAGIKARP 25 to 30, BARBOACH 25 to 30. Good Rod (60/20/20): GOLDEEN 40 to 45, PSYDUCK 40 to 45, BARBOACH 40 to 45. Super Rod (40/40/15/4/1): WHISCASH 56 to 58, SEAKING 56 to 58, GOLDUCK 57 to 58, GYARADOS 58, MILOTIC 58.

**Trainers (7; levels 56 to 58).**

| Class | Team |
|---|---|
| Hiker | Golem 56, Steelix 57, Magcargo 56 |
| Hiker | Rhydon 57, Donphan 57, Probopass 57 |
| Black Belt | Hariyama 57, Machamp 57, Heracross 56 |
| Cooltrainer male | Gallade 57, Skarmory 57, Aggron 58 |
| Cooltrainer female | Gabite 57, Dragonair 57, Weavile 57 |
| Bird Keeper | Corviknight 57, Talonflame 57, Staraptor 57 |
| Dragon Tamer | Gabite 57, Dragonair 57, Shelgon 58 |

**NPCs.** A lamplighter hurrying down to Beaconmouth ('The tower is dry in summer and wet in autumn'); a ranger by the second pond; **a clerk with a hand-cart stuck in the stream** (Scheme 9 beat: the cart tips and the player sees a box stencilled 'PERMITS (400) TO THE LAST GYM'; he restacks it and asks the player not to mention it); a hiker with a view. 4 NPCs.

**Items.** Visible: Max Revive on a ledge, Hyper Potion, Rare Candy at the east end behind a boulder (Strength, badge 4), Protein. Hidden: Nugget, Star Piece, Max Ether.

**Gate.** None (Waterfall is not needed here; it is needed on R22 and at Beaconmouth's rear cove).

**Goldsworth beat.** The clerk with the cart. A seed for Scheme 9, no battle.

**Flags (not claimed).** `FLAG_R25_CART_SEEN`, `FLAG_ITEM_R25_MAX_REVIVE`, `FLAG_ITEM_R25_HYPER_POTION`, `FLAG_ITEM_R25_RARE_CANDY`, `FLAG_ITEM_R25_PROTEIN`, `FLAG_HIDDEN_ITEM_R25_NUGGET`, `_STAR_PIECE`, `_MAX_ETHER`.

**Build effort.** Medium (a long cliff road with two ponds).

**Open questions.** Route 121 has no ponds, so the two ponds and the stream are added by hand. Is a hand-built stream acceptable, or would the author rather use a pond-bearing base?

---

## R26: Beaconmouth to Aldermere (water, post-game, sketch 25 and 26)

**Length and shape.** An open sea road with a current, 80 x 40 (`(80 + 15) * (40 + 14) = 5130`). Mood: grey water, the sea slowly pulling toward the drowned city, a few rocks. Source: vanilla **`Route134`** (`Route134_Layout`, 80 x 40), a sea route whose current runs toward the ruins and which has `Underwater_Route134` below it. It is Hoenn's own route to a sealed ruin, so the mood matches. Section id `MAPSEC_VELDRIS_ROUTE_26`.

**Edges.** East end enters Beaconmouth's west edge (the harbour mouth, rope-gated until `FLAG_SYS_GAME_CLEAR`). West end enters Aldermere's east quay. Dive spots mid-route (the underwater companion map).

**Wild table (PROPOSED), levels 62 to 68.** No land.

Surf (60/30/5/4/1): TENTACRUEL 62 to 66, LUMINEON 62 to 66, MANTINE 64 to 67, GOREBYSS 65 to 67, RELICANTH 66 to 68.
Old Rod (70/30): MAGIKARP 25 to 30, TENTACOOL 25 to 30. Good Rod (60/20/20): LUVDISC 45 to 50, CORSOLA 45 to 50, FINNEON 45 to 50. Super Rod (40/40/15/4/1): LUMINEON 62 to 66, CLAWITZER 62 to 66, JELLICENT 64 to 67, KINGDRA 66 to 68, RELICANTH 66.
Dive (underwater), levels 62 to 67: CLAMPERL 62 to 65 (60%), RELICANTH 64 to 67 (30%), HUNTAIL 65 to 67 (5%), GOREBYSS 65 to 67 (4%), WAILORD 66 to 67 (1%).

**Trainers (6; levels 62 to 68).**

| Class | Team |
|---|---|
| Swimmer male | Starmie 63, Floatzel 64, Kingdra 64 |
| Swimmer male | Wailord 64, Mantine 65 |
| Swimmer female | Milotic 65, Jellicent 65, Lanturn 64 |
| Swimmer female | Alomomola 64, Gastrodon 65, Walrein 65 |
| Fisherman | Gyarados 64, Whiscash 65, Sharpedo 65 |
| Sailor | Pelipper 64, Tentacruel 65, Cloyster 65, Kingdra 66 |

**NPCs.** A ferry captain at Beaconmouth (sets the gate flag); a diver near a red buoy (hint); an old fisher who tells the player to stay off the current's edge; a bobbing researcher on a boat (Aldermere's Researcher, hints about Unown). 3 NPCs.

**Items.** Visible: Max Revive on a rock, Rare Candy on a sandbar. Dive: Big Pearl, Pearl String, Relic Silver, Star Piece, Nugget.

**Gate.** **Story:** `FLAG_SYS_GAME_CLEAR` (the quay rope). **HM:** Surf, and **Dive (badge 9)** for the underwater spots (not for the road itself).

**Goldsworth beat.** None.

**Flags (not claimed).** `FLAG_R26_OPEN` (set with game clear), `FLAG_ITEM_R26_MAX_REVIVE`, `FLAG_ITEM_R26_RARE_CANDY`, `FLAG_HIDDEN_ITEM_R26_*` for the Dive items.

**Build effort.** Medium (a sea map plus its underwater twin).

**Open questions.** The sketch draws a brown line next to R26 (25 and 26). A land path is possible (cliff walk); I made it water only, as README's table says.

---

## R27: Vesperhaven to Wendlebury (water, post-game, no sketch number)

**Length and shape.** A long east-west sea road, about 80 x 40 built (`(80 + 15) * (40 + 14) = 5130`). Mood: open sea, big swells, a coast-guard cutter at the Vesperhaven end. Source: vanilla **`Route128`** (`Route128_Layout`, 120 x 40) trimmed to 80 x 40, or **`Route129`** (80 x 40) as it stands. (The centre group has Route 129 for R19. Route 128 appears unused.) Section id `MAPSEC_VELDRIS_ROUTE_27`.

**Edges.** West end enters Wendlebury's east or south dock (water). East end enters Vesperhaven's west sea gate. No side exits.

**Wild table (PROPOSED), levels 60 to 66.**

Surf (60/30/5/4/1): WAILORD 60 to 64, PELIPPER 60 to 64, MANTINE 62 to 65, ALOMOMOLA 62 to 65, LAPRAS 64 to 66.
Old Rod (70/30): MAGIKARP 25 to 30, TENTACOOL 25 to 30. Good Rod (60/20/20): WAILMER 45 to 50, CHINCHOU 45 to 50, QWILFISH 45 to 50. Super Rod (40/40/15/4/1): WAILORD 60 to 64, LANTURN 60 to 64, SHARPEDO 62 to 64, GYARADOS 64 to 66, MILOTIC 66.

**Trainers (6; levels 60 to 63).**

| Class | Team |
|---|---|
| Sailor | Pelipper 60, Tentacruel 61, Wailord 62 |
| Swimmer male | Starmie 61, Floatzel 62, Kingdra 62 |
| Swimmer female | Milotic 62, Mantine 62, Jellicent 63 |
| Fisherman | Gyarados 61, Whiscash 62, Sharpedo 63 |
| Tuber male | Politoed 61, Azumarill 62 |
| Sailor | Cloyster 61, Barraskewda 62, Toxapex 62 |

**NPCs.** The **coast guard cutter** at the Vesperhaven end (hide flag at game clear; 'League business'); a Wendlebury sailor selling a rumour; a fisher out of reach. 3 NPCs.

**Items.** Visible: Rare Candy, Max Elixir, Dive Ball. No Dive spots (or one optional: Pearl String).

**Gate.** Story: `FLAG_SYS_GAME_CLEAR` (the cutter leaves). Surf.

**Goldsworth beat.** None.

**Flags (not claimed).** `FLAG_R27_CUTTER_GONE` (shared with `FLAG_VESPERHAVEN_GATES_OPEN` if the author wants one flag), `FLAG_ITEM_R27_RARE_CANDY`, `_MAX_ELIXIR`, `_DIVE_BALL`.

**Build effort.** Easy to medium (a big, mostly empty sea).

**Open questions.** Does Vesperhaven open from Wendlebury before the League? The sketch's note says 'only unlocks post game', so no.

---

## R28: Vesperhaven to Ebbsworth (water, post-game, no sketch number)

**Length and shape.** A short strait, 60 x 20 (`(60 + 15) * (20 + 14) = 2550`). Mood: a sheltered channel, buoys, a reef. Source: vanilla **`Route106`** (`Route106_Layout`, 80 x 20), Dewford's rocky sea strip, trimmed to 60. (`Route107` is taken by the east group for R17.) Section id `MAPSEC_VELDRIS_ROUTE_28`.

**Edges.** West end enters Vesperhaven's east sea gate; east end enters Ebbsworth's west harbour mouth (sea gate, rope until game clear). No side exits.

**Wild table (PROPOSED), levels 62 to 68.**

Surf (60/30/5/4/1): TENTACRUEL 62 to 66, FLOATZEL 62 to 66, SEAKING 63 to 66, GASTRODON 64 to 67, KINGDRA 66 to 68.
Old Rod (70/30): MAGIKARP 25 to 30, TENTACOOL 25 to 30. Good Rod (60/20/20): SEEL 45 to 50, SHELLOS 45 to 50, FINNEON 45 to 50. Super Rod (40/40/15/4/1): SEADRA 62 to 66, OCTILLERY 62 to 66, QWILFISH 64 to 66, KINGDRA 66 to 68, GYARADOS 68.

**Trainers (5; levels 63 to 66).**

| Class | Team |
|---|---|
| Swimmer male | Floatzel 63, Starmie 64, Kingdra 64 |
| Swimmer female | Lanturn 63, Alomomola 64, Milotic 64 |
| Sailor | Pelipper 64, Gastrodon 64, Dewgong 65 |
| Fisherman | Qwilfish 63, Gyarados 65, Whiscash 64 |
| Triathlete | Poliwrath 64, Ludicolo 65, Swampert 66 |

**NPCs.** A buoy keeper; a cutter on the Vesperhaven side (hidden at game clear); a fisher with a story about the harbour that is not on any map. 3 NPCs.

**Items.** Visible: Max Revive on a reef rock, Rare Candy. Optional Dive spot: Big Pearl.

**Gate.** Story: `FLAG_SYS_GAME_CLEAR`. Surf.

**Goldsworth beat.** None.

**Flags (not claimed).** `FLAG_R28_CUTTER_GONE` (or the shared gate flag), `FLAG_ITEM_R28_MAX_REVIVE`, `_RARE_CANDY`.

**Build effort.** Easy.

**Open questions.** None specific.

---

## R29: Vesperhaven to Silverstrand (water, post-game, no sketch number)

**Length and shape.** A long north-south channel, about 48 x 80 built (`(48 + 15) * (80 + 14) = 5922`). Mood: a wide quiet sea with islets, a lamp on a rock, a hush. Source: vanilla **`Route126`** (`Route126_Layout`, 80 x 80, with `Underwater_Route126`), the dive route down to Hoenn's hidden city: right for a hidden coast. Trim to 48 columns. (`Route105` is taken by the east group for R16.) Section id `MAPSEC_VELDRIS_ROUTE_29`.

**Edges.** North end enters Vesperhaven's south-west strait; south end enters Silverstrand's jetty. No side exits.

**Wild table (PROPOSED), levels 64 to 70.**

Surf (60/30/5/4/1): STARMIE 64 to 68, DEWGONG 64 to 68, CLOYSTER 65 to 68, WALREIN 66 to 69, PALAFIN 68 to 70.
Old Rod (70/30): MAGIKARP 25 to 30, TENTACOOL 25 to 30. Good Rod (60/20/20): SPHEAL 45 to 50, STARYU 45 to 50, CORSOLA 45 to 50. Super Rod (40/40/15/4/1): STARMIE 64 to 68, DEWGONG 64 to 68, WALREIN 66 to 69, GYARADOS 68 to 70, MILOTIC 70.
Dive (underwater), levels 64 to 69: CLAMPERL 64 to 66 (60%), LUVDISC 65 to 67 (30%), HUNTAIL 66 to 68 (5%), GOREBYSS 66 to 68 (4%), RELICANTH 68 to 69 (1%).

**Trainers (6; levels 66 to 68).**

| Class | Team |
|---|---|
| Swimmer male | Wailord 66, Starmie 66 |
| Swimmer female | Lapras 67, Walrein 67, Dewgong 66 |
| Sailor | Cloyster 66, Tentacruel 67, Kingdra 68 |
| Fisherman | Gyarados 67, Sharpedo 67, Barraskewda 66 |
| Tuber female | Azumarill 66, Palafin 67 |
| Cooltrainer male (on a rock) | Milotic 68, Lanturn 66, Toxapex 67 |

**NPCs.** A cutter at the Vesperhaven end; a lamp-keeper on a rock; a fisher who says Silverstrand is 'where the sea keeps its sand'. 3 NPCs.

**Items.** Visible: Max Revive, Rare Candy, Dive Ball x3 on a reef. Dive spots: Pearl String, Big Pearl, Relic Gold, Nugget.

**Gate.** Story: `FLAG_SYS_GAME_CLEAR`. Surf; **Dive (badge 9)** for the underwater spots.

**Goldsworth beat.** None.

**Flags (not claimed).** `FLAG_R29_CUTTER_GONE`, `FLAG_ITEM_R29_*`, `FLAG_HIDDEN_ITEM_R29_*`.

**Build effort.** Medium (a long map and an underwater twin).

**Open questions.** Route 126 is Hoenn's dive route into the hidden city, so Dive spots fit here. Keep them, or use them only on R26?

---

## R30: Vesperhaven to Echo Hollow (land, post-game, no sketch number)

**Length and shape.** A short cliff road down to a cave mouth, about 22 x 30 built (`(22 + 15) * (30 + 14) = 1628`). Mood: bare stone, a sense of being watched, a cave door at the end. Source: Palladium **`Route 33.png`**, 375 x 307 px gridded, **22 x 18 tiles**: a hill with a rock cave door at the top, a signpost and a grass pocket. In Johto this route leads to Union Cave, which is exactly Echo Hollow. Extend it south by hand to about 30 rows for a proper road. Section id `MAPSEC_VELDRIS_ROUTE_30`.

**Edges.** South end enters Vesperhaven's south-east stair (offset to match the stair position). North end is the cave door into Echo Hollow ([landmarks-south.md](landmarks-south.md)). No other exits.

**Wild table (PROPOSED), levels 66 to 72.**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | GOLEM | 66 to 68 |
| 2 | 20% | SKARMORY | 66 to 68 |
| 3 | 10% | SABLEYE | 67 to 69 |
| 4 | 10% | NOIVERN | 68 to 70 |
| 5 | 10% | CRUSTLE | 68 to 70 |
| 6 | 10% | SWOOBAT | 68 to 70 |
| 7 | 5% | ABSOL | 70 |
| 8 | 5% | STEELIX | 70 to 71 |
| 9 | 4% | GLISCOR | 71 |
| 10 | 4% | WEAVILE | 71 to 72 |
| 11 | 1% | TYRANITAR | 72 |
| 12 | 1% | ZWEILOUS | 72 |

**Trainers (6; levels 67 to 71).**

| Class | Team |
|---|---|
| Hiker | Golem 67, Steelix 68, Rhyperior 69 |
| Black Belt | Machamp 68, Hariyama 68, Heracross 69 |
| Psychic | Alakazam 69, Gallade 69 |
| Cooltrainer female | Weavile 70, Froslass 69, Mamoswine 70 |
| Ruin Maniac (at the cave mouth) | Sigilyph 69, Claydol 69, Golurk 70 |
| Cooltrainer male | Dragonite 70, Hydreigon 70 |

**NPCs.** A signpost reader at the Vesperhaven end; a hiker with a thermos; an old woman who says the cave 'repeats you', the Echo Hollow hint. 3 NPCs.

**Items.** Visible: Max Revive, Rare Candy x2, Full Heal. Hidden: Star Piece, Max Elixir.

**Gate.** Story: the road opens after `FLAG_SYS_GAME_CLEAR` (Vesperhaven's service stair). No HM.

**Goldsworth beat.** None.

**Flags (not claimed).** `FLAG_R30_OPEN`, `FLAG_ITEM_R30_*`, `FLAG_HIDDEN_ITEM_R30_*`.

**Build effort.** Easy to medium (a compact map).

**Open questions.** None specific.

---

## R31: Hollowbrook to Argent Peak (land, post-game, no sketch number)

**Length and shape.** A long mountain trail, about 40 x 70 built (`(40 + 15) * (70 + 14) = 4620`). Mood: a climb by ledges, rock walls, tall grass at the bends, sea wind. Source: vanilla **`Route115`** (`Route115_Layout`, 40 x 80), the cliff road beside Meteor Falls with rock ledges and a sea edge, trimmed to 70 rows. (Palladium `Route 45.png`, 22 x 91, suits it best but the centre group has it.) Section id `MAPSEC_VELDRIS_ROUTE_31`.

**Edges.** South end enters Hollowbrook's south-west edge (a gate with a locked fence until `FLAG_SYS_GAME_CLEAR`; this is the sketch's brown landmark line from Hollowbrook). North end enters Argent Peak's Base Camp (south gate). No side exits.

**Wild table (PROPOSED), levels 68 to 74.**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | GOLEM | 68 to 70 |
| 2 | 20% | URSARING | 68 to 70 |
| 3 | 10% | MISMAGIUS | 69 to 71 |
| 4 | 10% | MACHAMP | 70 to 72 |
| 5 | 10% | PILOSWINE | 70 to 72 |
| 6 | 10% | MAGCARGO | 70 to 72 |
| 7 | 5% | STEELIX | 72 to 73 |
| 8 | 5% | WEAVILE | 72 to 73 |
| 9 | 4% | DRAGONAIR | 73 |
| 10 | 4% | GABITE | 73 to 74 |
| 11 | 1% | TYRANITAR | 74 |
| 12 | 1% | MAMOSWINE | 74 |

**Trainers (7; levels 70 to 73).**

| Class | Team |
|---|---|
| Hiker | Golem 70, Steelix 71, Rhyperior 72, Magcargo 71 |
| Black Belt | Machamp 71, Conkeldurr 72, Hariyama 71 |
| Cooltrainer female | Mamoswine 72, Weavile 72, Glaceon 71 |
| Cooltrainer male | Garchomp 73, Dragonite 73 |
| Psychic | Gardevoir 71, Alakazam 72, Gallade 72 |
| Pokémon Ranger | Ursaluna 72, Wyrdeer 71, Scizor 72 |
| Expert | Tyranitar 73, Aggron 72, Lucario 73 |

**NPCs.** A ranger at Hollowbrook's south-west fence (opens at game clear; 'It is closed in winter. It is also closed in summer. It is open now.'); a hiker with a flask; an old woman who knew Gatsby (hook for the post-game: a hint that he and a friend once climbed it); a child who has been told not to go. 4 NPCs.

**Items.** Visible: Max Revive, Rare Candy, PP Max, Full Restore. Hidden: Star Piece, Nugget, Max Elixir. (Leftovers is on the Argent Peak summit.)

**Gate.** Story: `FLAG_SYS_GAME_CLEAR`. Optional: Cut (a tree on the trail), Strength (a boulder), Rock Smash (a cracked rock to a nook): all earlier badges.

**Goldsworth beat.** None. An optional hook: a pile of old stones with 'G + C' scratched in one (Gatsby and Cynthia, from [../postgame.md](../postgame.md); the sketch's landmark idea was 'the old orchard or cabin where Gatsby met Cynthia').

**Flags (not claimed).** `FLAG_R31_OPEN` (or reuse `FLAG_ARGENT_PEAK_OPEN`), `FLAG_ITEM_R31_*`, `FLAG_HIDDEN_ITEM_R31_*`.

**Build effort.** Medium. The long climb is a long map, but it is only traced.

**Open questions.**
1. Is a 70-tile climb at Hollowbrook's door the right feel for a post-game road, or should it be shorter? Hoenn's Route 115 has water on one side: keep it as a coast cliff, or fill it in?
2. The sketch shows the landmark one short brown line from Hollowbrook; the vanilla route is long. Fine to trim?
