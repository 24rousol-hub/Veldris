# Engine edits log

The rule: keep edits to upstream (pokeemerald-expansion) files minimal, and prefer config switches in `include/config/*.h`, so upstream updates can still be pulled with few conflicts.

**Every edit to a file that exists upstream is logged here, in the same commit.** Hack-only files (everything under `design/`, new maps, new scripts) do not need a row.

Before pulling upstream, read this list. Each row is a place a merge could conflict.

| Date | File | Change | Why | Config switch instead? |
|---|---|---|---|---|
| 2026-09-29 | `.gitignore` | Appended a Veldris block at the end (ROMs, saves, build output). No upstream lines changed. | Public repo: never commit a ROM or save | n/a |
| 2026-09-29 | `data/text/birch_speech.inc` | Rewrote the intro text as Prof. Fennick. Text only: every label is unchanged and no C was touched | The author asked for the intro to be Fennick's, in this file | n/a (text file) |
| 2026-09-29 | `CREDITS.md` | Added a hack credits section above the upstream one. Upstream content is untouched. | Credit every third-party asset | n/a |
| 2026-09-29 | `include/constants/flags.h` | Renamed `FLAG_UNUSED_0x88E` to `FLAG_BADGE09_GET`; `NUM_BADGES` is now the literal `9` | 9th badge for 9 gyms | No |
| 2026-09-29 | `src/event_data.c` | Removed the `gBadgeFlags[]` definition (it moved to the hack-owned `src/veldris_badges.c`, generated from one table) | Single badge table | No |
| 2026-09-29 | `src/trainer_card.c` | Badge tile buffer is 2 sheet rows; badges load at BG3 tiles 192 and 352; front-page badges drawn edge to edge and centred from the table; badge flags read via `gBadgeFlags`; FRLG card layout untouched | Show 9 (up to 12) badges | No |
| 2026-09-29 | `graphics/trainer_card/badges.png`, `front.bin` | Sheet is now 128x32 (Kaixer badges 1-8 + placeholder 9); the 8 baked numbered slots in `front.bin` rows 15-16 were replaced by the plain band tile; slot 15 of the sheet is an empty-socket icon for unearned badges | Room for 9+ badges | No |
| 2026-09-29 | `src/main_menu.c`, `src/menu.c`, `src/tv.c`, `src/shop_criteria.c`, `src/battle_script_commands.c` | Badge-count loops replaced by `GetBadgeCount()`; `sBadgeLevel[]` gained a 65 entry | The old loops added `NUM_BADGES` to `FLAG_BADGE01_GET`, which breaks with a non-contiguous 9th flag | No |
| 2026-09-29 | `src/field_move.c` | `HasBadgeForFieldMove` reads `gBadgeFlags[arg]` instead of `FLAG_BADGE01_GET + arg` | HM gating works for any badge flag | No |
| 2026-09-29 | `src/battle_util.c` | Obedience: badge 9 ignores obedience, badge 8 gives level 90 (vanilla: badge 8 ignored it) | 9 badges | No |
| 2026-09-29 | `src/caps.c` | Added `FLAG_BADGE09_GET` rows to the level-cap (50, PROPOSED placeholder) and EV-cap tables; EV fractions now /19 | 9 badges. Caps are off by default (`B_LEVEL_CAP_TYPE`) | Caps are config-gated |
| 2026-09-29 | `src/region_map.c` | A-prime fly hooks: `#include "data/veldris_fly_towns.h"` plus one line each at the end of `sMapHealLocations`, `sFlyLocations` and before `default:` in `GetMapsecType` | One table row per fly town instead of 3 edits in this file | No |
| 2026-09-29 | `src/data/region_map/region_map_sections.json` | Appended six records at the end: `MAPSEC_HOLLOWBROOK`, `MAPSEC_WENDLEBURY`, `MAPSEC_CRESTFALL`, `MAPSEC_VELDRIS_ROUTE_1` to `_3`. `MAPSEC_NONE` moves from 209 to 215 | So Porymap's Location dropdown offers them and the name popup works. The town map grid and picture are not touched yet | No |

**Files Porymap writes.** When the author saves a new map, Porymap appends to or rewrites these upstream files. They are not engine edits, so they get one standing row here rather than a row per map: `data/maps/map_groups.json`, `data/layouts/layouts.json`, `data/event_scripts.s` (an appended `.include` line per new map), and on every save `src/data/region_map/region_map_sections.json`, `src/data/heal_locations.json`, `src/data/wild_encounters.json`. Read the changed-files list before committing.

**Files each new fly town touches (PROPOSED standing rows).** Per [region-map.md](region-map.md): `region_map_sections.json`, `include/constants/flags.h` (one rename), `src/data/heal_locations.json`, `src/data/region_map/region_map_layout.h`, and the map picture. Logging each of these per town would be 18 towns x 5 files of noise, so the proposal is one standing 'appends only' row per file, added when the file is first touched. That changes the logging rule above, so it waits for the author's OK. Hack-owned files (`src/data/veldris_fly_towns.h`, `src/veldris_badges.c`, `include/veldris_badges.h`) need no row.

## Planned edits (not yet made)

| File | Change | Waiting on |
|---|---|---|
| `include/constants/flags.h`, `vars.h` | One-line renames of `FLAG_UNUSED_*` / `VAR_UNUSED_*` as flags and vars are claimed. See [flags.md](flags.md) | First flag use |
| `include/constants/opponents.h` | Trainer slot changes (only 9 free) | Open decision 6 in [game-bible.md](game-bible.md) |
