# WAYMEET, detailed design (town, place 11, crossroads and rail stop, no gym)

Status: **PROPOSED.** Written 2026-10-01 for the author to build from. Card this expands: [../towns/waymeet.md](../towns/waymeet.md). Rules: [../interiors/README.md](../interiors/README.md), catalogue [../interiors/catalogue.md](../interiors/catalogue.md), house style [../../interiors.md](../../interiors.md). Roads: [routes-centre-detail.md](routes-centre-detail.md) (R12, R19), [../routes-east.md](../routes-east.md) (R13), [../routes-south.md](../routes-south.md) (R22). New minor names are PROPOSED. Coordinates are `x, y` tiles from the top-left tile (0,0), good to about one tile.

## 0. What I measured, and changes against the card

- **The two station renders are different sizes than the card says.** `trainstation2zi.png` is 476 x 197 px, no grid, and holds **two side-by-side panels of the same small hall** (one with the track empty, one with a white-and-blue train): each panel is about **13 x 12 tiles** (211 px wide). `stacjajs7.png` is 412 x 350 px with black margins: the hall itself is about **23 x 20 tiles** (platform, tracks, waiting hall). The card's '29 x 12' is the whole picture, and '25 x 21' is the picture including its black border. Use `stacjajs7.png` for the Station map and `trainstation2zi.png` for the **look of the train** (the empty-track panel is the platform without a train).
- **All doors face south** (the card has the Station door 'facing west', the Cafe 'facing east', Lost Property 'facing west'). Here every building opens south onto the square or a lane.
- **`Small town with lab Secondary` is not a station set.** I looked at its `example.png`: it is a farm and lab exterior with crop plots, a greenhouse and a dock, so the catalogue line 'train-station tiles' is wrong. It is **not used here**; it could dress R12's Lowbarrow Farm (see [routes-centre-detail.md](routes-centre-detail.md)) if flattened, but it is triple-layer.
- **Tilesets.** Outdoor: ORAS General (in tree) + **LeoB ORAS `mauville` secondary** (dual-layer, 510 metatiles; same set as Lingmoor, the vanilla Mauville and Verdanturf set). Folder `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS/tilesets/secondary/mauville/`. Needs a CREDITS row (extend the leob0505 row, naming `mauville`; Lingmoor uses it too, so one row covers both). Station interior: `gTileset_Building` + **`gTileset_Facility`** (the vanilla Cable Car Station's set, grey platform floors, glass, railings; no import). Cafe, Dock Office, Lost Property and houses: Gen 4 Interior.
- **Size** `(44+15)*(34+14) = 2832`, under 10240. Hand-laid **44 x 34** (vanilla Mauville, 40 x 20, is too small). Section `MAPSEC_WAYMEET` (new, PROPOSED). Fly destination, `HEAL_LOCATION_WAYMEET` PROPOSED, landing **(16,10)** outside the Center door.
- Credit **Project Palladium** if the Station render is traced (`stacjajs7.png`, `trainstation2zi.png`).

## 1. Description

**From R12 (the north).** The farm lane ends at a **plain gate** and drops onto a **cobbled street** that runs straight south to a **paved square** with a compass rose in the middle. A Pokémon Center roof (red) is on the left, a Mart (blue) on the right, a long grey **station roof** behind them to the east, and beyond all of it a **ribbon of brown water**. Everything on the screen points somewhere: a four-arrow signpost, a clock, rails. Sound: a distant clunk of nothing arriving. **Time of day:** mid-afternoon, brass light on the canal. **Music:** `MUS_SLATEPORT` (a harbour town tune; Waymeet is half port) outdoors, `MUS_POKE_CENTER` and `MUS_POKE_MART` as vanilla, `MUS_CABLE_CAR` (the vanilla cable car's tune) in the Station, `MUS_LITTLEROOT` in houses.

**From R13 (the east).** The road comes in beside a **railway line** (two tracks leading to the Station, buffers at the end), past a **fenced siding** with something large under a gold-trimmed tarpaulin, and into the square from the east.

**From R19 and R22 (the water roads).** The player arrives at a **pier**: a plain plank pier in the west, a second one in the south, each with a bollard, a lantern and a harbourmaster's flag.

**Mood and colour.** Weather-beaten brick-grey and blue, brass lamps, a handsome, tired, important-looking town with nothing arriving. **The memorable view:** standing at the **compass rose** (21,17), the signpost's arrows point north, east, west and south while the **Station's long roof** says 'WAYMEET' above empty tracks, and the siding's tarpaulin glints gold at the edge of the screen.

## 2. Street layout, in words

North at the top. `~` water, `t` trees, `:` ground, `,` the square, `.` roads and lanes, `=` rails, `p` piers, `g` the siding, `i` signpost, `k` clock, `+` compass rose. Buildings: `P` Pokémon Center, `M` Mart, `S` Station, `F` Cafe, `O` Dock Office, `L` Lost Property, `A` `B` houses; the digit in a building is its door.

```
      x: 00000000001111111111222222222233333333334444
         01234567890123456789012345678901234567890123
 y 0  |ttttt::::::::::::::::....:::::::::::::::::::|
 y 1  |ttttt::::::::::::::::....:::::::::::::::::::|
 y 2  |ttttt::::::::::::::::....:::::::::::::::::::|
 y 3  |ttttt::::::::::::::::....:::::::::::::::::::|
 y 4  |ttttt::::::::::::::::....:::::::::::::::::::|
 y 5  |ttttt::::::::::::::::....:::::::::::::::::::|
 y 6  |ttttt:::::::::PPPPP::....:MMMM::::::::::::::|
 y 7  |ttttt:::::::::PPPPP::....:MMMM::::::::::::::|
 y 8  |~~~~~:::::::::PPPPP::....:MMMM:SSSSSSSSS::::|
 y 9  |~~~~~:::::::::PP1PP::....:M2MM:SSSSSSSSS::::|
 y10  |~~~~~::::::::::::::::....::::::SSSSSSSSS::::|
 y11  |~~~~~::::::::::,,,,,,,,,,,,,,::SSSSSSSSS::::|
 y12  |~~~~~::::::::::,,,,,,k,,,,,,,::SSSSSSSSS::::|
 y13  |~~~~~::::::::::,,,,,,,,,,,,,,::SSSS4SSSS::::|
 y14  |~~~~~::::::::::,,,,,,,,,,,,,,:::::::::::::::|
 y15  |~~~~~:FFFFF::::,,,,,,i,,,,,,,............:::|
 y16  |~~~~~:FFFFF::::,,,,,,,,,,,,,,===============|
 y17  |~~~~~:FFFFF::::,,,,,,+,,,,,,,===============|
 y18  |~~~~~:FF3FF::::,,,,,,,,,,,,,,:::::::::::::::|
 y19  |~ppppp:::::::::,,,,,,,,,,,,,,::ggggggg::::::|
 y20  |~ppppp:::::::::,,,,,,,,,,,,,,::ggggggg::::::|
 y21  |~~~~~::::::::::,,,,,,,,,,,,,,:::::::::::::::|
 y22  |~~~~~::::::::::,,,,,,,,,,,,,,:..............|
 y23  |~~~~~::::::::::,,,,,,,,,,,,,,:..............|
 y24  |~~~~~:::::::::::::::::::::::::..............|
 y25  |~~~~~::::::::::OOOOO::::LLLLL:..............|
 y26  |~~~~~::::::::::OOOOO::::LLLLL::::AAAA:BBBB::|
 y27  |~~~~~::::::::::OOOOO::::LLLLL::::AAAA:BBBB::|
 y28  |~~~~~::::::::::OO5OO::::LL6LL::::AAAA:BBBB::|
 y29  |~~~~~:::::::::::::::pppp:::::::::A7AA:B8BB::|
 y30  |~~~~~~~~~~~~~~~~~~~~pppp~~~~~~~~~~~~~~~~~~~~|
 y31  |~~~~~~~~~~~~~~~~~~~~pppp~~~~~~~~~~~~~~~~~~~~|
 y32  |~~~~~~~~~~~~~~~~~~~~pppp~~~~~~~~~~~~~~~~~~~~|
 y33  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
```

Numbered walk:

1. **North (R12).** The lane arrives at **(21,0)-(24,0)** (4 wide) and runs south to the square. The gate is a **plain wooden farm gate** left open (a gate object or two post metatiles, no guard).
2. **Pokémon Center** (cols 14-18, rows 6-9, door **(16,9)**) on the west of the lane; **Mart** (cols 26-29, rows 6-9, door **(27,9)**) on the east. Both face south onto the top of the square. **Revive** by a Cut tree at **(19,3)** beside the gate (Revive at (18,3)).
3. **Junction Square** (cols 15-28, rows 11-23). **Compass rose** (21,17). **Signpost** 'FOUR WAYS' at (21,15), **clock** (21,12), benches at (16,14), (26,14). The square is the town: everything is one lane from it.
4. **The Station** (cols 31-39, rows 8-13, door **(35,13)**), a long grey building with a lamp over the door. In front of it a **platform strip** (cols 29-40, row 15) and the **rails** (cols 29-43, rows 16-17) running east to the map edge (they end at buffers just off-screen; the railway beside R12 is scenery that stops at a buffer, see Open question 2).
5. **The siding** (cols 31-37, rows 19-20), fenced, holding the **gold railcar** (an object under a tarpaulin, see section 5). **Rare Candy (hidden)** at (30,20) outside the fence.
6. **R13 road** at **(43,22)-(43,25)** (east edge), a plain road running west to the square along rows 22-25.
7. **Cafe 'The Junction'** (cols 6-10, rows 15-18, door **(8,18)**) on the west lane, with the **west pier** at **cols 1-5, rows 19-20** just south of it. **R19** leaves from the pier's end into the canal.
8. **South of the square.** **Dock Office** (cols 15-19, rows 25-28, door **(17,28)**) and **Lost Property** (cols 24-28, rows 25-28, door **(26,28)**) face south onto the shore lane (row 29). The **south pier** at **cols 20-23, rows 29-32** is between them; **R22** leaves from its end.
9. **South-east.** **House A** (cols 33-36, rows 26-29, door **(34,29)**) and **House B** (cols 38-41, rows 26-29, door **(39,29)**).
10. **The canal** wraps the west (cols 0-4, rows 8-33) and the south (rows 30-33). **Rock Smash rock** at **(5,12)** on the west bank hides a Heart Scale; a **rock islet** at **(26,31)** holds a Pearl (Surf); a **Max Repel** on a tile off the west pier at **(2,22)** (Surf).

**Palette and tile notes.** ORAS Mauville secondary gives brick, lamp posts, fences, the paved square pattern. Water: the General water tile with the canal edge from the same set; piers are the Slateport/Lilycove wooden pier metatiles in the vanilla General set. Compass rose: the Mauville set has a decorative floor circle (paint as a 2 x 2 or 3 x 3 patch); if not, a plain round bed of flowers. **Draw:** a 3-tile-long tarpaulin shape for the railcar (new object art or the truck object, see section 5), a gold trim on the Station sign.

## 3. Doors and warps (outdoor map `Waymeet`, 44 x 34)

| # | Tile | Destination (arrival) | Notes |
|---|---|---|---|
| 0 | (16,9) | `Waymeet_PokemonCenter_1F` (mat 6,8) | Fly lands (16,10) |
| 1 | (27,9) | `Waymeet_Mart` (mat 3,7) | |
| 2 | (35,13) | `Waymeet_Station` (mats 8,19 and 9,19) | |
| 3 | (8,18) | `Waymeet_Cafe` (mat 5,8) | |
| 4 | (17,28) | `Waymeet_DockOffice` (mat 2,7) | |
| 5 | (26,28) | `Waymeet_LostProperty` (mat 2,7) | |
| 6 | (34,29) | `Waymeet_HouseA` (mat 2,7) | |
| 7 | (39,29) | `Waymeet_HouseB` (mat 2,7) | |

**Connections.**

| Edge | Neighbour | Offset | Lines up |
|---|---|---|---|
| North | `VeldrisRoute12` (24 x 40) south edge | +10 | R12's gate opening (cols 11-14) meets the lane (cols 21-24) |
| East | `VeldrisRoute13` (64 x 23) west edge | +7 | R13's road rows 15-18 meet Waymeet rows 22-25 |
| West | `VeldrisRoute19` (80 x 40) east edge | +3 | R19's open water rows 14-20 meet Waymeet rows 17-23 (Surf) |
| South | `VeldrisRoute22` (40 x 40) north edge | set when R22 is built | the pier (cols 20-23) meets R22's north channel |

Check offsets in Porymap when the roads exist. R19 and R22 need **Surf** (badge 5): the player steps from the pier end onto water.

## 4. Interiors

Maps: `Waymeet_PokemonCenter_1F/_2F`, `_Mart`, `_Station`, `_Cafe`, `_DockOffice`, `_LostProperty`, `_HouseA`, `_HouseB`: **10 maps**.

### 4.1 Pokémon Center and Mart (vanilla, unchanged)

`LAYOUT_POKEMON_CENTER_1F/_2F`, `LAYOUT_MART`; vanilla tiles as in the other towns (nurse (7,2), mats (6,8),(7,8), stairs (1,6); Mart clerk (1,3), mats (3,7),(4,7)). Center NPCs (3): a **passenger with a suitcase** (4,4), a **railwayman on his tea** (10,6), a **child counting arrows** (3,7). Mart stock per the card: Great Ball, Ultra Ball, Super Potion, Hyper Potion, Full Heal, Revive, Repel, Super Repel.

### 4.2 The Station (23 x 20, `gTileset_Facility`)

Trace Palladium `stacjajs7.png` (platform and tracks above, a waiting hall below). **Recommended first pass: leave the track bed empty.** The line is 'between timetables', so an empty platform is funnier and needs no art. **Optional later:** the white-and-blue train from `trainstation2zi.png` (right panel) redrawn as about **9 x 3 tiles** of new metatile art across the track bed (cols 7-15, rows 6-8), a Palladium credit.

```
      x: 00000000001111111111222
         01234567890123456789012
 y 0  |#######################|
 y 1  |###########s###########|   timetable sign s (11,1)
 y 2  |#.....................#|
 y 3  |#.....................#|
 y 4  |#.....................#|   far platform (scenery)
 y 5  |#~~~~~~~~~~~~~~~~~~~~~#|   track bed (impassable), rows 5-8; the train would be cols 7-15, rows 6-8
 y 6  |#~~~~~~~~~~~~~~~~~~~~~#|
 y 7  |#~~~~~~~~~~~~~~~~~~~~~#|
 y 8  |#~~~~~~~~~~~~~~~~~~~~~#|
 y 9  |#....W..........e.....#|   near platform: waiting passenger W (5,9), bench with hidden Escape Rope e (16,9)
 y10  |#wwwwwwwwg.gwwwwwwwwww#|   glass partition w with the ticket gate at (10,10), pillars g (9,10) (11,10)
 y11  |#...vbbb....bbbv......#|   vending v (4,11) (15,11), sofas b (5..7,11) (12..14,11)
 y12  |#b........S.......T.C.#|   stationmaster S (10,12), ticket machine T (18,12), clerk C (20,12)
 y13  |#b.t...t......t.......#|   tables t (3,13) (7,13) (14,13), left bench b (1,12) (1,13)
 y14  |#.................#####|
 y15  |#.................#####|
 y16  |#.................#####|
 y17  |#p...............p#####|   plants p (1,17) (17,17)
 y18  |#.................#####|
 y19  |########DD#############|   mat D (8,19) (9,19)
```

Legend: `#` wall, `.` floor, `~` track bed (impassable; the train goes here), `w` glass partition, `g` gate pillar, `v` vending machine, `b` sofa or bench, `t` low table, `T` ticket machine, `p` plant, `s` timetable sign, `D` mat. The render's orange wooden hall floor is the Facility set's tile in a warm palette (edit palette slot) or the Gen 4 wood floor if the author prefers to repaint the hall in Gen 4 Interior (then the platform needs the Facility floor). Check in Porymap which reads better.

**NPCs (5):** **stationmaster** (10,12) facing down (permanently apologetic, 'the line is between timetables'); **ticket clerk** (20,12) beside the machine, facing left (tickets for nowhere; sells a platform ticket as a joke, **no real item**); **waiting passenger** (5,9) on the platform facing right (has waited since the old timetable); two ambient hall NPCs: a **child with a toy** (13,15) wandering and a **sleeping porter** on the left bench (1,13) facing down. **Signs:** timetable (11,1) ('EVERY DAY: SOMETHING'), the ticket board (17,11). **Hidden Escape Rope** at the platform bench (16,9). **Warp:** mats **(8,19) and (9,19)**. Objects 5 of 15.

### 4.3 Cafe 'The Junction' (11 x 8, Gen 4 Interior)

Template **N** = `Hollowbrook_NeighboursHouse` (11 x 8, mat (2,7), bookshelf signs (7,2),(8,2), free floor x 1-9, y 3-6). Counter and urn top-left (cols 1-4, row 2), four tables, a window onto the lane. **Cafe host** (3,3) facing right (cheap tea; a **drink** (Fresh Water) for a chat; comments on every direction a traveller takes); two **customers**: a **fisherman** (7,5) facing left and a **hiker** (9,4) facing down (just down from Cragdale, dramatic).

### 4.4 Dock Office (10 x 8, Gen 4 Interior, small N)

**Harbourmaster** (5,3) facing down (explains the piers: west for Gildhaven, south for Ebbsworth, Surf required, and the weir at the end of R22 needs Waterfall); a **chart table** with a model of the canal at (7,5) (sign); a **deckhand** (2,5) looking around; a **tide table** sign at (3,2).

### 4.5 Lost Property Office (11 x 8, Gen 4 Interior, N)

Shelves of umbrellas, hats and one enormous trunk labelled 'UNCLAIMED'. **Clerk** (5,3) facing down (the unclaimed **TM Thief**, 'nobody has claimed it', after a short chat); a **man looking for his hat** (8,5) wandering; the trunk (sign) at (9,3).

### 4.6 Houses A and B (11 x 8, Gen 4 Interior, N)

`Waymeet_HouseA` (a railwayman's family): **railwayman** (8,3) facing up (polishes a brass lamp, 'the timetable is under review'); his **wife** (5,6) facing up. `Waymeet_HouseB` (a retired ferryman): **ferryman** (4,4) facing right (the ferries 'are theoretical'); a **Wingull** (a Pokémon) in a basket (8,5) looking around.

## 5. NPCs outdoors (9 of 15 live objects)

| Role | Tile | Movement | Topic |
|---|---|---|---|
| Signpost reader | (22,16) | face left | reads the sign aloud: 'north is Lingmoor, east is Hemlock Reach' |
| Child | (19,19) | wander | counts the arrows on the sign and gets five |
| Railwayman at the siding | (30,19) | face right | polishes the gold railcar, 'private, not mine' |
| **Gold railcar** | (31,19)-(33,20) | none | a tarpaulin-covered shape; **object art options:** the vanilla `OBJ_EVENT_GFX_TRUCK` (the Littleroot moving truck) redrawn in gold, or three object tiles of the author's art. A sign reads 'PRIVATE. G.' |
| Fisherman | (3,19) | face right, on the west pier | bored, comments on R19's long water |
| Hiker | (23,2) | face down, at the north gate | just down from Cragdale |
| Harbourmaster | (21,28) | face down, by the south pier | Surf is needed for both piers |
| Rail inspector | (36,15) | wander, platform strip | 'the timetable is under review' |
| Pier-sitter | (22,30) | face left, on the south pier | R22 leads to Ebbsworth |

The 'Four Ways' signpost reads three destinations (the fourth, the Station, is not one): reading it twice is the card's joke.

## 6. Items and secrets (positions)

| Item | Where | Gate |
|---|---|---|
| **TM Thief** | Lost Property clerk | a short chat |
| Super Potion (visible) | behind the Cafe (8,14) | none |
| Escape Rope (hidden) | Station platform bench (16,9) | none |
| Rare Candy (hidden) | outside the siding fence (30,20) | none |
| Max Repel | water tile off the west pier (2,22) | Surf |
| Pearl | rock islet (26,31) | Surf |
| Heart Scale | behind the west-bank rock (5,12) | Rock Smash |
| Revive | by the north gate (18,3), behind the Cut tree (19,3) | Cut |

## 7. Build checklist (in order)

1. Import ORAS `mauville` (CREDITS row; also covers Lingmoor). Build `Waymeet` 44 x 34 per section 2 (canal, piers, square, Station exterior, rails, siding), doors per section 3. Save; check `event_scripts.s` once and `heal_locations.json`.
2. Add `MAPSEC_WAYMEET` and the fly row.
3. Shared Center and Mart; then the Station (empty-track version first); Cafe, Dock Office, Lost Property, the two houses.
4. Connections: R12 (north), R13 (east), then the water roads R19 and R22 with Surf-entry tiles at the pier ends.
5. Scripts (TM Thief, drink), dialogue (`python3 design/tools/dialogue_check.py`), `design/` updates, CREDITS, `make -j4`, no ROM staged.

## 8. Open questions

1. **Does the player ever use the train?** I assumed no (dressing only). A working rail link would be a new system. The empty-track Station is the cheapest, and the author can add the train art later.
2. **Rails.** The R12 card puts a railway beside the road. I let it stop at a buffer on R12's south end, so there is no rail continuity into Waymeet. If the author wants one line from Lingmoor country into the Station, R12's east side needs a longer rail strip and the Station gets a second rail entry at the north.
3. **Which of R19 and R22 first?** Unchanged from the card: R19 (to Gildhaven) is the natural first choice, R22 is gated by Waterfall at its weir.
4. **Gold railcar art.** Use the Truck object, redrawn, or a new 3-tile object?
5. **Station look:** Facility set (grey) or repainted in Gen 4 Interior (warm wood like the render)? The render's hall is orange wood.
6. **Palladium Route 42 appears in two cards (R10 and R13).** The east group's R13 card meets Waymeet's east edge; see [routes-centre-detail.md](routes-centre-detail.md) for a mirror plan.
