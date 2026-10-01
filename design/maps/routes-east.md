# Routes, the east (R13 to R17)

> **Open question (author, 2026-10-01): the Palladium route renders named in this file are NOT decided.** The author doubts that reusing Palladium route images will give a quality hack, so every 'source render' for a road below is a **mood and shape reference only** until the author decides how each road gets built (traced, redrawn or designed fresh). Lengths, edges, trainers, items and encounters stay as written.


Status: **PROPOSED.** Road cards for the east group, in the order of the table in [README.md](README.md) ('Route numbering'), which is my reading of the sketch and **needs the author's confirmation**. Settlements: [towns/hemlock-reach.md](towns/hemlock-reach.md), [towns/primrose-vale.md](towns/primrose-vale.md), [towns/brinecombe.md](towns/brinecombe.md), and Waymeet (centre group, not written here). Landmark: [landmarks-east.md](landmarks-east.md).

**Summary**

| Route | Between | Kind | Source render | Tiles | Section id (existing Hoenn entry reused, [../region-sketch.md](../region-sketch.md)) | Levels |
|---|---|---|---|---|---|---|
| R13 | Waymeet, Hemlock Reach | land | Palladium Route 42 | 64 x 23 | `MAPSEC_ROUTE_120` | 39 to 45 |
| R14 | Hemlock Reach, Brinecombe | water | Palladium Route 40, rotated and widened | 56 x 24 | `MAPSEC_ROUTE_123` | 45 to 50 |
| R15 | Primrose Vale, Brinecombe | land | Palladium Route 43 | 30 x 54 | `MAPSEC_ROUTE_124` | 47 to 52 |
| R16 | Hemlock Reach, Mirror Isle | water | vanilla `Route105`, trimmed | 40 x 60 | `MAPSEC_ROUTE_126` | 44 to 50 |
| R17 | Mirror Isle, Primrose Vale | water | vanilla `Route107`, trimmed | 56 x 20 | `MAPSEC_ROUTE_127` | 46 to 52 |

Porymap's dropdown shows the old constant while the game shows the Veldris name (ROUTE 13 and so on).

**Levels.** The curve in the README says a road runs from the gym behind it minus 3 to the gym ahead minus 3, shifted up a little where the road can be walked either way. Hemlock Reach (gym 7, ace 48) is reached via R13 after Gildhaven (gym 6, ace 42): **R13 runs 39 to 45**. Primrose Vale (gym 8, ace 55) follows: **R14, R15, R16, R17 run about 45 to 52**, with the rod and Rock Smash tables set lower for the cheaper tiers. All trainers use `IVs: 0` and reuse vanilla Hoenn ids (README). Wild Pokémon are not changed by that rule.

**Species check.** Every species named below was checked against `include/constants/species.h` and `src/data/pokemon/species_info/` in this tree (script run 2026-10-01). Form aliases (Floette, Florges, Mimikyu and the like) resolve to a base form but exist.

**Object budget.** Maps carry at most 15 live objects (README). Each road notes trainers + NPCs + visible items against that.

**Water road rules.** Surf slots follow vanilla's shape: 5 slots, rates 60/30/5/4/1. Fishing: Old Rod 2 slots (70/30), Good Rod 3 slots (60/20/20), Super Rod 5 slots (40/40/15/4/1). Rod levels are lower than the surf levels for the cheaper tiers.

---

## R13: Waymeet to Hemlock Reach (land, sketch 13)

**Feel.** A rocky heath road climbing east to the cliffs, with two small ponds, dry-stone walls, a boundary stone and a lot of people carrying baskets of herbs. It is the road the apothecaries use to fetch their ingredients. Mid-late game: mostly Poison and Rock types at 40 to 45.

**Shape.** 64 wide x 23 tall, a long east-west pass. Check: (64 + 15) x (23 + 14) = 2923, under 10240.

**Source.** Palladium `Route 42.png` (1089 x 392 px, 1 px grid, `(px-1)/17` = **64 x 23**). It is a mountain pass with a cliff band across the north, two ponds in the middle, a one-way ledge, a few Rock Smash rocks and a gatehouse at the west end. Trace it by eye in Porymap (README). Section `MAPSEC_ROUTE_120` (shown ROUTE 13).

**Edges.**
- **West edge** meets Waymeet's east edge, low in the map (about rows 15 to 18 of 23). In the picture the west end holds a gatehouse building; drop it (Waymeet is a town, not a toll booth) or keep it as a small rest-stop interior with one NPC.
- **East edge** meets Hemlock Reach's west edge at the south-west gap of Hemlock's Lower Quay. The east mouth of the picture is mid-height; the author may shift it to rows 17 to 20 to cut the connection offset.
- One **one-way ledge** drops from the northern cliff to the road in the middle (no way back up, a shortcut for the return walk).
- **Side:** a boundary-stone clearing in the north rock band that is the Strength boulder shelf. A small spur.

**Wild Pokémon (land, tall grass, 12 slots, levels 39 to 45).**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | GOLBAT | 40 to 41 |
| 2 | 20% | SKORUPI | 40 to 41 |
| 3 | 10% | STUNKY | 40 to 41 |
| 4 | 10% | KOFFING | 40 to 42 |
| 5 | 10% | GRAVELER | 41 to 42 |
| 6 | 10% | SKUNTANK | 42 to 43 |
| 7 | 5% | MACHOKE | 43 |
| 8 | 5% | GURDURR | 43 to 44 |
| 9 | 4% | RHYHORN | 43 |
| 10 | 4% | WEEZING | 44 to 45 |
| 11 | 1% | DRAPION | 45 |
| 12 | 1% | GLIGAR | 45 |

Rates add to 100%.

**Rock Smash rocks (5 slots, 60/30/5/4/1, levels 40 to 44):** GRAVELER 60, RHYHORN 30, ONIX 5, DWEBBLE 4, BOLDORE 1.

**Ponds (fishing, freshwater).** Old Rod: MAGIKARP 70 (20 to 25), BARBOACH 30 (20 to 25). Good Rod: BARBOACH 60 (34 to 38), GOLDEEN 20 (34 to 38), SEAKING 20 (36 to 38). Super Rod: WHISCASH 40 (42 to 45), SEAKING 40 (42 to 45), GYARADOS 15 (43 to 45), QUAGSIRE 4 (42 to 44), LANTURN 1 (44). No Surf slots (the ponds are too small to surf).

**Trainers (7).**

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Hiker | Graveler 40, Machoke 40, Rhyhorn 41 | On the west rocks, the first met |
| 2 | Aroma Lady | Roselia 41, Gloom 41 | Herb picker, leads from a basket |
| 3 | Collector | Koffing 40, Skorupi 41 | Labels everything |
| 4 | Picnicker | Skuntank 42, Gligar 41 | At the pond |
| 5 | Ruin Maniac | Graveler 42, Golem 43 | Obsessed with the boundary stone |
| 6 | Black Belt | Machoke 43, Gurdurr 44 | On the ledge |
| 7 | Bird Keeper | Golbat 44, Gligar 43 | Last, near Hemlock; the toughest (44) |

All reuse vanilla ids; no IVs.

**NPCs (3).** Hazmat foreshadow: two men in white suits with a stamp ring stand at a milestone and argue about whose clipboard it is (Scheme 7 foreshadow, like Route 1's surveyors); a herb gatherer who says the best leaves grow where the ground is worst; a walker who points out Hemlock Reach on the horizon. Optional: a rest bench with a pot of tea (Pecha Berry cure for the party, one-time, flavour).

**Items (visible 4, hidden 3).**

| Item | Where | Gate |
|---|---|---|
| HYPER POTION | open ground, middle | none |
| FULL HEAL | behind a Cut tree, north of the road | Cut (badge 1) |
| TM Brick Break | boulder shelf in the north rock band | Strength (badge 4) |
| MAX REPEL | south-west fork | none |
| Hidden: PP UP | under the boundary stone | none |
| Hidden: ETHER | beside the second pond | none |
| Hidden: ANTIDOTE | in the herb bed | none |

**Signs.** West end ('WAYMEET'), the boundary stone (flavour: 'HERE ENDS THE PARISH. THE NEXT IS WORSE.'), east end ('HEMLOCK REACH, CHEMISTS WELCOME').

**Gate.** None. Cut, Strength and Rock Smash are optional. R13 is reachable by land from Waymeet (R12 Lingmoor, R19 Gildhaven) before any Surf.

**Object budget:** 7 trainers + 3 NPCs + 4 items = 14 of 15.

**Goldsworth beat.** Scheme 7 foreshadow only (the milestone argument), as noted. No Troglodyte here.

**Flags (not claimed).** `FLAG_R13_SCHEME7_FORESHADOW` (optional), one-shot flags for the items and the tea bench, trainer flags from reused ids, hidden items in the 0x264 block.

**Build effort: medium.** One 64 x 23 trace, ponds and rock bands, three small scripts, seven trainers.

**Open questions.** Keep the west gatehouse? Does the boundary-stone shelf need a Strength tutorial hint from an NPC?

---

## R14: Hemlock Reach to Brinecombe (water, sketch 14 and 17)

**Feel.** Open sea with a reef: two lines of rocks (the picture's whirlpool-style rock pairs) mark the sailing lane, a few islets, gulls overhead, a lighthouse buoy. Cold, bright and a little salty. Surf from badge 5.

**Shape.** The Palladium picture is a vertical sea, 20 wide x 34 tall. I propose it **rotated a quarter turn** to run west to east and **widened to 56 x 24** with open water (Change Dimensions, then repaint elevation, README). Check: (56 + 15) x (24 + 14) = 2698, under 10240.

**Source.** Palladium `Route 40.png` (341 x 579 px, 1 px grid, **20 x 34**). It is the east group's only Palladium sea route. The beach at one end becomes Hemlock's landing; the two rows of rocks continue along the road. Section `MAPSEC_ROUTE_123` (shown ROUTE 14). Alternative if the author does not want a rotated trace: vanilla `Route107` (60 x 20).

**Edges.**
- **West edge** meets Hemlock Reach's east shore (the Lower Quay), mid-south of Hemlock's map.
- **East edge** meets Brinecombe's west shore, **lower than Hemlock's** (Brinecombe is south-east), so the two connection offsets differ by about ten rows.
- No side exits. Two islets to the north with items.

**Wild Pokémon (water, levels 45 to 50).**

| Surf slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 60% | TENTACRUEL | 45 to 49 |
| 2 | 30% | PELIPPER | 46 to 50 |
| 3 | 5% | MANTINE | 47 to 50 |
| 4 | 4% | WAILORD | 48 to 50 |
| 5 | 1% | LAPRAS | 49 to 50 |

| Fishing | Slot | Rate | Species | Levels |
|---|---|---|---|---|
| Old Rod | 1 | 70% | MAGIKARP | 20 to 25 |
| Old Rod | 2 | 30% | TENTACOOL | 22 to 26 |
| Good Rod | 1 | 60% | QWILFISH | 38 to 42 |
| Good Rod | 2 | 20% | TENTACRUEL | 38 to 42 |
| Good Rod | 3 | 20% | STARYU | 38 to 42 |
| Super Rod | 1 | 40% | QWILFISH | 46 to 50 |
| Super Rod | 2 | 40% | TENTACRUEL | 46 to 50 |
| Super Rod | 3 | 15% | GYARADOS | 46 to 50 |
| Super Rod | 4 | 4% | TOXAPEX | 48 to 50 |
| Super Rod | 5 | 1% | OVERQWIL | 50 |

**Trainers (6, all on the water or on islets, sight lines over water).**

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Sailor | Pelipper 46, Tentacruel 47 | Near Hemlock |
| 2 | Swimmer (M) | Wailord 47, Starmie 47 | Middle |
| 3 | Swimmer (F) | Starmie 46, Luvdisc 46 | North islet |
| 4 | Fisherman | Qwilfish 46, Gyarados 48 | Near the reef |
| 5 | Sailor | Mantine 46, Pelipper 47 | East |
| 6 | Triathlete | Tentacruel 48, Seadra 48 | Last, near Brinecombe; the toughest (48) |

**NPCs (2).** A buoy keeper on a tiny islet (tells the player the lane is safe 'between the rocks'); a Goldsworth compliance launch bobbing far off, ambient only (Scheme 7 foreshadow, no battle).

**Items (3 visible, 2 hidden).**

| Item | Where | Gate |
|---|---|---|
| ETHER | north islet | Surf |
| ELIXIR | middle rock | Surf |
| MAX REVIVE | reef corner | Surf |
| Hidden: PEARL | sea floor off the reef | Surf |
| Hidden: BIG PEARL | Dive spot under the second reef | **Dive (badge 9)**, return trip, PROPOSED |

**Gate.** **Surf (badge 5)** to enter. Dive (badge 9) only for the optional hidden item.

**Object budget:** 6 trainers + 2 NPCs + 3 items = 11 of 15.

**Goldsworth beat.** None. Scheme 7 foreshadow via the launch (ambient).

**Flags (not claimed).** One-shot item flags, trainer flags from reused ids, `FLAG_R14_BIG_PEARL` hidden item (0x264 block).

**Build effort: easy to medium.** A sea route is mostly open water; the work is the rotation and the reef lines.

**Open questions.** Rotate Route 40, or use vanilla `Route107`? Also: Brinecombe's pier is the arrival point; should R14 also have a Surf-only shortcut to R16?

---

## R15: Primrose Vale to Brinecombe (land, sketch 15 and 16)

**Feel.** A woodland and meadow road along the edge of a narrow stream, picking up the first petals as it nears Primrose Vale. Soft, warm light, hedges, small gatehouses. Mostly Fairy and Grass types at 47 to 52. Land route, but only reachable by Surf (Brinecombe is Surf-only), so it feels like a hidden valley.

**Shape.** 30 wide x 54 tall, north-south. Check: (30 + 15) x (54 + 14) = 3060, under 10240.

**Source.** Palladium `Route 43.png` (511 x 919 px, 1 px grid, `(px-1)/17` = **30 x 54**). It is a wooded valley with a narrow stream and pool in the west, a gatehouse on the east side, fenced paths and a stretch of tall grass. Section `MAPSEC_ROUTE_124` (shown ROUTE 15).

**Edges.**
- **North edge** meets Primrose Vale's south edge, at the centre of the gate court (the north gate of the picture becomes the garden gate arch).
- **South edge** meets Brinecombe's north edge, at the cliff gap (left of centre in the town).
- The picture's east gatehouse becomes a small **rest hut** with a free healing item (PROPOSED): a toll-house joke ('the toll is a kind word').
- One side exit: a narrow path east to a clearing with a Strength boulder.

**Wild Pokémon (land, 12 slots, levels 47 to 52).**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | ROSELIA | 47 to 48 |
| 2 | 20% | FLOETTE | 47 to 48 |
| 3 | 10% | GRANBULL | 48 |
| 4 | 10% | COTTONEE | 47 to 48 |
| 5 | 10% | GLOOM | 48 |
| 6 | 10% | PETILIL | 48 to 49 |
| 7 | 5% | RIBOMBEE | 49 |
| 8 | 5% | KIRLIA | 49 to 50 |
| 9 | 4% | MAWILE | 50 |
| 10 | 4% | SWIRLIX | 50 |
| 11 | 1% | COMFEY | 51 |
| 12 | 1% | TOGETIC | 52 |

Rates add to 100%.

**Stream and pool (fishing, freshwater; Surf in the pool).** Surf slots (pool): AZUMARILL 60 (46 to 50), GOLDUCK 30 (46 to 50), SLOWBRO 5 (48 to 50), SEAKING 4 (47 to 50), LUMINEON 1 (50). Old Rod: MAGIKARP 70 (20 to 25), MARILL 30 (20 to 25). Good Rod: SEAKING 60 (38 to 42), AZUMARILL 20 (38 to 42), LUMINEON 20 (38 to 42). Super Rod: AZUMARILL 40 (46 to 50), SEAKING 40 (46 to 50), GYARADOS 15 (46 to 50), LUMINEON 4 (48 to 50), MILOTIC 1 (50).

**Trainers (7).**

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Parasol Lady | Floette 47, Whimsicott 48 | At the south gate |
| 2 | Picnicker | Cottonee 47, Granbull 48 | In the grass |
| 3 | Aroma Lady | Roselia 48, Bellossom 49 | By the stream |
| 4 | Beauty | Ribombee 48, Swirlix 48 | On the path |
| 5 | Lady | Mawile 49, Granbull 49 | Near the hut |
| 6 | PokeFan | Dedenne 48, Togetic 49 | Beside the boulder clearing |
| 7 | Fisherman | Seaking 48, Quagsire 49 | At the pool; the toughest (49) |

All reuse vanilla ids; no IVs.

**NPCs (3).** A surveyor with a tripod and an orange flag at the north end, 'only measuring' (Scheme 8 foreshadow, like Route 1's surveyors); a rest-hut keeper; a walker carrying a bouquet for Primrose Vale's gym.

**Items (4 visible, 3 hidden).**

| Item | Where | Gate |
|---|---|---|
| REVIVE | open ground, south | none |
| SUPER POTION | by the stream | none |
| TM Solar Beam | boulder clearing, east side | Strength (badge 4) |
| FULL HEAL | rest hut shelf | none |
| Hidden: ELIXIR | tall grass, north | none |
| Hidden: MAX REPEL | under a hedge | none |
| Hidden: REVIVE | pool edge | none |

**Signs.** South end ('BRINECOMBE'), the hut, north end ('PRIMROSE VALE, KEEP TO THE PATHS').

**Gate.** None on the road itself, but it is only reachable after Surf (R14 or R17). Cut and Strength optional.

**Object budget:** 7 trainers + 3 NPCs + 4 items = 14 of 15 (the hut interior is a separate map).

**Goldsworth beat.** Scheme 8 foreshadow (the surveyor). No Troglodyte.

**Flags (not claimed).** `FLAG_R15_SCHEME8_FORESHADOW` (optional), one-shot item flags, hut flag, hidden items in the 0x264 block.

**Build effort: medium.** One 30 x 54 trace and a small interior.

**Open questions.** Should R15 join Primrose Vale by land only (current plan) and thus force a Surf trip? Keep the rest hut?

---

## R16: Hemlock Reach to Mirror Isle (water, sketch 18 and 19)

**Feel.** A still, cold mere dotted with reed islets and a ruined jetty. Quiet, a bit mournful: this is the 'lake' part of the east. Surf only.

**Shape.** 40 wide x 60 tall, north-south, trimmed from vanilla `Route105` (40 x 80). Check: (40 + 15) x (60 + 14) = 4070, under 10240.

**Source.** Vanilla `Route105` layout (`LAYOUT_ROUTE105`, 40 x 80). It is a vertical sea with several islets, which suits a lake road (no Palladium match: Route 40 is already used for R14). After duplicating, delete the old Hoenn cave and Regi-puzzle warps and objects (Porymap's Duplicate Map copies events, [../map-plan.md](../map-plan.md)). Section `MAPSEC_ROUTE_126` (shown ROUTE 16).

**Edges.**
- **South edge** meets Hemlock Reach's north inlet (the north shore, x about 20 to 24 of 44).
- **North edge** meets Mirror Isle's south jetty (the outdoor island, x about 14 to 16 of 30).
- No side exits. One islet with a **waterfall** on a tiny cliff is hinted but belongs to Hemlock's north inlet (see Hemlock card).

**Wild Pokémon (water, levels 44 to 50).**

| Surf slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 60% | LANTURN | 44 to 48 |
| 2 | 30% | QUAGSIRE | 44 to 48 |
| 3 | 5% | GOLDUCK | 45 to 48 |
| 4 | 4% | SEAKING | 45 to 48 |
| 5 | 1% | WHISCASH | 48 to 50 |

| Fishing | Slot | Rate | Species | Levels |
|---|---|---|---|---|
| Old Rod | 1 | 70% | MAGIKARP | 20 to 25 |
| Old Rod | 2 | 30% | CHINCHOU | 22 to 26 |
| Good Rod | 1 | 60% | SEAKING | 38 to 42 |
| Good Rod | 2 | 20% | WHISCASH | 38 to 42 |
| Good Rod | 3 | 20% | LANTURN | 38 to 42 |
| Super Rod | 1 | 40% | LANTURN | 44 to 48 |
| Super Rod | 2 | 40% | WHISCASH | 44 to 48 |
| Super Rod | 3 | 15% | GYARADOS | 44 to 48 |
| Super Rod | 4 | 4% | POLITOED | 44 to 48 |
| Super Rod | 5 | 1% | LUMINEON | 46 to 48 |

**Trainers (6).**

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Fisherman | Whiscash 46, Lanturn 46 | Near Hemlock |
| 2 | Swimmer (M) | Seadra 47, Golduck 47 | West islet |
| 3 | Swimmer (F) | Lanturn 47, Quagsire 47 | East islet |
| 4 | Tuber (M) | Poliwhirl 44, Seaking 45 | In an inner tube, easy |
| 5 | Triathlete | Whiscash 48, Politoed 48 | North |
| 6 | Fisherman | Seaking 47, Gyarados 48 | At the jetty, last; the toughest (48) |

All reuse vanilla ids; no IVs.

**NPCs (2).** A ferry-boat hand adrift on a reed islet (asks the way, points north to the Isle); a Goldsworth yacht aground in the shallows (ambient).

**Items (3 visible, 2 hidden).**

| Item | Where | Gate |
|---|---|---|
| ETHER | reed islet, west | Surf |
| MAX ELIXIR | north rock, past the swimmers | Surf |
| STAR PIECE | east islet | Surf |
| Hidden: HEART SCALE | shallow reef | Surf |
| Hidden: STARDUST | north shoal | Surf |

**Gate.** **Surf (badge 5).** Waterfall (badge 8) has no use on this road (it is at Mirror Isle and Hemlock's north inlet).

**Object budget:** 6 trainers + 2 NPCs + 3 items = 11 of 15.

**Goldsworth beat.** None.

**Flags (not claimed).** One-shot item flags, hidden items in the 0x264 block.

**Build effort: easy to medium.** Dimension change on a vanilla sea route and event cleanup.

**Open questions.** Does the author want a **sea-floor Dive route** (vanilla Route 105 has one) kept for badge 9? That would need underwater layouts, which is not planned.

---

## R17: Mirror Isle to Primrose Vale (water, no sketch number)

**Feel.** A reed-edged channel in the northern mere, leading east to a lakeshore and a sandy pier at Primrose Vale. Warmer and prettier than R16: lily pads, blossom drifting from the gardens, the smell of the city. Surf only.

**Shape.** 56 wide x 20 tall, east-west. Check: (56 + 15) x (20 + 14) = 2414, under 10240.

**Source.** Vanilla `Route107` (60 x 20, `LAYOUT_ROUTE107`), trimmed to 56 x 20. A flat sea strip with a few islets, which suits a short crossing. (Palladium has no lake route for this side.) Delete the copied Hoenn events after duplicating. Section `MAPSEC_ROUTE_127` (shown ROUTE 17).

**Edges.**
- **West edge** meets Mirror Isle's east ledge (the outdoor island, y about 12 of 26).
- **East edge** meets Primrose Vale's west shore pier (y about 30 of 63), so the offsets differ.
- No side exits. Two lily-pad islets with items.

**Wild Pokémon (water, levels 46 to 52).**

| Surf slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 60% | AZUMARILL | 46 to 50 |
| 2 | 30% | GOLDUCK | 47 to 51 |
| 3 | 5% | SLOWBRO | 48 to 50 |
| 4 | 4% | LUMINEON | 50 to 52 |
| 5 | 1% | MILOTIC | 50 to 52 |

| Fishing | Slot | Rate | Species | Levels |
|---|---|---|---|---|
| Old Rod | 1 | 70% | MAGIKARP | 20 to 25 |
| Old Rod | 2 | 30% | MARILL | 20 to 25 |
| Good Rod | 1 | 60% | SEAKING | 40 to 44 |
| Good Rod | 2 | 20% | AZUMARILL | 40 to 44 |
| Good Rod | 3 | 20% | LUMINEON | 40 to 44 |
| Super Rod | 1 | 40% | AZUMARILL | 48 to 52 |
| Super Rod | 2 | 40% | SEAKING | 48 to 52 |
| Super Rod | 3 | 15% | GYARADOS | 48 to 52 |
| Super Rod | 4 | 4% | LUMINEON | 50 to 52 |
| Super Rod | 5 | 1% | MILOTIC | 52 |

**Trainers (6).**

| # | Class | Team | Notes |
|---|---|---|---|
| 1 | Swimmer (F) | Azumarill 48, Luvdisc 48 | Near Mirror Isle |
| 2 | Swimmer (M) | Seaking 48, Golduck 49 | Middle |
| 3 | Fisherman | Qwilfish 47, Whiscash 49 | Reed islet |
| 4 | Tuber (F) | Slowbro 49, Azumarill 49 | In an inner tube |
| 5 | Triathlete | Lumineon 50, Starmie 50 | Near the pier |
| 6 | Beauty | Ribombee 50, Azumarill 51 | On the pier, last; the toughest (51) |

All reuse vanilla ids; no IVs.

**NPCs (2).** A boatman who rows between the isle and the pier at dawn and offers no ride (flavour); a petal-collector on the pier who says the blossom drifts out from the gardens every evening.

**Items (3 visible, 2 hidden).**

| Item | Where | Gate |
|---|---|---|
| ELIXIR | lily-pad islet, west | Surf |
| ETHER | lily-pad islet, east | Surf |
| NUGGET | rock in the middle channel | Surf |
| Hidden: PEARL | shallows near the pier | Surf |
| Hidden: STAR PIECE | reed bed, west | Surf |

**Gate.** **Surf (badge 5).**

**Object budget:** 6 trainers + 2 NPCs + 3 items = 11 of 15.

**Goldsworth beat.** None. (A surveyor's rowing boat could be seen on the pier, a Scheme 8 foreshadow like R15's, optional.)

**Flags (not claimed).** One-shot item flags, hidden items in the 0x264 block.

**Build effort: easy.** Short open-water strip.

**Open questions.** R17 has no number in the sketch (a blue line only). If the author wants it unnumbered, in-game it could be a named waterway rather than ROUTE 17.

---

## Open questions (east group)

1. **Is R15 truly land and only joined to Primrose Vale?** The sketch has no brown line between Hemlock Reach and Primrose Vale, so the whole north-east is a Surf pocket. Confirm that this is intended.
2. **R14 is one road, not two.** The README merges sketch numbers 14 and 17 (one arrow each way) into R14, and 18 and 19 into R16. Confirm the pairing.
3. **Palladium sea routes.** Only Route 40 is a sea route. I use it for R14 (rotated). R16 and R17 use vanilla `Route105` and `Route107`. If the author prefers a Palladium look for the mere, say which image to bend.
4. **Rod tiers.** Old and Good Rod tables use levels well below the surf level; where the player obtains each rod is not in the docs.
