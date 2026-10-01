# GLOOMSBY: detailed design (town, place 5, gym 3 Ghost)

Status: **PROPOSED** (written 2026-10-01). Nothing here is built. It adds detail to the card [../towns/gloomsby.md](../towns/gloomsby.md) and does not change its facts (species, levels, trainer lists, items, flags). Choices I had to make are marked **PROPOSED**; places where the card and the render disagree are marked **FIX**. Sources I used: the card, [../interiors/README.md](../interiors/README.md) and [../interiors/catalogue.md](../interiors/catalogue.md) (the rules), the Hollowbrook interiors in [../../interiors.md](../../interiors.md) (house style), the Palladium renders `ecruteakcity1xj.png` (the town) and `Ecruteak City Gym.png` (the gym), vanilla layouts in this tree, and the Team Aqua tilesets named below. Gym: [../../gyms.md](../../gyms.md), leader SANZUFORD ([../../leader-names.md](../../leader-names.md), [../../trainer-roster.md](../../trainer-roster.md)). Scheme 3 and Troglodyte fight 3: [../../troglodyte-arc.md](../../troglodyte-arc.md). Roads: [routes-west-b.md](routes-west-b.md).

**Coordinates.** Every `(x, y)` is a tile, x from the left and y from the top, 0-based. Outdoor positions are read by eye from the render (tile = `px / 17`, the image is 749 x 817 px with a 1 px grid, so **44 x 48** tiles) and **can be 1 or 2 tiles off**: treat them as 'about here'. Interior coordinates are mine and exact, because the interiors are built fresh in Porymap.

## At a glance

| Item | Value |
|---|---|
| Outdoor map | `Gloomsby`, 44 x 48. Size check (44 + 15) * (48 + 14) = 3,658 of 10,240 |
| Section | new `MAPSEC_GLOOMSBY` (interiors share it). Fly point and heal location: yes |
| Tilesets (outdoors) | primary `gTileset_General`, secondary `gTileset_Lavaridge` (vanilla, as the card says) |
| Weather | `WEATHER_FOG_HORIZONTAL` (header, no engine edit) |
| Music (existing Hoenn track, PROPOSED) | `MUS_MT_PYRE_EXTERIOR` outside, `MUS_MT_PYRE` in the Old Tower, `MUS_GYM` in the gym |
| Map connections | **none.** Both roads arrive through gatehouses (warps), not edges |
| Interiors | Center 1F and 2F, Mart, gym, Playhouse, Old Tower, 5 houses (3 locked), 2 gatehouses = 12 maps (see the table) |
| Objects outdoors | at most 13 at once (limit 15); see NPCs |
| Level at arrival and departure | about 22 and about 26 |

## 1. Description

**First glance, from the west gate (R4).** You step out of a grey gatehouse into a pale, damp, windless afternoon. The fog sits at about knee height and thickens toward the east. In front of you the town is a clearing cut out of a dark pine forest: tiles the colour of oatmeal, houses with long brown wooden roofs, a pond you can only half see. Far to the north-east a tall, narrow wooden tower (the **Long Hall**) rises out of the trees, floor above floor. Nothing moves except a lamp somewhere that flickers.

**First glance, from the east gate (R5).** You come out at the south-east corner. The gym is a long way off to the left, the red roof of the Pokémon Center is close, and the fog clings to the Playhouse and the long houses above it.

**Mood.** Damp, quiet, politely morbid. Everyone talks about the dead as neighbours who happen to be late. It is funny because nobody is frightened.

**Colour.** Oatmeal paths, brown wooden roofs, green-black pines, blue-grey fog, one red roof (the Center) and one blue one (the Mart and Sanzuford's house) as the only bright notes.

**Sound.** The Mt Pyre outdoor theme, very soft; a bell from the Old Tower every so often (a sound effect on an `OnFrame` timer, optional); in the gym a heartbeat-slow track.

**Time of day.** Permanently late afternoon. Use the header weather only; do not use a dark palette.

**The memorable view.** From the Pokémon Center door, looking north-west across the whole town to the Old Tower ruin on its rocky plateau, with fog between the roofs and the Long Hall standing above the trees on the far right.

## 2. Street layout in words (a numbered walk)

Tile positions are the render's (about). North is up. The town is a pale oval of paths inside a forest wall: **no exit is a road**, only gatehouses.

1. **West gate, x 0 to 4, y 30 to 34.** The render shows only the right edge of the building at the map's west side. **PROPOSED:** keep it inside the map: a grey gatehouse 5 wide and 5 tall, door on the south face at **(2, 34)**, arrival tile (2, 35). A tree row and a short fence at (0 to 1, 35) and (2 to 5, 36) frame it. From the arrival tile a pale path runs east.
2. **The south-west block.** East of the gate, along y 33 to 36, **House A (blue roof)** stands at x 5 to 9, y 33 to 35, door (7, 35) (Sanzuford's family). Two signs: (16, 35) 'GLOOMSBY. A QUIET TOWN. PLEASE KEEP IT THAT WAY' (the town sign) and (23, 35) a notice board, 'POOL LEVEL: LOW. GHOST LEVEL: STABLE'. A **second house** stands north of it at x 5 to 9, y 28 to 30 (locked, H1).
3. **The big south-west corner: the gym.** At x 4 to 10, y 38 to 42, a large pale building with a gold roof and a double door facing south: **door (7, 42)**, arrival (7, 43). The wide pavement in front, x 2 to 23, y 43 to 45, is where the film crew parks.
4. **South-centre.** **House H4 (locked)** at x 13 to 17, y 40 to 42, door (15, 42). **The Pokémon Center** (red roof) at x 24 to 28, y 39 to 42, **door (26, 42)**, arrival (26, 43). **House C** at x 31 to 35, y 40 to 42, door (33, 42). The **Mart** (blue roof) at x 31 to 34, y 33 to 35, door (33, 35). **House B** at x 24 to 28, y 33 to 35, door (26, 35).
5. **The east gate, x 38 to 43, y 39 to 43.** A grey gatehouse at the bottom-right corner, door on the south face at **(40, 43)**, arrival tile (40, 44). The render's bottom rows are trees; **PROPOSED:** clear a 6-tile path along y 44, x 36 to 41, so the arrival tile joins the pavement.
6. **The middle: houses and a pond.** North of the Center area: **H2 (locked)** at x 13 to 17, y 28 to 30, door (15, 30). A pale lane runs north along x 18 to 23. Two **long houses** side by side at x 13 to 17 and x 18 to 23, y 21 to 24: the left one is **the Mortician's Parlour**, door (15, 24); the right one is **the Production Office**, door (21, 24).
7. **The pond.** A small pond at x 24 to 29, y 25 to 29 (an L: x 24 to 29, y 25 to 27 and x 26 to 29, y 28 to 29), three **boulder-rocks** (tile rocks) at (24, 23), (26, 23), (28, 23) above it and one at (31, 28). The old man stands by it.
8. **The Playhouse.** North of the long houses, in a clearing x 17 to 23, y 12 to 20: the pale-brown theatre at **x 18 to 22, y 12 to 15, door (20, 15)**, arrival (20, 16). A narrow trail (x 17 to 23, y 16 to 20) joins it to the lane. REVIVE hidden on its west side at (17, 14).
9. **The Old Tower plateau (north-west).** A rocky plateau at x 2 to 11, y 11 to 13 behind a dark hall at x 4 to 8, y 13 to 16 with its door on the south face at **(6, 17)**, arrival (6, 18). Rock boulders at (0, 12), (0, 14), (2, 17), (0, 19) and (10, 19); a pair of small gravestones at (12, 12) and (13, 12); a white fence at (2 to 5, 20).
10. **The graveyard.** The pale clearing south of the tower, x 2 to 9, y 18 to 23, with eight gravestones (see Palette and tile notes for how to draw them): (3, 19), (5, 19), (7, 19), (9, 19), (3, 21), (5, 21), (7, 21), (9, 21). A one-way **ledge** along y 24, x 5 to 11 (the render's brown ledge), hops down to the town path.
11. **The Long Hall.** At the north-east, x 38 to 42, y 0 to 17: a very tall wooden tower, like a stack of eight floors. **Door at (39, 17)**, arrival (39, 18); a sign at (38, 18): `CLOSED. PLEASE STOP KNOCKING`. No warp, no interior. (Card: a prop.)
12. **The forest.** Pines fill y 0 to 10 across the whole top and every edge. The render has a **gap at the bottom** (x 18 to 21, y 46 to 47): close it with trees, the town has no south exit.

Water: one pond. Ledges: one (item 10). Trees: the whole frame, 3 deep.

## 3. Every building

Map names are PROPOSED (group `gMapGroup_IndoorVeldris`, section `MAPSEC_GLOOMSBY`). Heights are rows. **Kit** means the Hollowbrook furniture vocabulary (copy blocks from the built maps in Porymap): `Hollowbrook_NeighboursHouse` (11 x 8): kitchen block at x 0 to 3, y 1 to 2, window pair at x 5 to 6, y 0 to 1, bookshelf at x 7 to 8, y 1 to 2, TV-and-flower-table with cushions at x 5 to 8, y 4 to 6, plant column at x 10, y 4 to 6, exit mat at (2, 7). `Hollowbrook_PlayersHouse_2F` (13 x 8): bed x 1 to 2, y 1 to 3; PC desk x 4 to 5, y 1 to 3; TV stand x 9 to 10, y 1 to 3; a 3 x 3 rug at x 5 to 7, y 4 to 6; plants at (0, 5 to 6) and (12, 5 to 6).

| Building | Map | Layout and tileset | Size | Palladium image | Notes |
|---|---|---|---|---|---|
| Pokémon Center 1F, 2F | `Gloomsby_PokemonCenter_1F`, `_2F` | **vanilla** `LAYOUT_POKEMON_CENTER_1F`, `_2F` (nurse and counters stay) | 14 x 9, 14 x 10 | `newcenter.png` as reference only | shared layout (Add New Map with Layout) |
| Mart | `Gloomsby_Mart` | **vanilla** `LAYOUT_MART` | 11 x 8 | none | shared |
| Gym | `Gloomsby_Gym` | custom: `gTileset_Building` + `gTileset_DewfordGym` (see the gym) | 15 x 23 | `Ecruteak City Gym.png` | the render's pit and statues, my puzzle |
| Playhouse | `Gloomsby_Playhouse` | Gen 4 Interior (house style) | 13 x 10 | `Elm's House.png` for the proportions; `Trainer School.png` for the rows of seats | stage and seats |
| Old Tower | `Gloomsby_OldTower_1F` | custom: Team Aqua **Legend of Zelda House Secondary** (stone and timber), fallback Gen 4 | 11 x 10 | none | one room, no dungeon |
| House A (blue roof) | `Gloomsby_HouseA` | Gen 4 Interior | 11 x 8 | `Elm's House.png` | Sanzuford's family |
| House B | `Gloomsby_HouseB` | Gen 4 Interior | 11 x 8 | `Elm's House.png` | the story collector, trade |
| House C | `Gloomsby_HouseC` | Gen 4 Interior | 11 x 8 | `Elm's House.png` | the couple |
| Mortician's Parlour (optional, cut first) | `Gloomsby_Parlour` | Gen 4 Interior | 11 x 8 | none | Sanzuford's employer |
| Production Office | `Gloomsby_ProductionOffice` | Gen 4 Interior | 13 x 8 | `President's Office Tiled.PNG` for the desk idea | Scheme 3's crew HQ; empties after |
| West Gate | `Gloomsby_WestGate` | vanilla gate layout, see below | 15 x 6 | none | pass-through, shared with R4 |
| East Gate | `Gloomsby_EastGate` | the same layout | 15 x 6 | none | pass-through, shared with R5 |
| H1, H2, H4 | none | locked houses: painted, no warp | | | a sign beside each door |

**Locked houses.** The render has nine houses; the card needs three. Paint H1 (7, 30), H2 (15, 30) and H4 (15, 42) as ordinary houses with **no warp event** on their doors, and put a `bg_event` sign beside each: H1 `SHUTTERS DOWN. DO NOT KNOCK`, H2 `THE RESIDENTS ARE RESTING`, H4 `OUT. BACK AT DUSK. IT IS ALWAYS DUSK`. If the author prefers fewer buildings, delete them and plant pines.

### 3.1 `Gloomsby_PokemonCenter_1F` and `_2F` (vanilla)

Vanilla `LAYOUT_POKEMON_CENTER_1F` (14 x 9): nurse at (7, 2) facing down (the **first object**, so the heal respawn works), door pair (6, 8) and (7, 8), stairs warp (1, 6). 2F is 14 x 10: attendants at (1, 2), (2, 2), (6, 2), (10, 2). **Never move the nurse or the counters** (rule 2). NPCs: the vanilla 1F gentleman at (4, 4) becomes the **mourner** ('everyone here is perfectly alive. It is the visitors who worry me'), the boy at (10, 6) a **visitor** who reports a rich boy (optional Troglodyte sighting), the girl at (3, 7) is vanilla's. Warps: (6, 8) and (7, 8) to `Gloomsby` warp 0, (1, 6) to 2F.

### 3.2 `Gloomsby_Mart` (vanilla)

`LAYOUT_MART` (11 x 8): clerk at (1, 3) facing right, door pair (3, 7) and (4, 7). Stock (card): POKÉ BALL, GREAT BALL, POTION, SUPER POTION, ANTIDOTE, AWAKENING, PARALYZE HEAL, ICE HEAL, REPEL, ESCAPE ROPE. No REVIVE yet. Vanilla woman at (5, 5): the crew's runner buying snacks; the boy at (9, 4) wanders up and down. Warps: (3, 7) and (4, 7) to `Gloomsby` warp 1.

### 3.3 `Gloomsby_Gym`: see section 5

### 3.4 `Gloomsby_Playhouse` (13 x 10, Gen 4 Interior)

A small theatre where a play about someone who left is being rehearsed.

- **Floor:** wood, x 0 to 12, y 3 to 8; walls on y 0 to 2.
- **Back wall:** two window pairs at x 3 to 4 and x 8 to 9 (y 0 to 1), a bookshelf at x 1 to 2 and x 10 to 11 (y 1 to 2) as 'wings'.
- **Stage:** the 3 x 3 rug block from `Hollowbrook_PlayersHouse_2F`, repeated twice side by side at **x 3 to 8, y 2 to 4** (the stage is 6 wide, 3 deep). Plants at (1, 4) and (11, 4).
- **Seats:** two rows of stools (cushions): y 6 and y 8, at x 3, 5, 7, 9 (8 stools). Aisles at x 1 to 2 and x 10 to 12.
- **Props:** a small flower table at (11, 3).
- **Exit mat:** **(6, 9)** on the bottom row. Warps: one, (6, 9) to `Gloomsby` warp 3, landing (20, 16).
- **NPCs (3 live objects):** the **lead actor** at (4, 3) facing east, rehearsing one line over and over. **PROPOSED line seed:** 'Go on. Lose politely.' with the wrong stress each time (this is the line Troglodyte will use at the gym door in fight 3). The **second actor** at (6, 3) facing south, the **director** at (6, 5) facing north. An **audience member** at (9, 7) facing north who says the play is about 'someone who left, and why the ghost is not cross about it'. 4 objects.
- **What the player does:** talks to the cast; one actor mentions a rich boy asking whether the seats were reserved.

### 3.4b `Gloomsby_OldTower_1F` (11 x 10, Zelda House Secondary)

A cold stone-and-timber room: the ground floor of the ruined tower. No dungeon: a keeper, a lore NPC, a tablet.

- **Tileset: Team Aqua Legend of Zelda House Secondary** (`Tilesets/The Great Tileset Exchange/Full Tilesets/Legend of Zelda House Secondary/`). What it adds: timber-and-stone walls, a hearth, pot rows, plank tables, beds and a rug in a dim brown-pink palette (see its `example.png`), which is exactly 'old tower'. Cost: a triple-layer tileset, so a Porytiles bake exactly like Gen 4 Interior ([../../interiors.md](../../interiors.md)), and a `CREDITS.md` row: **Buildings: Hek-el-grande; assembler: Yumekua; main creators: Ekat99, Heartlessdragoon, Vurtax; plus Rahtak for the insertable reformat** (read the folder's `credits.md` and copy it). If the author declines: use Gen 4 Interior with the bookshelf and plant kit; it still reads as a room, just less ancient.
- **Layout:** top wall y 0 to 2; **altar shelf** at x 4 to 6, y 1 to 2 with candles (use the shelf block); a row of **pots** down the left wall at (1, 4) to (1, 7) (four); **a hearth** at x 8 to 9, y 1 to 2; a **bricked-up stairway** in the top right corner at (8 to 9, 3) (the stairs up are closed: `bg_event` sign at (8, 3): `THE UPPER FLOORS ARE CLOSED. THEY HAVE RESIDENTS`); a **tablet** (`bg_event`) at (2, 2): `THE NAMES OF THE LATE. 108 OF THEM. THE LAST ONE IS BLANK. PLEASE DO NOT FILL IT IN`; a **plank table** at (5, 5) to (6, 6); exit mat **(5, 9)**.
- **NPCs:** the **graveyard keeper** at (5, 4) facing south: respectful of 'new residents', and after Scheme 3 laughs about the HAUNTER and the sheets. A **lore NPC** at (8, 6) facing west who tells the Spiritomb story (a spirit bound to a keystone; 'the tower was built to keep a hundred and eight friends company').
- **Warps:** (5, 9) to `Gloomsby` warp 4, landing (6, 18).

### 3.5 `Gloomsby_HouseA` (11 x 8, Gen 4): SANZUFORD's family

- **Kit:** kitchen block x 0 to 3, y 1 to 2; window pair x 5 to 6; bookshelf x 7 to 8, y 1 to 2; a **long table with four stools** instead of the TV: table at x 5 to 6, y 4 to 5, stools at (4, 4), (7, 4), (4, 5), (7, 5); plant column x 10, y 4 to 6; exit mat (2, 7).
- **Portrait:** a `bg_event` on the wall at (4, 1): `A YOUNG WOMAN IN A BLACK GRADUATION HAT. VERY SERIOUS. VERY PLEASED`.
- **NPC (1):** **SANZUFORD's mother** at (6, 3) facing south, wandering. Jokes about her daughter's job. After badge 3: 'she will finally tidy her room'.
- **Warps:** (2, 7) to `Gloomsby` warp 5, landing (7, 36).

### 3.6 `Gloomsby_HouseB` (11 x 8, Gen 4): the ghost-story collector

- **Kit:** no kitchen. Three bookshelf blocks along the top wall at x 0 to 1, x 3 to 4, x 7 to 8 (y 1 to 2), a window pair at x 5 to 6. A low table with two cushions at x 4 to 5, y 4 to 5 and a **reading chair** (one cushion) at (7, 5). Plant at (10, 4). Exit mat (2, 7).
- **NPC (1):** the **collector** at (6, 4) facing west. Story swap: **in-game trade** (card): DUSKULL for the player's ZUBAT (flavour, no importance). He tells stories about the Long Hall.
- **Warps:** (2, 7) to `Gloomsby` warp 6, landing (26, 36).

### 3.7 `Gloomsby_HouseC` (11 x 8, Gen 4): the couple

Exactly the Hollowbrook neighbour's house kit: kitchen top-left, window, bookshelf, TV with flower table and cushions at x 5 to 8, y 4 to 6, plant column at x 10, mat (2, 7). NPCs: **wife** at (5, 6) facing north; **husband** at (8, 3) facing south. Both complain about the film crew's noise and the van that blocked the lane. After Scheme 3: the husband misses the noise. Warps: (2, 7) to `Gloomsby` warp 7, landing (33, 43).

### 3.8 `Gloomsby_Parlour` (11 x 8, Gen 4): Sanzuford's employer (optional, cut first)

A quiet front office. **Counter:** reuse the kitchen counter blocks as a reception desk at x 3 to 6, y 2 to 3. Two plants at (1, 3) and (9, 3). A **bench** of two cushions at (8, 5) and (9, 5). Exit mat (2, 7). NPC: the **mortician** (PROPOSED name Mr Wickham) at (4, 4) facing south: 'She is very good. She will never tell you.' (about Sanzuford); he can sell nothing. Warps: (2, 7) to `Gloomsby` warp 8, landing (15, 25).

### 3.9 `Gloomsby_ProductionOffice` (13 x 8, Gen 4): the film crew's office

Before Scheme 3 it is full of cables and boxes; after, it is empty with a note. **Layout:** two PC-desk kits (copy the 2F desk) at x 1 to 2 and x 10 to 11, y 1 to 3; a long folding table at x 5 to 7, y 3 to 4; five cardboard boxes (the plant block or the shelf-bottom block) at (1, 5), (2, 5), (11, 5), (11, 6), (12, 5); a **script board** (`bg_event`) at (6, 1): `SCENE 14: SHEETED GUESTS ENTER. SPOOKY.` Exit mat (6, 7). NPCs: the **producer** at (4, 5) on the phone ('they said it would be easier'), a **runner** at (9, 4). Both vanish after `FLAG_GLOOMSBY_SCHEME_DONE`; the board then reads `GONE OUT FOR LUNCH` (a second `bg_event` swapped by flag). Warps: (6, 7) to `Gloomsby` warp 9, landing (21, 25).

### 3.10 `Gloomsby_WestGate` and `Gloomsby_EastGate` (15 x 6, shared with the roads)

**Default (vanilla, no import):** duplicate `Route110_SeasideCyclingRoadEntrance_Layout` (15 x 6, secondary `gTileset_Shop`; it already has two door pairs on the bottom row). Remove the bike-shop bits, keep the counter. A guard stands at (7, 2) facing south behind the counter. The **left pair (1, 5) and (2, 5)** are warps ids 0 and 1, the **right pair (12, 5) and (13, 5)** are ids 2 and 3.

- **West gate:** left pair to `Gloomsby` warp 10 (the town's west door), right pair to `Route4` warp 0. The guard: 'Fog ahead? Behind. You are walking out of it.' (when you walk to the road); 'Welcome. Please do not wake anyone.' (to the town).
- **East gate:** left pair to `Gloomsby` warp 11, right pair to `Route5` warp 0. The guard: 'Smeltham next. Mind the cranes.'

**Optional upgrade: Team Aqua `Gatehouse Secondary` (or `Gatehouse Secondary Alt`).** What it adds: the Johto-style gatehouse: a green-and-brick room with a peach U-shaped counter, a clock, a window, a clean tile floor and a vending machine, which looks like the picture in `example.png` (it is the same room as the Hoenn cycling-road entrance, redrawn). It needs a Porytiles bake and a `CREDITS.md` row: **Ekat, Vurtax (FRLG rips), Heartlessdragoon (RSE rips), and Rahtak for the insertable reformat**; the Alt version credits 'princess-phoenix' (read both `credits.md` files). One import covers every gatehouse on the west chain (R5's toll gate, Mothwood's gate). I recommend the vanilla default first.

## 4. Door and warp table

Outdoor `Gloomsby` warps (id: tile, destination). Exit warps on the interiors land on the arrival tile (the tile in front of the door).

| id | Tile (outdoor) | Destination | Arrival after exiting |
|---|---|---|---|
| 0 | (26, 42), Center | `Gloomsby_PokemonCenter_1F` (6 and 7, 8) | (26, 43) = **the heal location tile** |
| 1 | (33, 35), Mart | `Gloomsby_Mart` (3 and 4, 7) | (33, 36) |
| 2 | (7, 42), gym | `Gloomsby_Gym` (7, 22) | (7, 43) |
| 3 | (20, 15), Playhouse | `Gloomsby_Playhouse` (6, 9) | (20, 16) |
| 4 | (6, 17), Old Tower | `Gloomsby_OldTower_1F` (5, 9) | (6, 18) |
| 5 | (7, 35), House A | `Gloomsby_HouseA` (2, 7) | (7, 36) |
| 6 | (26, 35), House B | `Gloomsby_HouseB` (2, 7) | (26, 36) |
| 7 | (33, 42), House C | `Gloomsby_HouseC` (2, 7) | (33, 43) |
| 8 | (15, 24), Parlour | `Gloomsby_Parlour` (2, 7) | (15, 25) |
| 9 | (21, 24), Production Office | `Gloomsby_ProductionOffice` (6, 7) | (21, 25) |
| 10 | (2, 34), west gate | `Gloomsby_WestGate` (1 and 2, 5) | (2, 35) |
| 11 | (40, 43), east gate | `Gloomsby_EastGate` (1 and 2, 5) | (40, 44) |

Interior-side warps are given in each building above. The Center's 1F-to-2F pair is vanilla's. R4's gate is `Route4` (3, 10) to `Gloomsby_WestGate` warp 2 (the right pair); R5's is `Route5` (14, 53) to `Gloomsby_EastGate` warp 2.

## 5. The gym (GHOST, SANZUFORD, WISP BADGE)

**`Gloomsby_Gym`, 15 x 23.** Built from the render `Ecruteak City Gym.png` (240 x 368 px with no grid, so 15 x 23 at 16 px per tile). The render: a wood hall with a tall black pit in the middle (x 5 to 9, y 7 to 16), a row of low rails (posts) down both sides of the pit, two statues at the top, a leader's platform at the top centre, two Poké Ball statues and a door mat at the bottom. I keep every one of those shapes and add a puzzle.

**Tilesets: primary `gTileset_Building`, secondary `gTileset_DewfordGym`** (vanilla: the Dewford gym is the one vanilla gym built to be dark; open `DewfordTown_Gym` in Porymap and copy its floor, wall and statue blocks, and see how its dark look works). Plain, no import, no credit row beyond Palladium.

**Darkness (a correction to the card).** The card says to set `requires_flash`. Vanilla Dewford does **not** use that header flag (`requires_flash` is false); its `OnTransition` script calls `setflashlevel` and gets brighter with every trainer beaten (`data/maps/DewfordTown_Gym/scripts.inc`). Copy that script: level 6 at the start, 4 after the first trainer, 2 after the second, 0 (lights on) after SANZUFORD. That makes the dark gym a script, not a header, and it does not need Flash. The leader still gives HM Flash as the badge gift.

### The floor, tile by tile

Legend (x 0 to 14 across, y 0 to 22 down): `#` wall or rail (impassable), `.` floor, `~` black void (impassable), `o` a **stepping stone** (floor on the void), `D` a doorway in the wall row, `L` SANZUFORD, `T` a trainer, `S` a guide statue (a `bg_event`, impassable), `m` the exit mat.

```
x     0         1
      012345678901234
y  0  ###############
y  1  ###############   (an orb emblem on the wall at (7, 1))
y  2  ###############
y  3  ##...S.L.S...##   L at (7, 3), statues at (5, 3) and (9, 3)
y  4  ##...........##
y  5  ##...........##
y  6  #####D#D#D#####   doorways at x 5, 7 and 9; the real one is x 9
y  7  #####.....#####   the landing, x 5 to 9
y  8  ##..#o~~~~#..##
y  9  ##..#o~~~~#..##
y 10  ##..#ooToo#..##   the Psychic stands on the stone at (7, 10)
y 11  ##..#~~~~o...##   a gap in the right rail at (10, 11)
y 12  ##...oo~oo#..##   a gap in the left rail at (4, 12)
y 13  ##..#~o~o~#..##
y 14  ##..#~ooo~#..##
y 15  ##..#~~o~~#..##
y 16  ##..#~~o~~#..##
y 17  ##...........##
y 18  ##.T.........##   T at (3, 18)
y 19  ##...........##
y 20  ##...S...S...##   statues at (5, 20) and (9, 20)
y 21  ##...........##
y 22  #######m#######   the exit mat at (7, 22)
```

(The pockets x 2 to 3 and x 11 to 12, y 8 to 15, are plain floor, reached only through the two rail gaps.)

**The puzzle (two parts).**

1. **The stepping stones.** The Gap is x 5 to 9, y 8 to 16: **void** (collision 1, drawn as a black metatile: a pure black block, tile 0 of the primary or the border colour; paint it and set the collision in Porymap). The `o` cells are the only walkable tiles in it, painted as the ordinary floor. They form a zig-zag: from the south hall at **(7, 17)** go north **(7, 16), (7, 15), (7, 14)**; the path forks at (7, 14): **west** fork (6, 14), (6, 13), (6, 12), (5, 12) ends at a gap in the left rail at **(4, 12)** which opens to the left pocket (floor x 2 to 3, y 8 to 15); **east** route (8, 14), (8, 13), (8, 12), (9, 12), (9, 11), (9, 10), then west along y 10 through **(8, 10), (7, 10), (6, 10), (5, 10)** and north **(5, 9), (5, 8), (5, 7)** to the landing. From (9, 11) a gap in the right rail at **(10, 11)** opens to the right pocket (floor x 11 to 12, y 8 to 15). Both pockets are harmless dead ends with a gravestone sign each: left `A WRONG TURN IS STILL A TURN`, right `KEEP LEFT. OR RIGHT. WE ARE NOT SURE`. With the map dark, the player sees only a few tiles around them at a time, which is what makes the zig-zag a puzzle.
2. **The three doors.** On the landing (x 5 to 9, y 7) the wall above has **three doorways**: (5, 6), (7, 6) and (9, 6). Only **(9, 6)** is real: it is a plain walkable doorway into the leader's hall. The other two are **fake**: a `coord_event` trigger on each doorway tile plays `The door opens onto the entrance. Somehow.` and runs `warpteleport MAP_GLOOMSBY_GYM, 7, 21` (the player lands at the start of the south hall). The real door has a lit **pool of light** in front of it: an object `OBJ_EVENT_GFX_LIGHT_SPRITE` (a 32 x 32 glow sprite, check how it looks) at **(10, 5)** just inside, which shines through the doorway; no tile art is needed. The hex maniac's dialogue gives the hint: 'The doors on the left lie. The one with a light is honest. Dead people usually are.'

Dead ends cost nothing: the penalty for a wrong door is the walk back, about 14 steps.

**Hall of the leader.** SANZUFORD at **(7, 3)** facing south, between two ghost statues. Walk in through the real door to (9, 5), cross to (7, 4) and talk.

### Gym trainers (2, from the card, positions PROPOSED)

| Class | Team | Stands at | Faces | Sight |
|---|---|---|---|---|
| Hex Maniac | SHUPPET 19, GASTLY 20 | (3, 18) in the south hall | east | 5 |
| Psychic | DROWZEE 20, DUSKULL 21 | (7, 10) on the stone at the zig-zag's corner | east | 3 |

The Hex Maniac sees the player walk in along y 18 and fights first. The Psychic stands on the path where the east route turns west, so the player cannot go round him: he must be beaten (levels 19 to 21, three to four below the leader's lowest 23, per the rule).

**Gym guide statue.** `bg_event` statues at (5, 20) and (9, 20): the joke about not whistling at the dead.

**Objects:** SANZUFORD, Hex Maniac, Psychic, the light sprite = 4. Limit 15: fine.

### Scripts and flags for the gym

- `OnTransition`: the `setflashlevel` ladder above, using `goto_if_defeated TRAINER_SANZUFORD` first (all lights on).
- Fake doors: two `coord_event` triggers with no var (they always fire).
- SANZUFORD: `trainerbattle` the leader pattern copied from `data/maps/RustboroCity_Gym/scripts.inc`; reward badge 3, HM Flash, TM Shadow Ball; `FLAG_BADGE03_GET`, `FLAG_RECEIVED_HM_FLASH` reused.

## 6. Scheme 3 and Troglodyte fight 3 (outdoor staging)

All positions are on `Gloomsby` and PROPOSED. The scene uses a **`coord_event` trigger** (CLAUDE.md: not `MAP_SCRIPT_ON_TRANSITION`) on the three tiles **(6, 43), (7, 43), (8, 43)** in front of the gym door, with a state var (name PROPOSED: `VAR_GLOOMSBY_STATE`, not claimed: 0 before, 1 after the Haunter, 2 after the fight). The trigger tiles must be walkable and at elevation 3.

**Before the scene (objects present while the state is 0):**

- The **film van**: a truck sprite (`OBJ_EVENT_GFX_TRUCK`, 3 x 3) at x 2 to 4, y 43 to 45, marked `SPECTRAL PICTURES LTD` (the same van seen on R4).
- The **director** (PROPOSED name Cormac Vane) at (9, 44) facing west: 'One more take. I need real atmosphere.'
- The **assistant** at (10, 45) facing north, a bedsheet with eyes cut in it over one arm.
- Two **sheeted guests** (frat guys; an ordinary male NPC sprite each, 'in sheets' is dialogue) at (12, 43) and (13, 44).
- The **mourner** at (14, 44) (square): 'The gym went dark for filming and nobody told me.'

**The beat (4 steps):**

1. *Setup.* The player steps on a trigger tile. The director shouts 'Cameras!'. The sheeted guests walk to (7, 41) and (8, 41) (in front of the gym door) and raise their arms.
2. *Reveal.* One sheet slips; it is a frat guy. A short exchange.
3. *Collapse.* **A real HAUNTER** (a temporary object, `OBJ_EVENT_GFX_SPECIES(HAUNTER)`: `graphics/pokemon/haunter/overworld.png` exists in this tree) floats in from the Old Tower side: it appears at (3, 18) and `applymovement` takes it south along x 3 to (4, 41), then east to (7, 41). It plays its cry once (`playmoncry`, no battle). The guests run (off to the east), leaving their sheets; the HAUNTER takes the sheets, wears two of them and drifts off. The crew leaves with the van: set `FLAG_GLOOMSBY_SCHEME_DONE`, hide the crew and the van, and the HAUNTER becomes a permanent resident NPC at (6, 21) in the graveyard (the keeper's friend).
4. *Troglodyte fight 3.* He arrives from the west gate along y 43: he starts at (3, 43) (spawn him off the trigger tiles, appear by script), walks to (6, 43), faces east. 'Go on. Lose politely.' Battle (party of 3, levels 20 to 22: starter at stage 2, Sir Biscuit as HERDIER, EEVEE; reuse a vanilla trainer id; no IVs, `IVs: 0` lines). Loss line: 'Nobody at home will believe this.' He leaves west. Then SANZUFORD opens the door (a script walks her to the door tile and talks).

Order: the scene starts the first time the player steps in front of the gym after arriving; you cannot enter the gym before it ends (the door is script-locked while the state is 0 or 1).

## 7. NPCs outdoors (13 at most at once)

| # | NPC | Position | Moves | Topic |
|---|---|---|---|---|
| 1 | Sign: town | (16, 35) | | 'GLOOMSBY. A QUIET TOWN. PLEASE KEEP IT THAT WAY' |
| 2 | Sign: gym | (11, 42), beside the door | | 'GLOOMSBY GHOST GYM. LEADER: SANZUFORD. WE DO THE DEAD RIGHT' |
| 3 | Film director (Cormac Vane) | (9, 44) | still | one more take (before Scheme 3 only) |
| 4 | Film assistant | (10, 45) | still | the bedsheet (before only) |
| 5 | Sheeted guest x2 | (12, 43), (13, 44) | still | 'we are the haunting' (before only) |
| 6 | Mourner | (14, 44) | still | the gym went dark |
| 7 | Graveyard keeper | (5, 22), in the graveyard | wander x 2 to 9, y 21 to 23 | respectful; after the scheme laughs |
| 8 | Old man by the pond | (27, 24) | still, face south | tells you to leave the rocks alone, hints Strength |
| 9 | Kid with a lamp | (10, 33) | wander x 8 to 12, y 32 to 36 | hunts GASTLY in the fog, shows the Dusk Stone spot |
| 10 | Troglodyte | spawned for the scene | | fight 3 |
| 11 | HAUNTER | spawned, then permanent (6, 21) | float | |
| 12 | Item ball: SPELL TAG | (6, 18), the tower steps | | visible |
| 13 | Item ball: POTION | (30, 26), behind the pond | | visible |

NPCs inside (no cost outdoors): nurse, clerk, mother, collector, couple, actors, director, keeper, lore NPC, producer, runner, mortician, gate guards. Total outdoors with the scene running: director, assistant, 2 guests, mourner, keeper, old man, kid, Troglodyte, HAUNTER, 2 item balls, 1 Strength boulder = 13. After the scheme the four crew objects vanish, so the town idles at 9.

## 8. Items and secrets (card, with positions)

| Item | Where | Gate |
|---|---|---|
| SPELL TAG | (6, 18), on the Old Tower steps | visible, none |
| POTION | (30, 26), behind the pond | visible, none |
| ESCAPE ROPE | (1, 36), by the west gate fence | hidden, none |
| TM Torment | (7, 19), behind a gravestone | hidden, none |
| DUSK STONE | (10, 16) in the tower nook, a Strength boulder at (10, 19) is pushed north to (10, 18) first | Strength (badge 4), return visit |
| REVIVE | (17, 14), the Playhouse's west side | hidden, none |
| HM Flash | SANZUFORD | badge 3 |
| TM Shadow Ball | gym reward | badge 3 |
| Trade: DUSKULL for ZUBAT | House B | none |

## 9. Palette and tile notes

- **Exterior:** General + Lavaridge. The render's brown wooden roofs are Lavaridge's. The pale ground is the Lavaridge path tile; the fog does the rest. A ghost-grey tint on the roofs is not needed.
- **Pines:** the General tree set, 3 deep all round (the render's forest wall). Trace it as a border.
- **The Long Hall:** the render's eight stacked floors. No vanilla tower exists in General or Lavaridge; build it from stacked wall-and-window blocks of the biggest wooden building you find in Lavaridge or Fortree (check `FortreeCity` for the tall wooden Fortree houses). A plain shuttered door block is enough. **Needs a bit of tile combining; no new art.**
- **Gravestones.** General and Lavaridge have none. Vanilla has gravestones in `gTileset_Facility` (Mt Pyre) and in the FRLG Lavender tilesets, but a map takes one secondary. Options, cheapest first: (a) use the **small rocks** (the General set's small boulder tile) as graves and give each a `bg_event` epitaph, as the render does with its posts; (b) paint a **gravestone metatile** into a copy of the Lavaridge secondary in Porymap's tileset editor (the author's call: Claude does not edit tilesets, CLAUDE.md rule 2); (c) use the Team Aqua Shady Forest set below, which has stumps and bare trees but **no graves**. Recommendation: (a) now, (b) later.
- **Mood upgrade (optional): Team Aqua `Shady Forest Secondary`** (`.../Full Tilesets/Shady Forest Secondary/`). What it adds over Lavaridge: dark teal pines, **bare dead trees, stumps, cobbled paths, iron street lamps, barrels and purple-roofed cottages**: the damp spooky village look. It would replace Lavaridge as the town's secondary (and then the roofs change from brown to purple-brown). Cost: triple-layer, so a Porytiles bake like Gen 4 Interior; a `CREDITS.md` row (assembler Yumekua; creators Ekat99, Heartlessdragoon, Vurtax and more; Rahtak for the reformat; copy the names from the folder's `credits.md`). I recommend this for a second pass: it matches R4's lamp-lighter and the fog.
- **Interiors:** Gen 4 Interior for houses, Playhouse and the office; Zelda House for the Old Tower; vanilla layouts for Center and Mart.

## 10. Flags (not claimed)

| Name | Meaning |
|---|---|
| `FLAG_VISITED_GLOOMSBY` | fly point, set in the town's `OnTransition` |
| `FLAG_GLOOMSBY_SCHEME_DONE` | Scheme 3 resolved: crew and van gone, HAUNTER stays, after-lines |
| `VAR_GLOOMSBY_STATE` | 0 before the scene, 1 after the HAUNTER, 2 after fight 3 |
| the reused trainer flag of the vanilla id Troglodyte fight 3 uses | fight 3 done |
| `FLAG_GLOOMSBY_ITEM_*` | one per item |
| `FLAG_GLOOMSBY_TRADE_DONE` | the DUSKULL trade |
| `FLAG_BADGE03_GET`, `FLAG_RECEIVED_HM_FLASH` | reused, not new |

Nothing is claimed in `design/flags.md`: that happens when each is built.

## 11. Build checklist (in order)

1. Add `Gloomsby` (44 x 48), tilesets General + Lavaridge, music, fog weather, `MAPSEC_GLOOMSBY` (a new section: section ids are scarce, [../../engine-limits.md](../../engine-limits.md) limit 3). 2. Trace the render's pine frame, paths and houses; close the bottom gap. 3. Place the two gate buildings and paint the pond, graves and ledge. 4. Add the Pokémon Center 1F and 2F and the Mart (shared vanilla layouts). 5. Add `Gloomsby_Gym` from the grid above, with the Dewford-style flash script. 6. Add the five houses and the gates. 7. Add the Playhouse and the Old Tower. 8. Add the Parlour and the Production Office last (both optional). 9. Warps in the order of the table. 10. Heal location and fly row: follow the checklist in [../../region-map.md](../../region-map.md) (write `respawn_map` before `respawn_npc` in `heal_locations.json`, and give both; the nurse is the Center's first object). 11. After pulling a duplicated map, grep `src/data/heal_locations.json` for duplicate ids (CLAUDE.md). 12. Credits: Project Palladium (render), Zelda House (Old Tower), plus Gatehouse and Shady Forest rows if those are imported, in the same commit as each import. 13. Close or reload Porymap before Claude edits event lists. 14. `make -j4` and `python3 design/tools/dialogue_check.py` on any text.

## 12. Build effort

**Medium** (the card agrees). The exterior is easy (trees, paths, nine houses). The gym is the real work: the stepping-stone void and three doors are one black block, one collision setting and two scripts. Hard parts afterwards: the Scheme 3 cutscene (a temporary HAUNTER and a van) and the fight.

## 13. Open questions

1. **Gates and edges.** Both roads arrive by gate (warps); the town has no edge connection. The card said 'west gatehouse for R4 and east for R5' and I followed it, but **I moved the Gloomsby ends of both roads to the render's own gatehouse** (see [routes-west-b.md](routes-west-b.md)): R4's Gloomsby end is its **west** end and R5's is its **south** end. Confirm.
2. **The Long Hall:** a prop only (my choice, the card's), or a small interior with a quest?
3. **Gym darkness:** `setflashlevel` brightening with each trainer (Dewford's way), or the header's `requires_flash` as the card says? I recommend the script.
4. **Graves:** small rocks with epitaphs (no new art), or a gravestone metatile drawn in the tileset editor?
5. **Three locked houses:** keep as dressing, or plant trees and drop them?
6. **The Parlour and the Production Office** are optional extras (they were not in the card's building list). Keep or cut?
7. **Shady Forest** upgrade for the whole town and R4, or the vanilla Lavaridge look?
8. **Troglodyte's line** 'Go on. Lose politely.' is seeded in the Playhouse (the lead actor rehearses it). Fun foreshadow, or confusing?
