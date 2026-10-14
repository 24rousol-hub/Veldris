# Routes, the east (R13 to R17), detailed design

> **Open question (author, 2026-10-01): the Palladium route renders named in this file are NOT decided.** The author doubts that reusing Palladium route images will give a quality hack, so every 'source render' for a road below is a **mood and shape reference only** until the author decides how each road gets built (traced, redrawn or designed fresh). Lengths, edges, trainers, items and encounters stay as written.


Status: **PROPOSED**, written 2026-10-01. Nothing here is built. This adds detail to the road cards in [../routes-east.md](../routes-east.md) (which keep the species, levels, teams, item lists and flags as canon; this file does not change them) and follows the 'Per road' list in [../interiors/README.md](../interiors/README.md). Towns: [hemlock-reach.md](hemlock-reach.md), [primrose-vale.md](primrose-vale.md), [brinecombe.md](brinecombe.md). Landmark: [mirror-isle-detail.md](mirror-isle-detail.md). **Pokémon only**: no real animals, even in names or jokes. Wild tables are not repeated here; use the card's tables. **Check:** every species named in the card was checked against the tree by the card writer; this file adds none.

**Conventions.** `(x,y)` is a tile from the map's top-left corner `(0,0)`, as Porymap shows it. Trainer **sight** is the number of tiles a trainer sees in the facing direction (`trainer_sight_or_berry_tree_id` in `map.json`). Palladium sizes are `(px - 1) / 17` for the gridded renders. Trainer teams are the card's; all reuse vanilla Hoenn ids with `IVs: 0` (CLAUDE.md, author rule). Object limit: **15 live objects per map**.

## 0. Overview, connections and object budgets

| Road | Between | Kind | Size | Source | Section id | Levels | Music (existing Hoenn track) |
|---|---|---|---|---|---|---|---|
| R13 | Waymeet, Hemlock Reach | land | 64 x 23 | Palladium `Route 42.png` | `MAPSEC_ROUTE_120` | 39 to 45 | `MUS_ROUTE113` |
| R14 | Hemlock Reach, Brinecombe | water | 56 x 24 | Palladium `Route 40.png` (shapes only) | `MAPSEC_ROUTE_123` | 45 to 50 | `MUS_ROUTE104` |
| R15 | Primrose Vale, Brinecombe | land | 30 x 54 | Palladium `Route 43.png` | `MAPSEC_ROUTE_124` | 47 to 52 | `MUS_ROUTE119` |
| R16 | Hemlock Reach, Mirror Isle | water | 40 x 60 | vanilla `Route105`, trimmed | `MAPSEC_ROUTE_126` | 44 to 50 | `MUS_ROUTE122` |
| R17 | Mirror Isle, Primrose Vale | water | 56 x 20 | vanilla `Route107`, trimmed | `MAPSEC_ROUTE_127` | 46 to 52 | `MUS_ROUTE104` |

**Connection table** (all offsets are my arithmetic from the planned openings; recompute when the maps exist and check Porymap's preview). For a connection from map A to map B, `offset` is where B's first row (left/right) or first column (up/down) sits in A's coordinates.

| From | Direction | To | Offset | Matching tiles |
|---|---|---|---|---|
| Waymeet | right | R13 | `+7` (R13 row 0 sits at Waymeet row 7; from [waymeet.md](waymeet.md)) | R13 rows 15 to 18 at its west edge meet Waymeet rows 22 to 25 |
| R13 | left | Waymeet | `-7` | |
| R13 | right | Hemlock Reach | `-26` | R13 rows 8 to 12 meet Hemlock rows 34 to 38 |
| Hemlock Reach | left | R13 | `+26` | |
| Hemlock Reach | right | R14 | `+24` | Hemlock rows 30 to 37 meet R14 rows 6 to 13 (sea) |
| R14 | left | Hemlock Reach | `-24` | |
| R14 | right | Brinecombe | `-10` | R14 rows 8 to 20 meet Brinecombe rows 18 to 30 (sea) |
| Brinecombe | left | R14 | `+10` | |
| Brinecombe | up | R15 | `+8` | R15 `x 13 to 15` meet Brinecombe `x 21 to 23` |
| R15 | down | Brinecombe | `-8` | |
| R15 | up | Primrose Vale | `-14` | R15 `x 12 to 15` meet Primrose `x 26 to 29` |
| Primrose Vale | down | R15 | `+14` | |
| Hemlock Reach | up | R16 | `+2` | Hemlock `x 19 to 26` meet R16 `x 17 to 24` (sea) |
| R16 | down | Hemlock Reach | `-2` | |
| R16 | up | Mirror Isle | `+5` | R16 `x 5 to 34` meet the isle's `x 0 to 29` (sea) |
| Mirror Isle | down | R16 | `-5` | |
| Mirror Isle | right | R17 | `+4` | isle rows 9 to 18 meet R17 rows 5 to 14 |
| R17 | left | Mirror Isle | `-4` | |
| R17 | right | Primrose Vale | `-19` | R17 rows 5 to 14 meet Primrose rows 24 to 33 (lake) |
| Primrose Vale | left | R17 | `+19` | |

**Object budgets (the card's sums left out some objects).** A Cut tree, a Strength boulder and a Rock Smash rock are each an object on the map. The card's R13 'object budget 14 of 15' counted only trainers, NPCs and visible items. With a Cut tree, a Strength boulder, a Rock Smash rock and the two hazmat men as separate objects, R13 would need 17 or 18, so it does not fit as written. Section 1 fixes this by turning two visible items into hidden items and folding one NPC into a sign (open question 1). R14 to R17 fit as written.

**Water roads: vocabulary used below.**
- **Surf patch:** the water the player can surf on that carries the water encounter table. Vanilla sea routes paint everything as ocean water; every water tile on these maps is a surf patch unless noted.
- **Shore line:** where sand, rock or planks meet water. A player dismounts from Surf onto a walkable tile next to the water; each islet below has at least one such tile, listed as a dismount tile.
- **Rocks:** the jagged-rock tiles of the Dewford set (collision, drawn in the water). The Palladium Route 40 render shows white swirling pairs of rocks along two lines; they read as whirlpools but **this tree has no whirlpool tile and no whirlpool field move** (checked: no whirlpool behaviour in `include/constants/metatile_behaviors.h`, no field effect, only battle animations use the word). So the pairs are **rock pairs**, solid, not a hazard. A real whirlpool would be a new system (ask first, open question 4).
- **Fishing spots:** the whole map shares one table per rod. A 'spot' is a named place where an NPC or sign points the player; it does not change the table. Rods: Old and Good Rod are given elsewhere (open question 4 of the card), the Super Rod at Brinecombe (PROPOSED).

## 1. R13: Waymeet to Hemlock Reach (land, sketch 13)

### Description and walk-through

A long rocky pass climbing east to the cliffs, with two small ponds, a boundary stone and a lot of people with baskets of herbs. It is the road the apothecaries use to fetch their ingredients. The player leaves Waymeet on warm, open ground, passes a herb bed, walks under two ponds and a long cliff ledge, and arrives at a milestone where two men in white suits are arguing about whose clipboard it is. Hemlock Reach stands as a smudge of steam on the horizon.

- **Opening view from the west:** a sand path between rock and a wall of round trees, a sign, a bench with a pot of tea, and a hiker already looking at the player.
- **Opening view from the east (coming back):** the milestone and a bird keeper's stare; behind the player, the steam of Hemlock.
- **Pacing:** seven trainers in 64 tiles, one every 8 or 9 tiles, one set piece (the milestone argument) and one optional reward spur (the boulder alcove). The toughest trainer is last, near Hemlock.
- **Traces:** Palladium `Route 42.png` is a **1089 x 392 px** render, 64 x 23 tiles. Verified: a gatehouse at the west edge (`x 0 to 4, y 7 to 12`), two ponds, three small dark doorways in the cliff (cave doors to Johto's Mt Mortar), a one-way brown ledge strip, rocks and signs.
- **Two changes to the trace (important):**
  1. **The ponds block the road in the render.** In the picture each pond runs from the cliff to the fence, so the player would need Surf or the cave to pass. Veldris has no Mt Mortar here. Trace pond 1 only down to **row 13** (it is `x 16 to 25, y 7 to 18` in the render) and pond 2 only to **row 13** (it is `x 36 to 45, y 9 to 18`), leaving a 5-tile corridor `y 14 to 18` for the road. Keep the pine rows at `y 19 to 22` as the south wall.
  2. **Drop the west gatehouse.** Waymeet is a town, not a toll booth (the card offers it as an optional rest stop). If kept, it would be a `Gatehouse Secondary` room (see Brinecombe, section 5.4); I recommend dropping it.
- **Tilesets:** `gTileset_General` + `gTileset_Lavaridge` (the same pair as vanilla Route 112, the road to Lavaridge), so the road matches Hemlock Reach's cliffs. No new import.
- **Weather:** `WEATHER_SUNNY`. **Visual identity:** warm grey rock, pale sand, pale green heath, a lot of orange herb beds; a long ridge silhouette in the north; the steam of Hemlock far in the east. Music: `MUS_ROUTE113`.

### Layout, segment by segment

| # | Segment | Tiles | What is there |
|---|---|---|---|
| 1 | **West Gate** | `x 0 to 10, y 8 to 17` | Opening at the west edge on **rows 15 to 18** (the card and [waymeet.md](waymeet.md) agree; the road then rises toward the render's sand patch). The sand path from the render (`x 5 to 15, y 9 to 15`). Sign at `(4,14)`: WAYMEET. A rest bench with a pot of tea at `(6,16)` (bg event, one-time Pecha Berry cure for the party, flavour). Round trees at `x 0 to 4`. West rocks (decor) at `(8,5)`. |
| 2 | **Herb Heath** | `x 11 to 15, y 8 to 16` | A herb bed (decor) at `x 12 to 14, y 10 to 11`. A Cut tree at `(15,9)` closes a nook with a FULL HEAL at `(15,8)`. A small tall-grass patch **G1** at `x 5 to 14, y 15 to 17`. Hidden ANTIDOTE at `(14,12)` in the herb bed. |
| 3 | **Under Pond 1** | `x 16 to 26, y 14 to 18` | Pond 1 above the road (`x 16 to 25, y 7 to 13`, a rock island at `(21,13)`). A fenced railing along the pond's south edge (`y 14`). The road is 5 wide. A Rock Smash rock at `(22,15)` (hides the encounters, no item). |
| 4 | **Middle Heath** | `x 27 to 36, y 8 to 18` | The green meadow between the ponds. Sand patch at `x 30 to 35, y 13 to 14`. Tall-grass patch **G2** at `x 27 to 35, y 15 to 18`. The **boulder alcove** is a 3 x 3 pocket `x 31 to 33, y 9 to 11` entered from the sand at `(32,12)` (the render's dark doorway at `(32,12)` is the spur): a Strength boulder at `(32,11)` just inside; push it north to `(32,10)`, then step round to the TM Brick Break at `(31,9)`. |
| 5 | **Pond 2 and the Ledge** | `x 36 to 48, y 4 to 14` | Pond 2 above the road (`x 36 to 45, y 9 to 13`, a rock island at `(41,13)`). The corridor drifts north between `x 38 and 46`, from `y 14 to 18` to `y 9 to 14`. The north rock band holds a **ledge shelf** `x 44 to 52, y 4 to 7`; one-way ledge tiles at `x 46 to 49, y 8` drop from the shelf to the heath. Round trees along the south edge. |
| 6 | **Boundary Stone** | `x 47 to 56, y 8 to 14` | A **boundary stone** (decor, collision) at `(50,11)`, sign at `(49,12)`: HERE ENDS THE PARISH. THE NEXT IS WORSE. A hidden PP UP at `(50,12)` in front of it. Tall-grass patch **G3** at `x 47 to 56, y 14 to 16`, on the slope just south of the corridor. Hidden ETHER at `(46,12)`. |
| 7 | **East Gate** | `x 55 to 63, y 7 to 14` | Sand. A **milestone** at `(56,10)` with two hazmat men at `(55,9)` and `(57,9)` arguing about whose clipboard it is (Scheme 7 foreshadow). Sign at `(58,11)`: HEMLOCK REACH, CHEMISTS WELCOME. The east edge is open on **rows 8 to 12** and meets Hemlock's quay gap. |

Seven segments, within the card's 4 to 8.

### Trainers (7) and positions

Positions are for the traced render with the changes above; if a tile is blocked in your paint, shift one tile.

| # | Class | Team | Position | Faces, sight | Notes |
|---|---|---|---|---|---|
| 1 | Hiker | Graveler 40, Machoke 40, Rhyhorn 41 | `(9,12)` | down, 4 | West rocks; first met, sees `(9,13)` to `(9,16)` on the road |
| 2 | Aroma Lady | Roselia 41, Gloom 41 | `(13,12)` | down, 4 | Herb bed; leads from a basket; sees `(13,13)` to `(13,16)` |
| 3 | Collector | Koffing 40, Skorupi 41 | `(21,16)` | left, 4 | Under pond 1; labels everything |
| 4 | Picnicker | Skuntank 42, Gligar 41 | `(24,14)` | down, 3 | At the pond's south bank |
| 5 | Ruin Maniac | Graveler 42, Golem 43 | `(52,12)` | left, 3 | Obsessed with the boundary stone |
| 6 | Black Belt | Machoke 43, Gurdurr 44 | `(47,6)` | down, 3 | On the ledge shelf; sees `(47,7)` to `(47,9)` |
| 7 | Bird Keeper | Golbat 44, Gligar 43 | `(59,11)` | left, 4 | Last, near Hemlock; toughest (44). The vanilla **class name 'Bird Keeper'** has a real animal in it; the card uses it, so keep, or rename the class (open question 3) |

### NPCs (2 objects, trimmed from the card's 3)

| Role | Position | Behaviour | Topic |
|---|---|---|---|
| Hazmat man A | `(55,9)` | faces right | The Scheme 7 foreshadow: argues about whose clipboard it is. |
| Hazmat man B | `(57,9)` | faces left | Holds the stamp. (If either is beaten later, Scheme 7 on [Hemlock's Upper Ledge](hemlock-reach.md) carries on.) |
| Herb gatherer (card NPC, dropped as an object) | n/a | Her line moves into the tea bench's bg text, because the object budget is full: 'the best leaves grow where the ground is worst'. | |

### Items

| Item | Where | Gate | Object? |
|---|---|---|---|
| FULL HEAL | `(15,8)` behind the Cut tree `(15,9)` | Cut (badge 1) | ball + tree = 2 |
| TM Brick Break | `(31,9)` in the alcove, boulder `(32,11)` | Strength (badge 4) | ball + boulder = 2 |
| ~~HYPER POTION~~ | `(29,14)` open ground | none | **moved to a hidden item** |
| ~~MAX REPEL~~ | `(6,18)` south-west fork | none | **moved to a hidden item** |
| Hidden PP UP | `(50,12)` | none | bg event |
| Hidden ETHER | `(46,12)` beside pond 2 | none | bg event |
| Hidden ANTIDOTE | `(14,12)` herb bed | none | bg event |
| Hidden HYPER POTION | `(29,14)` | none | bg event |
| Hidden MAX REPEL | `(6,18)` | none | bg event |

Visible objects: 7 trainers + 2 hazmat + 2 (Cut) + 2 (Strength) + 1 Rock Smash rock = **14 of 15**, one spare. Five hidden items use the reserved 0x264 block ([../../flags.md](../../flags.md)).

### Wild encounters (card's tables)

Land table in the three tall-grass patches: **G1** `x 5 to 14, y 15 to 17`, **G2** `x 27 to 35, y 15 to 18`, **G3** `x 47 to 56, y 14 to 16`. Rock Smash table from the rock at `(22,15)`. Pond fishing (Old, Good, Super) from the road along `y 14` under each pond; the two ponds are small and carry **no Surf table** (the card), and a player can still surf on them, which is harmless.

### Gate, flags, effort

- **Gate:** none; reachable by land before any Surf. Cut, Strength and Rock Smash are optional.
- **Flags (not claimed):** `FLAG_R13_SCHEME7_FORESHADOW` (optional), one-shot flags for the FULL HEAL, the TM and the tea bench, trainer flags from reused ids, five hidden-item flags.
- **Build effort: medium.** One 64 x 23 trace with the two pond changes, three grass patches, one small alcove, seven trainers.

## 2. R14: Hemlock Reach to Brinecombe (water, sketch 14 and 17)

### Description and walk-through

Open sea with a reef: two lines of rock pairs mark a sailing lane across a bright, cold bay, with a buoy keeper's islet to the north and a reef to the south-east. Wingull and Pelipper wheel overhead. Surf from badge 5.

- **Opening view from Hemlock (west):** the quay's pier at the player's back, an open lane between two rows of rocks stretching east, a small sandy islet to the north with a hut and a bobbing buoy.
- **Opening view from Brinecombe (east):** the lane runs away to the west; Hemlock's cliffs and steam fill the horizon.
- **Pacing:** six trainers, the first just beyond the pier, the toughest (the Triathlete) just before Brinecombe. The islets give the player three places to stop and the three item pickups.
- **Source and shape:** Palladium `Route 40.png` is **341 x 579 px, 20 x 34 tiles**, a vertical sea. The card proposes rotating it and widening to 56 x 24. **Recommendation: do not rotate; paint R14 directly at 56 x 24 using Route 40's shapes** (a sand islet with one building at the top, two columns of rock pairs, a rocky shore at the left edge) as a style guide, because Porymap cannot rotate a layout and a rotation by hand is the same work as a fresh paint. (56 + 15) x (24 + 14) = 2698.
- **Tilesets:** `gTileset_General` + `gTileset_Dewford` (vanilla Route 107 and 105). **Weather:** `WEATHER_SUNNY`. **Music:** `MUS_ROUTE104`. **Visual identity:** two long parallel dotted lines of grey rocks, a pale sandy islet with a hut and a buoy, very bright water.

### Layout of the water (56 x 24)

| Feature | Tiles | Notes |
|---|---|---|
| Open water | all other tiles | The surf patch, the card's water table. |
| West edge opening | `x 0, y 6 to 13` | Meets Hemlock's east shore. Rocks fill `y 0 to 5` and `y 14 to 23` at the edge so the connection is a clean 8-tile mouth. |
| East edge opening | `x 55, y 8 to 20` | Meets Brinecombe's west shore (13 tiles). |
| **Sailing lane** | centre line `(0,9)` to `(25,11)` to `(55,14)`, about 7 tiles wide | Marked on both sides by **rock pairs**. |
| North rock line (rock pairs, collision) | `(3,4)`, `(7,5)`, `(11,4)`, `(15,5)`, `(19,6)`, `(23,6)`, `(27,7)`, `(31,7)`, `(35,8)`, `(39,9)`, `(43,9)`, `(47,10)`, `(51,10)` | Each is a 2 x 1 pair. |
| South rock line (rock pairs) | `(3,15)`, `(7,15)`, `(11,16)`, `(15,16)`, `(19,17)`, `(23,17)`, `(27,18)`, `(31,18)`, `(35,19)`, `(39,19)`, `(43,20)`, `(47,20)`, `(51,20)` | Same. |
| **Buoy islet (north)** | `x 20 to 31, y 1 to 6` | Sand, a few round trees, a small hut (decor). The Palladium Route 40 sand-and-building shape. **Dismount tile** `(25,7)` (south shore). ETHER at `(26,3)`. |
| **Pier-rock islet (west)** | `x 7 to 9, y 15 to 16` | A rock ledge with a landing tile; the first Sailor stands here. Dismount `(8,14)`. |
| **Middle rock** | `x 29 to 31, y 11 to 13` | A small rock islet on the lane; ELIXIR at `(30,12)`. Dismount `(30,14)`. |
| **Reef islet** | `x 32 to 34, y 15 to 16` | The Fisherman's rock. Dismount `(33,14)`. |
| **East landing** | `x 45 to 47, y 7 to 8` | The second Sailor's rock. Dismount `(46,9)`. |
| **Reef (south-east)** | `x 40 to 44, y 19 to 22`, shallows | MAX REVIVE at `(42,20)`. Dismount: surf next to the shallows; the ball is on a rock tile `(42,20)` reached from `(42,19)`. |

**Shore lines.** West: Hemlock's quay planks at `x 36 to 41, y 35` (in the Hemlock map) end at the water, with R14's first water tile at `(0,9)`. East: Brinecombe's cliff-and-sand shelf at `x 1 to 5` meets the east edge; the water there is open for surfing. Every islet's shore is sand or flat rock on its south side.

**Fishing spots (named, for sign or NPC text):** the end of Hemlock's pier (the fisherman there says Tentacruel gather here), the south shore of the buoy islet `(25,7)`, the reef lip `(42,19)`, and the end of Brinecombe's pier `(1,30)`.

### Trainers (6), positions

All trainers are on rocks or in the water, with sight lines over water.

| # | Class | Team | Position | Faces, sight | Notes |
|---|---|---|---|---|---|
| 1 | Sailor | Pelipper 46, Tentacruel 47 | `(8,15)` on the pier-rock islet | up, 5 | Near Hemlock; sees `(8,10)` to `(8,14)` across the lane |
| 2 | Swimmer (M) | Wailord 47, Starmie 47 | `(24,9)` in the lane | down, 3 | Middle; sees `(24,10)` to `(24,12)` |
| 3 | Swimmer (F) | Starmie 46, Luvdisc 46 | `(26,7)` off the buoy islet | down, 4 | North islet; sees `(26,8)` to `(26,11)` |
| 4 | Fisherman | Qwilfish 46, Gyarados 48 | `(33,15)` on the reef islet | up, 5 | Near the reef; sees `(33,10)` to `(33,14)` |
| 5 | Sailor | Mantine 46, Pelipper 47 | `(46,8)` on the east landing | down, 5 | East; sees `(46,9)` to `(46,13)` |
| 6 | Triathlete | Tentacruel 48, Seadra 48 | `(51,14)` in the lane | left, 4 | Last, near Brinecombe; toughest (48) |

### NPCs, items

| Role | Position | Topic |
|---|---|---|
| Buoy keeper | `(25,3)` on the buoy islet, faces down | The lane is safe 'between the rocks'. |
| Compliance launch (ambient) | far off, `(52,3)` | A Goldsworth boat bobbing; no battle. If no boat sprite exists, drop it (card: Scheme 7 foreshadow, optional). |

| Item | Where | Gate |
|---|---|---|
| ETHER | `(26,3)` buoy islet | Surf |
| ELIXIR | `(30,12)` middle rock | Surf |
| MAX REVIVE | `(42,20)` reef | Surf |
| Hidden PEARL | `(37,21)` sea floor off the reef | Surf |
| Hidden BIG PEARL | under the second reef `(44,21)` | **Dive (badge 9)**, a return trip, PROPOSED. Dive needs an underwater map and none is planned (open question 2). |

**Objects:** 6 trainers + buoy keeper + launch + 3 balls = **11 of 15**.

### Gate, flags, effort

- **Gate:** Surf (badge 5). **Flags:** one-shot item flags, trainer flags (reused), two hidden-item flags. **Build effort:** easy to medium.
- **Question carried from the card:** a shortcut from R14 to R16: the lane's north rock line has no gap to the Hemlock inlet; Hemlock's own north edge is the way. No shortcut is drawn.

## 3. R15: Primrose Vale to Brinecombe (land, sketch 15 and 16)

### Description and walk-through

A woodland and meadow road along a narrow stream, picking up the first petals as it nears Primrose Vale. It feels like a hidden valley because the only way to it is by water: the player gets to Brinecombe by Surf and then walks north.

- **Opening view from Brinecombe (south):** the road climbs out of the cliff slot onto a sand bay with a parasol lady at the gate and a thin line of trees either side; a stream glitters on the left.
- **Opening view from Primrose Vale (north):** the road leaves the garden gate and slopes south through a field of tall grass, with a surveyor and his tripod at the top.
- **Pacing:** seven trainers over 54 rows; a rest hut midway as a breather; an optional boulder spur. The surveyor at the north end is the Scheme 8 foreshadow (a gentler cousin of Route 1's surveyors).
- **Traces:** Palladium `Route 43.png`, **511 x 919 px, 30 x 54 tiles**. In the render: tall trees in a border, a small pool `x 8 to 11, y 13 to 16`, a long stream `x 8 to 11, y 19 to 32`, tall-grass patches in the middle, a gatehouse in the middle-east (`x 18 to 23, y 33 to 38`), a second gatehouse at the south edge (`x 12 to 17, y 50 to 53`), a big brown cliff in the south-west, signs at `(17,4)`, `(18,41)`, `(17,49)`. **Drop the south gatehouse** (the road leaves the map through open ground to Brinecombe's slot); **keep the middle gatehouse as the rest hut.**
- **Tilesets:** `gTileset_General` + `gTileset_Petalburg` (the pair Hollowbrook and Primrose Vale use). **Weather:** `WEATHER_SUNNY`. **Music:** `MUS_ROUTE119`. **Visual identity:** layered green, white petals drifting in the music if not in the sky, small gatehouses, a bouquet in every second hand.

### Layout, south to north (the way most players walk it)

| # | Segment | Tiles | What is there |
|---|---|---|---|
| 1 | **South Gate** | `x 12 to 17, y 45 to 53` | Open ground, no building. The south edge is open on `x 13 to 15`. Sand `x 12 to 17, y 42 to 50`. Sign at `(17,49)`: BRINECOMBE. Parasol Lady at the gate. REVIVE ball at `(13,44)`. |
| 2 | **Sand Bay and ridge** | `x 12 to 22, y 38 to 45` | The sand narrows into the road. Two one-way ledge tiles at `(16,36)` and `(16,38)` (from the render's small brown strips) drop the player south, a shortcut back to Brinecombe. The big brown cliff block is the west wall (`x 0 to 11, y 33 to 54`). |
| 3 | **Rest hut** | `x 18 to 23, y 33 to 38` | The middle gatehouse becomes the rest hut (interior in section 3.3), door `(21,38)`, sign at `(18,41)`: the hut's 'the toll is a kind word'. The Lady stands near it. |
| 4 | **The Stream** | `x 8 to 13, y 13 to 32` | The stream `x 8 to 11, y 19 to 32` (4 wide) and the pool `x 8 to 11, y 13 to 16`. A bank path `x 12 to 13`. Fishing spots, and the pool is the one **Surf patch** (the card's pool table). SUPER POTION at `(12,21)`. Hidden REVIVE at `(12,16)` (pool edge). |
| 5 | **Meadow Grass** | `x 12 to 22, y 7 to 31` | The tall-grass patches: **G1** `x 14 to 21, y 7 to 12`, **G2** `x 17 to 22, y 12 to 20`, **G3** `x 12 to 16, y 26 to 31`. A sand patch `x 18 to 22, y 29 to 33`. Hidden ELIXIR at `(16,8)` in G1. |
| 6 | **Boulder Clearing (spur)** | `x 24 to 28, y 24 to 28` | A path east from `(23,26)`: a Strength boulder at `(25,26)` and a TM Solar Beam ball at `(27,25)` behind it. The PokeFan stands beside the clearing. |
| 7 | **North Gate** | `x 12 to 17, y 0 to 6` | The road narrows. The north edge is open on `x 12 to 15`. Sign at `(17,4)`: PRIMROSE VALE, KEEP TO THE PATHS. The surveyor at `(13,3)` with a tripod and an orange flag, 'only measuring'. A walker with a bouquet at `(14,9)`. Hidden MAX REPEL under a hedge at `(23,10)`. |

### Trainers (7), positions

| # | Class | Team | Position | Faces, sight | Notes |
|---|---|---|---|---|---|
| 1 | Parasol Lady | Floette 47, Whimsicott 48 | `(14,47)` | down, 3 | South gate |
| 2 | Lady | Mawile 49, Granbull 49 | `(19,40)` | left, 3 | Near the hut |
| 3 | Aroma Lady | Roselia 48, Bellossom 49 | `(13,27)` | left, 2 | By the stream |
| 4 | Beauty | Ribombee 48, Swirlix 48 | `(15,23)` | down, 3 | On the path |
| 5 | Picnicker | Cottonee 47, Granbull 48 | `(19,15)` | down, 3 | In the grass (G2) |
| 6 | PokeFan | Dedenne 48, Togetic 49 | `(26,28)` | up, 2 | Beside the boulder clearing |
| 7 | Fisherman | Seaking 48, Quagsire 49 | `(12,14)` | left, 2 | At the pool; toughest (49) |

### NPCs, items, signs

- **NPCs outdoors (2):** surveyor `(13,3)`, walker `(14,9)`. The rest-hut keeper is inside the hut map.
- **Items:** REVIVE `(13,44)`, SUPER POTION `(12,21)`, TM Solar Beam `(27,25)` (Strength). **FULL HEAL on the hut shelf** (inside). **Hidden:** ELIXIR `(16,8)`, MAX REPEL `(23,10)`, REVIVE `(12,16)`.
- **Objects outdoors:** 7 trainers + 2 NPCs + 3 balls + the boulder = **13 of 15**.
- **Signs:** `(17,49)` BRINECOMBE, `(18,41)` the hut, `(17,4)` PRIMROSE VALE.

### 3.3 Rest hut (`Route15_RestHut`)

- **Layout:** 10 x 8, house style. **Tileset:** Gen 4 Interior is enough; if the **`Gatehouse Secondary`** is imported for Brinecombe's Harbour Office ([brinecombe.md](brinecombe.md) 5.4), reuse it here (a counter, a clock, a rug), so the import pays off twice.
- **Plan:** back wall `y 0 to 1`; a short counter `x 2 to 5, y 3` with the keeper behind at `(3,2)`; a shelf (bg event) at `(8,2)` with the FULL HEAL (a one-time pickup); two stools at `(7,5)` and `(8,5)`; a plant `(1,6)`; door mat `(4,7)`.
- **Objects (1):** the **hut keeper** `(3,2)` facing down: 'the toll is a kind word'.
- **Warp:** `(4,7)` to `Route15` warp 0 (tile `(21,38)`).

### Gate, flags, effort

- **Gate:** none on the road, but only reachable after Surf (R14 or R17). Cut and Strength optional.
- **Flags (not claimed):** `FLAG_R15_SCHEME8_FORESHADOW` (optional), the TM and the FULL HEAL one-shots, three hidden-item flags, the hut pickup.
- **Build effort:** medium. One 30 x 54 trace and a small interior.

## 4. R16: Hemlock Reach to Mirror Isle (water, sketch 18 and 19)

### Description and walk-through

A still, cold mere dotted with reed islets and a ruined jetty. Quiet, a bit mournful: this is the 'lake' side of the east. Surf only.

- **Opening view from Hemlock (south):** a narrow channel between two lines of jagged rocks, with the cliff and its steam behind; ahead, a long open mere under a pale sky.
- **Opening view from Mirror Isle (north):** the wooden jetty at the player's back, the whole mere spread out south, a wreck of a jetty to the west.
- **Pacing:** the channel (south) is a corridor so the player cannot miss the first fisherman; the middle is open water with a tuber (an easy trainer) as a breather and a stranded ferry hand; the north is open, with the toughest trainers (a Triathlete, a Fisherman) guarding the jetty.
- **Source:** vanilla `Route105` (`LAYOUT_ROUTE105`, 40 x 80, `gTileset_General` + `gTileset_Dewford`). I read its collision map: it is an open sea with long jagged rock walls running north to south, a pocket island with a cave warp at `(9,20)`, and a sandbar at `x 6 to 9, y 71 to 77`. **Trim to 40 x 60** (delete the top 14 rows and the bottom 6, so the pocket island at old rows 19 to 24 becomes rows 5 to 10), then **delete every copied Hoenn event** (the cave warp at `(9,20)` is `MAP_ISLAND_CAVE`, the Regi puzzle map, eight trainers, the iron ball, two hidden items, and the **dive connection** to `MAP_UNDERWATER_ROUTE105`, which must be removed so the map does not point at an underwater map). Porymap's Duplicate Map copies events but not connections ([../../map-plan.md](../../map-plan.md)). (40 + 15) x (60 + 14) = 4070.
- **Tilesets:** `gTileset_General` + `gTileset_Dewford`. **Weather:** `WEATHER_NONE` (a cool light; `WEATHER_FOG_HORIZONTAL` would suit the mood but hides trainers on open water: do not). **Music:** `MUS_ROUTE122`. **Visual identity:** a long thin channel, then a wide pale mere, reed beds in the north-west, a pile of old piers in the west.

### Layout of the water (40 x 60)

| Feature | Tiles | Notes |
|---|---|---|
| South mouth (channel) | `x 17 to 24, y 52 to 59` | 8 wide, between jagged-rock lines `x 14 to 15` and `x 26 to 27`, running `y 36 to 58`. Meets Hemlock's north inlet. |
| Gaps in the rock lines | `(14 to 15, y 44 to 46)` and `(26 to 27, y 44 to 46)`; `(14 to 15, y 52 to 54)` | 3-tile gaps leading into the side bays. |
| **West bay** | `x 4 to 13, y 40 to 56` | Reed beds (decor, shallow). **Reed islet (west)** `x 6 to 9, y 46 to 49`, ETHER at `(7,47)`, dismount `(7,50)`. **Ruined jetty** `x 3 to 5, y 52 to 53` (decor posts, a dismount spot, a fishing spot). A pilings stub at `x 12 to 13, y 55 to 56` for the first fisherman. |
| **East bay** | `x 28 to 37, y 38 to 54` | **East islet** `x 31 to 34, y 44 to 47`, STAR PIECE at `(32,45)`, dismount `(32,48)`. |
| **The open mere** | `x 5 to 34, y 12 to 35` | All surf patch. A **stranded islet** `x 8 to 11, y 24 to 27` for the ferry hand `(9,25)`. A shallow **reef** (decor) at `x 10 to 13, y 29 to 31` with a hidden HEART SCALE `(11,30)`. The **grounded yacht** (decor, ambient) in the shallows at `x 28 to 33, y 28 to 30`. |
| North rock and reeds | `x 25 to 29, y 8 to 12` | A rock outcrop `(26 to 28, 9 to 11)` with MAX ELIXIR at `(27,10)`, dismount `(27,12)`. A reed bed `x 12 to 25, y 5 to 11` (shallow decor) with a hidden STARDUST at `(12,6)`. |
| **North pier** | `x 19 to 21, y 0 to 3` | The planks continue the isle's jetty (the isle's jetty is `x 14 to 16`, which with the connection offset is R16 `x 19 to 21`). The last Fisherman stands here. |
| North opening | `x 5 to 34, y 0` | All water, matches the whole isle's south edge. |

**Shore lines.** The mere has only islets and the two piers; no continuous shore. Every islet has sand or flat rock on its south side for dismounting. **Fishing spots:** the south pilings stub, the ruined jetty, the stranded islet, the north pier. **Whirlpools:** none (see the vocabulary note); the white rock pairs of the render are not used on this road.

### Trainers (6), positions

| # | Class | Team | Position | Faces, sight | Notes |
|---|---|---|---|---|---|
| 1 | Fisherman | Whiscash 46, Lanturn 46 | `(12,55)` on the pilings stub | right, 5 | Near Hemlock; sees `(13,55)` to `(17,55)` across the channel |
| 2 | Swimmer (M) | Seadra 47, Golduck 47 | `(11,45)` in the west bay | right, 5 | West islet; sees through the gap at `y 45` |
| 3 | Swimmer (F) | Lanturn 47, Quagsire 47 | `(29,46)` in the east bay | left, 5 | East islet; sees through the east gap |
| 4 | Tuber (M) | Poliwhirl 44, Seaking 45 | `(20,34)` | down, 3 | Inner tube, easy, the first in the open mere |
| 5 | Triathlete | Whiscash 48, Politoed 48 | `(22,12)` | down, 4 | North; sees `(22,13)` to `(22,16)` |
| 6 | Fisherman | Seaking 47, Gyarados 48 | `(20,2)` on the north pier | down, 5 | At the jetty, last; toughest (48) |

### NPCs, items

- **NPCs (2):** the ferry hand `(9,25)` on the stranded islet (faces right; asks the way, points north); the grounded yacht (decor, no object).
- **Items:** ETHER `(7,47)`, MAX ELIXIR `(27,10)`, STAR PIECE `(32,45)` (all Surf). **Hidden:** HEART SCALE `(11,30)` (shallow reef), STARDUST `(12,6)` (north shoal).
- **Objects:** 6 trainers + 1 ferry hand + 3 balls = **10 of 15**.

### Gate, flags, effort

- **Gate:** Surf (badge 5). Waterfall (badge 8) has no use on this road (it belongs to Hemlock's inlet and the isle's Falls chamber).
- **Flags (not claimed):** the three item flags, two hidden-item flags, trainer flags from reused ids.
- **Build effort:** easy to medium. A dimension change on a vanilla sea route and a careful event cleanup.
- **Question:** vanilla Route 105 has a Dive route kept under the sea; the connection is removed here, so Dive has no use on R16 (open question 2).

## 5. R17: Mirror Isle to Primrose Vale (water, no sketch number)

### Description and walk-through

A reed-edged channel in the northern mere, leading east to a lakeshore and a sandy pier at Primrose Vale. It is warmer and prettier than R16: lily pads, blossom that drifts out from the gardens every evening, and the smell of the city before the city is in view. Surf only.

- **Opening view from Mirror Isle (west):** the isle's stone landing at the player's back, a wide shallow channel ahead, reed beds above and below, a lily-pad islet to the north-east.
- **Opening view from Primrose Vale (east):** the pier, the sand, and a petal-collector; the channel runs west to the isle's grey shoulder.
- **Pacing:** six trainers in 56 tiles; a short corridor; the toughest, a Beauty on the landing stage, last before the pier.
- **Source:** vanilla `Route107` (`LAYOUT_ROUTE107`, 60 x 20, `gTileset_General` + `gTileset_Dewford`), trimmed to **56 x 20**. I read its layout: a flat strip of open sea with a few rock lines and a few small islets; seven Hoenn swimmers, no items. Delete the copied trainers; its two connections (Dewford left, Route 108 right) are not copied. (56 + 15) x (20 + 14) = 2414.
- **Tilesets:** `gTileset_General` + `gTileset_Dewford`. **Weather:** `WEATHER_NONE`. **Music:** `MUS_ROUTE104`. **Visual identity:** green-gold shallows, lily pads (decor), reed rows, a faint haze of petals.

### Layout of the water (56 x 20)

| Feature | Tiles | Notes |
|---|---|---|
| West opening | `x 0, y 5 to 14` | Meets Mirror Isle's east shore (the isle's rows 9 to 18). Rocks fill `y 0 to 4` and `y 15 to 19` at the edge. |
| East opening | `x 55, y 5 to 14` | Meets Primrose Vale's lake (Primrose rows 24 to 33). |
| North reed bed | `x 4 to 55, y 0 to 3` | Shallow decor reeds with a few gaps. A **dock stub** (planks, decor) at `x 30 to 33, y 1 to 2` for the boatman. |
| South reed bed | `x 4 to 55, y 16 to 19` | Same. The **reed bed (west)** at `x 6 to 12, y 15 to 18` holds a hidden STAR PIECE at `(9,15)`. |
| **Lily-pad islet (west)** | `x 12 to 16, y 3 to 6` | ELIXIR at `(14,4)`; dismount `(14,7)`. |
| **Lily-pad islet (east)** | `x 38 to 42, y 14 to 17` | ETHER at `(40,15)`; dismount `(40,13)`. |
| **Middle rock** | `x 26 to 28, y 9 to 10` | NUGGET at `(27,9)` (an item tile on a rock); dismount `(27,11)`. |
| **Reed islet** | `x 20 to 24, y 16 to 18` | The Fisherman's islet, `(22,16)`. |
| **Landing stage** | `x 49 to 52, y 8 to 10` | Wooden planks (decor) just before the pier, the Beauty's perch `(51,9)`. |
| **Sand spit** | `x 50 to 55, y 1 to 3` | The petal-collector `(53,2)`. |
| Shallows near the pier | `x 45 to 49, y 11 to 13` | Hidden PEARL at `(47,12)`. |

**Shore lines.** None continuous; the sand spit and the landing stage, and Primrose's own sand shore beyond the east edge. **Fishing spots:** the dock stub, the reed islet, the landing stage, the end of Primrose's pier `(2,29)` in the Primrose map. **Whirlpools:** none.

### Trainers (6), positions

| # | Class | Team | Position | Faces, sight | Notes |
|---|---|---|---|---|---|
| 1 | Swimmer (F) | Azumarill 48, Luvdisc 48 | `(6,9)` | right, 4 | Near Mirror Isle; sees `(7,9)` to `(10,9)` |
| 2 | Swimmer (M) | Seaking 48, Golduck 49 | `(24,8)` | down, 3 | Middle |
| 3 | Fisherman | Qwilfish 47, Whiscash 49 | `(22,16)` on the reed islet | up, 5 | Sees `(22,11)` to `(22,15)` |
| 4 | Tuber (F) | Slowbro 49, Azumarill 49 | `(34,11)` | left, 3 | Inner tube |
| 5 | Triathlete | Lumineon 50, Starmie 50 | `(46,9)` | left, 4 | Near the pier |
| 6 | Beauty | Ribombee 50, Azumarill 51 | `(51,9)` on the landing stage | left, 5 | On the stage before the pier, last; toughest (51) |

### NPCs, items

- **NPCs (2):** the **boatman** `(31,2)` on the dock stub, faces down (rows between the isle and the pier at dawn and offers no ride); the **petal-collector** `(53,2)` on the sand spit, faces down (the blossom drifts out from the gardens every evening). Optional (card): a surveyor's rowing boat on the sand spit as a Scheme 8 foreshadow.
- **Items:** ELIXIR `(14,4)`, ETHER `(40,15)`, NUGGET `(27,9)` (Surf). **Hidden:** PEARL `(47,12)`, STAR PIECE `(9,15)`.
- **Objects:** 6 trainers + 2 NPCs + 3 balls = **11 of 15**.

### Gate, flags, effort

- **Gate:** Surf (badge 5). **Flags (not claimed):** the three item flags, two hidden-item flags, trainer flags (reused). **Build effort:** easy.
- **Question:** R17 has no sketch number (a blue line only). If the author wants it unnumbered, name it a waterway in-game instead of ROUTE 17.

## 6. Build order for the east group (the author, then Claude)

1. Build **Brinecombe** first (medium, tests R14 and R15 on a small map), then **R15** and **R14**.
2. **Hemlock Reach**, then **R13** and **R16**.
3. **Primrose Vale**, then **R17** and **Mirror Isle**.
4. After each map: Claude wires connections (this file's table), warps, objects, trainers and flags, then updates [../../flags.md](../../flags.md) and `CREDITS.md`.
5. Credit Project Palladium by file name (`Route 42.png`, `Route 40.png`, `Route 43.png`) in the commit of the first trace that uses each.

## 7. Open questions (east routes)

1. **R13 object budget.** To stay under 15 live objects I moved HYPER POTION and MAX REPEL to hidden items and merged the herb gatherer into a sign. Accept, or drop a trainer instead?
2. **Dive and the underwater map.** Two hidden items (R14 BIG PEARL, Brinecombe BIG PEARL) need Dive and so an underwater map each. None exists. Drop them, or build one tiny shared underwater pocket (ask first).
3. **'Bird Keeper' class name.** It is a vanilla trainer class and the card uses it, but it contains a real animal word. Keep, or rename the class (a class rename touches `src/battle_main.c` and the class name table, so it would be a small engine edit; log it in `engine-edits.md` if done)?
4. **Whirlpools.** Not in this tree. A whirlpool hazard or field move would be a new system. The renders' white rock pairs are used as rock pairs instead.
5. **Waymeet connection.** Resolved: [waymeet.md](waymeet.md) already fixes it (R13 rows 15 to 18 meet Waymeet rows 22 to 25, offset `+7`); this file uses those numbers. Note Waymeet calls the map `VeldrisRoute13`; use one name for the map folder when it is built.
6. **Palladium traces need credits** in the commit that first uses each file.
7. **R13 grass patch G3** on the east ridge slope is my addition so the card's 12-slot table has enough grass; move it freely.
