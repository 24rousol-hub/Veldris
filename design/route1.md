# Route 1 (VeldrisRoute1): Hollowbrook to Wendlebury

Status: **PROPOSED**. Everything here is a draft until the author approves it. Map: 60 x 25, traced from `Route 29.png`, west end Hollowbrook (connection on Hollowbrook's right edge, author 2026-09-30), east end Wendlebury. Dialogue: [dialogue/route1.inc](dialogue/route1.inc).

## Feel
Farm country, gentle, a first walk. All Normal and other common early Pokémon. No real animals.

## Wild Pokémon (PROPOSED, land only, no water)
Tall-grass tiles only. Levels 2 to 4. Standard 12-slot rates (20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1).

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | ZIGZAGOON | 2 to 3 |
| 2 | 20% | LILLIPUP | 2 to 3 |
| 3 | 10% | BIDOOF | 2 to 3 |
| 4 | 10% | SENTRET | 2 to 3 |
| 5 | 10% | ZIGZAGOON | 3 |
| 6 | 10% | LILLIPUP | 3 |
| 7 | 5% | BIDOOF | 3 to 4 |
| 8 | 5% | SENTRET | 3 to 4 |
| 9 | 4% | SKITTY | 3 to 4 |
| 10 | 4% | SKITTY | 4 |
| 11 | 1% | SLAKOTH | 4 |
| 12 | 1% | MILTANK | 4 |

Rates add to 100%. I have not checked that every species is enabled in this build. SLAKOTH and MILTANK appear in the Crestfall gym, so they stay at 1% here. Porymap writes these to `wild_encounters.json` through its Wild Pokémon tab.

## Trainers (PROPOSED, three, all cheap to add)
All three reuse vanilla Hoenn trainer entries (no new trainer id, UNTESTED, see `CLAUDE.md` 'A new trainer'). No IVs or EVs, as for every trainer. Moves left to the default level-up set.

| Trainer | Team | Notes |
|---|---|---|
| Youngster | LILLIPUP L3 | Easy first fight |
| Lass | ZIGZAGOON L3, SKITTY L3 | Two-Pokémon fight |
| Farmer | ZIGZAGOON L4, SKITTY L4 | The toughest on the road |

## NPCs and items
- **Guide:** near the west end, gives 3 POTIONs once. Needs one flag (planned, unclaimed).
- **Hidden item or two:** a POTION and a REPEL in the grass, to reward exploring. Placed in Porymap or by me after the map is pushed.
- **Troglodyte sighting** (optional): a farmer says a rich boy came through. Can be cut.

## Connections
West edge to Hollowbrook's east gap (offset so they line up). East edge to Wendlebury.

## Events to place (me, after the author pushes the map)
Three trainers, the guide, two hidden items, two signs, and the connections. No triggers needed.
