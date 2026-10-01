# Detailed road design: west group B (R4, R5, R6, R7)

> **Open question (author, 2026-10-01): the Palladium route renders named in this file are NOT decided.** The author doubts that reusing Palladium route images will give a quality hack, so every 'source render' for a road below is a **mood and shape reference only** until the author decides how each road gets built (traced, redrawn or designed fresh). Lengths, edges, trainers, items and encounters stay as written.


Status: **PROPOSED** (written 2026-10-01). Nothing here is built. This is the brief the author builds from in Porymap, and the brief Claude uses for the events, trainers and dialogue afterwards. It adds detail to the existing cards in [../routes-west.md](../routes-west.md) and does not change them: species, levels, trainer lists, items and flags stay as the cards have them. Where I had to choose, the choice is marked **PROPOSED** (or **FIX** when an existing card contradicts the render). Rules and rates: [../README.md](../README.md), [../interiors/README.md](../interiors/README.md). Towns: [gloomsby.md](gloomsby.md), [smeltham.md](smeltham.md), [hoarfell.md](hoarfell.md). Landmark at the end of R7: [landmarks-west-detail.md](landmarks-west-detail.md).

How to read coordinates: every `(x, y)` is a tile on the **Palladium render as it is drawn** (x from the left, y from the top, 0-based). Tile size is `(px - 1) / 17` for these gridded images, which I checked by pixel size: Route 36 is 52 x 22, Route 43 is 30 x 54, Route 42 is 64 x 23, Route 46 is 22 x 36. I read every position by eye from the image, so it can be **1 or 2 tiles off**. Use them as 'about here'. The renders are used **unmirrored** for all four roads (see the edge table: this keeps every road's gatehouse and open end where the picture has them).

Credit: the Project Palladium team goes in `CREDITS.md` in the commit that traces the first of these maps (one row for the whole team, see [../../map-plan.md](../../map-plan.md)). Every road below also needs its section row (`region_map_sections.json` names are already planned: R4 `MAPSEC_ROUTE_101`, R5 `MAPSEC_ROUTE_102`, R6 `MAPSEC_ROUTE_103`, R7 `MAPSEC_ROUTE_105`, renamed to show ROUTE 4 to ROUTE 7).

## Summary table

| Road | Map name (PROPOSED) | Render | Size | Edges | Enemies at | Weather | Music (existing Hoenn track, PROPOSED) |
|---|---|---|---|---|---|---|---|
| R4 | `Route4` | `Route 36.png` | 52 x 22 | east edge to Briarwick, west gatehouse to Gloomsby | 17 to 21 | fog | `MUS_ROUTE113` (the ash road, eerie) |
| R5 | `Route5` | `Route 43.png` | 30 x 54 | south gatehouse to Gloomsby, north edge to Smeltham | 22 to 27 | none, a smoke column far north | `MUS_ROUTE119` |
| R6 | `Route6` | `Route 42.png` (alone, not stitched) | 64 x 23 | west edge to Smeltham, east edge to Hoarfell, a door to R7 | 28 to 33 | none, then snow flurries in the east third (optional) | `MUS_ROUTE120` |
| R7 | `Route7` | `Route 46.png` | 22 x 36 | a door from R6, the mine door at the top | 29 to 34 | none | `MUS_ROUTE104` (calm) |

Size checks (all under `(w + 15) * (h + 14) <= 10240`): R4 (52+15)*(22+14) = 2,412; R5 (30+15)*(54+14) = 3,060; R6 (64+15)*(23+14) = 2,923; R7 (22+15)*(36+14) = 1,850.

## Edge truth table (this fixes a contradiction in the road cards)

The road cards say 'west end meets Briarwick's west edge', which cannot be an edge connection (a west edge joins an **east** edge). I worked out the one consistent reading, and it matches where each render has its gatehouses:

| Join | Town side | Road side | Kind |
|---|---|---|---|
| Briarwick to R4 | Briarwick **west** edge (gravel path, top-left of town) | R4 **east** edge, sand band at y 10 to 12 | edge connection, offset: Briarwick's gravel row minus 10 |
| R4 to Gloomsby | Gloomsby **west** gatehouse | R4 **west** gatehouse (the render's own, x 0 to 5, y 6 to 10) | one gate interior, two doors |
| Gloomsby to R5 | Gloomsby **east** gatehouse | R5 **south** gatehouse (the render's own, x 12 to 17, y 51 to 53) | one gate interior, two doors |
| R5 to Smeltham | Smeltham **south** edge (3-wide gap cut through the bottom cliff, x 10 to 12) | R5 **north** edge, lane at x 12 to 15, y 0 | edge connection, offset: Smeltham's x minus R5's x for the same lane tile |
| Smeltham to R6 | Smeltham **east** edge (lane at y 13 to 15 of the render, the widened map shifts it, see [smeltham.md](smeltham.md)) | R6 **west** edge, sand at y 8 to 15 | edge connection (the render's west gatehouse is dropped) |
| R6 to Hoarfell | Hoarfell **west** edge (a 3-wide gap the author cuts in the rock wall at y 30 to 32, see [hoarfell.md](hoarfell.md)) | R6 **east** edge, sand at y 7 to 10 | edge connection |
| R6 to R7 | R6 cave door at (14, 8) | R7 south end, sand path at (10, 33) | one warp pair (a door), no edge |

**FIX against the cards:** (1) R4's Gloomsby end is the **west** end, so the card's 'fog in the east third' becomes the **west** third and the card's 'west' items (Briarwick end) are on the map's **east** side. The translation is written into R4 below. (2) R5's Gloomsby end is the **south** end (the card said the Smeltham end is south and suggested mirroring). Walking from Gloomsby you go **north** up R5, which also keeps the smoke on the far side, at Smeltham. If the author would rather mirror, flip every y below (`y' = 53 - y`) and swap the town ends.

All gate interiors are described in [gloomsby.md](gloomsby.md) (the shared interiors `Gloomsby_WestGate`, `Gloomsby_EastGate`). The roads only hold the outside half of each gate: a building on the road map with one door, whose warp goes to the gate interior.

---

## R4: Briarwick to Gloomsby (land, sketch 4)

**Map `Route4`, 52 x 22. Render `Route 36.png`, unmirrored. Wild levels 17 to 21.**

### Description and walk-through

You leave Briarwick by the gravel path on its west side and step onto a wide, damp meadow road. The road looks tidy at first (a sand band running west between two thick walls of pines), then it dips into a green hollow where the grass is wetter, the colours go grey-green and the **fog** rolls in. By the middle of the road you can hear nothing but your own steps and a far-off hooting. The one real set piece is a **film van** parked on the lower road with cables snaking out of its door (the Scheme 3 foreshadow, played straight for a laugh). The road ends at a grey gatehouse with a lit window: the **west gate**, and beyond it Gloomsby.

Mood: quiet, polite, a little spooky and a little silly (a girl selling 'authentic ghost stories for a coin' on a road where the fog does the work for free). Time of day: late afternoon, never full sun (use the header weather, not a palette change).

### Layout, segment by segment (walking from Briarwick, east to west)

1. **Briarwick edge, x 42 to 51.** The sand band (y 10 to 12) runs in off the east edge. North of it a tree wall (y 0 to 7), south of it a tree wall (y 13 to 21), both 2 deep. Sign at (47, 9): `ROUTE 4. WEST: GLOOMSBY. EAST: BRIARWICK`. Trainer 1 stands here.
2. **Berry row, x 32 to 41.** The sand band stays 3 wide. The render's **red-berry row** is the row of red flowers at x 32 to 41, y 8 to 9 (just north of the sand). It is a real set of flowers tiles (use the red flower tile of the General set), not berry trees. A tall-grass patch sits at x 28 to 33, y 6 to 7 above it. Hidden AWAKENING at (36, 8). The sand spur at x 36 to 39, y 13 to 15 leads south to the lodge (segment 7).
3. **Meadow crossing, x 20 to 31, y 8 to 16.** The render has no road here (open grass). **PROPOSED:** paint a worn dirt path along y 11 from (31, 11) to (20, 11), 2 tiles wide (y 11 and 12), so the walk stays a road. The meadow is wide on purpose (9 rows) so the fog reads as a place. Trainer 3 stands in it. Add the optional marsh pond here (see Water).
4. **The lower road, x 8 to 19, y 16 to 17.** The path bends south-west at x 19 and becomes the sand band the render has at y 16 to 17 (px 140 to 335). Two tree columns (x 12 to 13 at y 9 to 14, a stand of 5 pines) form a short corridor to the north: this is the **grass nook** with the small tall-grass patch at x 12 to 15, y 14 to 15. The **film van** parks here (x 11 to 13, y 17 to 19, south of the sand: use `OBJ_EVENT_GFX_TRUCK`, a 3 x 3 sprite, as the van). The film assistant stands at (14, 16).
5. **The climb to the gate, x 8 to 10, y 9 to 17.** The sand turns north along x 8 to 10 (3 wide) and runs up the west side of the pine stand to the gate. Sign at (9, 7) at the top of the climb: `GLOOMSBY 1 KM. FOG BEYOND THIS POINT, FREE OF CHARGE.` (the card's east-end sign, moved to the Gloomsby end by the FIX above).
6. **The west gate, x 0 to 5, y 6 to 10.** The render's gatehouse. Door on the south side at (3, 10), arrival tile (3, 11): the sand there is the 'ssss' strip at y 10 in the render, so move the door to y 10 and the doormat row to y 11, or keep the door at (3, 9) with the sand at y 10 (whichever the building piece gives). Pass-through: no NPC on the road side, the guard is inside (see [gloomsby.md](gloomsby.md)).
7. **The Marshkeeper's Lodge, x 34 to 39, y 16 to 20 (side spur, dead end).** The render's south gatehouse. It has no door facing the spur in the picture. **PROPOSED:** keep the building, put its door on the **south** face at (37, 20) and paint a 1-wide sand path from the spur around its east wall (x 40, y 14 to 21) so the player can reach the arrival tile (37, 21). That is 8 new path tiles and 1 tree removed at (40, 15). Lodge interior in the Interiors section below.
8. **The north stub, x 14 to 19, y 0 to 3.** The render has a sand stub from the top edge. **PROPOSED:** close it at the top with a tree and use it as a 6 x 4 clearing with one trainer and one item (it is reached by a gap in the tree wall at (16, 5), 1 tile wide, off the lower road at x 14 to 19). It is the 'ledge' item of the card (the render has no ledge).

### Water (optional, PROPOSED)

The render has no pond. If the author wants fishing: a **marsh pond** x 22 to 26, y 15 to 17 (5 x 3) in the meadow's south part, with a 1-tile islet at (24, 16) holding the ELIXIR (Surf, badge 5). Old Rod and Good Rod and Super Rod tables are in the card; the card also says 'no Surf slots required', so give the pond Surf slots only if it is added: reuse the R5 long pond Surf table from the card. If the pond is left out, drop the ELIXIR from the table or move it to a Cut tree (Cut, badge 1) at the Lodge spur.

### Wild Pokémon (from the card, unchanged)

12 land slots, 20/20/10/10/10/10/5/5/4/4/1/1: ODDISH 17 to 18, HOOTHOOT 17 to 18, ZUBAT 18, VENIPEDE 18 to 19, SPINARAK 18 to 19, STUNKY 19, PUMPKABOO 19 to 20, DUSKULL 20, GASTLY 19 to 20, MURKROW 20 to 21, PHANTUMP 21, MISDREAVUS 21. Tall grass at: x 28 to 33 y 6 to 7; x 12 to 15 y 14 to 15; **PROPOSED additions** (the render has too little grass for a road with 5 trainers): x 24 to 29, y 13 to 15 and x 4 to 7, y 12 to 14 (the bit left of the climb). Pond slots (if built): Old Rod MAGIKARP 12 (70), POLIWAG 12 (30); Good Rod POLIWAG 17 (60), WOOPER 17 (20), BARBOACH 17 (20); Super Rod WOOPER 20 (40), BARBOACH 20 (40), POLIWAG 20 (15), CORPHISH 20 (4), SKRELP 20 (1).

### Trainers (5, positions PROPOSED)

| # | Class and team | Stands at | Faces | Sight | Why there |
|---|---|---|---|---|---|
| 1 | Bug Catcher: VENIPEDE 17, SPINARAK 18 | (43, 8), on the north verge | south | 3 | sees the sand band as you step in from Briarwick: the first fight is 4 steps from the town |
| 2 | Picnicker: ODDISH 18, HOOTHOOT 18 | (36, 15), on the lodge spur | north | 4 | spots anyone passing the berry row (x 36), and guards the lodge path |
| 3 | Hex Maniac: GASTLY 19, DUSKULL 20 | (25, 13), in the meadow | north | 3 | the fog fight: she steps out of nowhere when you cross the dirt path at (25, 11) or (25, 12) |
| 4 | Bird Keeper: HOOTHOOT 19, MURKROW 20 | (14, 13), at the top of the grass nook | south | 3 | watches the nook's grass and the lower road at (14, 16) |
| 5 | Youngster: STUNKY 19, KOFFING 20 | (16, 3), in the north stub | south | 4 | optional: a clearing that rewards the curious (the hidden REPEL is in his clearing) |

Trainers 1 to 4 are on the main path, 5 is optional.

### NPCs (6 from the card, positions PROPOSED)

| NPC | Position | Notes |
|---|---|---|
| Marshkeeper | inside the lodge, (5, 3) | gives the GREAT BALL, fog lore |
| Lamp-lighter | (20, 10), the meadow's west edge | warns of the fog ahead, optional Troglodyte sighting ('a boy in a good coat demanded to know why fog is allowed') |
| Film assistant | (14, 16), by the van | clipboard, bedsheet over one arm; Scheme 3 foreshadow. The van's rear door is a `bg_event` at (12, 20): a script sheet reading 'Scene 14: SHEETED GUESTS ENTER. SPOOKY.' |
| Sleepy traveller | (27, 9), on a flat stone north of the dirt path | asleep, face-down |
| Ghost-story girl | (33, 12), next to the first sand tile | sells a joke 'story' for a coin (no real shop, a Yes/No and a tiny line) |
| Gym fan | (46, 10), near Briarwick | heading to Gloomsby, is cheerful about Sanzuford |

Signs (3, plus one bonus): (47, 9) Briarwick end, (21, 9) mid-road, (9, 7) Gloomsby end. The render's top sign at (17, 1) sits in the north stub: use it there for 'HIDDEN CLEARING. PLEASE ADMIRE QUIETLY'. Signs are `bg_event`s and cost no objects.

**Object count.** 5 trainers + 6 NPCs + 2 item balls (POTION, TM Rest) = 13 objects, which fits the limit of 15 with room for the van (1 object) and the lamp-lighter's lamp if the author wants one. Every other item is hidden (a `bg_event`) or a gift, so it costs nothing.

### Items

Visible items use up objects, so most are hidden or `bg_event`.

| Item | Where (about) | Kind | Gate |
|---|---|---|---|
| POTION | (49, 11), just inside the Briarwick edge | ball | none |
| TM Rest | (30, 14), the meadow's south-east corner | ball | none |
| REPEL | (16, 2), the north stub | hidden | none (card 'ledge') |
| AWAKENING | (36, 8), the berry row | hidden | none |
| MAX REPEL | (15, 17), by the van | hidden | none (card 'near the van') |
| GREAT BALL | from the Marshkeeper | gift | none |
| ELIXIR | the pond islet (24, 16) | ball | Surf (badge 5) |

### Interiors on this road

- **Marshkeeper's Lodge** (`Route4_MarshkeepersLodge`): 11 x 8, tileset `gTileset_Building` plus **Gen 4 Interior Secondary** (house style, rule 1), the Hollowbrook neighbour's-house kit. Exit mat (2, 7). Kitchen block at the top left (copy blocks x 0 to 3, y 1 to 2), bookshelf at (7, 1) to (8, 2), a **pair of tall lamps** against the right wall (use the plant blocks at (10, 4) to (10, 6)), a low table with cushions (the TV table kit at x 5 to 8, y 4 to 6 repainted as a table with no TV). The Marshkeeper stands at (5, 3) facing south. Warps: 1 (the mat). Palladium: `Elm's House.png` for the proportions. A reading nook (cushion at (9, 6)) is the 'fog lore' spot: a `bg_event` bookshelf.
- **West gate** shared with Gloomsby: see [gloomsby.md](gloomsby.md). On R4 the outside half is the render's gatehouse. Warp from R4: tile (3, 10) goes to `Gloomsby_WestGate` warp 2 (the right door pair).

### Warp table (R4)

| Map | Tile | Destination |
|---|---|---|
| `Route4` | (3, 10), the gate door | `Gloomsby_WestGate` warp 2 (the right door pair) |
| `Route4` | (37, 20), the lodge door | `Route4_MarshkeepersLodge` warp 0 |
| `Route4_MarshkeepersLodge` | (2, 7), exit mat | `Route4` warp 1, lands at (37, 21) |
| `Gloomsby_WestGate` | the right door pair (12 and 13, 5), see [gloomsby.md](gloomsby.md) | `Route4` warp 0, lands at (3, 11) |

### Visual identity and connections

- **Tilesets:** primary `gTileset_General`, secondary `gTileset_Petalburg` (the meadow, pines, flowers and small ponds of Route 102 and 104; Route 117 is the card's fallback). Optional mood upgrade: **Shady Forest Secondary** (Team Aqua, `Tilesets/The Great Tileset Exchange/Full Tilesets/Shady Forest Secondary/`): dark pines, dead trees, cobbled paths and street lamps in a teal-and-grey palette. It adds a darker, spookier pine set and lamp posts for the lamp-lighter. Needs Porytiles baking exactly like Gen 4 Interior (it is a triple-layer set, `design/interiors.md`) and a `CREDITS.md` row (assembler Yumekua, creators Ekat99, Heartlessdragoon, Vurtax and more, Rahtak for the reformat; the folder's `credits.md` lists everyone). I do not recommend it for the first pass.
- **Weather:** `WEATHER_FOG_HORIZONTAL` for the whole road (one header setting, simplest). The two-column option (a column of `COORD_EVENT_WEATHER_FOG_HORIZONTAL` weather events at x = 30) only changes weather when you step on it, so entering from the gate would load without fog: do not use it.
- **Colours:** grey-green meadow, pale sand, dark pines, red flower row as the one warm accent.
- **Silhouettes:** the gate's roof at the west end, the film van and its cables in the lower middle, the pine stand at x 12 to 13.
- **Connections:** east edge to Briarwick's west edge (offset = Briarwick's path row minus 10); no other edges. Border: tree blocks.

### Flags (not claimed)

`FLAG_R4_ITEM_*` (one per hidden or ball item), `FLAG_R4_LODGE_GIFT`, reused trainer flags. No new story flag.

### Build checklist (R4)

1. Duplicate or add the map `Route4` (22 rows by 52 columns), tilesets General + Petalburg, music, fog weather, `MAPSEC_ROUTE_101`. 2. Trace the render's tree walls and sand band; fill the meadow with grass and paint the dirt path along y 11 to 12. 3. Place the west gate building and the lodge building; paint the lodge's side path. 4. Paint grass patches and the optional pond. 5. Connect the east edge to Briarwick once Briarwick exists. 6. Place the 5 trainers, NPCs, items, signs. 7. Add the two warps. 8. Close the north stub's top and add the 1-tile gap. 9. Credit rows in the same commit. 10. `make -j4`.

### Build effort

Easy to medium. Mostly trees and sand; the only odd piece is the lodge's side path. 3 hours for the layout, 1 more for events.

---

## R5: Gloomsby to Smeltham (land, sketch 5)

**Map `Route5`, 30 x 54. Render `Route 43.png`, unmirrored. Wild levels 22 to 27.**

### Description and walk-through

The road runs **north** from Gloomsby, climbing out of the fog into foothills. It begins at a small gate at the bottom of a rocky shelf, goes up a wide sand clearing, then enters a long valley with a **thin pond running down its west side** and a great field of tall grass in the middle. Halfway, a **toll-style gatehouse** crosses the road (a guard with a sense of humour). Above it the valley opens into grass and tree walls and at the very top a column of thin smoke on the horizon tells you Smeltham is near. The sound shifts from fog-hush to distant hammering. Pacing: a quiet start, two fights in the first third, the grass field with the pond in the middle (most of the fights), the toll gate as a breather, and a short run up to Smeltham.

Mood: practical, outdoorsy, slightly noisy. Colours: pale sand, bright grass, grey rock on the west, one red-brown cliff at the bottom left.

### Layout, segment by segment (walking from Gloomsby, south to north)

1. **The gate and the sand yard, x 12 to 17, y 41 to 53.** The render's south gatehouse (x 12 to 17, y 51 to 53) shows only its roof, so its door would sit on the map's last row. **PROPOSED:** keep the door at (14, 53), the bottom row, with the arrival tile (14, 52) inside the gate's own front step; if the building piece needs one more row, make the map 30 x 55 and shift everything down 1 (the size check still passes). Sign at (17, 49): `ROUTE 5. SOUTH: GLOOMSBY. NORTH: SMELTHAM. MIND THE CRANES`. The sand clearing x 12 to 17, y 42 to 50. Rocky shelf on the left (x 0 to 9, y 33 to 53). Trees on the right (x 18 to 29, y 41 to 53) with a rock outcrop at x 22 to 29, y 49 to 53.
2. **The lower ledges, x 16 to 17, y 36 to 38.** Two one-tile ledges (hop down only, so going north you walk around): at (16, 36) and (17, 38). A sign at (18, 41): `SMELTHAM. 1 KM. THE KETTLE IS ALWAYS ON`.
3. **The toll gatehouse, x 18 to 23, y 34 to 40.** The render's middle gatehouse. A pass-through building. **PROPOSED:** one interior `Route5_TollGate` (a Gatehouse layout) with two doors: the south door at (20, 39) (the render's steps at y 39 to 40) and a north door at (20, 34) on the roof side of the building (the render has sand above it at y 30 to 33, so paint one door metatile in the building's top edge if the piece has none). Sand clearing above: x 18 to 23, y 30 to 33.
4. **The long valley, x 8 to 21, y 7 to 33.** The **long thin pond** is at x 8 to 11, y 19 to 32 (4 wide, 14 long) and a **small pond** at x 8 to 11, y 13 to 16, with a 1-tile land bridge at y 17 to 18. East of them, the **tall-grass field** x 12 to 21, y 7 to 28 (the render's big green patch, with tree stumps and scattered pines inside it), and a western strip of grass at x 2 to 8, y 8 to 10. Two more tall-grass patches at x 12 to 14, y 30 to 39 (a 3 x 10 strip along the road). The road is the **dirt/sand path** along x 17 to 21 (PROPOSED: paint a 2-wide sand path from (20, 33) north to (16, 7) weaving round the pines so the player always has a clean line).
5. **The grass field.** Most trainers stand along the field's edge (see Trainers). **PROPOSED:** keep the field as one big 'unclear' area 10 wide, so the fights come from the sides.
6. **The north run, x 12 to 15, y 0 to 6.** The valley narrows to a 4-wide lane (x 12 to 15) between two tree walls (x 6 to 11 and x 16 to 21 up to the top). A sign at (17, 4): `SMELTHAM FOUNDRY. WORKERS AT LUNCH`. The **surveyor** stands here at (14, 3). At y 0 the lane meets Smeltham's south edge. The smoke column itself belongs on Smeltham's map; here a bit of grey haze can be suggested by a dull cloud palette only if the author wants it (no object needed).
7. **The west bank, x 2 to 8, y 8 to 10 and x 0 to 9, y 33 to 53.** The render's rocky shelf with a cliff face (x 7 to 10, y 33 to 45) holds the TM and the IRON items.

### Water

The long pond (x 8 to 11, y 19 to 32) and the small pond (x 8 to 11, y 13 to 16). **Fishing at any time, Surf only after badge 5.** Tables from the card: Old Rod MAGIKARP 15 (70), BARBOACH 15 (30); Good Rod BARBOACH 22 (60), GOLDEEN 22 (20), WOOPER 22 (20); Super Rod BARBOACH 25 (40), GOLDEEN 25 (40), WOOPER 25 (15), CORPHISH 25 (4), WHISCASH 27 (1). Surf (return visit): GOLDEEN 22 to 26 (60), BARBOACH 22 to 26 (30), PSYDUCK 24 to 26 (5), WOOPER 24 (4), CHINCHOU 26 (1). **HP UP islet:** a 1-tile islet at (9, 25) in the long pond (Surf, badge 5).

### Wild Pokémon (from the card, unchanged)

MACHOP 22 to 23, GEODUDE 22 to 23, MAGNEMITE 23 to 24, ARON 23 to 24, DRILBUR 24, KLINK 24 to 25, TIMBURR 25, SANDSHREW 25, ROGGENROLA 25 to 26, NOSEPASS 26, MAWILE 26 to 27, LARVITAR 26 to 27 (20/20/10/10/10/10/5/5/4/4/1/1). The grass patches above are the encounter tiles. **PROPOSED:** make only the **field (x 12 to 21, y 7 to 28)** use this table; the three small strips use it too (one table per map in Emerald). Steel is seeded before gym 4 on purpose ([../../gyms.md](../../gyms.md)).

### Trainers (6, positions PROPOSED)

| # | Class and team | Stands at | Faces | Sight | Notes |
|---|---|---|---|---|---|
| 1 | Hiker: GEODUDE 22, ARON 23 | (6, 46), on the rocky shelf | east | 4 | spots the first sand clearing |
| 2 | Picnicker: SHINX 24, MAREEP 25 | (14, 35), in the lower grass strip | north | 3 | first fight on the road proper |
| 3 | Camper: TRAPINCH 24, SANDSHREW 25 | (22, 31), east of the sand above the toll gate | west | 4 | fights as you leave the gate |
| 4 | Fisherman: GOLDEEN 24, BARBOACH 25 | (12, 26), on the pond's east bank | west | 2 | looks over the long pond; fishing line gag |
| 5 | Hiker: MACHOP 24, ROGGENROLA 24 | (19, 17), inside the grass field | south | 4 | the field's heart |
| 6 | Black Belt: MEDITITE 25, MACHOP 25 | (14, 9), at the narrow top of the field | south | 5 | the last fight before the north run |

### NPCs (6 from the card)

| NPC | Position | Notes |
|---|---|---|
| Toll guard | inside the toll gate (see below) | 'Smeltham: mind the cranes' |
| Surveyor | (14, 3), the north lane | long tape measure, 'measuring for a scrap estimate' (Scheme 4 foreshadow, says nothing else) |
| Hiker | (20, 43), the sand clearing | recommends the Hoarfell Ice cave |
| Sleepy farmhand | (22, 14), beside the field | counts SKIDDO who are not there |
| Girl with a magnet | (11, 37), on the road | finds nails; offers one as a joke (no item) |
| Pebble kid | (7, 18), the pond's west bank | throws stones into the long pond |

Signs: (17, 49) south, (18, 41) mid-south, (17, 4) north.

### Items

| Item | Where (about) | Kind | Gate |
|---|---|---|---|
| POTION | (15, 47), the clearing | ball | none |
| SUPER POTION | (13, 22), a clearing in the field | ball | none |
| GREAT BALL | (20, 5), the narrow top | ball | none |
| ESCAPE ROPE | (17, 28), by a stump | hidden | none |
| MAX REPEL | (9, 8), the western strip | hidden | none |
| AWAKENING | (13, 41), the lower strip | hidden | none |
| HP UP | the islet (9, 25) | ball | Surf (badge 5) |
| IRON | (3, 36), behind a Cut tree on the shelf | ball | Cut (badge 1) |
| TM Sandstorm | (4, 40), the rocky shelf | ball | none |

**Object count.** 6 trainers + 6 NPCs + 6 visible balls (POTION, SUPER POTION, GREAT BALL, TM Sandstorm, IRON, HP UP) = 18, **over the limit of 15.** Cut it to 15: turn POTION and SUPER POTION into hidden items, and drop the girl with the magnet (her gag moves to the pebble kid). That leaves 6 + 5 + 4 = 15.

### Interiors on this road

- **`Route5_TollGate`** (Gatehouse): shared pattern, 15 x 6 (copy `LAYOUT_ROUTE110_SEASIDE_CYCLING_ROAD_ENTRANCE`, the vanilla gatehouse). Doors: south at (13, 5) (to the road's south half) and north at (1, 5) (to the road's north half). The toll guard stands at (7, 2) behind the counter, facing south, an `OBJ_EVENT_GFX_MART_EMPLOYEE` reskin or a `GUARD` sprite if one exists. Joke: 'A toll is due. It is a smile.' (no real toll). Optional upgrade: Team Aqua **Gatehouse Secondary** (see [gloomsby.md](gloomsby.md) for what it adds and the credit rows).
- **Gloomsby East Gate** (the south end): shared interior in [gloomsby.md](gloomsby.md).

### Warp table (R5)

| Map | Tile | Destination |
|---|---|---|
| `Route5` | (14, 53), the south gate door | `Gloomsby_EastGate` warp 2 (the right door pair) |
| `Route5` | (20, 39), the toll gate south door | `Route5_TollGate` warp 0 |
| `Route5` | (20, 34), the toll gate north door | `Route5_TollGate` warp 1 |
| `Route5_TollGate` | (13, 5) | `Route5` warp 1, lands at (20, 40) |
| `Route5_TollGate` | (1, 5) | `Route5` warp 2, lands at (20, 33) |

### Visual identity and connections

- **Tilesets:** `gTileset_General` + `gTileset_Rustboro` (grey rock face, foothills: as Route 104 north). Optional: the hill shelf in `gTileset_Fallarbor` for the rocky west.
- **Weather:** none. The fog stays behind at Gloomsby.
- **Colours:** bright grass, pale sand, grey rock, one dirt cliff.
- **Music:** `MUS_ROUTE119` (cheerful hills).
- **Silhouettes:** the toll gatehouse mid-road, the pond like a blue stripe, the first thread of smoke at the top.
- **Connections:** north edge (lane x 12 to 15) to Smeltham's south edge. South end: the gatehouse only.

### Flags (not claimed)

`FLAG_R5_ITEM_*`, reused trainer flags.

### Build checklist (R5)

1. Map `Route5` 30 x 54, tilesets, `MAPSEC_ROUTE_102`. 2. Trace the trees and the rock shelf. 3. Paint the ponds and the grass field. 4. Paint the sand path, ledges, toll gatehouse. 5. Place trainers/NPCs/items/signs with the 15-object trim. 6. Add the warps and the north connection after Smeltham exists. 7. Credits. 8. `make -j4`.

### Build effort

Medium: a tall map, four sets of events. 4 hours.

---

## R6: Smeltham to Hoarfell (land, sketch 6 and 9)

**Map `Route6`, 64 x 23. Render `Route 42.png` alone. Wild levels 28 to 33.**

**Answer to the card's open question 3: use Route 42 alone, not stitched with Route 44.** It is already the right shape (west entry, east exit, 3 cave doors, 2 lakes) and 64 columns is a long road already. I checked Route 44 (67 x 25): its east end is a sealed cave door and a solid rock mass, so it needs a gap cut through rock; Route 42's east end (sand at y 7 to 10) is already open. If the author later wants a longer road, add **Route 44's central grove and pond as a 20 x 23 bridge piece** between the two lakes; nothing else would change.

### Description and walk-through

The long climb over the north-west mountains. You leave Smeltham by a broad sand lane under a high cliff, pass a **sign for the mine** beside a dark door in the rock (the R7 junction), and follow a rocky pass with two blue lakes, shelves of ledges and sudden grass hollows. The air gets colder; by the east end snow dust blows along the ground. The east end is a wide sand clearing under a cliff; beyond it, through a gap in the rock, Hoarfell. Set pieces: the stranded **lorry** with a flat tyre (Goldsworth Salvage, foreshadows Scheme 4), the **junction door** to the mine, a **rest bench** with a free GREAT BALL in the middle, and the last long stretch of sand where the **ULTRA BALL** waits.

Mood: epic but friendly. Pacing: the first third is the junction and the lorry, the middle is the lakes and 3 fights, the last third is the ridge climb and 3 fights.

### Layout, segment by segment (walking from Smeltham, west to east)

1. **The Smeltham lane, x 0 to 15, y 8 to 15.** Sand band 8 tall at the west edge, narrowing to 5 at x 15. The render's west gatehouse (x 0 to 4, y 7 to 11) is **dropped**: replace it with sand so the edge connection meets open ground. Sign at (11, 8): `ROUTE 6. WEST: SMELTHAM. EAST: HOARFELL`. Sign at (8, 13): `SLAGWELL MINE. THIS WAY. IT'S A SPUR, NOT A SHORTCUT`. The **lorry** (a 3 x 3 `OBJ_EVENT_GFX_TRUCK`) sits at x 5 to 7, y 10 to 12; the lorry driver stands at (8, 11). The painted markings on the lorry read GOLDSWORTH SALVAGE.
2. **The junction door, (14, 8).** A dark door in the cliff with a sign (11, 8). A warp to R7 (see the table). One tile west of it a **guide** (the old guide) stands at (13, 9).
3. **The first lake, x 18 to 25, y 7 to 17.** A T-shaped lake with a rock islet at (20, 14). The road passes **south of it** along y 17 to 19, through the sand and the small pond at x 4 to 13, y 17 to 20 (a SW pond). A boulder at (24, 12) and rock outcrops at (22, 6) and (16, 11).
4. **The rest bench and the grass hollow, x 26 to 35, y 9 to 15.** A flat sand patch at x 30 to 35, y 13 to 14 (the render's sand strip). **PROPOSED:** the bench NPC sits at (31, 14) and gives one GREAT BALL. Above the patch is the render's second cave door at (32, 12), the **old adit**: seal it with a Rock Smash rock at (32, 13) (Rock Smash, badge 2). A tiny one-room interior behind it holds the EVERSTONE (see Interiors).
5. **The second lake, x 36 to 45, y 9 to 17.** A big lake with a bump at x 43 to 45, y 9 to 12 and an islet at (40, 14) holding the **RARE CANDY** (Surf, badge 5). The road passes on its **south** shore along y 17 to 19.
6. **The tall-grass band, x 28 to 33, y 5 to 7 and x 28 to 36, y 13 to 16** (the render has a patch of grass inside the pines). **PROPOSED:** two grass patches: x 38 to 47, y 5 to 7 (north verge) and x 28 to 36, y 15 to 17 (under the first bench). The render's trees (x 16 to 31, y 5 to 13) form a **grove** where the Ultra Ball hides.
7. **The ridge climb, x 46 to 58, y 7 to 14.** The road climbs a sand ramp (x 46 to 58) with two signs: (49, 12) and (58, 11). The **third cave door** at (50, 10) is a locked storage door (Goldsworth Salvage: a sign `WAREHOUSE. NO ENTRY. REALLY`), no warp. TM Dig sits at the end of the pass at (57, 9).
8. **The east clearing, x 56 to 63, y 7 to 10.** A wide sand patch with the east edge open at y 7 to 10: the connection to Hoarfell. The last sign, at (60, 9): `HOARFELL. SNOW, CLIFF AND TEA`. The **cold traveller** stands at (59, 8).

### Water

Two lakes (x 18 to 25 / y 7 to 17; x 36 to 45 / y 9 to 17) and a small pond (x 4 to 13, y 17 to 20). Fishing: Old Rod MAGIKARP 20 (70), GOLDEEN 20 (30); Good Rod GOLDEEN 28 (60), PSYDUCK 28 (20), SEEL 28 (20); Super Rod GOLDEEN 33 (40), SEEL 33 (40), PSYDUCK 33 (15), CHINCHOU 33 (4), LAPRAS 33 (1). Surf (return): GOLDEEN 28 to 32 (60), PSYDUCK 28 to 32 (30), SEEL 30 to 32 (5), SLOWPOKE 30 to 32 (4), LAPRAS 33 (1). RARE CANDY on the islet (40, 14).

### Wild Pokémon (from the card, unchanged)

SWINUB 28 to 29, SNORUNT 28 to 29, BOLDORE 30, BRONZOR 29 to 30, CUBCHOO 29 to 30, SKORUPI 30, SNEASEL 30 to 31, FERROSEED 31, VANILLITE 31 to 32, DELIBIRD 31 to 32, PILOSWINE 33, BERGMITE 31. Tall grass at the patches above; the ridge sand tiles are not grass. Rock Smash rocks for EVERSTONE use the card's R6 loot (EVERSTONE) rather than encounters.

### Trainers (6, positions PROPOSED)

| # | Class and team | Stands at | Faces | Sight | Notes |
|---|---|---|---|---|---|
| 1 | Hiker: ROGGENROLA 28, BOLDORE 29 | (12, 12), by the junction | east | 4 | the first fight, three steps past the guide |
| 2 | Camper: SWINUB 29, SNORUNT 30 | (27, 18), south of the first lake | north | 3 | on the south sand |
| 3 | Fisherman: SEEL 30, GOLDEEN 31 | (36, 17), the second lake's west shore | east | 2 | fishing at the shore |
| 4 | Picnicker: CUBCHOO 30, VANILLITE 30 | (42, 6), the north verge grass | south | 4 | stands in the grass |
| 5 | Hiker: ONIX 29, GRAVELER 30 | (47, 11), at the foot of the ridge | east | 4 | blocks the ramp |
| 6 | Bird Keeper: STARAVIA 30, DELIBIRD 31 | (55, 9), on the east clearing | west | 5 | last fight, the snow bird |

### NPCs (8 from the card)

| NPC | Position | Notes |
|---|---|---|
| Lorry driver | (8, 11) | flat tyre, waiting for a crane (Scheme 4 foreshadow; **removed or moved** after `FLAG_SMELTHAM_SCHEME_DONE`: the lorry is one of the vehicles folded into the cube, so on the first visit after Scheme 4 the lorry and the driver are gone, or the driver says 'it's just the same lorry... smaller') |
| Mountaineer | (21, 18) | Ice cave hint |
| Ore trader | (28, 12), beside the junction | flavour: sells ore samples as dialogue only |
| Old guide | (13, 9) | the Slagwell sign: 'the spur is quiet on Tuesdays' |
| Boy | (35, 16) | saw a rich boy shouting at a ledge (optional Troglodyte sighting) |
| Kid | (44, 18) | warns Surf is not yet available |
| Cold-weather traveller | (59, 8) | advice about Hoarfell |
| Bench NPC | (31, 14) | gives one GREAT BALL |

**Object count.** 6 trainers + 8 NPCs + the lorry = 15 already, before any ball. Trim: merge the kid and the boy into one NPC (the Troglodyte sighting and the Surf warning become two lines of one talker) and the ore trader into the old guide. That leaves 6 trainers + 6 NPCs + the lorry = 13, so only 2 visible balls fit (ULTRA BALL and TM Dig, the two that matter). POTION, SUPER POTION and the rest become hidden items, or the SUPER POTION and POTION are placed as the pair 'in the lorry's open back' (a `bg_event` each).

### Items

| Item | Where (about) | Kind | Gate |
|---|---|---|---|
| POTION | (3, 10), by the lorry | ball | none |
| SUPER POTION | (20, 19), south of the first lake | ball | none |
| GREAT BALL | from the bench NPC | gift | none |
| ULTRA BALL | (52, 8), the ridge's end (the first of the game) | ball | none |
| TM Dig | (57, 9), end of the pass | ball | none |
| MAX REPEL | (24, 4), the north rocks | hidden | none |
| ICE HEAL | (45, 5), the north grass | hidden | none |
| FULL HEAL | (34, 14), by the bench | hidden | none |
| EVERSTONE | the old adit room | ball | Rock Smash (badge 2) |
| CARBOS | (17, 15), behind two boulders | ball | Strength (badge 4) |
| RARE CANDY | the islet (40, 14) | ball | Surf (badge 5) |

### Interiors on this road

- **The old adit** (`Route6_OldAdit`, optional, cut first if effort is a problem): 10 x 7, cave, tileset `gTileset_General` + `gTileset_Cave` (vanilla). A single small room: a ladder-less dead end, one ball at (7, 2) (EVERSTONE), a pick-axe `bg_event` at (3, 3). Door at (5, 6) (the bottom edge, arrow warp). Warp from R6 (32, 12) once the rock is smashed.

### Warp table (R6)

| Map | Tile | Destination |
|---|---|---|
| `Route6` | (14, 8), the junction door | `Route7` warp 0 (R7's south end, tile (10, 33)) |
| `Route6` | (32, 12), the adit door (after Rock Smash) | `Route6_OldAdit` warp 0 |
| `Route6_OldAdit` | (5, 6) | `Route6` warp 1, lands at (32, 13) |
| `Route7` | (10, 34), the south warp tile | `Route6` warp 0, lands at (14, 9) |

### Visual identity and connections

- **Tilesets:** `gTileset_General` + `gTileset_Fallarbor` (the rocky Route 114 and 115 set, the brown mountains and sand of the render; check in Porymap by opening `Route114`). The cliffs, ledges, boulders and sand all exist there.
- **Weather:** header `WEATHER_NONE`. **PROPOSED optional:** a column of `COORD_EVENT_WEATHER_SNOW` weather events at x = 52, y 7 to 14 (the ridge) so the last third gets snow flurries as the player nears Hoarfell. `WEATHER_SNOW` exists in the build ('unused' in vanilla but compiled).
- **Colours:** brown rock, tan sand, two blue lakes, white dusting in the east.
- **Music:** `MUS_ROUTE120`.
- **Silhouettes:** the lorry at the west, two lakes like blue plates, the high ridge ramp.
- **Connections:** west edge to Smeltham's east edge (offset = Smeltham's lane row minus 8); east edge (y 7 to 10) to Hoarfell's west edge (offset = Hoarfell's gap row minus 7). The junction door is a warp.

### Flags (not claimed)

`FLAG_R6_ITEM_*`, `FLAG_R6_LORRY_SEEN` (only if the lorry should vanish when Scheme 4 is done), reused trainer flags.

### Build checklist (R6)

1. Map `Route6`, tilesets, `MAPSEC_ROUTE_103`. 2. Trace trees, cliffs, ledges, lakes. 3. Replace the west gatehouse with sand. 4. Paint the grass and ridge sand. 5. Place the junction door and the adit door. 6. Connect edges after the towns exist. 7. Place trainers and trimmed NPCs. 8. Add items. 9. Credits. 10. `make -j4`.

### Build effort

Medium to hard (long, 3 doors, 2 lakes). 5 hours. The render is one big piece, so it is a trace job more than a design job.

---

## R7: Slagwell spur (land, sketch 7 and 8)

**Map `Route7`, 22 x 36. Render `Route 46.png`. Wild levels 29 to 34.**

### Description and walk-through

A narrow side valley that leads north from R6 up to the mine door. You come out of the R6 door at the south end onto a short sand path with tall grass on the left. Walls of rock close in on both sides. A **tall stone pillar** stands in the middle with a dirt loop round it, a pair of rock shelves climb to the right, and at the top a **dark door with a lamp over it** is the mine. A sign at the foot (`SLAGWELL MINE. HARD HATS RECOMMENDED. HARD HEADS REQUIRED`) and a miner at the door who says the lamps are free but the dark is not.

Mood: a cul-de-sac with a goal. Pacing: grass at the bottom (2 fights), the pillar loop (the Rock Smash fight), the shelf climb (the Strength boulders), the door. The player can finish this road in 2 minutes.

### Layout, segment by segment (south to north)

1. **The arrival, x 8 to 13, y 28 to 35.** The render's south gate is **dropped**; the warp arrives at (10, 34) on a sand path (x 8 to 13, y 28 to 34, 6 wide) with trees both sides (x 0 to 3 and x 14 to 21). Sign at (11, 27) (the render's sign).
2. **The grass field, x 4 to 14, y 20 to 28.** Tall-grass patches: x 4 to 7, y 20 to 28 (west) and x 8 to 14, y 23 to 26 (central). The render's tall grass.
3. **The pillar loop, x 6 to 13, y 13 to 18.** A central standing-rock formation with a 1-tile dirt path round it (the 'loop'). Rocks on its west: x 6 to 9, y 14 to 17.
4. **The eastern shelf, x 14 to 21, y 5 to 20.** Rock shelves (cliff faces) stepping up the east side with ledges; two Strength boulders at (18, 14) and (19, 17); one Rock Smash rock at (16, 12).
5. **The head of the valley, x 8 to 17, y 3 to 8.** A green strip along the top with the **mine door** at (16, 5), a notch in the cliff with a lamp. Sign at (14, 5).
6. **The west pocket, x 2 to 7, y 5 to 11.** A small grass pocket with the ETHER, reached around the pillar.

### Wild Pokémon (from the card, unchanged)

ROGGENROLA 29 to 30, ZUBAT 29 to 30, MAGNEMITE 30 to 31, ONIX 30 to 31, BRONZOR 30 to 31, WOOBAT 30 to 31, NOSEPASS 31 to 32, DWEBBLE 31 to 32, SKORUPI 32, BOLDORE 32 to 33, MAWILE 33, LARVITAR 33. Rock Smash rocks: DWEBBLE 29 to 33 (60), GEODUDE 29 to 33 (30), ROGGENROLA 30 (5), NOSEPASS 32 (4), SHUCKLE 33 (1). No water, no fishing.

### Trainers (3, positions PROPOSED)

| # | Class and team | Stands at | Faces | Sight | Notes |
|---|---|---|---|---|---|
| 1 | Hiker: ROGGENROLA 30, MAGNEMITE 31 | (9, 24), at the grass field's west | east | 4 | sees you as you cross the field |
| 2 | Collector: WOOBAT 31, BRONZOR 32 | (10, 15), at the foot of the pillar | south | 3 | stands on the dirt loop |
| 3 | Black Belt: MACHOP 31, TIMBURR 32 | (14, 8), on the head strip | west | 5 | guards the door, the last fight |

### NPCs (3 from the card)

| NPC | Position | Notes |
|---|---|---|
| Miner | (15, 6), beside the mine door | 'Mind the dark. Flash helps' |
| Pebble boy | (5, 22) | collects pebbles in the grass |
| Cart-pusher | (12, 11) | his ore cart (a pushable-boulder look-alike, or a truck sprite, `bg_event`) is stuck; after Scheme 4 the cart bears a sticker '4001' (set with `FLAG_SMELTHAM_SCHEME_DONE`) |

Signs (2): (11, 27) junction, (14, 5) mine door.

### Items

| Item | Where (about) | Kind | Gate |
|---|---|---|---|
| ETHER | (3, 8), the west pocket | ball | none |
| ESCAPE ROPE | (10, 20), the grass | ball | none |
| SUPER REPEL | (7, 29), by the entry path | hidden | none |
| GREAT BALL | (16, 11), behind the Rock Smash rock at (16, 12) | ball | Rock Smash (badge 2) |
| IRON | (20, 15), behind the two boulders | ball | Strength (badge 4) |

### Interiors

None on the road (the mine is [landmarks-west-detail.md](landmarks-west-detail.md)). R7's 'door' at the top is a warp to `SlagwellMine_1F`.

### Warp table (R7)

| Map | Tile | Destination |
|---|---|---|
| `Route7` | (10, 34), the south arrival | `Route6` warp 0 |
| `Route7` | (16, 5), the mine door | `SlagwellMine_1F` warp 0 |

### Visual identity and connections

- **Tilesets:** `gTileset_General` + `gTileset_Fallarbor`, as R6, so the two roads feel the same.
- **Weather:** none. **Music:** `MUS_ROUTE104` (calm), then the mine's own track on entry.
- **Colours:** brown stone, dry grass, one lit lamp at the top.
- **Silhouettes:** the stone pillar at the centre, the notch with the lamp at the top.
- **Connections:** none by edge (a door at the south, a door at the north). Border: rock blocks.

### Flags (not claimed)

`FLAG_R7_ITEM_*`, reused trainer flags. After Scheme 4, the ore cart sticker is set by `FLAG_SMELTHAM_SCHEME_DONE`.

### Build checklist (R7)

1. Map `Route7`, tilesets, `MAPSEC_ROUTE_105`. 2. Trace rocks and trees. 3. Paint the grass patches and the dirt loop. 4. Place the two doors. 5. Boulders and rocks. 6. Trainers, NPCs, items, signs. 7. Credits. 8. `make -j4`.

### Build effort

Easy. 2 hours.

---

## Open questions (whole group)

1. **Edge truth.** The cards' 'west end meets Briarwick's west edge' is impossible as an edge join. I used the consistent reading in the edge table above. Confirm, or tell me to mirror a road.
2. **R6 length.** I picked Route 42 alone (64 x 23). Is that long enough, or do you want Route 44's grove bolted in (a 20 x 23 piece)?
3. **R6's junction as a door.** I used the render's cave door at (14, 8) as the R7 junction, so R7's south end is a warp, not an edge connection. The card said 'a gap in the north cliff'. Both work; a door needs one warp pair, an edge needs a corridor cut through four rows of rock.
4. **Object counts.** R4, R5 and R6 all go over 15 live objects once every NPC, trainer and visible item is placed. I trimmed in each section. Which NPCs does the author want to keep? The weakest ones are the sleepy traveller (R4), the girl with the magnet (R5) and the ore trader (R6).
5. **R4 weather.** Road-wide fog or only the west third? I recommend road-wide. A two-part fog (weather events on tiles) needs scripting and still loads wrong when you enter from the west.
6. **Marsh pond on R4.** Add it or not? It supports the ELIXIR item and fishing, but the render has no water.
7. **The Lodge door.** The render's south gatehouse has no obvious door for the lodge spur. The side path (8 tiles) is my fix.
8. **R6's lorry** vanishing after Scheme 4. Is that wanted, or does the driver just say a different line?
9. **Snow on R6's east end.** A column of snow weather events is an optional flourish. Skip or keep?
