# Author's hand-drawn region sketch (2026-10-01)

Status: **the author's own sketch, read by me.** Picture: [art/author_region_sketch_2026-10-01.jpg](art/author_region_sketch_2026-10-01.jpg). My reading below is a transcription, not canon: anything marked (?) is a guess to check. It is **newer than** [region-map.md](region-map.md) and [veldris-layout-annotated.png](veldris-layout-annotated.png), and it disagrees with them in places (see 'What changes').

Legend (as drawn): blue = water route, green = landmark, red = city, purple = town, brown = land route. Black arrows give the order the player walks the route.

## Settlements as drawn (20)

| Sketch no. | Place | Type as drawn | Notes |
|---|---|---|---|
| 1 | Hollowbrook | town | far south-west. A landmark hangs off it to the south-west (brown) |
| 2 | Crestfall | **town** (purple) | route 1 comes from Hollowbrook. Note: earlier decision says Crestfall is a city |
| 3 | Wendlebury | town | route 2 from Crestfall |
| 4 | (unnamed) | city | route 3 from Crestfall. A landmark hangs off it to the north-east |
| 5 | (unnamed) | town | route 4 |
| 6 | (unnamed) | town | route 5 |
| 7 | (unnamed) | city | route 9, after routes 6 to 8 (a landmark spur sits on the road) |
| - | (unnamed, north) | town | route 10 from city 7 |
| - | (unnamed, north-east) | town | route 11 |
| - | (unnamed, centre-right) | town | route 12 |
| - | (unnamed, east) | city | route 13 (and a second route also numbered 12) |
| - | (unnamed, far north-east) | city | route 15 and 16 from the town below it |
| - | (unnamed, far east) | town | routes 14 and 17 (water), 15 and 16 (land) |
| - | (unnamed, south of centre-right) | town | routes 21 and 30 (water) |
| - | (unnamed, south-east) | city | routes 22 and 29 |
| - | (unnamed, south-east) | town | routes 23 and 28 |
| - | (unnamed, far south-east) | city | routes 24 and 27 |
| - | **Lost City** | city | routes 25 and 26. Dead end |
| - | **Central City (with the skyscraper)** | city | the Goldsworth skyscraper. Land road from city 7 (unnumbered), water route 32 from the east |
| - | (unnamed, south-centre) | city | **'Only unlocks post game'** (author note). Water to Wendlebury, to the east town and to a landmark in the south, land to a landmark in the south-east |

Landmarks (7, green): south-west of Hollowbrook, north-east of city 4, the spur between routes 6 and 9, the **Elite 4** one (between Central City and the south-centre city, reached by routes 33 and 31(?)), two south of the post-game city, and one in the far north-east (water links to the city 15 and 16 and the city beside it).

## Routes as drawn

33 numbered (1 to 33). Number 12 is written twice and 20 never appears, so I read the second 12 as 20 (?). The route near the Elite 4 landmark reads '3c', which I take as 31 (?).
Water-only links (blue, no brown beside it): Wendlebury to the south-centre city, the south-centre city to the east town, route 32 into Central City from the east, and the north-east landmark to its two cities. These need Surf.

## What changes against the older docs

1. **Route 1 now ends in Crestfall, not Wendlebury.** The order is Hollowbrook, Route 1, Crestfall (gym 1), then Route 2 to Wendlebury. [route1.md](route1.md), [route2.md](route2.md), [wendlebury.md](wendlebury.md), [crestfall.md](crestfall.md) and the dialogue and script drafts all assume the old order.
2. Crestfall drawn as a town, Wendlebury as a town.
3. **20 settlements**, not 18. If the Lost City and the post-game city do not count, it is 18.
4. The Elite 4 is a landmark, not a town. Central City (gym 6, Flying, skyscraper) sits in the middle of the region.
5. The first branch is at Crestfall: Wendlebury (3) and city 4 are both one route away.

## Open questions

See the chat reply of 2026-10-01 and `game-bible.md`. **Update 2026-10-01:** the author confirmed Route 1 is Hollowbrook to Crestfall and chose to make **Crestfall a town**. Route 1, Route 2, Crestfall, Wendlebury, the map plan, the story outline and the dialogue were updated. Still open: the other questions in the chat reply (gyms per place, post-game city, landmarks, sections budget).

## Map section budget: no engine edit needed (2026-10-01, answering the author)

**Why an engine edit to add more names does not help.** A map section id is one byte, because a Pokémon's 'met at' place is stored in 8 bits (`mapsec_u8_t`, `include/gametypes.h`). Widening it would change the Pokémon data layout and the save. The ceiling is 253 ids (0xFD to 0xFF are special), and the tree already uses 215, so 37 are free after the six Veldris ones.

**What fits without any engine edit.** The 88 Hoenn sections (ids 0 to 87) are unreachable in Veldris, and a section's **name** and its **x, y, width, height** live only in `src/data/region_map/region_map_sections.json`. So Veldris routes can take over Hoenn route entries by editing JSON text only: for example, Veldris Route 4 uses the existing `MAPSEC_ROUTE_104` entry with its name changed to `ROUTE 4`. The Hoenn route entries are `MAPSEC_ROUTE_101` to `_134` (34 of them), enough for all 33 routes.

| Need | Count | Where it comes from |
|---|---|---|
| Routes 1 to 3 | 3 | already added (`MAPSEC_VELDRIS_ROUTE_1` to `_3`) |
| Routes 4 to 33 | 30 | renamed Hoenn route entries (`MAPSEC_ROUTE_104` to `_133`, PROPOSED), no new ids |
| Settlements | 20 | 3 added, **17 new ids** |
| Landmarks | up to 7 | **up to 7 new ids** (post-game ones can wait) |
| **New ids used** | **24 of 37** | 13 left over |

**Side effects to know about (untested).**
- Porymap's dropdown shows the old constant (`MAPSEC_ROUTE_104`) while the game shows `ROUTE 4`. A lookup table in this file or `region-map.md` would be needed.
- `src/landmark.c` gives some Hoenn routes landmark names on the Pokénav map (for example Route 104 shows PETALBURG WOODS). Pick route entries with no landmark rows, or the names would appear on the Veldris routes.
- It edits one upstream data file, so it needs a row in [engine-edits.md](engine-edits.md).

Not applied yet. It waits on the author's go.

## Landmarks (author, 2026-10-01)

Some of the 7 landmarks are **post-game only**, including the one next to Hollowbrook (south-west). Post-game landmarks do not need their section during the main story, so they can be added last. Still to learn from the author: which of the other six are post-game, and what each landmark is.
