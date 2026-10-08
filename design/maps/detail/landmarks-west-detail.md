# Detailed landmark design: Mothwood, Slagwell Mine, Hoarfell Ice cave

> **Mothwood moved (author, 2026-10-08):** the maze now **branches off R8** (Wendlebury to Briarwick), not off Briarwick by R9, which is dropped. R8 opens after badge 2, so Mothwood does too. Its entrance gate needs re-placing on R8 when the maze is designed. **Story event (author, 2026-10-08):** required; ranger closure; the Drowned Crown stealing a Time Gear-like piece of Dialga's seal from the shrine; Shedinja during the event and Celebi in the post-game (Shaymin goes to Primrose Vale). Details: [../landmarks-west.md](../landmarks-west.md) and [../../factions.md](../../factions.md).


Status: **PROPOSED** (written 2026-10-01). Nothing here is built. It adds floor-by-floor detail to the cards in [../landmarks-west.md](../landmarks-west.md); it does not change a species, level, item or flag from them. New minor names are marked PROPOSED. Roads that lead here: [routes-west-b.md](routes-west-b.md) (R7 to the mine), the R9 card in [../routes-west.md](../routes-west.md) (Mothwood). Towns: [smeltham.md](smeltham.md), [hoarfell.md](hoarfell.md), Briarwick in [../towns/briarwick.md](../towns/briarwick.md). Conventions: [../README.md](../README.md), [../interiors/README.md](../interiors/README.md).

All three are **optional** for the story, so they can be built last. Credit the Project Palladium team in `CREDITS.md` with the first map traced.

**Coordinates.** Every `(x, y)` is a tile on the Palladium render **as drawn** (0-based, x from the left). I measured the sizes from the pixels: gridded images are `(px - 1) / 17`. **One correction to the card:** `ilexforesttiled0ry.png` is 870 x 1074 px with a 1 px grid, so it is **51 x 63** tiles, not 54 x 67 (the card divided by 16). The Mt Mortar images are 39 x 35 (and 40 x 37), the Ice Path floors 43 x 33, 26 x 23, 24 x 20, 25 x 17, 26 x 24 and 16 x 22, as the card says. Positions are read by eye and can be **1 or 2 tiles off**: they say 'about here'. Where I give a puzzle grid, the grid is mine and was **checked by a throwaway solver** (it finds the solution and proves it is the shortest and the only shortest one), so those grids are exact; the author paints from them.

Map names, section ids and warps are PROPOSED. New interiors use the town's section where they hang off a town; the three landmarks need their own sections: `MAPSEC_MOTHWOOD`, `MAPSEC_SLAGWELL_MINE`, and the Ice cave either reuses `MAPSEC_HOARFELL` or gets `MAPSEC_HOARFELL_CAVE` (see Open questions; section ids are scarce, [../../engine-limits.md](../../engine-limits.md) limit 3).

---

# 1. MOTHWOOD (forest maze, off Briarwick)

## Role

An optional forest maze reached by R9, north-east of Briarwick. A Bug-type playground with a shrine in the middle of the loop, a Warden's lodge as the reward at the end, and a lot of items behind early HMs. A **return** destination: the first visit (Cut) opens the maze's shortcuts, Rock Smash and Strength open pockets, Surf opens one islet. It is a dead end.

## Source, size, tilesets

- Render: `ilexforesttiled0ry.png` (identical to `ilexforest5dh.png`), **51 x 63** tiles. Add 3 rows of ground along the bottom (**map 51 x 66**) so the south gate has an arrival tile (see Doors). Size check: (51 + 15) * (66 + 14) = 5,280 of 10,240.
- Primary `gTileset_General`, secondary `gTileset_Rustboro`. This is the pair vanilla Petalburg Woods uses (`PetalburgWoods_Layout`, 48 x 44: open it in Porymap and copy its tree wall and mushroom pieces). Cost: nothing new, no credit row beyond Palladium.
- **Optional mood upgrade: Shady Forest Secondary** (Team Aqua `Tilesets/The Great Tileset Exchange/Full Tilesets/Shady Forest Secondary/`). What it adds: dark pines, bare trees, stumps, cobbled paths, street lamps and two purple-roofed cottages (the Warden's lodge could be one). Needs Porytiles baking like Gen 4 Interior (triple-layer, `../../interiors.md`) and a `CREDITS.md` row (assembler Yumekua; creators Ekat99, Heartlessdragoon, Vurtax and more; Rahtak for the reformat; the folder's `credits.md` has the full list). I recommend skipping it for the first pass.
- Music: `MUS_PETALBURG_WOODS` (it exists in the build). Weather: none, or `WEATHER_SHADE` (overcast) for a darker canopy.

## What the render really is (a correction)

The card describes 'a tight lattice of single-tile corridors with a spiral'. The render is a **forest of tree walls two to six tiles thick with corridors and rooms between them**. I ran a path search on a tile map I made from the picture: from the south-west gate to the Lodge the shortest walk is **145 steps** (the card guessed about 120), and the render's own loop already is a spiral, so I keep it. The 'ledge line' the card mentions is the two short brown fences: at (36 to 38, 8) and (40 to 41, 8) in the north-east (one-way hops, down only), and a fenced garden at x 36 to 45, y 33 to 35 (the Glade). A third fence at (24, 23 to 25) is a one-tile ledge by the pond.

## Zones (render coordinates)

| Zone | Where | What |
|---|---|---|
| **Gate Yard** | x 3 to 8, y 55 to 64 | arrival from the south-west gate, 6 wide; a pair of flower tufts at (6 to 7, 55 to 57) |
| **West Corridor, south** | x 3 to 5, y 44 to 57 | 3 wide, runs north; a nook x 3 to 8, y 44 to 48 (the 'first fork' room) |
| **Fern Room** | x 6 to 17, y 41 to 43 | a 3-tall hall running east, flower tufts at (9 to 14, 41 to 42); **the Fern Room's west end is joined to the corridor by a gap at (6 to 8, 44)** |
| **Shrine Corridor** | x 15 to 17, y 38 to 48 | 3 wide, runs north-south from the Fern Room up to the Shrine Room |
| **Shrine Room** | x 6 to 17, y 35 to 37 (+ alcove x 12 to 17, y 33 to 34) | **the shrine statue is at (15, 35)**; the room is the loop's centre |
| **West Corridor, north** | x 3 to 5, y 29 to 37 and x 3 to 8, y 25 to 28 | runs north from the Shrine Room to the Hedge Gap |
| **Pond Meadow** | x 3 to 23, y 15 to 25 | an L-shaped pond at x 10 to 17, y 16 to 19 and x 10 to 14, y 20 to 22; shore row y 23 |
| **East Shore** | x 18 to 38, y 17 to 19 | open ground east of the pond |
| **North-East Channel** | x 36 to 47, y 9 to 14 and x 36 to 41, y 6 to 8 | a 12-wide clearing narrowing to a channel at x 36 to 41 |
| **North-East Clearing** | x 21 to 44, y 3 to 5 | a wide top lane with a tuft cluster at (39 to 41, 3 to 4) |
| **Lodge Yard** | x 3 to 26, y 9 to 14 | the lawn south of the Warden's Lodge |
| **Warden's Lodge** | x 3 to 11, y 2 to 8, door (7, 10) | the north-west gatehouse, see Doors |
| **Lower Run** | x 15 to 26, y 49 to 51 (+ x 24 to 26, y 36 to 48) | a loop off the Shrine Corridor, leads to the Glade |
| **The Glade** | x 24 to 47, y 33 to 51 | a big sealed meadow, the fenced garden at x 36 to 45, y 33 to 35 |
| **East Loop** | x 45 to 47, y 9 to 23 | a side corridor parallel to the east edge |
| **South-east Pocket / East Pocket** | see Pockets | |

## The intended walk (145 steps)

Waypoints are the corners of the shortest route (x, y). Distance between corners in tiles.

1. **Gate Yard to the corridor:** (7, 59) up to (7, 57), west to (5, 57) [4 steps]. Sign at (6, 54) 'THAT WAY. PROBABLY' pointing nowhere helpful. Item: POTION (5, 52) visible.
2. **West Corridor, south:** north (5, 57) to (5, 45) [12]. The 'first fork' at (5, 45): the nook to the east (x 6 to 8, y 44 to 48) is the way on. **Trainer 1** stands at (7, 46). Item: PARALYZE HEAL (8, 47) visible at the fork. REPEL hidden at (4, 50) near the first sign.
3. **Fern Room:** (6, 45) up to (6, 43), then east to (14, 43) [10]. **Trainer 2** at (11, 41). A child NPC hides in the room's tufts at (8, 42).
4. **Up the Shrine Corridor:** (14, 43), (15, 42), north to (15, 36) [8]. **Trainer 3** at (15, 39). Sign at (15, 41) 'TURN LEFT. OR RIGHT. YOU WILL FIGURE IT OUT'.
5. **The Shrine:** the statue at (15, 35); the player faces it from (15, 36). **Trainer 4** at (11, 36). The shrine keeper at (16, 36). **TM Giga Drain** is the shrine's reward (first interaction sets `FLAG_MOTHWOOD_SHRINE_VISITED`).
6. **West along the Shrine Room:** (14, 36), (14, 35), west to (5, 35) [10]. 
7. **Up the north corridor:** (5, 35) north to (5, 25) [10]. Sign at (5, 30) 'NORTH. OR SOUTH. WE LOST TRACK'.
8. **The Hedge Gap:** (6, 25), (6, 23), east along the shore row y 23 to (15, 23) [11]. Flower tufts at (12 to 14, 25 to 26).
9. **Round the pond:** (15, 20), east to (18, 20), north to (18, 17) [9]. **Trainer 5** at (20, 18). Hidden TINY MUSHROOM at (9, 19) (the pond's west bank, reached by a detour of 3 steps).
10. **The East Shore:** east along y 17 to (33, 17) [15]. Tufts at (30 to 33, 15 to 16). 
11. **Up the channel:** (33, 15), (36, 15), north to (36, 5) [13]. Sign at (36, 10).
12. **The North-East Clearing:** west along y 5 to (26, 5) [10]. HONEY hidden in the hollow trunk at (22, 6).
13. **Down and west to the lodge:** south (26, 5) to (26, 11) [6], west to (20, 11) [6], (20, 13), west along y 13 to (7, 13) [13] (**Trainer 6** at (10, 12)), then to the lodge mat (7, 11) [2].

The Lodge's door opens only after the shrine has been visited (see Doors), so the player must come back to the shrine, 35 steps in, first if they skipped it. Because the shrine is 35 steps from the gate the map is not 'a long walk to the shrine'. **If the author wants the shrine to be the finish, move the statue to the North-East Clearing at (36, 6) and put the TM there** (Open question 1); every other coordinate stays.

## Shortcuts (Cut, badge 1)

| Tree | At | Shortcut | Saves |
|---|---|---|---|
| CT1 | (4, 40), paint a 1-wide path x 4, y 38 to 43 through the tree band | Gate side of the West Corridor straight to the Shrine Room's west end | about 45 steps |
| CT2 | (25, 45) in the x 24 to 26 corridor | opens the Glade (see Pockets) | none, it is a pocket |
| CT3 | (46, 17) in the East Loop | joins the shore row at y 23 to the north-east, so the East Shore is skipped | about 40 steps |

## Pockets and HM spots

| Pocket | Where | Contents | Gate |
|---|---|---|---|
| The Glade | x 24 to 47, y 33 to 51, entered by CT2 | SILVER POWDER at (40, 34) inside the fenced garden; a tuft cluster at (24 to 29, 39 to 43) uses the maze's wild table | Cut |
| Alcove over the shrine | x 12 to 17, y 33 to 34 | REVIVE at (16, 33); a Strength boulder at (14, 34) is pushed west to open it | Strength (badge 4) |
| South-west nook | x 3 to 8, y 44 to 48 | ANTIDOTE at (3, 47) behind a boulder at (4, 47) pushed east into (5, 47) (the corridor): check it can be pushed | Strength |
| East Pocket | x 45 to 47, y 18 to 23 (the lower East Loop) | BIG MUSHROOM at (47, 21) behind a rock at (46, 20) | Rock Smash (badge 2) |
| Pond islet | a 1-tile islet at (13, 18) in the pond (PROPOSED: the render has no islet, paint it) | ELIXIR | Surf (badge 5) |
| Third boulder and second rock | boulder at (35, 7) and rock at (14, 45) | block two harmless side nooks with a view; no item (the card has three boulders and two rocks but only two items per kind, so these two are scenery that can be left out) | |

## Wild Pokémon and water

12-slot table from the card (SPINARAK 15 to 16, LEDYBA 15 to 16, PARAS 16, PINECO 16 to 17, VENIPEDE 16 to 17, SEWADDLE 16 to 17, BURMY 17, SHROOMISH 17, FOONGUS 17 to 18, JOLTIK 17 to 18, HERACROSS 18, PINSIR 18). **Grass is junction pockets, not corridors:** the render's flower tufts become tall grass at (4 to 8, 15 to 16), (12 to 14, 25 to 26), (30 to 33, 15 to 16), (39 to 41, 3 to 4), (24 to 29, 39 to 43), (9 to 14, 41 to 42), (6 to 7, 55 to 57). Pond fishing and Surf tables are the card's (Old Rod MAGIKARP 10, POLIWAG 10; Good Rod POLIWAG 13, MARILL 13, WOOPER 13; Super Rod MARILL 15, WOOPER 15, POLIWAG 16, PSYDUCK 16, CORPHISH 16; Surf WOOPER 14 to 18, MARILL 14 to 18, PSYDUCK 16, POLIWAG 16, CHINCHOU 18).

## Trainers (6, from the card; positions PROPOSED)

| # | Class and team (card) | Stands at | Faces | Sight |
|---|---|---|---|---|
| 1 | Bug Catcher (first fork): LEDYBA 15, SPINARAK 15 | (7, 46) | west | 3 |
| 2 | Camper (boulder pocket): SEWADDLE 15, PINECO 16 | (11, 41) | south | 2 |
| 3 | Picnicker (shrine path): COMBEE 15, BURMY 15, SHROOMISH 16 | (15, 39) | south | 3 |
| 4 | Collector (by the shrine): VOLBEAT 16, ILLUMISE 16 | (11, 36) | east | 3 |
| 5 | Bug Catcher (pond side): PARAS 15, VENIPEDE 16 | (20, 18) | west | 2 |
| 6 | Bug Catcher (north-west corner): KAKUNA 14, METAPOD 14 | (10, 12) | south | 2 |

Trainer 6 has the lowest levels but is met last: the card put him in the 'north-west corner', which on this render is the Lodge Yard at the end of the walk. **Open question 4** asks if the author wants him at the first fork instead and trainer 1 in the corner.

## NPCs (6, PROPOSED)

| NPC | Position | Notes |
|---|---|---|
| Guide with a hand-drawn map | (7, 61), in the Gate Yard | sells the first two turns for a joke price (dialogue only) |
| Lost visitor | (14, 43), in the Fern Room | 'in the maze since lunch', hint 'turn right at the second fence' |
| Child who hid an item | (8, 42) | refuses to say where (pure flavour) |
| Shrine keeper | (16, 36) | tells the shrine's story (unknown, Open question 2) |
| The Warden (PROPOSED name Alder) | inside the Lodge | explains the maze, gives the RARE CANDY after `FLAG_MOTHWOOD_SHRINE_VISITED` |
| Six junction signs | (6, 54), (15, 41), (5, 30), (20, 19), (36, 10), (22, 12) | each a different, useless direction ('THAT WAY. PROBABLY') |

Object count outdoors: 6 trainers + 4 people + 3 visible items (POTION, PARALYZE HEAL, the pair NET BALL x2 counts 2) = 15. The others are hidden (`bg_event`) or gifts.

## Items (from the card, with positions)

| Item | Where | Gate |
|---|---|---|
| POTION | (5, 52), entrance corridor | none |
| PARALYZE HEAL | (8, 47), first fork | none |
| NET BALL x2 | (3, 13) and (3, 14), the Lodge Yard's west pocket | none |
| HONEY | (22, 6), hidden, a hollow tree | none |
| TINY MUSHROOM | (9, 19), hidden, pond side | none |
| REPEL | (4, 50), hidden near the first sign | none |
| ANTIDOTE | (3, 47) | Strength (badge 4) |
| SILVER POWDER | (40, 34) in the Glade | Cut (badge 1) |
| BIG MUSHROOM | (47, 21) | Rock Smash (badge 2) |
| REVIVE | (16, 33) | Strength (badge 4) |
| ELIXIR | the islet (13, 18) | Surf (badge 5) |
| TM Giga Drain | the shrine (15, 35) | none, reach the shrine |
| RARE CANDY | from the Warden, in the Lodge | after the shrine |

**Note:** Briarwick's House B (Tansy, [../../dialogue/briarwick.inc](../../dialogue/briarwick.inc)) also hands over a SILVER POWDER. Two sources of the same item is fine, but say so if you want the Mothwood one swapped for another item.

## Doors, interiors and warps

| Map | Tile | Destination |
|---|---|---|
| `Mothwood` | (13, 61), the south-west gate (door on the south face; the render shows the entrance on the west, so rotate it, see Open question 3) | `Mothwood_Gate` warp 2 (the right door pair) |
| `Mothwood` | (7, 10), the Warden's Lodge | a script door: a `coord_event` trigger on (7, 11) that warps to `Mothwood_WardensLodge` only when `FLAG_MOTHWOOD_SHRINE_VISITED` is set, otherwise a sign says 'CLOSED. COME BACK WITH SOMETHING TO SHOW' |
| `Mothwood_Gate` | (1, 5) and (2, 5), the left door pair | R9's north gatehouse (the road side, defined in the R9 card) |
| `Mothwood_Gate` | (12, 5) and (13, 5), the right pair | `Mothwood` warp 0, lands at (13, 62) |
| `Mothwood_WardensLodge` | (2, 7), exit mat | `Mothwood` warp 1, lands at (7, 11) |

- **`Mothwood_Gate`:** the one gate interior shared with R9, as the R9 card asks. 15 x 6, copy of `LAYOUT_ROUTE110_SEASIDE_CYCLING_ROAD_ENTRANCE` (vanilla, secondary `gTileset_Shop`, has the two bottom door pairs already). The gatekeeper stands at (7, 2) facing south: 'Mothwood has no map. Bring snacks.' Optional skin: Team Aqua **Gatehouse Secondary** (see [gloomsby.md](gloomsby.md) for what it adds and the credit rows).
- **`Mothwood_WardensLodge`** (11 x 8): tileset `gTileset_Building` plus **Legend of Zelda House Secondary** (Team Aqua `.../Legend of Zelda House Secondary/`): a timber-and-stone hut with a hearth, two beds, a tall pot row and a plank table (see its `example.png`). What it adds over the house style: rustic wood and stone, right for a warden. Needs Porytiles baking, and a `CREDITS.md` row (Buildings: Hek-el-grande; assembler Yumekua; creators Ekat99, Heartlessdragoon, Vurtax; Rahtak for the reformat). The default if the author declines is the Gen 4 Interior kit (the neighbour's house footprint). Plan (11 x 8): hearth at the top right (8, 1) to (9, 2), two beds at (1, 1) and (3, 1), the plank table at (5, 4) to (6, 5), shelf at (1, 4) with pots below it at (1, 5) and (1, 6), exit mat (2, 7). The Warden stands at (5, 3) facing south. A 'mothwood map' on the wall (`bg_event` at (6, 1)) joking that it is blank.

## Visual identity

Greens only, dark in the middle, golden light on the Lodge Yard. Silhouettes: the grey gatehouse roof at the top left and the bottom left, the shrine statue standing alone in the Shrine Room, the pond's L-shape. Sound: `MUS_PETALBURG_WOODS`, with a rustle if the author adds one.

## Flags (not claimed)

`FLAG_MOTHWOOD_SHRINE_VISITED`, `FLAG_MOTHWOOD_GIFT_RECEIVED`, `FLAG_MOTHWOOD_ITEM_*` per ball or hidden item, and the reused trainer flags. No story flag.

## Build checklist (Mothwood)

1. Add map `Mothwood` (51 x 66), tilesets General + Rustboro, music, `MAPSEC_MOTHWOOD`. 2. Paint the tree frame (3 deep) and the thick tree walls from the render; open the corridors. 3. Paint the pond, the Glade fence, the NE fences. 4. Paint the three Cut trees, two rocks, three boulders. 5. Add the two gate buildings; add 3 rows of ground south. 6. Add grass on the tuft clusters. 7. Add `Mothwood_Gate` (copy of the cycling-road entrance) and `Mothwood_WardensLodge`. 8. Place trainers, NPCs, items, signs. 9. Add the warps and the script door. 10. Connect R9 once R9 exists. 11. Credits (Palladium; Zelda House or Shady Forest if used). 12. `make -j4`.

## Build effort

**Medium to hard** (card agrees). The tree walls are the work: 51 x 63 tiles, 80 percent trees. Budget a full session. The two interiors are tiny.

## Open questions (Mothwood)

1. **Where is the shrine?** In the render it is on the route 35 steps in. Move it to (36, 6) to make it the finish?
2. **What does the shrine enshrine?** Nothing is assumed. A plain shrine (the card's 'a Pokémon that watches over the wood', no encounter), a one-off wild Pokémon, or a post-game mythical?
3. **Gate door side.** The render's south gate has its entrance on the west side. Emerald doors face south. I rotate it and add 3 rows of ground. Fine?
4. **Trainer order.** Keep the card's 'north-west corner' (met last on this render) or swap with the first fork?
5. **Shady Forest** upgrade or the vanilla Petalburg Woods look?

---

# 2. SLAGWELL MINE (cave off R7, east of Smeltham)

## Role

An optional **working mine gone quiet**: ore carts, rails, ladders, a flooded lower chamber. A **revisit** cave: items need Rock Smash, Strength, Surf and finally Waterfall (badge 8), so the player cannot finish it on the first visit, deliberately. It ties Smeltham to its mountain ('the foundry takes its ore from here'). No scheme beat, no Troglodyte.

## Source, size, tilesets (answers the card's open question 1)

Four Mt Mortar images, all **the same big cavern**: a top pool, a waterfall in the middle, a lower pool with a platform, plateaus either side. I compared them tile by tile: `mtortar3xm.png` (grey-green plateaus, ring markers: the **1F**), `mtortar6bo.png` and `mtortar6bl.png` (the same cave with pink rock and ladder icons: the **Upper level**), `mtmortar4jh.png` (40 x 37: the same shape with the doors at the sides: the **Waterfall Chamber**). So the card's three-map plan is right. Sizes: 1F 39 x 35, Upper 39 x 35, Chamber **trimmed to about 24 x 18** (PROPOSED: only the top pool and the fall are needed, see below).

| Map | Name | Size | Source | Size check |
|---|---|---|---|---|
| 1F | `SlagwellMine_1F` | 39 x 35 | `mtortar3xm.png` | (39+15)*(35+14) = 2,646 |
| Upper | `SlagwellMine_Upper` | 39 x 35 | `mtortar6bl.png`, `mtortar6bo.png` | 2,646 |
| Chamber | `SlagwellMine_FallChamber` | 24 x 18 | the top half of `mtmortar4jh.png`, trimmed | (24+15)*(18+14) = 1,248 |

**Tilesets, Plan A (build this):** primary `gTileset_General`, secondary `gTileset_MeteorFalls`. Meteor Falls has the pool, the waterfall, the ladder, the rock stairs and the ledge walls (it is the Emerald waterfall cave; `MeteorFalls_1F_1R_Layout` is 30 x 42, open it in Porymap and copy pieces). No credit row beyond Palladium. Granite Cave (`gTileset_Cave`) is the fallback for flat caves.
**Plan B (a mine look, later):** Team Aqua **Caves Alt Primary + Caves Alt Secondary** (`.../Caves Alt Primary/` and `.../Caves Alt Secondary/`). What it adds: grey cave stone with a **mine cart track layout, ore crates, drilling machines, a plank bridge over water and a notice board** (see its `example.png`). That is the mine the card describes. What it costs: it is a **matched pair** (a new primary and a new secondary, 'meant to be used alongside'), both triple-layer, so two Porytiles bakes, and it asks for expanded metatiles. Credit row for both (creators Amethyst, Crim, Smeargletail, Pokémon Essentials, princess-phoenix, and Pokémon Reborn's Victory Road tiles; Rahtak for the reformat; the folder's `credits.md`). I recommend Plan A first and Plan B as a later visual pass for the 1F and Upper maps only.

**Darkness.** The card says dark by header, not Flash-locked. The player has Flash from Gloomsby by now. **PROPOSED:** `requires_flash` **false** on `SlagwellMine_1F` (the mine has lamps, so the first impression is the big blue pool), **true** on the Upper and the Chamber. Without Flash the Upper stays walkable but dim. Music (PROPOSED): `MUS_M_DUNGON`, the same on all three floors.

## `SlagwellMine_1F` (39 x 35)

### Zones (render coordinates)

| Zone | Where | Notes |
|---|---|---|
| **Island Landing** | x 13 to 20, y 26 to 31 | the arrival: a mat at (16 to 18, 31) with two wooden steps at (15, 29) and (18, 29); the island platform above x 14 to 19, y 26 to 28 holds **ladder L3 at (17, 28)** |
| **Bottom Strip** | x 0 to 38, y 31 to 34 | a tan walkway along the bottom edge joining everything south |
| **South-west Pocket** | x 2 to 6, y 26 to 31 | boulders (2 to 3, 26 to 29) and (4, 29); steps (5, 25) lead up to the West Terrace; a small dark opening at (8, 29) with a stream |
| **West Terrace** | x 4 to 9, y 21 to 24 | ring marker (7, 22) |
| **East Terrace** | x 27 to 36, y 21 to 32 | boulder field, steps (32, 25), ring marker (35, 24), a trickle at (30, 19 to 22) |
| **Cliff band** | y 18 to 21, x 0 to 38 | splits the cave in two; the only gaps are two 1-tile service doors at **(12, 20)** and **(26, 20)** and the waterfall |
| **West Plateau** | x 5 to 14, y 11 to 16 | ladder **L1 at (7, 13)**, an item at (10, 14) |
| **Far West Walk** | x 0 to 3, y 4 to 17 | a tan corridor along the left edge; a platform at x 3 to 7, y 6 to 8 |
| **East Plateau** | x 24 to 33, y 6 to 16 | ladder **L2 at (29, 8)**, a ring at (30, 14), an item at (32, 12) |
| **North-east Flat** | x 31 to 38, y 4 to 14 | open tan floor |
| **Lower Pool** | x 10 to 25, y 23 to 31 | around the Island Landing; surfable (badge 5) |
| **Waterfall** | x 15 to 22, y 17 to 23 | climbed with Waterfall (badge 8) |
| **Mid channel / Top Pool** | x 14 to 22, y 9 to 17 / x 8 to 24, y 6 to 10 | the north shore ledge x 16 to 18, y 6 to 7 with the **Chamber door at (16, 5)** |

### Paths and flow

- **First visit (no HMs):** arrive on the Island Landing (17, 30) → Bottom Strip → east to the **East Terrace** (boulder field, a Black Belt) and west to the **West Terrace** (Hiker) → the two service doors (12, 20) and (26, 20) lead north to the plateaus → ladders L1 (7, 13) and L2 (29, 8) go **up** to the Upper level. L3 (17, 28) on the island also goes up (to the Upper island and the rest cot).
- **Rock Smash (badge 2):** the rubble at (3, 31) opens the **South-west Pocket** (REVIVE, a miner's stash); the rock at (36, 20) opens the right ledge pocket (IRON).
- **Strength (badge 4):** boulders on the East Terrace are pushed to open the HARD STONE nook at (31, 30).
- **Surf (badge 5):** the Lower Pool has a 2 x 2 islet at (11, 27) to (12, 28) with the RARE CANDY (PROPOSED, paint it).
- **Waterfall (badge 8):** from the Lower Pool surf north at x 18 to 20 and ride the fall up to the Top Pool, land on the north shore ledge (16 to 18, 6 to 7) and walk north into the **Chamber door (16, 5)**.

### Wild Pokémon

Cave floor and the cave's grass-equivalent: the card's table (levels 31 to 36): ZUBAT 31 to 33 (20), BOLDORE 32 to 33 (20), GEODUDE 31 to 32 (10), WOOBAT 31 to 33 (10), MAGNEMITE 32 to 33 (10), ONIX 32 to 33 (10), GOLBAT 34 (5), DWEBBLE 34 (5), SKORUPI 34 (4), GRAVELER 34 to 35 (4), SHUCKLE 35 (1), LARVITAR 35 (1). Encounter tiles: **the whole floor** of the Bottom Strip, both Terraces and the Plateaus (cave floors are encounter tiles in vanilla caves; leave the Island Landing and the Far West Walk clear so the arrival and the corridor are calm). Surf, fishing, Rock Smash tables are the card's (Surf WOOPER 30 to 34, BARBOACH 30 to 34, PSYDUCK 32 to 36, QUAGSIRE 36, CHINCHOU 34 to 36; Rock Smash DWEBBLE 30 to 34, GEODUDE 30 to 34, BOLDORE 33, NOSEPASS 33, SHUCKLE 33; Old Rod MAGIKARP 15, BARBOACH 15; Good Rod BARBOACH 25, WOOPER 25, GOLDEEN 25; Super Rod WOOPER 30, BARBOACH 30, GOLDEEN 30, PSYDUCK 32, WHISCASH 34).

### Trainers on the 1F (3 of the card's 6; positions PROPOSED)

| # | Class and team (card) | Stands at | Faces | Sight | Notes |
|---|---|---|---|---|---|
| 1 | Hiker (1F entrance): GEODUDE 29, ONIX 30 | (17, 27) | south | 3 | on the island platform, sees the arrival (17, 28 to 30) |
| 2 | Hiker (1F left ledge): ROGGENROLA 30, BOLDORE 31 | (7, 23) | east | 4 | on the West Terrace, guards the steps to the pocket |
| 3 | Black Belt (1F right ledge): MACHOP 30, TIMBURR 31 | (30, 24) | west | 4 | on the East Terrace, among the boulders |

### NPCs on the 1F (3)

| NPC | At | Notes |
|---|---|---|
| Worker 'on lunch' | (8, 14) beside ladder L1 | continues Smeltham's joke: 'back at one' |
| Hiker who lost his torch | (2, 10) on the Far West Walk | hint: Flash |
| Rest-cot attendant | (6, 30) in the South-west Pocket | gives one free POTION, once (needs the Rock Smash opening, so it is a revisit gift) |

### Items on the 1F

| Item | Where | Kind | Gate |
|---|---|---|---|
| POTION | (14, 28), the island | visible | none |
| ESCAPE ROPE | (36, 30), lower right | visible | none |
| TM Rock Tomb | (8, 12), beside ladder L1 | visible | none (the Smeltham clerk also gives one) |
| HARD STONE | (31, 30), the East Terrace nook | hidden | none |
| IRON | (36, 20), right ledge pocket | visible | Rock Smash |
| REVIVE | (3, 28), behind the rubble | visible | Rock Smash |
| RARE CANDY | the islet (11, 27) | visible | Surf (badge 5) |

(The item icon at (10, 14) and (32, 12) in the render are the Upper's twins; on the 1F leave them empty or put the TM Rock Tomb and a Strength-only pocket there.)

## `SlagwellMine_Upper` (39 x 35)

Source: `mtortar6bl.png` and `mtortar6bo.png` (same footprint as the 1F, pink rock). It is the **ledge level**: the waterfall and the pools are the same shape (water, surfable), but the walkable ground is the upper plateaus.

| Zone | Where | Notes |
|---|---|---|
| **West Plateau** | x 3 to 14, y 11 to 18 | a big tan floor; ladder **L1 at (7, 13)** (down to the 1F West Plateau); item (7, 14) REPEL; **boulders at (4, 22), (5, 22), (4, 23)** in the south-west with the CARBOS at (3, 22) behind them (Strength) |
| **East Plateau** | x 24 to 34, y 6 to 19 | a **rock field** x 27 to 30, y 7 to 14 with the ETHER at (28, 11) in the middle; ladder **L2 at (33, 12)** |
| **Island** | x 13 to 20, y 26 to 30 | ladder **L3 at (17, 28)**; the rest cot with an NPC at (16, 26) who gives one POTION; surrounded by the lower pool |
| **Cliff band doors** | (12, 20) and (26, 20) | same service doors as the 1F (they link the plateaus to the south terraces) |

- **Trainers (3 of the card's 6):** Collector (upper left plateau): MAGNEMITE 31, KLINK 31 at (9, 15) facing east, sight 4. Guitarist (upper right plateau): MAGNEMITE 32, KLINK 32 at (31, 10) facing west, sight 4. **The foreman** (Hiker): ONIX 32, GRAVELER 33, NOSEPASS 33 at (18, 28), next to ladder L3, facing south, sight 3 (the mine's boss, the one trainer on the island).
- **NPC:** the old miner at (6, 16) on the West Plateau, talks about 'the day the lights went out'.
- **Items on the Upper:** REPEL (7, 14), ETHER (28, 11), CARBOS (3, 22) (Strength). The Upper has no other items.
- **Wild:** the same cave table as the 1F (the whole floor is encounter ground except the ladder tiles and the island).
- **Warps:** L1 (7, 13) to `SlagwellMine_1F` (7, 13) landing (7, 14); L2 (33, 12) to 1F (29, 8) landing (29, 9); L3 (17, 28) to 1F (17, 28) landing (17, 29).

## `SlagwellMine_FallChamber` (24 x 18, PROPOSED)

The room behind the top door, reached only by **Surf then Waterfall**. A bowl of dark rock with a small pool at the front and a waterfall dropping from the north wall. A tiny shrine-like alcove behind the fall.

- **Layout (trim of `mtmortar4jh.png`, its top half):** pool x 4 to 19, y 6 to 14; the waterfall at x 10 to 13, y 2 to 6 dropping into the pool; ledges east (x 19 to 22, y 4 to 8) and west (x 2 to 5, y 4 to 8); the arrival mat at (11, 16) (the bottom) from the 1F door; the alcove behind the fall at (11, 2).
- **Items:** MAX ETHER on the east ledge (21, 6), NUGGET hidden on the west ledge (3, 6), **BIG PEARL hidden at the alcove behind the fall (11, 2)** (reached by Waterfall again: a second climb inside the chamber). All need badge 8.
- **Trainers:** none. **NPC:** none. **Wild:** the Surf table of the 1F; no grass.
- **Warps:** the mat (11, 16) goes to `SlagwellMine_1F` (17, 6); the 1F door (16, 5) goes to `SlagwellMine_FallChamber` (11, 16).

## Warp table (Slagwell)

| Map | Tile | Destination |
|---|---|---|
| `Route7` | (16, 5), the mine door | `SlagwellMine_1F` warp 0 |
| `SlagwellMine_1F` | (17, 31), the entrance mat | `Route7` warp 1, lands at (16, 6) |
| `SlagwellMine_1F` | L1 (7, 13) / L2 (29, 8) / L3 (17, 28) | `SlagwellMine_Upper` L1 / L2 / L3 |
| `SlagwellMine_1F` | (16, 5), the Chamber door | `SlagwellMine_FallChamber` warp 0 |
| `SlagwellMine_FallChamber` | (11, 16) | `SlagwellMine_1F` warp 4, lands at (17, 6) |

## Flags (not claimed)

`FLAG_SLAGWELL_VISITED` (set on entry; the Smeltham clerk's hint), `FLAG_SLAGWELL_ITEM_*` per item, reused trainer flags. No story flag.

## Build checklist (Slagwell)

1. Add `SlagwellMine_1F`, tilesets General + MeteorFalls, `requires_flash` false, `MAPSEC_SLAGWELL_MINE`. 2. Trace `mtortar3xm.png`: rock frame, pools, waterfall, plateaus. 3. Cut the two service doors in the cliff band. 4. Add `SlagwellMine_Upper` (duplicate the 1F, repaint the floors, `requires_flash` true). 5. Add `SlagwellMine_FallChamber`. 6. Paint rubble, boulders, rocks, the islet. 7. Ladders and warps. 8. Trainers, NPCs, items. 9. Connect R7's mine door. 10. Credits. 11. `make -j4`.

## Build effort

**Medium** (the card agrees). Three maps, two of them copies; the pools and the fall are in Meteor Falls. A day with testing.

## Open questions (Slagwell)

1. Plan A (Meteor Falls) or Plan B (Caves Alt, two new tilesets) for the look?
2. Are the two sealed bottom exits really dead-end pockets? I made them in-map alcoves behind Rock Smash rubble (one pocket at the South-west) and left the south-east alone, because the render's two 'exits' (3, 32) and (34, 32) are tiny mats on the bottom strip, not doors.
3. Is the Fall Chamber (a small separate room) right, or should Waterfall just lead to the Top Pool inside the 1F?
4. Anything unique in the Chamber? Items only, as the card says.

---

# 3. HOARFELL ICE CAVE (optional, inside Hoarfell)

## Role

A frozen cave behind Hoarfell for slide puzzles and one good TM. Not required. It is a **loop**: the north-centre door above the lake is the main entrance and the north-east shelf door is the far exit, so the player can come back to town without recrossing the ice.

## Source, size, floors

Palladium **Ice Path**, five floors plus an annex. I read all six images. Floors in Veldris (the card's four-map plan, with B4F renamed B2F because B2F and B3F are cut):

| Map | Name | Size | Source | Notes | Size check |
|---|---|---|---|---|---|
| 1F | `HoarfellIceCave_1F` | 43 x 33 | `icepathf10va.png` | two exits, one big ice field, one descent | (43+15)*(33+14) = 2,726 |
| B1F | `HoarfellIceCave_B1F` | 26 x 23 | `icepathbasement112dw.png` | pillar maze with four holes | 1,517 |
| B2F | `HoarfellIceCave_B2F` | 26 x 24 (render B4F) | `icepathbasement216nd.png` | the big slide hall with an island | 1,558 |
| Annex | `HoarfellIceCave_Annex` | 16 x 22 | `icepathbasement229gg.png` | a small slide room, TM at the top | 1,116 |

(The render's B2F and B3F, `icepathbasement125fx.png` and `icepathbasement136kk.png`, are connectors; they are skipped as the card proposes. If the author wants a longer cave later, they slot in between B1F and B2F: B2F-old has two ladders and a 7 x 6 slide patch, B3F-old has two ladders and a green 2 x 2 patch.)

**Tilesets, Plan A (build this):** primary `gTileset_General`, secondary `gTileset_Cave` (vanilla). It is the pair `ShoalCave_LowTideIceRoom_Layout` (20 x 30) uses and it **contains the slippery ice tile**: I checked `data/tilesets/secondary/cave/metatile_attributes.bin`: metatile index 397 (id 909 in map data) has behaviour `MB_ICE`, and vanilla's ice room proves it slides. So it is Emerald-native, nothing to import, no credit row beyond Palladium. Open `ShoalCave_LowTideIceRoom` in Porymap, copy its ice blocks and its rock walls.
**Plan B (a prettier ice cave):** the FRLG Icefall Cave pair, `gTileset_General_Frlg` + `gTileset_SeafoamIslands`. The tree has them (they are the tilesets of `FourIsland_IcefallCave_*` and `SeafoamIslands_*`; `data/tilesets/secondary/seafoam_islands_frlg/` has 10 `MB_ICE` metatiles) and they give blue ice walls and snow patches. **Untested:** the FRLG maps are not built into this ROM, so I have not seen an Emerald-region map use an FRLG primary. Try it in Porymap on a scratch map first; if it renders cleanly it is the better look. Do not hand-edit tilesets (CLAUDE.md rule 2).

**What needs painting:** every ice tile is the one `MB_ICE` metatile; the 'snow patch' (a stop tile) is any normal floor metatile; boulders are the cave's rock blocks (collision 1). The author paints from the grids below.

## Floor 1: `HoarfellIceCave_1F` (43 x 33)

Zones from the render: a frame of rock 2 to 3 tiles thick all round; the **big ice field** at x 3 to 17, y 3 to 14 (upper left); a **central stone floor** x 18 to 31, y 3 to 22 with ledges and steps; a second, small **ice room** x 24 to 32, y 7 to 10; a **lower shelf** x 5 to 14, y 16 to 20 with a row of boulders at y 16 to 17; an **ice tongue** (a 2-wide strip of ice) at x 16 to 17, y 17 to 24 and across y 21 to 22 to x 21; a **right-bottom ice patch** x 34 to 39, y 19 to 22; and an eastern shelf x 33 to 39, y 4 to 14 with two items. Exits: the **left mat at (6, 21)** and the **right mat at (38, 29)**. Stone steps (cave ledges) at (21, 8), (29, 14), (35, 6), (37, 12) and (26, 22).

- **West door (the main entrance):** the town's north-centre cave door warps to `HoarfellIceCave_1F` at (6, 21). The player lands on the lower shelf, walks north-east along the shelf and the stone floor.
- **East door (the loop exit):** (38, 29) leads back to the town's north-east shelf door. It is reached along the stone floor, no ice crossing needed (the ice patches are optional).
- **Descent to B1F:** a cave ladder-down at **(21, 8)** (the render's stone steps at the top of the central floor), on foot.
- **The ice tongue** (x 16 to 17, y 17 to 24) crosses the way from the shelf to the stone floor. It is a **2-wide crossing**: step on it and you slide to the far side; it is the player's first taste of ice, safe because it has no hole.
- **Field A (the NUGGET puzzle), x 3 to 17, y 3 to 14:** the player enters at the bottom-right corner **(17, 14)**, a snow patch reached from the stone floor through a **Rock Smash rock at (18, 14)** (this is the card's Rock Smash gate). The NUGGET is a hidden item on the snow patch in the top-left corner **(3, 3)**. The grid (x 3 to 17 across, y 3 to 14 down; `#` boulder, `.` ice, `s` snow patch (a stop), `S` the entry, `G` the goal patch):

```
     x 3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
y  3   G  .  .  .  #  .  .  .  .  .  .  .  .  .  .
y  4   .  .  .  .  .  #  .  .  .  .  #  .  .  .  .
y  5   #  .  .  .  .  .  .  .  .  .  .  .  .  .  #
y  6   .  s  .  .  .  .  .  .  .  .  #  s  .  .  .
y  7   .  .  .  .  .  .  .  .  .  #  .  .  .  .  .
y  8   .  .  .  .  .  .  .  #  .  .  .  .  .  .  .
y  9   .  .  #  .  .  .  .  .  .  .  .  .  s  .  #
y 10   .  .  .  #  .  .  .  .  .  .  .  .  .  .  .
y 11   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
y 12   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
y 13   .  .  .  .  .  .  .  .  .  .  #  .  .  .  .
y 14   .  .  .  .  .  .  .  .  #  .  .  .  .  .  S
```

  **Solution (5 slides, the only shortest one):** from S **north** (the boulder at (17, 9) stops you at (17, 10)), **west** (the boulder at (6, 10) stops you at (7, 10)), **north** (up x 7, the boulder at (7, 3) stops you at (7, 4)), **west** (slides to (3, 4)), **north** to **G (3, 3)**. The solver found 40 stop tiles, so there are plenty of dead ends; none traps the player (every stop has a slide back to a patch or the entry).
- **Second ice room (x 24 to 32, y 7 to 10):** small, 9 x 4, no puzzle, one visible **ICE HEAL** at (32, 9) (the card's 1F visible item), a decoration for the loop. Optional.
- **Right-bottom ice patch (x 34 to 39, y 19 to 22):** a 6 x 4 decoration slide beside the east door's path; a hiker stands at its edge.

### Trainer on the 1F (card): Hiker: SWINUB 31, SNORUNT 32

At **(22, 14)** on the stone floor, facing west, sight 4, so he spots the player coming from the west door. (Level 31 to 32, the ice cave's lowest.)

### Items on the 1F

| Item | Where | Kind | Gate |
|---|---|---|---|
| ICE HEAL | (32, 9), the small ice room | visible | none |
| NUGGET | (3, 3), Field A | hidden | Rock Smash (badge 2): the rock at (18, 14) blocks the way in |
| NEVER-MELT ICE | on the town's north-east shelf, **not in the cave** | | see [hoarfell.md](hoarfell.md) |

### Wild Pokémon (the whole cave, from the card, levels 33 to 37)

SWINUB 33 to 34 (20), SNORUNT 33 to 34 (20), WOOBAT 33 to 34 (10), CUBCHOO 34 to 35 (10), VANILLITE 34 to 35 (10), BERGMITE 34 to 35 (10), SNEASEL 35 to 36 (5), SMOOCHUM 34 to 35 (5), DELIBIRD 35 to 36 (4), PILOSWINE 36 (4), CRYOGONAL 37 (1), GLALIE 37 (1). Encounter tiles: the **stone floor** (the non-ice floor) on every floor, not the ice. No water, so no Surf or fishing. The B1F Rock Smash rock set: GEODUDE 33 (60), SWINUB 33 (30), SMOOCHUM 34 (5), SNEASEL 35 (4), BERGMITE 35 (1).

## Floor B1F: `HoarfellIceCave_B1F` (26 x 23)

A frozen field of **ice pillars** (boulders) on **non-slippery** stone floor: a walking maze, not a slide room. The render: a frame of rock; an arch at the top centre **(13, 2)** (the stairs up); a bright pillar maze with clusters at (11 to 12, 5 to 8), (6 to 7, 11 to 12), (16 to 18, 10 to 14), (12 to 14, 14 to 15) and so on; **four holes** (black circles) at **(14, 5), (7, 10), (8, 15), (15, 16)**; a **ladder at (6, 17)**; an item at **(20, 6)**.

- **Warps:** the arch at (13, 2) is the stairs up: it warps back to 1F (21, 8), landing (21, 9). The ladder (6, 17) goes down to B2F's top-right platform (20, 4). **The four holes drop** the player to B2F's top-right platform as well (a fall: the player lands at (20, 4), the same spot, costing time).
- **Items:** PROTEIN visible at (4, 16) (bottom-left), **TM Hail at (20, 6)** (the ledge behind the pillars, top right), **RARE CANDY** hidden at (13, 17) beside the (15, 16) hole (the 'hole-side ledge'), a **Rock Smash rock** at (10, 8) hiding nothing but an encounter.
- **Trainer (card):** Lass: VANILLITE 32, CUBCHOO 33 at **(10, 13)**, facing east, sight 4.
- **Wild:** the stone floor uses the cave table above.

## Floor B2F: `HoarfellIceCave_B2F` (26 x 24, the big slide hall)

The render's biggest ice floor: ice at x 3 to 22, y 3 to 20, a stone ring round it, **four corner platforms** and a **central island** at x 10 to 12, y 10 to 14. The up-ladder arrives on the **top-right platform at (20, 3)**.

The grid below covers the ice field (x 3 to 22 across, y 3 to 20 down). `s` is a snow patch or platform (a stop, walkable), `#` is a boulder, `.` is ice, `S` the arrival tile. The four platforms are: top-left x 3 to 5, y 3 to 5; top-right x 19 to 22, y 3 to 5 (the ladder is the `S` tile (20, 3)); bottom-left x 3 to 6, y 17 to 20; bottom-right x 19 to 22, y 17 to 20; the island is x 10 to 12, y 10 to 14.

```
     x 3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22
y  3   s  s  s  .  .  .  .  .  .  .  .  .  #  .  .  .  s  S  s  s
y  4   s  s  s  .  .  .  .  .  .  .  .  .  .  .  .  .  s  s  s  s
y  5   s  s  s  .  .  .  .  .  .  .  .  .  .  .  #  .  s  s  s  s
y  6   .  .  .  .  .  .  .  .  #  .  .  .  .  .  .  .  .  .  .  .
y  7   .  .  .  .  .  .  .  .  .  .  .  .  .  #  .  .  .  .  .  .
y  8   .  .  .  .  .  .  .  #  .  .  .  .  .  .  .  .  #  .  .  .
y  9   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  #  .  .  .
y 10   .  #  .  .  .  .  .  s  s  s  .  .  .  .  .  .  .  .  .  .
y 11   .  .  .  .  .  .  .  s  s  s  .  .  .  .  .  .  .  .  .  .
y 12   .  #  #  .  .  .  .  s  s  s  .  .  .  .  .  .  .  .  .  .
y 13   .  .  .  .  .  .  .  s  s  s  .  .  .  .  .  .  .  .  .  .
y 14   .  .  .  .  .  .  .  s  s  s  .  .  .  .  .  .  .  .  .  .
y 15   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
y 16   .  .  .  .  .  .  .  .  .  .  .  .  .  .  #  .  .  .  .  .
y 17   s  s  s  s  .  .  .  .  .  .  .  .  .  .  .  .  s  s  s  s
y 18   s  s  s  s  .  .  .  .  .  .  .  .  .  .  .  .  s  s  s  s
y 19   s  s  s  s  .  .  .  .  .  .  .  .  .  #  .  .  s  s  s  s
y 20   s  s  s  s  .  .  #  .  .  .  .  .  .  .  .  .  s  s  s  s
```

- **The island (REVIVE), the verified solution (4 slides):** from the arrival `S` (20, 3): **west** (one step along the platform to (19, 3)), **west** (a slide: it stops at (16, 3) against the boulder at (15, 3)), **south** (down x 16, it stops at (16, 6) against the boulder at (16, 7)), **west** (along y 6, it stops at (12, 6) against the boulder at (11, 6)), **south** (down x 12, it stops on the island's top-right corner **(12, 10)**). It is the only shortest route (119 stop tiles exist, so there are many wrong turns).
- **The REVIVE** is at the island's centre **(11, 12)**.
- **To the bottom-right platform (MAX ELIXIR, Strength):** from the arrival walk **south** two tiles on the platform, then **south** again: the slide down x 20 ends on the bottom-right platform at (20, 17). The MAX ELIXIR is at **(22, 20)**, behind a **Strength boulder at (22, 19)** pushed west to (21, 19) (add that boulder; it is not in the grid).
- **To the bottom-left platform (the Annex ladder at (4, 18)):** from the bottom-right platform, one step west to (19, 17), then **west** along y 17: the slide stops on the bottom-left platform at (6, 17); walk to the ladder at **(4, 18)**.
- **Trainer (card): Fisherman: SEEL 33, SPHEAL 33**, ice fishing in a hole: he stands on the **top-left platform at (4, 4)**, facing east, sight 5, beside a small `bg_event` fishing hole. He sees the player on y 4 only, and none of the solutions above stops on y 4, so he is an optional fight: slide west along y 4 from the top-right platform to meet him.
- **Warps:** the up-ladder (20, 3) to `HoarfellIceCave_B1F` (6, 17) landing (7, 17); the Annex ladder (4, 18) to `HoarfellIceCave_Annex` (6, 17) landing (6, 16).
- **Items:** REVIVE (11, 12) island, MAX ELIXIR (22, 20) Strength. No other items.

## Floor Annex: `HoarfellIceCave_Annex` (16 x 22)

A small slide room with a **stone shelf at the top** (the TM) and a **ladder at the bottom**. In the render: an item at **(6, 6)** on a raised shelf x 3 to 9, y 2 to 9, stone **steps** at **(6, 10)**, a ladder at **(6, 17)**, and an ice floor x 2 to 15, y 11 to 21 below.

The grid (x 2 to 15 across, y 11 to 21 down; `s` snow patch, `#` boulder, `.` ice, `S` the ladder tile at (6, 17), `G` the goal (6, 11), directly below the steps):

```
     x 2  3  4  5  6  7  8  9 10 11 12 13 14 15
y 11   .  .  .  #  G  #  .  .  .  .  .  .  .  .
y 12   .  .  .  .  s  .  .  .  .  .  .  .  .  .
y 13   .  #  #  .  .  .  .  .  .  .  .  .  .  .
y 14   .  .  .  .  .  .  .  .  #  .  .  .  .  .
y 15   #  .  .  .  #  .  .  .  .  .  .  .  s  .
y 16   .  .  .  .  .  .  .  .  .  .  .  .  .  .
y 17   .  .  .  .  S  .  .  .  .  .  .  .  .  .
y 18   .  .  .  .  .  .  .  .  .  .  #  .  .  .
y 19   .  .  #  .  .  .  .  .  .  .  .  .  .  .
y 20   .  .  .  .  .  .  #  .  .  .  .  .  .  .
y 21   #  .  .  .  .  .  .  .  .  .  .  .  .  .
```

**Solution (6 slides, the only shortest one):** from S **west** (slides to (2, 17)), **south** (down x 2 to (2, 20), the boulder at (2, 21) below), **east** (along y 20 to (7, 20), the boulder at (8, 20) on the right), **north** (up x 7 to (7, 12), the boulder at (7, 11) above), **west** (onto the snow patch (6, 12), which stops you), **north** to **G (6, 11)**. Then walk **north up the steps (6, 10)** and across the shelf to the **TM Blizzard at (6, 6)**. The solver found 33 stop tiles, so there are many dead ends; none traps the player, because every stop has a slide back.

- **Trainer (card): Hiker: PILOSWINE 34, BERGMITE 34** at **(14, 15)**, facing west, sight 5, standing on the grid's snow patch at (14, 15) (it is a stop, so he is never in the way of the solution).
- **Warps:** the ladder (6, 17) to `HoarfellIceCave_B2F` (4, 18) landing (4, 17).

## Warp table (Ice cave)

| Map | Tile | Destination |
|---|---|---|
| `Hoarfell` | the north-centre cave door (about (24, 5)) | `HoarfellIceCave_1F` warp 0 |
| `Hoarfell` | the north-east shelf cave door (about (41, 12)) | `HoarfellIceCave_1F` warp 1 |
| `HoarfellIceCave_1F` | (6, 21) | `Hoarfell` warp 0, lands in front of the north-centre door |
| `HoarfellIceCave_1F` | (38, 29) | `Hoarfell` warp 1, lands in front of the north-east door |
| `HoarfellIceCave_1F` | (21, 8), the ladder down | `HoarfellIceCave_B1F` (13, 2) |
| `HoarfellIceCave_B1F` | (13, 2), stairs up | `HoarfellIceCave_1F` (21, 8), landing (21, 9) |
| `HoarfellIceCave_B1F` | (6, 17), ladder down; the four holes | `HoarfellIceCave_B2F` (20, 3) |
| `HoarfellIceCave_B2F` | (20, 3), ladder up | `HoarfellIceCave_B1F` (6, 17) |
| `HoarfellIceCave_B2F` | (4, 18), ladder down | `HoarfellIceCave_Annex` (6, 17) |
| `HoarfellIceCave_Annex` | (6, 17), ladder up | `HoarfellIceCave_B2F` (4, 18) |

## Items summary (card, with the gates)

| Item | Where | Gate |
|---|---|---|
| ICE HEAL | 1F (32, 9) | none |
| NUGGET | 1F (3, 3), Field A | Rock Smash (the rock at (18, 14) blocks Field A's entry) |
| PROTEIN | B1F (4, 16) | none |
| TM Hail | B1F (20, 6) | none |
| RARE CANDY | B1F (13, 17), hidden | none |
| REVIVE | B2F island (11, 12) | none, slide to it |
| MAX ELIXIR | B2F (22, 20) | Strength |
| TM Blizzard | Annex (6, 6) | slide puzzle |

## Visual identity

White, pale blue and slate; a cold hum; breath puffs (a `WEATHER_NONE` map with a light-blue palette). Silhouettes: the bright ice field in the first room, the pillars of B1F, the huge floor of B2F. Music (PROPOSED, an existing Hoenn track): `MUS_CAVE_OF_ORIGIN` (calm and hollow).

## Flags (not claimed)

`FLAG_HOARFELL_CAVE_*` per item and reused trainer flags. No story flag.

## Build checklist (Ice cave)

1. Open `ShoalCave_LowTideIceRoom` in Porymap and note the ice and wall blocks. 2. Add `HoarfellIceCave_1F` (43 x 33), tilesets General + Cave, then paint the frame, the central floor, the fields. 3. Paint Field A from the grid. 4. Add B1F, B2F, Annex. 5. Paint the ladders, holes, boulders and the grids' ice. 6. Test every slide in the game (the author plays it): a puzzle is only done when the emulator agrees with the grid. 7. Trainers, items. 8. Wire the two cave doors in Hoarfell. 9. Credits (Palladium). 10. `make -j4`.

## Build effort

**Medium** with the Shoal Cave tile (the card said hard because of ice art, but the ice tile exists); **hard** if Plan B's FRLG look is attempted. The puzzles are easy once painted from the grids, but **test each in the emulator** (see below).

## Open questions (Ice cave)

1. **Does sliding trigger trainer sight?** Not tested here. If a trainer does not spot a sliding player, put a `coord_event` on the stop tile in front of him that starts the fight (a standard pattern).
2. **Plan A or Plan B** tilesets (Shoal Cave pair or the Icefall FRLG pair)?
3. **Two doors, one cave.** The card asks if the north-east door is a second entrance to the same floor. I made it the exit of the same 1F (a loop). Right?
4. **A one-off Pokémon** in the cave? None assumed.
5. **Section id:** reuse `MAPSEC_HOARFELL` for all four caves (saves a scarce id) or a new `MAPSEC_HOARFELL_CAVE` (a separate popup)?
