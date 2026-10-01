# Crestfall (town 3, gym 1) - city plan

Status: **PROPOSED** except the name and Greta (approved earlier) and that Crestfall is a **city** (author, 2026-09-30). Everything else below is a suggestion. Map plan: [map-plan.md](map-plan.md) (reference `Azalea Town.png`, about 48 x 32, vanilla base `PetalburgCity`). Dialogue: [dialogue/crestfall.inc](dialogue/crestfall.inc) and [dialogue/crestfall_extra.inc](dialogue/crestfall_extra.inc).

## Role
Normal type farm city and the first gym. It is a city, so it has a **Goldsworth house** (NPC only). The skyscraper is **not** here unless the author says so. Greta is the leader (`TRAINER_CRESTFALL_GRETA`, STANDARD BADGE). Scheme 1 plays out here.

## Where it sits
South: Route 2 from Wendlebury. North or east: Route 3 onward to town 4, blocked for now. Farmland and the gym's hay maze fill the north and west sides, the market square and houses the south and middle. PROPOSED.

## Buildings
| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F and 2F | `LAYOUT_POKEMON_CENTER_1F` and `_2F` | Shared, no painting. Nurse, visitor (in `crestfall.inc`) |
| Mart | `LAYOUT_MART` | Shared. Clerk (in `crestfall.inc`) plus shopkeeper (extra) |
| Gym | custom, base `Azalea Town Gym.png` (see map-plan) | Greta, two trainers, hay maze, guide statue |
| Goldsworth house | shared house layout (see map-plan) | NPC only, build last with the other Goldsworth houses |
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
1. **Setup** (before the gym): consultant outside in town; locals and the old farmer grumble; Route 2 traveller in Wendlebury hints first.
2. **Reveal**: consultant boss and junior at the gym door, with the junior lost in the hay maze.
3. **Collapse**: Greta's MILTANK eat the paperwork, at the gym door (coord_event trigger, per CLAUDE.md).
4. **Troglodyte arrives and battles** (his second fight), then Greta invites the player in.
5. **Gym battle**, badge and CUT. Afterward the town NPCs switch to their 'After' text.

## Flags (not claimed)
One flag or var for the Scheme 1 stage is needed, and one for the gym-beaten state (`FLAG_BADGE01_GET` already exists for the After text). Claim them in [flags.md](flags.md) when the map is built.

## Open questions
- Flying: [towns-and-routes.md](towns-and-routes.md) says only towns are fly destinations, but Crestfall is a city and a listed fly destination. Decide.
- Does the skyscraper go in a later city? Not here unless the author says.
- Greta's farm link (see [characters.md](characters.md)).
