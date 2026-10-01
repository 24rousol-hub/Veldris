# GILDHAVEN, detailed design (city, place 8, gym 6 Flying)

Status: **PROPOSED.** Written 2026-10-01 for the author to build from. Everything here is a brief, nothing is built. Card this expands: [../towns/gildhaven.md](../towns/gildhaven.md). Rules: [../interiors/README.md](../interiors/README.md), catalogue: [../interiors/catalogue.md](../interiors/catalogue.md), house style: [../../interiors.md](../../interiors.md). Dialogue: [../../dialogue/goldsworth.inc](../../dialogue/goldsworth.inc). New minor names are marked PROPOSED. Coordinates are `x, y` in tiles from the top-left tile (0,0) of the map, and every one traced from a picture is good to about one tile: adjust to what the trace gives, keep the relations (door on the bottom row, counter in front of the clerk, and so on).

## 0. What I measured, and where this changes the card

- **The Goldenrod render is 59 x 51 tiles, not 62 x 54.** `goldenrodcitytiled.png` is 1005 x 868 px *with* a 1 px grid, so `(px - 1) / 17` = 59.06 x 51.0. (The card divided by 16.) Size check `(59+15) * (51+14) = 4810`, well under 10240. Plan **59 x 51**, with the sea on the east after mirroring.
- **All doors in the render face south** (every Gen 3 door does), so the card's 'Pokémon Center door faces north' and 'Emporium door faces west' are replaced by the render's real doors in the table in section 3. The Center and the Emporium both face south onto the lower avenue.
- **The render has a casino** (the yellow ball-emblem hall beside the tower) and a **white arched hall** (hotel). Both are used below. The big brown-roofed hall with the ball sign at the top is the **gym front**.
- **Gates are not interiors here.** A Gen 3 door sits on a building's south face only, so a pass-through gatehouse cannot be entered from the north. Gildhaven's two gates are **open-road guard lines on a plain map connection** (section 2). See Open question 4.
- **No elevator in the Goldsworth Tower.** The vanilla elevator menu (`MULTI_FLOORS`) is a fixed five-floor list in C. The tower uses stairs and a deadpan 'lift out of order' sign. The Emporium has exactly the five floors the vanilla lift expects, so its elevator works unchanged.
- **Scene 1 place.** `dialogue/goldsworth.inc` says Scene 1 is 'in the top-floor office' and ends with 'the lift is the shiny door', but the card and [../../troglodyte-arc.md](../../troglodyte-arc.md) put it on the gym forecourt. This document follows the card (forecourt) and moves the office to Scene 2. `Skyscraper_Text_MrMeet3` needs one reworded line (Open question 1).

## 1. Description

**First glance, from R18 (the north gate).** The player steps out from under a grey gate hut onto a **four-tile-wide cobbled avenue** that runs dead straight south for the whole screen and beyond. Cream cobbles with a yellow centre stripe, yellow-trimmed roofs on both sides, blue-glass shopfronts. On the left a brown-roofed hall with a ball sign (the gym) and a lawn of red flower beds. On the right, past a long fenced lawn, **the tower**: a glass spine fifteen tiles tall with a satellite dish on top, taller than anything the player has seen in the region, with the strip of the sea behind it. Nothing else in Veldris is this tall, which is the point.

**From the harbour (R19, by Surf).** The sea road ends at a **stone quay**: bollards, a railing, a short pier. The tower rises straight out of the plaza behind it, so the first thing on arrival is a wall of glass and gold with a big G on the roof. Wingull (a Pokémon, as ever) sit on the bollards.

**From the south (back from R20).** The Pinnacle Gate's guard line opens onto the avenue's bottom end. The player sees the whole avenue run north: Center roof (red), Emporium (gold and blue), the Casino's yellow dome, then the gym's brown roof at the far end.

**Mood and colour.** Glossy, expensive, a little too clean. Cream, pale yellow and gold, blue glass, red Center roof. Every shop sign sells something and everything is faintly overpriced. Deadpan, not menacing: nothing here is quite as good as it looks. **Sound and music:** `MUS_LILYCOVE` for the town (a busy harbour city; it is already used for the Lilycove dept store and fits), `MUS_POKE_CENTER` and `MUS_POKE_MART` indoors as vanilla, `MUS_GYM` in the gym, `MUS_RUSTBORO` in the Tower's office floors (it is Devon Corp's tune), `MUS_GAME_CORNER` in the Casino. **Time of day:** forenoon by default, long shadows, light off the water. No time-of-day system is assumed.

**The one memorable view.** At the end of the north quay (54,26) the player faces west: the tower fills the left of the screen top to bottom, the avenue's gold stripe runs away behind it, and the window cleaner dangles in front of the glass saying 'don't look up'.

## 2. Street layout, in words (mirrored render, north at the top)

Mirror the render left to right before tracing (the sea is on the render's west, and R19 leaves east). All coordinates below are for the mirrored 59 x 51 map. Cols 0-6 and rows are as in the picture flipped.

1. **North gate (R18).** A grey gate hut at cols 28-33, rows 0-4. Plan: two flanking huts (28-29 and 33-34, rows 0-4) with the road opening **cols 30-32** between them, and a barrier object plus a guard at (31,4). Connection to R18's south edge (offset below). Gate rule: closed from the Hoarfell side until `FLAG_BADGE06_GET` (R18 is under construction), always open from this side. See [../routes-centre.md](../routes-centre.md) R18.
2. **Estates Lawn (north-east).** Cols 34-50, rows 1-7: a big fenced green lawn with a row of trees along the top (cols 40-47, row 0-1) and a single boulder at (42,3). Scenery, one hidden item (see Items), and the park bench at (38,6) for the sulking jogger.
3. **The Avenue.** Cols 29-33, rows 5-50, cobbles with a yellow stripe (the 'path' tile in the ORAS General palette is already yellow-toned). It runs the full height. **Cross street** at rows 18-19 (a yellow-striped road running the full width, with blue fences along both sides, rows 17 and 20).
4. **Gym forecourt (north-west).** The gym is the brown-roofed hall at **cols 21-28, rows 8-12, door (25,12)** with a ball sign above the door. In front of it, **rows 13-16, cols 21-29**, is a cobbled forecourt bounded on the south by the cross-street fence at row 17. A bench at (22,14), a flower tub at (28,13), a windsock-style banner object at (21,13). **Scheme 6 plays here** (section 5). The flower beds (red) fill **cols 8-17, rows 5-9** west of the gym, with a yellow-roofed house at cols 16-20, rows 7-10 (decor, no door).
5. **Pilots' Club and the north-east terrace.** A row of four yellow-roofed buildings at **cols 33-47, rows 8-12**. The first (cols 33-37) is the **Pilots' Club**, door **(35,12)**. The third (cols 41-46) is the **Estates Sales Office**, door **(42,11)**. The second and fourth are decor.
6. **Casino and tower base (east).** The yellow-domed Casino at **cols 39-45, rows 16-20**, door **(43,20)**. East of it the **Goldsworth Tower**: body **cols 48-52, rows 8-24**, dark annex at cols 46-47, rows 15-20, wider base at rows 20-24 (cols 46-52), **lobby door (49,23)** (double door, warps on (49,23) and (50,23)). A round plaza and a statue plinth (the statue is of nobody: a deadpan joke, object at (47,25)) sit in front of the base.
7. **Harbour and quay (east edge).** Two paved quays: the **north quay** at **cols 50-55, rows 25-27** with a railing along row 27, and the **south quay** at **cols 52-54, rows 34-41** with a railing at col 54-55. The sea runs along cols 55-58 and widens south. **Surf starts at the quay ends** (54,26) and (54,38). A **rock islet** sits at (56,33), holding a Star Piece. R19's connection is on the whole east edge, rows 26-45 (offset in section 3).
8. **Market quarter (centre-south).** West of the avenue the **Emporium** at **cols 22-28, rows 26-39** (roof rows 26-28, deck rows 29-32, glass front rows 33-38). **Main door (23,38)**, a second ground-floor door at (27,38) (decor or a staff entrance to the same 1F). East of the avenue the **Pokémon Center** (red roof, **cols 33-37, rows 35-38, door (35,38)**). The **Hotel** (white arched hall) at **cols 33-40, rows 26-30, door (37,30)**, with two pillars at (36,30) and (38,30). The glass **pavilion** (render's bike shop) at **cols 18-21, rows 36-41**: a closed shop, shutters down, decor.
9. **Residential streets.** Yellow-roofed houses fill the south-west (cols 7-17, rows 25-50), the south-east (cols 38-54, rows 28-50) and the north-west. Most are decor (windows, no door). **Enterable:** the Navigator's house **door (13,15)**, the Window cleaner's flat **door (14,29)**, the Move Deleter's house **door (49,36)**, the Cafe **door (40,41)**.
10. **Pinnacle Gate (south).** Two flanking huts at cols 28-29 and 33-34, rows 47-50, with the road opening **cols 30-32** between them and a guard line at (31,48). Connection to R20's north edge. Gate rule: nine badges, counted with `GetBadgeCount()` (CLAUDE.md badge rule), the guard blocks until the count is 9.
11. **Cliffs.** The west fringe, cols 0-6, is rock wall with ledges (render's east flipped): one **Cut tree** in a pocket garden at (9,23), one **Rock Smash rock** at (4,33), one **Strength boulder** with a shelf at (5,43), all reached by ledge steps from the street at (7,22), (7,32) and (7,42).
12. **Palette.** The render's gold roofs: the LeoB ORAS General palette is already yellow-toned for paths; recolour a roof palette slot to yellow in Porymap's palette editor. The Emporium and the glass pavilion read as Lilycove's dept store and shopfront in the ORAS Lilycove secondary.

### Outdoor tilesets (recommended)

| Part | Tileset | Status |
|---|---|---|
| Primary | `gTileset_General` (already the LeoB ORAS recolour, Hollowbrook uses it) | in tree |
| Secondary | **LeoB ORAS `lilycove` secondary**: dual-layer, same metatile ids as vanilla Lilycove, so it drops straight in. Folder `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS/tilesets/secondary/lilycove/` (351 metatiles). Gives the department-store facade (brick, Poké Ball logo), the glass shopfront, white museum-style hall, harbour tiles | **needs a CREDITS row**: extend the existing leob0505 row to name `lilycove` (door anim `lilycove` if the author wants it) |

Do not use Brick City or Gatehouse here (see section 9).

### Tower exterior: decision to take first (see Open question 2)

The render's tower is 5 wide and 15 tall (rows 8-24), which no Emerald tileset has. Test in this order, each is cheap:

1. **Stack the ORAS Lilycove dept-store window band.** The facade's repeating row of window metatiles can be stacked 10 times with a base row and a roof row from the same set, giving a blue-and-orange glass tower about 6 wide. Paint it, look at it in Porymap, decide.
2. **A glass spine from the museum facade** (the white and blue hall in the same set), stacked the same way, so the tower is not the same colour as the Emporium.
3. **New metatiles** copied from the Palladium Radio Tower (cols 48-52, rows 8-24 of the mirrored render) and the Battle Tower render (`Battle Tower.png`, 24 x 26, a glass cylinder on a plaza), drawn by the author. Needs a Palladium credit.

The dish on the roof and the dark annex are two metatile pieces each. The window cleaner's rope is an object, not tile art.

## 3. Door and warp table: Gildhaven (outdoor map `Gildhaven`, 59 x 51)

Warp ids are suggestions in Porymap order. Exit warps from every interior point back to the matching id and land **outside the door** (one tile south).

| # | Tile on `Gildhaven` | Door facing | Destination map (arrival) | Notes |
|---|---|---|---|---|
| 0 | (35,38) | S | `Gildhaven_PokemonCenter_1F` (mat 6,8) | Fly lands at (35,39), `HEAL_LOCATION_GILDHAVEN` |
| 1 | (23,38) | S | `Gildhaven_Emporium_1F` (mat 8,12) | main door |
| 2 | (27,38) | S | `Gildhaven_Emporium_1F` (mat 10,12) | optional, second warp to the same 1F |
| 3 | (25,12) | S | `Gildhaven_Gym` (mat 7,17) | blocked by the basket object during Scheme 6 |
| 4 | (49,23) and (50,23) | S | `Gildhaven_GoldsworthTower_1F` (mat 9,12 and 10,12) | |
| 5 | (43,20) | S | `Gildhaven_Casino` (mat 3,15) | |
| 6 | (37,30) | S | `Gildhaven_Hotel_1F` (mat 5,8 and 6,8) | |
| 7 | (35,12) | S | `Gildhaven_PilotsClub` (mat 5,13) | |
| 8 | (42,11) | S | `Gildhaven_SalesOffice` (mat 5,7) | |
| 9 | (13,15) | S | `Gildhaven_NavigatorsHouse` (mat 2,7) | |
| 10 | (14,29) | S | `Gildhaven_CleanersFlat` (mat 2,7) | |
| 11 | (49,36) | S | `Gildhaven_MoveDeletersHouse` (mat 3,7) | |
| 12 | (40,41) | S | `Gildhaven_Cafe` (mat 5,8) | |

**Map connections** (Porymap `offset` is how far the neighbour is shifted from this map's edge, positive = right or down):

| Edge | Neighbour | Offset | Lines up |
|---|---|---|---|
| North | `VeldrisRoute18` (28 x 32) south edge | +17 | R18's opening (cols 13-15) meets the gate opening (cols 30-32) |
| East | `VeldrisRoute19` (80 x 40) west edge | +12 | Gildhaven rows 26-39 meet R19 rows 14-27 (open water, Surf) |
| South | `VeldrisRoute20` (22 x 91) north edge | +21 | R20's corridor (cols 8-13) meets the gate opening (cols 30-32, R20 cols 9-11) |
| West | none | | rock wall |

Check the offsets in Porymap when both maps exist and nudge by a tile.

## 4. Buildings and interiors

Map list: `Gildhaven`, `_PokemonCenter_1F`, `_PokemonCenter_2F`, `_Emporium_1F` to `_5F`, `_Emporium_Elevator`, `_Emporium_Roof`, `_Gym`, `_GoldsworthTower_1F` to `_6F`, `_GoldsworthTower_Roof`, `_Hotel_1F`, `_Hotel_2F`, `_PilotsClub`, `_Casino`, `_SalesOffice`, `_NavigatorsHouse`, `_CleanersFlat`, `_MoveDeletersHouse`, `_Cafe`. That is **27 maps** (the lean tower is 24). Do not name anything `Gildhaven_GoldsworthHouse`: the town has no house (the tower is it).

All interiors use `MAPSEC_GILDHAVEN` (new section, PROPOSED; one of the free ids, [../../engine-limits.md](../../engine-limits.md)).

### 4.1 Pokémon Center 1F and 2F (unchanged vanilla)

`LAYOUT_POKEMON_CENTER_1F` (14 x 9) and `_2F` (14 x 10), tileset `gTileset_PokemonCenter`. **Never move the nurse.** Vanilla facts (read from `OldaleTown_PokemonCenter_1F`): nurse (7,2); door mats **(6,8) and (7,8)**; stairs up (1,6). 2F: attendants at (2,2), (6,2), (10,2), mystery gift man (1,2); warps (1,6) back down, (5,1) Union Room, (9,1) Trade Center. Gildhaven's flavour NPCs (3, on the vanilla tiles): a **pilot waiting for a cup of tea** (4,4) facing down, a **shopper with too many bags** (10,6) facing right, a **kid reading the 'Gym Acquisition Programme' leaflet** (3,7) facing right. After Scheme 6 the **nurse** eats the gift-basket biscuits (an extra line only). Music `MUS_POKE_CENTER`.

### 4.2 Gildhaven Emporium: five floors, elevator, roof

**Base:** Palladium `Goldenrod Dept Store 1F.png`, which is really **six floor panels plus a roof panel on one sheet** (956 x 702 px, each panel about 304 x 220 px = **19 x 14 tiles**, panels at x 5, 328, 640 and y 5, 238, 473). **Tileset** `gTileset_Building` + `gTileset_Shop` (vanilla dept store's own), so the shelves, counters, flower pots and elevator door metatiles already exist. Vanilla Lilycove floors are only 18 x 8: use the Palladium panels (19 x 13 after trimming the black bottom row) for a bigger, handsomer store. The vanilla scripts (`LilycoveCity_DepartmentStore_*`) are duplicated floor by floor and the **vanilla elevator keeps working because the Emporium has exactly floors 1F to 5F** (`DEPT_STORE_FLOORNUM_1F..5F`). The sixth Palladium panel (the sofa and table floor) is not used; fold its sofa table into 5F or drop it. Credit the Palladium team in the commit that traces it.

Common layout on every floor (render coordinates, 19 wide; the stairs and elevator tiles are the vanilla ones):

| Feature | Tile |
|---|---|
| Landing hall (carpeted, window above) | cols 3-10, rows 1-3 |
| **Elevator doors** (double, with the floor sign above) | warp at (2,1), as vanilla (the render has the doors at (7,2); either works, keep (2,1) so the vanilla elevator scripts' arrival tiles do not move) |
| **Stairs** | follow vanilla: 1F up (16,1); 2F down (16,1) and up (13,1); 3F and 4F the same; 5F down (13,1) and the **rooftop stairs (16,1)** |
| Exit mat (1F only) | (9,12) and (10,12) |
| Left and right flower pots | cols 0 and 18, rows 7-11 |

Floor by floor (what the render shows, and where the clerks go):

| Floor | Render panel | Counters and shelves | Clerks and NPCs (tile) | Stock (card) |
|---|---|---|---|---|
| **1F, services** | top-left | white L-counter at cols 12-17, rows 5-8 with a register at (14,6); four pink display tables at (2,9), (6,9), (11,9), (15,9) | **floor guide** (14,4) facing down behind the counter; shopper (3,7); child (16,10) | Potion line, balls to Ultra Ball, Repels. A **lottery-style counter** is not used |
| **2F, medicine** | mid-left | long white counter cols 12-18, rows 8-12; 3 glass shelf cabinets cols 2-8, rows 9-11; medicine shelves on the top wall | **clerk L** (13,9), **clerk R** (15,9) facing down; nurse-intern (3,6) | Antidote, Full Heal, Revive |
| **3F, tools** | bottom-left | counter at cols 11-14, rows 4-5; glass tables (13,10),(15,10); 3 shelf cabinets cols 2-8 | clerk L (11,5) and R (13,5); a tinkerer (6,8) | X items, Escape Rope |
| **4F, TMs** | top-middle | counter at cols 12-17, rows 4-6; four display glass cases at the top; 4 cabinets cols 2-9, rows 8-12 | **TM clerk** (14,6); bored browser (5,6) | TMs (priced as TMs): Protect, Light Screen, Reflect, Double Team, Rest, Torment |
| **5F, vitamins** | middle | central pink-carpet counter (square) at cols 8-13, rows 7-10, with the carpet strip (9,5)-(10,6) | **clerks** at (7,8), (9,6), (12,8), (14,10); a shopper (3,11) | HP Up, Protein, Iron, Calcium, Zinc, Carbos (expensive); 6-badge gate PROPOSED (always met here) |
| **Roof** | bottom-right | a **garden roof**: green railing all round, a paved deck, a central raised bed (cols 7-13, rows 4-8), vending machines on the top-left wall at (1,2)-(2,2) | **vending kid** (4,6) facing right; thirsty visitor (10,10) | vending: Fresh Water, Soda Pop, Lemonade (vanilla `VendingMachine` scripts) |

The **Roof panel** (the one at the sheet's top-right) shows a yellow-and-green rail, three vending machines on the wall at (2,1),(3,1),(4,1) and a corner annex at (14,1)-(17,4). Copy the vanilla `LilycoveCity_DepartmentStoreRooftop` (18 x 12): **5F's stairs up (16,1) lead to Roof (13,3)**, exactly as vanilla. Use the vanilla warp tiles from `LilycoveCity_DepartmentStore_5F`: (13,1) down to 4F, (2,1) to the elevator, (16,1) to the Roof.

**Emporium Elevator** (`Gildhaven_Emporium_Elevator`, 5 x 6, `gTileset_BattleFrontier`): copy `LilycoveCity_DepartmentStoreElevator` exactly (attendant (0,5), dynamic warps (1,5),(2,5)).

**Emporium warp ids** (the vanilla set, re-pointed): 1F: exit mats (8,7)-(9,7) in vanilla become (9,12)-(10,12) here, stairs up, elevator door. Each upper floor: stairs down, stairs up, elevator door. Floor-name sign on 1F (vanilla `FloorNamesSign`): re-word for the Emporium's floors. Counts: each floor 3 to 7 objects, well under 15. Dialogue per clerk is one line from the card.

### 4.3 Gildhaven Gym: 'the Hangar' (PROPOSED name), full design

**Leader TOBIN**, Flying, Feather Badge, TM Aerial Ace, HM Fly (the HM is the story gate for Fly, [../../badges.md](../../badges.md)). Team and ids from [../../trainer-roster.md](../../trainer-roster.md): Swellow 40, Unfezant 41, Talonflame 41, Corviknight 42. **Tobin is a man** (leader pitch in [../../gyms.md](../../gyms.md), roster `TOBIN` 'Norman'); the Scheme 6 row of [../../troglodyte-arc.md](../../troglodyte-arc.md) says 'tip her', a wording slip to fix (Open question 7).

**Source and size.** Palladium `Violet City Gym.png` (208 x 288 px, no grid, **13 x 18 tiles**) is the *look*: a blue-grey hangar, a raised windowed platform at the top, a black void with a grey catwalk across it, two Poké Ball statues and the door at the bottom. **Layout adapted to 15 x 18** with straight catwalks (the render's serpentine bridge cannot carry wind belts and trainer sight lines). Size check `(15+15)*(18+14) = 960`. **Tilesets:** `gTileset_Building` + **`gTileset_MossdeepGym`** (a black void and metal floor already, the Mossdeep warp-pad gym), colour-matched to the render's blue-grey by palette. Music `MUS_GYM`.

**The puzzle: 'Crosswind' (PROPOSED).** Three **wind belts** cross the hall, each one tile tall, each blowing the whole length of the hall one way (east, west, east). The player must ride them to get up. Between the belts are two-tile **walking strips** where the trainers stand and watch the belts. Rules the player learns in the first ten seconds: step onto a belt and you are carried to its far end, and you cannot steer on it, so you cannot dodge a trainer who sees the belt tile you pass. Nothing falls: the void is only a backdrop and the strips and belts run edge to edge, so it **cannot soft-lock** (the return trip works the same way, see below).

Legend: `#` wall, `~` void (impassable), `.` strip floor, `>` east wind tile, `<` west wind tile, `e`/`w` normal tile at the belt's end (the wind stops here), `L` TOBIN, `1 2 3` trainers, `G` gym guide, `S` statue (a sign, not an object), `D` door mat.

```
      x: 000000000011111
         012345678901234
 y 0  |###############|
 y 1  |###############|   banner and windows
 y 2  |###.........###|   leader platform, cols 3-11
 y 3  |###....L....###|   TOBIN (7,3) facing down
 y 4  |#~~~~~~.~~~~~~#|   step down at (7,4)
 y 5  |#.........3...#|   strip S3, trainer 3 (10,5)
 y 6  |#.............#|   S3 lower row
 y 7  |#>>>>>>>>>>>>e#|   belt B3: east, ends at (13,7)
 y 8  |#.............#|   strip S2
 y 9  |#.....2.......#|   S2 lower row, trainer 2 (6,9)
 y10  |#w<<<<<<<<<<<<#|   belt B2: west, ends at (1,10)
 y11  |#.............#|   strip S1
 y12  |#......1......#|   S1 lower row, trainer 1 (7,12)
 y13  |#>>>>>>>>>>>>e#|   belt B1: east, ends at (13,13)
 y14  |#.............#|   entry hall S0
 y15  |#....S...S....#|   statues (5,15) and (9,15)
 y16  |#..G..........#|   gym guide (3,16)
 y17  |######D########|   door mat (7,17)
```

Rows are 15 wide. The belt rows have 12 wind tiles and one normal end tile, so every belt **ends on a normal tile** where the player regains control (the wall beyond it stops the push). The strip rows are walkable edge to edge.

**Arrow tiles.** Vanilla Emerald has the *behaviours* `MB_WALK_EAST` and `MB_WALK_WEST` (forced walking) but almost no tile art for them: my scan of the tree's attribute files finds them only in the **Trick House puzzle** secondary (`MB_WALK_EAST` on metatiles 48 and 62) and the **`unused_2`** tileset (`MB_WALK_EAST` on metatile 2, `MB_WALK_WEST` on metatile 6). Look at those in Porymap first. If the art is not a clean floor arrow, **the author draws 2 new metatiles** (an east arrow and a west arrow on the grey catwalk floor) in the gym secondary and sets their behaviour to `MB_WALK_EAST` and `MB_WALK_WEST`. Nothing else is needed. **Verify in the emulator** that forced walking on a belt tile ends cleanly on a normal tile and that holding a direction key does not let the player step off mid-belt (this is how Trick House conveyors behave, but it is untested here).

**Trainers (3, reuse vanilla ids, no IVs).** Levels follow the author's rule (3 or 4 under Tobin's lowest, 40):

| # | Class | Team | Tile and facing | Sight |
|---|---|---|---|---|
| 1 | Cooltrainer | Pelipper 36, Altaria 37 | (7,12) facing north | 2 (sees (7,11) and the belt tile (7,10)) |
| 2 | Pokémon Ranger | Dodrio 36, Fearow 38 | (6,9) facing north | 2 (sees (6,8) and the belt tile (6,7)) |
| 3 | Cooltrainer | Noctowl 37, Staraptor 38 | (10,5) facing south | 2 (sees (10,6) and (10,7)) |

Why each one is **unavoidable but fair**: after belt B1 the player arrives at (13,12) and must cross column 7 on S1 or ride B2 through (7,10), both inside trainer 1's sight. After B2 the player arrives at (1,9) and must cross column 6 on S2 (trainer 2 stands in row 9, so row 8 is the only way and it is in sight; riding B3 from the west of column 6 passes (6,7), also in sight). After B3 the player arrives at (13,6) and must walk west past column 10 on S3 (trainer 3 blocks row 5, row 6 is in sight). Each trainer is a separate fight; no healing in the gym (the Center is one street away).

**Return trip (leaving after the fight).** Step south onto B3 from S3 at any column: it carries you east to (13,7), then south to (13,8) on S2. Repeat for B2 (carried west to (1,10), south to (1,11)) and B1 (east to (13,13), south to (13,14)). The trainers do not fight again. Allow `Escape Rope` out of the gym map (`allow_escaping` true on the gym map) so a trapped player is never stuck.

**Objects (6 of 15):** TOBIN, trainers 1 to 3, gym guide (3,16), an NPC visitor optional. Statues and the hint board at (7,16) are signs. **Hint board:** 'Stand still. The wind will do the talking.' Sound: `MUS_GYM`; Tobin's battle music vanilla gym leader. After the fight Tobin gives the badge, TM, HM at (7,4).

**Gym warps:** door mat **(7,17)** only. Warp from the town door (25,12). Exit lands at (25,13).

### 4.4 Goldsworth Tower: seven floors by stairs (FULL build)

**Scope.** The author asked for the tower floors in full detail, so the full build is described: **1F Lobby, 2F Mailroom and Legal, 3F Accounts and Acquisitions, 4F Boardroom, 5F President's Office, 6F Penthouse, Roof**. The lean version (4 maps) merges 2F and 3F, and 4F into 5F, and drops the Penthouse; nothing else changes. **No battles inside** the tower and nothing to be won, so the floors are cheap to script. Music: `MUS_RUSTBORO` (Devon Corp's tune) on 1F to 3F, `MUS_POKE_MART`-style calm tune optional on 4F, `MUS_LILYCOVE_MUSEUM` on 5F and 6F.

**Stairs and lifts, standard.** Floors 1F to 3F: **stairs up at (16,1), stairs down at (2,1)** (4F's up stairs are at (14,1); 5F, the Penthouse and the Roof have their own, see their plans), copying the vanilla Lilycove dept-store convention (the stairs warp tile pair). The **lift is a prop** (an elevator-door metatile with a sign: 'OUT OF ORDER. THE STAIRS ARE A WELLNESS FEATURE.' at the top centre of 1F and the Boardroom). No elevator map, no `MULTI_FLOORS` edit, no engine change.

**Floor access (PROPOSED, flags not claimed).**

| Floor | Opens | Why |
|---|---|---|
| 1F, 2F, 3F | always (from the first visit) | public floors |
| 4F | after Scheme 6 Scene 1 | reception: 'the Boardroom is for family guests; you are, as of this morning, a guest' |
| 5F | after the gym (Scene 2 invitation from Whitmore) | Scene 2 |
| 6F Penthouse | after Scene 2, then stays open | the home above; the **post-game epilogue room** ([../../postgame.md](../../postgame.md)) |
| Roof | after Scene 2 | the helipad and the Rare Candy |

Gating is a guard NPC on each stair door, or a one-tile blocker object removed by flag, as the existing vanilla stair guard in `RustboroCity_DevonCorp_1F` (`LOCALID_DEVON_CORP_STAIR_GUARD`) does.

**Tilesets.** Public floors (1F to 3F): `gTileset_Facility` (vanilla Devon Corp's grey-blue corporate set, no import). Boardroom and President's Office (4F, 5F): **Little Office Interior Secondary**, folder `Tilesets/The Great Tileset Exchange/Full Tilesets/Little Office Interior Secondary/` (see section 9: triple-layer, 120 metatiles, small). Penthouse (6F): `gTileset_Gen4Interior` (already in the tree) because it is a home. The contrast is the story: **clerks work in grey, the family lives in warm wood and cushions.**

#### 4.4.1 1F Lobby (19 x 13, Facility, mats (9,12) and (10,12))

```
      x: 0000000000111111111
         0123456789012345678
 y 0  |###################|
 y 1  |####P#P#X#P#P###^##|   portraits P, clean rectangle X (8,1), stairs up (16,1)
 y 2  |#....i..........B.#|   directory i (5,2), stair guard B (16,2)
 y 3  |#.......=====.....#|   reception counter (8..12,3)
 y 4  |#.........R.......#|   receptionist R (10,4)
 y 5  |#.................#|
 y 6  |#.................#|
 y 7  |#...g.g.g.g.g.....#|   security gates g (4,7)..(12,7)
 y 8  |#..V...........C..#|   visitor V (3,8), courier C (15,8)
 y 9  |#.................#|
 y10  |#.....W...........#|   plant waterer W (6,10)
 y11  |#.................#|
 y12  |#########DD########|   mats (9,12) (10,12)
```
Legend: `#` wall, `.` floor, `=` reception counter, `g` security gate (a turnstile prop), `P` portrait sign, `X` the clean rectangle, `^` stairs up. The ground floor has **no stairs down**. **Directory board** (sign) at (5,2): '1 LOBBY, 2 MAILROOM AND LEGAL, 3 ACCOUNTS AND ACQUISITIONS, 4 BOARDROOM, 5 THE FAMILY, 6 NOT FOR YOU, ROOF PLEASE DO NOT'. **Portrait wall** (signs along y=1): (4,1) 'BARNABY GOLDSWORTH, Founder', (6,1) 'CHESTER GOLDSWORTH, Second', **(8,1) the clean rectangle: 'Something large was removed from here. It was not a window.'**, (10,1) and (12,1) portraits in gold frames. **NPCs (5):** receptionist (10,4) facing down; a **security guard** at the stair door (16,2) facing down (opens the stair per the gate table); a **visitor** with a clipboard (3,8) facing right; a **courier** (15,8) walking up and down; a **plant waterer** (6,10) facing left. **Scripts here:** visitors' pass joke, the floor list. **Object count 5 of 15.**

#### 4.4.2 2F Mailroom and Legal (19 x 11, Little Office)

Sorting-rack wall (white counters with files, the tileset's counter-and-bookcase pieces) along the top: cols 1-8 mailroom, cols 10-17 legal. Mailroom half **west**: a long sorting counter at **(3..7,4)**, stacks of parcels as items on the floor, the **mailroom clerk at (5,5)** facing up. Legal half **east**: two glass desks (the tileset's L-shaped glass desks at **(11,5)** and **(14,5)**), the **legal clerk at (12,6)** with a file labelled 'Schemes, in progress' (a sign on the shelf at (13,2), the reading of which is a one-line joke: 'Hay maze, tent, sheets, stickers, holes, basket... in progress'). A **fax/printer** at (17,3) (a sign: 'It has been printing the same Gym Acquisition invoice for six years'). **Stairs** down (2,1), up (16,1). **NPCs (4):** mailroom clerk (5,5), legal clerk (12,6), a courier asleep on a parcel (8,8) (facing down, a sleeping NPC), an intern (15,8) wandering. The **mailroom job joke** lands here (Mr. Goldsworth's Scene 1 offer): a **spare desk with a name plate 'NEW STARTER'** at (9,8) that the clerk gestures at.

#### 4.4.3 3F Accounts and Acquisitions (19 x 11, Little Office)

A long **wall chart** (sign pair at (6,1) and (7,1)) titled **'GYM ACQUISITION PROGRAMME'** (the badge-count secret, section 7). Four glass desks in two rows (the tileset's L-shaped pieces) at (3,5), (7,5), (11,5), (15,5); **accountant** at (13,7) facing up, behind his own desk, holding the running total that Scheme 9 reads out later ([../../troglodyte-arc.md](../../troglodyte-arc.md)). A **calculator** sign at (9,8) ('Four hundred. Counted twice.'). Stairs down (2,1), up (16,1). **NPCs (4):** accountant (13,7), two analysts at (3,7) and (7,7) both facing down, a runner (15,9) walking left and right.

#### 4.4.4 4F Boardroom (17 x 12, Little Office)

One **long glass table** made of the tileset's glass pieces, **cols 5-11, rows 4-6**, with 8 chairs around it as sign-less tiles (cols 4 and 12, rows 4-6, and the ends at (3,5), (13,5)). A **window wall** across the top (the gable window piece centred at cols 7-9). **Empty chairs, one with a cushion** at (12,5). **Hidden PP Up** in the drawer under the desk at (14,2) (a sign on the bookcase tile). **Out-of-order lift** at (8,1). **NPCs (2):** a **night cleaner** at (4,9) (the only person here, deadpan: 'The family meets here to agree with itself'), and a **board secretary** at (13,8) pointing at the minutes. Stairs down (2,1), up (14,1).

#### 4.4.5 5F President's Office (19 x 21, Little Office, from the Palladium render)

**Source:** Palladium `President's Office Tiled.PNG`, 324 x 366 px **with a 1 px grid**, so **19 x 21 tiles** and a half-row margin (`(324-1)/17 = 19.0`, `(366-1)/17 = 21.5`). The card's '20 x 22' is slightly high. The render is not one room but a **ring**: a left corridor, a bottom corridor, a right corridor and a lift hall, around one big office, with a small stairwell room at the top. **Trace it as it is**, it is already a good Scene 2 stage. The grid below is a **schematic of the render's structure** (measured by eye, +/- 1 tile) to fix where things go, not a replacement for tracing.

```
      x: 0000000000111111111
         0123456789012345678
 y 0  |###################|
 y 1  |######...p.########|   p painting (9,1)
 y 2  |######S....#......#|   S stairs down (6,2)
 y 3  |######........L...#|   L lift prop (14,3); (11,3) opening
 y 4  |######.....#......#|
 y 5  |#....#.....#####..#|
 y 6  |#..o.###.#######..#|   o orange pad (3,6); opening (8,6)
 y 7  |#....#c..ppp...#..#|   c PC (6,7), paintings p (9..11,7)
 y 8  |#....#f.b...b..#.d#|   f fridge (6,8), bonsai b (8,8) (12,8), d private door (17,8)
 y 9  |#....#...sss...#..#|   s sofa (9..11,9)
 y10  |#....#.........#..#|
 y11  |#....#..tttttt.#..#|   t glass table (8..13,11..13)
 y12  |#....#..tttttt.#..#|
 y13  |#....#..tttttt.#..#|
 y14  |#....#.........#..#|
 y15  |#....###..######..#|   office door (8,15) (9,15)
 y16  |#....###..######..#|
 y17  |#.................#|
 y18  |#.........bbb....u#|   plants b (10..12,18), service stair u (17,18)
 y19  |#.................#|
 y20  |###################|
```
Legend: `S` stairs down, `L` lift (prop), `o` orange floor pad (decor), `c` PC, `f` fridge, `p` painting (wall signs), `b` bonsai, `s` sofa, `t` glass table with the nobody-statue, `d` private door to the Penthouse, `u` service stair up to the Roof. **One liberty over the render:** a doorway at **(8,6)** between the stairwell room and the office, so the player does not walk the whole ring to reach the office (the render shows a plain wall there).

**Scene 2 stage (PROPOSED).** After the gym the player gets a note from Whitmore (a short scripted talk on the plaza) and the stair guard lets them up. The player arrives at (7,2), walks (8,6) to the office. **Mr. Goldsworth stands behind the glass table at (11,10) facing down; Mrs. Goldsworth by the sofa at (8,9) facing right; Whitmore at (7,10) with a notebook**; the player is walked to **(10,14)**, just south of the table. The `Skyscraper_Text_MrAfter*` and `MrsAfter*` lines run here; Mrs. Goldsworth gives the **Amulet Coin** (it was in the sandwich box in `MrsAfterThanks`). **Objects (4):** Mr., Mrs., Whitmore, a **tea-trolley attendant** at (6,13). After Scene 2 the three principals are gone from 5F and the private door (17,8) is open to the Penthouse.

#### 4.4.6 6F Penthouse: the Goldsworth parents' home (15 x 10, `gTileset_Gen4Interior`)

The home above the office, in the house style (Gen 4 Interior), but **everything is slightly too big**. Private stair door at **(1,8)** (up from 5F's (17,8)); exit mat **(2,9)**.

```
      x: 000000000011111
         012345678901234
 y 0  |###############|
 y 1  |###############|
 y 2  |#kkk.....i..h.#|   kitchen k (1..3,2), list i (9,2), photo shelf h (12,2)
 y 3  |#..M.........c#|   maid M (3,3), cabinet c (13,3)
 y 4  |#..rrrrrrrr...#|   rug r (3..10, 4..6)
 y 5  |#..rrSSSSrr...#|   sofa S (5..8,5)
 y 6  |#..rrrrrrrm...#|   Mr. m (10,6)
 y 7  |#....w........#|   Mrs. w (5,7)
 y 8  |#d............#|   stair door d (1,8)
 y 9  |##D############|   mat D (2,9)
```
Legend: `k` kitchen counter, `r` rug, `S` sofa, `i` framed list, `h` photo shelf, `c` locked cabinet, `M` housemaid, `m` Mr., `w` Mrs., `d` stair door, `D` mat. The Gen 4 set has the furniture; the point is the **scale** (an oversized sofa and rug, a cook's counter nobody uses, a window wall with the harbour behind). **Signs:** the framed list of 'things bought' at (9,2): 'THE HOTEL. THE HARBOUR. A CLOUD. (RETURNED)'; the photo shelf at (12,2) with **one gap in the frame** (Gatsby's place; foreshadow); the locked cabinet at (13,3), 'GG' etched. **NPCs:** before the post-game only a **housemaid** (3,3), who says the family is 'at the office, being baffled'. After `FLAG_SYS_GAME_CLEAR` the **post-game epilogue** puts **Mr. Goldsworth at (10,6)** and **Mrs. Goldsworth at (5,7)**, baffled by 'the board' (`PostGame_Text_GoldsworthEpilogue` is Troglodyte's own line, so also put **Troglodyte** at (7,7) with his job joke, per [../../postgame.md](../../postgame.md)). Objects 4 of 15. Music `MUS_LILYCOVE_MUSEUM`.

#### 4.4.7 Roof: Sky Terrace (18 x 12)

Copy `LilycoveCity_DepartmentStoreRooftop` (18 x 12, `gTileset_Shop`): two satellite dishes (props, the render's dishes), a **helipad painted with an enormous G** (a painted circle at cols 6-11, rows 4-9; use the Poké Ball centre decal), the wind sock (a sign at (15,2); Tobin's wind sock is visible from here). **Hidden Rare Candy under the helipad** at (8,6). **Stairs down** at (13,3) (the vanilla rooftop's warp tile) lead to 5F's service stair at (17,18). **NPC:** a **helipad attendant** (13,8) who is not sure what lands here. Objects 1 of 15.

### 4.5 Hotel: 'Gildhaven Grand' (Hotel 1F and 2F)

**Source:** the render's white arched hall (cols 33-40, rows 26-30, door (37,30)). **Interior base:** vanilla `LilycoveCity_CoveLilyMotel_1F` and `_2F` (12 x 9, `gTileset_GenericBuilding`, motel owner at (10,3), mats (5,8),(6,8), stairs (2,1)) kept as the layout, **or** repainted in `gTileset_Gen4Interior` to match the house style (recommended; the Hollowbrook homes use it). The **free rest** (the receptionist says 'compliments of the house', which it is not) uses the vanilla motel script (a sleep-and-heal). Receptionist at (10,3) facing down; a bellhop (4,5) wandering; a guest on 2F (8,4) who says the room view is 'of a wall'. 2F: four bed alcoves; stairs (2,1) down.

### 4.6 Pilots' Club (12 x 14)

**Source:** Palladium `Trainer School.png` (192 x 224 px, no grid, **12 x 14**: the same size as vanilla `LilycoveCity_PokemonTrainerFanClub`). **Tileset** `gTileset_Gen4Interior` (the classroom desks, blackboard and bookshelf are the Gen 4 set's furniture). Mat **(5,13)** and (6,13). The blackboard on the top wall becomes a **flight chart**: sign at (5,2). **NPCs (4):** **pilot friend** (3,5) facing right (teases Tobin, warns that R20 is for nine-badge holders), a **cadet** at the front desk (8,5) facing left, a **map-reader** at (9,8), a **wind-sock maker** at (2,10). Items: none. Objects 4.

### 4.7 Casino (20 x 16)

**Source:** Palladium `casino2-2.png` (342 x 272 px with a grid, `(342-1)/17 = 20.06`, `(272-1)/17 = 15.9`: **20 x 16**). The render shows two prize and exchange counters on the top wall (left x 1-5, right x 14-18), a central terminal/poster at (12,1), **two double banks of slot machines** (cols 6-9 and 11-14, rows 6-11) with blue stools, two green game tables at (17,7),(17,10), plants and stools on the left (col 1, rows 5-12) and the red entry mat at **(3,15)**. **Tileset** `gTileset_MauvilleGameCorner` (the vanilla Mauville Game Corner's set, 22 x 11 there) so slot machine, counter and prize-counter metatiles exist. Reuse the vanilla scripts (`MauvilleCity_GameCorner`: coin case, slots, prize counters). **PROPOSED: this is optional** (Open question 6). **Goldsworth hook:** the casino is owned by 'Goldsworth Leisure'; the manager's line is that Troglodyte lost 4,000 coins to a Pokémon. **NPCs (6):** coin clerk (2,2), prize clerk (16,2), manager (9,3), two gamblers (7,9),(12,9), a croupier at (17,8). **Prizes:** vanilla table (TMs are covered by the Emporium). Music `MUS_GAME_CORNER`.

### 4.8 Houses (Gen 4 Interior, primary `gTileset_Building`)

Template **N** = `Hollowbrook_NeighboursHouse` (11 x 8, built; mat (2,7); bookshelf signs (7,2),(8,2); free floor for NPCs at x 1-9, y 3-6; the built NPCs sit at (5,6), (8,3), (9,5), (2,4)). **Duplicate Map** from it (shared painting only if the rooms are meant to be identical) and move objects as listed.

| Map | Door (outdoor) | Template and size | Interior in words | NPCs (tile, facing) |
|---|---|---|---|---|
| `Gildhaven_NavigatorsHouse` | (13,15) | N, 11 x 8 | charts on the wall (the top wall's window turned into a map frame), a table with a compass, kitchen left | **retired navigator** (8,3) facing up; his **wife** (5,6) facing up |
| `Gildhaven_CleanersFlat` | (14,29) | S, 10 x 8 (Gen 4 single room: bed top-left, kitchen bottom-right, rope and bucket on the wall) | a single room, a bed, a rope coil and a squeegee as decor | **window cleaner's partner** (6,4) facing down; a **Skitty** (2,5) |
| `Gildhaven_MoveDeletersHouse` | (49,36) | N, 11 x 8 (mat (3,7) rather than (2,7)) | cluttered, a wall of crossed-out lists | **Move Deleter** (4,4) facing down (vanilla `LilycoveCity_MoveDeletersHouse`: object at (4,4), `LAYOUT_HOUSE2` uses mat (3,7),(4,7)) |
| `Gildhaven_SalesOffice` | (42,11) | 11 x 8, **Little Office** | a **scale model of Gildhaven** on a table (glass pieces) with the gym removed, two clerks | **sales clerk** (5,4) facing down; a **model-maker** (8,5) facing left |
| `Gildhaven_Cafe` | (40,41) | 11 x 8, Gen 4 Interior | counter at cols 1-4 top-left, four tables, a quiet booth; Brick Cafe is the optional upgrade (section 9) | **owner** (2,3) facing right; two **customers** (6,5) and (8,6) |

NPC topics are in the card ([../towns/gildhaven.md](../towns/gildhaven.md)); the Cafe is new (PROPOSED): owner sells a **free drink** (a berry) for a chat, customers gossip about 'the lad who sulks past'.

## 5. Scheme 6: the gift basket (placement; beats are in the card)

Coord-event triggers (CLAUDE.md), not `OnTransition`. All on `Gildhaven` and keyed by `VAR_GILDHAVEN_STATE` (proposed meaning in the card):

| Beat | Tile and positions |
|---|---|
| **Setup** (any time in town before the gym) | **Two basket porters** carry a sofa-sized basket across the plaza from (29,19) to the forecourt: they walk to (24,13) and (26,13) and set the **basket object** down at **(25,13), across the gym door**. The basket is an object (blocking). |
| **Reveal trigger** | `coord_event` on the forecourt tiles **(24,15), (25,15), (26,15)** (3 wide, just before the basket). **Mr. Goldsworth** walks to (24,14), **Mrs. Goldsworth** to (26,14), **Whitmore** to (23,14) from the avenue at (31,16). **TOBIN** steps out of the door (25,12), the basket blocks (25,13), so he walks round to **(27,13)** beside the tub (28,13). |
| **Collapse** | Tobin explains twice; the parents tip him (a folded note); they sit on the **bench at (22,14)** 'for the receipt'; the basket is cleared (to the Center, where the nurse eats the biscuits). |
| **Troglodyte fight 5** | He enters from the avenue at (31,16), walks to (25,15) facing north. Fought with the parents watching from the bench. Team: Stoutland 'Sir Biscuit' 37, Vaporeon 38, Gardevoir 38, Pyroar 39, plus the starter final stage at 40 ([../towns/gildhaven.md](../towns/gildhaven.md)). |
| **After** | the parents leave towards the tower (they walk south-east along the avenue and despawn at (31,17)); the gym door is open; Tobin: 'in you come'. |

## 6. NPCs in town (outdoors, 14; max 15 live objects)

| # | Role | Tile, movement | Topic |
|---|---|---|---|
| 1 | Gate guard, north | (31,4) face down | R18 road works: closed for resurfacing; once the Feather Badge is held he waves you through |
| 2 | Gate guard, south | (31,48) face up | nine-badge check |
| 3, 4 | Basket porters | start (29,19); end (24,13) and (26,13) | Scheme 6 setup; complain about the stairs |
| 5 | Window cleaner | (47,15), facing the tower | 'Don't look up.' Recites what he sees through the glass |
| 6 | Harbourmaster | (53,26) face east | Surf hint: open water east is R19 |
| 7 | Glossy shopper | (28,22) wander | loves the tower |
| 8 | Commuter | (36,20) look around, in a hurry | late for everything |
| 9 | Jogger | (38,5) wander | 'saw Troglodyte sulk past' |
| 10 | Wingull ambient (Pokémon) | (53,25) face down | none |
| 11 | Child on the plaza | (47,24) wander | tries to climb the plinth |
| 12 | Gym guide | inside the gym | see 4.3 |
| 13 | Tobin | gym, and on the forecourt for Scene 1 | |
| 14 | The statue plinth sign | (47,25) sign | 'In memory of nobody in particular' |

Objects on `Gildhaven` itself: 10 live (guards, porters when present, cleaner, harbourmaster, shopper, commuter, jogger, wingull); the others live in the gym or are scene-only. Keep the Scheme 6 actors on the **same** map with hide flags so the object count never exceeds 15.

## 7. Items and secrets (positions)

| Item | Where | Gate |
|---|---|---|
| **HM Fly, TM Aerial Ace** | Tobin, (7,4) in the gym | the Feather Badge |
| **Amulet Coin** | Mrs. Goldsworth, Tower 5F | after the gym |
| Nugget (hidden) | fountain or round bed on the Estates Lawn (36,3), a hidden item tile | none |
| Max Revive (hidden) | behind the Emporium (21,34) | none |
| Ultra Ball (hidden) | pier bollard (54,27) | none |
| **Star Piece** | the rock islet (56,33) | Surf |
| Revive | tree in the west cliff garden (9,23) | Cut |
| Max Ether | behind the cracked boulder (4,33) | Rock Smash |
| Big Nugget | shelf behind the Strength boulder (5,43) | Strength |
| PP Up (hidden) | Tower 4F desk (14,2) | none |
| Rare Candy (hidden) | Tower Roof, helipad (8,6) | after Scene 2 (roof opens) |

**Secret: the Programme chart (Tower 3F, signs at (6,1),(7,1)).** It lists the earlier schemes and rewrites a line as the badge count rises ('Crestfall: consultants, pending' becomes 'consultants, returned, MILTANK, ate'); only the first six rows can show before Gildhaven; rows 7 to 9 read 'not yet scheduled'. **Secret: the clean rectangle (Tower 1F, (8,1))**: 'Something large was removed from here. It was not a window.'

## 8. Palette and tile notes

- **Outdoor:** ORAS General (in tree) + **ORAS Lilycove** (new, dual-layer, same ids as vanilla Lilycove, so every `gTileset_Lilycove` map in the tree would also change if both used the same name: **the ORAS Lilycove tileset replaces vanilla's in place**, as the Petalburg and General recolours already did; check no vanilla Lilycove maps are in the build you care about). Roof palette: edit one slot to yellow.
- **Interiors:** Pokémon Center unchanged. Emporium: `gTileset_Shop`. Gym: `gTileset_MossdeepGym` + 2 new arrow metatiles. Tower: Facility, Little Office, Gen 4 Interior. Houses: Gen 4 Interior. Casino: Mauville Game Corner set.
- **To redraw:** the tower (tile art, section 2), the 2 wind arrow metatiles, a gold-roof recolour, a 'G' decal for the helipad.
- **Credits needed in the same commit as each import:** Project Palladium team (the traced renders: `goldenrodcitytiled.png`, `Goldenrod Dept Store 1F.png`, `President's Office Tiled.PNG`, `Violet City Gym.png`, `Trainer School.png`, `casino2-2.png`), leob0505 (extend the existing row with `lilycove`), Ekat and Kumatora (Little Office), Glazed credits already present (Gen 4 Interior).

## 9. Team Aqua tilesets: verdicts

| Tileset (folder under `Tilesets/The Great Tileset Exchange/Full Tilesets/`) | Verdict | Why |
|---|---|---|
| **Little Office Interior Secondary** | **Yes, for 4F and 5F (and the Sales Office)** | I looked at its `example.png`: it is a small cosy office (wooden floor, white counters with files, L-shaped glass desks, PCs, chairs, a fax, calendar, rug, a gable window, stairs). **It is not a glossy skyscraper set**, so it suits the family floors and the Sales Office, not the corporate lobby. 120 triple-layer metatiles (`metatiles.bin` is 2880 bytes = 120 x 24), so it has to be **flattened to dual-layer with Porytiles 2.0** as Gen 4 Interior was (the author did this for Hollowbrook; the recipe is in [../../interiors.md](../../interiors.md)). Credit: Ekat (DeviantArt 'Little Office'), imported by Kumatora, in `CREDITS.md` |
| Brick City Secondary | **Not for Gildhaven** | Red brick, slate roofs, a canal and boats: a lovely look but it reads as Kingsquay or Wendlebury, not a gold-and-glass city. 375 triple-layer metatiles and a note that it is a quick import. Keep for Kingsquay |
| Brick Cafe Interior Secondary | Optional later | Nicer than Gen 4 for the Cafe but 512 triple-layer metatiles to flatten for one room. Not worth it here |
| Gatehouse Secondary / Gatehouse Secondary Alt | **No** | The example is a bike-shop style counter room and the README says it needs expanded metatiles and triple layer. Not a gate |
| Gate Platinum Secondary | **No (not needed)** | The example is a lovely potted-plant gate hall, but Gildhaven's gates are open-road guard lines. Keep it for a gatehouse interior elsewhere; it is triple-layer and expanded |
| LeoB ORAS `lilycove` | **Yes, outdoor** | See section 2 |

## 10. Build checklist (in order)

1. Decide the tower exterior (section 2) and the render orientation (mirrored, decided). Import ORAS Lilycove (CREDITS row) in the commit that first uses it.
2. Trace `Gildhaven` mirrored at 59 x 51, doors per section 3, roofs yellow, the two gates, the harbour quays. Save; Porymap writes `map_groups.json`, `layouts.json`, `event_scripts.s`. **Check `.include` once** and `heal_locations.json` ids ([../../../CLAUDE.md](../../../CLAUDE.md)).
3. Add `MAPSEC_GILDHAVEN` (one new section) and the fly-town row (`src/data/veldris_fly_towns.h` plus the checklist in [../../region-map.md](../../region-map.md): `respawn_map` before `respawn_npc`).
4. Pokémon Center 1F/2F (vanilla layouts), then the Emporium floors (duplicate Lilycove scripts, re-point warps), then the elevator.
5. The Gym: tile the 2 arrow metatiles, paint the hall, place TOBIN and the 3 trainers, test the belts and sight lines in the emulator.
6. The Tower: 1F to 6F and the Roof, in order.
7. Casino (optional), Hotel, Pilots' Club, Sales Office, the 4 houses, the Cafe.
8. Gate scripts (badge count), Scheme 6 scene and Troglodyte fight 5.
9. Dialogue (`python3 design/tools/dialogue_check.py`), `design/` updates (`flags.md`, `engine-edits.md` if any), `CREDITS.md`, `make -j4`, check no ROM staged.

## 11. Open questions

1. **Scene 1: forecourt or office?** `dialogue/goldsworth.inc` (`MrMeet3` ends 'the lift is the shiny door') reads as an office, the card as the forecourt. This document uses the forecourt and the office for Scene 2. Reword `MrMeet3`, or move Scene 1 to the 5F office?
2. **Tower exterior art**: stacked ORAS dept-store windows, stacked museum facade, or new Radio Tower tiles? Test the first two before drawing anything.
3. **Lean tower (4 maps) or full (7 maps)?** This document is the full one; the Penthouse only matters for the post-game epilogue.
4. **Gate buildings.** Doors only exist on a building's south face, so a pass-through gatehouse cannot be entered by someone walking south. This document uses guard lines on plain connections. Do the other groups' cards (routes-west) use two-door interiors? If the author wants gatehouse interiors, they are built from the south-facing side only.
5. **Gym puzzle behaviour** (forced walking, `MB_WALK_EAST`/`WEST`) is **untested** in this build. If a belt does not end cleanly, fall back to Mossdeep-style warp pads.
6. **Casino: keep or cut?** It is a Game Corner (coins only, no prizes of real value) from the vanilla set, so no new system, but it adds the Goldsworth hook and one more map.
7. **Tobin's pronoun in the arc table** ('tip her') versus the roster (a man). I read him as a man.
8. **Palladium Route 35 reuse.** R18 uses `Route 35.png`; the west group (R9) uses it too. Mirror one (see [routes-centre-detail.md](routes-centre-detail.md)).
