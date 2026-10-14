# DRIFTSANDS (town, beach town; the sketch gives it no number)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)). Template and rules: [../README.md](../README.md). Roads: R24 and R25 in [../routes-south.md](../routes-south.md). Neighbours: [kingsquay.md](kingsquay.md), [beaconmouth.md](beaconmouth.md).

## Role in the story

- A **breather town** before the last gym: a small, sunny beach town with deck chairs and a slightly too-quiet Pokémon Center. No gym, no scheme of its own, no Goldsworth house (a town gets none).
- A **Scheme 9 gag**: the junior clerk **Pip** (PROPOSED, from Kingsquay) is sitting on the beach with a parasol, reading invoices in the sun, and has dropped one. The player can hand it back, which does nothing, or leave it. A small deadpan beat to show the lawyers are on the road ahead of the player.
- Where the player hears that the old town of **Aldermere** sank 'two cliffs north-west of here' and how Dive will open it (post-game hint).
- A short tutorial of the sea: a small hidden-item hunt in the sand, a lifeguard who sells Net Balls and Dive Balls.
- Post-game: nothing new to unlock; a Swimmer rematch on the beach.

## Where it sits

South of Beaconmouth, east of Kingsquay.

| Road | Edge of Driftsands | How |
|---|---|---|
| R24 from Kingsquay | **West edge** | The fenced lane of R24 (Palladium Route 38) ends at a gate and narrows into a boardwalk |
| R25 to Beaconmouth | **North edge**, towards the north-east | A headland path, a cliff stair at the start |

## Source and size

- **Vanilla base: Dewford Town** (`DewfordTown_Layout`, 20 x 20). Dewford is the island beach town: a small harbour, a hall, a gym (not needed here). Enlarge to **about 30 x 24**: `(30 + 15) * (24 + 14) = 1710`.
- **Palladium:** none. A beach reference is the sand edge of `Route 40.png` (20 x 34, a sea route with a beach and gatehouse).
- **Section id:** `MAPSEC_DRIFTSANDS` (name `DRIFTSANDS`, 10 chars).
- **Fly and heal:** a fly destination. One row in `src/data/veldris_fly_towns.h`, plus `HEAL_LOCATION_DRIFTSANDS`.

## Layout

- **West boardwalk (R24 arrival).** A wooden walkway, a sign, a lifeguard tower on stilts (decorative, with the lifeguard standing at its foot).
- **The Lido (middle).** A line of beach huts. The Pokémon Center door faces the sea. The Mart (a kiosk) next to it.
- **Beach (south).** Soft sand with deck chairs, a parasol, two Tubers on floats (not trainers), a sandcastle. Hidden items in the sand. A rowing boat tied to a post (decorative).
- **Tide pool (south-east).** A shallow pool with a visible Pearl.
- **North cliff and R25 stair (top right).** The stair is the town's north exit.
- No tall grass in town. The beach has no wild encounters; encounters are on the roads.

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | Shared |
| Kiosk Mart | `LAYOUT_MART` | Net Ball, Dive Ball, Super Potion, Hyper Potion, Super Repel |
| Beach Hall | `DewfordTown_Hall` style, or `LAYOUT_HOUSE2` | The 'Sand Museum': a tiny room with sand sculptures, a sculptor, the TM Sandstorm gift |
| Lifeguard's Hut | `LAYOUT_HOUSE1` | The Net Ball seller, a first-aid shelf |
| Beachcomber's Cottage | `LAYOUT_HOUSE2` | Soft Sand, Heart Scale swap (a Heart Scale for a Shell Bell, once) |
| Two houses | `LAYOUT_HOUSE1` | A family, a sunburnt couple |

## NPCs

8 to 14 for a town.

| Role | Where | Topic |
|---|---|---|
| Lifeguard | At the tower foot | Warns about the tide and the deep sea beyond; sells Net Balls |
| Junior clerk Pip (PROPOSED) | Beach, under a parasol | Sunburnt, reading invoices. 'One went. Wind.' Optional return of the dropped invoice |
| Sculptor | Beach Hall | Sandcastles. Gives **TM Sandstorm** (PROPOSED) |
| Beachcomber | Cottage | Trades a Shell Bell for a Heart Scale |
| Old boatman | Jetty | Says the sunken town of Aldermere is north-west; a Dive-able trainer can enter the old streets |
| Kid with bucket | Beach | A sand-in-the-pail joke, no items |
| Swimmer (rematch) | Beach shallows | A trainer, post-game rematch |
| Tuber and Tuber | Beach | Not trainers: float, talk about the heat |
| Couple | House | 'We came for a day. That was nine years ago.' |
| Pokémon Center nurse and clerk | Center, kiosk | Standard |
| Fan | A house | A Beaconmouth-bound fan who says the lighthouse leaks |
| Ranger | North stair | Warns the cliff road 'has a water problem' (the R25 stream) |

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| TM Sandstorm | Beach Hall sculptor | Story: speak to him twice |
| Soft Sand | Beachcomber's shelf | None |
| Shell Bell | Beachcomber trade | A Heart Scale |
| Pearl | Tide pool (visible) | None |
| Big Pearl | Sand dune (hidden) | None |
| Heart Scale x2 | Two sand spots (hidden) | None |
| Stardust | Behind the lifeguard tower (hidden) | None |
| Max Elixir | Rowing boat (visible, post-game) | After the League |

## Flags (not claimed)

- `FLAG_VISITED_DRIFTSANDS`.
- `FLAG_RECEIVED_TM_SANDSTORM`, `FLAG_RECEIVED_SHELL_BELL`.
- `FLAG_DRIFTSANDS_PIP_MET` (clerk beat).
- Hidden items: `FLAG_HIDDEN_ITEM_DRIFTSANDS_BIG_PEARL`, `_HEART_SCALE_1`, `_HEART_SCALE_2`, `_STARDUST`.

## Build order and effort

**Easy.** Dewford is small and nearly the right shape; the layout only needs stretching and a stair. All interiors are shared layouts or small houses. Build after R24, before R25.

## Open questions

1. Should the beach carry real encounters? I put none in town, so the wild tables on R24 and R25 are the only ones.
2. Is the Pip-and-the-invoice gag welcome, or should Driftsands stay silent on Scheme 9?
3. Dewford is an island town in Hoenn; the sketch draws Driftsands on the mainland. Fine, it just needs a land exit and a stair.
