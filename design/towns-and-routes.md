# Towns and routes

Fixed by the author: **18 towns, 33 routes.** Status legend: PROPOSED / APPROVED / BUILT (see [README.md](README.md)).

Only the first 3 towns and 3 routes are named for now, so they can be flown between. Everything else is a numbered placeholder. **The names of towns 1 to 3 are APPROVED** (author, 2026-09-29): Hollowbrook, Wendlebury, and Crestfall (from the author's `TRAINER_CRESTFALL_GRETA`, the first gym town). Everything else is a placeholder.

Where each map comes from (Palladium references and vanilla bases): [map-plan.md](map-plan.md). Map cells, connections and the full section list for all 18 towns and 33 routes are in [region-map.md](region-map.md) (layout proposal). Towns 4 to 18 and routes 4 to 33 keep placeholder names until the author names them.

## Naming convention (PROPOSED)

The tree still carries FRLG's map folders and constants. They are not built into this Emerald ROM, but names such as `Route1_Frlg` and `MAPSEC_ROUTE_1` to `MAPSEC_ROUTE_25` exist. To stay clear of them and of Hoenn's:

- Town map folders use the town name: `Hollowbrook`, `Wendlebury`, `Crestfall`.
- Route map folders use a `VeldrisRoute` prefix: `VeldrisRoute1` to `VeldrisRoute33`.
- Map constants follow from the folder name (`MAP_VELDRIS_ROUTE1`). Map sections use `MAPSEC_VELDRIS_ROUTE_1` and `MAPSEC_HOLLOWBROOK`.
- Indoor maps append the building: `Hollowbrook_ProfFennickLab`, `Crestfall_Gym`, `Crestfall_PokemonCenter_1F`.
- Goldsworth houses (PROPOSED): `<Town>_GoldsworthHouse`, for example `Hollowbrook_GoldsworthHouse`, all on one shared layout.

## Towns

| # | Name | Role | Status | Map section | Built? |
|---|---|---|---|---|---|
| 1 | Hollowbrook | Start town, Prof. Fennick's lab | APPROVED (name) | `MAPSEC_HOLLOWBROOK` | No |
| 2 | Wendlebury | Second town, Pokémon Center and shop | APPROVED (name) | `MAPSEC_WENDLEBURY` | No |
| 3 | **Crestfall** | Gym 1: Greta (Normal, retired farmer) | APPROVED (name, from the author's trainer constant) | `MAPSEC_CRESTFALL` | No |
| 4 to 18 | TBD | Gyms 2 to 9, Elite Four approach, League, post-game | Not started | | |

## Routes

| # | Name | Connects | Status | Map section | Built? |
|---|---|---|---|---|---|
| 1 | VeldrisRoute1 | Hollowbrook and Wendlebury | PROPOSED | `MAPSEC_VELDRIS_ROUTE_1` | No |
| 2 | VeldrisRoute2 | Wendlebury and Crestfall | PROPOSED | `MAPSEC_VELDRIS_ROUTE_2` | No |
| 3 | VeldrisRoute3 | Crestfall onwards to town 4. Blocked for now (gate or barricade) so the first three towns stand alone | PROPOSED | `MAPSEC_VELDRIS_ROUTE_3` | No |
| 4 to 33 | TBD | | Not started | | |

## Goldsworth houses and the skyscraper (author note 2026-09-29; details PROPOSED)

Every town has a Goldsworth house (17 or 18 maps depending on decision 8 in [game-bible.md](game-bible.md)). One town has the Goldsworth skyscraper. How they are built: [map-plan.md](map-plan.md). Town roles in the table above are not changed yet, and the houses are added per town as each town is built.

## Fly destinations

Only towns are fly destinations (see [region-map.md](region-map.md)). Initial set: Hollowbrook, Wendlebury, Crestfall.

## Update this file when

A map is created in Porymap, renamed, or changes status; when a route or town gets its real name; when a map section is added.
