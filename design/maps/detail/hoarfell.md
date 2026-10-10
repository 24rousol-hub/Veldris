# HOARFELL: detailed design (city, place 7, gym 5 Ice, gives Surf)

Status: **PROPOSED** (written 2026-10-01). Nothing here is built. It adds detail to the card [../towns/hoarfell.md](../towns/hoarfell.md) and does not change its facts (species, levels, trainer lists, items, flags). Choices I had to make are marked **PROPOSED**; render-versus-card conflicts are marked **FIX**. Sources I used: the card, [../interiors/README.md](../interiors/README.md), [../interiors/catalogue.md](../interiors/catalogue.md), the Hollowbrook interiors in [../../interiors.md](../../interiors.md) (house style), the Palladium renders `blacthorncity.png` (the town) and `Mahogany Town Gym.png` (the gym), the vanilla layouts and tilesets in this tree, and the Team Aqua tilesets named below. Gym: [../../gyms.md](../../gyms.md), leader WAKASAGI ([../../leader-names.md](../../leader-names.md), [../../trainer-roster.md](../../trainer-roster.md)). Scheme 5 and Troglodyte fight 4: [../../troglodyte-arc.md](../../troglodyte-arc.md). Goldsworth houses: [../../goldsworth.md](../../goldsworth.md). Roads: [routes-west-b.md](routes-west-b.md). Ice cave: [landmarks-west-detail.md](landmarks-west-detail.md).

**Coordinates.** Every `(x, y)` is a tile, x from the left, y from the top, 0-based. Outdoor positions are read by eye from the render (`blacthorncity.png` is 737 x 703 px with no grid, so about **46 x 44** tiles at 16 px; the card says 46 x 43, the picture is 44 rows tall) and **can be 1 or 2 tiles off**: treat them as 'about here'. Interior coordinates are mine and exact; the gym grid was **checked by a throwaway solver** (it finds the solution and proves it is the only shortest one).

## At a glance

| Item | Value |
|---|---|
| Outdoor map | `Hoarfell`, 46 x 44. Size check (46 + 15) * (44 + 14) = 3,538 of 10,240 |
| Section | new `MAPSEC_HOARFELL` (interiors and the cave share it, or the cave gets `MAPSEC_HOARFELL_CAVE`, see Open questions). Fly point and heal location: yes |
| Tilesets (outdoors) | Plan A: **new primary `gTileset_GeneralSnow`** (Team Aqua `Emerald Slide`) + secondary `gTileset_Rustboro`. Plan B: `gTileset_General` + `gTileset_Rustboro` and `WEATHER_SNOW` |
| Weather | `WEATHER_SNOW` (the constant exists, 'unused' in vanilla but compiled; **test it**) |
| Music (existing Hoenn track, PROPOSED) | `MUS_SOOTOPOLIS` outside (calm and cold), `MUS_GYM` in the gym |
| Connections | **west** edge to R6 (a gap cut at y 31 to 33), **east** edge to R10 (a gap cut at y 27 to 29), **south** edge to R18 (x 12 to 16, closed until the Feather Badge). The two cave doors are warps |
| Interiors | Center 1F and 2F, Mart, gym, 2 houses, the Goldsworth house = 7 maps, plus the cave (4 maps, other file) |
| Objects outdoors | at most 15 during Scheme 5 (limit 15, tight): see NPCs |
| Level at arrival and departure | about 33 and about 37 |

## 1. Description

**First glance, from R6 (the west).** A cliff stair brings you up onto a ledge and the town opens below you in a bowl of brown rock: a **big lake** at the top with a **grey gym standing on its south shore with its feet in the water**, a snow-dusted lawn, two tiny dark doors in the cliffs (the Ice cave), smoke rising from three grey-roofed houses and the red roof of the Center. A thin white powder blows along the sand. Everything is the colour of slate and tea.

**First glance, from R10 (the east).** You come in along a dirt path, the east house (with the best view and the worst taste) on your left and the cliffs on your right; a dirt path runs up the cliff to the north-east shelf.

**Mood.** Cold, practical, tea-warm. Everyone has a thermos. The lake is the heart: old fishermen, a surveyor, a hole in the ice.

**Colour.** Slate-brown rock, white snow, ice-blue water, soot-grey roofs, one red roof (the Center) and one blue (the Mart), the gold of the gym roof.

**Sound.** Wind, a gentle track, distant ice creak (an optional sound effect).

**Time of day.** Permanent grey dawn (snow weather does the work).

**The memorable view.** From the north-east shelf, looking down on the whole bowl: the lake, the gym, the town, the cliff stair you came up.

## 2. Street layout in words (a numbered walk)

Tile positions are the render's (about). North is up.

1. **The west entrance (R6).** The render's left side is solid rock; the sign at (8, 30) and a sand patch at x 5 to 10, y 29 to 39 are all that is open. **PROPOSED:** cut a **3-tile-high gap at x 0 to 5, y 31 to 33** through the rock to the west edge; R6's east sand (y 7 to 9) joins it. The sign at (8, 30): `HOARFELL. SNOW, CLIFF AND TEA. IN THAT ORDER` (the town sign, card). The skier kid stands here.
2. **The south half: the sand ground.** A wide dirt-and-sand floor x 6 to 40, y 22 to 43. The **Pokémon Center** (red roof) at x 23 to 27, y 32 to 35, **door (25, 35)**, arrival (25, 36). The **Mart** (blue roof) at x 17 to 20, y 33 to 35, **door (19, 35)**, arrival (19, 36). South-west **House B** at x 10 to 14, y 36 to 38, **door (12, 38)**, arrival (12, 39). Rocks (tile rocks) scattered at (6, 32), (31, 33), (40, 33), (33, 37), (6, 41), (8, 43), (10, 43), (20, 41).
3. **The south exit (R18).** The sand reaches the bottom edge at x 7 to 19 between big rocks at (8, 43) and (10, 43). **PROPOSED:** the opening is **x 12 to 16, y 43**, 5 wide. Until the Feather Badge it is **closed** (see Items and secrets / Flags): a `coord_event` row on y 42 turns the player back with 'R18 IS UNDER CONSTRUCTION. THE ROAD WORKS ARE NOT OURS' (decided, [../index.md](../index.md): not a toll road).
4. **The west lawn and House A.** The grey-roofed **House A** (WAKASAGI's hut) at x 15 to 19, y 24 to 26, **door (17, 26)**, arrival (17, 27). Rocks flank it at (10, 22) and (12, 22). The boy with a flask stands beside it at (14, 27).
5. **The middle block.** A raised rock block at **x 21 to 28, y 20 to 24** in the middle of the lawn with dirt paths round it; the Strength puzzle nook on its east side (item 9).
6. **The east house (the Goldsworth house).** At **x 32 to 36, y 26 to 28, door (34, 28)**, arrival (34, 29). A sign at (31, 29): `Goldsworth_Text_HouseSign`. An east lane runs from it to the east edge.
7. **The lake.** The big rectangular lake at **x 15 to 29, y 8 to 18**, ice-white in the snow palette. The top part narrows (x 21 to 27, y 8 to 9). The **gym** stands in it: **x 19 to 25, y 12 to 15, door (22, 15)**, arrival (22, 16). Left of the gym the lake is x 15 to 18, right of it x 26 to 29. Two rocks flank the top cave door at (22, 7) and (27, 7).
8. **The lawn south of the lake,** x 13 to 30, y 16 to 21. The lake sign at (21, 18): `FISHING PERMITTED. FOR NOW`. The gym sign at (20, 19): `HOARFELL ICE GYM. LEADER: WAKASAGI. MIND THE ICE. IT MINDS YOU`. The old angler's **fishing hole** (a `bg_event`) at (26, 16) by the gym's east wall. A **pier** (wooden bridge tiles) from (27, 17) north to (27, 10) and a 3 x 3 platform at x 26 to 28, y 9 to 11 for Scheme 5's drill rig (see section 6).
9. **The middle block's nook (HYPER POTION).** A 2 x 2 nook at **x 30 to 31, y 23 to 24** on the block's east side, with a **Strength boulder at (30, 24)** and the HYPER POTION at **(31, 24)**; the entrance is (30, 25). The player pushes the boulder **north** from (30, 25) to (30, 23); (30, 24) is then clear and the item is one step east. Needs a free (30, 23).
10. **The top cave door.** At **(24, 5)**, in a small green meadow at x 21 to 28, y 6 to 8 at the top of the lake. Reached by a **dirt path along the lake's east shore** (PROPOSED: paint a 2-wide path from the lawn up x 30 to 31, y 9 to 18, then west along y 6 to 8). This is the Ice cave's main entrance.
11. **The north-east shelf.** A green shelf at **x 39 to 43, y 12 to 19** with the second cave door at **(41, 12)**, reached by a dirt path from the east side: x 37 to 43, y 19 to 25 (the render's path) up the cliff. NEVER-MELT ICE visible at (42, 14). This is the Ice cave's far exit.
12. **The cliffs.** The render's rock walls fill the rest of the frame (up to 12 tiles thick in the north-west and south-east). The long ledge lines along them are decoration.
13. **The east edge (R10).** **PROPOSED:** cut a **3-tile gap at x 41 to 45, y 27 to 29** through the rock east of the east house; R10's west edge joins it. A sign at (39, 30): `HOARFELL. EAST: CRAGDALE. IT IS LONG. IT IS WINDY`. The hiker stands at (38, 28).

Water: the lake (Surf only after badge 5). Ledges: decorative. Trees: none (rock bowl).

## 3. Every building

Map names are PROPOSED (group `gMapGroup_IndoorVeldris`, section `MAPSEC_HOARFELL`). **Kit** means the Hollowbrook furniture vocabulary (copy blocks from the built maps in Porymap): `Hollowbrook_NeighboursHouse` (11 x 8): kitchen x 0 to 3, y 1 to 2; window pair x 5 to 6, y 0 to 1; bookshelf x 7 to 8, y 1 to 2; TV table with cushions x 5 to 8, y 4 to 6; plant column x 10, y 4 to 6; exit mat (2, 7). `Hollowbrook_PlayersHouse_2F` (13 x 8): bed x 1 to 2, y 1 to 3; PC desk x 4 to 5, y 1 to 3; TV stand x 9 to 10, y 1 to 3; 3 x 3 rug x 5 to 7, y 4 to 6; plants (0, 5 to 6), (12, 5 to 6).

| Building | Map | Layout and tileset | Size | Palladium image | Notes |
|---|---|---|---|---|---|
| Pokémon Center 1F, 2F | `Hoarfell_PokemonCenter_1F`, `_2F` | **vanilla** `LAYOUT_POKEMON_CENTER_1F`, `_2F` | 14 x 9, 14 x 10 | `newcenter.png` as reference only | shared |
| Mart | `Hoarfell_Mart` | **vanilla** `LAYOUT_MART` | 11 x 8 | none | shared |
| Gym | `Hoarfell_Gym` | custom: `gTileset_General` + `gTileset_Cave` (the Shoal Cave ice pair) | 15 x 23 | `Mahogany Town Gym.png` | slide puzzle |
| House A (hut) | `Hoarfell_HouseA` | Gen 4 Interior, or Team Aqua **Legend of Zelda House Secondary** (a fishing hut) | 11 x 8 | `Elm's House.png` | WAKASAGI's hut |
| House B | `Hoarfell_HouseB` | Gen 4 Interior | 11 x 8 | `Elm's House.png` | skier family |
| Goldsworth house | `Hoarfell_GoldsworthHouse` | Gen 4 Interior, the **shared Goldsworth layout** | 13 x 10 | `President's Office Tiled.PNG` for the rich feel | NPC only, no trainers |
| Ice cave, 4 floors | `HoarfellIceCave_*` | see [landmarks-west-detail.md](landmarks-west-detail.md) | | | optional |

### 3.1 `Hoarfell_PokemonCenter_1F` and `_2F` (vanilla)

`LAYOUT_POKEMON_CENTER_1F` (14 x 9): nurse at (7, 2) facing down (the **first object**), door pair (6, 8) and (7, 8), stairs warp (1, 6). 2F: 14 x 10. **Never move the nurse or counters** (rule 2). NPCs: the vanilla gentleman at (4, 4) is the **mountaineer** ('Surf is not allowed on the frozen lake before the Leader is beaten. Sorry'); the boy at (10, 6) a **gym fan**; the girl at (3, 7) vanilla's. Warps: (6, 8) and (7, 8) to `Hoarfell` warp 0.

### 3.2 `Hoarfell_Mart` (vanilla)

`LAYOUT_MART` (11 x 8): clerk at (1, 3) facing right, door pair (3, 7) and (4, 7), woman at (5, 5), boy at (9, 4). Stock (card): GREAT BALL, **ULTRA BALL (first one here)**, SUPER POTION, ICE HEAL, HYPER POTION, REPEL, SUPER REPEL. Warps: (3, 7) and (4, 7) to `Hoarfell` warp 1.

### 3.3 `Hoarfell_Gym`: see section 5

### 3.4 `Hoarfell_HouseA` (11 x 8): WAKASAGI's hut

Thermos, spare rods, a hole in the floor for the fire. **Default (Gen 4 Interior):** kitchen top-left (the stove is the 'thermos stove'), window pair x 5 to 6, a **rod rack** (the bookshelf block at x 7 to 8, y 1 to 2), a low table with two cushions at x 4 to 5, y 4 to 5, plant column, mat (2, 7). **Upgrade (Zelda House):** the same room in timber and stone, with the hearth at (8, 1) and four pots in a row; the same tileset serves Gloomsby's Old Tower and Mothwood's lodge (see [gloomsby.md](gloomsby.md), [landmarks-west-detail.md](landmarks-west-detail.md)), so one import and one credit row cover three buildings. NPC (1): **WAKASAGI's grandson** (the boy with a flask) at (5, 4) facing east: thermos hints for the gym ('Up the middle, then left, then up. Do not look down.'). Warps: (2, 7) to `Hoarfell` warp 3, landing (17, 27).

### 3.5 `Hoarfell_HouseB` (11 x 8): the skier family

Kit: kitchen top-left, window, bookshelf, TV table at x 5 to 8, y 4 to 6, plant column, mat (2, 7), and a **pair of skis** (a plant block at (9, 3) reads fine) leaning by the door. NPCs (2): the **mother** at (5, 5) facing north, and the **skier kid's father** at (8, 3) facing south, who gives an **ICE HEAL** (card). Warps: (2, 7) to `Hoarfell` warp 4, landing (12, 39).

### 3.6 `Hoarfell_GoldsworthHouse` (13 x 10): the second Goldsworth house

**Use the shared Goldsworth layout** already specified in [briarwick.md](briarwick.md) section 3.5 (13 x 10, Gen 4 Interior, cold and tidy: trophy cabinets at x 1 to 2 and x 10 to 11, a TV at x 5 to 6, two armchairs each side, a 3 x 5 rug, plants at the front corners, door mat **(6, 9)**). In Porymap make this map with **Add New Map with Layout** on that layout (painting once changes every Goldsworth house). If the layout differs when it is built, shift the positions below.
- **NPCs (4, NPC only, no trainers, no ids; Briarwick's slots reused):** the **butler** at (6, 7) facing down (`ButlerDoor`-style: rules and a sniff); **PRESCOTT** (wine snob) at (3, 6) facing up beside the left armchair: before Scheme 5 'a bottle of 1984, wasted on you', after 'has to pay for his own dinner'; **BIFF** (gym rat) at (9, 6) facing up beside the right armchair, flexing at the glass of the trophy cabinet: before 'flexes in the mirror', after 'even his form is better than Beau's'; **WINSTON** (phone talker) at (10, 3) facing down: before 'tries to buy the lake', after 'the lake was not for sale'. Names from [../../goldsworth.md](../../goldsworth.md); no cousin is repeated from Briarwick (BARNABY, a lounger, KIP and DUCHESS are there). Swearing is mild and only in this house (author rule). Before/after switches on `FLAG_HOARFELL_SCHEME_DONE`.
- **Sign** outside at (31, 29): `Goldsworth_Text_HouseSign`.
- **Warps:** (6, 9) to `Hoarfell` warp 5, landing (34, 29).

## 4. Door and warp table

Outdoor `Hoarfell` warps (id: tile, destination). Exit warps land on the arrival tile.

| id | Tile | Destination | Arrival after exiting |
|---|---|---|---|
| 0 | (25, 35), Center | `Hoarfell_PokemonCenter_1F` (6 and 7, 8) | (25, 36) = **the heal location tile** |
| 1 | (19, 35), Mart | `Hoarfell_Mart` (3 and 4, 7) | (19, 36) |
| 2 | (22, 15), gym | `Hoarfell_Gym` (7, 22) | (22, 16) |
| 3 | (17, 26), House A | `Hoarfell_HouseA` (2, 7) | (17, 27) |
| 4 | (12, 38), House B | `Hoarfell_HouseB` (2, 7) | (12, 39) |
| 5 | (34, 28), Goldsworth house | `Hoarfell_GoldsworthHouse` (6, 9) | (34, 29) |
| 6 | (24, 5), top cave door | `HoarfellIceCave_1F` (6, 21) | (24, 6) |
| 7 | (41, 12), north-east cave door | `HoarfellIceCave_1F` (38, 29) | (41, 13) |

Edges: **west** edge (y 31 to 33) to `Route6` (east edge, its y 7 to 9); **east** edge (y 27 to 29) to `Route10` (west edge); **south** edge (x 12 to 16) to `Route18` (north edge), blocked by script until `FLAG_BADGE06_GET`.

## 5. The gym (ICE, WAKASAGI, FROST BADGE)

**`Hoarfell_Gym`, 15 x 23.** Built from `Mahogany Town Gym.png` (224 x 368 px with no grid, so 14 x 23 at 16 px; I make it **15 wide** so the ice floor is 11 wide and the leader's alcove is centred). The render: a hall of slippery ice with snow-capped boulders along the walls and scattered in the floor, grey **snow patches** that are not slippery, a purple entry carpet with two Poké Ball statues at the bottom, a snow-bank wall at the top with the leader's spot.

**Tilesets: primary `gTileset_General`, secondary `gTileset_Cave`.** This is the pair Shoal Cave's ice room uses (`ShoalCave_LowTideIceRoom_Layout`, 20 x 30): I checked `data/tilesets/secondary/cave/metatile_attributes.bin`: **metatile index 397 (id 909 in map data) has the behaviour `MB_ICE`**, which makes the player slide, and vanilla's ice room proves it works. Open that map in Porymap and copy its ice blocks, its rock-wall blocks and its snow patch. Boulders are the cave's rock blocks (collision 1). **No import, no credit row beyond Palladium.** Set the map type to indoor. The gym becomes 'an ice hall carved in the lake': stone-and-ice, not a building interior, which suits the card ('the gym stands in the lake').
**Optional prettier floor:** the FRLG `gTileset_General_Frlg` + `gTileset_SeafoamIslands` pair has 10 `MB_ICE` metatiles and blue ice walls, but I have **not** verified it renders in an Emerald-region map (the FRLG maps are not built into this ROM).

### The floor, tile by tile

Legend (x 0 to 14 across, y 0 to 22 down): `#` wall, `b` the snow bank (impassable decor), `B` an **ice boulder** (impassable), `.` **ice** (slippery), `s` a **snow patch** (a stop: you stop when you enter it and can step off it normally), `S` the start patch, `G` the goal patch, `L` WAKASAGI, `c` the purple entry carpet (not slippery), `a` a Poké Ball statue (`bg_event`), `m` the exit mat.

```
x     0         1
      012345678901234
y  0  ###############
y  1  ###############   (an emblem on the wall at (7, 1))
y  2  ###############
y  3  ##bbbbbbbbbbb##
y  4  ##bbbbbLbbbbb##   WAKASAGI at (7, 4), in an alcove
y  5  ##....BGB....##   G = (7, 5), the goal patch in front of him
y  6  ##.B.B..BB.B.##
y  7  ##...........##
y  8  ##B..B......B##
y  9  ##.....B..B..##
y 10  ##.......B.BB##
y 11  ##B..BB......##
y 12  ##B.........B##
y 13  ##B.....B...B##
y 14  ##B.s.B.....B##
y 15  ##B..s......B##
y 16  ##Bs.B.sBs...##
y 17  ##B..B.S.B..B##   S = (7, 17), the start patch
y 18  ##..ccccccc..##
y 19  ##..ccccccc..##
y 20  ##..cacccac..##   statues at (5, 20) and (9, 20)
y 21  ##..ccccccc..##
y 22  #######m#######   the exit mat at (7, 22)
```

**How sliding works here.** The player moves one step onto an ice tile and then keeps going in that direction until the **next tile is blocked** (a boulder or wall) or until they step onto a **snow patch** `s`. The solver found **50 spots the player can stop on**, so there are many dead ends; none traps the player (from any stop a slide returns to a patch or the start). The leader's alcove is closed on both sides with the snow bank, so the player **cannot walk round the puzzle**: only the goal patch (7, 5) touches the leader at (7, 4).

**The solution, 8 moves, the only shortest one:** from S (7, 17):
1. **north** (one step onto the patch (7, 16), a stop);
2. **north** (slides up x 7 until the boulder at (7, 9) stops you at **(7, 10)**);
3. **west** (slides along y 10 to **(2, 10)**, the wall);
4. **north** (slides up x 2 until the boulder at (2, 8) stops you at **(2, 9)**);
5. **east** (slides along y 9 until the boulder at (7, 9) stops you at **(6, 9)**);
6. **north** (slides up x 6 until the boulder at (6, 5) stops you at **(6, 6)**);
7. **east** (slides along y 6 until the boulder at (8, 6) stops you at **(7, 6)**);
8. **north** to **G (7, 5)**, a patch: you stop. WAKASAGI is at (7, 4), facing south. Talk.

(Moves 1 and 8 are single steps on non-ice.) The coordinates above use the drawn grid: the picture's boulders are at the `B` cells and nowhere else.

### Gym trainers (3, from the card, positions PROPOSED)

| Class | Team | Stands at | Faces | Sight | Notes |
|---|---|---|---|---|---|
| Fisherman | SPHEAL 31, SEEL 32 | (6, 16), an ice tile next to the start | east | 2 | sees the first stop (7, 16), one tile away: **the first fight, unavoidable** |
| Hiker | SWINUB 31, SNORUNT 32 | (5, 15), a patch | east | 3 | sees (6, 15), (7, 15), (8, 15): optional unless the player stops there |
| Lass | VANILLITE 32, CUBCHOO 33 | (3, 16), a patch | north | 5 | sees the x 3 lane (3, 11 to 15): optional |

(Levels 31 to 33 are three to four below WAKASAGI's lowest of 35, as the rule says.) The Hiker and the Lass stand on **patches**; the Fisherman stands on one ice tile, (6, 16), that the solution never slides through. **I re-ran the solver with all three trainers as obstacles: the answer is still 8 moves and still the only shortest one** (45 stops remain). **Test in the game** whether a trainer notices a sliding player: if not, add a `coord_event` on the stop tile in front of him that starts the fight (the standard pattern), and use one on (7, 10) and (6, 9) if the author wants all three forced.

**Hints (PROPOSED).** The Fisherman, after the fight: 'Straight up to the big rock. Then west. Then up. Then east...' (the first four moves). The Hiker: 'Left wall, up, then right. Mind the rock.' The Lass: 'Near the top, go east then up. It is only a nudge.' The grandson in House A: 'Up the middle, then left, then up. Do not look down.'

**Objects:** WAKASAGI, 3 trainers = 4. Limit 15: fine. Guide statues are `bg_event`s at (5, 20) and (9, 20) (the joke about not slipping).

### Scripts and flags for the gym

- No `OnTransition` needed (the ice is a tile behaviour). The goal is just WAKASAGI's dialogue.
- WAKASAGI: the leader pattern copied from `data/maps/RustboroCity_Gym/scripts.inc` (without its rematch branch, see CLAUDE.md); reward badge 5, **HM Surf**, TM Ice Beam; `FLAG_BADGE05_GET`, `FLAG_RECEIVED_HM_SURF` reused.
- Optional: a `coord_event` at the entrance carpet (7, 18) that tells first-time players 'ICE! WALK ON IT AND YOU GLIDE'.

## 6. Scheme 5 and Troglodyte fight 4 (outdoor staging)

All positions are on `Hoarfell` and PROPOSED. The scene uses a **`coord_event` trigger** (CLAUDE.md: not `MAP_SCRIPT_ON_TRANSITION`) on the three tiles **(21, 17), (22, 17), (23, 17)** in front of the gym door; state var (name PROPOSED `VAR_HOARFELL_STATE`, not claimed): 0 before, 1 after the thaw, 2 after fight 4. The tiles must be walkable and at elevation 3.

**The decision about GLALIE.** The author fixed that the scheme Pokémon are cutscene-only and belong to a staff member or a local ([../../troglodyte-arc.md](../../troglodyte-arc.md), 'Cutscene-only Pokémon'). So the **GLALIE belongs to the old angler**, WAKASAGI's friend, standing at (24, 17); the GLALIE is an overworld object beside him (`OBJ_EVENT_GFX_SPECIES(GLALIE)`; `graphics/pokemon/glalie/overworld.png` exists in the tree). WAKASAGI's team (SNEASEL, VANILLISH, LAPRAS, AVALUGG) does not change. This answers the card's open question 2.

**Before (objects present while the state is 0):**
- The **drill man** (hard hat) at (27, 11), on the pier's platform, facing south, with a **drill rig** (a truck sprite `OBJ_EVENT_GFX_TRUCK` or any big object) at (27, 10).
- Two **crew** (hard hats) at (26, 10) and (28, 10) on the platform.
- Two **flag props** (objects) at (24, 18) and (29, 18): a flag in each 'hole'. (Three in the card's text; two fit the object limit.)
- The **surveyor** at (27, 18) on the shore at the pier's foot, with the paperwork.
- The **old angler** at (24, 17) and his **GLALIE** at (25, 17).

**The beat:**
1. *Setup.* Stepping on a trigger tile: the drill man shouts down that he has 'bought the angling rights'.
2. *Reveal.* The surveyor reads from the paperwork: the lake is closed to anyone without a membership. The old angler grumbles about the flags; the Mountaineer's line about Surf is echoed.
3. *Collapse.* The rig **freezes in place** (replace the rig's tile with a snow-covered one by `setmetatile`, or the object plays a palette flash), then the **pier freezes** (`setmetatile` the bridge tiles at x 27, y 10 to 17 to a snow slab). The crew stands on a **floating slab** (the platform). The old angler's **GLALIE** floats along the pier (`applymovement` (25, 17) to (27, 17) then north to (27, 11)), exhales a cold breath, and the slab thaws (`setmetatile` back). The crew steps off to the shore. The **soup seller** appears at (16, 19) (a new object, a table `bg_event` at (15, 19) with the hidden PP UP, see Items) and sells them soup at cost. The crew walks off south-west along the lawn and out by the west gap. Set `FLAG_HOARFELL_SCHEME_DONE`. The flags and the rig vanish.
4. *Troglodyte fight 4.* He arrives from the east lane: he spawns at (38, 28), walks west along y 28 and north to (23, 18), faces west; the player is at (21, 17). The sneer line (card): 'Five towns of peasants cheering for you. It's frankly rude.' Battle: party of 4, levels 30 to 33: starter at stage 2, **Sir Biscuit as HERDIER**, **VAPOREON**, **KIRLIA** (reuse a vanilla trainer id; no IVs, `IVs: 0` lines). He leaves east. The gym door is script-locked while the state is 0 or 1; after fight 4 the player may go in.

## 7. NPCs outdoors (15 at most, tight)

| # | NPC | Position | Moves | Topic |
|---|---|---|---|---|
| 1 | Sign: town | (8, 30) | | `HOARFELL. SNOW, CLIFF AND TEA. IN THAT ORDER` |
| 2 | Sign: gym | (20, 19) | | `... MIND THE ICE. IT MINDS YOU` |
| 3 | Sign: lake | (21, 18) | | `FISHING PERMITTED. FOR NOW` (funny after Scheme 5) |
| 4 | Drill man | (27, 11) | still | before Scheme 5 |
| 5 | Two crew | (26, 10), (28, 10) | still | before Scheme 5 |
| 6 | Drill rig | (27, 10) | | vanishes after |
| 7 | Two flag props | (24, 18), (29, 18) | | vanish after |
| 8 | Surveyor | (27, 18) | still | the paperwork (reveal) |
| 9 | Old angler | (24, 17) | still | WAKASAGI's friend, grumbles about the flags |
| 10 | GLALIE | (25, 17) | float | the thaw |
| 11 | Troglodyte | spawned for fight 4 | | fight 4 |
| 12 | Soup seller | (16, 19), after Scheme 5 | still | soup at cost |
| 13 | Skier kid | (6, 31), west gap | wander | Ice cave's slippery floors |
| 14 | Cragdale-bound hiker | (38, 28), east lane | still | R10 is long and windy |
| 15 | Item balls: ICE HEAL x2 at (14, 38), POTION at (22, 31), NEVER-MELT ICE at (42, 14) | | | visible |
| 16 | Strength boulder | (30, 24) | | the HYPER POTION nook |

(The signs are `bg_event`s and cost no object. **Object count:** with the scene running: drill man, 2 crew, rig, 2 flags, surveyor, angler, GLALIE, Troglodyte = 10, plus skier, hiker = 12, plus the ICE HEAL, POTION and NEVER-MELT ICE balls = 15, plus the boulder = 16. **One too many.** Make the POTION a **hidden** item or drop the skier kid to the inside of House B. The soup seller replaces the crew after the scene, so the scene itself is the peak.)

Inside buildings (no cost outdoors): nurse, clerk, mountaineer, gym fan, grandson, skier parents, butler and the three cousins, WAKASAGI and the trainers.

## 8. Items and secrets (card, with positions)

| Item | Where | Gate |
|---|---|---|
| POTION | (22, 31), by the Center | visible (or hidden to save an object), none |
| ICE HEAL x2 | (14, 38), the south-west entrance area | visible, none |
| HYPER POTION | (31, 24), the nook east of the middle block | Strength (badge 4): push the boulder (30, 24) north |
| NEVER-MELT ICE | (42, 14), the north-east shelf | visible, none (walk the path) |
| PP UP | (15, 19), under the soup seller's table | hidden, after Scheme 5 |
| PROTEIN | in the Ice cave (B1F) | see [landmarks-west-detail.md](landmarks-west-detail.md) |
| TM Hail | in the Ice cave (B1F) | see landmarks |
| HM Surf | WAKASAGI | badge 5 |
| TM Ice Beam | gym reward | badge 5 |
| RARE CANDY | the lake islet at (29, 9) (PROPOSED: paint a 1-tile islet in the lake's north-east corner) | hidden, Surf (badge 5) |

**Note on Surf.** The player receives Surf here, so every earlier pond (R4, R5, R6, R8, Mothwood) becomes fully playable on a return, and the player learns it right before the water roads.

## 9. Palette and tile notes

- **Snow, Plan A (build this):** Team Aqua **Emerald Slide**, `Tilesets/The Great Tileset Exchange/Full Tilesets/Emerald Slide/`. What it is: a **snow recolour of the General primary**: three palette files (`02.pal`, `03.pal`, `05.pal`) and, for Pawkkie's tile tweaks, a tile image (`gTileset_GeneralSnow_Tiles_Pal2.png`) and a `metatiles.bin`. `SnowGeneralDemo.png` shows snow-covered pines, grass, ledges, a sign and drift patches. **How to use (the README's recipe):** in Porymap make a **new primary tileset**, copy the contents of `general` into it, use the three `.pal` files instead of the vanilla ones, and copy the tile image and `metatiles.bin` for the tile changes. This answers the card's open question 1: Hoarfell **does** get a snow tileset. It costs one new primary (the tileset count rises by one; check `src/data/tilesets/` after Porymap writes it) and a `CREDITS.md` row: **Ryu (winter theme and palette), Archie's Emerald Slide project, Pawkkie (minor tile and palette changes)**; copy the exact lines from the folder's `README.md`. It recolours **only the primary** (trees, grass, ledges, sand, water); the **Rustboro secondary** (rock walls and house roofs) stays vanilla brown and grey, which is fine: Blackthorn's cliffs are brown.
- **Plan B (free):** `gTileset_General` + `gTileset_Rustboro` and `WEATHER_SNOW` (falling flakes, no white ground). Cheaper, flatter. Good enough for a first pass; swap in Plan A later (the map keeps its blocks if the new primary has the same metatile order, which a recolour has).
- **The lake:** the ordinary water tile in the snow palette reads as grey-blue; 'ice' is the story (Surf is only allowed after the Leader). **PROPOSED:** keep it water. The pier is the General set's wooden bridge pieces (check `Route 119` or `Route 120` for them). The frozen slab in Scheme 5 is the same bridge tiles swapped for a snow-covered tile by `setmetatile` (use a patch or a sand tile as the slab if the snow set has no slab).
- **Rock walls:** the Rustboro cliff blocks (check `RustboroCity` and `Route104`'s north end). For taller walls the Fallarbor secondary (`Route114`, `Route115`) has big brown mountains; if the bowl needs them, use Fallarbor instead of Rustboro and the buildings change to its roofs.
- **Cave doors:** a dark 1 x 1 gap in the cliff face with a stone step (the General set's cave mouth block, as in Granite Cave's entrance on `Route106`).
- **Interiors:** Gen 4 Interior for houses; Zelda House for House A (optional); the Shoal Cave pair for the gym; vanilla layouts for Center and Mart.

## 10. Flags (not claimed)

| Name | Meaning |
|---|---|
| `FLAG_VISITED_HOARFELL` | fly point, set in `OnTransition` |
| `FLAG_HOARFELL_SCHEME_DONE` | Scheme 5 resolved: crew, rig and flags go; soup seller stays; after-lines |
| `VAR_HOARFELL_STATE` | 0 before the scene, 1 after the thaw, 2 after fight 4 |
| the reused trainer flag of the vanilla id Troglodyte fight 4 uses | fight 4 done |
| `FLAG_HOARFELL_ICE_CAVE_*` | one per cave item (in the cave file) |
| `FLAG_HOARFELL_ITEM_*` | one per town item |
| `FLAG_BADGE05_GET`, `FLAG_RECEIVED_HM_SURF`, `FLAG_BADGE06_GET` (for R18) | reused, not new |

Nothing is claimed in `design/flags.md`; that happens when built.

## 11. Build checklist (in order)

1. Add `Hoarfell` (46 x 44). **First decide Plan A or B**, because Plan A needs the new snow primary imported (Porymap: new primary, copy `general`, replace the three `.pal` files, copy the tile image and `metatiles.bin`). 2. Trace the render into rock walls, lake, lawn, sand ground; cut the three edge gaps; paint the pier. 3. Add the two cave doors on the top meadow and the north-east shelf. 4. Add the Center 1F and 2F and the Mart (shared vanilla layouts). 5. Add the houses A and B and the Goldsworth house. 6. Add `Hoarfell_Gym` from the grid (open `ShoalCave_LowTideIceRoom` first). 7. Warps in the order of the table. 8. Heal location and fly row: follow the checklist in [../../region-map.md](../../region-map.md) (write `respawn_map` before `respawn_npc` in `heal_locations.json`, and give both; the nurse is the Center's first object). 9. After pulling a duplicated map, grep `src/data/heal_locations.json` for duplicate ids (CLAUDE.md). 10. Connect R6 (west), R10 (east) and R18 (south, blocked) once those roads exist. 11. Events, trainers, NPCs; the Scheme 5 cutscene and fight 4 last. 12. The Ice cave (optional) after the gym. 13. Credits: Project Palladium (render); Emerald Slide if used; Zelda House if used; in the same commit as each import. 14. Close or reload Porymap before Claude edits event lists. 15. `make -j4` and `python3 design/tools/dialogue_check.py` on any text.

## 12. Build effort

**Hard in the card; now medium to hard.** The snow look is solved by a tileset that exists (Plan A) or by weather (Plan B). The gym is a **medium** job: one ice metatile, boulders, and a verified grid. The remaining risk is the lake, the pier and the Scheme 5 staging (`setmetatile` swaps, a rig, a GLALIE), and testing the slide puzzle and trainer sight in an emulator. The Ice cave is separate and optional.

## 13. Open questions

1. **Snow look** (card question 1): I found a snow tileset in the Team Aqua repo (Emerald Slide). Plan A (a new snow primary, one credit row) or Plan B (`WEATHER_SNOW` only)?
2. **GLALIE** (card question 2): decided by the author as cutscene-only, the old angler's. I used that. Confirm the angler owns it.
3. **Cave doors** (card question 3): top-centre (24, 5) is the main entrance and the north-east shelf (41, 12) the far exit. Confirmed in the cave file's loop.
4. **The Goldsworth house** (card question 4): the east house, as the card guessed. Confirm.
5. **`WEATHER_SNOW`** is marked unused in the tree. **I have not tested it**; if it does not render, Plan A's white ground carries the look and the weather can stay off.
6. **The pier and the slab:** are bridge tiles over the lake acceptable for the Scheme 5 set, or should the crew work on the lawn?
7. **Object count:** the Scheme 5 scene peaks at 16 objects. I trimmed in the NPC table; which NPC does the author want to lose?
8. **R18's closed gap** uses a `coord_event` row that turns the player back. Fine, or a barrier object?
9. **Shoal Cave pair for the gym** (a stone-and-ice hall) or the FRLG Seafoam pair (prettier, untested)?
