# CLAUDE.md - Pokémon: Piss Off Troglodyte (Veldris)

A personal-use GBA ROM hack built on pokeemerald-expansion. Custom region **Veldris**: 18 towns, 33 routes, 9 gyms, an Elite Four and a post-game. The player's only motivation is humiliating Troglodyte (Beauregard Goldsworth IV), a sheltered, mediocre rival whose rich parents keep staging gym sabotage schemes that fail. **This repository is PUBLIC.**

## Hard rules

1. **Never commit a ROM, a `.gba` file, a save file or build output.** `.gitignore` blocks them and a local pre-commit hook double-checks. The only `.gba` files in the repo are the three upstream multiboot helpers in `data/mb_*.gba`. Before every commit run `git diff --cached --name-only | grep -Ei '\.(gba|sav|srm|sgm)$'`. Deliver a built ROM to the author by copying it out of the repo (scratchpad) and sending it as a file. Never `git add` it.
2. **Do not write a script that generates map files.** Maps are fragile. The author builds and edits maps in Porymap. Claude handles scripts, events, warps, trainers and dialogue. Do not hand-edit map block data (`map.bin`, `border.bin`) or tileset files. Editing event lists in `map.json` (warps, coord events, object events) is fine, but tell the author to close or reload Porymap first so it does not overwrite the change.
3. **Read `design/` before building content, and update it in the same change.** See `design/README.md` for what lives where.
4. **Track every flag and var** in `design/flags.md`. Reuse unused ones from the spare pool and never overwrite one that is in use.
5. **Keep engine edits minimal.** Prefer config switches in `include/config/*.h` so upstream updates can still be pulled. Log every edit to an upstream file in `design/engine-edits.md`.
6. **The build must pass after every change** (`make -j4`). Do not commit or push a state that does not build.
7. **Credit every asset.** Reuse existing maps and tilesets instead of drawing from scratch. Sources: the author's repos `24rousol-hub/Team-Aquas-Asset-Repo` and `24rousol-hub/sprites`, plus other free community resources. Every asset from there gets a row in `CREDITS.md` in the same commit. **Do not use maps from other hacks without the author's permission.**
8. **Ask before doing anything big:** engine changes across several files, new systems, mass renames, importing large asset packs, anything hard to undo or visible outside the repo. Keep explanations short and plain.
9. Proposals are **PROPOSED** until the author approves them. Do not treat a suggested name, scheme or layout as canon.

## Engine rules learned the hard way

All checked against this tree.

- **Indoor maps take walls and floors from the secondary tileset, not the primary.** True for Emerald-format indoor layouts, whose primary tileset `gTileset_Building` has only 8 metatiles (98 of the 99 blocks in Brendan's house 1F are secondary). Keep new maps at `layout_version` `emerald`.
- **Never strip the top 6 bits of a map block.** The map grid word is: bits 0-9 metatile ID (`0x03FF`), bits 10-11 collision (`0x0C00`), bits 12-15 elevation (`0xF000`). The top 6 bits are `0xFC00`. Masking to the metatile ID alone destroys collision and elevation (`include/global.fieldmap.h`).
- **The charmap has no plain double quote (`"`),** and even `\"` is a build error. Use single quotes for speech. The ASCII apostrophe `'` maps to the *closing* glyph (`B4`), so for an **opening** quote type `‘` (U+2018) and close with `’`. Curly `“ ”` also exist (`B1`/`B2`), but this project uses single quotes.
- **Use `coord_event` triggers for cutscenes, not `MAP_SCRIPT_ON_TRANSITION`.** In `map.json`:
  `{ "type": "trigger", "x": 10, "y": 1, "elevation": 3, "var": "VAR_...", "var_value": "0", "script": "Map_EventScript_Name" }`
  The tile must be walkable and its elevation must match (normally 3). `MAP_SCRIPT_ON_FRAME_TABLE` is also fine for cutscenes. `MAP_SCRIPT_ON_TRANSITION` is still the right place for instant setup such as `setflag FLAG_VISITED_<TOWN>`.
- **Name Greta's trainer `TRAINER_CRESTFALL_GRETA`.** `TRAINER_GRETA` already exists (`include/constants/opponents.h`, `src/data/trainers.party`).
- **The intro is C-driven.** Edit `data/text/birch_speech.inc` for intro dialogue (used by `src/main_menu.c`, included from `data/event_scripts.s`). The 'This is what we call a POKéMON' line is in `src/strings.c` instead, and the Birch art is in `graphics/birch_speech/`. Birch's name is hard-coded in the `.inc` text, so renaming him to Fennick is a text edit. `ENABLE_QUICKSTART` lets you skip the intro while testing.
- **Write map scripts as `scripts.inc`, not Poryscript.** The build has no Poryscript rules.
- **`{RIVAL}` expands to MAY or BRENDAN** (`src/string_util.c`). Write TROGLODYTE literally.
- **Only 9 new trainer IDs fit** before trainer flag space overflows. See `design/engine-limits.md` and open decision 6 in `design/game-bible.md`.
- **The engine is built for 8 badges.** Nine gyms need a decision. See open decision 1 in `design/game-bible.md`.
- FRLG map folders sit in `data/maps` but are **not built into this Emerald ROM** (`mapjson` skips maps not tagged `REGION_HOENN`). Their `MAP_*` and `MAPSEC_*` constants still exist (for example `MAPSEC_ROUTE_1`), so new Veldris names must not collide with them. See `design/towns-and-routes.md`.
- **The town map picture can use at most 256 distinct 8x8 tiles**, at most about 43 more map sections fit, and Fly needs the Feather Badge in this build. All hard limits are in `design/engine-limits.md`; the town map wiring is in `design/region-map.md`.

## Adding things

**A new map.** Porymap does steps 1 to 3. **Step 4 is Claude's.**
1. `data/maps/<Name>/map.json` and `scripts.inc` (with a `<Name>_MapScripts::` label).
2. An entry in `data/maps/map_groups.json`.
3. A layout entry in `data/layouts/layouts.json`.
4. **`.include "data/maps/<Name>/scripts.inc"` in `data/event_scripts.s`.** Porymap does not write this line. Without it the build should fail at link time on the undefined label (inferred, not tested).

Keep the map's `region` at `REGION_HOENN` (the default) and `layout_version` at `emerald`, or the build silently leaves it out.

**A new trainer.**
1. `src/data/trainers.party`: add a `=== TRAINER_X ===` block. Its `Pic` and `Class` must already exist.
2. `include/constants/opponents.h`: add `#define TRAINER_X 855` (next free id) and raise `TRAINERS_COUNT_EMERALD` by one, staying at or below `MAX_TRAINERS_COUNT_EMERALD` (864). The defeated flag is `0x500 + id`.
3. In the map script: `trainerbattle_single TRAINER_X, Intro, Defeat` (gym leaders: copy the pattern in `data/maps/RustboroCity_Gym/scripts.inc`), and an object event in `map.json` with a `trainer_type`.
4. A brand-new trainer pic or class needs more edits (`include/constants/trainers.h`, `src/battle_main.c`, `src/data/graphics/trainers.h`). Untested end to end.

## Build

The container is ephemeral, so a fresh session must reinstall the toolchain first (Ubuntu 24.04):

```
apt-get update && apt-get install -y gcc-arm-none-eabi binutils-arm-none-eabi libnewlib-arm-none-eabi libpng-dev pkg-config
```

That installs `arm-none-eabi-gcc` 13.2.1 and binutils 2.42, plus libpng 1.6.43. `build-essential` and `git` were already present. No devkitPro and no base ROM are needed: the ROM builds from source.

```
make -j4          # builds pokeemerald.gba (gitignored)
```

The Makefile takes `arm-none-eabi-*` from `PATH`, so the system toolchain needs no `TOOLCHAIN=` override. A clean build takes about 3 min 40 s on 4 cores. The result is a 32 MiB ROM with header `POKEMON EMER` / `BPEE`. It does not match `rom.sha1`, which only applies to vanilla pokeemerald.

## Git

- Develop on branch `claude/pokemon-pot-setup-evpysj` only. Commit after each working step, then push.
- Open pull requests as **drafts**.
- The asset repos (`Team-Aquas-Asset-Repo`, `sprites`) are read-only sources. Do not modify or push them unless the author says so.

## Where things are

| What | Where |
|---|---|
| Game bible, story, characters, towns and routes, flags, style guide | `design/` |
| Asset credits | `CREDITS.md` (hack section at the top) |
| Maps | `data/maps/<Map>/` (`map.json`, `scripts.inc`) |
| Trainers | `src/data/trainers.party`, `include/constants/opponents.h` |
| Flags and vars | `include/constants/flags.h`, `vars.h` |
| Intro dialogue | `data/text/birch_speech.inc` |
| Config switches | `include/config/*.h` (summary in `design/engine-limits.md`) |

## Checklist for any content change

1. Read the relevant `design/` files.
2. Make the change.
3. Update `design/` (including `flags.md`, `engine-edits.md`), and `CREDITS.md` if an asset was added.
4. `make -j4` passes.
5. Check no ROM or save is staged, commit, push.
