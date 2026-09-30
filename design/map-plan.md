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

## Plan for the first three towns and routes (APPROVED)

The author approved these pairings on 2026-09-29 ("the palladium and vanilla pairings looks great"). **Hollowbrook is the first map the author builds.** Later swaps are still fine; note them here.

The Johto start lines up with Veldris' first stretch: New Bark Town, Route 29, Cherrygrove, Route 30, and so on. Sizes are in tiles. Every one is well inside the engine's map-size limit `(width + 15) * (height + 14) <= 10240`.

| Veldris map | Palladium reference | Tiles | Vanilla alternative or base |
|---|---|---|---|
| **Hollowbrook** (town) | `New Bark Town.png` | 32 x 28 | `LittlerootTown` |
| Hollowbrook: Prof. Fennick's lab | `Elm's Lab.png` | 13 x 14 | `LittlerootTown_ProfessorBirchsLab`. **Needs a starter table**: paint a table at least 4 tiles wide (the picture's is 3) with a free tile in front of each of four Poké Ball spots. See 'Starters and the lab scene' in [story-outline.md](story-outline.md) |
| Hollowbrook: player's house 1F | `Hero's House 1st Floor.png` | about 13 x 9 | `LittlerootTown_BrendansHouse_1F` |
| Hollowbrook: player's house 2F | `Hero's House 2nd Floor.png` | 14 x 11 | `LittlerootTown_BrendansHouse_2F` |
| Hollowbrook: neighbour's house | `Elm's House.png` | 13 x 10 | `LittlerootTown_MaysHouse_1F` |
| Hollowbrook: Goldsworth house (the grandfather's, author) | none | | Shared house layout (see below). Post-game only: the door is locked until the League is beaten, so build it last |
| **Route 1** | `Route 29.png` | 60 x 25 | `Route101` |
| **Wendlebury** (town) | `Cherrygrove City.png` | about 51 x 29 | `OldaleTown` |
| Wendlebury: Pokémon Center 1F and 2F | (Palladium `PokeMon Center Johto.PNG`, about 16 x 22, is an alternative) | | Shared layouts `LAYOUT_POKEMON_CENTER_1F` and `_2F`. No painting needed |
| Wendlebury: Mart | | | Shared layout `LAYOUT_MART`. No painting needed |
| **Route 2** | `Route 30.png` | 37 x 59 | `Route102` |
| **Crestfall** (town, gym 1) | `Azalea Town.png` | about 48 x 32 | `PetalburgCity` |
| Crestfall: Greta's gym (Normal type; greenery is aesthetic only, use non-encounter grass) | `Azalea Town Gym.png` | 15 x 17 | `PetalburgCity_Gym` is Normal type in vanilla too, but it is 9 x 112 with 38 warps and 11 objects, so it is a poor base. Decide when Crestfall comes up |
| **Route 3** (blocked at first) | `Route 31.png` | 46 x 22 | `Route104` |

Pokémon Centers and Marts should come from the vanilla maps above, since each town needs one and Palladium has no Mart. Fitting a Johto route to a Veldris route is a proposal. The region-map shape is independent of it.

## Vanilla bases for everything else

- **Interiors** (Pokémon Centers, Marts, houses, other gyms): start from the vanilla maps in the tree. They are official and already in upstream, so nothing extra to credit. Pokémon Centers and Marts need no painting: pick the existing layout ids in Porymap's New Map dialog (see below).
- **Towns and routes Palladium does not cover:** start from Hoenn maps in the same way. Palladium has 16 route images (Routes 29 to 46 with gaps) against Veldris' 33 routes, so about half the routes come from vanilla.
- The FRLG maps in the tree are not built into this Emerald ROM and use another layout format, so they are not usable as bases here.

## Who does what

1. **The author (Porymap):** trace the map, starting from the vanilla base where one exists, with the Palladium image beside it. Keep the map's `region` at `REGION_HOENN` and `layout_version` at `emerald`. Step-by-step guide: [porymap-first-map.md](porymap-first-map.md).
2. **Claude:** the wiring. That is the region-map section (already added for the first six), warps, triggers, scripts, dialogue and trainers. Porymap itself appends the `.include` line to `data/event_scripts.s` on the first save of a new map; Claude checks it is there once. Claude also updates [towns-and-routes.md](towns-and-routes.md), [flags.md](flags.md) and `CREDITS.md`, and checks the build.
3. See "Adding things" in `CLAUDE.md` for the four-step new-map checklist.

## Open items

- ~~Confirm the mapping above, or swap any pairing.~~ Approved (author, 2026-09-29).
- Which Palladium images cover towns 4 to 18 and routes 4 to 33: decide as each comes up.
- Whether to use any hash-named uploads.

## Duplicate or shared layout: the one thing to get right (from Porymap's source)

Porymap gives two ways to start a map from an existing one:

- **Duplicate Map** copies the blocks into a new layout of its own. Use it for Hollowbrook, the routes, and any house you will repaint. It also copies **all events** (NPCs, warps, triggers, signs and the two heal locations), and not the map connections. The copied heal locations keep their old ids, so delete them before the first save or the build breaks on duplicate ids. Those events still point at Littleroot's scripts and flags, so delete or rewrite them before testing. The header still says `MAPSEC_LITTLEROOT_TOWN` until you change it.
- **A new map on an existing layout** shares one layout between maps, with no copy. In the map list's Layouts tab, right-click the layout and choose **Add New Map with Layout**. (In the New Map dialog, type the Map Name first and pick the Layout ID after, because typing the name overwrites the Layout ID.) Use it for buildings that stay identical: Pokémon Centers, Marts and the Goldsworth houses. Painting in one map changes all of them. Vanilla does this too: 31 layouts are shared among the maps this ROM builds (49 counting the FRLG folders), for example `LAYOUT_HOUSE1` by 9 maps and `LAYOUT_POKEMON_CENTER_1F` by 15.

Vanilla sizes are smaller than the plan: LittlerootTown is 20 x 20 (Hollowbrook plan 32 x 28), OldaleTown 20 x 20 (about 51 x 29), PetalburgCity 30 x 30 (about 48 x 32), Route101 20 x 20 (60 x 25). After duplicating, use **Change Dimensions**, not new numbers in the duplicate dialog. The new area comes in empty with elevation 0, and normal ground is elevation 3, so repaint it in the Collision tab too.

## How close vanilla tiles get to the Palladium pictures (opinion, not a build)

From comparing renders of the vanilla maps with `New Bark Town.png`, `Elm's Lab.png` and `Hero's House 1st Floor.png`: the layout (buildings, paths, pond, signs, fences, furniture positions) can be matched almost completely, and about 70% of the look. What vanilla `gTileset_General` and `gTileset_Petalburg` do not have: pine trees (only round trees), green roofs with teal trim (vanilla roofs are red or orange), the pale-green path colour, and the grey brick lab. The indoor floors and rugs also come out in different colours. So Hollowbrook would look like a Hoenn village laid out like New Bark Town. **Options:** accept that; use the LeoB ORAS recolour in the asset repo, which shows pines and pale paths but keeps brown roofs (only its preview was looked at, and it needs a `CREDITS.md` row and your OK); or draw new tiles, which is not planned. Your call, no rush: it does not block the first tracing.

## Goldsworth houses and the skyscraper (author notes 2026-09-29; details PROPOSED)

**Houses (one per city, plus Hollowbrook's, which is the one town exception; the skyscraper's city has none).** With the example of 7 cities that is 6 houses plus Hollowbrook's, so about 7 maps, not 18.
- **One shared layout.** Maps can share a layout id (see above), so every house is its own map with its own NPCs and text, on one layout. Cost: 0 map sections, because an interior uses its town's section (checked on vanilla houses); thousands of map numbers are free; the ROM cost is small (a 10 x 9 layout is 180 bytes, stored once).
- **The layout can start as a vanilla stand-in** (`LAYOUT_HOUSE1` is 10 x 9, `LAYOUT_HOUSE2` is 11 x 8), then be swapped for one custom Goldsworth-house layout: a nicer, richer room, painted once in Porymap.
- **Per house:** its own `map.json`, a `map_groups.json` entry, a `scripts.inc` with a `<Map>_MapScripts::` label, and its warps (Porymap adds the `event_scripts.s` include on the first save). Do not use `shared_events_map` for houses, because it also shares warps and every exit goes to a different town. Use unique `LOCALID_` names per house.
- **NPC-only.** No trainer ids in the houses (open decision 11 in [game-bible.md](game-bible.md)). A vanilla house holds 1 to 7 objects, and the limit is 15 NPCs plus the player.
- **Naming:** `<Town>_GoldsworthHouse` (a city's works the same way, for example `Hollowbrook_GoldsworthHouse`).

**Skyscraper (one city, TBD; Troglodyte's parents are inside).** It goes in a city, not a town (author).
- **Interiors need no new art:** the vanilla Devon Corp (`RustboroCity_DevonCorp_1F` to `3F`, 19 x 9 each, stairs) or the Lilycove Department Store set (five floors 18 x 8, an elevator, a rooftop). Both use their town's section. The store's elevator script is tied to a fixed five-floor list, so a taller tower needs a script check.
- **The exterior is the hard part.** A tall, distinctive tower needs new tile art or a compromise. Nothing in the Emerald tilesets in the tree has it. Options, cheapest first: (1) a big Devon Corp style block (about 10 x 9) in a normal town tileset. It reads as a large office, not a skyscraper; (2) the vanilla or LeoB ORAS Battle Tower (about 17 wide and 15 or more tall). It looks like a Battle Frontier facility and sits in a tileset with no houses, so the author would need a combined tileset in Porymap; (3) new tiles, drawn or converted from the sprite rips in the tilesets repo (unclear licences, not recommended).
- **Palladium references (images only):** `goldenrodcitytiled.png` and `goldenrodrodcity.png` (the Radio Tower, about 5 to 7 wide and 15 tall, none of its tiles exist in Emerald), `Goldenrod Dept Store 1F.png` (six floor panels and a roof), `President's Office Tiled.PNG` (an executive floor), `Battle Tower.png` (24 x 26). `johtobuildings.PNG` contains a Radio Tower and a skyscraper but stays on the leave-out list above.
- FRLG's Silph Co and Celadon department store maps are in the tree but not built into Emerald, so they are design reference only.
