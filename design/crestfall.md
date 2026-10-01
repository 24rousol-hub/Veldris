# Crestfall (town 2, gym 1) - town plan

Status: **PROPOSED** except the name and Greta (approved earlier) and that Crestfall is a **town** (author, 2026-10-01, replacing the earlier 'city'; the sketch also draws it purple). Everything else below is a suggestion. Map plan: [map-plan.md](map-plan.md) (reference `Azalea Town.png`, about 48 x 32, vanilla base `PetalburgCity`). Dialogue: [dialogue/crestfall.inc](dialogue/crestfall.inc) and [dialogue/crestfall_extra.inc](dialogue/crestfall_extra.inc).

## Role
Normal type farm town and the first gym, one road from Hollowbrook. It is a town, so it has **no Goldsworth house** (changed 2026-10-01): the NPC-only cousin set below moves to **Briarwick** (approved 2026-10-01). The Center and Mart here are the player's first. The skyscraper is **not** here unless the author says so. Greta is the leader (`TRAINER_CRESTFALL_GRETA`, STANDARD BADGE). Scheme 1 plays out here.

## Where it sits
West: Route 1 from Hollowbrook. East or north-east: Route 2 to Wendlebury. North: Route 3 onward to city 4, blocked for now. Farmland and the gym's hay maze fill the north and west sides, the market square and houses the south and middle. PROPOSED.

## Buildings
| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F and 2F | `LAYOUT_POKEMON_CENTER_1F` and `_2F` | Shared, no painting. Nurse, visitor (in `crestfall.inc`) |
| Mart | `LAYOUT_MART` | Shared. Clerk (in `crestfall.inc`) plus shopkeeper (extra) |
| Gym | custom, base `Azalea Town Gym.png` (see map-plan) | Greta, two trainers, hay maze, guide statue |
| ~~Goldsworth house~~ | removed 2026-10-01 | A town gets none. Its draft lines (`GoldCousin*` and the rest in `crestfall_extra.inc`) are reused for the first city |
| House A (retired couple) | `LAYOUT_HOUSE1` | Ordinary residents |
| House B (stuck trainer) | `LAYOUT_HOUSE2` | Ordinary resident |
| Market square | exterior objects only | Three stalls, a fountain, signs |
| Farm and tomato patch | exterior objects only | Farmhands, old farmer, grandma |

Map names follow [towns-and-routes.md](towns-and-routes.md): `Crestfall`, `Crestfall_Gym`, `Crestfall_PokemonCenter_1F`, `Crestfall_GoldsworthHouse`, and so on.

## NPCs (all PROPOSED)
| NPC | Where | Label prefix `Crestfall_Text_` | File |
|---|---|---|---|
| Consultants (outside, boss, junior) | Town, gym door | `Consultant*` | crestfall |
| Local worried, farmhand, kid, grandma, visitor, clerk, nurse | Town, Center, Mart | `Local*`, `Farmhand*`, `Kid*`, `Grandma*` | crestfall |
| Greta and two gym trainers | Gym | `Greta*`, `Trainer1*`, `Trainer2*` | crestfall |
| Market berry, tomato, milk stalls | Square | `Market*` | extra |
| Two farmhands (fence, barn) | Farm road | `FarmhandFence*`, `FarmhandBarn*` | extra |
| Gym guide statue, signs | Gym, town | `GymStatue*`, `FarmSign`, `SquareSign` | extra |
| Retired couple | House A | `HouseA*` | extra |
| Stuck trainer | House B | `HouseB*` | extra |
| Second kid, old farmer | Square, farm | `KidSquare*`, `OldFarmer*` | extra |
| Shopkeeper | Mart | `Shopkeeper*` | extra |
| Goldsworth cousins (boaster, lounger, pet owner), butler | Goldsworth house | `GoldCousin*`, `GoldLounger*`, `GoldPetOwner`, `GoldButler` | extra |

Goldsworth house: the boaster cousin (BARNABY, name PROPOSED) brags about the family, per author. Residents swear mildly (PG-13) and are rude to the player, not cruel to townsfolk. No battle, no flag needed beyond the before/after-gym check.

## Where Scheme 1 beats happen
1. **Setup** (before the gym): consultant outside in town; locals and the old farmer grumble; the two surveyors on Route 1 hint first.
2. **Reveal**: consultant boss and junior at the gym door, with the junior lost in the hay maze.
3. **Collapse**: Greta's MILTANK eat the paperwork, at the gym door (coord_event trigger, per CLAUDE.md).
4. **Troglodyte arrives and battles** (his second fight), then Greta invites the player in.
5. **Gym battle**, badge and CUT. Afterward the town NPCs switch to their 'After' text.

## Flags (not claimed)
One flag or var for the Scheme 1 stage is needed, and one for the gym-beaten state (`FLAG_BADGE01_GET` already exists for the After text). Claim them in [flags.md](flags.md) when the map is built.

## Open questions
- Flying: Crestfall is a town, so this is settled: it is a fly destination.
- The skyscraper is in Central City (sketch), not here.
- Greta's farm link (see [characters.md](characters.md)).
