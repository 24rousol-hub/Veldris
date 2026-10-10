# Wendlebury (town 3)

Status: **PROPOSED** except the name (approved 2026-09-29). Map plan: [map-plan.md](map-plan.md) (base `OldaleTown`, reference `Cherrygrove City.png`, about 51 x 29). Dialogue: [dialogue/wendlebury.inc](dialogue/wendlebury.inc).

## Role
A market crossroads off the main path, reached from Crestfall by Route 2 (changed 2026-10-01: Crestfall is now the first stop and Wendlebury the third place). Pokémon Center, Mart, and the crossroads. The player hears the gossip about the Goldsworths and about the Crestfall scheme here. It has no gym. It is a **town** (author, 2026-09-30), so it has no Goldsworth house. The next stop, Crestfall, is a city.

## Where it sits
Route 2 from Crestfall (south or west edge, map shape undecided). The sketch also joins it to city 4 and, by water, to the south-centre city. East edge: a blocked exit toward the later routes (R16 on the region plan), shut by a barricade until the author says otherwise. South edge: sea or trees.

## Buildings (all interiors reuse vanilla layouts, no painting)
| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F and 2F | `LAYOUT_POKEMON_CENTER_1F` and `_2F` | Nurse, a visitor, a 2F trading and battling counter if kept |
| Mart | `LAYOUT_MART` | Clerk. Stock: POKé BALL, POTION, ANTIDOTE, PARALYZE HEAL (first stock, proposed) |
| Two houses | `LAYOUT_HOUSE1`, `LAYOUT_HOUSE2` | Ordinary residents |
| A market stall row | exterior objects only | Gives the town its character, NPCs behind stalls |

## Flavour (PROPOSED)
A small market crossroads. Traders pass through on the way to the gym. Things run on signs and on gossip. The joke: everyone has heard of the Goldsworths and nobody has met one.

## NPCs (text in [dialogue/wendlebury.inc](dialogue/wendlebury.inc))
Sign, Center nurse (shared wording with Crestfall's), Mart clerk, a market trader, a kid, a gossip, a traveller who warns about the route north, a man on the barricade. The traveller now talks about Crestfall's hay maze (Scheme 1 is foreshadowed on Route 1 instead).

## Added 2026-10-01 (dialogue only)
Two market sellers (berries, tea), a second Center visitor, a 2F counter clerk, a Mart shopper, House 1 (resident, SLAKOTH, shelf), House 2 (resident, child, TV), a Troglodyte sighting, and four return-visit lines after Crestfall's gym (`FLAG_BADGE01_GET`, no new flag). The gossip line calls back Scheme 1.

## Villain teams (author, 2026-10-04)

- **The Commons leader lives in a house here**, met as an ordinary local; who they are is a surprise revealed later (author). PROPOSED: after the talk the Commons grunts blocking Route 3 leave, which is why Route 3 opens after Wendlebury.
- Story order (author): Crestfall, then Wendlebury, then Route 3 to Briarwick. See [factions.md](factions.md).

## To place after the map is pushed
Warps for each door, signs, the NPCs above, the heal location (two traps: `respawn_map` before `respawn_npc`, see CLAUDE.md), and the Route 1 and Route 2 connections. No triggers, no new flags.
