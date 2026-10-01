# VESPERHAVEN: detailed design (the hidden coast, post-game hub)

Status: **PROPOSED.** Written 2026-10-01 from [../interiors/README.md](../interiors/README.md), [../interiors/catalogue.md](../interiors/catalogue.md), [../README.md](../README.md), [../../interiors.md](../../interiors.md), [../index.md](../index.md), the card [../towns/vesperhaven.md](../towns/vesperhaven.md), [../../postgame.md](../../postgame.md), [../../trainer-roster.md](../../trainer-roster.md) (built teams), [../../dialogue/league.inc](../../dialogue/league.inc) (the drafts for OSSIAN, HYACINTH, DUNMORE, DRAYDEN, Cynthia, Troglodyte), the roads R21 and R27 to R30 ([../routes-south.md](../routes-south.md)), and by looking at the Palladium renders `halloffamegscrevampzr1.png` (160 x 263, about **10 x 16**), `Elm's House.png` (208 x 160, **13 x 10**) and `championlacetq2.png` (240 x 512, about 15 x 32), and the Team Aqua examples named below. Templates **G4-A, G4-B, G4-C** are in [ebbsworth.md](ebbsworth.md) section 6.0. Neighbours: [beaconmouth.md](beaconmouth.md) (MIZZLE's rematch seat), [ebbsworth.md](ebbsworth.md) (R28), [kingsquay.md](kingsquay.md) (the ferry), [landmarks-south-detail.md](landmarks-south-detail.md) (Silverstrand, Echo Hollow, Argent Peak), [routes-south-detail.md](routes-south-detail.md) (R27 to R30).

**New minor names and details introduced in this file are all PROPOSED:** the League service gate, the cutters (card), the Lounge floor names, the Hall attendant, the staff houses' occupants.

Conventions: **(x, y) from the top-left tile (0,0)**; footprints `(x0,y0)-(x1,y1)` inclusive; a 4-wide building's door is the bottom-row tile `(x0+1, y1)`, larger buildings give theirs; mats are two tiles wide; maps stay `layout_version` `emerald`, `REGION_HOENN`, section `MAPSEC_VESPERHAVEN`.

---

## 1. Quick facts

| | |
|---|---|
| Map | `Vesperhaven`, **52 x 44** (`(52+15)*(44+14) = 3886`, limit 10240) |
| Exterior base | Vanilla **`SootopolisCity`** (60 x 60), cut down, with **LeoB ORAS `secondary/sootopolis`** (the repo's `16 - Sootopolis.png` shows it: pale rock terraces, cream houses, blue spire towers, a blue crater lake) |
| Section / fly | `MAPSEC_VESPERHAVEN` (11 characters); fly town after the first arrival (Feather Badge); `HEAL_LOCATION_VESPERHAVEN` on (16,9) outside the Center |
| Music | `MUS_SOOTOPOLIS` (town, houses), `MUS_HALL_OF_FAME_ROOM` (Hall of Past Champions), battle tracks for rematches (`MUS_VS_GYM_LEADER`, `MUS_VS_ELITE_FOUR`, `MUS_VS_CHAMPION`) |
| Weather | `WEATHER_SHADE` (a permanent soft evening, for the name; check it does not make the LeoB colours muddy, else `WEATHER_SUNNY`), `MAP_TYPE_CITY` |
| Gym / scheme | None. A post-game hub: rematches, Cynthia's tea, the Gatsby thread, Troglodyte's cloakroom job |
| Roads | **R21** north (first arrival, a stair), **R27** west (water), **R28** east (water), **R29** south-west (water), **R30** south-east (land stair) |
| Objects | Town map about 8; Lounge floors at most 15 each |
| Build effort | **Hard** (card). Build last of the south group, after The Pinnacle and R21 exist |

---

## 2. Description

**First glance from R21 (the north stair).** The first time, the player comes down a long, steep stone stair cut into a crater wall, with the last of a gold evening light flooding the bowl below. At the bottom: a fountain terrace with a Pokémon Center and a Mart, then a ring of pale paving round a great blue pool, a long stone building facing it (the League's lounge), a little cottage on a ledge with red flowers, and, down in the south, a tiny boathouse. Nothing here is on any signpost. Everyone who lives here has the air of having stepped out for a rest.

**From the sea.** Three narrow channels (west, east, south-west) feed the pool; each has a wooden pontoon with a rope across it until the League is beaten (a coast guard cutter sits in each strait, an NPC boat, 'League business. Come back when you have finished'). After the League the cutters leave.

**Mood, colour, sound, time of day.** Hushed, warm and slightly wistful: the one place in Veldris where everyone, even the Elite Four, is off duty. Palette: pale grey-white rock, cream plaster, blue spires, deep lake blue, red flower beds at the cottage. **Time of day: permanent early evening** (the town is called Vesperhaven). Sound: the calm Sootopolis track, water, a kettle.

**The one memorable view.** The north terrace at (25,10), just below the foot of the stair: the fountain behind you, the whole pool in front of you with its statue of an old Champion on its islet, the Lounge's long windows catching the evening light on the left, and Cynthia's red flowers on the right. Keep the line between (25,10) and the statue at (25,24) clear.

---

## 3. Street layout in words (a numbered walk)

The town is a bowl: a crater rim of cliffs all round (trees and white rock), terraces stepping down to a **ring path** round the pool.

1. **The north stair (x 24-27, y 0-3).** R21 arrives at the north edge. A long stone stair; at its top, a **League service gate** (iron, closed until game clear: see section 10) at y 3, x 24-27.
2. **North terrace (x 12-39, y 2-11).** Fountain at (24,5)-(25,6); **Pokémon Center** (15,5)-(18,8), door (16,8), on the west side; **Mart** (33,5)-(36,8), door (34,8), on the east side. A **Fisher** at (28,9) and a bench at (26,9). Steps down to the ring path at (23,10)-(26,11).
3. **Hall of Past Champions (NW).** (4,4)-(9,9), door (6,9), a small museum building on the west ledge, reached by a path from the terrace along y 10.
4. **The ring path** round the pool (x 13-38, y 12-35, two tiles wide).
5. **The Pool** (water x 15-36, y 14-33), surfable, with a fountain **statue of an old Champion** on a 3 x 3 islet at (24,23)-(26,25). The three channels enter it: **West** (x 0-14, y 28-30), **East** (x 37-51, y 28-30), **South-west** (x 8-11, y 35-43).
6. **The League Lounge** on the west ledge, **(1,16)-(10,23)** (10 x 8), the big door on the **south face, 5 tiles from the left corner: (6,23)**. A path from the door leads south, then east along y 24-25 to the ring.
7. **Cynthia's Cottage** on a ledge to the east, **(42,19)-(46,23)** (5 x 5), door (44,23). The path approaches from the west along y 24 ('door faces west' in the card: Emerald doors are always on the south face, so I read it as the garden path arriving from the west). A garden of red flowers and a bench at (41,21).
8. **Boathouse (south edge).** (22,37)-(25,40), door (23,40), on a spur at the pool's south; a rowing boat (decoration) at (27,41), the **Boatman** at (24,41).
9. **Two staff houses:** **House 1** (42,9)-(45,12), door (43,12) on the north-east ledge; **House 2** (3,36)-(6,39), door (4,39) on the south-west ledge by the strait.
10. **South-east stair (x 44-47, y 36-39)** to R30, with a **service gate** at y 39 (same gate logic).
11. **The three sea gates:** pontoons at the channel ends: west (0,27)-(1,31), east (50,27)-(51,31), south-west (7,42)-(12,43), each with a **cutter** (`SS_TIDAL` ship object) before the League and a **Dockhand** at the west and east pontoons.

---

## 4. Map plan

Sketch, **1 character = 2 x 2 tiles** (26 x 22 characters for 52 x 44 tiles); the footprints above generated it. Legend: `T` crater rim and trees, `.` terraces and paving, `s` north stair, `P` Pokémon Center, `M` Mart, `o` fountain, `h` Hall of Past Champions, `r` steps, `L` League Lounge, `~` water, `i` statue islet, `C` Cynthia's Cottage, `H` House 1, `e` House 2, `B` Boathouse, `z` SE stair, `>` R30 connection, `g` sea-gate pontoons.

```
x:  0    1    2    3    4    5
y0  TTTTTTTTTTTTssTTTTTTTTTTTT
y2  TTTTTT......ss......TTTTTT
y4  TThhhT.PPP..o...MMM.TTTTTT
y6  TThhhT.PPP..o...MMM.TTTTTT
y8  TThhhT.PPP......MMM..HH...
y10 T..........rrr.......HH...
y12 T....................HH...
y14 T......~~~~~~~~~~~~.......
y16 LLLLLL.~~~~~~~~~~~~.......
y18 LLLLLL.~~~~~~~~~~~~..CCC..
y20 LLLLLL.~~~~~~~~~~~~..CCC..
y22 LLLLLL.~~~~~ii~~~~~..CCC..
y24 T......~~~~~ii~~~~~.......
y26 g......~~~~~~~~~~~~......g
y28 g~~~~~~~~~~~~~~~~~~~~~~~~g
y30 g~~~~~~~~~~~~~~~~~~~~~~~~g
y32 T......~~~~~~~~~~~~.......
y34 T...~~....................
y36 Teee~~.....BB...TTTT..zz..
y38 Teee~~.....BB...TTTT..zz..
y40 T...~~.....BB...TTTT..>>..
y42 T..gggg.........TTTT..>>..
```
(Header digits mark every 10 tiles. The sketch is coarse: the pool sits at x 15-36, y 14-33, the channel mouths are the rows marked `g`.)

**Connections:**

| Edge | Neighbour | Offset | Notes |
|---|---|---|---|
| North | `R21` (south end) | 0 | The stair x 24-27, y 0-3; service gate closed until `FLAG_VESPERHAVEN_GATES_OPEN` |
| West | `R27` (east end) | 9 (R27's channel y 19-21 meets y 28-30) | Water x 0, y 28-30, rope and cutter until game clear |
| East | `R28` (west end) | 24 (R28's channel y 4-6 meets y 28-30) | Water x 51, y 28-30, rope and cutter until game clear. Shared pontoon for the Kingsquay ferry arrival (49,29) |
| South (west part) | `R29` (north end) | 4 (R29's top water x 4-7 meets x 8-11) | Water x 8-11 at y 43, cutter until game clear |
| South (east part) | `R30` (north end) | 36 (R30's top x 8-11 meets x 44-47) | Land x 44-47 at y 43 via the stair, gate until game clear. R30 is traced flipped so its cave is at the south end (see routes-south-detail.md) |

---

## 5. Base, tilesets, palette notes

**Exterior.** Duplicate `SootopolisCity` (60 x 60) and **Change Dimensions** to 52 x 44. Vanilla already has: the crater lake and its wall of white rock terraces with cream-and-blue houses on ledges (the vanilla map's houses sit at x 6-12 / 44-54 on stepped ledges), a Pokémon Center on the east (x 41-45, y 27-31), a Mart on the west (x 15-19, y 26-29), the gym on an islet in the lake at (28,28)-(33,33) and a small stairway at the top. Use: the lake (reshape to 22 x 20), the stepped ledges, the Center and Mart blocks (move them to the terrace), the blue-spire tower as decoration, the islet (becomes the **statue islet**, repaint the gym block as a plinth with a statue), the stairway at the top (becomes the north stair). Delete the vanilla cave entrance and Mystery Events House warps and the Sootopolis legends scripts (duplicates carry events, delete or rewrite them; and delete the duplicated heal locations before saving).

**Tilesets (recommended):**

| Where | Primary | Secondary | Source and credit |
|---|---|---|---|
| Outdoors | `gTileset_General` (LeoB, imported) | **LeoB ORAS `secondary/sootopolis`** | `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS/tilesets/secondary/sootopolis`, door anims `sootopolis.png` and `sootopolis_peaked_roof.png`. Same metatile ids as vanilla. **CREDITS.md row (leob0505)**; `engine-edits.md` entry (replaces vanilla files in place) |
| Center, Mart | `gTileset_Building` | `PokemonCenter`, `Shop` | Vanilla |
| **League Lounge 1F and 2F** | `gTileset_Building` | **Brick Cafe Interior Secondary** | `.../Full Tilesets/Brick Cafe Interior Secondary` (Ekat99, imported to pokeemerald by Kumatora; credits: **Ekat, Vurtax (FRLG rips), Heartlessdragoon (RSE rips)**). Looking at its example: a brick wall with arched lit windows, a long counter with shelves of jars and bottles, 4 long tables with green chairs on a blue rug, a checker floor, door mats at the bottom: it is a lounge and a bar. `metatiles.bin` is 12288 bytes = 512 **triple-layer** metatiles, so it needs the Porytiles conversion Gen 4 Interior got. **Fallback:** vanilla `LAYOUT_LILYCOVE_CITY_CONTEST_LOBBY` (31 x 12, `Contest`), no import, a bright pink-and-purple room that looks like a contest lobby, which is the wrong mood |
| Cottage, boathouse, houses | `gTileset_Building` | `Gen4Interior` | Hollowbrook's |
| Hall of Past Champions | `gTileset_Building` | `CableClub` (vanilla, the Emerald Hall of Fame floor) | Vanilla `EverGrandeCity_HallOfFame` pattern, no import |
| Dive pool | `gTileset_Underwater` | vanilla | `Underwater_SootopolisCity` (20 x 10) copy |

**Why Brick Cafe for the Lounge.** README decision 3 says special buildings take a themed Team Aqua tileset and names Brick Cafe for eateries; the Lounge is a lounge with a bartender, a cloakroom and tables. The README's decision 5 (E4 and Champion rooms in vanilla Ever Grande tilesets) is about the League's rooms, not this off-duty lounge. I looked at the Palladium `championlacetq2.png` (a teal-tiled hall, red carpet, horn-shaped pillars) as an alternative and rejected it: it is the Champion's *chamber*, grand and cold, not a lounge.

**Palladium credit.** The first commit that traces the Hall image or `Elm's House.png` adds a row crediting the **Project Palladium team** with the file names.

---

## 6. Buildings and interiors

### 6.1 Overview

| # | Building | Footprint | Door | Interior maps | Layout |
|---|---|---|---|---|---|
| 1 | Pokémon Center | (15,5)-(18,8) | (16,8) | `Vesperhaven_PokemonCenter_1F`, `_2F` | `LAYOUT_POKEMON_CENTER_1F`, `_2F` |
| 2 | Mart | (33,5)-(36,8) | (34,8) | `Vesperhaven_Mart` | `LAYOUT_MART` |
| 3 | League Lounge | (1,16)-(10,23) | (6,23) | `Vesperhaven_LoungeFloor1`, `Vesperhaven_LoungeFloor2` | custom 31 x 12 each (Brick Cafe) |
| 4 | Cynthia's Cottage | (42,19)-(46,23) | (44,23) | `Vesperhaven_CynthiasCottage` | custom 13 x 10 (`Elm's House.png`) |
| 5 | Boathouse | (22,37)-(25,40) | (23,40) | `Vesperhaven_Boathouse` | G4-B (10 x 8) |
| 6 | Hall of Past Champions | (4,4)-(9,9) | (6,9) | `Vesperhaven_HallOfPastChampions` | custom 10 x 16 (`halloffamegscrevampzr1.png`) |
| 7 | House 1 | (42,9)-(45,12) | (43,12) | `Vesperhaven_House1` | G4-A (11 x 8) |
| 8 | House 2 | (3,36)-(6,39) | (4,39) | `Vesperhaven_House2` | G4-C (12 x 9) |
| 9 | The Pool (Dive) | none | Dive spot (25,28) | `Underwater_Vesperhaven` | copy of `Underwater_SootopolisCity` (20 x 10) |

About **11 maps** (card said nine; the Pool's dive map and the two-floor Center add two).

### 6.2 Pokémon Center and Mart (shared)

Vanilla, unmoved: nurse (7,2), mats (6,8),(7,8), stairs (1,6); Mart mats (3,7),(4,7), clerk (1,3). A **retired nurse** at the Center bench (10,6) `FACE_LEFT` ('remembers the Hoenn League'). Post-game Mart stock (card): Max Revive, Full Restore, Max Potion, Ultra Ball, Max Repel, PP Up.

### 6.3 League Lounge 1F (31 x 12, Brick Cafe): the Elite Four, the cloakroom

**Purpose.** The off-duty Elite Four, the bartender, a clerk, and **Troglodyte at the cloakroom** (the post-game job, `PostGame_Text_TrogEpilogue`). Plan (1 tile = 1 character). Legend: `#` wall, `Z` shelves of jars and bottles, `W` arched lit window, `k` counter, `b` bartender, `s` stool, `R` rug (walkable) and coat racks where they sit by the cloak counter, `t` table, `O` OSSIAN, `H` HYACINTH, `U` DUNMORE, `Y` DRAYDEN, `T` Troglodyte, `L` clerk, `P` plant, `^` stairs to 2F, `D` mats.

```
     x: 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
y0    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y1    # . Z Z Z Z Z Z Z Z Z Z . . W . . W . . W . . W . . . . . ^ #
y2    # . . . . . . b . . . . . . . . . . . . . . . . . . . . . . #
y3    # . . k k k k k k k k k . . . . . . . . . . . . . . . . . . #
y4    # . . . s . s . s . s . . . . . . . . . . . . H t t . . . . #
y5    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #
y6    # . . . . . . . . . R R R Y t t R R R R R . . . . . . . . . #
y7    # . O t . . . . . . R R t t R R t t R R R . . . . . . U . . #
y8    # . . . . . . . . . R R R R R R R R R R R . . . . . . . . . #
y9    # . . . . . . . k k k . . . . . . . . k k k k . . . . . . . #
y10   # P . . . . . . . L . . . . . . . . . R T R R . . . . . . P #
y11   # # # # # # # # # # # # # # D D # # # # # # # # # # # # # # #
```
- **Mats** (14,11),(15,11) to `Vesperhaven` warp 2 (the Lounge door (6,23)). **Stairs** (29,1) to 2F (29,1).
- **Objects (7):** **OSSIAN** (2,7) in a black armchair (`FACE_RIGHT`), a small table beside him at (3,7); **HYACINTH** (23,4) reading at the window table (24,4),(25,4) (`FACE_RIGHT`); **DUNMORE** (27,7) asleep (`FACE_LEFT`; talking wakes him, he naps again afterwards); **DRAYDEN** (13,6) with tea at table (14,6),(15,6) (`FACE_RIGHT`); **Bartender** (7,2) behind the bar counter (3..11,3), `FACE_DOWN` ('Nobody told you about this place.'); **League clerk** (9,10) behind the desk (8..10,9), `FACE_UP` (explains the rematch rules); **Troglodyte** (20,10) behind the cloak counter (19..22,9) with coat racks, `FACE_UP`: 'a sincere "sir" that is clearly painful'. The player stands at (20,8), faces south, the counter between.
- **Rematches (card):** OSSIAN, HYACINTH, DUNMORE and DRAYDEN fight on request: `trainerbattle_single` with `cleartrainerflag` per fight (postgame.md), rematch aces 80, 81, 82, 83. First win pays **PP Max** each (card).
- **Warps summary:** see section 7.

### 6.4 League Lounge 2F: the Terrace (31 x 12), the nine gym leaders

A copy of the 1F shell with the same Brick Cafe vocabulary, windows along the back wall onto the pool, **nine tables**, one leader each. The leaders sit in **gym order, left to right and top to bottom**, so the player can read the whole story in a loop. Positions (leader on the left of the table, facing right; the player stands above or below):

```
     x: 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
y0    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y1    # . . . W W . . . . W W . . . . W W . . . . W W . . . . . ^ #
y2    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #
y3    # . . . 1 t t . . . . . . . 2 t t . . . . . . . 3 t t . . . #
y4    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #
y5    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #
y6    # . . . 4 t t . . . . . . . 5 t t . . . . . . . 6 t t . . . #
y7    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #
y8    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #
y9    # . . . 7 t t . . . . . . . 8 t t . . . . . . . 9 t t . . . #
y10   # P . . . . . . . . . . . . . . . . . . . . . . . . . . . P #
y11   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
```
| Seat | Leader (original ace → rematch ace, from the card) | Tile |
|---|---|---|
| 1 | GRETA (12 → 70) | (4,3) |
| 2 | HACHIMEL (19 → 71) | (14,3) |
| 3 | SANZUFORD (25 → 72) | (24,3) |
| 4 | HAGANE (31 → 73) | (4,6) |
| 5 | WAKASAGI (37 → 74) | (14,6) |
| 6 | TOBIN (42 → 75) | (24,6) |
| 7 | ASEBY (48 → 76) | (4,9) |
| 8 | SUZURAN (55 → 77) | (14,9) |
| 9 | MIZZLE (60 → 78) | (24,9) |

The floor has **nine leader objects** and nothing else (well under 15). The only exit is the **stairs (29,1)** down to 1F (the bottom row is a plain wall; the player arrives on the stair tile). Each leader: deadpan holiday talk and a rematch on request; first win pays a **Rare Candy** (card). Their rematch teams are the built teams plus one Pokémon each (card, `trainer-roster.md`), `IVs: 0` lines, reused vanilla ids: **the author must pick the vanilla ids** (card open question 4), which is a later job.

### 6.5 Cynthia's Cottage (13 x 10, from `Elm's House.png`)

**Purpose.** Tea, a short story, **Cynthia's rematch** (ace 85, Ability Capsule on the first win), and the **letter to carry to Gatsby**. Palladium `Elm's House.png` (13 x 10) shows exactly the shape: a desk with a computer at the top left, a window, a stove and a kettle, green display shelves along the top right, a green carpet with a blue table and four chairs in the middle, a red mat at the bottom. Plan, Gen 4 vocabulary (`C` writing desk with stationery, `W` window, `S` stove and kettle, `B` trophy shelves, `f` tea table, `c` cushions or chairs, `R` rug, `N` Cynthia, `P` plant, `D` mats):

```
     x: 0 1 2 3 4 5 6 7 8 9 0 1 2
y0    # # # # # # # # # # # # #
y1    C C . W W . S . B B B B .
y2    C C . . . . S . B B B B *      * = Sea Incense (after tea)
y3    . . . . . . . . . . . . .
y4    . . . R R R R R R R . . .
y5    . P . R c f f c R N . P .      N = Cynthia (9,5) standing at the table, facing left
y6    . . . R c f f c R R . . .
y7    . . . R R R R R R R . . .
y8    . . . . . . . . . . . . .
y9    . . . . . D D . . . . . .
```
- **Cynthia** at (9,5) `FACE_LEFT`: dry, warm, sharp; mentions the old friend who writes. Talk branches: **tea** (`FLAG_VESPERHAVEN_TEA_DONE`, a short scripted pour at the table, `PostGame_Text_*` drafts to extend), then **the letter** (`FLAG_VESPERHAVEN_LETTER_TAKEN`, a key item or flag-only), then **the rematch** (`TRAINER_CYNTHIA`, ace 85, `MUS_VS_CHAMPION`). After tea the **Sea Incense** appears at (12,2).
- `bg_event`s: the stationery desk (0,1) (a half-written letter), trophy shelves (8..11,1) (three trophies, one a Sinnoh shield). A **kettle** on the stove (6,1): the card's recurring tea.
- **Warps:** mats (5,9),(6,9) to `Vesperhaven` warp 3 (door (44,23)).

### 6.6 Boathouse (G4-B, 10 x 8)

**Purpose.** A bench, a kettle and a rowing boat; **Gatsby optional** (card open question 5). Plan G4-B: a **bench** (decor) at (2,5), a kettle on the stove nook (8,1); a rowing-boat model on the table (bg_event (4,5)). Objects: **Gatsby** at (3,5) `FACE_RIGHT`, **hidden until `FLAG_VESPERHAVEN_LETTER_TAKEN` is set** (Cynthia's letter): after the errand he serves tea; the **kettle gift**: a berry and a TM (Hyper Beam, PROPOSED, check the TM ledger). The **Boatman** stands outside at (24,41); at night (`GetTimeOfDay`-style check optional) he rows the player to the R29 strait (optional, PROPOSED). Warps: mats (3,7),(4,7) to `Vesperhaven` warp 4 (door (23,40)).

### 6.7 Hall of Past Champions (10 x 16, from `halloffamegscrevampzr1.png`)

The Palladium image (160 x 263): a red-and-gold wall with a blue Hall of Fame recording console at the top, a plaque at (6,5), a diamond-pattern floor, a small exit at the bottom centre. Plan (`M` console, `p` portrait `bg_event` on a wall tile, `A` attendant, `*` Rare Candy, `D` mats):

```
     x: 0 1 2 3 4 5 6 7 8 9
y0    # # # # # # # # # #
y1    # # # M M M M # # #
y2    # . . M M M M . . #
y3    # . . . . . . . . #
y4    p . . . . . . . . p
y5    # . . . . A . . . #
y6    p . . . . . . . . p
y7    # . . . . . . . . #
y8    p . . . . . . . . p
y9    # . . . . . . . . #
y10   p . . . . . . . . p
y11   # . . . . . . . . #
y12   p . . . . . . . . p
y13   # . . . . . . . . #
y14   # . * . . . . * . #
y15   # # # # D D # # # #
```
- **Portraits** are `bg_event`s on the wall tiles at x 0 and x 9, y 4, 6, 8, 10, 12: ten portraits of past Champions, oldest at the top left; **Cynthia's is the newest finished** at (0,12); **the last portrait (9,12) is an unfinished frame** (Veldris is seatless, Cynthia is the guest; the card's note).
- **Hall attendant** at (5,5) `FACE_DOWN`: names the Champions in order and the sad joke about the empty frame.
- **Rare Candy x2** (visible item balls) at (2,14) and (7,14) (card, 'after the League').
- **Warps:** mats (4,15),(5,15) to `Vesperhaven` warp 5 (door (6,9)).
- The console at (3..6,1..2) reuses the vanilla Hall of Fame machine metatiles (it is decoration here; do not trigger the real Hall of Fame).

### 6.8 Staff houses

- **House 1 (G4-A 11 x 8):** a retired League clerk's family: a mother (5,6) `FACE_UP`, a father (8,3) `FACE_UP`, a child (9,5) wandering. Warps: mats (2,7),(3,7) to `Vesperhaven` warp 6.
- **House 2 (G4-C 12 x 9):** a lighthouse keeper's widow and a Pokémon of hers: an old woman (8,5) `FACE_LEFT`, an ambient Slowbro (3,5) wandering. Warps: mats (5,8),(6,8) to `Vesperhaven` warp 7.

---

## 7. Door and warp table

`Vesperhaven` outdoor warps:

| # | Tile | Destination | Dest warp |
|---|---|---|---|
| 0 | (16,8) | `Vesperhaven_PokemonCenter_1F` | 0 |
| 1 | (34,8) | `Vesperhaven_Mart` | 0 |
| 2 | (6,23) | `Vesperhaven_LoungeFloor1` | 0 |
| 3 | (44,23) | `Vesperhaven_CynthiasCottage` | 0 |
| 4 | (23,40) | `Vesperhaven_Boathouse` | 0 |
| 5 | (6,9) | `Vesperhaven_HallOfPastChampions` | 0 |
| 6 | (43,12) | `Vesperhaven_House1` | 0 |
| 7 | (4,39) | `Vesperhaven_House2` | 0 |
| (dive) | (25,28) | `Underwater_Vesperhaven` | |

| Interior | Tiles | Destination | Dest warp |
|---|---|---|---|
| `Vesperhaven_PokemonCenter_1F` | (6,8),(7,8) / stairs (1,6) | `Vesperhaven` 0 / `_2F` | |
| `Vesperhaven_Mart` | (3,7),(4,7) | `Vesperhaven` | 1 |
| `Vesperhaven_LoungeFloor1` | (14,11),(15,11) | `Vesperhaven` | 2 |
| `Vesperhaven_LoungeFloor1` / `_2` | (29,1) | each other | |
| `Vesperhaven_CynthiasCottage` | (5,9),(6,9) | `Vesperhaven` | 3 |
| `Vesperhaven_Boathouse` | (3,7),(4,7) | `Vesperhaven` | 4 |
| `Vesperhaven_HallOfPastChampions` | (4,15),(5,15) | `Vesperhaven` | 5 |
| `Vesperhaven_House1` | (2,7),(3,7) | `Vesperhaven` | 6 |
| `Vesperhaven_House2` | (5,8),(6,8) | `Vesperhaven` | 7 |

(Follow Porymap's numbering if it differs.) Escape warp: `setescapewarp MAP_VESPERHAVEN, 16, 9`.

---

## 8. NPCs and objects outdoors (about 8)

| Object | Tile | Move | Topic |
|---|---|---|---|
| Fisher | (28,9) | `FACE_RIGHT` | 'We have the sea to ourselves.' Hint on Silverstrand |
| Kid | (36,18) | `WANDER_AROUND` | Wants to know what Fly is |
| Dockhand W | (4,27) | `FACE_DOWN` | West pontoon, ferry times (R27) |
| Dockhand E | (47,27) | `FACE_DOWN` | East pontoon; the Kingsquay ferry reaches here post-game |
| Boatman | (24,41) | `FACE_UP` | Optional night row to the R29 strait |
| Coast guard cutter W | (2,29) | static | `SS_TIDAL` ship object, hidden at game clear: 'League business. Come back when you have finished.' |
| Coast guard cutter E | (49,29) | static | same |
| Coast guard cutter SW | (9,41) | static | same |
| Wingull on the fountain | (24,4) | `LOOK_AROUND` | Ambient |

Bg events: town sign (24,10) (the card's note: nothing here is on a signpost, so the sign is a small plaque 'VESPERHAVEN. PLEASE KEEP IT QUIET.'), statue plaque (25,22) on the islet, Lounge plaque (5,24), Cottage mailbox (41,23), gate signs. Heal tile (16,9).

---

## 9. Items and secrets (positions)

| Item | Where | Gate |
|---|---|---|
| Rematch gifts | Lounge (Rare Candy x9 at leaders, PP Max x4 at E4) and Cottage (Ability Capsule) | First win each |
| Letter for Gatsby | Cottage, Cynthia | After tea |
| Max Elixir (hidden) | Behind the Lounge at (5,15) | None |
| Rare Candy x2 | Hall of Past Champions (2,14), (7,14) | After the League |
| Pearl, Big Pearl | Pool bottom (`Underwater_Vesperhaven`), visible at (4,5) and (10,7) | Dive |
| Sea Incense | Cottage shelf (12,2) | After tea |
| Ability Capsule | Cynthia rematch | Win |
| Berry and TM (Hyper Beam, PROPOSED) | Boathouse kettle | After the letter errand |

---

## 10. Gates, scripts and events the build needs

- **One gate flag:** `FLAG_VESPERHAVEN_GATES_OPEN`, set by the town's `ON_TRANSITION` the first time `FLAG_SYS_GAME_CLEAR` is set (card). It hides the three cutter objects, opens the **north service gate** (a metatile swap at (24..27,3)) and the **south-east service gate**, and removes the pontoon ropes. The R27/R28/R29/R30 cards share it (the R27 card suggests `FLAG_R27_CUTTER_GONE` could be the same flag). Because the player's first arrival is by R21 *after* game clear, the gate is already open then; the flag matters for the sea and for R30's gate.
- **First-arrival beat:** `ON_TRANSITION` sets `FLAG_VISITED_VESPERHAVEN` (fly destination, Feather Badge) and the heal location. No cutscene is required.
- **Troglodyte's job:** `FLAG_VESPERHAVEN_TROG_HIRED` shows him at the cloakroom (set at game clear). His rematch is **not** here: it is at Argent Peak ([landmarks-south-detail.md](landmarks-south-detail.md)).
- **Rematch scripts:** each seat is a trainer object; the script `cleartrainerflag`s the old id before each fight, then pays the gift once (`FLAG_REMATCH_<NAME>`).
- **Cynthia's tea** is a short scripted scene on a once-only flag.
- **Boatman and kettle** are optional.

**Flags (not claimed, from the card):** `FLAG_VISITED_VESPERHAVEN`, `FLAG_VESPERHAVEN_GATES_OPEN`, `FLAG_REMATCH_GRETA` to `FLAG_REMATCH_MIZZLE` (nine), `FLAG_REMATCH_OSSIAN` to `_DRAYDEN` (four), `FLAG_REMATCH_CYNTHIA`, `FLAG_VESPERHAVEN_TEA_DONE`, `FLAG_VESPERHAVEN_LETTER_TAKEN`, `FLAG_VESPERHAVEN_LETTER_DELIVERED`, `FLAG_VESPERHAVEN_TROG_HIRED`, `FLAG_RECEIVED_ABILITY_CAPSULE_CYNTHIA`, `FLAG_HIDDEN_ITEM_VESPERHAVEN_MAX_ELIXIR`. That is 15 flags for rematches alone: check [../../flags.md](../../flags.md) (316 spare flags); consider **one flag per rematch row packed into a single var** or reusing the reused trainers' own flags.

---

## 11. Build checklist (in order)

1. Read flags.md, engine-edits.md, trainer-roster.md. Confirm the Pinnacle and R21 exist (build last).
2. Decide the LeoB `sootopolis` import and the Brick Cafe import (a Porytiles conversion); credits and engine-edits in the commit that imports each.
3. Duplicate `SootopolisCity`, Change Dimensions to 52 x 44, clean events and heal locations, set `MAPSEC_VESPERHAVEN`.
4. Shape the pool and terraces, place Center and Mart on the north terrace, the Lounge on the west ledge, the cottage on the east ledge, the boathouse, the Hall, two houses, the stairs and sea gates.
5. Build the shared Center and Mart; the G4 houses and boathouse; the Hall (Palladium plan on `CableClub`); the cottage (Gen 4).
6. Build **Lounge 1F** (Brick Cafe, or the Contest lobby fallback), then duplicate the shell for **2F** and repaint the tables.
7. Warps (section 7) and connections (north R21, west R27, east R28, south-west R29, south-east R30). The roads must exist first.
8. Close and reload Porymap after Claude edits events.
9. Claude wires the gate flag, rematch scripts, cutters, dialogue (from `league.inc`); dialogue_check; `make -j4`.
10. Update design docs, credits; no ROM or save staged; commit and push.

---

## 12. Open questions

1. **Cynthia's tea and rematch here or in Hollowbrook** (card question 1): I built the cottage here; the reunion stays in Hollowbrook.
2. **Brick Cafe for the Lounge** needs a triple-layer conversion. Fallback is the vanilla Contest lobby; which mood does the author want?
3. **Door faces west.** Emerald doors always face south; I read the card as the garden path arriving from the west. OK?
4. **15 rematch flags** is a lot of the 316 spare flags. Pack them in a var, or reuse the reused trainers' own flags (the script clears and re-sets them anyway)?
5. **Gatsby at the Boathouse** (card question 5) duplicates the Hollowbrook kettle plan; keep or cut?
6. **A Pokémon 'Slowbro' in House 2** is ambient decoration and could be dropped.
7. **Weather `SHADE`** may look muddy over the LeoB colours; test it in Porymap before committing.
