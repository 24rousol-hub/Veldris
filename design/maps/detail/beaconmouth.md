# BEACONMOUTH: detailed design (lighthouse city, GYM 9 Water, Scheme 9)

Status: **PROPOSED** (the leader MIZZLE and his team are BUILT in [../../trainer-roster.md](../../trainer-roster.md); everything else here is a suggestion until the author approves it). Written 2026-10-01 from [../interiors/README.md](../interiors/README.md), [../interiors/catalogue.md](../interiors/catalogue.md), [../README.md](../README.md), [../../interiors.md](../../interiors.md), [../index.md](../index.md), the card [../towns/beaconmouth.md](../towns/beaconmouth.md), [../../gyms.md](../../gyms.md), [../../troglodyte-arc.md](../../troglodyte-arc.md), [../../goldsworth.md](../../goldsworth.md), roads R25 and R26 ([../routes-south.md](../routes-south.md)), and by looking at the Project Palladium renders `Olivine City.png` (44 x 41, the town), `KantoGyms3YearsLatercorrected.png` (the Water gym panel), `Olivine City Gym.png` and the Team Aqua tileset examples named below. Templates **G4-A, G4-B, G4-C** are in [ebbsworth.md](ebbsworth.md) section 6.0; the **shared Goldsworth House layout** (13 x 11) is in [kingsquay.md](kingsquay.md) section 6.10. Neighbours: [driftsands.md](driftsands.md) (R25), [aldermere.md](aldermere.md) (R26), [kingsquay.md](kingsquay.md) (ferry, Tallow & Crane).

**New minor names and details introduced in this file are all PROPOSED:** the wheel names Brass, Red and Blue, the logbook wording, the gym floor names (Pump Room, Gallery, Lamp Room are the card's), the Cove ranger's post, the plaza and causeway coordinates.

Conventions: **(x, y) from the top-left tile (0,0)**; footprints `(x0,y0)-(x1,y1)` inclusive; a 4-wide building's door is the bottom-row tile `(x0+1, y1)`; interior exit mats are two tiles wide; maps stay `layout_version` `emerald`, `REGION_HOENN`.

---

## 1. Quick facts

| | |
|---|---|
| Map | `Beaconmouth`, **52 x 41** (the Olivine render's 44 x 41 plus an 8-column strip on the east for the Waterfall cove: `(52+15)*(41+14) = 3685`, limit 10240) |
| Exterior base | **Palladium `Olivine City.png`** traced, painted with **LeoB ORAS `secondary/dewford`** (sand ground, blue tile roofs, pines: it matches the Olivine picture almost exactly). The card's fallback base (`SootopolisCity`) is **not** recommended: it is white rock, not sand |
| Section / fly | `MAPSEC_BEACONMOUTH` (11 characters); fly town; `HEAL_LOCATION_BEACONMOUTH` on (14,26) outside the Center door |
| Music | Town `MUS_PETALBURG` (a gentle Hoenn track), gym `MUS_GYM`, leader battle `MUS_VS_GYM_LEADER`, Scheme 9 scene `MUS_ENCOUNTER_SUSPICIOUS`, underwater `MUS_UNDERWATER` |
| Weather | `WEATHER_SUNNY`. Optional gag (the leader's name is a drizzle): `WEATHER_RAIN` on this one map; check `include/config/battle.h` first, because some expansion configs bring overworld rain into battles |
| Gym / scheme | **Gym 9 Water**: MIZZLE, TIDE BADGE, TM Water Pulse, HM Dive. **Scheme 9, the invoice**, played on the causeway in front of the gym door. **Goldsworth house** (Prescott and Kip) |
| Roads | R25 south edge (left), R26 west edge (post-game), ferry from Kingsquay |
| Objects | Town map 12 visible at most (scene actors are hidden until the scene); gym maps 2 each; houses under 6 |
| Build effort | **Hard** (card): the biggest card in the south |

---

## 2. Description

**First glance from R25 (the cliff road).** The player climbs a long stone causeway across the harbour mouth: sea on both sides, a gateway of two stone pillars at the far end beside a weathered 'BEACONMOUTH' sign. Ahead, the town stacks up the sandy shore: blue roofs, pines, and, standing alone on its own headland to the right, a white tower with a brass lamp in its crown. The lamp turns even in daytime. The whole town is arranged around that one tall thing.

**From the sea (the Kingsquay ferry).** The ferry noses into a wooden pier at the foot of the town; the first thing on the quay is a Wingull on a bollard and a Lamplighter carrying a ladder.

**From R26 (post-game, by water).** A stone pier and ferry quay on the west edge, a coil of rope across the mouth until the League is beaten.

**Mood, colour, sound, time of day.** Salt-faded and cheerful: sand, white plaster, blue roof tiles, pine green, brass. A town that has seen the sea take things and has opinions about it. Sound: a gentle Petalburg-style track and a slow foghorn-like lamp bell (one-shot on entering the gym causeway). **Time of day: mid-afternoon with a faint haze** (stock sunny palette); if the author takes the drizzle gag, light rain.

**The one memorable view.** The causeway at (28,27): three tiles wide, inlet water on the left, open sea on the right, and the lighthouse door straight ahead at (32,30). It is the picture the Scheme 9 scene needs, so keep the causeway clear of everything but the lantern posts.

---

## 3. Street layout in words (a numbered walk)

Palette note for the numbers: sand ground everywhere; fences are the pale picket pieces; the sea is south and west; the inlet (a quiet blue bay) cuts in from the east.

1. **South gate and the causeway bridge (x 5-8, y 29-40).** R25 arrives at the bottom edge (x 5-8, y 40). A 4-wide stone **causeway bridge** crosses the harbour mouth (water below it is surfable; use the same bridge pieces as Ebbsworth's). Two stone gate pillars at (5,38) and (8,38), the town sign at (9,28). A stream from the cliffs (R25's stream) runs under the bridge into the harbour.
2. **The beach shelf and the main street (y 26-28).** A sandy street runs east from the bridge head along the harbour: (5,26) to (25,27), edged with beach grass.
3. **Lower town (x 6-25, y 20-27).** The **Pokémon Center** (13,22)-(16,25), door (14,25), faces the street; the **Diver's Shed** (6,22)-(9,25), door (7,25), on the west; the **market square** (x 18-24, y 20-24) with a well at (21,22) and four market stalls at (18,20), (22,20), (18,23), (22,23).
4. **Middle town (x 13-24, y 15-19).** The **Lamplighters' Lodge** (13,16)-(16,19), door (14,19); the **Mart** (20,15)-(23,18), door (21,18).
5. **Upper town (x 25-34, y 11-14).** Two blue-roofed houses side by side: the **Fishing family's house** (25,11)-(28,14), door (26,14); the **Artist's house** (30,11)-(33,14), door (31,14).
6. **The Goldsworth House (8,9)-(15,13)**, door (11,13), top-left, the grandest roof in town, behind a picket fence (y 14, x 6-17) with a gate at (11,14) and a nameplate sign at (7,14). Pines west and north.
7. **The harbour (x 9-25, y 29-40).** The **pier** (14,29)-(16,31) with a wooden ferry berth; the Kingsquay ferry (an `SS_TIDAL` ship object, already in the tree) moored at (15,33); deep water at (10,36), the **Dive spot**.
8. **The Keeper's Cottage (21,28)-(24,31)**, door (22,31), at the foot of the causeway on the shore, with the keeper's **LAPRAS** (a ferry Pokémon, ambient object) in the water behind it at (23,33).
9. **The causeway (x 26-30, y 26-28)**, 3 tiles wide, to the **lighthouse headland** (the plaza x 31-37, y 26-33). The **Lighthouse (the gym)** stands at (31,20)-(34,30), door (32,30). A **Lamplighter apprentice** polishes a lens at (29,26).
10. **The rear cove (x 44-51, y 20-35).** East of the headland behind a rock wall: reached only by **Waterfall** from the sea: from the plaza's south water (x 38-43, y 36-38) surf east to the cascade at (45,33)-(45,35) and climb to the cove pool (x 44-50, y 24-32). A rock ledge (x 47-51, y 20-23) with the **Cove ranger** and a visible Max Revive.

Surfable: the harbour, the inlet, the sea south and west, the cove pool. No grass in town.

---

## 4. Map plan

Sketch, **1 character = 2 x 2 tiles** (26 x 21 characters for 52 x 41 tiles). It was generated from the footprints, so it matches the tables. Legend: `T` trees, `V` Goldsworth House, `-` fence, `f` Fishing family, `a` Artist, `L` Lodge, `M` Mart, `s` market square, `P` Pokémon Center, `d` Diver's Shed, `k` Keeper's Cottage, `H` lighthouse, `:` causeway, `_` plaza, `=` main street, `c` causeway bridge, `p` pier, `S` ferry, `~` water, `e` cove ledge, `|` cascade.

```
x:  0    1    2    3    4    5
y0  TTTTTTTT....TTTTTTTTTT....
y2  TTTTTTTT....TTTTTTTTTT....
y4  TTTTTTTT....TTTTTTTTTT....
y6  TTTTTTTT....TTTTTTTTTT....
y8  TTTTVVVV....TTTTTTTTTT....
y10 TT..VVVV....fffaaTTTTT....
y12 TT..VVVV....fffaa.TTTT....
y14 TT.------.MMfffaa~~TTT....
y16 TT....LLL.MM.~~~~~~TTT....
y18 TT....LLL.MM.~~~~~~TTT....
y20 TT.......ssss~~HHH~TTT.eee
y22 TT.dd.PPPssss~~HHH~TTT.eee
y24 TT.dd.PPPssss~~HHH~...~~~~
y26 ..===========::HHH_...~~~~
y28 ..ccc..pp.kkk::HHH_...~~~~
y30 ~~ccc~~pp~kkk..HHH_...~~~~
y32 ~~ccc~SSSS~~~..____...~~~~
y34 ~~ccc~SSSS~~~......~~~~~~~
y36 ~~ccc~SSSS~~~......~~~~~~~
y38 ~~ccc~~~~~~~~......~~~~~~~
y40 ~~ccc~~~~~~~~......~~~~~~~
```
(Header digits mark every 10 tiles. The cascade `|` at x 44-46, y 33-35 is drawn under the sea in this coarse sketch.)

**Connections:**

| Edge | Neighbour | Offset | Notes |
|---|---|---|---|
| South | `R25` (top edge, east end) | **-54** (R25's road end x 59-62 meets x 5-8) | The causeway bridge x 5-8 reaches y 40. R25 is built so its road ends against its top edge at the east end |
| West | `R26` (east end) | 0 | Water x 0-4, y 31-38, post-game. Before the League a **rope** (impassable fence metatile) closes x 1, y 33-35; the **ferry captain** stands on the stone pier at (3,31) and removes it at game clear (see section 9). R26's east end is open sea |
| North, east | none | | Trees and rock. **Wall the Olivine render's north road with trees** (card): the pale road at x 18-22, y 0-9 becomes forest |

---

## 5. Base, tilesets, palette notes

**Tracing `Olivine City.png`** (705 x 653 px, no grid line, so 44 x 41 tiles at 16 px). Where the render's features go:

| Olivine feature (tiles) | Becomes |
|---|---|
| Brown-roofed gym, (8,9)-(15,13), door (11,13) | **Goldsworth House** (the grandest house in town) |
| Blue-roofed Mart, (20,15)-(24,18) | Mart (draw it 4 wide: (20,15)-(23,18), door (21,18)) |
| Red-roofed Pokémon Center, (13,22)-(17,25) | Center (4 wide: (13,22)-(16,25), door (14,25)) |
| Blue houses: (13,16)-(17,19), (6,22)-(10,25), pair (25,11)-(34,14) | Lamplighters' Lodge, Diver's Shed, Fishing family and Artist |
| White eight-sided tower, (30,20)-(35,31), door (32,30) | **The Lighthouse (the gym)**, drawn 4 wide x 11 tall (see below) |
| Wooden pier and red-roofed ship, (14,29)-(25,37) | The pier and the `SS_TIDAL` ship **object** (no ship tiles needed) |
| North sandy road x 18-22, y 0-9 | **Walled with trees** (Veldris has no road there) |
| Inlet water, x 26-37, y 15-26 | The inlet |

Added by hand: the **causeway bridge** (x 5-8, y 29-40, south edge), the **Keeper's Cottage plot** (21,28)-(24,31), the **headland plaza** (31-37, 26-33), the **causeway** (26-30, 26-28), and the **east cove strip** (x 44-51).

**The lighthouse art problem (card open question 3).** Emerald has no tall lighthouse tileset, and none of the tilesets in the Team Aqua repo has one. Options, cheapest first, with my recommendation:

1. **(Recommended) A stacked 'tall white house'.** Build a 4-wide, 11-tall tower from the LeoB Dewford house pieces: white plaster wall metatiles for the shaft, three window metatiles at rows y 22, 25 and 28, the blue roof tiles as a cap at y 20-21, and the lamp-post or window-light metatile as the lantern at (32,20). It reads as a squat white lighthouse at this scale, needs no new art, and only exterior tiles change; the interior does not depend on it.
2. A white block with a lantern roof drawn like the Devon Corp building (about 6 wide, 9 tall), if the Mauville or Rustboro secondaries were in use (they are not for this town).
3. New tiles drawn for the author (a 4 x 11 sprite sheet, about 44 metatile slots). Not planned.

**Tilesets (recommended).**

| Where | Primary | Secondary | Source, credit |
|---|---|---|---|
| Beaconmouth outdoors | `gTileset_General` (LeoB, imported) | **LeoB ORAS `secondary/dewford`** | `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS/tilesets/secondary/dewford` + `graphics/door_anims/dewford.png`. Same metatile ids as vanilla. **CREDITS.md row (leob0505)**; `engine-edits.md` entry (replaces vanilla files in place). **Shared with Driftsands**: import once, in the first commit that needs it |
| Shared Center and Mart | `gTileset_Building` | `PokemonCenter`, `Shop` | Vanilla |
| Houses, huts, cottage | `gTileset_Building` | `Gen4Interior` | Hollowbrook's, credited |
| **Gym, all floors** | `gTileset_Building` (try first; fall back to `gTileset_General` if the water tile is missing) | **Sewer (Clear water) Secondary** | `.../Full Tilesets/Sewer (Clear water) Secondary`. Credits (its `credits.md`): **Magiscarf** (platform and the round drain), **Kyle Dove** (the barrel), **Kane89** (the pipes), **Aveontrainer** (compiled the sheet), **Rahtak** (clear-water variants; credit Rahtak for the insertable reformat too). Its `metatiles.bin` is 6144 bytes = 384 two-layer or 256 triple-layer metatiles; the README does not mention triple-layer, so I expect two-layer: open it in Porymap to confirm before committing. It has an `anim` folder (animated water): for a first version skip the animation (static water), and only wire `src/tileset_anims.c` if the author approves an engine edit (log it in `design/engine-edits.md`). Importing a tileset follows the Gen 4 Interior pattern (`graphics.h`, `metatiles.h`, `headers.h` entries). **Fallback with no import:** vanilla `gTileset_Facility` (Aqua Hideout B2F has a railed pool, pipes and tanks) |
| Dive cove | `gTileset_Underwater` | (vanilla) | Copy `Underwater_SootopolisCity` (20 x 10) |

**Why Sewer (Clear water) for the gym.** Looking at its `example.png`: a brick wall with arched alcoves and wall lamps, vertical brass pipes, floor grates, a steel mesh gantry (a catwalk across water), stone walkway, clear blue water with a drain mouth pouring in. That is a lighthouse pump room almost verbatim, and it is the only set in the repo with a gantry and clear water. README decision 4 says to paint gyms with the vanilla gym tilesets and add theme tiles only where the card says so; the card asks for flooded floors and valve wheels, which none of the vanilla gym tilesets has (vanilla Sootopolis gym is an ice cave, I rendered it to check). Hence one imported tileset.

**The three wheels.** The tileset has no wheel. **Needs 3 small new metatiles**: a round brass valve wheel in brass, red and blue, placed on the wall tile. Cheapest: recolour the tileset's round drain-mouth metatile three ways (the author, in Porymap's tileset editor and an image editor). If that is too much, the wheels are `bg_event`s on a plain wall with a `bg_event` text, and colour names carry the puzzle. **Water behaviour.** The gym water must be a metatile with behaviour `MB_NORMAL` (not surfable) and painted with collision 1, so it cannot be walked on or surfed. Copy the water metatile to a free slot and set its behaviour in the tileset editor.

**Palladium credit.** The first commit that traces `Olivine City.png` or the Kanto gym panel adds a `CREDITS.md` row crediting the **Project Palladium team** with the file names.

---

## 6. Buildings

### 6.1 Overview

| # | Building | Footprint | Door | Interior maps | Layout |
|---|---|---|---|---|---|
| 1 | Pokémon Center | (13,22)-(16,25) | (14,25) | `Beaconmouth_PokemonCenter_1F`, `_2F` | `LAYOUT_POKEMON_CENTER_1F`, `_2F` |
| 2 | Mart | (20,15)-(23,18) | (21,18) | `Beaconmouth_Mart` | `LAYOUT_MART` |
| 3 | **Lighthouse Gym** | (31,20)-(34,30) | (32,30) | `Beaconmouth_Gym_1F`, `_2F`, `_3F` | custom, 15 x 21 / 15 x 21 / 15 x 19 (section 6.3) |
| 4 | Keeper's Cottage | (21,28)-(24,31) | (22,31) | `Beaconmouth_KeepersCottage` | custom G4-C style (12 x 9) |
| 5 | Goldsworth House | (8,9)-(15,13) | (11,13) | `Beaconmouth_GoldsworthHouse` | shared Goldsworth layout (13 x 11) |
| 6 | Diver's Shed | (6,22)-(9,25) | (7,25) | `Beaconmouth_DiversShed` | G4-B (10 x 8) |
| 7 | Lamplighters' Lodge | (13,16)-(16,19) | (14,19) | `Beaconmouth_LamplightersLodge` | G4-C (12 x 9) |
| 8 | Fishing family's house | (25,11)-(28,14) | (26,14) | `Beaconmouth_FishingFamilyHouse` | G4-A (11 x 8) |
| 9 | Artist's house | (30,11)-(33,14) | (31,14) | `Beaconmouth_ArtistsHouse` | G4-B (10 x 8) |
| 10 | Underwater cove | none | Dive at (10,36) | `Underwater_Beaconmouth` | copy of `Underwater_SootopolisCity` (20 x 10) |

Twelve interior maps. Heal location only for the Center.

### 6.2 Pokémon Center and Mart (shared)

Vanilla, unmoved: Center nurse (7,2), mats (6,8),(7,8), stairs (1,6); Mart mats (3,7),(4,7), clerk (1,3). **Mart stock** (card, the last Mart before the League): Max Potion, Full Heal, Revive, Ultra Ball, Dive Ball, Net Ball, Hyper Potion, Max Repel. Ambient: a Lamplighter on the Center bench.

### 6.3 The Lighthouse Gym (three floors, the puzzle in tiles)

**What it is.** A flooded lighthouse. The player climbs by **draining the water floor by floor with brass valve wheels**. Gym facts (built): leader **MIZZLE** (`TRAINER_MIZZLE`, Water, a big jolly deadpan man; picture Scott), team Gyarados 58, Seismitoad 58, Araquanid 59, Barraskewda 59, Lanturn 59, Milotic 60. Rewards: **TIDE BADGE** (`FLAG_BADGE09_GET`), **TM Water Pulse**, **HM Dive**. Four gym trainers (card, PROPOSED, 3 Pokémon each, levels 54 to 56, no IVs, reuse vanilla Hoenn ids): 1F Swimmer male **Corrin** (Floatzel 54, Starmie 55, Octillery 55), 1F Swimmer female **Marlo** (Seaking 54, Jellicent 55, Mantine 55), 2F Sailor **Ivo** (Pelipper 54, Gastrodon 55, Cloyster 56), 2F Fisherman **Hobb** (Qwilfish 54, Whiscash 55, Sharpedo 56). 15-object limit respected (1F: 2, 2F: 2, 3F: 2).

**Gym guide statue** outside the door at (30,30) and (35,30), text 'The tide waits for no one. The pumps wait for the right one.' (bg_event; two statues flanking the door as in vanilla gyms).

**Interior look.** The Palladium Water panel in `KantoGyms3YearsLatercorrected.png` (top-centre panel, about 15 x 19 tiles: pale blue floor tiles, a deep pool, a cream sand catwalk winding down to the door, the leader on a cross-shaped platform with four porthole lamps on the back wall) is the **3F layout idea**; 1F and 2F use the same vocabulary on the Sewer tileset. Palladium credit applies.

#### Legend for the three plans

`#` wall, `.` stone floor, `=` catwalk or sandbar (walkable from the start), `~` flooded water (blocked), `1` `2` `3` (1F) or `4` `5` (2F) or `1` (3F) = **water that becomes walkable** at that step (swap with `setmetatile`), `S` stairs or ladder warp, `D` door mat, `P` pump decoration (blocked). Wheels, the lever, the lectern and statues are `bg_event`s on **wall tiles**, written as coordinates in the tables, so they cost no object slots.

#### 1F: the Pump Room (15 x 21)

```
     x: 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
y0    # # # # # # # # # # # # # # #
y1    # # # # # # # S # # # # # # #
y2    # # . . . . . . . . . . . # #
y3    # # . . . . . . . . . . . # #
y4    # # ~ ~ ~ ~ ~ ~ 3 ~ ~ ~ ~ # #
y5    # # ~ ~ ~ ~ ~ ~ 3 ~ ~ ~ ~ # #
y6    # # ~ ~ ~ ~ ~ ~ 3 ~ ~ ~ ~ # #
y7    # # ~ ~ ~ ~ ~ ~ 3 ~ ~ ~ ~ # #
y8    # = ~ ~ ~ ~ ~ ~ = = = = ~ = #
y9    # = ~ ~ ~ ~ ~ ~ = = = = ~ = #
y10   # = ~ ~ ~ ~ ~ ~ = = = = ~ = #
y11   # = ~ ~ ~ ~ ~ ~ ~ ~ 2 ~ ~ = #
y12   # = ~ ~ ~ = = = = = 2 ~ ~ = #
y13   # = ~ ~ ~ = = = = = 2 ~ ~ = #
y14   # = ~ ~ ~ = = = = = ~ ~ ~ = #
y15   # = ~ ~ ~ ~ ~ 1 ~ ~ ~ ~ ~ = #
y16   # = ~ ~ ~ ~ ~ 1 ~ ~ ~ ~ ~ = #
y17   # = . . . . . . . . . . . = #
y18   # = . . . . . . . . . . . = #
y19   # = . . . . . . . . . . . = #
y20   # # # # # # D D # # # # # # #
```

(Validated with a small connectivity check while writing this: the three wheels are reachable at the start, the islands and the stairs are not, and the stairs become reachable only after all three steps.)

- **Entrance:** door mats (6,20),(7,20) to `Beaconmouth` warp 2 (gym door (32,30)). **Stairs up:** (7,1) to `Beaconmouth_Gym_2F` (7,20).
- **The pit** (water, blocked) x 2-12, y 4-16. **West catwalk** x 1, y 8-19 and **east catwalk** x 13, y 8-19 are walkable from the start and lead to the wheels, so the order is a memory puzzle, not a geometry one. **Island 1** (x 5-9, y 12-14), **Island 2** (x 8-11, y 8-10): sandbars with a trainer each, unreachable until their strips open. Water at x 12 (y 8-10) keeps Island 2 off the east catwalk.
- **Wheels** (bg_events on wall tiles; the player stands on the catwalk and faces the wall): **Brass** at (0,18), stand (1,18); **Red** at (0,11), stand (1,11); **Blue** at (14,11), stand (13,11).
- **Keeper's logbook** (lectern, bg_event) at (3,18); **gym statues** (bg_event) at (5,19) and (8,19) flanking the door.
- **Trainers.** **Corrin** (Swimmer male) at (7,13) `FACE_DOWN`, sight 4: he looks down strip A (x 7, y 14-17). **Marlo** (Swimmer female) at (10,9) `FACE_DOWN`, sight 4: she looks down strip B (x 10, y 10-13). Each fights as soon as the strip they watch becomes walkable and the player steps on it ('come into view', card).
- **The puzzle.** The log's wording (PROPOSED): 'Brass, then Red, then Blue: the sea comes in the way it goes out.' Turning a wheel in the **right order** lowers the water one step; the **wrong** wheel floods everything back with a joke line and resets to 0.

| Step | Turn | `VAR_BEACONMOUTH_GYM_WATER` | Tiles that become sand (`setmetatile`, walkable, collision 0) | What the player can now do |
|---|---|---|---|---|
| 0 | start | 0 | none | Platform and both catwalks only |
| 1 | **Brass** (when var is 0) | 1 | strip A: (7,15), (7,16) | Reach Island 1; Corrin sees the player on the strip |
| 2 | **Red** (when var is 1) | 2 | strip B: (10,11), (10,12), (10,13) | Reach Island 2; Marlo sees the player |
| 3 | **Blue** (when var is 2) | 3, and `FLAG_BEACONMOUTH_GYM_1F_DRAINED` | strip C: (8,4), (8,5), (8,6), (8,7) | Reach the north gallery and the stairs (7,1) |
| any wrong wheel | | back to 0 | all nine strip tiles back to water (walkable only while the flag is unset) | The line: the pump coughs and the sea comes back |

On entering the map, an `OnTransition` script re-applies every strip up to the saved var (or all of them if the 1F flag is set), so leaving the gym does not undo progress. Wheels are inert once the flag is set ('already open'). **Warp rule:** because the trainers stand on islands and the wheels are on the catwalks, a player can never be standing on a strip when it floods, but still make the flood script check the player's tile (and refuse with a gentle 'wait for the water to settle' if it is a strip) as a safety.

#### 2F: the Gallery (15 x 21)

A raised gantry round a flooded pit. The player arrives from the 1F stairs on the bottom platform and must reach the top stairs.

```
     x: 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
y0    # # # # # # # # # # # # # # #
y1    # # # # # # # S # # # # # # #
y2    # # # # # # . . . # # # # # #
y3    # = = = = = = = = = = = = = #
y4    # = ~ ~ ~ ~ ~ ~ ~ ~ = ~ ~ = #
y5    # = ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ = #
y6    # = ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ = #
y7    # = ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 5 #
y8    # = ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 5 #
y9    # ~ ~ ~ ~ ~ P P P ~ ~ ~ ~ = #
y10   # ~ ~ ~ ~ ~ P P P ~ ~ ~ = = #
y11   # = ~ ~ ~ ~ P P P ~ ~ ~ ~ = #
y12   # = ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 4 #
y13   # = ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 4 #
y14   # = ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ = #
y15   # = ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ = #
y16   # = ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ = #
y17   # = ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ = #
y18   # = . . . . . . . . . . . = #
y19   # = . . . . . . . . . . . = #
y20   # # # # # # D D # # # # # # #
```
(The raised walkway is 1 tile wide, with two one-tile **alcoves** at (12,10) and (10,4).)

- **Arrival:** stairs mats (6,20),(7,20) from 1F's (7,1). **Stairs up** to 3F at (7,1).
- **The central pump** `P` (x 6-8, y 9-11) is decoration: a big brass pump in the middle of the pit, blocked.
- **West catwalk** (x 1) has a **permanent water gap** at (1,9),(1,10): it is a dead end, a visible broken route, no solving it. **East catwalk** (x 13) has two gaps: **GA** at (13,12),(13,13) (state 4) and **GB** at (13,7),(13,8) (state 5).
- **Wheels:** **Blue** at (0,14), stand (1,14), reached by the west catwalk; **Red** at (14,16), stand (13,16), reached by the east catwalk. The log is **reversed**: 'Mind the second pump: Blue, then Red' (wording PROPOSED; the card gives it). Order: Blue first.

| Step | Turn | Var | Tiles that become catwalk | Result |
|---|---|---|---|---|
| start | | 3 (the 1F value) | none | East catwalk walkable only up to (13,14) |
| 4 | **Blue** (when var is 3) | 4 | GA: (13,12), (13,13) | Reach the alcove and **Ivo**; (13,9)-(13,11) |
| 5 | **Red** (when var is 4) | 5, and `FLAG_BEACONMOUTH_GYM_2F_DRAINED` | GB: (13,7), (13,8) | Reach (13,3) and the top catwalk (x 1-13, y 3), the gallery (6..8,2) and the stairs |
| wrong order | | back to 3 | GA and GB back to water | The pump kicks back |

- **Trainers.** **Ivo** (Sailor) in alcove (12,10), `FACE_RIGHT`, sight 1: fights when the player steps on (13,10). **Hobb** (Fisherman) in alcove (10,4), `FACE_DOWN`, sight 1: fights when the player steps on (10,3). Both trainers are on one-tile alcoves beside the 1-wide walkway so the player can never be blocked by one.
- After step 5 the west part of the top catwalk (x 1-6, y 3) and the upper west catwalk (x 1, y 4-8) are open: a good place for a visible Hyper Potion if the author wants a small reward (PROPOSED, not in the card).

#### 3F: the Lamp Room (15 x 19)

Traced from the Palladium Water panel: a winding sand catwalk through a pool, the leader on a cross-shaped platform with the brass lamp behind him.

```
     x: 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
y0    # # # # # # # # # # # # # # #
y1    # # # # # # # # # # # # # # #
y2    # # # # # # # # # # # # # # #
y3    # ~ ~ ~ ~ ~ = = = = = ~ ~ ~ #
y4    # ~ ~ ~ ~ ~ = = = = = ~ ~ ~ #
y5    # ~ ~ ~ ~ ~ = = = = = ~ ~ ~ #
y6    # ~ ~ ~ ~ ~ ~ ~ ~ ~ 1 ~ ~ ~ #
y7    # ~ ~ ~ ~ ~ ~ ~ ~ ~ 1 ~ ~ ~ #
y8    # ~ ~ ~ ~ ~ ~ ~ ~ ~ = ~ ~ ~ #
y9    # ~ ~ ~ ~ ~ ~ ~ ~ ~ = ~ ~ ~ #
y10   # ~ ~ ~ = = = = = = = ~ ~ ~ #
y11   # ~ ~ ~ = ~ ~ ~ ~ ~ ~ ~ ~ ~ #
y12   # ~ ~ ~ = ~ ~ ~ ~ ~ ~ ~ ~ ~ #
y13   # ~ ~ ~ = ~ ~ ~ ~ ~ ~ ~ ~ ~ #
y14   # ~ ~ ~ = = = = = = = = = . #
y15   # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ = # #
y16   # # # # # # # # # # # # = # #
y17   # # # # # # # # # # # # = # #
y18   # # # # # # # # # # # D D # #
```
(Row 14, x 13 is a one-tile alcove for the guide; (13,15) and (13,16) are wall tiles holding the lever.)

- **Arrival** from 2F: stairs mats (11,18),(12,18) (a ladder warp). **Entrance column** x 12 (y 14-17), then the catwalk runs **west along y 14**, **north along x 4**, **east along y 10**, **north along x 10** to a **gap at (10,6),(10,7)**, then the **platform** (x 6-10, y 3-5).
- **Lever** (the 'final sluice', bg_event) on the wall at (13,15), stand (12,15). Pulling it (the wheel the player turned last, in the story) **lowers the pool and raises the platform's causeway**: (10,6) and (10,7) become catwalk. No wrong order here.
- **Brass lamp** (a 2 x 2 decoration, glowing) on the back wall at (7,1)-(8,2), with the four porthole lamps along the wall (x 3, 6, 9, 12 at y 2) as in the Palladium panel.
- **Mizzle** at (8,3) `FACE_DOWN` (leader, talked to; gym-leader script patterned on `data/maps/RustboroCity_Gym/scripts.inc` (without its rematch branch, see CLAUDE.md): intro, `trainerbattle_single`, badge, TM, HM Dive, after-text). The player reaches (8,4) to talk.
- **Guide** at (13,14) `FACE_LEFT` (a Lamplighter apprentice): 'Pull the lever, then mind your feet.' Talks once; heal not offered.
- **Reward flow after the win:** set `FLAG_BADGE09_GET` (through the badge table, `gBadgeFlags[]`, CLAUDE.md), give TM Water Pulse (`FLAG_RECEIVED_TM_WATER_PULSE`) and HM Dive (`FLAG_RECEIVED_HM_DIVE`); the town's NPCs switch to 'After' lines (card); the pool level stays down.

#### Gym build notes

- All three floors are new layouts at 15 wide, inside the size rule (gym 13 to 15 wide, 17 to 23 tall). `(15+15)*(21+14) = 1050`.
- **Painting recipe.** Wall: the Sewer tileset's brick wall with the arched alcove and wall lamp; floor: stone walkway (the light grated floor); `=` catwalk: the steel mesh gantry (vertical and horizontal pieces); `~` water: the clear-water tile with `MB_NORMAL` and collision 1; pipes and drains on the back wall rows y 1-2 (not on 3F where the lamp goes); entrance door mat: any mat metatile in the primary (`gTileset_Building` has one) or a ladder tile as a stairs warp.
- **Metatile ids for `setmetatile`:** note the ids of (a) the blocked water tile and (b) the walkable catwalk/sand tile while painting, and give them to Claude; add the secondary tileset offset 0x200 when writing them in scripts (as in `design/interiors.md`).
- **Do not strip the top 6 bits of a map block** (CLAUDE.md, engine rules): when Claude writes the swap scripts, check how `setmetatile` handles collision and elevation, and use the 'impassable' argument 0 for the open state and 1 for the flooded state.
- The Palladium panel is a **15 x 19 interior with a one-tile border**; the one-tile border is exactly the wall ring in the 3F plan above.

### 6.4 Keeper's Cottage (custom G4-C style, 12 x 9)

**Purpose.** Mizzle's home: his brass logbook, a chest holding **Sea Incense** (after the badge), a PSYDUCK that holds the stamp pad (the 'PSYDUCK stamp' of Scheme 9), and the view of his LAPRAS ferry. Plan:

```
     x0 1 2 3 4 5 6 7 8 9 10 11
y0   #  # # # # # # # # # #  #
y1   B  B . W . . L W . . w  w      B = bookshelf run, L = brass logbook on a stand (bg_event (6,1)), w = chest (item ball (10,2))
y2   B  B . . . . . . . . *  w
y3   .  . . . . . . . . . .  .
y4   .  . . R R R R R R . .  .
y5   .  P . R R f f R R . P  .      f = low table with the stamp pad (bg_event (5,5)); PSYDUCK wanders (8,5)
y6   .  . . R R R R R R . .  .
y7   .  . . . . . . . . . .  .
y8   .  . . . . D D . . . .  .
```
- Objects: **PSYDUCK** at (8,5) `WANDER_AROUND` (ambient Pokémon; 'it is holding a stamp pad and does not know why'), **Sea Incense** item ball at (10,2) (visible only after `FLAG_BADGE09_GET`, hide flag before). Warps: mats (5,8),(6,8) to `Beaconmouth` warp 3 (door (22,31)).
- **LAPRAS** (ambient object `SPECIES(LAPRAS)`) outside at (23,33), in the water behind the cottage; its `Scheme 9` role is in section 7. It is cutscene-only and does not battle (index.md decision).

### 6.5 Goldsworth House (shared layout)

13 x 11, defined in [kingsquay.md](kingsquay.md) section 6.10: mats (5,10),(6,10), Butler (6,3), vase at (6,5),(7,5). **Cousin A = Prescott** (wine snob) at (3,6) `FACE_RIGHT`; **Cousin B = Kip** (owner of a PERSIAN) at (10,6) `FACE_LEFT` with his PERSIAN **'Duchess'** (ambient object `SPECIES(PERSIAN)`, 'Do not pet her') at (9,6). Before and after switch on `FLAG_BEACONMOUTH_SCHEME9_DONE` (text `Goldsworth_Text_PrescottBefore/After`, `KipBefore/After`, in `dialogue/goldsworth.inc`). Outside the door a sign (`Goldsworth_Text_HouseSign`) at (7,14). Goldsworths may swear mildly; nobody else. Warps: mats (5,10),(6,10) to `Beaconmouth` warp 4 (door (11,13)).

### 6.6 Diver's Shed (G4-B, 10 x 8)

The Dive hint ('The old city is a long way down, and nobody tidies it'). Plan G4-B with a **wetsuit rack** (bg_event (6,1)) and a diving-bell prop on the shelf; **Diver** at (5,5) `FACE_LEFT`; **Ferry clerk** (post-game, hidden until `FLAG_SYS_GAME_CLEAR`) at (7,3) `FACE_DOWN`, who opens the R26 ferry rope (`FLAG_BEACONMOUTH_FERRY_ALDERMERE_OPEN`). Warps: mats (3,7),(4,7) to `Beaconmouth` warp 5.

### 6.7 Lamplighters' Lodge (G4-C, 12 x 9)

Local history, the maintenance chief, the **Waterfall hint** ('The back cove is for people who can climb water.'), **Mystic Water** on a shelf after the badge. Plan G4-C: the **Lamplighters' chief** at (8,5) `FACE_LEFT`; a ladder, lens and oil cans as `bg_event`s on the bookshelves (2,1), (3,1); **Mystic Water** item ball at (10,7), hidden until `FLAG_BADGE09_GET`. Warps: mats (5,8),(6,8) to `Beaconmouth` warp 6 (door (14,19)).

### 6.8 Fishing family's house (G4-A) and Artist's house (G4-B)

- **Fishing family (11 x 8).** A grandmother at (5,6) `FACE_UP` who knows every Water-type by name; a father at (8,3) `FACE_UP` who wants his boat back; a boy at (9,5) wandering who wants a Water-type. Warps: mats (2,7),(3,7) to `Beaconmouth` warp 7.
- **Artist (10 x 8).** An **easel** (bg_event (5,3)) and a wall of **crooked lighthouse paintings** (bg_events (2,1), (4,1), (6,1), each saying the lighthouse looks 'slightly different each time'); the **Artist** at (4,4) `FACE_UP`. Warps: mats (3,7),(4,7) to `Beaconmouth` warp 8.

### 6.9 The two coves

- **Rear cove (Waterfall, on the town map, x 44-51, y 20-35).** The pool x 44-50, y 24-32; the **cascade** (waterfall metatiles) at (45,33)-(45,35); the rock ledge x 47-51, y 20-23. The **Cove ranger** at (49,22) `FACE_DOWN` gives a **PP Max** (`FLAG_RECEIVED_PP_MAX_BEACONMOUTH`) ('You climbed it? Then it is yours.'); a visible **Max Revive** at (50,23). Use the vanilla General waterfall pieces (as on Route 119).
- **Underwater cove (Dive at (10,36)).** `Underwater_Beaconmouth`, 20 x 10 (copy of `Underwater_SootopolisCity`), dive connection to (10,36). Visible: **Pearl** x2 at (4,5) and (15,3), **Big Pearl** at (10,7). No encounters (the card lists none). A dive connection and an underwater map are a pair in Porymap.

---

## 7. Scheme 9: staging the invoice (positions)

From the card and [../../troglodyte-arc.md](../../troglodyte-arc.md): **no battle**; all Pokémon; deadpan. The scene triggers when the player steps on any of the three tiles in front of the gym door.

- **Trigger:** three `coord_event`s at **(31,31), (32,31), (33,31)** pointing at one script, `VAR_BEACONMOUTH_SCHEME9` = 0 (elevation 3, walkable; CLAUDE.md rule on cutscenes). Not `ON_TRANSITION`.
- **Before the scene** (setup, in town): the Lamplighter chief says the Keeper had a letter a week ago; an NPC says 'A box arrived by barge. Four hundred of something.'; the Kingsquay dockhand said 'permits'.
- **Actors (all hidden objects until the scene):** **Mr Tallow** (PROPOSED) starts at (37,31) and walks to (35,31); two **clerks** start at (37,30) and (37,32) and walk to (35,30) and (35,32); the **hand-cart** with the box of 400 permits is a small object at (36,31). **Troglodyte** (his 'Work' phase) walks in along the causeway to (30,31). **Mizzle** (the gym leader, hidden object distinct from the 3F one, or the same object moved) comes out of the door (32,30) to (32,31) after the player is auto-walked one tile west to (31,31). **LAPRAS** appears in the water at (36,34).
- **Beats.** 1) Tallow addresses Mizzle: the invoice of Schemes 1 to 8, billed to the last gym. 2) He cannot read it; Troglodyte takes the sheet and **reads the total aloud**, getting quieter with each comma (optional last line item: 'minus four hundred', from the dropped Scheme 3 gag). 3) Nobody has a response. Mizzle's LAPRAS carries the box and cart out to sea (cart object hidden, LAPRAS swims west along y 34 and off). 4) **Mizzle signs for the receipt with a PSYDUCK stamp** (the stamp pad from his cottage): he is a man, so 'he signs'. 5) Tallow thanks him politely and leaves with the clerks (walk east and hide). 6) Troglodyte walks off without a word (he is not fought here). 7) Mizzle: 'Come in, then.' The gym is now open and the scene's var is set to 1.
- **After the scene:** `FLAG_BEACONMOUTH_SCHEME9_DONE`; town NPCs switch to 'After' lines after the **badge** (card); the cousins' lines switch on the flag.
- **Music:** `MUS_ENCOUNTER_SUSPICIOUS` for the arrival, the town track resumes when Tallow leaves.

---

## 8. Door and warp table

`Beaconmouth` outdoor warp events:

| # | Tile | Destination | Dest warp |
|---|---|---|---|
| 0 | (14,25) | `Beaconmouth_PokemonCenter_1F` | 0 |
| 1 | (21,18) | `Beaconmouth_Mart` | 0 |
| 2 | (32,30) | `Beaconmouth_Gym_1F` | 0 |
| 3 | (22,31) | `Beaconmouth_KeepersCottage` | 0 |
| 4 | (11,13) | `Beaconmouth_GoldsworthHouse` | 0 |
| 5 | (7,25) | `Beaconmouth_DiversShed` | 0 |
| 6 | (14,19) | `Beaconmouth_LamplightersLodge` | 0 |
| 7 | (26,14) | `Beaconmouth_FishingFamilyHouse` | 0 |
| 8 | (31,14) | `Beaconmouth_ArtistsHouse` | 0 |
| (dive) | (10,36) | `Underwater_Beaconmouth` (Porymap dive connection) | |

(Follow Porymap's numbering if it differs; interiors below refer to this table.)

| Interior | Tiles | Destination | Dest warp |
|---|---|---|---|
| `Beaconmouth_PokemonCenter_1F` | (6,8),(7,8) | `Beaconmouth` | 0 |
| `Beaconmouth_PokemonCenter_1F` / `_2F` | (1,6) / (1,6) | each other | |
| `Beaconmouth_Mart` | (3,7),(4,7) | `Beaconmouth` | 1 |
| `Beaconmouth_Gym_1F` | (6,20),(7,20) | `Beaconmouth` | 2 |
| `Beaconmouth_Gym_1F` | (7,1) | `Beaconmouth_Gym_2F` | 0 (tile (7,20)) |
| `Beaconmouth_Gym_2F` | (6,20),(7,20) | `Beaconmouth_Gym_1F` | 2 (tile (7,1)) |
| `Beaconmouth_Gym_2F` | (7,1) | `Beaconmouth_Gym_3F` | 0 (tile (11,18)/(12,18)) |
| `Beaconmouth_Gym_3F` | (11,18),(12,18) | `Beaconmouth_Gym_2F` | 2 (tile (7,1)) |
| `Beaconmouth_KeepersCottage` | (5,8),(6,8) | `Beaconmouth` | 3 |
| `Beaconmouth_GoldsworthHouse` | (5,10),(6,10) | `Beaconmouth` | 4 |
| `Beaconmouth_DiversShed` | (3,7),(4,7) | `Beaconmouth` | 5 |
| `Beaconmouth_LamplightersLodge` | (5,8),(6,8) | `Beaconmouth` | 6 |
| `Beaconmouth_FishingFamilyHouse` | (2,7),(3,7) | `Beaconmouth` | 7 |
| `Beaconmouth_ArtistsHouse` | (3,7),(4,7) | `Beaconmouth` | 8 |
| `Underwater_Beaconmouth` | dive surface | `Beaconmouth` (10,36) | |
| Ferry arrival (script) | from `Ferry_Deck` | `Beaconmouth` (15,31) on the pier, facing up | |

Escape warp: `setescapewarp MAP_BEACONMOUTH, 14, 26` (the Center door's outside tile) in the gym floors' `OnTransition`, as the vanilla harbour does.

---

## 9. NPCs and objects (town map 12 visible)

| Object | Tile | Move | Topic |
|---|---|---|---|
| Lamplighter apprentice | (29,26) | `FACE_DOWN` | On the causeway, polishing the same lens forever |
| Dockhand | (15,30) | `FACE_DOWN` | On the pier; the ferry sells tickets to Aldermere after the League |
| Market stall vendor | (19,21) | `FACE_DOWN` | Market stall (berries and snacks), no shop script; Net Ball x3 are an item ball at his stall (20,22) |
| Cove ranger | (49,22) | `FACE_DOWN` | Rear cove (PP Max) |
| Ferry captain (post-game) | (3,31) | `FACE_RIGHT` | Pier at the roped mouth; opens R26 at game clear |
| Wingull on bollard | (16,29) | `LOOK_AROUND` | Ambient |
| Pelipper on pier | (15,29) | `LOOK_AROUND` | Ambient |
| LAPRAS (ambient) | (23,33) | `FACE_DOWN` | The keeper's ferry; never battles |
| `SS_TIDAL` ferry (object) | (15,33) | `FACE_RIGHT` | The moored ferry, as in the vanilla harbours |
| Scene actors (hidden until Scheme 9) | see section 7 | | Tallow, 2 clerks, Troglodyte, Mizzle, cart |

Bg events: town sign (9,28), gate sign (4,38), nameplate (7,14), lighthouse statues (30,30),(35,30), stall signs, Center board, a notice on the Lodge. Heal tile (14,26).

---

## 10. Items and hidden items (positions)

| Item | Where | Gate |
|---|---|---|
| TIDE BADGE, TM Water Pulse, HM Dive | Mizzle, 3F | Beat him |
| Max Revive | Rear cove ledge (50,23), visible | **Waterfall** |
| PP Max | Cove ranger | Waterfall |
| Mystic Water | Lodge shelf (10,7) | After the badge |
| Sea Incense | Keeper's Cottage chest (10,2) | After the badge |
| Pearl x2, Big Pearl | Underwater cove | **Dive** (badge 9) |
| Max Elixir (hidden) | Behind the Mart, (21,14) | None |
| Heart Scale (hidden) | Pier post, (15,30) | None |
| Net Ball x3 | Market stall item ball (20,22) | None |
| Nugget (hidden) | Pier barrel, (16,29) | After the League |

---

## 11. Scripts and events the build needs

- `Beaconmouth_MapScripts`: `ON_TRANSITION` sets `FLAG_VISITED_BEACONMOUTH` and the heal location; hides/shows post-game objects; for the rope at x 1, y 33-35, uses `FLAG_BEACONMOUTH_FERRY_ALDERMERE_OPEN` (set by the ferry captain after `FLAG_SYS_GAME_CLEAR`).
- `coord_event`s (31,31),(32,31),(33,31): Scheme 9 (`VAR_BEACONMOUTH_SCHEME9`).
- Gym floor scripts: `bg_event` wheel scripts with the table in section 6.3 (var checks and `setmetatile` lists), the lever script (3F), a `MAP_SCRIPT_ON_TRANSITION` that re-applies saved drain state, the leader script pattern copied from Rustboro, trainer scripts (`trainerbattle_single`).
- Ferry arrival from Kingsquay: set `FLAG_KINGSQUAY_TALLOW_LEFT` the first time the player reaches Beaconmouth **on foot** (so the ferry route unlocks at Kingsquay) and `FLAG_KINGSQUAY_FERRY_BEACONMOUTH`.

**Flags (not claimed, from the card):** `FLAG_VISITED_BEACONMOUTH`, `FLAG_BADGE09_GET`, `FLAG_BEACONMOUTH_SCHEME9_DONE` (or `VAR_BEACONMOUTH_SCHEME9`, stage 0 to 2), `FLAG_BEACONMOUTH_GYM_1F_DRAINED`, `FLAG_BEACONMOUTH_GYM_2F_DRAINED`, `VAR_BEACONMOUTH_GYM_WATER`, `FLAG_RECEIVED_TM_WATER_PULSE`, `FLAG_RECEIVED_HM_DIVE`, `FLAG_RECEIVED_PP_MAX_BEACONMOUTH`, `FLAG_BEACONMOUTH_FERRY_ALDERMERE_OPEN`, hidden `FLAG_HIDDEN_ITEM_BEACONMOUTH_MAX_ELIXIR`, `_HEART_SCALE`, `_NUGGET`; new (PROPOSED): `FLAG_ITEM_BEACONMOUTH_NET_BALL`, `FLAG_ITEM_BEACONMOUTH_MAX_REVIVE`, `FLAG_ITEM_BEACONMOUTH_MYSTIC_WATER`, `FLAG_ITEM_BEACONMOUTH_SEA_INCENSE`, `FLAG_ITEM_BEACONMOUTH_PEARL_1`, `_PEARL_2`, `_BIG_PEARL`. Trainer flags are the reused Hoenn ids' flags (card). A 2F-only extra var is not needed (the single var runs 0 to 5).

---

## 12. Build checklist (in order)

1. Read flags.md, engine-edits.md; check [../../trainer-roster.md](../../trainer-roster.md) that MIZZLE exists; the four gym trainers are still unbuilt blocks (they need vanilla ids chosen, a later job).
2. Decide the LeoB `dewford` import (shared with Driftsands), and the Sewer (Clear water) import for the gym (Gen 4 Interior pattern); credits and engine-edits in the commit that imports each.
3. Create `Beaconmouth` from a duplicate of a small town (Dewford) with Change Dimensions to 52 x 41, or start empty; trace `Olivine City.png` per section 5; set `MAPSEC_BEACONMOUTH`; delete duplicated heal locations before saving.
4. Add the causeway bridge, the Keeper's Cottage plot, the causeway, the plaza, the lighthouse (stacked-house option), the east cove strip and cascade.
5. Build the town without the gym first: all exteriors and doors; shared Center and Mart; houses from the G4 templates; Goldsworth house door as a sign until the shared layout exists.
6. Build **gym 1F first** (the hardest script): paint the pit, catwalks, islands and nine strip tiles; note the two metatile ids; add the wheel `bg_event`s. Then 2F, then 3F. Test each with `setmetatile` by hand in the debug menu.
7. Build the Scheme 9 hidden objects and the three trigger tiles.
8. Underwater cove, then the cove ledge objects.
9. Warps (section 8) and connections (south R25 offset -54, west R26). R25 and R26 must exist before the connections can be saved.
10. Close and reload Porymap after Claude edits events.
11. Claude wires scripts; dialogue_check on each `scripts.inc`; `make -j4`; test the three wheel orders and the wrong-order reset in mGBA (CLAUDE.md testing notes).
12. Update design docs (`flags.md`, `engine-edits.md`, `gyms.md` if the puzzle changes), `CREDITS.md`; check no ROM or save is staged; commit and push.

---

## 13. Open questions

1. **Lighthouse art.** I recommend the stacked 'tall white house' (4 x 11, no new art). Confirm that, or choose a drawn sprite sheet.
2. **Gym tileset.** Sewer (Clear water) needs an import (and perhaps a Porytiles conversion if it turns out to be triple-layer), a three-colour wheel, and an optional water animation. The no-import fallback is the vanilla Facility tileset. Which one?
3. **R25 comes in over a causeway bridge across the harbour mouth** (so R26's water west of it and the harbour east of it stay connected under the bridge). The card said only 'south edge, left, a gate'. OK?
4. **Weather.** A permanent drizzle on this one map is a gag on MIZZLE's name. Keep or leave sunny?
5. **The 15 x 21, 15 x 21, 15 x 19 gym plans** are mine; the card said about 17 x 26 per floor. I shrank them to the Palladium panel's size and the engine's gym-size rule. Does the author want bigger?
6. **Wheel order.** 1F: Brass, Red, Blue. 2F: Blue, Red. Is a 5-turn memory puzzle with a one-line hint enough, or should 2F have more gaps?
7. **Troglodyte present at the causeway** (card question 5): staged with him, as the card does.
8. **Shared Goldsworth layout and cousin allocation.** The house uses the 13 x 11 layout from kingsquay.md; Briarwick's file defines a 13 x 10 one, and Prescott and Kip are claimed by other cards too (see kingsquay.md open question 3).
9. **Scheme 9 text says 'she signs'** in troglodyte-arc.md; I wrote 'he' (MIZZLE is a man, per the arc file's own note).
