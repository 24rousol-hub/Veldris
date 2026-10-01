# Route 1 (VeldrisRoute1): Hollowbrook to Crestfall

Status: **PROPOSED**. Everything here is a draft until the author approves it. Map: 60 x 25, traced from `Route 29.png`, west end Hollowbrook (connection on Hollowbrook's right edge, author 2026-09-30), east end **Crestfall** (changed 2026-10-01 from Wendlebury, per the author's sketch: [region-sketch.md](region-sketch.md)). Dialogue: [dialogue/route1.inc](dialogue/route1.inc).

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
West edge to Hollowbrook's east gap (offset so they line up). East edge to Crestfall.

## Events to place (me, after the author pushes the map)
Three trainers, the guide, two hidden items, two signs, and the connections. No triggers needed.
