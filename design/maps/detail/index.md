# Detailed design index (PROPOSED, 2026-10-01)

The detailed pass requested by the author: description, walk-through, every building interior (with x,y plans), warps, tilesets, gyms tile by tile, road segments with trainer positions, and build checklists. Rules and sources: [../interiors/README.md](../interiors/README.md) and [../interiors/catalogue.md](../interiors/catalogue.md). Overview of the cards these extend: [../index.md](../index.md).

| File | Title | Lines |
|---|---|---|
| [aldermere.md](aldermere.md) | ALDERMERE: detailed design (the Lost City, post-game, dead end) | 443 |
| [beaconmouth.md](beaconmouth.md) | BEACONMOUTH: detailed design (lighthouse city, GYM 9 Water, Scheme 9) | 482 |
| [briarwick.md](briarwick.md) | BRIARWICK: detailed city design (PROPOSED, 2026-10-01) | 423 |
| [brinecombe.md](brinecombe.md) | BRINECOMBE, detailed design (town, place 14, no gym) | 216 |
| [cragdale.md](cragdale.md) | CRAGDALE, detailed design (town, place 9, ridge town, no gym) | 173 |
| [crestfall.md](crestfall.md) | CRESTFALL: detailed town design (PROPOSED, 2026-10-01) | 321 |
| [driftsands.md](driftsands.md) | DRIFTSANDS: detailed design (beach town, no gym) | 249 |
| [ebbsworth.md](ebbsworth.md) | EBBSWORTH: detailed design (river port, town, no gym) | 373 |
| [gildhaven.md](gildhaven.md) | GILDHAVEN, detailed design (city, place 8, gym 6 Flying) | 412 |
| [gloomsby.md](gloomsby.md) | GLOOMSBY: detailed design (town, place 5, gym 3 Ghost) | 330 |
| [hemlock-reach.md](hemlock-reach.md) | HEMLOCK REACH, detailed design (city, place 12, gym 7 Poison) | 353 |
| [hoarfell.md](hoarfell.md) | HOARFELL: detailed design (city, place 7, gym 5 Ice, gives Surf) | 288 |
| [kingsquay.md](kingsquay.md) | KINGSQUAY: detailed design (harbour city, no gym) | 386 |
| [landmarks-south-detail.md](landmarks-south-detail.md) | SOUTH LANDMARKS: detailed design (Silverstrand, Echo Hollow, Argent Peak) | 350 |
| [landmarks-west-detail.md](landmarks-west-detail.md) | Detailed landmark design: Mothwood, Slagwell Mine, Hoarfell Ice cave | 510 |
| [lingmoor.md](lingmoor.md) | LINGMOOR, detailed design (town, place 10, heather highland, no gym) | 157 |
| [mirror-isle-detail.md](mirror-isle-detail.md) | MIRROR ISLE, detailed design (landmark, lake island shrine, optional) | 273 |
| [pinnacle-detail.md](pinnacle-detail.md) | THE PINNACLE, detailed design (landmark, the League) | 299 |
| [primrose-vale.md](primrose-vale.md) | PRIMROSE VALE, detailed design (city, place 13, gym 8 Fairy) | 311 |
| [routes-centre-detail.md](routes-centre-detail.md) | Roads of the centre, detailed design: R10, R11, R12, R18, R19, R20, R21 | 504 |
| [routes-east-detail.md](routes-east-detail.md) | Routes, the east (R13 to R17), detailed design | 374 |
| [routes-south-detail.md](routes-south-detail.md) | SOUTH ROADS R22 TO R31: detailed design | 437 |
| [routes-west-a.md](routes-west-a.md) | Roads, west group A: R1, R2, R3, R8, R9 (detailed design, PROPOSED, 2026-10-01) | 418 |
| [routes-west-b.md](routes-west-b.md) | Detailed road design: west group B (R4, R5, R6, R7) | 458 |
| [smeltham.md](smeltham.md) | SMELTHAM: detailed design (town, place 6, gym 4 Steel) | 275 |
| [vesperhaven.md](vesperhaven.md) | VESPERHAVEN: detailed design (the hidden coast, post-game hub) | 362 |
| [waymeet.md](waymeet.md) | WAYMEET, detailed design (town, place 11, crossroads and rail stop, no gym) | 207 |
| [wendlebury.md](wendlebury.md) | WENDLEBURY: detailed town design (PROPOSED, 2026-10-01) | 266 |

Hollowbrook is built (see [../../interiors.md](../../interiors.md)); it has no file here.

## Decisions and corrections from this pass

- **Gen 4 Interior** for all ordinary houses; vanilla layouts for Centers and Marts; every Gen 3 door faces south; gates are guard lines on plain connections (Gate Platinum only where a gate interior is wanted).
- **Catalogue corrections:** `Gatehouse Secondary` is a counter lobby; `Small town with lab Secondary` is a farm and lab exterior; the object limit is about 16 near the camera, not per map.
- **Route renders are open questions** (author, 2026-10-01); Gildhaven's Crosswind gym puzzle stays.
- **Gildhaven is 59 x 51**, Ilex Forest 51 x 63 (the cards divided by 16 instead of using the grid).
- **Edges changed to make renders connect** (R2 into Crestfall's east edge, R8 into Wendlebury's north, R4 and R5 ends swapped, Briarwick widened to 50 columns). Every offset is computed in the road files.

## Goldsworth houses: one proposed resolution (needs the author's yes)

The writers collided on layouts and cousins. PROPOSED fix: **one shared 13 x 11 Goldsworth layout** (Kingsquay's, [kingsquay.md](kingsquay.md) 6.10) for every house, and **one cousin set per city** from [../../goldsworth.md](../../goldsworth.md): Briarwick BARNABY, the lounger and KIP (Duchess); Hoarfell BIFF and PRESCOTT; Hemlock Reach CHAD; Primrose Vale TRIP; Kingsquay WINSTON; Beaconmouth the whole family back together for Scheme 9. The butler stays with Briarwick. Aldermere and Vesperhaven get no house.

## Open questions (collected from the five writers)

1. **Tileset imports.** Best value: Legend of Zelda House (Gloomsby tower, Mothwood lodge, Hoarfell hut), Emerald Slide (Hoarfell snow primary), Brick Cafe, Gate Platinum, Little Office, plus the LeoB ORAS recolours of the Slateport, Lilycove, Dewford, Sootopolis, Mossdeep and Fallarbor secondaries (these replace vanilla tileset files in place, so each needs a `CREDITS.md` row and an `engine-edits.md` entry). The triple-layer sets need the Porytiles conversion Gen 4 Interior got. Caves Alt cannot be used (over the metatile limit).
2. **Gym art.** Hay bales, hedges, webs (Crestfall, Briarwick), gas curtains, vats and buds (Hemlock Reach, Primrose Vale), three coloured wheel tiles (Beaconmouth) and the Crosswind arrow tiles (Gildhaven) are not in the tree: drawn by the author, or use the fallbacks written in each file.
3. **Custom sprites and buildings:** a tent and a wrapped crew (Scheme 2), the Apiary tower and Goldsworth pod buildings, and the Goldsworth Tower exterior (no tall-tower tiles in Emerald; the writers propose stacked ORAS windows, the museum facade, or Radio Tower tiles).
4. **Wendlebury Inn:** a third building (first use of Brick Cafe), or a scenery house.
5. **Untested engine assumptions:** trainers seeing a sliding player (Hoarfell gym, Ice cave), `WEATHER_SNOW` (marked unused), the Crosswind forced-walk belts, gate arrival direction from arrow warps, Shoal Cave's ice tile.
6. **Object counts:** Hoarfell's Scheme 5 scene (16), R4 to R6 and R23 to R25 sit at or over 15 on screen. Trims are written in each file; pick which NPCs to drop.
7. **Dive pearls and underwater maps** (R14, Brinecombe, R26, R29) are unplanned; whirlpools do not exist in Emerald (rock pairs used instead); Ditto is catchable from badge 5 unless the shrine stairs lock on badge 8.
8. **Geometry conflicts with the cards:** R22's weir is a three-pass switchback inside the road; vanilla Routes 109, 122, 125 and 126 do not have the shapes the cards assume; Aldermere is two outdoor maps; swap the Alph hall images (`2bl` water for the Drowned Hall, `39cd` glyphs for the Sanctum).
9. **Class names with animal words** ('Bird Keeper'): pick other classes.
