# Route 2 (VeldrisRoute2): Crestfall to Wendlebury

Status: **PROPOSED**. Everything here is a draft until the author approves it. Map: not started. South end Crestfall (a **town**, author 2026-10-01), north end Wendlebury. It is now a **post-gym-1** road, so levels were raised on 2026-10-01 (see below). Dialogue: [dialogue/route2.inc](dialogue/route2.inc).

## Feel
Farm country, gentle but a step up from Route 1: more trainers, slightly higher levels, hay and fences. All Normal and other common early Pokémon. No real animals.

## Wild Pokémon (PROPOSED, land only, no water)
Tall-grass tiles only. Levels 8 to 11 (was 4 to 7 before the order changed; PROPOSED). Standard 12-slot rates (20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1).

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | ZIGZAGOON | 8 to 9 |
| 2 | 20% | PATRAT | 8 to 9 |
| 3 | 10% | LILLIPUP | 8 to 9 |
| 4 | 10% | SENTRET | 9 |
| 5 | 10% | PIDOVE | 9 to 10 |
| 6 | 10% | SKITTY | 9 to 10 |
| 7 | 5% | BIDOOF | 10 |
| 8 | 5% | PATRAT | 10 to 11 |
| 9 | 4% | MEOWTH | 10 to 11 |
| 10 | 4% | PIDOVE | 11 |
| 11 | 1% | SLAKOTH | 11 |
| 12 | 1% | MILTANK | 11 |

Rates add to 100%. Every species was checked to exist in `src/data/pokemon/species_info/`. SLAKOTH and MILTANK appear in the Crestfall gym, so they stay at 1%. Porymap writes these to `wild_encounters.json` through its Wild Pokémon tab.

## Trainers (PROPOSED, four)
All reuse vanilla Hoenn trainer entries (no new trainer id, UNTESTED, see `CLAUDE.md` 'A new trainer'). No IVs or EVs. Moves left to the default level-up set.

| Trainer | Team | Notes |
|---|---|---|
| Youngster | PATRAT L8, LILLIPUP L8 | Easiest |
| Lass | SKITTY L9, PIDOVE L9 | |
| Farmer | ZIGZAGOON L9, SENTRET L10 | Also hints at the surveyors |
| Camper | BIDOOF L10, MEOWTH L11 | The toughest on the road, near Crestfall |

## NPCs and items
- **Guide:** near the south end, gives a REPEL once. Needs one flag (planned, unclaimed).
- **Scheme 1 leftovers:** the surveyors now live on Route 1 ([route1.md](route1.md)). Here only a dropped clipboard remains (`SurveyorLeftover`).
- **Troglodyte sighting** (optional): a walker saw him storm north. No battle here. Can be cut.
- **Ambient:** a gym fan and a worried local.
- **Hidden items (PROPOSED):** a POTION and an ANTIDOTE in the grass. Placed in Porymap or by me after the map is pushed.
- **Signs:** three (south end, middle, north end).

## Connections
South edge to Crestfall. North edge to Wendlebury. (Directions follow the sketch loosely: Wendlebury is north-east of Crestfall; the map shape is the author's call.)

## Events to place (me, after the author pushes the map)
Four trainers, the guide, the leftover clipboard, the sighting NPC, two ambient NPCs, two hidden items, three signs, and the connections. No triggers needed. One flag for the guide's REPEL (planned, unclaimed, see [flags.md](flags.md)).
