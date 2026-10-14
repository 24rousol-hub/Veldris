# BRINECOMBE, detailed design (town, place 14, no gym)

Status: **PROPOSED**, written 2026-10-01. Nothing here is built; minor names are marked PROPOSED. Adds detail to [../towns/brinecombe.md](../towns/brinecombe.md), following [../interiors/README.md](../interiors/README.md). House style: [../../interiors.md](../../interiors.md). Catalogue: [../interiors/catalogue.md](../interiors/catalogue.md). Roads: [routes-east-detail.md](routes-east-detail.md). Sister towns: [hemlock-reach.md](hemlock-reach.md) and [primrose-vale.md](primrose-vale.md). House layouts follow the templates G4-A, G4-B, G4-C in [ebbsworth.md](ebbsworth.md) 6.0.

**Coordinates:** `(x,y)` tiles from the top-left `(0,0)` as Porymap shows them. Interiors: top two rows are back wall, exit mat on the bottom row. Exterior footprints are estimates; door tiles matter. **Pokémon only**, no real animals, even in names or jokes.

## 1. Description

**First glance.**
- **From the sea (R14, the west, the way the player arrives first).** A low, pale town on a sand shelf under a cliff, with a broken line of moored boats and a short pier. The nearest building is a red-roofed Pokémon Center right at the water's edge, and behind it, big and brown, the salt works with its long ridged roof. Everything is the colour of dry sand and driftwood.
- **From R15 (the north).** The road comes down a slot in the cliff and the whole town opens below: rectangles of shallow water on the sand, shining, with white heaps between them, and in the middle of them, tilted, a rich cousin's yacht that is not going anywhere.
- This is a working town, not a pretty one. It smells of brine and sun-dried rope.

**Mood and colour.** Bright, flat midday light, cream sand, white salt, brown roofs, one red roof. A rest between two gyms. Weather: sunny.

**Sound.** Music suggestion: town `MUS_DEWFORD` (a quiet harbour tune), Center `MUS_POKE_CENTER`. Ambient: none.

**The memorable view.** The salt pans seen from the cliff slot: a grid of mirrors lying on the sand, each holding a square of sky.

## 2. Source, size, tilesets

| Item | Decision |
|---|---|
| Palladium render | **`Cianwood City.png`** (579 x 868 px, 1 px grid, `(px-1)/17` = **34 x 51 tiles**). The approved pairing in [../../region-names.md](../../region-names.md). Credit the Project Palladium team in `CREDITS.md` in the first-trace commit. |
| Mirroring | **Trace it mirrored left to right** (the picture has the sea on the east; Brinecombe's sea is west). Every picture tile `(x,y)` becomes map tile `(33 - x, y)`. |
| Base | Vanilla `PacifidlogTown` (`LAYOUT_PACIFIDLOG_TOWN`, 20 x 40, `gTileset_General` + `gTileset_Pacifidlog`) duplicated and enlarged to the final size. Pacifidlog's tileset has sea tiles, rope bridges and rocks. |
| Final size | **34 x 51.** (34 + 15) x (51 + 14) = 3185, under 10240. |
| Tilesets | `gTileset_General` (LeoB ORAS recolour) plus `gTileset_Pacifidlog` for the sea and rock. The render's sand, brown cliff and orange-roof houses come close to the Hoenn General sand tiles and brown cliffs. No new import for the exterior. |
| Section | New `MAPSEC_BRINECOMBE` (PROPOSED). Interiors share it. |
| Fly and heal | One row in `src/data/veldris_fly_towns.h` plus the checklist in [../../region-map.md](../../region-map.md). Heal location `HEAL_LOCATION_BRINECOMBE` at `(7,38)` (in front of the Center door), `respawn_map` before `respawn_npc`, both given. `FLAG_VISITED_BRINECOMBE` on transition. |

### The render read, in mirrored map coordinates

The picture has: a west cliff band down its whole left edge, a north cliff block with a notch, five small orange-roofed houses, a Pokémon Center (red roof), one large building (the Johto gym), three signs, an open sand shelf, and sea on the east with a line of sea rocks. After mirroring:

| Feature | Map `(x,y)` |
|---|---|
| Cliff band (east edge now) | `x 29 to 33`, `y 0 to 50` |
| North cliff block | `x 15 to 33`, `y 0 to 7` |
| **The notch in the north cliff (the R15 slot)** | `x 22 to 23`, `y 5 to 7` in the render; **widen to `x 21 to 23`, `y 0 to 7`** |
| Small house, picture NE (orig `x 5 to 8, y 7 to 10`) | `x 25 to 28`, `y 7 to 10`, door `(27,10)` |
| Small house, picture middle (orig `x 10 to 13, y 21 to 24`) | `x 20 to 23`, `y 21 to 24`, door `(22,24)` (a shed) |
| Small house (orig `x 16 to 19, y 27 to 30`) | `x 14 to 17`, `y 27 to 30`, door `(16,30)` (a shed) |
| Small house (orig `x 18 to 21, y 33 to 36`) | `x 12 to 15`, `y 33 to 36`, door `(14,36)` |
| Small house (orig `x 15 to 18, y 40 to 43`) | `x 15 to 18`, `y 40 to 43`, door `(17,43)` |
| Pokémon Center (orig `x 24 to 28, y 34 to 37`) | `x 5 to 9`, `y 34 to 37`, door `(7,37)` |
| Large building (orig `x 7 to 13, y 34 to 38`) | `x 20 to 26`, `y 34 to 38`, door `(23,38)` |
| South cliff and east-lobe (orig `x 21 to 32, y 41 to 50`) | `x 1 to 12`, `y 41 to 50`, and the bottom band `y 44 to 50` |
| Sea | west of a stepped shore: at `y 8 to 14` water reaches `x 16`; at `y 15 to 19` it reaches `x 20`; at `y 20 to 23` `x 18`; at `y 24` `x 11`; at `y 29` `x 4`; below that `x 0 to 4`. The whole west edge `x 0` is water for `y 0 to 38` |
| Sea rocks (the line of rocks in the render) | a diagonal run at `x 5 to 11`, `y 0 to 22` (decor, shown in the sea) |

## 3. Street layout, a numbered walk

1. **The R15 slot (north).** A slot 3 tiles wide, `x 21 to 23, y 0 to 7`, cut through the north cliff block, with the cliff either side. The R15 connection is its top edge. A sign at `(22,8)`: BRINECOMBE.
2. **The north third.** The path opens onto sand. **House A** (the retired boatman) at the east, `x 25 to 28, y 7 to 10`, door `(27,10)`. The **Harbour Office** (a new building, not in the render) at the shore, `x 21 to 25, y 14 to 17`, door `(23,17)`, with its back to the cliff and a sign at `(22,18)`: HARBOUR OFFICE. A rock outcrop (decor) at `x 26 to 29, y 13 to 16`.
3. **The salt pans, middle third.** A flat `x 6 to 19, y 24 to 32` with **five shallow pans** (decor) in two rows: row 1 at `y 25 to 26`, pans at `x 7 to 9`, `x 11 to 13`, `x 15 to 17`; row 2 at `y 28 to 29`, pans at `x 6 to 8` and `x 10 to 12`. White **salt heaps** on the sand between the rows at `y 27` and `y 30`. The two picture houses at `(22,24)` and `(16,30)` become **salt sheds** (decor, no warp, a closed door and a sign; open question 3). A **grounded yacht** (decor) at `x 18 to 21, y 28 to 30`: a rich cousin's yacht stuck on the pans. A sign at `(11,26)`: DO NOT RAKE IN CIRCLES.
4. **The Salt Works, south.** The large building at `x 20 to 26, y 34 to 38`, door `(23,38)` (the card's 'big-roofed' building), with a sign at `(25,40)`: SALT WORKS.
5. **The quay and Center, south-west.** The Pokémon Center at `x 5 to 9, y 34 to 37`, door `(7,37)`, right on the shore. The **Chandlery** (the Mart) at `x 12 to 15, y 33 to 36`, door `(14,36)`. **House B** (the net-mender) at `x 15 to 18, y 40 to 43`, door `(17,43)`. The **pier** is a plank run `x 1 to 5, y 30` on the shore between the pans and the Center, ending at `(1,30)` over the water; the player surfs from its end, and the R14 connection is the water at `x 0`. Two moored boats (decor, if the tileset has a boat tile; otherwise just posts and rope) at `(2,32)` and `(2,34)`.
6. **The south ledge.** The south cliff (`x 14 to 30, y 44 to 48`) has a top ledge reached by a short stair at `x 19 to 20, y 44`. A Cut tree at `(19,45)` guards an ETHER at `(19,46)`. A Strength boulder at `(24,45)` and a PP UP at `(26,45)` behind it.
7. **A nook behind House B.** The cliff foot east of House B has a 1-tile-wide nook `x 19 to 21, y 42 to 43` closed by a Rock Smash rock at `(20,42)`, holding the TM Reflect at `(21,43)`. The card said 'behind House B'; this is east of it.

### Connections

| Edge | Map | Offset | Matching tiles |
|---|---|---|---|
| North | `Route15` (R15, 30 x 54) | Brinecombe `up` offset `+8` (R15 `x 0` sits at Brinecombe `x 8`) | R15 `x 13 to 15` meets Brinecombe `x 21 to 23` |
| West | `Route14` (R14, 56 x 24) | Brinecombe `left` offset `+10` (R14 row 0 sits at Brinecombe row 10) | R14 rows 8 to 20 meet Brinecombe rows 18 to 30 (sea) |
| East, south | none | | cliff |

Recompute when the maps exist; check Porymap's connection preview.

## 4. Palette and tile notes

- **Salt pans:** painted with water tiles, then set to **collision** in Porymap's collision tab so the player cannot step onto them and cannot Surf in them. They must not be encounter water: the town carries no water table (the harbour water uses the R14 table, see section 8). Alternative: paint them as sand with the blue 'wet sand' tile if the tileset has one.
- **Heaps:** white rock or boulder-shaped tiles from the General tileset, collision on.
- **Yacht:** no yacht tile exists in General. Use any boat tile the Pacifidlog or Slateport sets have, or a block of `Cut` tree-like crates, or just skip the art and keep the yacht as text and a sign at `(19,31)`. Cut freely.
- **Sea rocks:** the Hoenn sea-rock tiles, with the shallow ring.
- **Needs redrawing:** nothing for a first playable version.

## 5. Every building

### 5.1 Pokémon Center (`Brinecombe_PokemonCenter_1F`, `_2F`)

Shared `LAYOUT_POKEMON_CENTER_1F` and `_2F` (decision 2). Nurse `(7,2)` (needs `LOCALID_BRINECOMBE_NURSE`), counter `x 4 to 9, y 2 to 3`, mats `(6,8)` and `(7,8)`, stairs `(1,6)`. Objects: a **sailor on shore leave** `(10,6)` facing left, a **net-mender's apprentice** `(5,5)` wandering. Warps: `(6,8)` and `(7,8)` to `Brinecombe` warp 0 (tile `(7,37)`).

### 5.2 Chandlery (`Brinecombe_Chandlery`)

Shared `LAYOUT_MART` (11 x 8): clerk `(1,3)`, counter `x 2, y 2 to 4`, mats `(3,7)` and `(4,7)`. Stock leans to Great Ball, Super Potion, Repel, Net Ball (card). Objects: a **customer** buying rope `(5,5)` facing right, an **old sailor** `(9,5)`. Warps: `(3,7)` and `(4,7)` to `Brinecombe` warp 1 (tile `(14,36)`).

### 5.3 Salt Works (`Brinecombe_SaltWorks`)

- **Layout:** new, **13 x 10**, **Team Aqua `Legend of Zelda House Secondary`** + `gTileset_Building` (clay pots, a shelf of bowls, a hearth, jugs, a green mat: see its `example.png`). It is the right workshop look for a place that boils and dries salt. **What it adds:** timber and stone walls, pots, jugs, a hearth, bowl shelves. **What it needs:** a Porytiles conversion (the folder is a triple-layer set of 512 metatiles, the same job the Gen 4 Interior set got, see [../../interiors.md](../../interiors.md) 'Tileset notes'), a `CREDITS.md` row (credits: Buildings Hek-el-grande, Assembler Yumekua, Main Creator Ekat99, reformat Rahtak; asset repo norm: credit creators), imported **in the commit that first needs it**. [Hemlock's Boathouse](hemlock-reach.md) uses the same tileset, so the import pays off twice; whichever town is built first carries the CREDITS row.
- **Plan:**
  - Back wall `y 0 to 1` with two windows at `x 3` and `x 9`; hearth at `(11,2)` (the boiling fire); a shelf of bowls at `x 2 to 4, y 2` (finished salt).
  - A long **drying table** (counter, collision) `x 4 to 8, y 4` with white heaps on it.
  - Clay pots (salt jars) along the west wall at `(1,3)`, `(1,4)`, `(1,5)`, `(1,6)`; jugs at `(10,3)` and `(10,4)`.
  - **Stools** at `(5,6)` and `(8,6)`; a sieve rack at `(11,6)` (bg event).
  - Green mat `x 5 to 7, y 8`; **door mat `(6,9)`**.
- **Objects (3):** the **foreman** `(6,3)` behind the drying table, facing down (complains about flat-pack condominiums on the next coast; asks the player to find his lost sieve, then gives SEA INCENSE), a **raker** `(3,6)` facing right (tea break), a **boiler** `(10,5)` facing the hearth.
- **Quest:** the sieve is found on the pier (a flag-only bg event at `(2,30)`, no new item, so no engine edit); returning to the foreman gives SEA INCENSE once.
- **Warps:** `(6,9)` to `Brinecombe` warp 2 (tile `(23,38)`).

### 5.4 Harbour Office (`Brinecombe_HarbourOffice`)

- **Layout:** new, **13 x 10**, **Team Aqua `Gatehouse Secondary`** + `gTileset_Building` (a U-shaped counter, a wall clock, a round rug, plants, an unused back door: see its `example.png`). The tileset ships a `porytiles/` folder in the repo (ready for the conversion tool that Hollowbrook already used), but it also says in its README that it needs expanded and triple-layer metatiles, so it needs the same conversion as the Zelda set, plus a `CREDITS.md` row (Ekat, Vurtax (FRLG rips), Heartlessdragoon (RSE rips), reformat Rahtak). It is also what the R13 and R15 rest huts would use ([routes-east-detail.md](routes-east-detail.md)), so it is worth importing once for three buildings. Fallback: Gen 4 Interior with the counter and shelf vocabulary.
- **Plan:**
  - Back wall `y 0 to 1`: a wall clock at `(6,1)`, a window at `(3,1)`, a dark back door at `(9,1)` (decor, no warp).
  - **U-shaped counter** (collision): left arm `x 3, y 3 to 5`, bottom `x 3 to 9, y 5`, right arm `x 9, y 3 to 5`. The harbour master stands inside at `(6,3)`, facing down. The player talks from `(6,6)` facing up.
  - A **tide table** board (bg event) at `(1,2)`; a **chart table** with a lamp at `(11,4)` and `(11,5)`.
  - Plants `(1,8)` and `(11,8)`; a round rug `x 5 to 7, y 7 to 8`.
  - **Door mat `(6,9)`.**
- **Objects (2):** the **harbour master** `(6,3)` (gives the SUPER ROD once; sea roads close in rough weather, flavour), a **sailor** `(10,7)` at the chart table, facing left (confirms the Mirror Isle legend).
- **Warps:** `(6,9)` to `Brinecombe` warp 3 (tile `(23,17)`).

### 5.5 House A, the retired boatman (`Brinecombe_HouseA`)

Shares **`LAYOUT_HOLLOWBROOK_NEIGHBOURS_HOUSE`** (11 x 8, built; free floor at `(8,3)`, `(5,6)`, `(9,5)`; bookshelf bg `(7,2)`, `(8,2)`; exit mat `(2,7)`). Objects (2): the **retired boatman** `(8,3)` facing up (tells the legend: 'the shrine has no door, only a doorstep'), a Skitty `(2,4)`. Warp `(2,7)` to `Brinecombe` warp 4 (tile `(27,10)`).

### 5.6 House B, the net-mender (`Brinecombe_HouseB`)

The **G4-B 'One-room cottage' template, 10 x 8** ([ebbsworth.md](ebbsworth.md) 6.0: bed `x 0 to 1, y 1 to 2`, window `(3,1)`, bookshelf `x 6 to 7, y 1 to 2`, stove and cupboard `x 8 to 9, y 1 to 2`, rug `x 1 to 4, y 4 to 6` with a low table `(3,5)` and `(4,5)`, plant `(9,6)`, door mats `(3,7)` and `(4,7)`). A new layout; the sea cottage suits the one-room plan. Objects (2): the **net-mender** `(2,3)` facing right (her mother taught her knots at 'about the same time as walking'), a Slakoth `(7,5)`. Warps `(3,7)` and `(4,7)` to `Brinecombe` warp 5 (tile `(17,43)`).

### 5.7 Non-enterable

Two salt sheds (decor), the grounded yacht, boats, cranes. No Goldsworth house (it is a town). No gym.

## 6. NPCs

12 roles (towns want 8 to 14). **Outdoor live objects (15 maximum, 12 used):**

| # | Role | Position | Behaviour | Topic |
|---|---|---|---|---|
| 1 | Salt raker | `(9,27)` | wanders left and right | Rakes in rows, never in circles; hints at a hidden Big Pearl off the pier. |
| 2 | Raker's apprentice | `(13,27)` | wanders | Mixes up salt and sugar. Harmless. |
| 3 | Child with a bucket | `(15,32)` | wanders | Collects pebbles and sea glass; swaps one for nothing. |
| 4 | Fisherman | `(3,31)` | faces west | Tentacruel gather off the Hemlock side; optionally 'a boy in a very clean jacket rowed past with a lot of luggage'. |
| 5 | Cousin on the yacht | `(19,29)` | faces down; **only before gym 7 is beaten** (`FLAG_BADGE07_GET` hides him) | Shouts at a tide table. |
| 6 | Hazmat inspector, returned | `(12,24)` | faces left; shown only when `VAR_HEMLOCK_SCHEME7 >= 2` | Buys salt, clipboard under one arm, avoids eye contact. |
| 7 | Cut tree | `(19,45)` | tree | ETHER `(19,46)`. |
| 8 | ETHER ball | `(19,46)` | item | |
| 9 | Strength boulder | `(24,45)` | boulder | PP UP `(26,45)`. |
| 10 | PP UP ball | `(26,45)` | item | |
| 11 | Rock Smash rock | `(20,42)` | rock | TM Reflect `(21,43)`. |
| 12 | TM Reflect ball | `(21,43)` | item | |

Interior NPCs: Center nurse, sailor, apprentice; Chandlery clerk, customer, old sailor; Salt Works foreman, raker, boiler; Harbour master and sailor; the boatman and Skitty; the net-mender and Slakoth. Card roles kept: harbour master, foreman, raker, apprentice, nurse, clerk, boatman, net-mender, fisherman, child, cousin, inspector.

## 7. Items and secrets (positions added to the card)

| Item | Where | Gate |
|---|---|---|
| **SUPER ROD** | harbour master, Harbour Office | none, once. PROPOSED (open question 1) |
| SEA INCENSE | foreman, after finding the sieve at the pier `(2,30)` | none |
| ETHER | `(19,46)` behind the Cut tree | Cut (badge 1) |
| PP UP | `(26,45)` behind the boulder | Strength (badge 4) |
| TM Reflect | `(21,43)` behind the rock | Rock Smash (badge 2) |
| Hidden PEARL | `(21,28)` in a salt heap | none (0x264 hidden-item range) |
| Hidden SUPER POTION | `(4,42)` on the beach | none |
| Hidden BIG PEARL | the pier end water `(1,29)` | **Dive (badge 9)**, a return trip, PROPOSED. Dive needs an underwater map and none exists (open question 2) |
| Fly point | the town | Fly (badge 6) |

## 8. Wild Pokémon

None in the town. The pier and the harbour use the **R14** surf and fishing tables ([routes-east-detail.md](routes-east-detail.md)). The salt pans are collision-only decor with no encounters.

## 9. Flags and vars (not claimed)

- `FLAG_VISITED_BRINECOMBE`.
- `FLAG_RECEIVED_SUPER_ROD` (an existing vanilla flag may be reused for the rod).
- `FLAG_BRINECOMBE_SIEVE_FOUND`, `FLAG_BRINECOMBE_SEA_INCENSE`.
- `FLAG_BRINECOMBE_ITEM_ETHER`, `FLAG_BRINECOMBE_ITEM_PPUP`, `FLAG_BRINECOMBE_TM_REFLECT`.
- The returned inspector reads `VAR_HEMLOCK_SCHEME7 >= 2` (no flag of its own). The yacht cousin reads `FLAG_BADGE07_GET`.
- Hidden items: three flags from 0x264. About 8 flags, no var.

## 10. Door and warp table

| Map | Tile | To | Dest warp |
|---|---|---|---|
| `Brinecombe` 0 | `(7,37)` | `Brinecombe_PokemonCenter_1F` | 0 |
| `Brinecombe` 1 | `(14,36)` | `Brinecombe_Chandlery` | 0 |
| `Brinecombe` 2 | `(23,38)` | `Brinecombe_SaltWorks` | 0 |
| `Brinecombe` 3 | `(23,17)` | `Brinecombe_HarbourOffice` | 0 |
| `Brinecombe` 4 | `(27,10)` | `Brinecombe_HouseA` | 0 |
| `Brinecombe` 5 | `(17,43)` | `Brinecombe_HouseB` | 0 |
| PC 1F | `(6,8)`, `(7,8)` | `Brinecombe` | 0 |
| PC 1F and 2F | `(1,6)` | each other | 0 and 2 |
| Chandlery | `(3,7)`, `(4,7)` | `Brinecombe` | 1 |
| Salt Works | `(6,9)` | `Brinecombe` | 2 |
| Harbour Office | `(6,9)` | `Brinecombe` | 3 |
| House A | `(2,7)` | `Brinecombe` | 4 |
| House B | `(3,7)`, `(4,7)` | `Brinecombe` | 5 |

Signs (bg events): `(22,8)` BRINECOMBE, `(22,18)` HARBOUR OFFICE, `(11,26)` salt pans, `(25,40)` SALT WORKS, `(8,38)` Center, `(15,37)` Chandlery.

## 11. Build checklist, in order

1. Add the Project Palladium row to `CREDITS.md` naming `Cianwood City.png` in the commit of the first trace.
2. Duplicate `PacifidlogTown`, delete the two copied heal locations, set the header to `MAPSEC_BRINECOMBE`, Change Dimensions to 34 x 51, repaint ground elevation 3.
3. Trace `Cianwood City.png` **mirrored**: cliffs first, then the shore line and the sea rocks, then the sand and the building footprints.
4. Carve the R15 slot (`x 21 to 23, y 0 to 7`), paint the salt pans and set their collision, place the signs.
5. Build the pier and set the water so the player can surf from `(1,30)`.
6. Interiors: Center and Mart on shared layouts; House A on the Hollowbrook layout; House B on the G4-B template (a new layout); Salt Works on the Zelda set; Harbour Office on the Gatehouse set. Import and convert each Team Aqua tileset in the commit that first needs it, with its `CREDITS.md` row.
7. Claude wires: connections (offsets in section 3), warps, objects, flag-gated NPCs, the Super Rod, the sieve quest, Fly row and heal location, `flags.md`.
8. Test: arrive from R14, from R15, heal and fly, the rod, the sieve, the returned inspector after Scheme 7.

Effort: **medium**. One mirrored trace, two small Team Aqua imports, otherwise shared interiors. A good early build in the east: it can be tested with only R14 and R15.

## 12. Open questions

1. **Where do the Old and Good Rods come from?** The Super Rod is here (PROPOSED); the docs do not say where the lower rods come from.
2. **BIG PEARL needs Dive.** Dive needs an underwater map and none is planned. Either drop it, or build one tiny underwater pocket (about 12 x 10, vanilla `Underwater` secondary, one hidden item). Ask before adding it.
3. **Salt sheds.** The two spare picture houses are decor sheds. Make one an enterable house if the town wants more voices.
4. **Yacht art.** No yacht tile; a text-and-sign fallback is described.
5. **Two Team Aqua imports for one small town** (Zelda House for the Salt Works, Gatehouse for the Harbour Office). The fallback for both is Gen 4 Interior. Which does the author want?
6. **Mirroring.** If the author prefers the render unflipped, move R14 to the east edge and the cliff to the west.
7. **Harbour Office placement.** It is my addition (the render has no building at the north-west shore); the card asked for a Harbour Office there.
