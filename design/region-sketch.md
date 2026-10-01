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

## Map section budget: no engine edit needed (APPLIED 2026-10-01 for routes 4 to 21)

**Why an engine edit to add more names does not help.** A map section id is one byte, because a Pokémon's 'met at' place is stored in 8 bits (`mapsec_u8_t`, `include/gametypes.h`). Widening it would change the Pokémon data and the save. The ceiling is 253 ids (0xFD to 0xFF are special), and the tree uses 215, so 37 are free after the six Veldris ones.

**What was done (data only, no C change).** The 88 Hoenn sections (ids 0 to 87) are unreachable in Veldris, and a section's name and its x, y, width, height live only in `src/data/region_map/region_map_sections.json`. Veldris routes 4 to 21 now take over 18 Hoenn route entries by name and position. Only 18 of the 34 Hoenn route entries are clean: the other 16 (104, 106, 109, 110, 111, 112, 114, 115, 116, 119, 121, 122, 125, 132, 133, 134) carry always-on landmark rows in `src/landmark.c` (for example Route 104 would show PETALBURG WOODS on the Pokénav map), so they are not used.

| Veldris route | Section id used (the constant Porymap shows) |
|---|---|
| R1 to R3 | `MAPSEC_VELDRIS_ROUTE_1` to `_3` (added earlier) |
| R4 | `MAPSEC_ROUTE_101` |
| R5 | `MAPSEC_ROUTE_102` |
| R6 | `MAPSEC_ROUTE_103` |
| R7 | `MAPSEC_ROUTE_105` |
| R8 | `MAPSEC_ROUTE_107` |
| R9 | `MAPSEC_ROUTE_108` |
| R10 | `MAPSEC_ROUTE_113` |
| R11 | `MAPSEC_ROUTE_117` |
| R12 | `MAPSEC_ROUTE_118` |
| R13 | `MAPSEC_ROUTE_120` |
| R14 | `MAPSEC_ROUTE_123` |
| R15 | `MAPSEC_ROUTE_124` |
| R16 | `MAPSEC_ROUTE_126` |
| R17 | `MAPSEC_ROUTE_127` |
| R18 | `MAPSEC_ROUTE_128` |
| R19 | `MAPSEC_ROUTE_129` |
| R20 | `MAPSEC_ROUTE_130` |
| R21 | `MAPSEC_ROUTE_131` |
| R22 to R33 | not yet: 12 new ids, added when those routes are built |

The positions (x, y, w, h) came from the **old** layout in [region-map.md](region-map.md) and must be redone from the author's sketch.

**New ids still needed:** 12 routes (R22 to R33) + 17 settlements + up to 7 landmarks = 36 of the 37 free. That is tight. Post-game landmarks can borrow Hoenn cave and ruin entries (Granite Cave, Desert Ruins and so on) instead of new ids, which would free up to 7. Not decided.

**Side effects.** Porymap's dropdown shows the old constant (`MAPSEC_ROUTE_101`) while the game shows `ROUTE 4`, so use the table above. The Hoenn maps in the ROM now carry Veldris names but are unreachable. Logged in [engine-edits.md](engine-edits.md).

## Landmarks (author, 2026-10-01)

Some of the 7 landmarks are **post-game only**, including the one next to Hollowbrook (south-west). Post-game landmarks do not need their section during the main story, so they can be added last. Still to learn from the author: which of the other six are post-game, and what each landmark is.

## Suggested terrain, gyms and landmarks (PROPOSED, 2026-10-01, for the author to react to)

Picture: [art/region_sketch_labelled.png](art/region_sketch_labelled.png) (the author's sketch redrawn with labels).

Follows the sketch's walking order and the gym order Normal, Bug, Ghost, Steel, Ice, Flying, Poison, Fairy, Water. Nothing here is canon.

| Place (sketch) | Terrain | Gym | Nearby landmark idea |
|---|---|---|---|
| Hollowbrook (1) | quiet farm village, south-west corner | none | SW landmark (post-game): an old orchard or cabin where Gatsby met Cynthia |
| Crestfall (2, town) | farmland, hay maze | 1 Normal | none |
| Wendlebury (3, town) | market crossroads | none | none (water link south is Surf) |
| City 4 | forest edge city, first Goldsworth house | 2 Bug | the NE landmark: a deep forest maze or hollow log cave |
| Town 5 | foggy marsh and old graveyard | 3 Ghost | none |
| Town 6 | mining and foundry town | 4 Steel | the spur between routes 6 and 9: the foundry mine (cave) |
| City 7 | snowy mountain city | 5 Ice (gives Surf, which opens the water links) | a frozen cave system on its mountain, optional |
| Central City | the skyscraper, hub of the region | 6 Flying | none; the Elite 4 landmark is just south of it |
| North and east towns (3) | ridge and highland towns | none | none |
| East cities (2) | cliffs and gardens | 7 Poison, 8 Fairy | far north-east landmark: a lake island or shrine |
| Far south-east city | harbour and lighthouse | 9 Water | none |
| Lost City | sunken ruin city, dead end | post-game | its water routes only |
| South-centre city | hidden coast city | post-game only (author) | two south landmarks: a beach and a cliff cave |

Open: the 7 landmarks' final list, which ones are post-game, and whether Poison and Fairy sit in the two east cities or elsewhere.
