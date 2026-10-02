# KINGSQUAY: detailed design (harbour city, no gym)

Status: **PROPOSED.** Written 2026-10-01 from [../interiors/README.md](../interiors/README.md), [../interiors/catalogue.md](../interiors/catalogue.md), [../README.md](../README.md), [../../interiors.md](../../interiors.md), [../index.md](../index.md), the card [../towns/kingsquay.md](../towns/kingsquay.md), roads R23 and R24 ([../routes-south.md](../routes-south.md)), the Goldsworth drafts ([../../goldsworth.md](../../goldsworth.md), [../../dialogue/goldsworth.inc](../../dialogue/goldsworth.inc)) and the Project Palladium renders `SSAqua1/2/Cabins/Captain`, `Olivine City`, `Cianwood City`. House templates **G4-A, G4-B, G4-C** are defined in [ebbsworth.md](ebbsworth.md) section 6.0. Neighbours: [ebbsworth.md](ebbsworth.md), [driftsands.md](driftsands.md), [beaconmouth.md](beaconmouth.md), [vesperhaven.md](vesperhaven.md). Road detail: [routes-south-detail.md](routes-south-detail.md).

**New minor names and details introduced in this file are all PROPOSED:** Quayside Tea Rooms, `Ferry_Deck`, `Ferry_Galley`, `Ferry_CaptainsCabin`, the Ferry Captain, the optional ferry-hand rematch.

Conventions: **(x, y) from the top-left tile (0,0)**; a footprint is `(x0,y0)-(x1,y1)` inclusive; a 4-wide building's door is the bottom-row tile `(x0+1, y1)` (vanilla rule, checked on Lilycove: Pokémon Center door (24,14) on footprint x23-26; houses' doors at `x0+1`); larger buildings give their door explicitly. Interior mats are two tiles wide as in vanilla.

---

## 1. Quick facts

| | |
|---|---|
| Map | `Kingsquay`, **64 x 40** (`(64+15)*(40+14) = 4266`, limit 10240) |
| Exterior base | Vanilla `LilycoveCity` (80 x 40), trimmed, with **LeoB ORAS `secondary/lilycove`** (see section 5). Palladium `Olivine City.png` supplies only the dock mood (its lighthouse goes to Beaconmouth, not here) |
| Section / fly | `MAPSEC_KINGSQUAY`; fly town; `HEAL_LOCATION_KINGSQUAY` on the tile outside the Center door, (56,21) |
| Music | `MUS_LILYCOVE` (town and shops), `MUS_LILYCOVE_MUSEUM` (museum), `MUS_SAILING` (ferry) |
| Weather / type | `WEATHER_SUNNY`, `MAP_TYPE_CITY` |
| Gym / scheme | None. Scheme 9 **setup** (Tallow & Crane, the invoice pile) and a **Goldsworth house** (cousins Chad and Winston) |
| Roads | R23 north (land path at the north gate, water at the north-west bay), R24 east, ferries from the south pier |
| Objects | Town map 11; every interior under 15 |

---

## 2. Description

**First glance from R23 (the north gate).** The land path comes over a pine ridge and drops through a gateway into a hill street. To the left a pale, wide villa with white steps stands behind iron railings; to the right a department-store tower; between them the road falls away to a cobbled square with a fountain, and beyond it the masts. The player sees the whole city in one screen: it is the first place in Veldris that looks like it has money.

**From R23 by water.** A stone slipway in the north-west bay lets you step ashore beside the hill; the villa's railings come right down to the sea wall.

**From R24 (the east gate).** A fenced lane opens onto the east end of the square: the Pokémon Center first, then the notice board and the solicitors' brass plate.

**From the sea (ferry).** A long quay with three piers, cranes and stacked container-boxes (decoration), a yacht in the east berth, a smaller ship moored by the ferry pier.

**Mood, colour, sound, time of day.** Busy, bright and a little pleased with itself. Palette: white and pale stone, sea blue, the LeoB Lilycove orange-brown roofs and teal awnings, polished brass on the solicitors' door, yellow gold on the villa. Sound: the Lilycove track, a ship's horn at the quay (one-shot object sound on the ferry hand's script). **Time of day: bright late morning**; the stock sunny palette. After Scheme 9 nothing changes in the palette, only a 'FOR SALE' sign appears on the yacht.

**The one memorable view.** The top of the hill-street steps at (23,11): villa on the left, Emporium on the right, the fountain square straight ahead and the sea behind it. Keep the three sight lines clear of trees.

---

## 3. Street layout in words (a numbered walk)

Land runs from a hill in the north-west to a long south quay. All main streets are cobbles; the quay is stone.

1. **North gate and hill street (x 21-26, y 0-12).** R23's land path arrives at (22..25, 0) through a stone gateway (two pillars, fence stubs). The street runs south, 4 tiles wide, down to the square. A signpost 'KINGSQUAY' at (21,2).
2. **The Goldsworth Villa (10,1)-(21,8)**, door (15,8). A pale-stone villa with white steps (x 14-16, y 9-10) down to the street, behind an **iron fence** (y 10, x 10-21) with a gate at (15,10). Sign 'GOLDSWORTH RESIDENCE' at (13,10). Lawn and clipped bushes either side.
3. **North-west bay and slipway (x 0-8, y 0-12).** Water (R23's sea arrival). A stone slipway at (9,11)-(9,13) climbs to a path joining the hill street.
4. **Emporium terrace.** The **Kingsquay Emporium** (35,3)-(43,9) (9 x 7), door (39,9), stands on the east side of the north terrace; a stair-free ramp at (38..40,10) leads down to the square.
5. **Market Square (x 18-46, y 11-23).** Cobbles. A **fountain** (2 x 2 basin) at (31,16)-(32,17), benches at (28,19) and (35,19), lamp posts every 6 tiles.
6. **Solicitors' row (east of the square, x 47-53, y 10-16).** **Tallow & Crane** (48,11)-(52,15), door (50,15), brass plate on the door; a notice board at (46,15).
7. **Tea Rooms (optional, 38,12)-(43,16)**, door (40,16): the Quayside Tea Rooms, on the square's north-east corner.
8. **East end and Pokémon Center.** The **Center** at (55,17)-(58,20), door (56,20) (heal tile (56,21)); east of it the lane to the **east gate** (decorative gateway at x 60-61, y 21-24, R24 connection at x 63, y 20-24).
9. **Museum and Fan Club row (west, x 3-18, y 13-27).** A short street: **Maritime Museum** (4,14)-(10,20) door (7,20); **Pokémon Trainer Fan Club** (12,15)-(17,20) door (14,20); the **Move Reminder's House** (3,23)-(6,26) door (4,26); the **retired pilot's house** (11,23)-(14,26) door (12,26).
10. **Harbour (y 27-39).** A quay at y 27-29 from x 8 to x 58. Three piers: **west pier** x 14-17, y 30-36; **middle pier** x 28-33, y 30-37 with the **Ferry Terminal** at its root (27,23)-(33,28), door (30,28); **east pier** x 44-48, y 30-37 with **Chad's yacht** in the berth at (46..49, 32..36). Beside the west pier a **Harbour Master's Hut** (21,24)-(24,27), door (22,27). A **dockhand's house** (36,24)-(39,27), door (37,27). South-east quay (x 50-62, y 27-31): crates and stacked containers, a crane (decoration).

Surfable water: everything below the quay, the north-west bay. No grass inside the city.

---

## 4. Map plan

Sketch, **1 character = 2 x 2 tiles** (32 x 20 characters for 64 x 40 tiles; the tables are exact, this is orientation only). Legend: `~` water, `V` Goldsworth Villa, `G` hill street, `E` Emporium, `s` steps or slipway, `-` villa fence, `T` Tallow & Crane, `e` Tea Rooms, `o` fountain, `M` Museum, `F` Fan Club, `R` Move Reminder, `p` pilot's house, `h` Harbour Master, `B` Ferry Terminal, `d` dockhand, `P` Pokémon Center, `g` east gateway, `>` R24 connection, `=` quay, `#` piers, `Y` the yacht, `c` crates and cranes.

```
x:  0    1    2    3    4    5    6 
y0  ~~~~~VVVVVGGGG..................
y2  ~~~~~VVVVVGGGG...EEEEE..........
y4  ~~~~~VVVVVGGGG...EEEEE..........
y6  ~~~~~VVVVVGGGG...EEEEE..........
y8  ~~~~~VVVVVGGGG...EEEEE..........
y10 ~~~~s-----GGGG.....ss...TTT.....
y12 ~~~~s.....GGGG.....eee..TTT.....
y14 ..MMMMFFF..........eee..TTT.....
y16 ..MMMMFFF......oo..eee.....PPP..
y18 ..MMMMFFF..................PPP..
y20 ..MMMMFFF..................PPPg>
y22 .RRR.ppp.....BBBB.............g>
y24 .RRR.ppp..hhhBBBB.dd..........g>
y26 .RRR=ppp==hhhBBBB=dd=====ccccccc
y28 ....=========BBBB========ccccccc
y30 ~~~~~~~##~~~~~###~~~~~###ccccccc
y32 ~~~~~~~##~~~~~###~~~~~#YY~~~~~~~
y34 ~~~~~~~##~~~~~###~~~~~#YY~~~~~~~
y36 ~~~~~~~##~~~~~###~~~~~#YY~~~~~~~
y38 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
(The header digits mark every 10 tiles: `0` at x 0, `1` at x 10, and so on. The sketch was generated from the footprints in section 6.1, so they agree.)

**Connections:**

| Edge | Neighbour | Offset | Notes |
|---|---|---|---|
| North | `R23` (south end) | 0 | Land path x 21-26 at y 0; water x 0-8 at y 0 (bay). R23's south end must have the path at x 21-26 and water at x 0-8 (see routes-south-detail.md, R23) |
| East | `R24` (west end) | 0 | Lane x 63, y 20-24. R24's west end is the lane's start |
| South | none | | The sea is decoration; the ferry is a warp |
| West | none | | Cliff and trees |

---

## 5. Base, tilesets, palette notes

**Exterior base.** Duplicate `LilycoveCity` (80 x 40) and **Change Dimensions** to 64 x 40. The vanilla map already has: the white pillared museum at top-left (x 7-18, y 0-8) which **becomes the Goldsworth Villa** (its wide white stair is the villa's steps); the five-storey department store at top centre (x 23-31, y 0-6) which **becomes the Emporium** (move or recopy it to (35..43, 3..9)); the Center (x 23-26, y 11-14); the Fan Club (the gold-roofed building, x 36-41, y 20-24); the contest-hall block (x 20-26, y 18-24), reused as the **Maritime Museum** exterior; the red-roofed harbour building (x 9-15, y 27-32), reused as the **Ferry Terminal**; several blue-roofed houses. Remove the cliffs and Aqua Hideout cave entrance on the right. **Palladium `Olivine City.png`** (44 x 41) is used only as a dock reference: its pier at the bottom (moored red-roofed ship at x 18-25, y 31-37, boardwalk x 20-22, y 29-31) shows how a pier reaches the water.

**Tilesets (recommended):**

| Where | Primary | Secondary | Source, credit |
|---|---|---|---|
| Kingsquay outdoors | `gTileset_General` (LeoB, already imported) | **LeoB ORAS `secondary/lilycove`** | `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS/tilesets/secondary/lilycove` (`14 - Lilycove.png` shows it). Same metatile ids as vanilla. **CREDITS.md row (leob0505)**, door anims `lilycove.png`, `lilycove_dept_store.png` (Emporium door), optionally `lilycove_wooden.png`. Replaces vanilla files in place, so a `design/engine-edits.md` entry |
| Emporium floors and rooftop | `gTileset_Building` | `Shop` | Vanilla |
| Museum | `gTileset_Building` | `LilycoveMuseum` | Vanilla |
| Fan Club, Move Reminder, Harbour Master, dockhand, pilot, Goldsworth House | `gTileset_Building` | `Gen4Interior` | Hollowbrook's tileset (credited) |
| Tallow & Crane | `gTileset_Building` | **Little Office Interior Secondary** (Ekat99, imported by Kumatora) | `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/Little Office Interior Secondary`. **Credit row: 'Ekat'** (one name, per its credits.md, plus 'imported to pokeemerald by Kumatora'). Its `metatiles.bin` is 2880 bytes, which is either 180 two-layer or 120 triple-layer metatiles (ambiguous): open it in Porymap first; if triple-layer it needs the same Porytiles conversion Gen 4 Interior got. **Fallback:** vanilla `RustboroCity_DevonCorp_1F` layout (19 x 9, Facility), no import |
| Quayside Tea Rooms (optional) | `gTileset_Building` | **Brick Cafe Interior Secondary** (Ekat99 via Kumatora; credits: Ekat, Vurtax, Heartlessdragoon) | `.../Full Tilesets/Brick Cafe Interior Secondary`. Its `metatiles.bin` is 12288 bytes = 512 **triple-layer** metatiles, so it also needs the Porytiles conversion; skip the Tea Rooms if the author does not want a second conversion job |
| Ferry Terminal | `gTileset_General` | `Facility` | Vanilla `LAYOUT_HARBOR` (24 x 15) |
| Ferry deck, galley, captain's cabin | `gTileset_General` | `InsideShip` | Vanilla SS Tidal layouts (same look as the Palladium SS Aqua) |

**Not recommended here:** *Brick City Secondary* (brick canal-and-boats town) is triple-layer (9000 bytes / 24 = 375 metatiles, not a multiple of 16), and the catalogue earmarks it for Gildhaven; LeoB Lilycove already gives a bright harbour city.

**What has to be redrawn:** the fountain (check the Lilycove secondary for a statue or basin metatile; if none, build a 2 x 2 stone basin from the quay-edge tiles with a lamp post in the middle), the three piers (copy from Lilycove's own pier or Slateport's), cranes and containers (stacked crate tiles, decoration only), the villa railings (the Lilycove iron fence pieces), and the gateway pillars.

---

## 6. Buildings

### 6.1 Overview

| # | Building | Footprint | Door | Interior maps | Layout |
|---|---|---|---|---|---|
| 1 | Pokémon Center | (55,17)-(58,20) | (56,20) | `Kingsquay_PokemonCenter_1F`, `_2F` | `LAYOUT_POKEMON_CENTER_1F`, `_2F` |
| 2 | Emporium (the Mart) | (35,3)-(43,9) | (39,9) | `Kingsquay_Emporium_1F`, `_2F`, `_3F`, `_Rooftop` | `LILYCOVE_CITY_DEPARTMENT_STORE_1F`, `_2F`, `_3F` (18 x 8 each), `_ROOFTOP` (18 x 12) |
| 3 | Ferry Terminal | (27,23)-(33,28) | (30,28) | `Kingsquay_FerryTerminal` | `LAYOUT_HARBOR` (24 x 15) |
| 4 | Maritime Museum | (4,14)-(10,20) | (7,20) | `Kingsquay_MaritimeMuseum_1F`, `_2F` | `LILYCOVE_CITY_LILYCOVE_MUSEUM_1F` (21 x 14), `_2F` (22 x 13) |
| 5 | Pokémon Trainer Fan Club | (12,15)-(17,20) | (14,20) | `Kingsquay_FanClub` | `LILYCOVE_CITY_POKEMON_TRAINER_FAN_CLUB` (12 x 14) |
| 6 | Move Reminder's House | (3,23)-(6,26) | (4,26) | `Kingsquay_MoveRemindersHouse` | G4-B (10 x 8) |
| 7 | Tallow & Crane Solicitors | (48,11)-(52,15) | (50,15) | `Kingsquay_TallowAndCrane` | Little Office, custom 14 x 10 (or Devon 1F fallback) |
| 8 | Goldsworth House | (10,1)-(21,8) | (15,8) | `Kingsquay_GoldsworthHouse` | The shared Goldsworth layout (13 x 11), defined below |
| 9 | Harbour Master's Hut | (21,24)-(24,27) | (22,27) | `Kingsquay_HarbourMastersHut` | G4-A (11 x 8) |
| 10 | Dockhand's House | (36,24)-(39,27) | (37,27) | `Kingsquay_DockhandsHouse` | G4-A |
| 11 | Retired Pilot's House | (11,23)-(14,26) | (12,26) | `Kingsquay_PilotsHouse` | G4-C (12 x 9) |
| 12 | Quayside Tea Rooms (optional, PROPOSED) | (38,12)-(43,16) | (40,16) | `Kingsquay_TeaRooms` | Brick Cafe, custom 13 x 9 |
| 13 | Ferry boat | none | via the terminal | `Ferry_Deck`, `Ferry_Galley`, `Ferry_CaptainsCabin` | SS Tidal layouts and Palladium `SSAqua` images |

About **15 maps** (13 buildings and the ferry set), all with section `MAPSEC_KINGSQUAY` except the ferry set (use `MAPSEC_KINGSQUAY` too, interiors cost no section).

### 6.2 Pokémon Center (shared)

Unchanged `LAYOUT_POKEMON_CENTER_1F` and `_2F`: nurse (7,2), mats (6,8),(7,8), stairs (1,6); 2F stairs (1,6), Union Room (5,1), Trade (9,1). Two ambient objects at most (a sailor on the bench at (10,7), a diver at (11,8)). The Center stands at the east end of the square so a player leaving for Driftsands heals on the way.

### 6.3 Kingsquay Emporium (the department store, 3 floors and a rooftop)

Use stairs only: the vanilla elevator script is tied to a five-floor list ([../towns/kingsquay.md](../towns/kingsquay.md)). On every floor **paint over the elevator door with a plain wall tile** (or leave the doors as a closed lift with a `bg_event` 'OUT OF ORDER') and **delete the elevator warp at (2,1)**. Floor positions are from the vanilla Lilycove maps.

| Floor | Layout | What the player does | Warps (vanilla positions) | Objects (vanilla positions, retargeted) |
|---|---|---|---|---|
| **1F, services** | `DEPARTMENT_STORE_1F` 18 x 8 | Floor guide, a free PC, the 'daily window'. No shop | Mats (8,7),(9,7) to `Kingsquay` warp 1 (door (39,9)); stairs (16,1) to 2F warp 0 | Two clerks (8,2) and (10,2) `FACE_DOWN` (info desk, one explains the floors, one runs the PC); a wandering shopper (14,5); a girl (4,4) wandering; a man (3,6) looking around; a Azumarill (2,6) looking around (ambient). PC as a `bg_event` at (14,1) |
| **2F, balls and medicine** | `DEPARTMENT_STORE_2F` 18 x 8 | Clerk left (7,6): potions and healing (Super Potion, Hyper Potion, Max Potion, Revive, Full Heal, Antidote line). Clerk right (10,6): **Ultra Ball, Net Ball, Dive Ball**. Prices are placeholders | Stairs down (16,1) to 1F warp 2; stairs up (13,1) to 3F warp 0 | Clerks (7,6),(10,6); the vanilla cook (8,2) becomes a lemonade seller (flavour, no shop); a shopper (0,5); a sailor (13,5) |
| **3F, TM counter** | `DEPARTMENT_STORE_3F` 18 x 8 | Clerks (8,2),(10,2): **TM Hyper Beam, TM Rock Tomb** plus battle items (X items). TM list and prices PROPOSED, **check the TM ledger in [../../gyms.md](../../gyms.md) for duplicates before wiring** | Stairs down (13,1) to 2F warp 1; stairs up (16,1) to the **Rooftop** warp 0 (instead of 4F) | Clerks; a runner (0,5); a man (7,7); a woman (13,5) |
| **Rooftop, vending corner** | `DEPARTMENT_STORE_ROOFTOP` 18 x 12 | Vending machines at (9,1),(10,1) (`bg_event`s with the three drinks of vanilla, free of charge to look, buy via the vanilla vending script); a visible **Max Revive** in the corner at (16,10); the rooftop kid at (15,5) asks for a drink | Stairs (13,3) to 3F warp 1 | Sale woman (6,1) kept as the drink seller; kid (15,5); a man (4,4); a man (7,5) wandering |

**Warp numbers to set (so the loop closes):** 1F warp 2 (16,1) to 2F warp 0; 2F warp 0 (16,1) to 1F warp 2; 2F warp 1 (13,1) to 3F warp 0; 3F warp 0 (13,1) to 2F warp 1; 3F warp 1 (16,1) to Rooftop warp 0; Rooftop warp 0 (13,3) to 3F warp 1. 4F and 5F are not built.

The Mart role is the Emporium: **no separate `LAYOUT_MART`**. Dive Ball and Net Ball are sold on 2F as the card says.

### 6.4 Ferry Terminal (vanilla `LAYOUT_HARBOR`, 24 x 15)

**Purpose.** Ticket counter and the ferry hand; the ferry itself is the next section. Vanilla map: mats (11,14),(12,14), a ticket-attendant object stack at (8,10), the docked ship object (graphic `SS_TIDAL`) at (8,9), a sailor wandering at (3,13). The water pool and rail fill the middle, the attendant stands at the deck edge.

**Veldris use.**
- **Ferry hand** (the attendant, (8,10) `FACE_DOWN`): sells tickets. Destinations menu: **Beaconmouth** (enabled once the player has walked into Beaconmouth, `FLAG_KINGSQUAY_FERRY_BEACONMOUTH`), **Vesperhaven** (post-game, `FLAG_KINGSQUAY_FERRY_VESPERHAVEN`). Before either is set the ferry hand says the ferry 'does not go anywhere you have not been'.
- The docked ship object (8,9) stays as the visible vessel.
- A **sailor** wanders at (3,13); a **sign** 'FERRY TIMETABLE' at (13,12) (`bg_event`).
- **Warps:** mats (11,14),(12,14) to `Kingsquay` warp 2 (door (30,28)); boarding is a script warp (not a tile) to `Ferry_Deck`.

### 6.5 The ferry (optional garnish, SS Aqua images)

Palladium `SSAqua1.png` (674 x 352), `SSAqua2.png` (544 x 256), `SSAquaCabins.png` (693 x 380) and `SSAquaCaptain.png` (176 x 191, **11 x 11 tiles**) show a Johto liner: pale lavender walls with round porthole lamps, wooden decks and white-framed doors. The vanilla SS Tidal maps (`SSTidalCorridor` 18 x 13, `SSTidalLowerDeck` 17 x 13, `SSTidalRooms` 36 x 18, tilesets `General` + `InsideShip`) are the same style, already in the tree, so the ferry needs **no Team Aqua tileset and no credit beyond Project Palladium** (credit the team in `CREDITS.md` in the commit that first traces an image).

Plan (cheapest first):
1. **v1: no ferry maps.** The ferry hand's script fades to black with the ship horn and `warp`s straight to the destination quay. Zero maps.
2. **v2: `Ferry_Deck` (18 x 13).** Duplicate `SSTidalCorridor` (shared layout via *Add New Map with Layout*). The player arrives at (9,10), a `MAP_SCRIPT_ON_FRAME_TABLE` plays `MUS_SAILING`, a text box ('Hope you enjoy the voyage'), 4 seconds of walking time, then `warp` to the destination quay. A `VAR_FERRY_DEST` (PROPOSED) selects Beaconmouth or Vesperhaven. Two objects: a sailor (16,7) wandering up and down, a passenger (9,2) looking down. The doors at (4,9),(7,9),(10,9),(13,9) to cabins stay locked decorations.
3. **v3 extras.** `Ferry_Galley` (SS Aqua 2's dining room, 20 x 9: the long table with 6 chairs, a tea urn) reached by the right-hand door of the corridor, **tea for a Heart Scale joke**; `Ferry_CaptainsCabin` (`SSAquaCaptain.png`, 11 x 11: desk with a book, a stool, a wall shelf, a bed, a stair-like step, a red mat at (3,9)): the **Ferry Captain**, who tells a gym 9 hint ('the lighthouse keeper drains the tower by hand, floor by floor') if the player has not heard the pilot. Both extras are 2 objects each.

### 6.6 Maritime Museum 1F and 2F

Vanilla `LilycoveMuseum` layouts (1F 21 x 14, 2F 22 x 13, tileset `LilycoveMuseum`). **1F** vanilla: mats (9,13),(10,13), stairs up (16,1), ten objects, many `bg_event` display cases. Veldris keeps the layout, reads the cases as ship models and sea charts, and re-uses these objects:

- **Museum guide** (the gentleman at (16,2), `FACE_DOWN`): explains **Aldermere**, 'a town the sea took in a night: two thousand years and a bad tide'.
- Visitors at (5,12) (beauty), (13,7) (school kid), (13,10) (artist wandering), (2,8),(3,8) (a boy and a woman looking up), (11,3) (woman wandering), (19,3) (artist), (2,2) (fat man wandering), (6,2) (psychic wandering). Keep 8 to 10; that is under 15 and ambient.
- **2F** (22 x 13): the **1F stairs (16,1) lead to 2F warp 0 at (13,1)**, and that tile leads back down. Objects: the **Curator** (gentleman at (10,8) `FACE_UP`) with a corner display case at (19,10): the curator gives a **Shell Bell** for a **Relic Statue** (post-game, Aldermere), see the card; other visitors (19,10) girl wandering, (7,3) expert, (14,6) rich boy.
- **Warps:** 1F mats (9,13),(10,13) to `Kingsquay` warp 3 (door (7,20)).

### 6.7 Pokémon Trainer Fan Club (vanilla, 12 x 14)

Mats (5,13),(6,13). Objects, vanilla positions: lass (3,11), man (8,10), pokefan (6,11), little girl (5,8), ninja boy (7,11), boy (1,9), woman (3,10), expert (10,10), **chair** (boy at (11,5) `FACE_DOWN`). The Chair reacts to the player's badge count with different lines ('Seven badges?', 'Eight?') and **gives a Soothe Bell at 9 badges** (`FLAG_RECEIVED_SOOTHE_BELL`). Warps: mats to `Kingsquay` warp 4 (door (14,20)). Fans may hold a one-line topic each; none is a trainer.

### 6.8 Move Reminder's House (G4-B)

**Purpose.** Relearn moves for Heart Scales (the card asks whether the author wants this system, open question 4; build it last). Plan G4-B (10 x 8), the **Move Reminder** at (4,4) `FACE_DOWN` in front of the table, a stove nook with a kettle. Warps: mats (3,7),(4,7) to `Kingsquay` warp 5 (door (4,26)).

### 6.9 Tallow & Crane Solicitors (Little Office, custom 14 x 10)

**Purpose.** The Scheme 9 setup: the player sees the pile of invoices, learns the total is 'nearly finalised', and sees **Mr Tallow** leave on the Beaconmouth ferry. Plan, **PROPOSED**, on Little Office tiles (glass partition, desks, filing shelves, the stairwell tile unused):

```
     x0 1 2 3 4 5 6 7 8 9 10 11 12 13
y0   #  # # # # # # # # # #  #  #  #
y1   Q  Q . W . . L . . W .  .  Q  Q      Q = filing shelves (bg_event 'files'), L = locked inner door (6,1)
y2   Q  Q . . . . . . . . .  .  Q  Q
y3   .  . . . . . . N . . .  .  .  .      N = second clerk (7,3) facing down, behind the counter
y4   .  . k k k k k k k k k  k  .  .      k = reception counter x 2..11 at y 4
y5   .  . . . . . . . . . .  .  .  .
y6   .  . . . P . . . . . i  i  .  .      i = invoice pile table (10,6),(11,6): bg_event, sets FLAG_KINGSQUAY_SAW_INVOICES
y7   .  . . . . . . . . . i  i  p  .      p = Pip (12,7) facing left, counting invoices aloud
y8   .  . . . . . . . . . .  .  .  .
y9   .  . . . . . D D . . .  .  .  .
```
- **Mr Tallow** (PROPOSED) stands at (6,2) `FACE_DOWN` in front of the locked door until the player has seen the invoice pile; then he is hidden (`FLAG_KINGSQUAY_TALLOW_LEFT` is set when the player first reaches Beaconmouth) and the inner door stays locked ('closed for conclusions'). Courteous, never smiles: 'Our clients prefer the matter be concluded in person.'
- **Second clerk** (7,3): 'a number with a lot of commas'. **Pip** (12,7): counts out loud, mentions that one invoice is missing (he later loses it on Driftsands beach, see [driftsands.md](driftsands.md)).
- **Warps:** mats (6,9),(7,9) to `Kingsquay` warp 7 (door (50,15)). Fallback on Devon Corp 1F (19 x 9): same cast, put the pile on the right-hand desk.

### 6.10 The shared Goldsworth House layout (13 x 11, defined here once, used by every Goldsworth house)

**PROPOSED** and the author may replace it with a better one ([../../map-plan.md](../../map-plan.md) says one shared layout, painted once). If another detail file in this folder defines a different one, the author picks. One layout, many maps ('Add New Map with Layout'), NPC-only, no trainer ids. A richer Gen 4 room than the ordinary houses:

```
     x0 1 2 3 4 5 6 7 8 9 10 11 12
y0   #  # # # # # # # # # #  #  #
y1   B  B B . W . . . W . T  T  P      B = tall bookshelf run, W windows, T = TV and cabinet, P = plant
y2   B  B B . . . . . . . T  T  .
y3   .  . . . . . N . . . .  .  .      N = Butler (6,3), facing down
y4   .  . . . R R R R R R .  .  .
y5   .  c . . R R f f R R .  c  .      f = low table with THE VASE: bg_event on (6,5),(7,5) (Chad's 'worth more than your whole town')
y6   .  . . . R R R R R R .  .  .
y7   .  P . . . . . . . . .  P  .
y8   .  . . . . . . . . . .  .  .
y9   .  . . . . . . . . . .  .  .
y10  .  . . . . D D . . . .  .  .
```
Mats (5,10),(6,10). **Objects (3):** Butler (6,3), Cousin A at (3,6) `FACE_RIGHT`, Cousin B at (10,6) `FACE_LEFT`. The cousins are chosen per city; the text comes from `dialogue/goldsworth.inc` (`Goldsworth_Text_<Name>Before` and `After`). Outside, a sign using `Goldsworth_Text_HouseSign`. Make the rug a rich colour (gold on cream) so the room reads as the family's.

**Kingsquay's house:** Cousin A = **Chad** (boaster, now with a yacht), Cousin B = **Winston** (phone talker, tries to buy the harbour), plus the Butler. Before the Beaconmouth scheme they boast. After `FLAG_BEACONMOUTH_SCHEME9_DONE` Chad says the yacht was lost on a bet (`Goldsworth_Text_ChadAfter`) and Winston that the harbour 'was not for sale' (`WinstonAfter`); the yacht berth sign reads FOR SALE. (Winston reappears at Aldermere in the post-game as a gag, see [aldermere.md](aldermere.md); that is deliberate continuity: he lost the harbour deal and went looking for a drowned town.) Goldsworths may swear mildly; nobody else may.

### 6.11 Harbour Master's Hut, Dockhand's House, Retired Pilot's House

- **Harbour Master's Hut (G4-A 11 x 8).** The **Harbour Master** at (8,4) `FACE_LEFT` ('R24 is the road with the sand in its shoes'); a ferry rules `bg_event` at (7,2); a timetable at (8,2). Warps: mats (2,7),(3,7) to `Kingsquay` warp 8.
- **Dockhand's House (G4-A).** A mother at (5,6) `FACE_UP`, a son at (9,5) wandering, a Wingull on a perch at (2,4) (ambient Pokémon). The dockhand outside (30,32) says the crates are 'permits'. Warps: mats (2,7),(3,7) to `Kingsquay` warp 9.
- **Retired Pilot's House (G4-C 12 x 9).** The **pilot** at (8,5) `FACE_LEFT`: the gym 9 hint ('the lighthouse keeper drains the tower by hand, floor by floor'). Model ship on the table (bg_event (6,5)). Warps: mats (5,8),(6,8) to `Kingsquay` warp 10.

### 6.12 Quayside Tea Rooms (optional, PROPOSED name)

An eatery for the harbour, purely to use **Brick Cafe Interior Secondary** (README decision 3). Costs a triple-layer conversion, so it is the first thing to cut. Plan, 13 x 9 (counter left, tables right, checker floor, windows with lamps, as the tileset's example shows):

```
     x0 1 2 3 4 5 6 7 8 9 10 11 12
y0   #  # # # # # # # # # #  #  #
y1   Z  Z Z . W . . W . . W  .  #      Z = tea counter and urns (x0..2, y1..2), W = lit windows
y2   Z  Z Z . . . . . . . .  .  #
y3   .  k k k . . . . . . .  .  .      k = counter front (x1..3,y3), clerk N at (2,2)
y4   .  . . . . . . . . . .  .  .
y5   .  . . . . t t . . t t  .  .      t = cafe tables (2 wide) with cups
y6   .  . . . . c c . . c c  .  .
y7   .  . . . . . . . . . .  .  .
y8   .  . . . . . D D . . .  .  .
```
Objects: the **barista** (2,2) `FACE_DOWN` (a tea for free once, flavour), two customers (5,5) and (10,6), a ferry hand on his break (11,3), reading the timetable. Warps: mats (6,8),(7,8) to `Kingsquay` warp 11 (door (40,16)).

---

## 7. Door and warp table

`Kingsquay` outdoor warp events (indexes in order):

| # | Tile | Destination | Dest warp |
|---|---|---|---|
| 0 | (56,20) | `Kingsquay_PokemonCenter_1F` | 0 |
| 1 | (39,9) | `Kingsquay_Emporium_1F` | 0 |
| 2 | (30,28) | `Kingsquay_FerryTerminal` | 0 |
| 3 | (7,20) | `Kingsquay_MaritimeMuseum_1F` | 0 |
| 4 | (14,20) | `Kingsquay_FanClub` | 0 |
| 5 | (4,26) | `Kingsquay_MoveRemindersHouse` | 0 |
| 6 | (15,8) | `Kingsquay_GoldsworthHouse` | 0 |
| 7 | (50,15) | `Kingsquay_TallowAndCrane` | 0 |
| 8 | (22,27) | `Kingsquay_HarbourMastersHut` | 0 |
| 9 | (37,27) | `Kingsquay_DockhandsHouse` | 0 |
| 10 | (12,26) | `Kingsquay_PilotsHouse` | 0 |
| 11 | (40,16) | `Kingsquay_TeaRooms` (optional) | 0 |

(Porymap assigns warp indexes by order, so follow its numbering if it differs from this table. The numbers here are the ones section 6 uses.)

Interior warps (exit mats back to the outdoor warp number above):

| Map | Mats / stairs | Destination | Dest warp |
|---|---|---|---|
| `Kingsquay_PokemonCenter_1F` | (6,8),(7,8) | `Kingsquay` | 0 |
| `Kingsquay_Emporium_1F` | (8,7),(9,7) | `Kingsquay` | 1 |
| `Kingsquay_Emporium_1F` / `_2F` | stairs (16,1) | `_2F` warp 0 / `_1F` warp 2 | |
| `Kingsquay_Emporium_2F` / `_3F` | (13,1) | `_3F` warp 0 / `_2F` warp 1 | |
| `Kingsquay_Emporium_3F` / `_Rooftop` | (16,1) / (13,3) | `_Rooftop` warp 0 / `_3F` warp 1 | |
| `Kingsquay_FerryTerminal` | (11,14),(12,14) | `Kingsquay` | 2 |
| `Kingsquay_MaritimeMuseum_1F` | (9,13),(10,13) | `Kingsquay` | 3 |
| `Kingsquay_MaritimeMuseum_1F` / `_2F` | (16,1) / (13,1) | `_2F` warp 0 / `_1F` warp 2 | |
| `Kingsquay_FanClub` | (5,13),(6,13) | `Kingsquay` | 4 |
| `Kingsquay_MoveRemindersHouse` | (3,7),(4,7) | `Kingsquay` | 5 |
| `Kingsquay_GoldsworthHouse` | (5,10),(6,10) | `Kingsquay` | 6 |
| `Kingsquay_TallowAndCrane` | (6,9),(7,9) | `Kingsquay` | 7 |
| `Kingsquay_HarbourMastersHut` | (2,7),(3,7) | `Kingsquay` | 8 |
| `Kingsquay_DockhandsHouse` | (2,7),(3,7) | `Kingsquay` | 9 |
| `Kingsquay_PilotsHouse` | (5,8),(6,8) | `Kingsquay` | 10 |
| `Kingsquay_TeaRooms` | (6,8),(7,8) | `Kingsquay` | 11 |
| Ferry (script warps) | to `Ferry_Deck` (9,10) | then to Beaconmouth quay (21,30) or Vesperhaven east pontoon | scripts |

---

## 8. NPCs and objects outdoors (11)

| Object | Tile | Move | Topic |
|---|---|---|---|
| Dockhand with crates | (30,32) | `FACE_DOWN` | Crates are 'permits'. Scheme 9 seed |
| Tourist | (28,17) | `FACE_RIGHT` | Photographs the fountain |
| Kid | (22,20) | `WANDER_AROUND` | Chases a Wingull that took his hat |
| Sailor | (45,28) | `WANDER_LEFT_AND_RIGHT` | Quay patrol |
| Old woman on the bench | (28,19) | `FACE_UP` | Remembers when the villa was a hospital (gag) |
| Fisherman | (15,33) | `FACE_DOWN` | West pier; says Super Rod spots are the deep blue by the crane |
| Parasol lady | (24,20) | `WANDER_UP_AND_DOWN` | Gossip: the family at the villa 'never come out' |
| Crane worker | (55,29) | `FACE_LEFT` | Container yard |
| Wingull on lamp post | (33,16) | `LOOK_AROUND` | Ambient Pokémon |
| Wingull on pier | (16,31) | `LOOK_AROUND` | Ambient Pokémon |
| Azumarill by the fountain | (31,18) | `WANDER_AROUND` | Ambient Pokémon |

`bg_event`s: town sign (21,2), villa sign (13,10), solicitors' brass plate (50,15) (door sign), notice board (46,15) (a poster listing the ferry times), yacht sign (47,32) (FOR SALE after Scheme 9), pier sign (31,30). **Fishing:** the harbour water, with R23's tables; the pier (16,31) and quay edge are the spots.

---

## 9. Items and hidden items (positions)

| Item | Where | Gate |
|---|---|---|
| TM Hyper Beam, TM Rock Tomb | Emporium 3F TM counter | None (prices PROPOSED; check the TM ledger first) |
| Dive Ball, Net Ball | Emporium 2F counter | None |
| Max Revive | Emporium rooftop, (16,10), visible | None |
| Soothe Bell | Fan Club chair | 9 badges |
| Shell Bell | Maritime Museum 2F, case at (19,10) | Post-game, bring a Relic Statue (Aldermere) |
| Heart Scale (hidden) | Behind a crate on the east pier, (47,34) | None |
| Pearl (hidden) | The fountain, (31,17) (hidden-item bg_event on the basin tile) | None |

---

## 10. Scripts and events the build needs

- `Kingsquay_MapScripts`: `ON_TRANSITION` sets `FLAG_VISITED_KINGSQUAY` and the heal location; hides Mr Tallow (`FLAG_KINGSQUAY_TALLOW_LEFT`), switches the yacht sign on `FLAG_BEACONMOUTH_SCHEME9_DONE`; on game clear enables the Vesperhaven ferry.
- `Kingsquay_TallowAndCrane`: invoice pile `bg_event` sets `FLAG_KINGSQUAY_SAW_INVOICES`; Tallow and Pip dialogue switched on it and on `FLAG_KINGSQUAY_TALLOW_LEFT`.
- `Kingsquay_FerryTerminal`: ticket script with a multichoice (Beaconmouth, Vesperhaven, Cancel), sets `VAR_FERRY_DEST`, warps to `Ferry_Deck` (or direct).
- `Ferry_Deck`: on-frame script plays the sail and warps (v2).
- Goldsworth House: Before/After switches on `FLAG_BEACONMOUTH_SCHEME9_DONE`.
- Fan Club chair: badge count branch (`GetBadgeCount()`, CLAUDE.md badge table), `FLAG_RECEIVED_SOOTHE_BELL`.
- No trainer battles in the city; a post-game ferry-hand rematch is a *possible* addition (card: 'one trainer (a ferry hand) gives rematch fights'): the ferry hand at the terminal, a Sailor class trainer reusing a vanilla Hoenn id, 3 Pokémon at levels 66 to 68 (PROPOSED), `cleartrainerflag` per fight. Only if the author confirms.

**Flags (not claimed):** `FLAG_VISITED_KINGSQUAY`, `FLAG_KINGSQUAY_SAW_INVOICES`, `FLAG_KINGSQUAY_TALLOW_LEFT`, `FLAG_KINGSQUAY_FERRY_BEACONMOUTH`, `FLAG_KINGSQUAY_FERRY_VESPERHAVEN`, `FLAG_RECEIVED_SOOTHE_BELL`, `FLAG_HIDDEN_ITEM_KINGSQUAY_HEART_SCALE`, `_PEARL`, `VAR_KINGSQUAY_GOLDSWORTH` (or reuse `FLAG_BEACONMOUTH_SCHEME9_DONE`), `FLAG_ITEM_KINGSQUAY_MAX_REVIVE`; new (PROPOSED): `VAR_FERRY_DEST`, `FLAG_RECEIVED_SHELL_BELL_KINGSQUAY`.

---

## 11. Build checklist (in order)

1. Read flags.md and engine-edits.md; decide the LeoB `lilycove` import (CREDITS row, door anims, engine-edits entry).
2. Duplicate `LilycoveCity`, Change Dimensions to 64 x 40, delete the Aqua Hideout entrance and the right-hand cliffs, set `MAPSEC_KINGSQUAY`, delete duplicated heal locations before the first save.
3. Re-place the museum block as the villa (10,1), the department store at (35,3); paint the square, fountain, hill street, fence and gateway; bay and slipway.
4. Paint the quay and three piers; the yacht, cranes, containers (decoration).
5. Place the ten building exteriors (section 6.1). Build the Goldsworth layout (13 x 11) **last** (it is shared), but the door can exist as a locked sign first.
6. Interiors in this order: Center (shared), Emporium 1F to Rooftop (duplicate vanilla), Museum 1F/2F (duplicate vanilla), Fan Club (duplicate vanilla), Terminal (duplicate `LAYOUT_HARBOR`), G4 houses, Tallow & Crane (Devon fallback first, Little Office later), optional Tea Rooms, ferry set.
7. Add warps and connections (north R23, east R24).
8. Close and reload Porymap after Claude edits events.
9. Claude wires scripts and dialogue; dialogue_check on each `scripts.inc`; `make -j4`.
10. Update design docs and credits; check no ROM or save is staged; commit and push.

---

## 12. Open questions

1. **Ferry.** It lets a returning player skip R24 and R25. I gate it on having walked to Beaconmouth once (card). v1 (no ferry maps) is cheapest; do you want the deck, galley and captain's cabin at all?
2. **Winston twice.** Kingsquay's house and Aldermere's kiosk both use Winston. I made it a deliberate gag; otherwise Aldermere's kiosk takes Trip.
3. **Shared Goldsworth layout: two definitions exist.** I defined it here (13 x 11, mats (5,10),(6,10); Hemlock Reach and Primrose Vale adopted it). [briarwick.md](briarwick.md) section 3.5 defines its own **13 x 10** layout (door mat (6,9)), which Hoarfell adopted. Only one can be painted and shared: the author picks, and the other files' coordinates shift by a row. **Cousin allocation also collides** across files (Winston appears at Kingsquay, Aldermere, Hoarfell and Primrose Vale; Prescott and Kip at Beaconmouth and elsewhere): the author or the index writer must assign each cousin to one city.
4. **Little Office and Brick Cafe are triple-layer or ambiguous** and need a Porytiles conversion like Gen 4 Interior got (design/interiors.md). Are two more conversions worth it for one office and an optional tea room? Fallback for the office is vanilla Devon Corp 1F; the tea room can simply be dropped.
5. **TMs in shops.** The card sells Hyper Beam and Rock Tomb at the Emporium; keep, or make them found items?
6. **Move Reminder.** Keep (a small script system) or leave out?
7. **Fountain tile.** The Lilycove secondary may have no fountain; a basin built from quay-edge tiles is my fallback.
