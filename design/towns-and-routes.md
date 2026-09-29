# Towns and routes

Fixed by the author: **18 towns, 33 routes.** Status legend: PROPOSED / APPROVED / BUILT (see [README.md](README.md)).

Only the first 3 towns and 3 routes are named for now, so they can be flown between. Everything else is a numbered placeholder. **All names below are PROPOSED.** Only **Crestfall** is implied by the author (`TRAINER_CRESTFALL_GRETA`), and it is assumed to be the first gym town.

## Naming convention (PROPOSED)

The tree already contains the full Hoenn and FRLG maps, and FRLG already owns names such as `Route1_Frlg` and `MAPSEC_ROUTE_1` to `MAPSEC_ROUTE_25`. To stay clear of both:

- Town map folders use the town name: `Hollowbrook`, `Wendlebury`, `Crestfall`.
- Route map folders use a `VeldrisRoute` prefix: `VeldrisRoute1` to `VeldrisRoute33`.
- Map constants follow from the folder name (`MAP_VELDRIS_ROUTE1`). Map sections use `MAPSEC_VELDRIS_ROUTE_1` and `MAPSEC_HOLLOWBROOK`.
- Indoor maps append the building: `Hollowbrook_ProfFennickLab`, `Crestfall_Gym`, `Crestfall_PokemonCenter_1F`.

## Towns

| # | Name | Role | Status | Map section | Built? |
|---|---|---|---|---|---|
| 1 | Hollowbrook | Start town, Prof. Fennick's lab | PROPOSED | `MAPSEC_HOLLOWBROOK` | No |
| 2 | Wendlebury | Second town, Pokémon Center and shop | PROPOSED | `MAPSEC_WENDLEBURY` | No |
| 3 | **Crestfall** | Gym 1: Greta (Normal, retired farmer) | Name implied by the author | `MAPSEC_CRESTFALL` | No |
| 4 to 18 | TBD | Gyms 2 to 9, Elite Four approach, League, post-game | Not started | | |

## Routes

| # | Name | Connects | Status | Map section | Built? |
|---|---|---|---|---|---|
| 1 | VeldrisRoute1 | Hollowbrook and Wendlebury | PROPOSED | `MAPSEC_VELDRIS_ROUTE_1` | No |
| 2 | VeldrisRoute2 | Wendlebury and Crestfall | PROPOSED | `MAPSEC_VELDRIS_ROUTE_2` | No |
| 3 | VeldrisRoute3 | Crestfall onwards to town 4. Blocked for now (gate or barricade) so the first three towns stand alone | PROPOSED | `MAPSEC_VELDRIS_ROUTE_3` | No |
| 4 to 33 | TBD | | Not started | | |

## Fly destinations

Only towns are fly destinations (see [region-map.md](region-map.md)). Initial set: Hollowbrook, Wendlebury, Crestfall.

## Update this file when

A map is created in Porymap, renamed, or changes status; when a route or town gets its real name; when a map section is added.
