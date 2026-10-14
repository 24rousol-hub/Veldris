# EBBSWORTH: detailed design (river port, town, no gym)

Status: **PROPOSED** (nothing here is canon until the author approves it). Written 2026-10-01 from: [../interiors/README.md](../interiors/README.md) (decisions), [../interiors/catalogue.md](../interiors/catalogue.md), [../README.md](../README.md), [../../interiors.md](../../interiors.md) (Hollowbrook house style), [../index.md](../index.md), the card [../towns/ebbsworth.md](../towns/ebbsworth.md), and the road cards R22, R23, R28 ([../routes-south.md](../routes-south.md)). Companion detail files: [routes-south-detail.md](routes-south-detail.md) (R22 weir, R23, R28), [kingsquay.md](kingsquay.md), [vesperhaven.md](vesperhaven.md).

**New minor names and details introduced in this file are all PROPOSED:** Harbour Market (the card's 'Fish Market', renamed), East Gate, the G4-A, G4-B and G4-C template names, Lock House as an interior.

This file follows the 'Per settlement' list in the interiors README. It also holds the **three Gen 4 house templates (G4-A, G4-B, G4-C)** that the other south files reuse by name.

Conventions used in every plan below: coordinates are **(x, y) from the top-left tile (0,0) of the map**; ground elevation is 3; a '4-wide' building footprint is written `(x0,y0)-(x1,y1)` inclusive and its door is on the **bottom row**, second tile from the left (`x0+1, y1`), as in the vanilla Slateport, Lilycove and Dewford town maps (checked: Slateport Pokémon Center footprint x18-21, door (19,19); Mart door (13,26); Lilycove houses' door at `x0+1`). Interior exit mats are two tiles wide as in vanilla (both mat tiles warp to the same outside door). Maps stay `layout_version` `emerald`, region `REGION_HOENN`, section `MAPSEC_EBBSWORTH`.

---

## 1. Quick facts

| | |
|---|---|
| Map | `Ebbsworth`, **44 x 36** (card said about 40 x 36; 4 wider so the river sits in the middle: `(44+15)*(36+14) = 2950`, limit 10240) |
| Exterior base | Vanilla `SlateportCity` (40 x 60), cut down, **with LeoB ORAS `secondary/slateport`** (see section 5) |
| Section / fly | `MAPSEC_EBBSWORTH`; fly town (row in `src/data/veldris_fly_towns.h`, `HEAL_LOCATION_EBBSWORTH` outside the Center door at (13,14), write `respawn_map` before `respawn_npc`) |
| Music | `MUS_SLATEPORT` (the vanilla Slateport track, fits the harbour). Interiors: `MUS_POKE_CENTER` / `MUS_POKE_MART` for the shared two, `MUS_SLATEPORT` elsewhere |
| Weather | `WEATHER_SUNNY`, map type `MAP_TYPE_TOWN` |
| Gym / scheme | None. One Scheme 9 **seed** (the barge) |
| Roads | R22 north (water, via the Waterfall weir), R23 south (water through the lock gate; land path through the East Gate), R28 west (post-game sea gate) |
| Objects | Town map about 10 live objects (limit 15). Each interior far below it |

---

## 2. Description

**First glance from R22 (the north quay).** The player has just climbed the last stone weir of R22 and slides down a broad, brown, slow tidal river between two lines of honey-coloured quay wall. Ahead the river is crossed by one low stone bridge, with slate-blue roofs on both banks, white bollards every four tiles, blue market awnings on the left bank, and a stack of crates stencilled in fat black capitals on the right bank. A barge sits tied up under the crates. A pelipper stands on every second bollard and does not move for anyone.

**From the south (R23 water, the lock gate).** The sea ends in a stone sluice with two tall brass wheels. Behind it the harbour basin opens up and the whole town stacks up the river like a staircase of roofs.

**From the east gate (R23 land path).** A small pine-framed gatehouse opens onto the east quay: boatyard sheds and the barge are the first things you see.

**Mood, colour, sound, time of day.** A working port, unhurried and tidy: stone, rope, tar, and tarpaulin. Palette: slate blue and honey stone, brown-green water, white bollards, blue and yellow awnings (the LeoB Slateport recolour supplies all of this), with the crates as the one stark black-on-pale accent. Light is **late afternoon with the tide halfway out** (the stock sunny palette is right; the damp stone strip along the waterline sells the tide). Sound: Wingull cries and the Slateport track; every door gives a creak, nothing louder.

**The one memorable view.** The crown of the bridge, at (22,16): looking south you see both lock wheels, the barge with its crates, and the harbour mouth at the west edge; looking north you see the river running back up to a tiny white thread of cascade that is the weir you just climbed. Put a bench-sized gap in the rail there so the player stops.

---

## 3. Street layout in words (a numbered walk)

The river is a straight tidal channel running north to south at **x 20-25** (6 tiles wide), widening into the harbour basin at **y 27**. West of it is the market bank (x 0-19), east of it the working bank (x 26-43).

1. **North quay (x 17-27, y 0-6).** R22 arrives in the river at the top edge (x 20-25, y 0). Stone quay both sides, a bollard row (white posts every 4 tiles: (18,2), (18,6), (27,2), (27,6)), a signpost 'EBBSWORTH' at (18,4), the **Quay lookout** at (18,3). Trees fill the top corners (x 0-12 and x 31-43, y 0-1).
2. **West lane (y 5-8, x 3-17).** A paved lane under the top row of houses: the **Net Menders' Cottage** and the **Old Captain's House**. Pale cobbles, a yellow awning arch at (3,9) marking the market's north gate.
3. **Harbour Market (x 2-9, y 10-23)** (the card's 'Fish Market'; renamed so no real animal is in the name, PROPOSED). Open-air: three blue-awning stalls, crates and baskets (Slateport's stall block, copied as is: 8 x 14 tiles). Vendor behind the middle stall.
4. **Pokémon Center (12,10)-(15,13), door (13,13).** The Center faces south onto the lane to the bridge: from the door go (13,14), then east along y 16 to the bridge's west ramp at x 17. That is the 'about 4 tiles from the bridge end' of the card.
5. **Mart (12,19)-(15,22), door (13,22).** Six rows south of the Center on the same lane.
6. **The bridge (x 18-27, y 15-17).** A 3-wide stone bridge (deck x 20-25, ramps x 18-19 and 26-27). A sign 'MIND THE TIDE' at (19,14). The **Kid** races along it.
7. **East bank, upper (x 28-43, y 8-17).** **Harbour Master's House** (29,9)-(32,12), door (30,12); the **Warehouse** (34,9)-(40,14) with its big locked door at (36,14) and the **Foreman** at (36,15); crates stacked (31-37, 15-17).
8. **East quay and Boatyard (x 26-39, y 18-26).** A stone quay with the **barge** tied up on the river side (hull painted at (24,19)-(25,23)), **Barge hand** at (27,21), and the **Boatyard** (31,19)-(39,25), door (33,25).
9. **The harbour (x 0-26, y 27-31).** The river opens into the basin. Quay walk along its north edge (y 26) and south edge (y 32).
10. **South quay and the lock gate (y 32-35).** The sluice crosses the channel at **x 20-25, y 33**, two wheels at (19,33) and (26,33), the **Lock House** (27,29)-(30,32), door (28,32), **Maud** at (27,34). South of the gate the sea begins (map edge y 35, connection to R23).
11. **West harbour mouth (x 0-3, y 28-30).** Water leaving the basin to the west edge: R28's sea gate, roped off until the League. **Customs Shed** (1,23)-(4,26), door (2,26) (exterior only), **Customs Officer** at (2,27).
12. **East Gate (39,26)-(43,29), door (41,29).** The pass-through gatehouse to R23's land path. Reached from the east quay lane at y 30.

Surfable water: the river, the basin, the lock chamber. No tall grass. Pines at the top corners and around the East Gate are decoration.

---

## 4. Map plan

Sketch, **1 character = 2 x 2 tiles** (22 x 18 characters for 44 x 36 tiles). The tables give the exact coordinates, the sketch is only for orientation (it was generated from the footprints in section 6.1). Legend: `~` water, `T` trees, `=` quay wall or quay, `N` Net Menders' Cottage, `C` Old Captain's House, `^` market arch, `S` market stalls, `P` Pokémon Center, `M` Mart, `K` Customs Shed, `H` Harbour Master, `W` Warehouse, `c` crates, `b` bridge, `B` Boatyard, `r` barge hull, `L` Lock House, `G` East Gate.

```
x:  0    1    2    3    4 
y0  TTTTTTT..=~~~=.TTTTTTT
y2  .NNNCCC..=~~~=........
y4  .NNNCCC..=~~~=........
y6  .........=~~~=........
y8  .^^......=~~~=HHHWWWW.
y10 .SSSS.PP.=~~~=HHHWWWW.
y12 .SSSS.PP.=~~~=HHHWWWW.
y14 .SSSS....bbbbb.ccccWW.
y16 .SSSS....bbbbb.cccc...
y18 .SSSS.MM.=~~r=.BBBBB..
y20 .SSSS.MM.=~~r=.BBBBB..
y22 KKKSS.MM.=~~r=.BBBBB..
y24 KKK......=~~~=.BBBBB..
y26 ==========~~~=.....GGG
y28 ~~~~~~~~~~~~~LLL...GGG
y30 ~~~~~~~~~~~~~LLL......
y32 ==========~~~=========
y34 ==========~~~=========
```
(The header digits mark every 10 tiles. The lock chamber is the 6-wide water gap at x 20-25, y 32-35, and the sluice gate runs across it at y 33.)

**Connections (Porymap):**

| Edge | Neighbour | Offset | Tiles that matter |
|---|---|---|---|
| North | `R22` (south end) | 0 | Water x 20-25 at y 0. R22's exit pass is built at the same columns |
| South | `R23` (north end) | 0 | Water x 20-25 at y 35 (beyond the lock gate). R23's north end must have water at x 20-25 (see routes-south-detail.md, R23 segment 1) |
| West | `R28` (east end) | 0 | Water x 0-3, y 28-30, post-game (the sea gate). Pre-League, the connection exists but a rope (impassable fence metatile) blocks the mouth at x 1, y 28-30 |
| East | none | | The East Gate is a warp, not a connection |

Hide the R28 connection from the player before the League with the rope metatiles, not by removing the connection, so no map edit is needed at game clear (just `setmetatile` the rope away).

---

## 5. Base, tilesets, palette notes

**Exterior base.** Duplicate `SlateportCity` (40 x 60). It already has: a market block with stalls (x 2-14, y 33-55 in vanilla), stone quays, bollards, a long pier, a shipyard exterior (x 24-32, y 32-38, door (26,38)), the Pokémon Center (x 18-21, y 16-19), Mart (x 12-15, y 23-26), small houses, the yellow awning arches. Use **Change Dimensions** (not the duplicate dialog) to 44 x 36, then redraw:

- **The river.** Slateport has no river. Paint a 6-wide channel x 20-25 from y 0 down to the basin at y 27 with the vanilla water metatile and the quay-wall edge pieces Slateport already uses along its harbour (the stone edge with white bollard tops). Water in the basin is the same.
- **The bridge.** Use the bridge pieces vanilla Route 120 uses over its river (walkable on top, surfable underneath). Check the tile behaviours in Porymap before painting; the bridge must let the player surf south under it.
- **Market, shipyard, Center, Mart, awnings:** copy from Slateport and arrange per the table in section 6. The Slateport 'museum island' is not used.

**Tilesets (recommended).**

| Where | Primary | Secondary | Source and credit |
|---|---|---|---|
| Ebbsworth outdoors | `gTileset_General` (already the LeoB ORAS recolour, imported for Hollowbrook) | **LeoB ORAS `secondary/slateport`** | `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS/tilesets/secondary/slateport` (the repo's `8 - Slateport.png` shows exactly this town in the recolour). **Same metatile ids as vanilla**, so the traced Slateport layout keeps working. **Needs a `CREDITS.md` row (leob0505, same row text as the existing Hollowbrook one) and the door animation `graphics/door_anims/slateport.png` from the same folder.** It replaces the vanilla Slateport tileset files in place, which is an upstream-file edit: log it in `design/engine-edits.md` (CLAUDE.md rule 5). Only do this in the commit that first needs it |
| Shared Center and Mart | `gTileset_Building` | `PokemonCenter`, `Shop` | Vanilla, unchanged (decision 2). Later optional re-skin with **Alternative Pokecenter Secondary** (Rahtak/Ekat), name the folder in the credits row if it is ever used |
| Houses | `gTileset_Building` | `Gen4Interior` (already in the tree) | Hollowbrook's tileset, credited already |
| Boatyard | `gTileset_General` | `gTileset_Facility` | Vanilla (the Sterns Shipyard layout) |
| East Gate | `gTileset_General` | `gTileset_Shop` | Vanilla `Route110_SeasideCyclingRoadEntrance` layout (15 x 6) |

**Palladium images for this town:** none match (Olivine's pier is used by Beaconmouth, see [beaconmouth.md](beaconmouth.md)). The card suggests `Route 32.png` (28 x 94) for the jetty mood; it is **not needed** because the vanilla Slateport pier already supplies the wooden piers and bollards.

**What has to be redrawn by hand:** the river channel and bridge (no vanilla town has one), the lock gate (two wheels and a sluice wall across 6 tiles: build it from a stone wall tile, two 1x2 'tall wheel' decorations drawn from the Slateport harbour lamp-post tiles, and a gate leaf made of the Slateport pier fence tiles), and the barge hull (use the Slateport harbour's moored sailboat tiles stretched to 2 x 5).

---

## 6. Buildings

### 6.0 House templates (used by every south file)

All ordinary homes use the **Gen 4 Interior Secondary** already in the tree (README decision 1). Furniture vocabulary: kitchen counter, stove, fridge, stools, bookshelf, TV with flower table and cushions, rug, plant, bed, window, stairs. The three templates below are **plans in that vocabulary**; they are proposals drawn from the Hollowbrook neighbour's house (11 x 8, real object positions from its `map.json`: woman (5,6), man (8,3), girl (9,5), Skitty (2,4), bookshelf signs (7,2),(8,2), exit warp (2,7)), not a claim about its exact painting, so **check against the real layout in Porymap**. Legend: `#` wall, `.` floor, `D` exit mat (warp), `S` stove and counter, `F` fridge, `K` counter/cupboard, `B` bookshelf, `T` TV, `t` table (flower table where marked `f`), `c` cushion or stool, `R` rug (walkable), `P` plant, `W` window, `b` bed, `w` wardrobe/chest, `C` PC desk.

**G4-A, 'Kitchen and lounge', 11 x 8** (the neighbour's house layout itself: share it with *Add New Map with Layout* for plain family houses):

```
     x0 1 2 3 4 5 6 7 8 9 10
y0   #  # # # # # # # # # #
y1   S  S F . . W . B B T T
y2   K  K F . . . . B B T T
y3   .  . . . . . . . . . .
y4   .  . . . . . . . . . .
y5   .  . . . . . c f c . P
y6   .  . . . . . . . . . .
y7   .  . D . . . . . . . .
```
Exit mat (2,7) as built in Hollowbrook; if two mat tiles are wanted (vanilla style) use (2,7) and (3,7). Kitchen floor is the light tile at x 0-4, lounge floor the green carpet at x 5-10 (as in the Hollowbrook render).

**G4-B, 'One-room cottage', 10 x 8** (new layout, own painting):

```
     x0 1 2 3 4 5 6 7 8 9
y0   #  # # # # # # # # #
y1   b  b . W . . B B S S
y2   b  b . . . . B B K K
y3   .  . . . . . . . . .
y4   .  R R R R . . . . .
y5   .  R R f f R . c . .
y6   .  R R R R . . . . P
y7   .  . . D D . . . . .
```
Warp mats (3,7),(4,7).

**G4-C, 'Study and lounge', 12 x 9** (new layout):

```
     x0 1 2 3 4 5 6 7 8 9 10 11
y0   #  # # # # # # # # # #  #
y1   B  B B . W . . T T . B  B
y2   B  B B . . . . T T . B  B
y3   .  . . . . . . . . . .  .
y4   .  . . R R R R R R . .  .
y5   .  P . R R f f R R . P  .
y6   .  . . R R R R R R . .  .
y7   .  . . . . . . . . . .  .
y8   .  . . . . D D . . . .  .
```
Warp mats (5,8),(6,8).

(Extras such as a rod rack, a chest or a tide chart are `bg_event`s on a wall tile in row 1, so they cost no objects.)

### 6.1 Building table (overview)

| # | Building | Footprint (x0,y0)-(x1,y1) | Door (bottom row) | Interior map(s) | Layout |
|---|---|---|---|---|---|
| 1 | Pokémon Center | (12,10)-(15,13) | (13,13) | `Ebbsworth_PokemonCenter_1F`, `_2F` | `LAYOUT_POKEMON_CENTER_1F`, `_2F` unchanged |
| 2 | Mart | (12,19)-(15,22) | (13,22) | `Ebbsworth_Mart` | `LAYOUT_MART` unchanged |
| 3 | Net Menders' Cottage | (3,2)-(6,5) | (4,5) | `Ebbsworth_NetMendersCottage` | G4-B (10 x 8) |
| 4 | Old Captain's House | (9,2)-(12,5) | (10,5) | `Ebbsworth_OldCaptainsHouse` | G4-C (12 x 9) |
| 5 | Harbour Master's House | (29,9)-(32,12) | (30,12) | `Ebbsworth_HarbourMastersHouse` | G4-A (11 x 8) |
| 6 | Boatyard | (31,19)-(39,25) (9 x 7) | (33,25) | `Ebbsworth_Boatyard_1F`, `_2F` | `SlateportCity_SternsShipyard_1F` (21 x 15), `_2F` (17 x 15) |
| 7 | Lock House (optional interior) | (27,29)-(30,32) | (28,32) | `Ebbsworth_LockHouse` | G4-B (10 x 8) |
| 8 | East Gate | (39,26)-(43,29) | (41,29) | `Ebbsworth_EastGate` | `Route110_SeasideCyclingRoadEntrance` layout (15 x 6) |
| 9 | Warehouse | (34,9)-(40,14) | (36,14) | none | Exterior only, locked, 'TALLOW & CRANE' stencil. The door tile has a `bg_event` sign, no warp |
| 10 | Customs Shed | (1,23)-(4,26) | (2,26) | none | Exterior only, locked, a notice board. Post-game officer stands at (2,27) |
| 11 | Harbour Market stalls | (2,10)-(9,23) | none | none | Exterior objects and `bg_event`s |

### 6.2 Pokémon Center and Mart (shared)

Unchanged vanilla layouts. Positions that scripts rely on, from the vanilla maps: **Center 1F** (14 x 9): nurse (7,2), exit mats (6,8),(7,8), stairs up warp (1,6); the Link/PC objects at (1,3),(2,3) stay. **Center 2F** (14 x 10): stairs (1,6), Union Room warp (5,1), Trade warp (9,1). **Mart** (11 x 8): exit mats (3,7),(4,7), clerk (1,3). Add two ambient objects only if wanted: a sailor at the Center bench, a dock kid in the Mart. Stock: Ultra Ball, Super Potion, Hyper Potion, Super Repel, Net Ball, Dive Ball, Revive.

### 6.3 Net Menders' Cottage (G4-B)

**Purpose.** Two old net menders, a tide table, a rod display and a free item. **Plan (10 x 8):**

```
     x0 1 2 3 4 5 6 7 8 9
y0   #  # # # # # # # # #
y1   b  b . W . i B B S S      i = tide table (bg_event at (5,1))
y2   b  b . . . . B B K K      rod display = bg_event (6,1)
y3   .  . . . . . . * . .      * = Net Ball x3 (item ball at (7,3))
y4   .  R R R R . . . . .
y5   .  R M f m R . . . .      M = Mender A (3,5) facing right; m = Mender B (5,5) facing left
y6   .  R R R R . . . . P
y7   .  . . D D . . . . .
```
- **Mender A** (3,5) `FACE_RIGHT`: the one who mends nets. **Mender B** (5,5) `FACE_LEFT`: mends the first one's work. Both talk once each (topic: the tide table, 'The sea is always out for something').
- **bg_events:** tide table (5,1), rod rack (6,1) (flavour: which rod catches what on the south coast, one line).
- **Item:** Net Ball x3 as an item ball at (7,3).
- **Warps:** mats (3,7),(4,7) to `Ebbsworth` warp 2 (door (4,5)).

### 6.4 Old Captain's House (G4-C)

**Purpose.** The Dive and Aldermere hint. **Plan (12 x 9):**

```
     x0 1 2 3 4 5 6 7 8 9 10 11
y0   #  # # # # # # # # # #  #
y1   B  B B . W . . T T . B  B     (replace the TV with a ship's wheel decoration at (7,1) if a metatile exists; else keep the TV off)
y2   B  B B . . . . T T . B  B
y3   .  . . . . . . . . . .  .
y4   .  . . R R R R R R . .  .
y5   .  P . R R f f R N . P  .      N = Old Captain (8,5) facing left
y6   .  . . R R R R R R . .  .
y7   .  . . . . . . . . . *  .      * = Sea Incense (post-game ball at (10,7), hidden until FLAG_SYS_GAME_CLEAR)
y8   .  . . . . D D . . . .  .
```
- **Old Captain** (8,5) `FACE_LEFT`: says the Beaconmouth lighthouse keeper (MIZZLE) once pulled him out of a wreck; the old city (Aldermere) is drowned south-east; a Dive-capable trainer can go in (post-game hint).
- **Item:** Sea Incense (post-game). **Warps:** mats (5,8),(6,8) to `Ebbsworth` warp 3.

### 6.5 Harbour Master's House (G4-A)

**Purpose.** The Harbour Master (a woman) and her ledger; gives **TM Rain Dance** after the barge has been seen. **Plan:** G4-A as above.
- **Harbour Master** (8,4) `FACE_LEFT`: ledger bg_event on the bookshelf (7,2). Her line before the barge is seen: 'Come back when you've looked at the quay.' After `FLAG_EBBSWORTH_BARGE_SEEN`: gives TM Rain Dance, 'someone should write down where it is going' (topic only).
- **Second object:** an Azumarill or Wingull at (3,5) wandering (ambient Pokémon) (ambient, Pokémon only).
- **Warps:** mats (2,7),(3,7) to `Ebbsworth` warp 4.

### 6.6 Boatyard 1F and 2F (Sterns Shipyard layouts)

**Purpose.** Workshop, shipwright, apprentice; the **Super Rod** man upstairs. These are the vanilla `SlateportCity_SternsShipyard_1F` (21 x 15, Facility tileset) and `_2F` (17 x 15) copies. The big drum-and-pipes machine is the boat's engine ('the keel' in the shipwright's boast). Positions from the vanilla maps, reused:

- **1F:** door mats (2,14),(3,14); stairs up (3,1) to 2F (3,1). Objects: **Shipwright** at (5,5) `FACE_DOWN` (vanilla man_1), **Apprentice** at (10,7) `FACE_UP` (looking for the Wailmer pail), a wandering worker (18,8) `WANDER_LEFT_AND_RIGHT` (ambient), an expert at (12,11) `WANDER_AROUND` (a customer). Four objects.
- **2F:** stairs down (3,1) to 1F. **Rod man** at (10,7) `FACE_UP` (replaces the vanilla scientist). The other two vanilla scientists at (8,4) and (0,9) are removed or turned into a blueprint reader and a tea drinker (ambient).
- **Dialogue topics:** the Shipwright boasts and mentions a sunken town south-east ('the one the tide took': Aldermere). The Rod man asks a short fishing question and gives the **Super Rod** (badge 8 and `FLAG_EBBSWORTH_HARBOUR_MASTER_TALKED`, PROPOSED), then lists what each rod catches on the coast.
- **Warps:** 1F (2,14),(3,14) to `Ebbsworth` warp 5 (door (33,25)).

### 6.7 Lock House (optional, G4-B)

**Purpose.** Maud's hut. Optional interior (the gate script lives outside, on Maud's object). Plan: G4-B with a kettle on the stove (bg_event (8,1)), Maud's logbook on the table (4,5) as a bg_event, a sleeping Wailmer plush decoration. **Warps:** mats (3,7),(4,7) to `Ebbsworth` warp 6. Build last or skip; the town works without it.

### 6.8 East Gate (vanilla gate layout)

**Purpose.** The pass-through between the east quay and R23's land path. Vanilla layout 15 x 6: door pairs at (1,5),(2,5) and (12,5),(13,5); clerk object at (7,2). Veldris: **west door pair (1,5),(2,5)** goes to `Ebbsworth` warp 7 (door (41,29)); **east door pair (12,5),(13,5)** goes to `R23` warp 0 (the land path's start, see routes-south-detail.md). The **Gatekeeper** at (7,2) (vanilla Mart-employee sprite is fine, or a sailor) tells you the pines were planted by the 'harbour widows' (flavour) and that R23 is the road with the pier.

---

## 7. Door and warp table

`Ebbsworth` (outdoor map) warp events, in order. Interior mat warps return to the matching exterior warp number.

| # | Map | Tile | Destination | Dest warp | Notes |
|---|---|---|---|---|---|
| 0 | `Ebbsworth` | (13,13) | `Ebbsworth_PokemonCenter_1F` | 0 | Center door |
| 1 | `Ebbsworth` | (13,22) | `Ebbsworth_Mart` | 0 | Mart door |
| 2 | `Ebbsworth` | (4,5) | `Ebbsworth_NetMendersCottage` | 0 | |
| 3 | `Ebbsworth` | (10,5) | `Ebbsworth_OldCaptainsHouse` | 0 | |
| 4 | `Ebbsworth` | (30,12) | `Ebbsworth_HarbourMastersHouse` | 0 | |
| 5 | `Ebbsworth` | (33,25) | `Ebbsworth_Boatyard_1F` | 0 | |
| 6 | `Ebbsworth` | (28,32) | `Ebbsworth_LockHouse` | 0 | optional |
| 7 | `Ebbsworth` | (41,29) | `Ebbsworth_EastGate` | 0 | |

Interior warps:

| Map | Tiles | Destination | Dest warp |
|---|---|---|---|
| `Ebbsworth_PokemonCenter_1F` | (6,8),(7,8) | `Ebbsworth` | 0 |
| `Ebbsworth_PokemonCenter_1F` | (1,6) | `Ebbsworth_PokemonCenter_2F` | 0 |
| `Ebbsworth_PokemonCenter_2F` | (1,6) | `Ebbsworth_PokemonCenter_1F` | 2 |
| `Ebbsworth_Mart` | (3,7),(4,7) | `Ebbsworth` | 1 |
| `Ebbsworth_NetMendersCottage` | (3,7),(4,7) | `Ebbsworth` | 2 |
| `Ebbsworth_OldCaptainsHouse` | (5,8),(6,8) | `Ebbsworth` | 3 |
| `Ebbsworth_HarbourMastersHouse` | (2,7),(3,7) | `Ebbsworth` | 4 |
| `Ebbsworth_Boatyard_1F` | (2,14),(3,14) | `Ebbsworth` | 5 |
| `Ebbsworth_Boatyard_1F` | (3,1) | `Ebbsworth_Boatyard_2F` | 0 |
| `Ebbsworth_Boatyard_2F` | (3,1) | `Ebbsworth_Boatyard_1F` | 2 |
| `Ebbsworth_LockHouse` | (3,7),(4,7) | `Ebbsworth` | 6 |
| `Ebbsworth_EastGate` | (1,5),(2,5) | `Ebbsworth` | 7 |
| `Ebbsworth_EastGate` | (12,5),(13,5) | `R23` | 0 |

(Warp numbers in the vanilla Center are: 1F warp 0 and 1 are the mats, warp 2 is the stairs; keep that order so the dest ids above hold. If Porymap renumbers, follow its numbering.)

---

## 8. NPCs and objects outdoors (town map, 10 objects)

| Object | Tile | Facing/move | Role |
|---|---|---|---|
| Quay lookout (PROPOSED: **Dunstan**) | (18,3) | `FACE_RIGHT` | Counts boats. 'You came up the weir? Nobody comes up the weir.' Praises Waterfall |
| Lock-keeper (PROPOSED: **Maud**) | (27,34) | `FACE_LEFT` | Opens the gate for anyone with the Surf badge (`FLAG_BADGE05_GET`), sets `FLAG_EBBSWORTH_LOCK_OPEN`, swaps the gate-leaf metatiles with `setmetatile`. Complains the gate has not been shut since the Goldsworth barges came |
| Barge hand | (27,21) | `FACE_LEFT` | 'Four hundred permits. The foreman counted.' Scheme 9 seed |
| Foreman | (36,15) | `FACE_DOWN` | Sticks to the crates and does not know what is in them. Does not like being asked |
| Kid on the bridge | (22,16) | `WANDER_LEFT_AND_RIGHT` | Races the player to the other bank. Rude, gives nothing |
| Market vendor | (5,14) | `FACE_DOWN` | Berry seller (Oran, Pecha, Sitrus at ordinary prices). Shop script |
| Customs Officer | (2,27) | `FACE_DOWN` | Visible from the start; before the League he says 'Vesperhaven? Never heard of it. Mind the rope.' and the rope stays. After `FLAG_SYS_GAME_CLEAR` he unhooks the rope (script swaps the rope metatiles at x 1, y 28-30) |
| Wingull on bollards x2 | (18,6), (27,2) | `LOOK_AROUND` | Ambient Pokémon (gull objects) |

Bg events: sign 'EBBSWORTH' (18,4); bridge sign 'MIND THE TIDE' (19,14); **barge crates** signs (31,16),(32,16) reading the stencil, which set `FLAG_EBBSWORTH_BARGE_SEEN`; warehouse door sign (36,14); customs notice (2,26); lock wheel signs (19,33),(26,33); market stall signs.

**Fishing spots (PROPOSED, so Surf stays encounter-free in town).** Fishing only (the card says no wild encounters in town, and fishing is not a grass encounter): North quay (21,2), bridge rail (22,18), south quay (14,32), using R22's and R23's Good Rod and Super Rod tables at levels 53 to 55. The Old Rod never gets anything here. Remove this if the author wants no town fishing at all.

---

## 9. Items and hidden items (positions)

| Item | Where | Gate |
|---|---|---|
| Super Rod | Boatyard 2F, Rod man | Badge 8 plus the Harbour Master talked to (PROPOSED) |
| TM Rain Dance | Harbour Master's House | After the barge is seen |
| Net Ball x3 | Net Menders' Cottage (7,3) | None |
| Pearl (hidden) | Under the north quay bollard at (17,2) | None |
| Heart Scale (hidden) | Behind the crates at (31,17) | None |
| Max Ether (hidden) | Behind the Lock House at (31,30) | None |
| Big Pearl | The harbour rock, a Dive spot at (12,29) (needs a tiny `Underwater_Ebbsworth` 20 x 10 map copied from `Underwater_SootopolisCity`) | Dive (badge 9), post-game |
| Sea Incense | Old Captain's House ball (10,7) | After the League |

---

## 10. Scripts and events the build needs (for Claude to wire afterwards)

- `Ebbsworth_MapScripts`: `ON_TRANSITION` sets `FLAG_VISITED_EBBSWORTH` and the heal location; if `FLAG_EBBSWORTH_LOCK_OPEN` set the gate-open metatiles; if `FLAG_SYS_GAME_CLEAR` set the rope-open metatiles at x 1, y 28-30 once the officer has been spoken to.
- Lock gate: Maud's object script (Surf badge check, `setmetatile` over (20..25,33), `setflag FLAG_EBBSWORTH_LOCK_OPEN`). The gate leaves must be impassable until opened (collision bits 0x0C00 kept on the closed tiles, CLAUDE.md warning about the top 6 bits).
- Barge crates `bg_event`s and barge hand: `FLAG_EBBSWORTH_BARGE_SEEN`.
- Harbour Master TM gift and Rod man Super Rod gift: both once-only flags.
- Customs rope: officer script clears rope at game clear.
- No trainers in town, no battles, no coord_events. (The player's arrival from R22 is a plain map connection.)

**Flags (not claimed, from the card):** `FLAG_VISITED_EBBSWORTH`, `FLAG_EBBSWORTH_LOCK_OPEN`, `FLAG_EBBSWORTH_BARGE_SEEN`, `FLAG_RECEIVED_SUPER_ROD`, `FLAG_RECEIVED_TM_RAIN_DANCE`, `FLAG_EBBSWORTH_SEA_GATE_OPEN`, hidden `FLAG_HIDDEN_ITEM_EBBSWORTH_PEARL`, `_HEART_SCALE`, `_MAX_ETHER`; new here (PROPOSED): `FLAG_EBBSWORTH_HARBOUR_MASTER_TALKED` (gates the Super Rod), `FLAG_ITEM_EBBSWORTH_NET_BALL`, `FLAG_ITEM_EBBSWORTH_SEA_INCENSE`, `FLAG_HIDDEN_ITEM_EBBSWORTH_BIG_PEARL`. Reuse spare flags from [../../flags.md](../../flags.md); never overwrite one in use.

---

## 11. Build checklist (in order)

1. Read [../../flags.md](../../flags.md) and [../../engine-edits.md](../../engine-edits.md); decide whether to import LeoB `slateport` now (CREDITS row, door anim, engine-edits entry in the same commit).
2. `Change Dimensions` on a duplicate of `SlateportCity` to 44 x 36; clear the unused museum island and shipyard-side pier; set `region_map_section` to `MAPSEC_EBBSWORTH`. Delete Slateport's two duplicated heal locations before saving (duplicate ids break the build).
3. Paint the river (x 20-25), basin (y 27-31), quays, bridge; place the buildings per section 6.1; plant the trees; hang the awnings.
4. Paint the **lock gate** as two states (closed and open) and note the metatile ids for the script.
5. Build the three Gen 4 templates (G4-A is a shared copy; G4-B and G4-C new) and the six small interiors.
6. Duplicate Center and Mart layouts via *Add New Map with Layout*; set the heal location (13,14).
7. Build the Boatyard from the Sterns layouts; replace the engine decoration only if wanted.
8. Add warps per section 7; set connections (north R22, south R23, west R28).
9. Close and reload Porymap after Claude edits warps or events (CLAUDE.md rule 2).
10. Claude wires scripts, objects and dialogue; run `python3 design/tools/dialogue_check.py` on each `scripts.inc`; `make -j4`.
11. Update `design/` (flags.md, engine-edits.md if tileset files were replaced, CREDITS.md), check no ROM or save is staged, commit and push.

---

## 12. Open questions

1. **R22's Waterfall dog-leg versus the card.** The card has 'the town beyond the top' of the weir, but R22 reaches Ebbsworth's north edge, so a climb cannot be the last thing before the town. My resolution (details in routes-south-detail.md): the weir is a switchback inside R22 (down, a cascade up, down again), and the town is entered by a plain connection. Confirm, or tell me to put the weir inside this town's north end instead.
2. **'The Surf gate south'.** I kept the card's reading (a lock gate Maud opens for Surf-badge holders). It is an NPC plus a metatile swap, not a hard block, because R22 already needs Surf and Waterfall.
3. **Importing LeoB `secondary/slateport`** replaces vanilla tileset files in place (as was done for General and Petalburg). Is the author happy to do that for every harbour town (Slateport, Lilycove, Dewford, Sootopolis), or should these towns stay on the vanilla art with a recolour later?
4. **House tilesets.** The town card names `LAYOUT_HOUSE1`/`HOUSE2` (GenericBuilding tiles), but README decision 1 says all ordinary homes are Gen 4 Interior. I followed the README. Shared G4-A means every plain family house looks the same; the author may want a few more layouts.
5. **Town fishing.** Fishing-only in town water is my addition. Keep or drop?
6. **Super Rod gate.** Rod man needs badge 8 plus the Harbour Master first (card, PROPOSED). If the Super Rod is earned earlier elsewhere, the Rod man gives a Net Ball set instead (card open question 4).
