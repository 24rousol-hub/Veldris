# Route 1 (VeldrisRoute1): Hollowbrook to Crestfall

Status: **BUILT 2026-10-01** (map, events, trainers, wild Pokémon, Hollowbrook connection). Map: 60 x 25, Palladium's `Route 29.png` **mirrored left-right** (author 2026-10-01), built in **LeoB ORAS** tiles (General + Petalburg, the same pieces as vanilla Route 102: trees, tall grass, ledges 213/135/214, ledge walls 255/134/635, pale path), its Route 46 gatehouse replaced by forest. The sandy patches are pale path. West edge joins Hollowbrook's east exit (connection offset -2 from Hollowbrook, +2 back); the east edge (sand path, rows 9-12) waits for **Crestfall** (changed 2026-10-01 from Wendlebury, per the author's sketch: [region-sketch.md](region-sketch.md)). Dialogue: [dialogue/route1.inc](dialogue/route1.inc).

## Feel
Farm country, gentle, a first walk. All Normal and other common early Pokémon. No real animals.

## Wild Pokémon (PROPOSED, land only, no water)
Tall-grass tiles only. Levels 3 to 5 (raised 2026-10-01: the gym is now one route away, so the player arrives at about level 7 to 9). Standard 12-slot rates (20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1).

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | ZIGZAGOON | 3 to 4 |
| 2 | 20% | LILLIPUP | 3 to 4 |
| 3 | 10% | BIDOOF | 3 to 4 |
| 4 | 10% | SENTRET | 3 to 4 |
| 5 | 10% | ZIGZAGOON | 4 |
| 6 | 10% | LILLIPUP | 4 |
| 7 | 5% | BIDOOF | 4 to 5 |
| 8 | 5% | SENTRET | 4 to 5 |
| 9 | 4% | SKITTY | 4 to 5 |
| 10 | 4% | SKITTY | 5 |
| 11 | 1% | SLAKOTH | 5 |
| 12 | 1% | MILTANK | 5 |

**Night (BUILT 2026-10-09, species PROPOSED).** From 20:00 to 06:00 on the fake clock Route 1 uses a second table, `gVeldrisRoute1_Night` in `src/data/wild_encounters.json`: same slots, rate 20 and levels, only some species change (slot 2 and 4 and 6 HOOTHOOT, slots 3 and 7 RATTATA, slot 8 SPINARAK, slot 12 MURKROW; ZIGZAGOON, SKITTY and SLAKOTH stay). Full table and the open-air rule: [time-of-day.md](time-of-day.md).

Rates add to 100%. I have not checked that every species is enabled in this build. SLAKOTH and MILTANK appear in the Crestfall gym, so they stay at 1% here. Porymap writes these to `wild_encounters.json` through its Wild Pokémon tab.

## Trainers (PROPOSED, three, all cheap to add)
All three reuse vanilla Hoenn trainer entries (no new trainer id, UNTESTED, see `CLAUDE.md` 'A new trainer'). No IVs or EVs, as for every trainer. Moves left to the default level-up set.

| Trainer | Team | Notes |
|---|---|---|
| Youngster | LILLIPUP L4 | Easy first fight |
| Lass | ZIGZAGOON L4, SKITTY L4 | Two-Pokémon fight |
| Farmer | ZIGZAGOON L5, SKITTY L5 | The toughest on the road |

## NPCs and items
- **Guide:** near the west end, gives 3 POTIONs once. Needs one flag (planned, unclaimed).
- **Hidden item or two:** a POTION and a REPEL in the grass, to reward exploring. Placed in Porymap or by me after the map is pushed.
- **Added 2026-10-01 (dialogue only, see `route1.inc`):** a bucket kid near the Hollowbrook end, a walker with a map, a SENTRET lookout (interactable), a field sign, a rest bench, plus return-visit lines for the guide and the three trainers once the player has badge 1 (`FLAG_BADGE01_GET`, no new flag).
- **Scheme 1 surveyors (moved here from Route 2, 2026-10-01):** two men in suits with clipboards (not trainers) and a worried local, so the Crestfall consultants are foreshadowed before the gym. Labels `SurveyorA/B`, `LocalWorried` in `route1.inc`.
- **Troglodyte sighting** (optional): a farmer says a rich boy came through. Can be cut.

## Connections
West edge to Hollowbrook's east gap (offset so they line up). East edge to Crestfall: `right` offset -5 (Crestfall has `left` +5), built 2026-10-01. The east path was trimmed to two rows (10-11) to meet Crestfall's road (rows 15-16).

## Events to place (me, after the author pushes the map)
Three trainers, the guide, two hidden items, two signs, and the connections. No triggers needed.

## As built (2026-10-01, updated after the merge: Crestfall end, levels +1)

| What | Where |
|---|---|
| West sign (WEST: HOLLOWBROOK, EAST: CRESTFALL) / east sign / field sign | (10,11) / (50,11) / (22,8) |
| Guide (3 POTIONs once, `FLAG_VELDRIS_ROUTE1_GUIDE_POTIONS`; after-badge line) | (12,12), faces west |
| Youngster TOBY, Lillipup 4, sight 4 | (24,13), faces west |
| Lass MAISIE, Zigzagoon 4 + Skitty 4, sight 3 | (38,15), faces west |
| Farmer AMOS (Hiker stand-in), Zigzagoon 5 + Skitty 5, sight 4 | (46,14), faces west |
| Troglodyte-sighting farmer (wanders) | (32,9) |
| Bucket kid / walker (wanders) / SENTRET lookout | (7,10) / (36,12) / (41,9) |
| Scheme 1 surveyors A and B (main lines before badge 1, 'After' lines once `FLAG_BADGE01_GET` is set) / worried local | (49,14), (54,13) / (44,12) |
| Hidden POTION / REPEL | (27,13) / (44,17) |

11 objects. Wild table as above (levels 3-5), rate 20. All three trainers and the guide switch to their after-badge lines on `FLAG_BADGE01_GET` (no new flag). **Not placed:** the rest bench (`RestBench`), because the Gen 4 tiles have no bench yet. Ledges are blocked tiles with the jump-south behaviour (as vanilla); the brown vertical edges are walls. **Checked in mGBA:** walking across from Hollowbrook (no seam), the guide's gift and repeat line, a wild Lillipup in the grass, TOBY's full battle (at the old level 3), a ledge jump, the new west sign. Not checked: MAISIE, AMOS, the new NPCs' lines, the hidden items.
