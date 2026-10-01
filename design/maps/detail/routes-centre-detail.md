# Roads of the centre, detailed design: R10, R11, R12, R18, R19, R20, R21

Status: **PROPOSED.** Written 2026-10-01 for the author to build from. Cards this expands: [../routes-centre.md](../routes-centre.md) (species, levels, wild tables, items, flags are **unchanged and not repeated**), template in [../interiors/README.md](../interiors/README.md) ('Per road'). Related: [cragdale.md](cragdale.md), [lingmoor.md](lingmoor.md), [waymeet.md](waymeet.md), [gildhaven.md](gildhaven.md), [pinnacle-detail.md](pinnacle-detail.md). New minor names are PROPOSED.

## How to read the tile numbers

- `x, y` are tiles from the render's top-left (0,0). I measured every Palladium road render on its **1 px grid** (`(px - 1) / 17`) and read positions off a labelled copy of each. Sizes agree with the card: R10 64 x 23, R11 67 x 25, R12 24 x 40, R18 28 x 32, R20 22 x 91, R21 22 x 36.
- **Trainer, item and sign tiles are targets, good to about 2 tiles.** Each one is on a tile that is walkable in the render, with a clear line of sight in the stated direction. If the author's trace moves a feature, move the trainer with it and keep the **facing and sight**.
- **Trainer sight is blocked by walls, ledges, objects and by water** (elevation mismatch), so a trainer must look along walkable ground. Sight ranges below follow the vanilla pattern (1 to 5 tiles).
- **Wild grass.** The Palladium roads are mostly plain grass with a few tall-grass tiles, but the cards give 12-slot land tables, so each road below lists **tall-grass patches to paint** (heather and fern count as tall grass).
- **Object budget:** at most 15 live objects per map. Each road notes its count.
- **Palladium renders reused by more than one card.** Route 42 is used by R10 (here), R13 (east group) and R6 (west group); Route 44 by R11 and R6; Route 35 by R18 and R9. See Open question 1.

## Summary

| Road | Render | Size | Edge to | Edge to | Gate |
|---|---|---|---|---|---|
| R10 | Route 42 | 64 x 23 | Hoarfell (west) | Cragdale (east) | none |
| R11 | Route 44 | 67 x 25 | Cragdale (west) | Lingmoor (east) | none |
| R12 | Route 39 | 24 x 40 | Lingmoor (north) | Waymeet (south) | none |
| R18 | Route 35 | 28 x 32 | Hoarfell (north) | Gildhaven (south) | closed from Hoarfell until the Feather Badge (works) |
| R19 | vanilla Route 129 | 80 x 40 | Gildhaven (west) | Waymeet (east) | Surf |
| R20 | Route 45 + vanilla Victory Road | 22 x 91 + three caves | Gildhaven (north) | The Pinnacle (south) | nine badges at the Pinnacle Gate guard line |
| R21 | Route 46 | 22 x 36 | The Pinnacle (north) | Vesperhaven (south) | `FLAG_SYS_GAME_CLEAR` |

**Gates are open-road guard lines in this document**, not enterable gatehouses: Gen 3 doors exist only on a building's south face, so a pass-through hut cannot be entered by a player walking south. Each gate is two flanking huts (scenery) with a **guard NPC and a barrier object** across the road, removed or opened by a flag (the same trick as vanilla roadblocks). The render's grey gatehouses are traced as the flanking huts.

---

## R10: Hoarfell to Cragdale (land, Palladium Route 42, 64 x 23)

### Description and walk-through

**Opening view from Hoarfell (west).** The player leaves the snow city and steps out of a **closed toll hut** (a grey hut at the map edge, shutters down, a sign 'CLOSED SINCE FOREVER') into **clear, cold air**: a sand clearing in a stand of dark pines, a signpost, and a long pass opening east between a cliff wall on the left and the green floor on the right. **Opening view from Cragdale (east).** A wide sand plain under the cliff, a one-way ledge to hop down, then a long walk west along two ponds.

**Shape and pacing.** A long east-west pass, about 60 tiles. The pass is a **green belt between a cliff wall to the north and pines or rock to the south**, with two ponds set into the belt, so the player is always walking the shore of something. Set pieces: the closed toll hut (west), the **first pond with a rock islet**, the heath between the ponds, the **second pond with another islet**, three **dark cave doorways** in the cliff (scenery, see below), and the **east sand plain** with two signs. Pacing: a trainer roughly every 7 tiles; the two ponds are rest points with Fishermen and Surf items.

### Segments (about 6)

| # | Columns | What is there |
|---|---|---|
| 1 | 0-15 | **West clearing.** The toll hut at cols 0-3, rows 7-11 (scenery; the render's hut straddles the edge). **Carve the road at the west edge: rows 12-14** (remove the pines at cols 0-4, rows 12-14). A **sand clearing** at cols 5-15, rows 9-14. Signs **(11,8)** ('HOARFELL, snow city') and **(8,13)**. A lone boulder at (9,5). A dark doorway (cave nook, decor) at **(14,8)** |
| 2 | 16-29 | **First pond.** Pond at **cols 16-25, rows 7-17** (an upper lobe cols 18-23 rows 7-13 and a lower arm cols 16-25 rows 13-17), **rock islet at (20,14)** (Surf; make it a 1-tile sand islet for the PP Up). The land route runs along the **north bank, rows 6-8**, then down the **east bank, cols 26-29, rows 8-18**. Boulders at (22,8) and (24,17). Sign (mid-road): 'Ponds: Surf to the islets' at (27,9) |
| 3 | 26-35 | **The heath.** Green with a small sand patch at **cols 30-35, rows 13-14**. A dark doorway at the cliff foot **(32,12)** (decor). Boulder (17,16) near the south pines |
| 4 | 36-47 | **Second pond.** Pond at **cols 36-45, rows 9-17** (lower arm cols 38-40 rows 14-17), **islet (40,14)**. Boulders at (44,10) and (48,16). The land route follows the south-east shore, rows 15-18, under the rock shelf (cols 40-60, rows 16-22) |
| 5 | 48-60 | **East sand plain.** Sand at **cols 48-60, rows 10-14**. Signs **(49,12)** and **(58,11)**. A dark doorway at **(50,10)**. Boulder (55,7) on the cliff shelf. A **one-way ledge at cols 56-59, row 9** drops from the shelf into the plain (from the Cragdale side only) |
| 6 | 60-63 | **East exit.** The render ends in rock: **carve rows 12-14 east to col 63** (3 wide) as a cut through the cliff, meeting Cragdale's lane |

**Tall-grass patches to paint** (PROPOSED, all on the green): **A** (30-35, 9-12), **B** (26-28, 9-14), **C** (47-52, 14-16), **D** (10-14, 15-17). The sand tiles stay sand.

**The three dark doorways** at (14,8), (32,12) and (50,10) are the render's Union-Cave style cave mouths. They are **scenery** here (a doorway tile with no warp), except that one (the author's choice) can become a **nook** with a free item. The card has none, so they stay decor.

### Trainers (8, class, team and levels as the card)

| # | Class | Tile, facing, sight | Notes |
|---|---|---|---|
| 1 | Hiker | (7,10) east, 5 | on the west clearing, the first fight |
| 5 | Cooltrainer (sulking Hoarfell graduate) | (13,12) north, 3 | beside the sign (11,8) |
| 3 | Black Belt | (24,7) west, 4 | on the north-bank track |
| 7 | Fisherman | (26,13) south, 3 | east bank of pond 1 (looks along the shore, not over water) |
| 2 | Hiker | (30,13) west, 4 | on the heath sand patch |
| 8 | Picnicker | (46,13) south, 3 | near pond 2's east shore |
| 4 | Battle Girl | (50,12) west, 4 | on the sandy slope |
| 6 | Pokémon Ranger | (57,8) south, 4 | on the ledge shelf above the plain, east |

The numbers are the card's order; the rows above are in **walking order from Hoarfell** so the walk escalates (Hiker, Cooltrainer, Black Belt, Fisherman, Hiker, Picnicker, Battle Girl, Ranger). Objects on the map: 8 trainers, 4 NPCs, 3 visible items = 15 (the hut attendant is a **sign**, not an object).

**NPCs (4 live):** the walker with the thermos (13,10) facing east; the weather watcher (28,10) facing south (points at Cragdale's station); the sleeping Hiker on the ledge (57,10) lying down (blocks the ledge landing until woken, optional); the signpost reader (49,13) facing up.

### Items (positions)

| Item | Tile | Gate |
|---|---|---|
| Hyper Potion (visible) | (27,7) on the north track | none |
| Super Repel (visible) | (51,13) on the sandy slope | none |
| Great Ball (visible) | (57,10) at the ledge landing | none |
| Ether (hidden) | (17,10) by the first pond | none |
| Full Heal (hidden) | (33,10) at the cliff foot | none |
| PP Up | islet (20,14) | Surf |
| Rare Candy | islet (40,14) | Surf |

### Visual identity

**Tilesets:** ORAS General (in tree) + **LeoB ORAS `fallarbor`** secondary (rock cliff, ledges; the same set as Cragdale, one CREDITS row). Cold feel from the palette: pale grey rock, desaturated green, dark blue-green pines. **Weather:** `WEATHER_SUNNY` (clear cold sky), no snow. **Music:** `MUS_ROUTE113` (a quiet windy tune). **Silhouettes:** the long cliff line along the north; at the east end the Cragdale ridge rises behind the plain. Credit Palladium for `Route 42.png` in the commit that traces it.

### Connections

| Edge | Neighbour | Offset | Matching |
|---|---|---|---|
| West | `Hoarfell` east edge | set when Hoarfell is built | Hoarfell's east lane (card: 'the lane at the lower right') meets R10 rows 12-14 |
| East | `Cragdale` west edge | **+9 from Cragdale's side** (R10's top at Cragdale row 9) | R10's carved exit (rows 12-14) meets Cragdale's lane (rows 21-23) |

Line up R10's carved opening with Cragdale rows 21-23 and R10's west opening with Hoarfell's east lane, then read the Porymap offset. **Build effort:** medium.

---

## R11: Cragdale to Lingmoor (land, Palladium Route 44, 67 x 25)

### Description and walk-through

**Opening view from Cragdale (west).** The player steps off the lane into a **high basin**: a wide sand track heads east along the foot of a rock wall, a small pond lies below, and a **dark pine grove** fills the middle of the screen. The whole thing is **sky and wind**. **Opening view from Lingmoor (east).** A fenced enclosure on a green shelf with a cave doorway above, a sand column leading down, and the long southern track running away west under the grove.

**Shape and pacing.** A broad basin with **two tracks**: a **south sand track (rows 17-20)** that runs the whole length, and the **moor above it (rows 4-10)** open to the sky with the grove and the ponds between. The first half is open ground and a pond, the second is the enclosure and its ledge. Set pieces: the west pond, the **cairn clearing**, the grove (impassable scenery, a dense wall of pines), the **north pond**, the **enclosure** with its ledge and a **dark doorway (a closed cellar)**.

### Segments (about 6)

| # | Columns | What is there |
|---|---|---|
| 1 | 0-13 | **West sands.** Sand at cols 0-9, rows 12-14 (3-wide road at the west edge); sign **(6,15)** 'CRAGDALE'; the **west pond** at cols 4-13, rows 17-20 (a small basin with a stepped bank); carve **a 2-row grass strip at (0..3, 17..18)** for Cragdale's ledge drop (the render has rock there) |
| 2 | 10-30 | **South track.** Sand at rows 17-20, cols 14-53, long and straight, with the **grove** pressing in from the north (cols 12-33, rows 4-17) and the **centre pond** at cols 22-29, rows 13-18 |
| 3 | 12-20 | **Cairn clearing.** Open green at cols 12-19, rows 6-9, reached from the track by a gap in the grove at (13,16)-(13,12). The **cairn (15,8)**. Trees at (10,5) and (12,5) and a row of four at the clearing's west (0-3, 9) |
| 4 | 31-47 | **North pond and moor.** Pond at **cols 32-45, rows 8-14** (a stepped lake, east arm cols 43-45 rows 10-12); **tall grass row at cols 30-37, row 13** (the render's own patch) plus the moor above the pond (cols 36-47, rows 4-7) |
| 5 | 46-62 | **East shelf.** A vertical ledge at **col 48, rows 9-18** (a one-way ledge line west to east); a **sand column at cols 50-53, rows 10-18**; trees at cols 46-55, rows 4-6. The **enclosure**: green strip at **cols 52-60, rows 11-13** with a ledge at row 13, **sign (55,11)**, **dark doorway (58,11)** |
| 6 | 61-66 | **East exit.** The render ends in rock: **carve rows 11-12 east to col 66** (2 wide, make it 3 with row 13) into Lingmoor's track |

**Tall-grass patches to paint** (PROPOSED): **A** (30-37, 12-14) extending the render's row, **B** (36-46, 5-8), **C** (14-19, 6-9), **D** (10-20, 15-16) on the track's north edge. The sand stays sand.

### Trainers (7, as the card)

| Order | Class | Tile, facing, sight | Notes |
|---|---|---|---|
| 1 | Pokéfan | (8,13) east, 4 | on the west sand, the first fight |
| 2 | Lass | (21,16) east, 3 | on the south bank of the centre pond |
| 3 | Hex Maniac | (16,8) west, 3 | at the cairn |
| 4 | Psychic | (40,7) south, 4 | on the open moor |
| 5 | Gentleman | (50,16) north, 4 | on the sand column, by the enclosure ledge |
| 6 | Guitarist | (53,12) east, 5 | on a rock in the enclosure strip |
| 7 | Pokémon Breeder (toughest) | (58,12) west, 3 | at the enclosure's east end, before the exit |

Objects: 7 trainers, 5 NPCs, 3 visible items = 15. **NPCs (5):** the cairn-builder (15,9) facing down; the lost walker (24,19) wandering; the photographer (44,6) facing west; the **gatekeeper at the enclosure** (51,12) facing east (the 'closed' sign, said twice); the heather-picker (35,5) wandering.

### Items (positions)

| Item | Tile | Gate |
|---|---|---|
| Super Potion (visible) | (25,19) on the south track | none |
| Full Heal (visible) | (47,6) on the moor | none |
| Revive (visible) | behind the enclosure fence **(59,11)**, reached from the east | none (from the Lingmoor side) |
| Max Ether (hidden) | the cairn (15,8) | none |
| Pecha Berry (hidden) | a heather clump (38,5) | none |
| Star Piece | the north pond's islet: **paint a 1-tile islet at (38,11)** | Surf |

### Visual identity

**Tilesets:** ORAS General + **LeoB ORAS `mauville`** (matching Lingmoor; heather, stone). Palette: heather purple on the moor tiles, grey rock, dark pines. **Weather:** `WEATHER_SUNNY` with a strong wind (a flag only; Emerald has none). **Music:** `MUS_ROUTE118`. **Silhouettes:** a cairn on the clearing, the grove's dark wall, the enclosure's fence line against the sky. The dark doorway (58,11) is a **locked cellar** (decor).

### Connections

| Edge | Neighbour | Offset | Matching |
|---|---|---|---|
| West | `Cragdale` east edge | R11's top at Cragdale row 8 (offset +8 from Cragdale's side) | R11 rows 13-15 meet the lane (rows 21-23); R11 rows 17-18 meet Cragdale's ledge strip (rows 25-26) |
| East | `Lingmoor` west edge | Lingmoor's top sits at R11 row 5 (offset **-5** from Lingmoor's side) | R11's carved rows 12-13 meet the track (Lingmoor rows 7-8) |

**Build effort:** medium.

---

## R12: Lingmoor to Waymeet (land, Palladium Route 39, 24 x 40)

### Description and walk-through

**Opening view from Lingmoor (north).** A **stone gate** opens onto a **small paddock** with a fence, then a farmyard: a red-roofed barn (left) and farmhouse (right), a wide **sand yard**, and a long **fenced pen** in the middle. **Opening view from Waymeet (south).** A **sand track** climbing between pines, ledges on the left and right, flower patches, a signpost, and the faint noise of a railway.

**Shape and pacing.** A tall vertical road. North third: **Lowbarrow Farm** (the yard, the barn, the farmhouse, the pen). Middle third: the **long fenced field** and sand turns east. South third: the **ledged track** and the tall-grass field to the west, a straight sand road to Waymeet. Easy, pastoral, a very gentle first look at crossroads country.

### Segments (about 5)

| # | Rows | What is there |
|---|---|---|
| 1 | 0-5 | **North gate.** The render has trees across the top: **clear the trees at cols 12-15, rows 0-2** to make the opening (4 wide) with two stone posts at (11,1) and (16,1) and a gate sign. The **paddock** (cols 12-15, rows 3-5) with fence along row 3 and col 16 |
| 2 | 2-12 | **The farm yard.** The **barn** (cols 2-6, rows 2-5, **door (4,5)**) and **farmhouse** (cols 7-11, rows 1-5, **door (9,5)**) with the sand yard at cols 3-16, rows 6-12. Fences: top row 8 (cols 2-5) and row 11 (cols 2-5 and 12-15), left col 2 (rows 6-19), right col 16 (rows 3-19) |
| 3 | 13-20 | **The pen.** A green fenced pen at **cols 4-14, rows 13-19** (decor, a Miltank object grazing at (8,16)), a sand lane along its right side (cols 15-17, rows 11-19); bottom fence at row 20 (cols 2-15) |
| 4 | 9-30 | **The east side.** A sand road leaves the yard east along rows 9-11 to the map's east edge (**decor only**, a farm lane that ends in a fence), a fenced field at cols 21-23, rows 17-26 (the **railway strip**, see below) |
| 5 | 21-39 | **The track.** A sand road at **cols 10-13, rows 23-39** south to the **south opening (cols 11-14, row 39)**. West of it a **tall-grass field at cols 6-8, rows 23-30** (and 5-7, row 31). **Ledges** (brown cliff steps) at **(14..17, 26)**, **(14..17, 28)**, **(14..17, 30)** (one-way, jump south), and small ones at (9..10, 26), (9..10, 28), (9..10, 30). **Flowers** at (11-13, 20-22) and (16-17, 31-34) and (19, 24-25). **Sign (7,34)** (wooden), signs (13,8) 'Lowbarrow Farm' and (19,10) |

**The railway.** The render has no railway. The card puts one 'on the east, beside the road'. There are **no rail tiles in this tree**, so make it a **fenced gravel strip at cols 21-23, rows 17-26** with a **signal post** (a sign) and a **Goldsworth-livery crate** (an object, 'Estates, urgent', rusting) on a short spur at (22,23). The strip ends at a buffer stop (a fence block). No tracks are needed for the joke.

**Tall-grass patches to paint** (PROPOSED): **A** (6-8, 23-31) the render's own field (3 x 8 + 3), **B** (17-19, 33-37) beside the flowers, **C** (2-5, 22-26) west field, **D** (13-15, 14-17) beside the pen (outside the fence).

### Trainers (6, as the card)

| Order | Class | Tile, facing, sight | Notes |
|---|---|---|---|
| 1 | Pokémon Breeder | (12,7) south, 3 | at the yard gate, right after the paddock |
| 2 | Pokéfan | (6,7) east, 3 | by the barn (door (4,5)) |
| 3 | Camper | (19,10) west, 4 | on the east farm lane |
| 4 | Picnicker | (16,16) west, 3 | by the pen on the sand lane |
| 5 | Youngster | (9,25) west, 3 | in the long grass field |
| 6 | Bug Maniac | (12,32) north, 4 | at the foot of the ledges, the last fight |

Objects: 6 trainers, 5 NPCs, 3 items = 14 live. **NPCs (5):** the **farmer** (13,6) in the yard facing down (the railway shakes the barn); his **wife** (inside the farmhouse); the **barn hand** (inside the barn); the **rail inspector** (22,19) wandering the gravel strip ('the timetable is under review'); the **rail-watching child** (20,21) facing east.

### Items and interiors

| Item | Tile | Gate |
|---|---|---|
| Super Repel (visible) | (11,12) at the yard edge | none |
| Hyper Potion (visible) | (15,22) by the pen's corner | none |
| Revive (visible) | (12,36) on the track | none |
| Max Repel (hidden) | a hay stack (3,10) | none |
| Moomoo Milk (hidden) | the barn side (7,6) | none |
| Full Heal (hidden) | a fence post (16,14) | none |
| Max Elixir | behind a Cut tree at the yard's corner **(15,7)**: item at (16,7) | Cut |

**Interiors (2):** `VeldrisRoute12_Farmhouse` (11 x 8, Gen 4 Interior, template N = `Hollowbrook_NeighboursHouse`, mat (2,7)) with the farmer's **wife** at (5,4) facing down (gives **Moomoo Milk x2** once); `VeldrisRoute12_Barn` (10 x 9, Gen 4 Interior or the vanilla `LAYOUT_HOUSE1` 10 x 9 with the Gen 4 palette), mat (2,8), a **barn hand** (4,4) facing right and an **object Miltank** (`OBJ_EVENT_GFX_SPECIES(MILTANK)`, enabled by `OW_POKEMON_OBJECT_EVENTS`) at (7,5). The **Lowbarrow Farm** name is PROPOSED.

### Visual identity

**Tilesets:** ORAS General + `petalburg` secondary (already in tree) for the farm look, **or** `mauville` to match the towns it joins. **Weather:** `WEATHER_NONE`. **Music:** `MUS_ROUTE104`. **Silhouettes:** red barn and farmhouse roofs at the top, a line of pines on both sides, the grey gravel strip on the east. Optional later: the `Small town with lab Secondary` tileset (crop plots, windmill) would dress the farm better but is triple-layer (see [waymeet.md](waymeet.md) section 0): **not recommended**.

### Connections

| Edge | Neighbour | Offset | Matching |
|---|---|---|---|
| North | `Lingmoor` south edge | **+3 from Lingmoor's side** (R12's left edge at Lingmoor col 3) | the cleared opening (R12 cols 12-15) meets Lingmoor's farm lane (cols 15-18) |
| South | `Waymeet` north edge | **+10 from Waymeet's side** | R12's opening (cols 11-14) meets Waymeet's lane (cols 21-24) |

**Build effort:** easy.

---

## R18: Hoarfell to Gildhaven (land, Palladium Route 35, 28 x 32): the road under construction

### Description and walk-through

**Opening view from Hoarfell (north).** The player walks up to a **grey gate hut with orange barriers across the road**: a foreman, a works truck, a sign 'ROAD WORKS, RESIDENTS ONLY' and a second, smaller sign: 'GOLDSWORTH ESTATES: building a better you, eventually'. Until the Feather Badge is held, the guard says it is 'closed for resurfacing'. Once the badge is held the barriers and foreman are gone and the road is open. **Opening view from Gildhaven (south).** Always open: the player passes the guard line and sees a **tidy, expensive road**: wide sand, white fences, flower beds, a pond with a neat edge, and nothing out of place except **the tall grass the contractors forgot to trim**.

**Shape and pacing.** A **tree-lined avenue** about 30 tiles, entered at the north-west and leaving at the south-centre. A long fenced sand channel, a broad sand bend, a pond, and a fenced right-hand strip. Pacing is slow and tidy: five trainers, each a 'posh road' preview of Gildhaven.

### Segments (about 5)

| # | Rows | What is there |
|---|---|---|
| 1 | 0-9 | **North gate (guard line).** The render's grey gatehouse (cols 4-9, rows 0-6) is traced as **two flanking huts at cols 4 and 9, rows 0-5** with the road opening **cols 5-8** between them: **barrier objects at (6,5) and (7,5)**, the **guard at (5,5)**, the **foreman at (8,5)** (hidden once the badge is held). Below it a sand approach at cols 5-8, rows 6-9, with **flowers** at (4,6), (4,8), (10,6), (9,7), (11,7) and a **sign (5,7)** ('GILDHAVEN, 1 mile of lawn'). The works truck (`OBJ_EVENT_GFX_TRUCK`) parked at (9,8) |
| 2 | 10-20 | **The fenced sand channel.** A fence col at 5 (rows 10-20) and col 10 (rows 10-15) make a channel at **cols 6-9**, widening at row 16 to a broad sand bend (cols 6-16, rows 16-20). Fence row 16 (cols 10-16) and col 16 (rows 16-29) |
| 3 | 8-23 | **The tall-grass lane (NE).** A hidden green lane at **cols 20-21, rows 0-7** leads to a 2-wide **tall-grass strip at cols 20-21, rows 10-23** and a patch at **cols 12-21, rows 8-9**. The main road does not enter it; the lane is reached by a gap in the pines at (19,8). This is the **wild encounter area** |
| 4 | 21-29 | **The pond.** Pond at **cols 7-10, rows 22-29** (4 x 8), ringed by a low wall; the right sand strip at **cols 11-15, rows 16-30**; **a 1-tile sand islet at (9,25)** (Pearl). Sign **(15,29)** ('GILDHAVEN HARBOUR, ahead') |
| 5 | 30-31 | **South gate (guard line).** The render's lower gatehouse (cols 11-16, rows 30-31) becomes **two flanking huts at cols 11 and 16** with the opening **cols 12-15** (narrow to 3 tiles, cols 13-15, at the last row) and a **guard at (13,30)** who always waves the player through |

**Tall-grass patches to paint:** the render's own (the strip at cols 20-21, rows 10-23, and cols 12-21, rows 8-9). That is enough for the 12-slot table; no extras.

### Trainers (5, as the card, in walking order from Hoarfell)

| Order | Class | Tile, facing, sight | Notes |
|---|---|---|---|
| 1 | Rich Boy | (7,11) south, 4 | in the channel just past the north gate, bored |
| 2 | Lady | (11,8) west, 3 | on the lawn east of the approach |
| 3 | Pokémon Ranger | (8,18) east, 4 | on the broad bend |
| 4 | Parasol Lady | (12,24) west, 3 | by the pond |
| 5 | Cooltrainer | (13,26) north, 4 | south end, a Gildhaven preview (Staraptor 39, Altaria 40) |

Objects: 5 trainers, guards (2), foreman, gardener, jogger, truck, 2 visible items = 14 live (the barrier objects can be tiles, not objects). **NPCs:** the **gardener** (6,13) facing down (waters the same bed, again); the **jogger** (14,22) wandering (has been through the tower three times); the **foreman** (8,5) and **guard** (5,5) at the north gate; the guard (13,30) at the south gate.

### Items (positions)

| Item | Tile | Gate |
|---|---|---|
| Super Potion (visible) | (8,12) in the channel | none |
| Revive (visible) | (12,19) on the bend | none |
| Rare Candy (hidden) | (11,24) at the pond's edge | none |
| Escape Rope (hidden) | (5,13) behind the fence | none |
| Pearl | islet (9,25) | Surf |

### Gate behaviour

- **From Hoarfell:** the guard at (5,5) blocks until `FLAG_BADGE06_GET` (the Feather Badge). Before it: 'closed for resurfacing, courtesy of Goldsworth Estates'. After it: the barriers (6,5),(7,5) and the foreman are hidden, the guard steps aside. **The works are 'finished'** (a one-line change in the sign).
- **From Gildhaven:** the guard (13,30) always lets the player through; the player can walk north to Hoarfell freely, and back, but only the Hoarfell-to-Gildhaven direction is gated.
- Flags (not claimed): `FLAG_R18_GATE_OPEN` (optional, or test `FLAG_BADGE06_GET`), plus hide flags for the barrier, foreman and truck.

### Visual identity

**Tilesets:** ORAS General + `petalburg` (white fences, flower beds) or `mauville`. Roads and fences very clean, pale sand, white fences, red flower beds; orange barrier cones and a hard-hat sign as the only dirty colour. **Weather:** `WEATHER_SUNNY`. **Music:** `MUS_ROUTE101` (bright, tidy). **Silhouettes:** two flat grey huts at each end, a cement-coloured works truck at the north end, Gildhaven's glass spine rising over the south huts as the player approaches.

### Connections

| Edge | Neighbour | Offset | Matching |
|---|---|---|---|
| North | `Hoarfell` south edge | set when Hoarfell is built (about +16: R18's left edge at Hoarfell col 16) | R18's opening (cols 5-8) meets Hoarfell's bottom-centre path |
| South | `Gildhaven` north edge | **+17 from Gildhaven's side** (R18's left edge at Gildhaven col 17) | R18's opening (cols 13-15) meets Gildhaven's north-gate gap (cols 30-32) |

**Build effort:** easy. **Resolved question:** the author confirmed 'under construction, not a toll road'.

---

## R19: Waymeet to Gildhaven (water, vanilla `Route129`, 80 x 40)

### Description and walk-through

**Opening view from Waymeet (east).** The player surfs off the pier into **open, calm water**: a rocky reef to the north-east, a rail viaduct (scenery) overhead near the pier, reed banks, Wingull on the pilings. **Opening view from Gildhaven (west).** The tower is behind the player; ahead, an empty blue sea with a few rock islets and sandbanks and the far shore of Waymeet's canal.

**Shape and pacing.** A wide, sheltered channel, **80 x 40, a mostly open sea with a few reefs** (the vanilla Route 129 layout gives rocky reefs at **cols 4-22, rows 8-13** (a long north-west reef), **cols 46-62, rows 0-13** (a big rock mass at the north-east), and **cols 18-36, rows 24-34** (a south-central reef)). The player surfs west-east along **rows 14-22**, between the reefs. Pacing: a swimmer or sailor every ~10 tiles, with **sandbanks as rest points**. The sandbanks and islets are **painted by the author** (the vanilla map has none).

### Segments (about 5)

| # | Columns | What is there |
|---|---|---|
| 1 | 68-79 | **Waymeet side.** Open water, the **viaduct** (a row of 3 pillars as scenery at cols 70-72, rows 13-24; if bridge tiles are used the player can surf under them), the Waymeet pier directly east of col 79. A **ferryman asleep in a moored boat** at (74,19) |
| 2 | 56-67 | **Reed bank.** **Sandbank 1** at **cols 64-67, rows 17-19** with a single grass tuft; **Max Revive** (visible) at (66,18). The big rock mass at the north-east (cols 46-62, rows 0-13) shades this stretch |
| 3 | 40-55 | **Open water and the lookout.** A **skerry** (the vanilla rock at (47-49, 20-22)) with a **lookout NPC** at (48,19) pointing at the tower; a **pier-sitter** on a pylon at (52,15). **Sandbank 2** at **cols 52-55, rows 25-27** with an **Ultra Ball** (visible) at (54,26) |
| 4 | 20-39 | **The south reef and the buoy line.** The vanilla reef at cols 18-36, rows 24-34 along the south; a **Goldsworth-branded buoy line** ('for guests of the Estate') along row 19 (objects or tiles: a sign each 8 tiles); **Sandbank 3** at **cols 26-29, rows 15-17** with **TM Rain Dance** (visible) at (28,16) |
| 5 | 0-19 | **Gildhaven approach.** Open water, a small reef at cols 4-14, rows 11-13 to the north, and the harbour mouth to the west: R19's west edge rows 14-27 meet Gildhaven's east harbour. A sign 'GILDHAVEN HARBOUR' at (3,19) on a pylon |

### Trainers (7, as the card, walking order from Waymeet)

Swimmers stand **in the water** (facing along the route); Fishermen and Sailors stand on **sandbanks or skerries**.

| Order | Class | Tile, facing, sight | Notes |
|---|---|---|---|
| 1 | Swimmer (male) | (72,16) west, 4 | just off the pier, near Waymeet |
| 2 | Fisherman | (70,19) west, 2 | on the viaduct footing, by the pilings |
| 3 | Sailor | (65,18) west, 3 | on sandbank 1 |
| 4 | Swimmer (female) | (56,17) west, 4 | open water, middle |
| 5 | Sailor | (48,21) north, 3 | at the skerry |
| 6 | Fisherman | (24,16) east, 3 | west end, on a pylon near sandbank 3 |
| 7 | Swimmer (male, toughest) | (10,17) east, 5 | just before Gildhaven |

Objects: 7 trainers, 5 NPCs, 3 visible items = 15. **NPCs:** the **ferryman asleep** (74,19); the **lookout** (48,19); the **pier-sitter** (52,15); two **sandbank islanders** (item holders) at (66,17) and (54,25). **Signs (2):** 'WAYMEET PIER' at (78,19), 'GILDHAVEN HARBOUR' at (3,19).

### Items and Dive spots

| Item | Tile | Gate |
|---|---|---|
| Max Revive (visible) | sandbank 1 (66,18) | Surf |
| Ultra Ball (visible) | sandbank 2 (54,26) | Surf |
| TM Rain Dance (visible) | sandbank 3 (28,16) | Surf |
| Pearl (hidden) | open water (45,17) | Surf |
| Heart Scale (hidden) | by the skerry (50,21) | Surf |
| Stardust (hidden) | north-west reef edge (12,14) | Surf |

**Dive** spots (Dive, badge 9) are for the post-game: the vanilla map has an underwater map `UNDERWATER_ROUTE129` linked by a Dive connection; reuse it or drop the connection. Not listed in the card.

### Visual identity

**Tilesets:** vanilla `gTileset_General` (ORAS recolour) + `gTileset_Mossdeep` (the vanilla set for this map; the LeoB ORAS `mossdeep` secondary is a drop-in and gives bluer water, extend the CREDITS row). **Weather:** `WEATHER_SUNNY` (vanilla's own). **Music:** `MUS_ROUTE119` (vanilla Route 129's tune). **Silhouettes:** the viaduct pillars on the east, the north-east rock mass, Gildhaven's tower from the middle of the channel.

### Connections

| Edge | Neighbour | Offset | Matching |
|---|---|---|---|
| West | `Gildhaven` east edge | R19's top sits at Gildhaven row 12 (offset +12 from Gildhaven's side) | R19 rows 14-27 meet Gildhaven rows 26-39 (water, Surf) |
| East | `Waymeet` west edge | R19's top sits at Waymeet row 3 (offset +3 from Waymeet's side) | R19 rows 14-20 meet Waymeet rows 17-23 |

**Remove vanilla's connections** (it has Up to `Route128`, Left to `Route130` and a Dive link) and add the two above. **Build effort:** medium (large, mostly water; paint 3 sandbanks and the viaduct).

---

## R20: Gildhaven to The Pinnacle (land and cave, Palladium Route 45 + vanilla Victory Road): the gauntlet

### Description and walk-through

**Opening view from Gildhaven (north).** The guard line at the avenue's south end, and beyond it **a narrow sand corridor** between two grey walls of rock under a high sky, a signpost, and the sound of wind. **Opening view from the Pinnacle (south, on the way back).** The summit stair, then the cave's bright exit.

**Shape and pacing.** The longest road, a **climb and a cave**. Part (a): the **surface**, 22 x 91, a long mountain track that winds south-east through **three lanes, a camp, switchbacks, grass shelves and a meadow**, with 7 trainers and the level curve starting at 56. Part (b): the **three cave floors** (the vanilla Victory Road: 1F, B1F, B2F), with 9 trainers and Troglodyte's fight 7 at the very end, in the **top chamber of 1F** next to the exit stair. The road is built to feel heavy: the player has all nine badges, so every trainer is a Cooltrainer, Expert or Dragon Tamer, and none of them is gentle about it.

### Part (a): the surface (22 x 91), segments

Rows below are the render's rows (north = Gildhaven end at row 0).

| # | Rows | What is there |
|---|---|---|
| 1 | 0-9 | **The gate ramp.** A sand corridor at **cols 8-13, rows 0-9** between cliffs. Top: the **guard line** (flanking huts at cols 7 and 14, rows 0-2; the guard at (10,1), the barrier at (11,1); the check is nine badges, see below). Boulders (rock outcrops) at (4,0)-(5,3) and (6,0)-(7,3) west of the corridor. **Sign (10,4)** ('GILDHAVEN' behind, 'THE PINNACLE, nine badges required' ahead; one sign, two lines). A **dark doorway at (2,5)** (a small shed: 'Sign painter's shed', optional interior or decor). The corridor opens at row 6 into the E-W strip |
| 2 | 6-23 | **The Three Lanes.** An E-W sand strip at **rows 6-8, cols 2-15**. Two rock ridges below it (**cols 6-9, rows 8-19** and **cols 12-15, rows 11-21**) split three routes down: the **west lane** (**tall grass at cols 4-5, rows 10-19**, plus 2 x 4 at cols 2-5, rows 16-17), the **centre lane** (**sand at cols 10-11, rows 10-19** with one-way ledges at (10..11, 13) and (10..11, 17), entered by jumping the strip's ledge at **(10..15, 9)**) and the **east lane** (**sand at cols 16-17, rows 12-19** with ledges at (16..17, 13) and (16..17, 19)). **Tall grass** also at cols 12-17, rows 10-11 (a 6 x 2 patch) and cols 10-11, rows 18-19 |
| 3 | 18-30 | **The Camp.** A sand room at **cols 2-7, rows 18-29** (a ledge at row 23 and row 29 cutting it into three steps). A big tall-grass patch at **cols 8-13, rows 20-23**. A **bench (the rest-bench NPCs) at (3,24)**. A side pocket at cols 14-15, rows 22-23 reached from the east lane's bottom. A sand lane at **cols 12-13, rows 24-30** |
| 4 | 30-53 | **The Switchbacks.** Tall grass at cols 10-13, rows 30-33 (4 x 4) and cols 8-9, rows 32-33. A narrow **sand corridor at cols 4-5, rows 34-39** (the narrowest ledge), ending in a ledge at row 41. A plaza at **cols 6-11, rows 34-37**. A lane at **cols 10-13, rows 41-48** with ledges at **row 45** and **row 48** (the card's 'ledges mid-climb'). Tall grass at cols 4-5, rows 42-45 and cols 2-5, rows 46-49. A sand room at **cols 2-15, rows 50-53** with a ledge at row 53 (cols 8-15) |
| 5 | 54-75 | **The Grass Shelves.** Open green: a grass lane at **cols 8-9, rows 54-60** (the narrow part), sand pockets at cols 8-9 rows 58-61 and cols 16-17 rows 58-61, tall grass at **cols 10-15, rows 54-58** and **cols 2-3, rows 56-61**; then green shelves (cols 2-7, rows 66-71; cols 14-17, rows 62-66) with ledges at **row 67** (cols 2-7, 10-13, 14-17), **row 70** (cols 12-13) and **row 75** (cols 0-3, 9-12, 14-17). Tall grass at cols 2-5, rows 64-65, **cols 12-17, rows 68-69** and cols 12-13, rows 72-75. The **small pond** at **cols 12-15, rows 78-81** is segment 6's centrepiece |
| 6 | 76-91 | **The meadow at the foot.** A green meadow at cols 10-17, rows 76-84 around the pond, a stepped ledge at (6..9, 85) and (10..11, 85), grass at cols 4-11, rows 82-87, and the **cave mouth** (a dark doorway tile) at **(7,88)** in the rock row below it (the render ends in rock there: paint the doorway). **Sign (9,86)**: 'THE LONG CLIMB, mind your head' |

**Tall-grass patches to paint:** the render's own (segments above) are enough for the 12-slot surface table; no extras.

**Surface trainers (7, classes, teams and levels as the card).**

| # | Class | Tile, facing, sight | Notes |
|---|---|---|---|
| 1 | Hiker | (11,15) north, 4 | on the centre lane, between its ledges |
| 2 | Black Belt | (17,16) north, 3 | on the east lane |
| 3 | Cooltrainer | (12,43) north, 4 | in the Switchbacks lane (cols 10-13, rows 41-48) |
| 4 | Battle Girl | (4,36) south, 4 | in the narrow corridor (cols 4-5, rows 34-39) |
| 5 | Ruin Maniac | (9,56) east, 3 | on the grass lane |
| 6 | Dragon Tamer | (7,86) south, 2 | at the cave mouth |
| 7 | Psychic | (9,87) west, 2 | beside the cave door |

Objects on the surface map: 7 trainers, 6 NPCs, 3 visible items = 16. **Cut the child with the boulder** or move a trainer into the caves (the card allows the cave guide to share), or leave one NPC as a sign, to hold 15.

**Surface NPCs (6):** the **Pinnacle Gate guard** (10,1); the **cave guide** (a Hiker with a spare torch, gives a Repel once, recommends Flash) at (6,85) beside the cave; two **resting trainers** on the bench at (3,24) and (4,24) (non-battlers: a Cooltrainer who has lost for the third time, a Black Belt stretching); a **child pushing a small boulder** (11,70) ('this is Strength practice'); the **sign painter** at (11,5) touching up 'THE PINNACLE: 1 MILE'.

**Surface items (positions):** Max Elixir (visible) on a surface ledge **(12,46)**; **TM Brick Break** behind a Rock Smash rock in the Camp's east pocket (cols 14-15, rows 22-23): **rock at (14,22), TM at (15,23)**; hidden Ultra Ball **(5,12)** in the west tall grass; hidden Max Ether **(16,15)** on the east lane; hidden Elixir **(8,60)** at the grass lane's end. The cave items follow.

**Gate: nine badges at the Pinnacle Gate guard line** (the guard at (10,1), the barrier across cols 8-13): the script counts badges with `GetBadgeCount()` (CLAUDE.md badge rule), not a flag list. Vanilla's guards test only one flag. Surface wild areas use the card's surface table.

### Part (b): the three cave floors (vanilla `VictoryRoad_1F` 46 x 45, `_B1F` 46 x 31, `_B2F` 46 x 31)

**Rename and place.** Duplicate the three vanilla maps as `VeldrisRoute20_Cave_1F`, `_B1F`, `_B2F` (section PROPOSED: share `MAPSEC_ROUTE_130` with the surface, the card's open question 2). Tileset `gTileset_General` + `gTileset_Cave` (vanilla). **Music `MUS_VICTORY_ROAD`.** `requires_flash` is already set on B1F and B2F (dark with a small light); **Flash is optional** because the caves are crossable in the dark.

**The route through (vanilla's own, confirmed by its warp table):** the surface cave mouth lands on **1F at (15,40)**. Take the stair at **(21,32)** down to **B1F (20,21)**. From B1F take **(17,16)** down to **B2F (19,12)**. On B2F use **(5,26)** up to **B1F (5,26)**, then B1F **(8,3)** up to **1F (9,14)**. Cross 1F east and north to the **exit chamber (rows 3-5, cols 30-40)** and the exit at **(39,5)**, which becomes the warp to The Pinnacle. The other warps ((42,38) to B1F, B1F (30,25) to B2F, B1F (42,2), (42,25)) are the maze's side loops and keep their vanilla targets.

**Cave objects: reuse the vanilla trainer slots, drop the rest.** Vanilla has 16 trainers (5 on 1F, 5 on B1F, 6 on B2F); the card wants 9 plus Troglodyte, so **keep these** and delete the others:

| # | Class and team (card) | Map and tile (vanilla slot) | Facing, sight |
|---|---|---|---|
| 8 | Cooltrainer (Aggron 58, Crobat 58, Medicham 59) | 1F **(27,34)** (Albert's slot) | down-and-right, 3: first on 1F, between the entrance and the stair (21,32) |
| 9 | Expert (Hariyama 58, Machamp 59) | 1F **(33,22)** (Edgar's slot) | down, 3: in the room south of the exit corridor |
| 10 | Hex Maniac (Dusknoir 58, Sableye 59) | 1F **(6,15)** (Hope's slot) | left, 4: in the top-left room where B1F's (8,3) stair arrives at (9,14) |
| 11 | Dragon Tamer (Haxorus 59, Flygon 59) | B1F **(37,12)** (Samuel's slot) | left, 3: the pit-edge path in the east |
| 12 | Psychic (Claydol 59, Alakazam 60) | B1F **(14,16)** (Mitchell's slot) | down, 4: the dark room at the west |
| 13 | Cooltrainer (Bisharp 59, Probopass 60, Mawile 59) | B1F **(14,20)** (Halle's slot) | up-and-right, 3: at the stair (17,16) |
| 14 | Black Belt (Hariyama 60, Machamp 60) | B2F **(43,14)** (Owen's slot) | up, 4: the corridor under the exit stair (43,2) |
| 15 | Expert (Rhyperior 60, Steelix 60) | B2F **(25,21)** (Felix's slot) | up, 2: corridor |
| 16 | Ruin Maniac (Golem 60, Probopass 61, Claydol 61) | B2F **(35,22)** (Julie's slot) | left, 2: the toughest |

**Delete (vanilla slots not used):** 1F Katelynn (29,17), Quincy (32,17), Wally objects (12,25), (31,9); B1F Shannon (26,16), Michelle (5,21); B2F Vito (15,6), Caroline (2,17), Dianne (25,18). **The vanilla Strength boulders and Rock Smash rocks on B1F stay** (7 boulders, 6 rocks): they are the puzzle, and the card wants Strength mandatory in the cave (**check that the route above does not need a boulder pushed**: vanilla's path does use some; the card's 'boulder corridor' trainer slot moves to 1F because 1F has no boulders).

**Re-point the vanilla items** (positions are vanilla's): 1F (40,26) **Max Revive**, 1F (37,39) **Rare Candy**, hidden 1F (30,39) Ultra Ball (keep); B1F (32,3) **PP Max** (behind the boulders at (34,4) and the rock (34,3)), B1F (42,8) **Full Restore**, B2F (13,8) Full Heal (keep, or swap for Max Ether), hidden B2F (28,5) Elixir, hidden B2F (37,1) Max Ether (re-labelled from Max Repel). That puts the card's list (Max Revive, Full Restore, Rare Candy, PP Max visible; Ultra Ball, Max Ether, Elixir hidden) on the vanilla item tiles.

### Troglodyte, fight 7 (the Work phase): the exit chamber on 1F

**Place.** The **chamber at the top of 1F** (rows 3-5, cols 30-40, the exit at (39,5)). The corridor into it runs **north from (30..32, 12) up to (30..32, 6)** (3 wide). Troglodyte stands in the chamber at **(35,4) facing west**. **Trigger:** `coord_event` tiles at **(30,6), (31,6), (32,6)** on the corridor mouth (CLAUDE.md: a trigger, not `OnTransition`; the elevation must match the tile: vanilla Wally's triggers use elevation 4 on 1F). He walks from (35,4) to (31,5) and speaks. **Team:** Stoutland 'Sir Biscuit' 55, Vaporeon 55, Gardevoir 56, Pyroar 56, Tyranitar 56, plus one stage-3 starter at 57 (Party Size 6, `Pool Prune: Rival Starter`; [../../troglodyte-arc.md](../../troglodyte-arc.md); no Garchomp). **Behaviour:** stiff, no jokes ('Fight me. Properly. Please.'). After the fight he stands aside; the exit (39,5) is the next warp. Flags (not claimed): `TRAINER_TROGLODYTE_VICTORY_ROAD` alias, `VAR_R20_TROG_STATE`.

### Visual identity (R20)

**Tilesets:** surface ORAS General + `fallarbor` (rock) so it matches Cragdale and R10 (or the vanilla `gTileset_General` + `gTileset_Rustboro` cliff set); caves vanilla `gTileset_Cave`. **Weather:** `WEATHER_NONE` on the surface (a stern, still sky), none in the caves. **Music:** surface `MUS_MT_CHIMNEY` (tense mountain), caves `MUS_VICTORY_ROAD`. **Silhouettes:** tall rock walls on both sides of the corridor, the Pinnacle's dome far ahead in the last meadow shot.

### Connections (R20)

| Edge | Neighbour | Offset | Matching |
|---|---|---|---|
| North | `Gildhaven` south edge | **+21 from Gildhaven's side** (R20's left edge at Gildhaven col 21) | R20's sand mouth (cols 8-13) meets the avenue gap (cols 29-33) |
| Cave mouth | warp (7,88) to `VeldrisRoute20_Cave_1F` (15,40) | | the cave's first warp |
| Cave exit | `VeldrisRoute20_Cave_1F` (39,5) to `ThePinnacle` (13,2) | | arrives at the exterior's north landing (see [pinnacle-detail.md](pinnacle-detail.md)) |

**Build effort:** hard. A 22 x 91 outdoor map plus three duplicated vanilla caves, 16 trainers (9 on slots that already exist), one scripted fight.

---

## R21: The Pinnacle to Vesperhaven (land, post-league, Palladium Route 46, 22 x 36)

### Description and walk-through

**Opening view from the Pinnacle (north).** The iron gate at the plateau's south wall opens (after the Hall of Fame) onto **wind**: a cliff-top path, grassy shelves stepped down between rock walls, a view of the sea beyond. **Opening view from Vesperhaven (south).** A sand landing and a sign, a dark doorway high above, and a path climbing between ledges to the League.

**Shape and pacing.** A **cliff-top descent**, north to south, 22 x 36. A top shelf, a mid shelf, a rock-lined stretch, tall-grass fields and the sandy landing at the foot. Six 'League graduate' trainers, a tall-grass band, and **one dead-end doorway** at the top. Post-game, so the player is strong and the road is a victory lap with a few hard fights.

### Segments (about 5)

| # | Rows | What is there |
|---|---|---|
| 1 | 0-9 | **The top shelf.** The render has rock rows 0-3 across the top: **carve the opening at cols 8-12, rows 0-3** to meet the Pinnacle's south wall gap. A green shelf at **cols 8-12, rows 4-9**. The **dark doorway (locked cellar) at (16,5)** in the cliff to the east, reached by the ledge-bounded pocket at cols 14-20, rows 5-8. A pocket at **(20..21, 4)** (Max Revive) |
| 2 | 10-14 | **The mid shelf.** The central rock block at **cols 6-13, rows 8-11**; a green shelf at **cols 2-9, rows 12-14** and a corridor at cols 10-13, rows 10-15; a ledge at **(14..17, 11)** and a short ledge at (14..17, 13). A **post** at (10,13) |
| 3 | 15-22 | **The rock stretch.** The second rock block at **cols 8-11, rows 14-19**; green corridors on both sides (cols 2-7 and cols 12-15, rows 15-19); a right-hand mass at cols 16-21, rows 17-27 (impassable). A west pocket at **cols 2-4, rows 13-16** (Full Restore) |
| 4 | 20-27 | **The tall-grass fields.** Tall grass at **cols 4-7, rows 20-24**, a band at **cols 6-15, rows 24-25**, and pockets at cols 6-7 rows 26-27, cols 12-15 rows 26-27, cols 14-15 rows 28-29. **Sign (11,27)** ('VESPERHAVEN, hidden coast') |
| 5 | 28-35 | **The sandy landing.** Sand at **cols 8-13, rows 28-33** (a wide plaza), flanked by pines; the render's grey gate at (8-13, 34-35) is dropped (Vesperhaven's own gate stands there): the road runs off the south edge at cols 8-13 into Vesperhaven |

**Tall-grass patches to paint:** the render's own fields (segment 4) are enough for the 12-slot table.

### Trainers (6, as the card, in walking order from the Pinnacle)

| Order | Class | Tile, facing, sight | Notes |
|---|---|---|---|
| 1 | Cooltrainer | (10,6) south, 4 | top shelf |
| 2 | Cooltrainer | (5,13) east, 4 | mid shelf, west |
| 3 | Expert | (15,12) west, 3 | on the ledge shelf |
| 4 | Black Belt | (12,17) south, 3 | the rock stretch corridor |
| 5 | Dragon Tamer | (9,25) south, 4 | the tall-grass band, toughest, near the foot |
| 6 | Pokémon Ranger | (11,30) north, 4 | on the sandy landing (the last fight) |

Objects: 6 trainers, 5 NPCs, 4 visible items = 15. **NPCs (5):** the **League guard** (10,3) at the north opening (lets the player through once the Hall of Fame is done; stands in the gap before then, and the Pinnacle-side gate shuts); the **sign painter** (9,8) with the already-updated 'champions of the region' sign; a **retired Elite Four fan with a flag** (12,16); a **surveyor with an orange stake** (4,22) ('Estates are still thinking about this one', a Goldsworth nod); a **rest-bench trainer** (13,29) on a bench at (13,30).

### Items (positions)

| Item | Tile | Gate |
|---|---|---|
| Max Revive | (20,4) pocket | none |
| Full Restore | (3,15) west pocket | none |
| Rare Candy x2 | (14,15) corridor and (7,22) behind the fields | none |
| Max Elixir (hidden) | (6,21) | none |
| PP Max (hidden) | (19,24) | none |
| Cellar gift cache (optional) | behind the dark doorway (16,5) | a late post-game flag, PROPOSED |

### Visual identity

**Tilesets:** ORAS General + `ever_grande` (the same set as the Pinnacle, drop-in dual-layer; folder `LeoB ORAS/tilesets/secondary/ever_grande/`, extend the CREDITS row) for the rock, or `fallarbor`. **Weather:** `WEATHER_SUNNY`. **Music:** `MUS_ROUTE122` (sea air). **Silhouettes:** the sea at the bottom edge, the League's dome behind the player as they descend.

### Connections

| Edge | Neighbour | Offset | Matching |
|---|---|---|---|
| North | `ThePinnacle` south edge | **+4 from the Pinnacle's side** (R21's left edge at Pinnacle col 4) | R21's carved opening (cols 8-12) meets the Pinnacle's iron-gate gap (cols 12-15 and the gate at the wall); shut until `FLAG_SYS_GAME_CLEAR` |
| South | `Vesperhaven` north edge | set when Vesperhaven is built | R21's landing (cols 8-13) |

**Gate:** `FLAG_SYS_GAME_CLEAR`. **Build effort:** medium. **Goldsworth beat:** the surveyor's stake.

---

## Open questions

1. **Reused Palladium renders.** R10 here and R13 ([../routes-east.md](../routes-east.md)) and R6 ([../routes-west.md](../routes-west.md)) all use Route 42; R11 and R6 both use Route 44; R18 here and R9 both use Route 35. Tracing the same picture three times will look repetitive. Easiest fix: **mirror and re-dress** (flip left-right, change the pond shapes, swap trees for rock). Alternatively use renders that no card claims (Route 29, 30, 31, 32, 33 and 37 are unassigned in this group's reading, **check the other groups first**).
2. **Gates as guard lines, not interiors.** Decided here because Gen 3 doors face south only. If the author wants a gatehouse interior anywhere, it must be entered from its south side.
3. **Cave floors for the road.** The vanilla Victory Road enters on 1F, returns to 1F and exits there; the card says 'the cave's last floor exits'. This document keeps vanilla's routing and puts Troglodyte on **1F**, not B2F.
4. **R20 surface has 7 trainers + 6 NPCs + 3 items = 16 live objects.** One has to go (a hidden item or the boulder child).
5. **R11 and R10 east exits** need a rock cut. Confirm the author is happy to cut through the render's rock edge, or shorten the maps so the road ends on open ground.
6. **R19 viaduct.** The vanilla map has no bridge; a bridge the player surfs under needs the right metatiles (vanilla Route 122/Cycling Road have them). If not, use plain pilings.
7. **Tall grass on sand.** The renders are mostly grass and sand; encounters need tall grass. The patches above are PROPOSED.
