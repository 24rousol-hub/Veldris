# Roads, west group A: R1, R2, R3, R8, R9 (detailed design, PROPOSED, 2026-10-01)

Status: **PROPOSED.** The build brief for the author's Porymap work. It adds tile positions, trainer facings and sight ranges, item spots, edges and offsets to the existing cards: [../../route1.md](../../route1.md), [../../route2.md](../../route2.md) and, for R3, R8 and R9, [../routes-west.md](../routes-west.md) (those cards also hold the wild tables, which this file does **not** repeat: use them unchanged). Dialogue drafts: [../../dialogue/route1.inc](../../dialogue/route1.inc), [route2.inc](../../dialogue/route2.inc), [route3.inc](../../dialogue/route3.inc) (R8 and R9 have none yet). Towns they join: [crestfall.md](crestfall.md), [wendlebury.md](wendlebury.md), [briarwick.md](briarwick.md); Hollowbrook is built ([../../interiors.md](../../interiors.md)). Rules: [../interiors/README.md](../interiors/README.md). Nothing is built; new minor names are marked PROPOSED.

**Reading the coordinates.** `(x, y)` in tiles from the top-left of each road map. Every position is read off the Project Palladium render, so it is right to about one tile; **confirm with Porymap's status bar** before placing an event. Palladium route renders have a 1 px grid, so the map size is `(px - 1) / 17`. Facing is the direction the object looks; **sight** is the trainer's range in tiles in that direction (the Hoenn `trainer_sight_or_berry_tree_id`). Trainer classes and teams are exactly those in the cards; they reuse vanilla Hoenn trainer ids (class, team and level only here).

**What every road shares.** Tilesets `gTileset_General` + `gTileset_Petalburg` (the LeoB ORAS recolour already in the tree, as Hollowbrook): **no import, no new `CREDITS.md` row** except the Project Palladium credit that goes in with the first traced map (naming the files used). Wild grass is the render's tall-grass patches (listed per road); water and ledges as the render. Ledges (the one-way hops) are metatiles with a ledge behaviour: **copy them from `Route101`** rather than painting new ones (the author's own advice in [../../porymap-walkthrough.md](../../porymap-walkthrough.md)). Elevation 3 on walkable ground, collision on trees and water.

**Object limit.** The engine spawns only the objects within about the camera window (`TrySpawnObjectEvents`, `OBJECT_EVENTS_COUNT` 16, `OBJECT_EVENT_TEMPLATES_COUNT` 64 per map). So '15 per map' (the README) is really '15 in view'. The tall roads (R2, R8) hold more than 15 templates in total and stay legal; the longest cluster in any one screen is noted in the open questions.

| Road | Render | Size | Section | Music | Weather |
|---|---|---|---|---|---|
| R1 | `Route 29.png` | 60 x 25 | `MAPSEC_VELDRIS_ROUTE_1` | `MUS_ROUTE101` | sunny |
| R2 | `Route 30.png` | 37 x 59 | `MAPSEC_VELDRIS_ROUTE_2` | `MUS_ROUTE104` | sunny |
| R3 | `Route 31.png` | 46 x 22 | `MAPSEC_VELDRIS_ROUTE_3` | `MUS_PETALBURG_WOODS` | sunny |
| R8 | `Route 32.png` | 28 x 94 | `MAPSEC_ROUTE_107` (renamed ROUTE 8) | `MUS_ROUTE118` | sunny |
| R9 | `Route 35.png` | 28 x 32 | `MAPSEC_ROUTE_108` (renamed ROUTE 9) | `MUS_FORTREE` | sunny |

Size checks: (60 + 15) x (25 + 14) = 2,925; (37 + 15) x (59 + 14) = 3,796; (46 + 15) x (22 + 14) = 2,196; (28 + 15) x (94 + 14) = 4,644; (28 + 15) x (32 + 14) = 1,978; all under 10,240.

---

## R1: Hollowbrook to Crestfall (land, 60 x 25)

### Description and walk-through

**Opening view from the west (leaving Hollowbrook).** You walk out of Hollowbrook's east gap (rows 9 to 10) and the pines open up: a wide, bright meadow, a pale sand path at your feet that fades into grass after a few tiles, and low hop ledges stitching the field into rooms. No building in sight except, far to the north-east, a grey weigh-house roof.

**Opening view from the east (leaving Crestfall).** A pale road runs west out of Crestfall between the pines. At its far end the meadow starts, with the tall grass of the big east field on your left.

**Path shape.** An open meadow, not a corridor. The player is never forced along a line: the three trainers sit on the natural walking line (rows 9 to 13), the ledges add small hops that the player can use or avoid, the tall-grass patches are visible and avoidable, and the north is a wall of pines with one grey building set into it. Gentle, first walk, Normal types, no water, no HM gates. It is the same road the player walks home from after the gym.

**Set pieces and pacing.** (1) The first ledge garden right after Hollowbrook teaches the hop. (2) The grey weigh-house is a landmark you see for 30 tiles before you reach it. (3) The sand rest patch with the SENTRET lookout and the bench is the half-way breath. (4) The surveyors on the pale road are the last thing before Crestfall and set up Scheme 1. About 60 tiles, 40 to 60 seconds of walking without fights, 3 trainers.

### Segments (west to east)

1. **West gate: x 0 to 11, y 6 to 15.** The sand band (x 0 to 7, rows 9 to 11), which becomes a short sand L (x 6 to 8, y 12 to 14, then a pad x 6 to 11, y 13 to 15). Guide, bucket kid, west sign. Pines at x 0 to 3, y 12 to 14. A vertical hop ledge at x 8 (y 9 to 12) plus a ledge at (8 to 10, 12) fences a small yard.
2. **Ledge garden: x 8 to 20, y 5 to 14.** Long tall-grass patch (x 10 to 17, y 9 to 10), short patch (x 16 to 19, y 7 to 8), vertical ledge at x 15 (y 5 to 8) with a ledge row (12 to 15, 8), ledge at (10, 8) and (12 to 13, 12). The Youngster stands here.
3. **The meadow and the weigh-house: x 20 to 31, y 0 to 14.** Open grass; the grey building (x 24 to 29, y 0 to 5) with a sand yard (x 25 to 28, y 5 to 7); a ledge at (24 to 27, 12). The Lass and the walker are here.
4. **The rest patch: x 28 to 37, y 13 to 21.** Vertical ledge at x 28 (y 13 to 16) with a turn at (28 to 29, 16); a sand patch (x 30 to 35, y 17 to 21, spilling to x 29). SENTRET lookout, bench.
5. **The east field: x 32 to 50, y 5 to 20.** The big tall-grass field: x 38 to 45, y 5 to 9; x 32 to 37, y 7 to 9; x 36 to 37, y 10 to 11; x 40 to 41, y 10 to 14; x 44 to 47, y 13 to 15; the long strip x 38 to 53, y 17 to 18; x 40 to 47, y 19 to 20. A ledge row (38 to 43, 16) and a ledge column (43, y 11 to 16). The Farmer stands here. Pines close the north and south.
6. **The pale road: x 50 to 59, y 11 to 12.** The lighter grass band running out of the east edge. Surveyors, the worried local, the east sign.

### Trainers (3; teams from [../../route1.md](../../route1.md))

| Trainer | Team | Tile | Facing | Sight | Why there |
|---|---|---|---|---|---|
| Youngster | LILLIPUP L4 | (10, 7) | down | 3 | north of the long grass patch; sees (10, 8 to 10) as the player steps in. The easy first fight |
| Lass | ZIGZAGOON L4, SKITTY L4 | (23, 10) | left | 3 | in the open meadow; sees (20 to 22, 10), on the row the player walks |
| Farmer | ZIGZAGOON L5, SKITTY L5 | (37, 12) | right | 4 | guarding the east field; sees (38 to 41, 12), the toughest on the road |

### NPCs, items, signs (labels from `route1.inc`, prefix `VeldrisRoute1_Text_`)

| What | Tile | Facing / type | Label |
|---|---|---|---|
| Guide (3 POTIONs once, `FLAG_...GUIDE` planned) | (3, 8) | down | `GuideGive` / `GuideAfter` / `GuideAfterBadge` |
| Bucket kid | (4, 12) | up | `BucketKid` |
| West sign | (6, 8) | bg event | `SignWest` ('WEST: HOLLOWBROOK, EAST: CRESTFALL') |
| Walker with a map | (26, 8) | left | `Walker` |
| Field sign | (22, 8) | bg event | `FieldSign` |
| SENTRET lookout (interactable, Pokémon object) | (33, 18) | down | `SentretLookout` |
| Rest bench | (31 to 32, 17) | bg event | `RestBench` |
| Surveyor A (not a trainer) | (52, 10) | down | `SurveyorA` / `SurveyorAAfter` |
| Surveyor B (not a trainer) | (55, 13) | up | `SurveyorB` / `SurveyorBAfter` |
| Worried local | (50, 13) | up | `LocalWorried` |
| East sign | (49, 10) | bg event | `SignEast` ('Please keep off the crops. They bite') |
| Troglodyte sighting (optional) | (24, 14) | right | `TrogSighting` |

Hidden items: **POTION** at (13, 9) (the long patch) and **REPEL** at (6, 19) (the south-west patch). No visible items. Flags (not claimed): `FLAG_R1_GUIDE_POTIONS`, two `FLAG_R1_ITEM_*`; trainers reuse their ids' flags. After badge 1 the guide, the three trainers and the surveyors use their `AfterBadge` / `After` lines (`FLAG_BADGE01_GET`, no new flag). **Surveyors:** the Scheme 1 foreshadow; they flank the pale road so the player walks between them and sees clipboards (they are not trainers, and they talk, they do not block).

Live objects in the busiest screen (around the west gate): guide, bucket kid, sign: 3. East end: 3 NPCs plus the sign. Fine.

### Visual identity

Bright farm meadow: pale sand path, soft grass, low round trees and the hop ledges. Sunny; no weather effect. `MUS_ROUTE101` (the opening Hoenn route tune, gentle). Landmark silhouettes: the grey flat weigh-house roof (x 24 to 29, y 0 to 5) is the only building on the road; the pale band at the east end is the 'you are almost there' cue. **The weigh-house is scenery** (decision): no interior, a sign on its front (`VeldrisRoute1_Text_FieldSign` or a new line, 'WEIGH-HOUSE. CLOSED FOR THE HARVEST', PROPOSED). The render's gatehouse here has no destination in Veldris (its north exit goes nowhere), so it is dressed as a farm building.

### Connections

| Edge | Neighbour | Opening here | Opening there | Offset (on this map) |
|---|---|---|---|---|
| Left | `Hollowbrook` (east edge) | rows 9 to 11 (sand) | Hollowbrook x 31, rows 8 to 11 walkable (the path is rows 9 to 10) | **0** (rows line up exactly) |
| Right | `Crestfall` (west edge) | rows 11 to 12 (the pale band) | Crestfall x 0, rows 21 to 22 | **-10** (R1's row 11 meets Crestfall's row 21, so Crestfall's top is 10 rows above R1's top) |

**Hollowbrook side.** `data/maps/Hollowbrook/map.json` has `connections: null` today. In Porymap add on Hollowbrook a **Right** connection to `VeldrisRoute1` with **offset 0**; the east-edge tiles at x 31 are walkable for y 8 to 11 (metatiles `1d1`/`1e1` on rows 9 to 10, plain grass `001` on rows 8 and 11, all non-solid). If R1's row 12 at x 0 is a pine (the render has pines at x 0 to 3, y 12 to 14), that edge is just a wall; nothing to change in Hollowbrook. Close or reload Porymap first; Porymap rewrites map JSON on save.

### Build checklist

1. Create `VeldrisRoute1` (60 x 25, section `MAPSEC_VELDRIS_ROUTE_1`), trace `Route 29.png`: pine border, grass, ledges (copy `Route101`'s), tall grass, sand, then the grey building.
2. Connect Left to Hollowbrook (offset 0), Right to Crestfall (offset -10) when it exists.
3. Wild tab: the 12-slot table in [../../route1.md](../../route1.md). 4. Tell Claude to wire the three trainers, NPCs, signs, hidden items. 5. Update `flags.md`, `make -j4`.

**Effort:** easy to medium (a lot of ledges and small grass patches, but no buildings, no interiors).

---

## R2: Crestfall to Wendlebury (land, 37 x 59)

### Description and walk-through

**Opening view from the south (leaving Crestfall).** You come in from the west through a sand lane cut in the pines (R2's west edge, rows 53 to 55) and meet a straight sand road that runs north. Ahead: a long, narrow valley of pines, the sand road a pale ribbon with a hop ledge across it. To the right, tall grass and a small pond.

**Opening view from the north (leaving Wendlebury).** A 3-wide sand road drops south between pines. A blue-roofed farmstead stands to the east.

**Path shape: 'the long way up, the short way down'.** The sand road runs the whole 59 rows, but **five hop ledges cross it**. Going **north** (Crestfall to Wendlebury) the ledges block the sand road, so the player weaves through the grass lanes beside it (a west tall-grass strip, an east grass column). Going **south** (back to Crestfall) the same ledges are shortcuts: hop down and you save a long detour. It is a gentle step up from R1 with more trainers (4) and slightly higher levels (post-gym).

**Set pieces and pacing.** (1) The ledge-and-grass weave at the start (Camper). (2) The pond and the sign at the half-way mark. (3) The big sand bend. (4) The long straight with the ledges. (5) The farmstead at the top and the gap to Wendlebury. About 60 rows, 4 trainers, one guide.

### Segments (south to north)

1. **Crestfall lane: x 0 to 14, y 52 to 58.** Cut a sand lane through the pines on rows 53 to 55 from the west edge to the sand column (x 12 to 14). **Close the render's bottom exit** with pines (the render's column continues to the bottom edge; here it ends in a short sand alcove, y 56 to 58, x 12 to 14, where the guide stands). Dropped clipboard at (12, 54).
2. **First ledge: x 12 to 20, y 43 to 55.** Ledge row (12 to 18, 51). Detour: the grass column (x 19 to 20, y 44 to 51) with tall grass at (19 to 20, 50 to 51) and (15 to 20, 52 to 53). Camper here. Pond (x 21 to 24, y 43 to 47), sign (15, 47), sand band (x 12 to 18, y 43 to 45) and a sand lane (x 16 to 18, y 45 to 51). Farmstead 2 (x 12 to 16, y 40 to 42, door (15, 42)): scenery.
3. **The sand bend: x 8 to 22, y 33 to 44.** A wide sand band (x 8 to 22, y 33 to 35) with a sand spur up to the sign at (20, 30) (x 21 to 22, y 31 to 35); the road continues west and south along x 8 to 10 (y 35 to 44), then east along y 43 to 44. Tall grass (21 to 24, 35 to 37), (17 to 24, 37 to 38), (19 to 22, 40 to 42). Lass here.
4. **The middle: x 6 to 24, y 19 to 33.** Grass lanes and trees; the ledge (8 to 11, 26) (a 1-tile gap at x 12 lets the sand road through); tall grass (17 to 22, 21 to 26), (13 to 16, 27 to 29). Signs (9, 22) and (20, 30). Berry flowers at (13 to 14, 20) and (17 to 18, 31 to 32).
5. **The long straight: x 6 to 14, y 5 to 19.** The sand road (x 10 to 12) with three ledges (10 to 14, 18), (8 to 12, 12), (10 to 12, 4). Detours: tall-grass columns (8 to 9, 15 to 19) and (6 to 7, 7 to 14), and the grass lane (13 to 14, 0 to 5). Tall grass (23 to 26, 15 to 18), (19 to 21, 15 to 16), (21 to 24, 13 to 14). Farmer here, Youngster at the top.
6. **The north farmstead: x 15 to 27, y 0 to 11.** A blue-roofed house (x 22 to 26, y 4 to 6, door (25, 6)) with a sign (21, 6) and a diagonal of berry flowers ((26, 7), (25, 8), (21, 9), (20, 10)). Scenery.
7. **North gap: x 8 to 14, y 0 to 3.** The sand road (x 10 to 12) leaves the top edge into Wendlebury's south lane.

### Trainers (4; teams from [../../route2.md](../../route2.md))

| Trainer | Team | Tile | Facing | Sight | Why there |
|---|---|---|---|---|---|
| Camper | BIDOOF L10, MEOWTH L11 | (20, 47) | down | 3 | at the top of the east grass column, sees (20, 48 to 50) as the player climbs; the toughest, near Crestfall |
| Lass | SKITTY L9, PIDOVE L9 | (16, 38) | up | 3 | sees (16, 35 to 37), the sand bend |
| Farmer | ZIGZAGOON L9, SENTRET L10 | (9, 13) | left | 3 | guards the west grass detour; sees (6 to 8, 13). Hints at the surveyors |
| Youngster | PATRAT L8, LILLIPUP L8 | (14, 8) | left | 3 | near the north end; sees (11 to 13, 8) on the sand road. The easiest |

### NPCs, items, signs (labels from `route2.inc`, prefix `VeldrisRoute2_Text_`)

| What | Tile | Facing / type | Label |
|---|---|---|---|
| Guide (REPEL once, flag planned) | (13, 57) | up | `GuideGive` / `GuideAfter` |
| Surveyor leftover (clipboard) | (12, 54) | bg event | `SurveyorLeftover` |
| Gym fan (ambient) | (9, 40) | right | `FanTalk` |
| Worried local (ambient) | (19, 45) | left | `LocalWorried` |
| Troglodyte sighting (optional) | (11, 23) | up | `TrogSighting` |
| South sign | (12, 53) | bg event | `SignSouth` |
| Mid sign | (15, 47) | bg event | `SignMid` |
| North sign | (13, 2) | bg event | `SignNorth` |

Hidden items: **POTION** at (24, 16) (the east grass patch) and **ANTIDOTE** at (14, 28) (the grass at (13 to 16, 27 to 29)). The render's two extra signs at (9, 22) and (20, 30) are optional decoration (reuse `SignMid` or leave blank). Flags (not claimed): `FLAG_R2_GUIDE_REPEL`, two `FLAG_R2_ITEM_*`. **Both farmsteads are scenery**: locked doors with a name plate (a possible later interior); the card gives them no NPC.

### Visual identity

Farm valley, narrow and green, pine-walled, hop ledges everywhere. Sunny. `MUS_ROUTE104`. Landmark silhouettes: the blue-roofed farmstead at the top right, the pond with its sign at the middle, the sand band, the ledge rows like stripes. Colours: pale sand, bright green, two blue roofs.

### Connections

| Edge | Neighbour | Opening here | Opening there | Offset (on this map) |
|---|---|---|---|---|
| Left | `Crestfall` (east edge) | rows 53 to 55 (new cut) | Crestfall x 47, rows 20 to 22 | **+33** (R2's row 53 meets Crestfall's row 20, so Crestfall's top is 33 rows below R2's top) |
| Up | `Wendlebury` (south edge) | x 10 to 12 | Wendlebury y 28, x 10 to 12 | **0** |

Mirror the connections on the town maps (Crestfall Right, offset -33; Wendlebury Down, offset 0). **Why the west cut:** the Route 30 render is a south-north road with no west opening, so it needs one to reach Crestfall's east edge. The alternative (R2's bottom joined to a Crestfall edge) would put Wendlebury south of Crestfall. See the open questions.

### Build checklist

1. Create `VeldrisRoute2` (37 x 59, `MAPSEC_VELDRIS_ROUTE_2`), trace `Route 30.png`; remove the bottom exit; cut the west lane (rows 53 to 55). 2. Connect Up to Wendlebury (0), Left to Crestfall (+33). 3. Wild tab from [../../route2.md](../../route2.md). 4. Tell Claude to wire trainers, NPCs, signs, hidden items. 5. `flags.md`, `make -j4`.

**Effort:** medium (59 rows, many ledges and grass patches; no interiors).

---

## R3: Crestfall to Briarwick (land, 46 x 22)

### Description and walk-through

**Opening view from the south (leaving Crestfall).** Orange cones across a 3-wide sand stub, a lorry, three workers in hard hats, a board reading 'ROAD CLOSED. RESURFACING BY GOLDSWORTH ROADWAYS'. Before badge 1 you cannot pass. After, the cones are gone: a quiet sand stub opening into a wide wooded meadow.

**Opening view from the west (leaving Briarwick through the east gatehouse).** You step out of a grey gate onto a sand path between pines; to the east the meadow, a pond, and a tall rocky mound with a dark doorway.

**Path shape.** A wooded lane running west to east. From the south stub the player goes north through the meadow to a long sand band, then west along it to the gatehouse. The pond and the mound fill the north; tall grass sits in the lower left and lower right. After badge 1 it is the main road to Briarwick (the other way round is R2, Wendlebury and R8).

**Set pieces and pacing.** (1) The road-works barrier at the very start (before badge 1: the Goldsworth Roadways joke, a foreman who is in no hurry). (2) The pond and the hiker. (3) The ledge hops on the sand band. (4) The Cut-tree nook with a GREAT BALL. (5) The grey gatehouse at the far end. Short card, three trainers, easy.

### Segments (south to north to west)

1. **The Crestfall stub: x 24 to 30, y 14 to 21.** A sand stub (x 26 to 28, y 17 to 21) to the bottom edge. The barrier at y 18, the foreman at (27, 19), the lorry at (30, 19). A hidden ANTIDOTE at (26, 20) in the clearing.
2. **The south meadow: x 16 to 40, y 12 to 20.** Open grass with tall-grass patches left and right: (8 to 15, 13 to 14), (10 to 15, 15 to 16), (12 to 13, 17 to 18), (16 to 17, 17 to 18), (18 to 19, 15 to 16); (34 to 35, 13 to 14), (30 to 37, 17 to 18), (34 to 38, 15 to 16). Ledges (18 to 20, 14) and (22 to 23, 14).
3. **The north meadow and the mound: x 28 to 43, y 0 to 12.** The rocky mound (x 34 to 41, y 0 to 6) with a dark doorway at (37, 6) (scenery, boarded; no warp). Berry flowers at (30, 5), (31, 6), (38, 8), (39, 7). Signs at (33, 6) (optional decoration) and the Cut tree at (40, 8) with a nook (x 41 to 43, y 7 to 9).
4. **The pond: x 18 to 27, y 3 to 8.** An L-shaped pond (x 18 to 23, y 3 to 6 and x 22 to 27, y 5 to 8). Fishing only (the pond is tiny; no Surf slots). Hiker on the south shore.
5. **The sand band: x 6 to 23, y 7 to 11.** The long sand road west: a 3-row band (x 6 to 15, y 7 to 9) widening to (x 15 to 23, y 9 to 11), with a vertical ledge at (15, 7 to 11) and ledge rows (8 to 10, 11) and (12 to 15, 11).
6. **The west gate yard: x 0 to 8, y 5 to 11.** The grey gate building (x 0 to 6, y 5 to 9), **door (3, 9)**, approach tile **(3, 10)** (replace the render's fence row at y 10 with sand and lay a short sand lane along y 10 from x 3 to x 8 joining the road), sign at (9, 6).

### Trainers (3; teams from [../routes-west.md](../routes-west.md))

| Trainer | Team | Tile | Facing | Sight | Why there |
|---|---|---|---|---|---|
| Camper | ODDISH L12, POOCHYENA L12 | (30, 11) | left | 3 | beside the lane north of the stub; sees (27 to 29, 11). 'I sleep under these trees' |
| Bug Catcher | WURMPLE L10, KRICKETOT L11 | (16, 13) | left | 3 | at the east edge of the left grass patch; sees (13 to 15, 13) |
| Youngster | PATRAT L11, PIDOVE L12 | (21, 11) | left | 4 | on the sand band; sees (17 to 20, 11) |

### NPCs, items, signs

Labels from `route3.inc`, prefix `VeldrisRoute3_Text_`.

| What | Tile | Notes |
|---|---|---|
| Barrier board | (27, 18) | impassable object, `RoadworksSign` |
| Cones (2) | (26, 18), (28, 18) | objects, hidden after badge 1 |
| Foreman | (27, 19) facing down | `ForemanBefore`, `ForemanBefore2` |
| Worker on a break | (25, 19) facing right | `WorkerBreak` |
| Third worker | (29, 17) facing left | PROPOSED line, or reuse `WorkerBreak` |
| Lorry | (30, 19) | 'GOLDSWORTH ROADWAYS' (object or bg event) |
| Hiker | (20, 9) facing up | `HikerBefore` / `HikerAfter` |
| Girl with the lost net | (36, 14) wander 1 | `GirlNet` / `GirlNetAfter` |
| Troglodyte sighting (optional) | (24, 13) facing right | `TrogSighting` |
| Signs | (24, 19) `SignCrestfall`; (9, 6) `SignBriarwick` | |
| Cut tree | (40, 8) | `CutTreeHint` |

The barrier board, two cones, three workers and the lorry (7 objects) **are hidden by a map script on load when `FLAG_BADGE01_GET` is set** (the card: no new flag; `FLAG_R3_ROADWORKS_CLEARED` only if it should not rely on the badge). With them gone R3 has about 6 objects. The barrier cluster at the start screen (7 objects) is the busiest; fine. Items: **POTION** visible at (9, 12); **PECHA BERRY** hidden at (17, 6) by the pond; **ANTIDOTE** hidden at (26, 20) in the clearing; **GREAT BALL** visible at (42, 8) in the Cut nook (Cut, badge 1). Flags (not claimed): `FLAG_R3_ITEM_*`, reused trainer flags.

**Gate interior** `Briarwick_R3Gatehouse` is designed in [briarwick.md](briarwick.md) 3.9 (one 9 x 12 interior, door (4, 11) to Briarwick's east gate, door (4, 1) to this map's warp 0). This map has **one warp: 0 at (3, 9), destination `Briarwick_R3Gatehouse` warp 1**, arrive at (3, 10).

### Visual identity

Wooded meadow lane: sand, a small pond, tall rocky mound, round trees, a grey gate building. Sunny. `MUS_PETALBURG_WOODS` (the Hoenn woods tune, calmer than R2's). Landmark silhouettes: the tall rock mound with its dark doorway, the pond, the grey gatehouse at the west end, the road-works cones at the south end.

### Connections

| Edge | Neighbour | Opening here | Opening there | Offset (on this map) |
|---|---|---|---|---|
| Down | `Crestfall` (north edge) | x 26 to 28 | Crestfall y 0, x 33 to 35 | **-7** (R3's x 26 meets Crestfall's x 33, so Crestfall's left edge is 7 columns left of R3's) |
| West gate | `Briarwick_R3Gatehouse` | warp 0 at (3, 9) | - | - |

(Crestfall's mirror: Up, offset +7.)

### Build checklist

1. Create `VeldrisRoute3` (46 x 22, `MAPSEC_VELDRIS_ROUTE_3`), trace `Route 31.png`; cut the lane at the bottom edge (x 26 to 28, already sand in the render) and add the sand lane along y 10. 2. Connect Down to Crestfall (-7). 3. Wild tab and pond fishing from [../routes-west.md](../routes-west.md). 4. Tell Claude: trainers, barrier objects and the on-load hide script, items, signs. 5. `flags.md`, `make -j4`.

**Effort:** easy (small, simple, one gate).

---

## R8: Briarwick to Wendlebury (land with a lake, 28 x 94)

### Description and walk-through

**Opening view from the north (leaving Briarwick).** A grass lane opens onto a quiet pale valley: low rocky shelves on both sides, a sand path threading down, a small pond and a stone doorway off to the west. Somewhere below you can see the glint of a lake.

**Opening view from the south (leaving Wendlebury).** A sand corridor cut through red-brown cliffs leads up to a sand yard with a red-roofed rest house, and beyond it the lake opens on your left.

**Path shape.** A long relaxed descent in four parts: the rocky shelf (north), the winding sand path through grass hollows, the **lake and its pier** (the set piece), and the cliff cutting and rest house at the south. At the lake the road **splits**: the **pier** (a 17-tile boardwalk straight across the water, one fisherman) or the **west bank** (a longer way round through tall grass, more trainers and items). Both rejoin at the south shore. The lake's open water needs Surf (badge 5), so the islets are return-visit rewards. It is the longest road in the west group and the most scenic.

**Set pieces and pacing.** (1) The rocky shelf and the billboard at the start. (2) The grass hollows and the bug trainers. (3) **The pier**: the long boardwalk with a T-branch and a platform. (4) The rest house halfway down the south half. (5) The cliff cutting at the bottom. About 94 rows, 6 trainers, 8 NPCs.

### Segments (north to south)

1. **The Briarwick end: x 0 to 24, y 0 to 11.** Open grass at the top (opening x 13 to 15; plant pines at (12, 0) and (16 to 19, 0) to narrow the render's wide opening; **drop the render's gatehouse building** (x 4 to 10, y 1 to 5) and fill it with pines). Sand (x 10 to 15, y 3 to 5). West strip: sand (x 0 to 3, y 0 to 19), a small pond (x 0 to 3, y 9 to 12), and a **stone doorway** (x 3 to 5, y 14 to 17, door (4, 17); scenery, a roadside spring, no warp). Rock mounds (x 4 to 7, y 9 to 16). Billboard at (15 to 16, 5).
2. **The rocky shelf: x 4 to 24, y 7 to 24.** Rock plateaus (x 14 to 21, y 7 to 12) and (x 16 to 19, y 15 to 20), pines (x 4 to 13, y 6 to 19). The sand path (x 12 to 17, y 11 to 15). Grass at (x 22 to 23, y 6 to 14) as the east lane. Tall grass (x 14 to 15, y 23 to 24), (x 17 to 22, y 21 to 22), (x 22 to 24, y 15 to 20).
3. **The grass hollows: x 4 to 24, y 24 to 40.** A sand path (x 16 to 17, y 25 to 33), a bend west (x 12 to 17, y 33 to 34), then (x 6 to 13, y 35 to 37). Plateau (x 10 to 15, y 27 to 32). Tall grass (x 6 to 9, y 29 to 34), (x 6 to 11, y 33 to 34). Big plateau east (x 18 to 23, y 26 to 40).
4. **The lake: x 8 to 27, y 41 to 70.** Lake from y 41. **North shore** (x 10 to 15, y 41 to 42 tall grass) meets the **pier head at (14 to 15, 43)**. **The pier:** x 14 to 15 (y 43 to 52), a **T-branch** x 10 to 13 (y 49 to 51), then the **platform** at (16 to 17, 53 to 54) and the boardwalk x 16 to 17 (y 55 to 59) to the south shore at y 60. **West bank:** sand (x 4 to 8, y 36 to 46), tall grass (x 4 to 11, y 49 to 59), pines. Rocks in the water at x 20 to 23 (y 41 to 59).
5. **The south shore: x 4 to 20, y 60 to 70.** Fence posts at (12 to 13, 60) and (18 to 19, 60) either side of the pier landing, sand (x 12 to 16, y 60 to 63), then (x 10 to 14, y 63 to 64) and (x 8 to 9, y 64 to 70). Tall grass (x 4 to 9, y 61 to 64). East shore pines (x 18 to 19).
6. **The rest house and the cutting: x 8 to 20, y 70 to 93.** The **red-roofed rest house** (x 13 to 17, y 70 to 74, **door (15, 74)**), the sand yard (x 10 to 17, y 71 to 85), a dark cave mouth at (10, 80) with ledge pieces at (10 to 13, 82) and a rock at (16 to 17, 81 to 82) (all **scenery**, the cave mouth is boarded, no warp), a rock at (10 to 11, 85 to 86). **Cut the exit:** the render ends in cliffs at y 86 to 93, so **replace the rock at x 12 to 14, y 86 to 93 with a 3-wide sand cutting** to the bottom edge.

The sand in the render is a continuous path; **trace it** and keep the grass beside it walkable. I have not verified every junction from the picture alone, so check the walkable line in Porymap as you paint (open question 5).

### Trainers (6; teams from [../routes-west.md](../routes-west.md))

| Trainer | Team | Tile | Facing | Sight | Why there |
|---|---|---|---|---|---|
| Youngster | PIDOVE L12, BUNEARY L13 | (15, 12) | left | 3 | on the sand near the top; sees (12 to 14, 12) |
| Lass | HOPPIP L13, MAREEP L14 | (16, 24) | down | 3 | at the top of the sand lane (x 16 to 17); sees (16, 25 to 27) |
| Camper | KRICKETOT L13, SKIDDO L14 | (11, 35) | left | 3 | on the west bend; sees (8 to 10, 35) |
| Fisherman (lake bank) | POLIWAG L13, MARILL L14 | (6, 48) | up | 3 | on the west bank; sees (6, 45 to 47) |
| Bug Catcher | KAKUNA L13, BURMY L14 | (9, 58) | up | 3 | in the west-bank tall grass; sees (9, 55 to 57) |
| Fisherman (pier) | MAGIKARP L12, WOOPER L13 | (10, 50) | right | 4 | at the end of the T-branch; sees (11 to 14, 50), so the pier route meets exactly one fight |

The first three are on the shared stretch; **the pier route meets only the pier Fisherman, the west bank meets the bank Fisherman and the Bug Catcher.** The pier is the quick road and is also the pretty one; the bank has more items.

### NPCs, items, signs

No dialogue is drafted yet for R8 or R9 beyond the card topics below (write it in the dialogue pass; keep it under 216 px x 2 lines, `dialogue_check.py`).

| What | Tile | Topic |
|---|---|---|
| Surveyor measuring the billboard | (14, 6) facing right | 'GOLDSWORTH ESTATES' foreshadow |
| Boy | (12, 9) facing down | 'Briarwick has the biggest trees' |
| Cyclist | (16, 29), wander 1 | flavour |
| Gym fan heading to Briarwick | (7, 37) facing right | flavour |
| Pier talker (not a trainer) | (16, 53) on the platform, facing down | the lake |
| Girl who lost her hat | (13, 62) facing left | the lake |
| Kid counting passing PIDOVE | (12, 77) facing up | flavour |
| Rest-house keeper | inside the house (see below) | free heal |
| Billboard | (15 to 16, 5), bg event | 'GOLDSWORTH ESTATES: LAKESIDE LIVING. UNITS FROM TWO MILLION. NO LAKE INCLUDED.' |
| Signs | north (12, 6); pier (13, 42); rest house (12, 75); south (13, 84) | 5 signs incl. the billboard |

Items: **POTION** visible at (14, 13); **POKé BALL x3** visible at (17, 26), (5, 34), (9, 64); **TM Double Team** visible at (21, 4) at the north end; **GREAT BALL** visible at (17, 77) near the rest house; **ANTIDOTE** hidden at (12, 36); **ELIXIR** hidden at the pier end (17, 58); **REVIVE** on an islet at (22, 44) (replace the rock) and **RARE CANDY** on a second islet at (23, 63) (Surf, badge 5). Flags (not claimed): `FLAG_R8_ITEM_*`, reused trainer flags, `FLAG_R8_REST_HEAL_USED` (only if the free heal is limited).

### The rest house: `VeldrisRoute8_RestHouse`, 11 x 8 (PROPOSED name)

Gen 4 Interior Secondary, after `Elm's House.png`. An NPC house, **not** a Pokémon Center; the keeper heals the party once per visit (flavour).

- **Back wall (y 1 to 2):** window (1), stove (2 to 3), fridge (4 to 5), kitchen counter (7 to 9, 3), a plant at (10, 2).
- **Floor:** a **bed** at (1 to 2, 4 to 5) (a place to rest), a flower table (5 to 6, 4 to 6) with cushions (4, 5) and (7, 5); rug (4 to 7, 4 to 6).
- **Door mat and warp:** (5, 7), to `VeldrisRoute8` warp 0 at (15, 74); arrive at (15, 75).
- **Object:** **keeper** (name PROPOSED) at (8, 2), behind the counter, facing down. 1 object.

### Visual identity

Lakeside valley: pale stone, red-brown cliffs, blue lake, sand path, warm light. `MUS_ROUTE118` (the river route tune). Landmark silhouettes: the long pier running out across the lake and the red rest-house roof are the two things players will remember. Colours: stone, lake blue, red roof, pine green. Sunny. Water is the General tileset's lake (surf-able; encounters from [../routes-west.md](../routes-west.md)).

### Connections

| Edge | Neighbour | Opening here | Opening there | Offset (on this map) |
|---|---|---|---|---|
| Up | `Briarwick` (south edge) | x 13 to 15 | Briarwick y 39, x 16 to 18 | **-3** (R8's x 13 meets Briarwick's x 16, so Briarwick's left edge is 3 columns left of R8's) |
| Down | `Wendlebury` (north edge) | x 12 to 14 | Wendlebury y 0, x 24 to 26 | **-12** (R8's x 12 meets Wendlebury's x 24, so Wendlebury's left edge is 12 columns left of R8's) |

(Mirrors: Briarwick Down +3, Wendlebury Up +12.) Warp on this map: 0 at (15, 74) to the rest house.

### Build checklist

1. Create `VeldrisRoute8` (28 x 94, section `MAPSEC_ROUTE_107` renamed ROUTE 8), trace `Route 32.png`; drop the north gatehouse; cut the south exit.
2. Paint the lake, the pier, the T-branch, the platform and the south landing last. 3. Rest house (Gen 4 Interior). 4. Connect Up (-3) and Down (-12). 5. Wild tab (grass, Surf, rods) from [../routes-west.md](../routes-west.md). 6. Tell Claude: trainers, NPCs, signs, items. 7. `flags.md`, `make -j4`.

**Effort:** medium (94 rows, but mostly water, pines and rock; one interior).

---

## R9: Briarwick to Mothwood (land, 28 x 32)

### Description and walk-through

**Opening view from the south (leaving Briarwick through its north-east gate).** You step out of the gate arch onto a wide pale-sand avenue between white fences, a flower row far ahead, and a grey gatehouse at the top. A narrow pool lies at your left. It feels like a park, or an estate drive.

**Opening view from the north (leaving Mothwood).** A grey gatehouse behind you; the avenue falls away to the south with the fences leading your eye to the Briarwick gate.

**Path shape.** A tidy parkland avenue, 28 wide and 32 tall, with **two lanes round a central fence run**: an inner lane (x 11 to 15) and an outer lane (x 17 to 18) that rejoin at the top plaza. The only wild grass is a tall strip on the east side. A well-kept road, the mood of an avenue. The road is a **pocket**: no map edges connect; both ends are gates.

**Set pieces and pacing.** (1) The arch at the start (the gate arch you leave through). (2) The pool. (3) The flower rows by the north gate and the gardener. (4) The grey gatehouse at the end, 'Mothwood has no map'. About 30 rows, 4 trainers, a bench and a Cut-tree nook.

### Segments (south to north)

1. **South gate arch: x 11 to 17, y 30 to 31.** Three **arrow-warp** tiles at **(13, 31), (14, 31), (15, 31)** (the render's roof strip at the bottom edge is the arch). Fence rows (4 to 11, 30) and (16 to 24, 30) with the gap at x 12 to 15. A sign at (15, 29). The inner lane starts here.
2. **The pool lane: x 11 to 15, y 17 to 29.** The inner lane between the pool (x 7 to 10, y 22 to 29) and a tall fence (x 16, y 16 to 29). Sand. Bug Catcher near the start.
3. **The plaza: x 5 to 17, y 10 to 21.** Where the lanes join: the west column (x 5 to 9, y 10 to 20) up to the north, a horizontal fence at (5 to 10, 21), a sand plaza east (x 11 to 17, y 10 to 15) with a bench. The Lass and the Youngster here.
4. **The outer lane and the grass strip: x 17 to 23, y 6 to 29.** An outer sand lane (x 17 to 18, y 14 to 29) with the Picnicker; the wild **tall-grass strip (x 20 to 21, y 8 to 23)** and a row (x 12 to 21, y 8 to 9). A Cut-tree nook at (19, 26).
5. **The flower rows: x 4 to 11, y 5 to 9.** Berry flowers at (4, 6), (10, 6), (9, 7), (11, 7), (4, 8) with a sign at (5, 7).
6. **The north gate: x 4 to 9, y 0 to 5.** The grey gatehouse; **door (7, 4)**, approach (7, 5), sand yard (5 to 8, 5 to 6).

### Trainers (4; teams from [../routes-west.md](../routes-west.md))

| Trainer | Team | Tile | Facing | Sight | Why there |
|---|---|---|---|---|---|
| Bug Catcher | LEDYBA L14, KAKUNA L14 | (13, 26) | up | 3 | just inside the arch; sees (13, 23 to 25) |
| Lass | SEWADDLE L15, ODDISH L15 | (8, 18) | right | 3 | the plaza's west side; sees (9 to 11, 18) |
| Picnicker | SPINARAK L15, PARAS L16 | (18, 20) | up | 3 | on the outer lane; sees (18, 17 to 19) |
| Youngster | PINECO L16, NYMBLE L16 | (7, 12) | down | 3 | in the west column; sees (7, 13 to 15) |

### NPCs, items, signs

No dialogue is drafted for R9; the topics are from the card. The gatekeeper's line ('Mothwood has no map. Bring snacks') is `Briarwick_Text_R9Guard` and is spoken in the **Briarwick-side** gatehouse ([briarwick.md](briarwick.md) 3.9), which keeps the card's count; the north gatehouse interior has no NPC.

| What | Tile | Topic |
|---|---|---|
| Gardener watering the flower rows | (5, 7) facing up | flavour |
| Bug-catching kid | (20, 12) facing down | flavour |
| Retired traveller on a bench | (13, 13) | flavour (bench at (13 to 14, 13)) |
| Picnicking couple (2 NPCs) | (11, 25), (12, 25), facing each other | flavour |
| Beekeeper's assistant carrying a hive | (13, 19), wander 2 | foreshadows Briarwick's hives |
| Signs | (5, 7), (15, 29), (14, 9) | 3 signs |

Items: **POTION** visible at (7, 19); **NET BALL x2** visible at (14, 12) and (12, 24); **PECHA BERRY** visible at (21, 6); **HONEY** hidden at (10, 6) in the flower row; **PARALYZE HEAL** hidden at (20, 22) in the grass strip; **SUPER POTION** behind a Cut tree: tree at (19, 26), ball at (20, 26) in a 1 x 2 nook (Cut, badge 1). Pool: fishing only (no Surf slots). Flags (not claimed): `FLAG_R9_ITEM_*`, reused trainer flags.

### The north gate: `VeldrisRoute9_NorthGatehouse` (PROPOSED name; shared with Mothwood)

One interior with two doors, the same 9 x 12 plan as the Briarwick gatehouses ([briarwick.md](briarwick.md) 3.9, Gate Platinum Secondary, credit blloop; no guard here).

- **South warp (4, 11):** to **this map's warp 0 at (7, 4)**. Arrive at (7, 5).
- **North warp (4, 1):** to Mothwood's south-west gatehouse ([../landmarks-west.md](../landmarks-west.md)). That card says the two buildings are one interior seen from both sides, which this is.
- **This map's warps:** **0** at (7, 4) to `VeldrisRoute9_NorthGatehouse` warp 0; **1, 2, 3** at (13, 31), (14, 31), (15, 31) (arrow warps) to `Briarwick_R9Gatehouse` warp 1, arrive (14, 30).

### Visual identity

A well-kept avenue: pale sand, white fences, bright flower rows, one narrow pool, a grey gatehouse at each end. Sunny, the brightest road of the group. `MUS_FORTREE` (continuity with Briarwick, which is where the road comes from). Landmark silhouettes: the long white fence lines and the grey north gatehouse.

### Connections

None by edge. Gates only: warps listed above. The Briarwick side has its own gate map; the north gate leads to Mothwood.

### Build checklist

1. Create `VeldrisRoute9` (28 x 32, `MAPSEC_ROUTE_108` renamed ROUTE 9), trace `Route 35.png`. 2. Paint the arch tiles on the bottom row and set arrow-warp behaviours. 3. Build `VeldrisRoute9_NorthGatehouse` after Gate Platinum is imported (see Briarwick). 4. Wild tab from [../routes-west.md](../routes-west.md). 5. Tell Claude: trainers, NPCs, items, signs. 6. `flags.md`, `make -j4`.

**Effort:** easy (small, tidy, but depends on the gate import and the arrow-warp behaviour).

---

## Summary of edges and offsets (check them together)

| Join | On this map | Offset | On the other map | Offset |
|---|---|---|---|---|
| Hollowbrook (Right) and R1 (Left) | Hollowbrook rows 9 to 11 | 0 | R1 rows 9 to 11 | 0 |
| R1 (Right) and Crestfall (Left) | R1 rows 11 to 12 | -10 | Crestfall rows 21 to 22 | +10 |
| R2 (Left) and Crestfall (Right) | R2 rows 53 to 55 | +33 | Crestfall rows 20 to 22 | -33 |
| R2 (Up) and Wendlebury (Down) | R2 x 10 to 12 | 0 | Wendlebury x 10 to 12 | 0 |
| R3 (Down) and Crestfall (Up) | R3 x 26 to 28 | -7 | Crestfall x 33 to 35 | +7 |
| R8 (Up) and Briarwick (Down) | R8 x 13 to 15 | -3 | Briarwick x 16 to 18 | +3 |
| R8 (Down) and Wendlebury (Up) | R8 x 12 to 14 | -12 | Wendlebury x 24 to 26 | +12 |
| R3 gate, R9 gate | warps only | - | see Briarwick | - |

(Offset rule used: the connected map's top-left relative to this map's top-left, as in Porymap's Connections tab. If Porymap shows the opposite sign on a given edge, flip it; the numbers are the same size.)

---

## Open questions

1. **Compass versus renders (the big one).** The Palladium roads are one-way strips (Route 30 and 32 run south-north, 31 and 29 west-east), but the sketch wants Crestfall to feed Wendlebury to the north-east and Briarwick to the north. I resolved it this way: R1 west-east, R2 enters Crestfall's **east** edge via a **new west cut** at R2's south end (so it climbs north to Wendlebury's south edge), R3 uses Crestfall's **north-east** lane and its own south stub, R8 hangs from Briarwick's south edge down to Wendlebury's **north** edge. Wendlebury's render is **mirrored** so its sea faces east. Confirm all of it; every offset above is built on it.
2. **R1's weigh-house and R2's farmsteads** are scenery with locked doors. Fine, or give them interiors later?
3. **Gate approach.** Every gate is a south-facing door building plus a 9 x 12 interior in Gate Platinum Secondary (a new import, credit blloop); R9's south end is an arrow-warp arch with no building. The player's arrival direction needs a test in mGBA. The alternative is plain edge connections and no gate interiors.
4. **R9's guard** is in the Briarwick-side gate (the card's guard), not the north gate. OK?
5. **R8's sand path.** I read the render's sand as continuous but could not verify every junction between the rocky shelves from the picture alone. Check the walkable line as you trace; if a gap appears, join it with sand rather than moving the plateaus.
6. **Cut-tree rewards on R3 and R9** need badge 1 (Cut). Both roads are reachable earlier only via R3's barrier (R3) or R8 (R9 via Briarwick), so the rewards are return-visit prizes, as the cards say.
7. **Object density.** R3's start screen (barrier board, cones, workers, lorry, sign) is the densest cluster (about 8 objects); R8's lake has 4 NPCs in a 12-row window. Both are under 16 in view.
