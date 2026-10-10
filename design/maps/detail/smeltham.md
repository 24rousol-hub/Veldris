# SMELTHAM: detailed design (town, place 6, gym 4 Steel)

Status: **PROPOSED** (written 2026-10-01). Nothing here is built. It adds detail to the card [../towns/smeltham.md](../towns/smeltham.md) and does not change its facts (species, levels, trainer lists, items, flags). Choices I had to make are marked **PROPOSED**; render-versus-card conflicts are marked **FIX**. Sources I used: the card, [../interiors/README.md](../interiors/README.md), [../interiors/catalogue.md](../interiors/catalogue.md), the Hollowbrook interiors in [../../interiors.md](../../interiors.md) (house style), the Palladium renders `Mahogany Town.png` (the town) and `Olivine City Gym.png` (the gym), the vanilla layouts and tilesets in this tree, and the Team Aqua tilesets named below. Gym: [../../gyms.md](../../gyms.md), leader HAGANE ([../../leader-names.md](../../leader-names.md), [../../trainer-roster.md](../../trainer-roster.md)). Scheme 4: [../../troglodyte-arc.md](../../troglodyte-arc.md). Roads: [routes-west-b.md](routes-west-b.md). Mine: [landmarks-west-detail.md](landmarks-west-detail.md).

**Coordinates.** Every `(x, y)` is a tile, x from the left, y from the top, 0-based. Outdoor positions are read by eye from the render (`Mahogany Town.png` is 390 x 406 px with no grid, so 24 x 25 tiles at 16 px) **moved into the widened map by +5 rows** (see section 2) and can be 1 or 2 tiles off: treat them as 'about here'. Interior coordinates are mine and exact.

## At a glance

| Item | Value |
|---|---|
| Outdoor map | `Smeltham`, **36 x 30** (the render widened east by 12 and made 5 taller). Size check (36 + 15) * (30 + 14) = 2,244 of 10,240 |
| Section | new `MAPSEC_SMELTHAM`. Fly point and heal location: yes |
| Tilesets (outdoors) | primary `gTileset_General`, secondary `gTileset_Rustboro` (vanilla, the card's vanilla base) |
| Weather | `WEATHER_SHADE` (overcast, a header setting). Optional `WEATHER_VOLCANIC_ASH` instead (grey flakes falling everywhere; moody, but constant) |
| Music (existing Hoenn track, PROPOSED) | `MUS_RUSTBORO` outside, `MUS_GYM` in the gym |
| Connections | south edge to R5 (a 4-wide gap, x 10 to 13); east edge to R6 (the lane at y 17 to 19) |
| Interiors | Center 1F and 2F, Mart, gym, mine office, 3 houses = 8 maps |
| Objects outdoors | 11 at the Scheme 4 scene (limit 15) |
| Level at arrival and departure | about 28 and about 32 |

## 1. Description

**First glance, from R5 (the south).** The road ends under a cliff and you step out of a 4-wide gap into a wide, sand-coloured lane. In front of you is a small town squeezed between rock walls and a **foundry**: a grey square-roofed hall at the top (the gym, with a wide stair and two iron posts at its door), a smoke column behind it, and on the right the chain-link fence of the yard with two chimneys and a crane. Everything is grey, tan and soot-brown. It is late morning and a bell rings somewhere for a tea break that never seems to end.

**First glance, from R6 (the east).** You come in down the yard lane at y 17 to 19, between the fenced north yard (crates and the crane) and the south yard (slag heaps, the mine office). Ahead, the grey gym and the red-roofed Center.

**Mood.** Smoke, clanging and tea. A foundry town, politely exhausted. Everyone is always on a break.

**Colour.** Slate grey, tan sand, soot brown, a rust-red Center roof, the pale blue Mart, the yellow of the gym's stair rails.

**Sound.** A faint clang (a repeating sound effect, optional), steam, the Rustboro track.

**Time of day.** Overcast late morning, permanent.

**The memorable view.** Standing on the gym steps at (11, 10), looking down the sand square to the Center with the yard fence and the crane on the right and the smoke column over everything.

## 2. Street layout in words (a numbered walk)

**How the render becomes the map.** The render is only 24 x 25. **FIX/PROPOSED** (card open question 1: yes, widen): the map is **36 x 30**. Put the render at **x 0 to 23, y 5 to 29** (every render coordinate gets +5 in y), use the top 5 rows (y 0 to 4) for cliffs, pines and the chimneys' tops, and make **x 24 to 35, y 5 to 29 the foundry yard** (new). The text below gives map coordinates (render + 5 rows). All tile positions are 'about'.

1. **The south lane and the R5 gap.** The render's sand lane runs along the bottom of the town (map y 25 to 27, x 3 to 23) under a rock wall (y 28 to 29). **PROPOSED:** cut a **4-wide gap at x 10 to 13** through the bottom rock (y 28 to 29) so the lane reaches the south edge: the R5 connection (R5's lane x 12 to 15 maps to Smeltham x 10 to 13: offset -2). A sign at (11, 27): `SMELTHAM. PLEASE MIND THE CRANES. THEY MIND YOU`. REPEL hidden at (12, 27).
2. **The Mart (bottom-left).** The big building x 4 to 10, y 20 to 24, door **(7, 24)**, arrival (7, 25). An old shop sign at (3, 24) (the render's small sign): `STEEL & SUNDRIES. SINCE BEFORE THE KETTLE`.
3. **The Pokémon Center (bottom-right of the square).** x 16 to 20, y 21 to 24, **door (18, 24)**, arrival (18, 25). The heal location is that arrival tile.
4. **The sand square.** The middle of the town, x 5 to 17, y 11 to 19, wide and sand-coloured, cut by short one-tile **ledges** (hop down only) at **y 14 (x 4 to 6 and x 7 to 11)** and **y 21 (x 2 to 3 and x 13 to 15)**. POTION visible at (9, 15). The two lunch workers stand on it.
5. **The gym (top).** The grey flat-roofed hall at **x 8 to 14, y 5 to 9**, with a wide stair down to the square; **door (11, 9), arrival (11, 10)**. Two iron bollards at (9, 10) and (13, 10). A row of pines on its right, x 14 to 18, y 5 to 9. The gym sign at (13, 11): `SMELTHAM FOUNDRY GYM. LEADER: HAGANE. WORKERS ARE AT LUNCH. BACK AT ONE. PROBABLY`.
6. **The terrace houses.** Two thatch-roofed houses on a raised terrace east of the stair: **House A** at x 11 to 15, y 14 to 16, **door (13, 16)**, and **the Canteen** (House B) at x 19 to 23, y 14 to 16, **door (21, 16)**. ANTIDOTE hidden behind the terrace wall at (16, 13). A sign at (10, 16): the town sign.
7. **House C (the scrap collector).** **PROPOSED:** in the west lane stub the render leaves open (x 0 to 8, y 15 to 17): a small house at x 3 to 7, y 15 to 17, **door (5, 17)**, arrival (5, 18). This closes the stub the card says to close. A sign at (8, 17): `ORE & SCRAP. NOT A SHOP. DO NOT ASK`.
8. **The foundry yard (new, east).** A chain-link fence along x 24 (y 5 to 29) with one open **gate at the lane (24, 17 to 19)**; the lane is the road to R6. **North yard (x 25 to 35, y 5 to 16):** two **chimneys** at (28, 6) and (32, 6) (tile art or a tall tile column), a **crane** at (30, 10) (tile art, 2 wide and 5 tall, see Palette notes), crates at (26 to 27, 12 to 13), two slag-grey trucks parked at (26, 14) and (31, 14) (objects), a **Strength boulder** at (33, 8) guarding a small recess (x 34 to 35, y 6 to 8) with the METAL COAT at (34, 7): the player stands at (33, 9) and pushes the boulder north to (33, 7), which clears the way in. **South yard (x 25 to 35, y 20 to 29):** the **mine office** at x 25 to 29, y 21 to 24 (door **(27, 24)**, arrival (27, 25)), ore heaps (Rock Smash rocks at (28, 27), (30, 25) and (33, 26): HARD STONE hidden behind the one at (33, 26)).
9. **The R6 lane.** Sand along y 17 to 19 from the square (x 17) through the yard gate to the east edge (x 35). The R6 connection: Smeltham's lane **y 17 to 19** maps to R6's west sand **y 11 to 13** (offset 6).
10. **The cliffs.** The render's rock on the left (x 0 to 4, y 5 to 11 and y 21 to 29) and on the right (x 20 to 23, y 21 to 29) stays. Pines at the top right.

Water: none. Ledges: two. Trees: pines top and right.

## 3. Every building

Map names are PROPOSED (group `gMapGroup_IndoorVeldris`, section `MAPSEC_SMELTHAM`). **Kit** means the Hollowbrook furniture vocabulary (copy blocks from the built maps in Porymap): `Hollowbrook_NeighboursHouse` (11 x 8): kitchen x 0 to 3, y 1 to 2; window pair x 5 to 6, y 0 to 1; bookshelf x 7 to 8, y 1 to 2; TV table with cushions x 5 to 8, y 4 to 6; plant column x 10, y 4 to 6; exit mat (2, 7). `Hollowbrook_PlayersHouse_2F` (13 x 8): bed x 1 to 2, y 1 to 3; PC desk x 4 to 5, y 1 to 3; TV stand x 9 to 10, y 1 to 3; 3 x 3 rug x 5 to 7, y 4 to 6; plants (0, 5 to 6), (12, 5 to 6). `Hollowbrook_ProfFennickLab` (14 x 12): dome machine at x 1 to 2, y 4 to 6, instrument cabinet at x 11 to 12, y 4 to 6, desks and stools.

| Building | Map | Layout and tileset | Size | Palladium image | Notes |
|---|---|---|---|---|---|
| Pokémon Center 1F, 2F | `Smeltham_PokemonCenter_1F`, `_2F` | **vanilla** `LAYOUT_POKEMON_CENTER_1F`, `_2F` | 14 x 9, 14 x 10 | `newcenter.png` as reference only | shared |
| Mart | `Smeltham_Mart` | **vanilla** `LAYOUT_MART` | 11 x 8 | none | shared |
| Gym | `Smeltham_Gym` | custom: `gTileset_Building` + `gTileset_TrickHousePuzzle` | 13 x 20 | `Olivine City Gym.png` | assembly-line belts |
| Mine office | `Smeltham_MineOffice` | Gen 4 Interior | 11 x 8 | `Elm's House.png` | the clerk, the Slagwell map |
| House A (terrace) | `Smeltham_HouseA` | Gen 4 Interior | 11 x 8 | `Elm's House.png` | retired foreman |
| Canteen (House B) | `Smeltham_Canteen` | Team Aqua **Brick Cafe Interior Secondary** (fallback Gen 4) | 13 x 10 | none | two workers, an eternal lunch |
| House C | `Smeltham_HouseC` | Gen 4 Interior | 11 x 8 | `Elm's House.png` | scrap collector |

### 3.1 `Smeltham_PokemonCenter_1F` and `_2F` (vanilla)

`LAYOUT_POKEMON_CENTER_1F` (14 x 9): nurse at (7, 2) facing down (the **first object**), door pair (6, 8) and (7, 8), stairs warp (1, 6). 2F: 14 x 10. **Never move the nurse or counters** (rule 2). NPCs: the vanilla 1F gentleman at (4, 4) is a **tired smelter** ('I have been on tea for six hours'), the boy at (10, 6) a **gym fan**, the girl at (3, 7) vanilla's. A traveller can mention 'a rich boy asked who owned the smoke' (optional Troglodyte sighting). Warps: (6, 8) and (7, 8) to `Smeltham` warp 0.

### 3.2 `Smeltham_Mart` (vanilla)

`LAYOUT_MART` (11 x 8): clerk at (1, 3) facing right, door pair (3, 7) and (4, 7), vanilla woman at (5, 5), boy at (9, 4). Stock (card): POKÉ BALL, GREAT BALL, POTION, SUPER POTION, ANTIDOTE, BURN HEAL, PARALYZE HEAL, REPEL. Plain, no special shelf. Warps: (3, 7) and (4, 7) to `Smeltham` warp 1.

### 3.3 `Smeltham_Gym`: see section 5

### 3.4 `Smeltham_MineOffice` (11 x 8, Gen 4 Interior)

The Slagwell Mine's office. **Kit:** kitchen block at x 0 to 3, y 1 to 2 (the kettle); window pair x 5 to 6; a **large map of the mine** (a `bg_event` on the wall at (8, 1), using the window or shelf block): `SLAGWELL MINE. YOU ARE HERE. SO ARE THE ORE CARTS`; a **desk** at x 6 to 8, y 3 to 4 (use the 2F PC desk kit, no PC), a row of **hard hats** on a shelf at x 8 to 9, y 1 (the shelf block); plant column x 10, y 4 to 6; exit mat (2, 7).
- **NPC (1):** the **mine clerk** at (7, 5) facing north behind the desk. Explains that R7 is the way to the mine (the gate opens with Strength or a Rock Smash TM: a hint, not a hard gate, card). After the player has entered Slagwell (`FLAG_SLAGWELL_VISITED`) he gives **TM Rock Tomb** (card).
- **Warps:** (2, 7) to `Smeltham` warp 6, landing (27, 25).
- **Open question 4 of the card:** a second door from the office into the mine. **Answer: no.** Keep R7 the only way in; one door per place keeps the mine's items on the revisit loop.

### 3.5 `Smeltham_HouseA` (11 x 8, Gen 4): the retired foreman

Kit: kitchen top-left, window, bookshelf at x 7 to 8, a **long chair** (two cushions) at (6, 4) and (7, 4) where the foreman sits, plant column, mat (2, 7). A framed photo `bg_event` at (4, 1): `THE 1ST SHIFT. EVERYONE ON TIME. NO ONE ON TIME EVER AGAIN`. NPC (1): the **foreman** at (5, 4) facing east: the story of the last strike that ended by tea. Warps: (2, 7) to `Smeltham` warp 3, landing (13, 17).

### 3.6 `Smeltham_Canteen` (13 x 10, Brick Cafe Interior): the eternal lunch

- **Tileset: Team Aqua Brick Cafe Interior Secondary** (`Tilesets/The Great Tileset Exchange/Full Tilesets/Brick Cafe Interior Secondary/`). What it adds over the house style: a red-brick cafe wall with lamps and arched windows, a long counter, tall mugs and a **kitchen, tables with chairs on a blue rug**, a black-and-white checker floor (see its `example.png`): a perfect works canteen. Cost: triple-layer, so a Porytiles bake like Gen 4 Interior ([../../interiors.md](../../interiors.md)) and a `CREDITS.md` row: **Ekat (Ekat99, 'Brick Cafe', DeviantArt, public use for non-commercial projects, credit requested), Vurtax (FRLG rips), Heartlessdragoon (RSE rips); imported to pokeemerald by Kumatora** (read the folder's `Credits.md`). If the author declines: Gen 4 Interior with the kitchen block and two tables built from the TV-table kit; still a room, not a canteen.
- **Layout (13 x 10):** top wall y 0 to 2 with two arched windows at x 2 to 3 and x 7 to 8; a **long counter** along y 3 at x 1 to 6 with the kitchen behind it at y 1 to 2; a **tea urn** (the mugs block) at (8, 3); tables with chairs at x 3 to 5, y 5 to 6 and x 8 to 10, y 5 to 6 (copy the example's table-and-chair blocks); a plant at (11, 3); exit mat **(6, 9)**.
- **NPCs (3):** a **worker on lunch** at (4, 4) facing south, a **second worker on lunch** at (9, 4) facing south (the card's 'two workers on break'): both say they are 'back at one' and it is 'about one'; the **cook** at (3, 2) behind the counter facing south, who pours tea but has no shop.
- **Warps:** (6, 9) to `Smeltham` warp 4, landing (21, 17).

### 3.7 `Smeltham_HouseC` (11 x 8, Gen 4): the scrap collector

Kit: kitchen top-left, window, a **workbench** at x 5 to 8, y 1 to 2 (use the lab's shelf and desk block), a heap of scrap (the instrument cabinet block at x 9 to 10, y 1 to 3 and the dome machine block at (1, 4) to (2, 6) as 'a thing he is building'), a low table with cushions at x 4 to 5, y 5 to 6, mat (2, 7). NPC (1): the **collector** at (5, 4) facing south: gives a trade or a flavour item (card, no item defined). Warps: (2, 7) to `Smeltham` warp 5, landing (5, 18).

## 4. Door and warp table

Outdoor `Smeltham` warps (id: tile, destination). Exit warps land on the arrival tile.

| id | Tile | Destination | Arrival after exiting |
|---|---|---|---|
| 0 | (18, 24), Center | `Smeltham_PokemonCenter_1F` (6 and 7, 8) | (18, 25) = **the heal location tile** |
| 1 | (7, 24), Mart | `Smeltham_Mart` (3 and 4, 7) | (7, 25) |
| 2 | (11, 9), gym | `Smeltham_Gym` (6, 19) | (11, 10) |
| 3 | (13, 16), House A | `Smeltham_HouseA` (2, 7) | (13, 17) |
| 4 | (21, 16), Canteen | `Smeltham_Canteen` (6, 9) | (21, 17) |
| 5 | (5, 17), House C | `Smeltham_HouseC` (2, 7) | (5, 18) |
| 6 | (27, 24), Mine office | `Smeltham_MineOffice` (2, 7) | (27, 25) |

Edges: **south** edge (x 10 to 13) to `Route5` (north edge, its x 12 to 15), offset -2; **east** edge (y 17 to 19) to `Route6` (west edge, its y 11 to 13), offset 6.

## 5. The gym (STEEL, HAGANE, RIVET BADGE)

**`Smeltham_Gym`, 13 x 20.** Built from `Olivine City Gym.png` (176 x 320 px with no grid, so 11 x 20 at 16 px): a narrow hall with a raised terrace at the top (x 2 to 9, y 3 to 7) and steps, a sandy central strip between rocky sides, two Poké Ball statues and a mat at the bottom. I **widen it to 13** (two more columns) so four lanes fit, and keep the terrace, the steps, the two statues and the mat in the same places in proportion.

**Tilesets: primary `gTileset_Building`, secondary `gTileset_TrickHousePuzzle`** (vanilla). It is the Trick House puzzle set: grey metal floors, walls, and **arrow tiles that move the player** (conveyor belts). I read the tileset's behaviours: metatile indices **96 and 124 are `MB_WALK_EAST`, 97 and 123 are `MB_WALK_WEST`, 98 is `MB_WALK_NORTH`, 99 is `MB_WALK_SOUTH`** (the 'SLIDE' versions are faster). Add 0x200 for the id in map data. Open `Route110_TrickHousePuzzle1` in Porymap to see the pieces. This answers the card's open question 3: **no new tile art; the belts are vanilla**. No import, no credit row beyond Palladium. (Alternative if the look is wrong: the FRLG `gTileset_ViridianGym` has spinner arrows; untested in Emerald.)

### The floor, tile by tile

Legend (x 0 to 12 across, y 0 to 19 down): `#` wall or machine (impassable), `.` floor (a **rest cell** where you can stop and step off), `>` `<` conveyor belt east or west (forced walk), `G` a **gap** in a machine row (floor; the **true** one, leads up), `X` a **gap that is a press** (floor with a hazard trigger; fake), `S` steps up (walkable), `L` HAGANE, `T` trainer, `s` a Poké Ball statue (`bg_event`), `m` the exit mat.

```
x     0         1
      0123456789012
y  0  #############
y  1  #############   (top wall; lights and vents)
y  2  #...........#
y  3  #.....L.....#   HAGANE at (6, 3), the terrace x 1 to 11, y 2 to 4
y  4  #...........#
y  5  #####S#######   steps at (5, 5)
y  6  #X###G##X##X#   gaps at x 1 (press), 5 (TRUE), 8 (press), 11 (press)
y  7  #.<<<.<<.<<.#   lane D (belts carry you west)
y  8  #####X##X##G#   gaps at x 5 (press), 8 (press), 11 (TRUE)
y  9  #T>>>.>>.>>.#   lane C (east); T at (1, 9)
y 10  #X###G#####X#   gaps at x 1 (press), 5 (TRUE), 11 (press)
y 11  #T<<<.<<.<<.#   lane B (west); T at (1, 11)
y 12  #####X##G##X#   gaps at x 5 (press), 8 (TRUE), 11 (press)
y 13  #.>>>.>>.>>T#   lane A (east); T at (11, 13)
y 14  #...........#
y 15  #...........#
y 16  #..s.....s..#   statues at (3, 16) and (9, 16)
y 17  #...........#
y 18  #...........#
y 19  ######m######   exit mat at (6, 19)
```

(Each `T` stands on a rest cell at the end of a lane: (1, 9), (1, 11) and (11, 13).)

**Every lane has the same six cells repeating:** a rest cell at x 1 (west end), belts at x 2 to 4, a rest cell at x 5, belts at x 6 to 7, a rest cell at x 8, belts at x 9 to 10, a rest cell at x 11 (east end). **East lanes (A and C)** use `>`, **west lanes (B and D)** use `<`. A belt chain always **ends on a rest cell** (the belt at x 4 carries you to x 5, the pair at x 6 to 7 to x 8, the pair at x 9 to 10 to x 11, and the west lanes mirror that), so no belt is ever blocked and nobody is stuck.

**The puzzle: pick the true gap on each of the four lines.** Enter lane A from the start hall by stepping north from any tile of y 14 onto y 13: a belt tile carries you to the next rest cell (from x 2 to 4 you end on x 5, from x 6 to 7 on x 8, from x 9 to 10 on x 11), a rest cell lets you stay. Then step north through a gap:

| Line | Y | Belt direction | True gap | How you get there |
|---|---|---|---|---|
| A | 13 | east | **(8, 12)** | enter on a belt at x 6 or 7 (or the rest cell x 8 directly), stop on the rest cell (8, 13), step north |
| B | 11 | west | **(5, 10)** | from the arrival rest cell (8, 11), step west onto the belts at x 7 and 6: you stop on (5, 11), step north |
| C | 9 | east | **(11, 8)** | from (5, 9) step east: the belts carry you to (8, 9), step east again: to (11, 9), step north |
| D | 7 | west | **(5, 6)** | from (11, 7) step west: you stop on (8, 7), step west again: to (5, 7), step north through (5, 6) to the steps (5, 5) |

**The presses.** Every other gap (`X`) is a **press**: the player steps into it, a `coord_event` trigger plays a clang and `The press drops. The line spits you out.`, then `warpteleport MAP_SMELTHAM_GYM, 6, 18` puts the player back at the start of the hall. The cost of a wrong gap is a short walk back, no damage. **Clues:** a **hazard stripe** tile on a press gap if the tileset has one (check the Trick House set), otherwise nothing; the workers' dialogue gives the true gaps (below).

### Gym trainers (3, from the card, positions PROPOSED)

| Class | Team | Stands at | Faces | Sight | Why there |
|---|---|---|---|---|---|
| Hiker | BRONZOR 25, ARON 26 | (11, 13) the east end of lane A | west | 3 | sees the rest cell (8, 13), where the player stops before the first gap: the first fight |
| Black Belt | MACHOP 26, TIMBURR 26 | (1, 11) the west end of lane B | east | 4 | sees the rest cell (5, 11) where line B ends: the second fight |
| Guitarist | MAGNEMITE 26, KLINK 27 | (1, 9) the west end of lane C | east | 4 | sees the rest cell (5, 9) where the player enters line C: the third fight |

(Levels 25 to 27 are three to four below HAGANE's lowest of 29, as the rule says.) The trainers stand on rest cells at the **ends** of lanes, never on the true route, so they never block a belt. **Test in the game:** a trainer's sight is checked when the player has stopped; I placed each one to see a rest cell the player must stop on, so the fight is unavoidable. If a trainer does not spot the player at the stop, add a `coord_event` on the rest cell that starts the fight.

**Worker dialogue (the clues, PROPOSED).** The Hiker, after the fight: 'First line, the third bay. I never use the others. They crush.' The Black Belt: 'Second line, the middle bay. Do not go left. Or right.' The Guitarist: 'Third line, all the way east. Then up.' HAGANE: 'The last line is the middle bay again. We keep it simple. We are on a break.'

**Workers on lunch.** Three `bg_event` lunchboxes on rest cells (2 to 3 in the start hall: at (2, 15), (10, 15), (6, 17)): 'A LUNCHBOX. IT HAS NOT BEEN OPENED. IT HAS BEEN WAITING SINCE ONE.' Nothing else.

**Objects:** HAGANE, 3 trainers = 4. Limit 15: fine.

### Scripts and flags for the gym

- `OnTransition`: nothing special.
- Press triggers: 9 `coord_event`s (no var), each `warpteleport` to (6, 18). They are at `X` gap cells: (1, 6), (8, 6), (11, 6), (5, 8), (8, 8), (1, 10), (11, 10), (5, 12), (11, 12).
- HAGANE: the leader pattern copied from `data/maps/RustboroCity_Gym/scripts.inc` (without its rematch branch, see CLAUDE.md); reward badge 4, HM Strength, TM Iron Tail; `FLAG_BADGE04_GET`, `FLAG_RECEIVED_HM_STRENGTH` reused.

## 6. Scheme 4 (outdoor staging)

All positions are on `Smeltham` and PROPOSED. A **`coord_event` trigger** (not `MAP_SCRIPT_ON_TRANSITION`, CLAUDE.md) on the three tiles **(10, 10), (11, 10), (12, 10)** just in front of the gym door fires the scene; state var (name PROPOSED `VAR_SMELTHAM_STATE`, not claimed): 0 before, 1 after. The tiles must be walkable and at elevation 3.

**Before (objects present at state 0):**
- The **sticker man** (hard hat) at (12, 11), facing south, sticking numbered stickers on the bollards.
- **Site supervisor Mr Quill** (PROPOSED name) at (14, 10), facing west, suit and hard hat: 'This building is to be declared scrap.'
- The **crane operator** at (30, 12), facing south (in the north yard, beside the crane).
- Two **trucks** (`OBJ_EVENT_GFX_TRUCK`) at (26, 14) and (31, 14), marked 'GOLDSWORTH SALVAGE' (the R6 lorry's twins).
- The **foreman's work Pokémon**: a MAGNEZONE (an overworld object `OBJ_EVENT_GFX_SPECIES(MAGNEZONE)`; `graphics/pokemon/magnezone/overworld.png` exists in the tree) at (33, 16), hovering by the yard fence, idle. **Decision recorded:** the author fixed that the scheme Pokémon are cutscene-only and belong to a staff member or local ([../../troglodyte-arc.md](../../troglodyte-arc.md), 'Cutscene-only Pokémon'); here it belongs to the **foreman** (the retired foreman's old working partner), so HAGANE's battle team (BRONZOR, PAWNIARD, TINKATUFF) does not change. **This answers the card's open question 2.**
- Two **lunch workers** on the square at (9, 17) and (13, 18).

**The beat (4 steps):**
1. *Setup.* Stepping on a trigger tile: the sticker man holds up a final sticker, Quill reads a form: 'Tagged, numbered, scrap.' Stickers on the beams are the props (4 `bg_event`s on the gym's stair rails reading `4001`, `4002`...).
2. *Reveal.* Quill: the whole foundry is to be hauled off by crane for a cheap sale. A phone call: a hint of 'the family'.
3. *Collapse.* The MAGNEZONE (a free Pokémon of the retired foreman, who is standing in the doorway of House A, (13, 17)) rises, flies along y 17 to 19 west to the crane at (30, 10), takes hold of it, drags both trucks along the lane (the two truck objects `applymovement` west along y 16 to (14, 12) and (16, 12)), and folds crane, trucks and Quill's clipboard into one grey cube at **(14, 12)**: a single large object (suggested sprite: the `OBJ_EVENT_GFX_BIG_REGIROCK_DOLL` or a new 2 x 2 cube; **PROPOSED**), with a **receipt** pinned to it (`bg_event` on the cube: `RECEIPT: 1 CRANE, 2 TRUCKS, 1 SCRAP ORDER. PAID IN FULL. THANK YOU`). The crane's tiles are replaced with ground by `setmetatile` (if the crane is tile art; the author's choice, see Palette notes). The crew leaves east. Set `FLAG_SMELTHAM_SCHEME_DONE`.
4. *Aftermath.* The cube stays as scenery (card). Quill reappears at (16, 20) with a bouquet and apologises; the foreman says tea is on him. The lorry on R6 and the cart on R7 change (see [routes-west-b.md](routes-west-b.md)). No Troglodyte fight here (his fights are at gyms 1, 3, 5, 6, 7).

## 7. NPCs outdoors (11 at the scene)

| # | NPC | Position | Moves | Topic |
|---|---|---|---|---|
| 1 | Sign: town | (11, 27) south entrance | | `SMELTHAM. PLEASE MIND THE CRANES. THEY MIND YOU` |
| 2 | Sign: gym | (13, 11) | | `... WORKERS ARE AT LUNCH. BACK AT ONE. PROBABLY` |
| 3 | Sticker man | (12, 11) | still | before Scheme 4 |
| 4 | Mr Quill | (14, 10) | still | before Scheme 4; after: apologises |
| 5 | Crane operator | (30, 12) | still | an object that vanishes in Scheme 4 |
| 6 | Two lunch workers | (9, 17), (13, 18) | wander in a 2 x 2 box | HAGANE's staff, 'never present when he needs them' |
| 7 | 2 trucks | (26, 14), (31, 14) | | vanish in Scheme 4 |
| 8 | MAGNEZONE | (33, 16) | float | the scene |
| 9 | Item ball: POTION | (9, 15) | | visible |
| 10 | Item ball: METAL COAT | (34, 7), behind the Strength boulder | | visible |
| 11 | Strength boulder | (33, 8) | | pushable |

Inside buildings (no cost outdoors): nurse, clerk, clerk of the mine, foreman, two canteen workers and the cook, the collector, HAGANE and the trainers. After Scheme 4 the sticker man, Quill, the operator, the trucks and the MAGNEZONE leave (cube appears): the town idles at 7.

## 8. Items and secrets (card, with positions)

| Item | Where | Gate |
|---|---|---|
| POTION | (9, 15), near the square | visible, none |
| ANTIDOTE | (16, 13), behind a terrace wall | hidden, none |
| HARD STONE | (33, 26), behind the slag heap rock | hidden, Rock Smash (badge 2) |
| REPEL | (12, 27), the south entrance path | hidden, none |
| METAL COAT | (34, 7), the north yard recess; push the boulder at (33, 8) north to (33, 7) first | Strength (badge 4) |
| HM Strength | HAGANE | badge 4 |
| TM Iron Tail | gym reward | badge 4 |
| TM Rock Tomb | the mine clerk, after `FLAG_SLAGWELL_VISITED` | none |

## 9. Palette and tile notes

- **Exterior:** General + Rustboro. The gym is the biggest grey Rustboro building (Devon Corp-style flat roof; see `RustboroCity` for the Devon Corp block: copy it for the gym, with a plain door); the terrace houses use Rustboro's grey-blue roofs (the render's thatch roofs do not exist in Rustboro: accept the grey roofs). The sand square is Rustboro's paved path tile in sand; the render's cliffs are Rustboro's rock walls.
- **The yard:** Rustboro has crates, fences, and stacked chimneys on the Devon Corp roof; there is **no crane and no chimney sprite in vanilla**. Options for the author: (a) chimneys as tall narrow wall blocks (the Devon Corp vent block stacked two high); (b) draw one crane (2 wide x 5 tall) in the tileset editor, or build it from the tall antenna block on Mauville's radio tower if it is in the General set; (c) skip the crane and have the MAGNEZONE take 'the trucks and the fence' instead (the card's cube still works). **I recommend (c) for the first pass** because it needs no art; the crane is the only genuine tile-art risk in Smeltham. The cube is an object either way.
- **Weather:** `WEATHER_SHADE`. The smoke column behind the gym is two stacked grey cloud blocks from the Rustboro roof tiles, or nothing.
- **Gym:** the Trick House puzzle secondary on the Building primary.
- **Canteen:** Brick Cafe Interior (see 3.6); everything else Gen 4 Interior.

## 10. Flags (not claimed)

| Name | Meaning |
|---|---|
| `FLAG_VISITED_SMELTHAM` | fly point, set in `OnTransition` |
| `FLAG_SMELTHAM_SCHEME_DONE` | Scheme 4 resolved: crew, trucks, MAGNEZONE leave, cube stays, after-lines |
| `VAR_SMELTHAM_STATE` | 0 before the scene, 1 after |
| `FLAG_SMELTHAM_RECEIVED_*` | one per item, and the mine hint (TM Rock Tomb) |
| `FLAG_BADGE04_GET`, `FLAG_RECEIVED_HM_STRENGTH` | reused, not new |

Nothing is claimed in `design/flags.md`; that happens when built.

## 11. Build checklist (in order)

1. Add `Smeltham` (36 x 30), tilesets General + Rustboro, music, `WEATHER_SHADE`, `MAPSEC_SMELTHAM` (a new section: scarce, [../../engine-limits.md](../../engine-limits.md) limit 3). 2. Trace the render into x 0 to 23, y 5 to 29; paint the 5 top rows of cliff and pine; paint the yard east of x 24 and cut the 4-wide south gap and the east lane. 3. Add the Center 1F and 2F and the Mart (shared vanilla layouts). 4. Add the houses A and C, the canteen and the mine office. 5. Add `Smeltham_Gym` from the grid. 6. Warps in the order of the table. 7. Heal location and fly row: follow the checklist in [../../region-map.md](../../region-map.md) (write `respawn_map` before `respawn_npc` in `heal_locations.json`, and give both; the nurse is the Center's first object). 8. After pulling a duplicated map, grep `src/data/heal_locations.json` for duplicate ids (CLAUDE.md). 9. Connect R5 (south) and R6 (east) once those roads exist. 10. Events, trainers, NPCs; the Scheme 4 cutscene last. 11. Credits: Project Palladium (render); Brick Cafe if imported; in the same commit as each import. 12. Close or reload Porymap before Claude edits event lists. 13. `make -j4` and `python3 design/tools/dialogue_check.py` on any text.

## 12. Build effort

**Medium to hard** (the card agrees). The map is easy once widened. The gym is a **medium** job now that the belts are vanilla (a grid of arrow tiles and nine trigger events). The hard parts are the cutscene (a flying MAGNEZONE, two trucks, a cube) and, if the author wants it, the crane art.

## 13. Open questions

1. **Widen to 36 x 30:** the render is 24 x 25; I moved it to x 0 to 23, y 5 to 29 and made the yard east. OK?
2. **MAGNEZONE** (card question 2): decided by the author as cutscene-only and the foreman's work Pokémon, per [../../troglodyte-arc.md](../../troglodyte-arc.md). I used that. Confirm the foreman owns it.
3. **Belts** (card question 3): vanilla Trick House conveyors, no new art. Confirm, or look at the Viridian-spinner alternative.
4. **The mine office's second door** (card question 4): I said no. Confirm.
5. **The crane:** needs tile art. Skip it for the first pass (option c above)?
6. **Cube sprite:** a stand-in object or a new 2 x 2 sprite?
7. **Canteen:** import Brick Cafe (a tileset import and credit row for one building), or keep it in the house style?
8. **Weather:** `WEATHER_SHADE` or falling ash?
9. **R5 gap and the R6 lane** are cut by the author through the render's cliffs; confirm the positions when tracing.
