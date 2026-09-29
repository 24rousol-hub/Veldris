# Map plan

**Decision (author, 2026-09-29):** a mix. Use the **Project Palladium** maps from the Team Aqua repo where they fit, and **vanilla bases** for the rest. The rule stands: reuse existing maps, never draw from scratch, and never use another hack's maps without permission (Palladium's README gives it, see below).

## What Palladium is, and what it is not

- **Images, not map files.** `Team-Aquas-Asset-Repo/Maps/Project Palladium/` holds 128 screenshots of a cancelled Johto (Gold/Silver remake) project. There is no `map.json` and no `map.bin`. So "using" a map means the author **traces it in Porymap by eye**, with the image beside it as a blueprint. Nothing can be imported.
- **Sizes.** 56 of the images have a 1 px grid line every 16 px, so their size in tiles is `(pixels - 1) / 17`. Stripping those lines would probably give clean 16 px tiles (untested). For the rest, tiles are about `pixels / 16`.
- **The art is not identical to our tilesets.** Palladium uses Gen 3-style tiles. The author approximates them with the tilesets already in the tree, or LeoB ORAS.
- **Permission, as written.** The folder README says: "The project team release all of their assets to the public for free use" and "Please credit the entire team for used assets." Its source URL is dead (one Wayback capture from 2018), so this cannot be verified. The author has chosen to rely on it.
- **Condition:** credit "Project Palladium team" in [`CREDITS.md`](../CREDITS.md), naming the files, in the same commit as the first traced map.
- **Leave out.** Files with other authors or unknown origin: `johtobuildings.PNG` (credits Gridiron, Kyledove and Pokémon Platinum art), the two `..._by_lostimpact-...` images, and `New Bark Town Lab tile.png` (a comic, not a map). Treat hash-named uploads (for example `bobhx7.png`) as unconfirmed and check with the author before using them.
- **Layouts are Game Freak's Johto designs, redrawn by the team.** That is the same footing as the vanilla Hoenn maps upstream already ships, but it is a fan project's redraw. Noted for a public repo. The author's call.

## Plan for the first three towns and routes (PROPOSED)

The Johto start lines up with Veldris' first stretch: New Bark Town, Route 29, Cherrygrove, Route 30, and so on. Sizes are in tiles. Every one is well inside the engine's map-size limit `(width + 15) * (height + 14) <= 10240`.

| Veldris map | Palladium reference | Tiles | Vanilla alternative or base |
|---|---|---|---|
| **Hollowbrook** (town) | `New Bark Town.png` | 32 x 28 | `LittlerootTown` |
| Hollowbrook: Prof. Fennick's lab | `Elm's Lab.png` | 13 x 14 | `LittlerootTown_ProfessorBirchsLab` |
| Hollowbrook: player's house 1F | `Hero's House 1st Floor.png` | about 13 x 9 | `LittlerootTown_BrendansHouse_1F` |
| Hollowbrook: player's house 2F | `Hero's House 2nd Floor.png` | 14 x 11 | `LittlerootTown_BrendansHouse_2F` |
| Hollowbrook: neighbour's house | `Elm's House.png` | 13 x 10 | `LittlerootTown_MaysHouse_1F` |
| **Route 1** | `Route 29.png` | 60 x 25 | `Route101` |
| **Wendlebury** (town) | `Cherrygrove City.png` | about 51 x 29 | `OldaleTown` |
| Wendlebury: Pokémon Center 1F and 2F | (Palladium `PokeMon Center Johto.PNG`, about 16 x 22, is an alternative) | | `OldaleTown_PokemonCenter_1F`, `_2F` |
| Wendlebury: Mart | | | `OldaleTown_Mart` |
| **Route 2** | `Route 30.png` | 37 x 59 | `Route102` |
| **Crestfall** (town, gym 1) | `Azalea Town.png` | about 48 x 32 | `PetalburgCity` |
| Crestfall: Greta's gym | `Azalea Town Gym.png` | 15 x 17 | `PetalburgCity_Gym` (Normal type in vanilla too) |
| **Route 3** (blocked at first) | `Route 31.png` | 46 x 22 | `Route104` |

Pokémon Centers and Marts should come from the vanilla maps above, since each town needs one and Palladium has no Mart. Fitting a Johto route to a Veldris route is a proposal. The region-map shape is independent of it.

## Vanilla bases for everything else

- **Interiors** (Pokémon Centers, Marts, houses, other gyms): start from the vanilla maps in the tree. They are official and already in upstream, so nothing extra to credit.
- **Towns and routes Palladium does not cover:** start from Hoenn maps in the same way. Palladium has 16 route images (Routes 29 to 46 with gaps) against Veldris' 33 routes, so about half the routes come from vanilla.
- The FRLG maps in the tree are not built into this Emerald ROM and use another layout format, so they are not usable as bases here.

## Who does what

1. **The author (Porymap):** trace the map, starting from the vanilla base where one exists, with the Palladium image beside it. Keep the map's `region` at `REGION_HOENN` and `layout_version` at `emerald`.
2. **Claude:** the wiring. That is the `.include` line in `data/event_scripts.s` that Porymap does not write, the region-map section, warps, triggers, scripts, dialogue and trainers. Claude also updates [towns-and-routes.md](towns-and-routes.md), [flags.md](flags.md) and `CREDITS.md`, and checks the build.
3. See "Adding things" in `CLAUDE.md` for the four-step new-map checklist.

## Open items

- Confirm the mapping above, or swap any pairing.
- Which Palladium images cover towns 4 to 18 and routes 4 to 33: decide as each comes up.
- Whether to use any hash-named uploads.
