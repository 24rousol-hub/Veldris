# Wendlebury (town 2)

Status: **PROPOSED** except the name (approved 2026-09-29). Map plan: [map-plan.md](map-plan.md) (base `OldaleTown`, reference `Cherrygrove City.png`, about 51 x 29). Dialogue: [dialogue/wendlebury.inc](dialogue/wendlebury.inc).

## Role
The player's first real stop: Pokémon Center, Mart, and the crossroads. It is the first place that sells things, and the first place the player hears about Troglodyte's family as a public nuisance. It has no gym. It is a **town** (author, 2026-09-30), so it has no Goldsworth house. The next stop, Crestfall, is a city.

## Where it sits
West of it: Hollowbrook, by Route 1 (enters on Wendlebury's west edge). North: Route 2 to Crestfall (leaves on the north edge). East edge: a blocked exit toward the later routes (R16 on the region plan), shut by a barricade until the author says otherwise. South edge: sea or trees.

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
Sign, Center nurse (shared wording with Crestfall's), Mart clerk, a market trader, a kid, a gossip, a traveller who warns about the route north, a man on the barricade. The Route 2 traveller hints that a rich boy hired men in suits to Crestfall, which sets up Scheme 1.

## Added 2026-10-01 (dialogue only)
Two market sellers (berries, tea), a second Center visitor, a 2F counter clerk, a Mart shopper, House 1 (resident, SLAKOTH, shelf), House 2 (resident, child, TV), a Troglodyte sighting, and four return-visit lines after Crestfall's gym (`FLAG_BADGE01_GET`, no new flag). The gossip line calls back Scheme 1.

## To place after the map is pushed
Warps for each door, signs, the NPCs above, the heal location (two traps: `respawn_map` before `respawn_npc`, see CLAUDE.md), and the Route 1 and Route 2 connections. No triggers, no new flags.
