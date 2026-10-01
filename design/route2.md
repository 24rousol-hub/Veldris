# Route 2 (VeldrisRoute2): Wendlebury to Crestfall

Status: **PROPOSED**. Everything here is a draft until the author approves it. Map: not started. South end Wendlebury (north edge), north end Crestfall (a **city**, author 2026-09-30). Dialogue: [dialogue/route2.inc](dialogue/route2.inc).

## Feel
Farm country, gentle but a step up from Route 1: more trainers, slightly higher levels, hay and fences. All Normal and other common early Pokémon. No real animals.

## Wild Pokémon (PROPOSED, land only, no water)
Tall-grass tiles only. Levels 4 to 7. Standard 12-slot rates (20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1).

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | ZIGZAGOON | 4 to 5 |
| 2 | 20% | PATRAT | 4 to 5 |
| 3 | 10% | LILLIPUP | 4 to 5 |
| 4 | 10% | SENTRET | 5 |
| 5 | 10% | PIDOVE | 5 to 6 |
| 6 | 10% | SKITTY | 5 to 6 |
| 7 | 5% | BIDOOF | 6 |
| 8 | 5% | PATRAT | 6 to 7 |
| 9 | 4% | MEOWTH | 6 to 7 |
| 10 | 4% | PIDOVE | 7 |
| 11 | 1% | SLAKOTH | 7 |
| 12 | 1% | MILTANK | 7 |

Rates add to 100%. Every species was checked to exist in `src/data/pokemon/species_info/`. SLAKOTH and MILTANK appear in the Crestfall gym, so they stay at 1%. Porymap writes these to `wild_encounters.json` through its Wild Pokémon tab.

## Trainers (PROPOSED, four)
All reuse vanilla Hoenn trainer entries (no new trainer id, UNTESTED, see `CLAUDE.md` 'A new trainer'). No IVs or EVs. Moves left to the default level-up set.

| Trainer | Team | Notes |
|---|---|---|
| Youngster | PATRAT L5, LILLIPUP L5 | Easiest |
| Lass | SKITTY L6, PIDOVE L6 | |
| Farmer | ZIGZAGOON L6, SENTRET L7 | Also hints at the surveyors |
| Camper | BIDOOF L7, MEOWTH L8 | The toughest on the road, near Crestfall |

## NPCs and items
- **Guide:** near the south end, gives a REPEL once. Needs one flag (planned, unclaimed).
- **Two surveyors (Scheme 1 foreshadowing):** men in suits with clipboards, planting markers along the road. They are not trainers and do not battle. Together with the Wendlebury traveller they set up `Crestfall_Text_ConsultantOutside` in [dialogue/crestfall.inc](dialogue/crestfall.inc).
- **Troglodyte sighting** (optional): a walker saw him storm north. No battle here. Can be cut.
- **Ambient:** a gym fan and a worried local.
- **Hidden items (PROPOSED):** a POTION and an ANTIDOTE in the grass. Placed in Porymap or by me after the map is pushed.
- **Signs:** three (south end, middle, north end).

## Connections
South edge to Wendlebury's north edge (offset so they line up). North edge to Crestfall.

## Events to place (me, after the author pushes the map)
Four trainers, the guide, two surveyors, the sighting NPC, two ambient NPCs, two hidden items, three signs, and the connections. No triggers needed. One flag for the guide's REPEL (planned, unclaimed, see [flags.md](flags.md)).
