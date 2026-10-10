# CLAUDE.md - Pokémon: Piss Off Troglodyte (Veldris)

A personal-use GBA ROM hack built on pokeemerald-expansion. Custom region **Veldris**: 18 towns, 33 routes, 9 gyms, an Elite Four and a post-game. The player's motivation is humiliating Troglodyte (Beauregard Goldsworth IV), a sheltered, mediocre rival whose rich parents keep staging gym sabotage schemes that fail. The real danger is two villain teams, **The Commons** (land) and **the Drowned Crown** (sea), which the player deals with as a necessary nuisance (`design/factions.md`). **This repository is PUBLIC.**

## Hard rules

1. **Never commit a ROM, a `.gba` file, a save file or build output.** `.gitignore` blocks them and the tracked pre-commit hook `.githooks/pre-commit` double-checks (run `git config core.hooksPath .githooks` once per clone; web sessions do it for you through `.claude/hooks/session-start.sh`, author-approved 2026-10-09, which deliberately does not install the toolchain; it also checks dialogue and wild-encounter files, see `design/debug-presets.md`). The only `.gba` files in the repo are the three upstream multiboot helpers in `data/mb_*.gba`. Before every commit run `git -c core.quotePath=false diff --cached --name-only -z | tr '\0' '\n' | grep -Ei '(\.(gba|sav|srm|sgm|sa[0-9]|ss[0-9]|st[0-9]|state|elf|map|sym|o|zip|7z|rar|gz|tgz|tar|xz|bz2|zst|ips|bps|ups|xdelta|ppf)(\.[^/]*)?$|(^|/)build/)'` (the hook's list; the hook also blocks any staged file over 8 MB, and `git commit --no-verify` skips the whole hook, so run this by hand first). Deliver a built ROM to the author by copying it out of the repo (scratchpad) and sending it as a file. Never `git add` it.
2. **Do not write a script that generates map files** unless the author asks for a map to be built (author, 2026-10-01: the Hollowbrook interiors and town were built this way, reviewed render by render, see `design/interiors.md`). Otherwise maps are fragile and the author builds and edits them in Porymap. Claude handles scripts, events, warps, trainers and dialogue. Do not hand-edit map block data (`map.bin`, `border.bin`) or tileset files. Editing event lists in `map.json` (warps, coord events, object events) is fine, but tell the author to close or reload Porymap first so it does not overwrite the change.
3. **Read `design/` before building content, and update it in the same change.** See `design/README.md` for what lives where.
4. **Track every flag and var** in `design/flags.md`. Reuse unused ones from the spare pool and never overwrite one that is in use.
5. **Keep engine edits minimal.** Prefer config switches in `include/config/*.h` so upstream updates can still be pulled. Log every edit to an upstream file in `design/engine-edits.md`.
6. **The build must pass after every change** (`make -j4`). Do not commit or push a state that does not build.
7. **Credit every asset.** Reuse existing maps and tilesets instead of drawing from scratch. Sources: the author's repos `24rousol-hub/Team-Aquas-Asset-Repo` and `24rousol-hub/sprites`, plus other free community resources. Every asset from there gets a row in `CREDITS.md` in the same commit. **Do not use maps from other hacks without the author's permission.**
8. **Ask before doing anything big:** engine changes across several files, new systems, mass renames, importing large asset packs, anything hard to undo or visible outside the repo. Keep explanations short and plain.
9. Proposals are **PROPOSED** until the author approves them. Do not treat a suggested name, scheme or layout as canon.
10. **Ask the author at key story points (author, 2026-10-04).** Before building or writing dialogue for a route, town or scene that carries an important story beat, stop and ask for the author's input first (a short AskUserQuestion with options is fine). Key beats include anything with the Commons or the Drowned Crown, Troglodyte's fights and turning points, the Goldsworth schemes, gym leaders' story lines, the legendaries (Dialga, Kyogre, Giratina), Gatsby and Cynthia, and the climax and post-game. Ordinary trainers, signs and filler NPCs do not need this. The story so far is in `design/story-outline.md` and `design/factions.md`.

## Engine rules learned the hard way

All checked against this tree.

- **Indoor maps take walls and floors from the secondary tileset, not the primary.** True for Emerald-format indoor layouts, whose primary tileset `gTileset_Building` has only 8 metatiles (98 of the 99 blocks in Brendan's house 1F are secondary). Keep new maps at `layout_version` `emerald`.
- **Never strip the top 6 bits of a map block.** The map grid word is: bits 0-9 metatile ID (`0x03FF`), bits 10-11 collision (`0x0C00`), bits 12-15 elevation (`0xF000`). The top 6 bits are `0xFC00`. Masking to the metatile ID alone destroys collision and elevation (`include/global.fieldmap.h`).
- **The charmap has no plain double quote (`"`),** and even `\"` is a build error. Use single quotes for speech. The ASCII apostrophe `'` maps to the *closing* glyph (`B4`), so for an **opening** quote type `‘` (U+2018) and close with `’`. Curly `“ ”` also exist (`B1`/`B2`), but this project uses single quotes.
- **Use `coord_event` triggers for cutscenes, not `MAP_SCRIPT_ON_TRANSITION`.** In `map.json`:
  `{ "type": "trigger", "x": 10, "y": 1, "elevation": 3, "var": "VAR_...", "var_value": "0", "script": "Map_EventScript_Name" }`
  The tile must be walkable and its elevation must match (normally 3). `MAP_SCRIPT_ON_FRAME_TABLE` is also fine for cutscenes. `MAP_SCRIPT_ON_TRANSITION` is still the right place for instant setup such as `setflag FLAG_VISITED_<TOWN>`.
- **An NPC that walks up to the player and talks** (no battle) is a `TRAINER_TYPE_NORMAL` object with a `FACE_*` movement type and a sight range, whose script starts with `cant_see_if_set FLAG_..._DONE` (upstream's guard) and sets that flag before `release`. Built and run in a scratch clone 2026-10-10: copy `design/scripts/walkup_template.inc`.
  Traps: nothing visible in a done branch (endless loop); a `coord_event` inside his sight line is skipped on its first step; he exists only within 9 tiles left, 10 right, 7 above and 9 below the player, so keep the range at 7 sideways and 4 down; list a walker before any real trainer that shares a tile; 15 NPCs at most at once.
  The 27-row test log and the optional checker `design/tools/walkup_lint.py` are described in `design/npc-walkup.md`.
- **Name Greta's trainer `TRAINER_CRESTFALL_GRETA`.** `TRAINER_GRETA` already exists (`include/constants/opponents.h`, `src/data/trainers.party`).
- **The intro is C-driven.** Edit `data/text/birch_speech.inc` for intro dialogue (used by `src/main_menu.c`, included from `data/event_scripts.s`). The 'This is what we call a POKéMON' line is in `src/strings.c` instead, and the Birch art is in `graphics/birch_speech/`. Birch's name is hard-coded in the `.inc` text, so renaming him to Fennick is a text edit. `ENABLE_QUICKSTART` lets you skip the intro while testing.
- **`local_id` names must be unique across all maps** (they all land in one header, `include/constants/map_event_ids.h`). A clash builds without error and the later value wins, so a script moves the wrong person (seen 2026-10-08 with Greta in Crestfall and its gym). Suffix outdoor copies, e.g. `LOCALID_CRESTFALL_GRETA_OUTSIDE`.
- **FRLG overworld sprites (`OBJ_EVENT_GFX_*_FRLG`) are not compiled into this Emerald build.** Using one builds fine but crashes (the game resets) when the object spawns.
- **Devices (author, 2026-10-09).** The author tests on a **phone with Delta** (its GBA core looks VBA-M based; our headless tests use mGBA) and plans to play on a **Miyoo Mini Plus**. A GBA ROM can never exceed 32 MiB (about 25.8 MiB used on 2026-10-10, exact figures and how to measure in `design/devices.md`); keep the file at 32 MiB; Delta save states break on every rebuild, so **never change the SaveBlock layout without telling the author**; the dev ROM keeps the debug menu, a device build uses `make release` (output `pokeemerald-release.gba`). `design/devices.md`.
- **Talking furniture is on (2026-10-09).** One hack-owned lookup, `src/veldris_furniture.c`, runs before the `IS_FRLG` block of `GetInteractedMetatileScript`; add a furniture type with one table row plus one script in `data/scripts/veldris_furniture.inc`. `flavor_text.inc` is FRLG-only and not assembled, so do not point C at it. A `bg_event` sign (facing ANY) beats the general line; the author sets the metatile Behavior in Porymap. `design/furniture-lines.md`.
- **Write map scripts as `scripts.inc`, not Poryscript.** The build has no Poryscript rules.
- **`{RIVAL}` expands to MAY or BRENDAN** (`src/string_util.c`). Write TROGLODYTE literally.
- **Dialogue must fit the text box: 216 px wide, 2 lines** (measured). Run `python3 design/tools/dialogue_check.py <file>` before committing any text. Details in `design/dialogue-style.md`.
- **A new fly town is one row in `src/data/veldris_fly_towns.h`** plus the data steps in the checklist in `design/region-map.md`. Two traps: write `respawn_map` before `respawn_npc` in `heal_locations.json`, and always give both.
- **Only 9 brand-new trainer IDs fit** before trainer flag space overflows, but that is not a cap on trainers: a trainer can **reuse a vanilla Hoenn entry** (rewrite its block in `src/data/trainers.party`, nothing else changes), which costs no new id. See 'A new trainer' below, `design/engine-limits.md` and open decision 6 in `design/game-bible.md`.
- **Badges: 9, through a table.** `src/veldris_badges.c` and `include/veldris_badges.h` hold one row per badge (flag and art slot), and every badge loop goes through `gBadgeFlags[]` or `GetBadgeCount()`. Details and limits in `design/badges.md`.
- FRLG map folders sit in `data/maps` but are **not built into this Emerald ROM** (`mapjson` skips maps not tagged `REGION_HOENN`). Their `MAP_*` and `MAPSEC_*` constants still exist (for example `MAPSEC_ROUTE_1`), so new Veldris names must not collide with them. See `design/towns-and-routes.md`.
- **Connected maps must share a primary tileset.** Crossing a map connection swaps only the secondary (`LoadMapFromCameraTransition`). **Exteriors use LeoB ORAS** (`gTileset_General` plus a LeoB town secondary; author 2026-10-01, after briefly trying Gen 4 outdoor tiles the same day). Interiors stay on the Gen 4 Interior secondary.
- **The town map picture can use at most 256 distinct 8x8 tiles**, only about 8 more map sections fit (2026-10-10: 244 records in `region_map_sections.json`, 35 over the vanilla 209; the `STATIC_ASSERT` in `src/data/veldris_fly_towns.h` fails the build past 252, so recount before planning: 252 minus the number of records), and Fly needs the Feather Badge in this build. All hard limits, with how to recount them, are in `design/engine-limits.md`; the town map wiring is in `design/region-map.md`.

- **Assets and sprites policy (author, 2026-10-01).** Sources that copy official Pokémon art are fine, but every one still gets a `CREDITS.md` row. Pokémon sprites stay as shipped (expansion's Gen 4/5-style art at 64x64; GBA-style art exists only for species 1-386 through `P_GBA_STYLE_SPECIES_GFX`, currently FALSE); no sprite import is planned. Catalogue of every source: `design/sprite-catalog.md`. Troglodyte uses the DP **Rich Boy** picture; the Goldsworth cousins get similar but not identical pictures (recolours or neighbouring DP classes).
- **Houses use shared one-floor layouts, never one custom layout per house** (six drawn up in `design/maps/interiors/house-layouts.md`; **at least 5 distinct single-floor interiors, a hard minimum from the author**). Everything looks Gen 4 inside (Gen 4 Interior secondary); exteriors are LeoB ORAS.
- **Trainer slides (mid-battle lines)** live in `src/data/veldris_trainer_slides.h`, with one include in `src/trainer_slide.c`. Key = trainer id (list each id once; an alias is the same id). Rows use `VELDRIS_SLIDE(NAME, "text")`, no `\n`, `{B_PLAYER_NAME}` not `{PLAYER}`. Check with `python3 design/tools/dialogue_check.py src/data/veldris_trainer_slides.h`. **Scope (author, 2026-10-09): lines only for key battles** (gym leaders, Commons and Crown bosses, the Elite Four, Cynthia); none for ordinary trainers or Troglodyte. Troglodyte's party order is random unless pinned with `Tags: Lead / Ace`. No lines are wired until the author approves wording (`design/trainer-slides.md`).
- **Badges are drawn by `design/tools/draw_badges.py`** (14x14 art in 16 px slots, one shared palette; the trainer card spaces them with `BADGE_PITCH` in `src/trainer_card.c`). Re-run the script after editing it, from the repo root.

## Adding things

**A new map.** Porymap does all four steps when the author saves a new or duplicated map for the first time (checked in Porymap's source: `saveMap` writes steps 1 and 4, `saveGlobalData` writes 2 and 3).
1. `data/maps/<Name>/map.json` and `scripts.inc` (with a `<Name>_MapScripts::` label).
2. An entry in `data/maps/map_groups.json`.
3. A layout entry in `data/layouts/layouts.json`.
4. **`.include "data/maps/<Name>/scripts.inc"` in `data/event_scripts.s`**, which Porymap appends at the end of the file. **Move that line into the commented Veldris block after the Hollowbrook includes** (about line 190), so upstream's appends at the end of the file never conflict. **Check it is there exactly once** before adding it by hand (a second copy defines the label twice). Add it yourself only for a map made without Porymap. If it is missing the build should fail at link time on the undefined label (inferred, not tested).

Porymap also rewrites `region_map_sections.json`, `heal_locations.json` and `wild_encounters.json` on every save, so read the changed-files list before committing. Two maps can share one layout (vanilla does it for Pokémon Centers, Marts and houses): in Porymap's map list, Layouts tab, right-click the layout and choose Add New Map with Layout. Painting in one then changes all of them.

**After pulling a duplicated map, grep `src/data/heal_locations.json` for duplicate ids.** Porymap's Duplicate Map copies the source's heal locations with their old ids (Littleroot's two), and a duplicate id breaks the build. The author is told to delete them before saving, and this is the check that catches a miss.

Keep the map's `region` at `REGION_HOENN` (the default) and `layout_version` at `emerald`, or the build silently leaves it out.

**A new trainer.** **Author rule: always reuse a vanilla Hoenn id (below); use a brand-new id only if the author says so.**
1. `src/data/trainers.party`: the `=== TRAINER_X ===` block. Its `Pic` and `Class` must already exist. **Every Pokémon needs `IVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe`: a missing `IVs:` line means 31.**
2. `include/constants/opponents.h`: for a brand-new id, add `#define TRAINER_X 855` (next free id) and raise `TRAINERS_COUNT_EMERALD` by one, staying at or below `MAX_TRAINERS_COUNT_EMERALD` (864). The defeated flag is `0x500 + id`. For a reused id see below (no new id, no count change).
3. In the map script: `trainerbattle_single TRAINER_X, Intro, Defeat`, and an object event in `map.json` with a `trainer_type`. **Gym leaders: copy `data/maps/Crestfall_Gym/scripts.inc` (the built Veldris example), not Rustboro's.** Never use `ShouldTryRematchBattle` or `trainerbattle_rematch*`: the reused leader ids still sit in `gRematchTable` (`src/battle_setup.c`), so a rematch would load a Crestfall or Hoenn trainer. Post-game rematches use `cleartrainerflag` (`design/postgame.md`). Never set `FREE_MATCH_CALL` to TRUE.

**Reusing a vanilla id (BUILT, 21 reused ids on 2026-10-10: count the `#define X TRAINER_Y` aliases in `include/constants/opponents.h`; see `design/trainer-roster.md`; no new id, tested in battle).** Pick an unused vanilla trainer (grep `data/maps/*/scripts.inc` and `design/trainer-roster.md` first so no Veldris fight shares its defeated flag), rewrite its block in `src/data/trainers.party` (party, pic, class, name). Its defeated flag is the old id's flag. Two cases, both compile:
- **Named characters** (gym leaders, Elite Four, Champion, Troglodyte, Greta): rename the party header and the `#define` to the Veldris name and keep the old Hoenn name as an alias on the next line (`#define TRAINER_CRESTFALL_GRETA 770` then `#define TRAINER_ROXANNE_2 TRAINER_CRESTFALL_GRETA`).
- **Anonymous route trainers** (the Route 1 trio): keep the Hoenn header and `#define`, and append `#define TRAINER_VELDRIS_<ROUTE>_<ROLE> TRAINER_<OLD>` at the end of `opponents.h` (append-only, so the merge-friendliest). Scripts use the Veldris name.
**A brand-new trainer pic or class** needs more edits (`include/constants/trainers.h`, `src/battle_main.c`, `src/data/graphics/trainers.h`). Veldris pictures (15 built, the 15th is Troglodyte's, `veldris_troglodyte.png`) are seen in battle and render correctly (index 0 must be the background colour).

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

## Testing in an emulator

The ROM boots headless in mGBA, which is how the intro and trainer card were checked on 2026-09-29. The container is ephemeral, so reinstall each time: `apt-get install -y mgba-sdl xvfb xdotool imagemagick` (binary `/usr/games/mgba`, not on `PATH`). Start `Xvfb :99 -screen 0 1280x960x24`, run `SDL_AUDIODRIVER=dummy DISPLAY=:99 /usr/games/mgba <copy of the rom>` on it, send keys with `xdotool` and screenshot with `import -window root`. **Hold every key**: a plain `xdotool key` drops presses (7 of 12 registered in a test), so use `xdotool keydown Down; sleep 0.15; xdotool keyup Down`. For R+START, keydown `s` and `Return`, wait 0.2 s, then release both. mGBA's keys are **X = A, Z = B**, Return = Start, Backspace = Select. This is a normal (non-release) build, so the **debug menu opens with R+START** (mGBA: the S key is R): Set Flag XYZ, Toggle All badges, Fly to map and more. Run a copy of the ROM from the scratchpad, never inside the repo.

**Robot player (preferred, 2026-10-10).** `python3 design/tools/emu/run_tests.py` plays the built ROM in a hidden mGBA and checks flags, vars, scripts, gates, the fake clock and Route 1's Night table (about 2 minutes; `--slow` adds the Route 1 walk). `python3 design/tools/emu/scene.py preset:4 warp:MAP_X,x,y shot:a.png` plays a scenario and saves a picture, which replaces long hand-driven xdotool walks. Needs `make -j4` first. Details and limits in `design/tools/emu/README.md`; it tests mGBA, not Delta.

## Git

- Develop on branch `claude/pokemon-pot-setup-evpysj` only. Commit after each working step, then push.
- Open pull requests as **drafts**.
- The asset repos (`Team-Aquas-Asset-Repo`, `sprites`) are read-only sources. Do not modify or push them unless the author says so.

## Where things are

| What | Where |
|---|---|
| Game bible, story, characters, towns and routes, flags, style guide | `design/` |
| Villain teams (the Commons, the Drowned Crown), the climax and the legendary lore | `design/factions.md` |
| Asset credits | `CREDITS.md` (hack section at the top) |
| Maps | `data/maps/<Map>/` (`map.json`, `scripts.inc`) |
| Trainers | `src/data/trainers.party`, `include/constants/opponents.h` |
| Flags and vars | `include/constants/flags.h`, `vars.h` |
| Intro dialogue | `data/text/birch_speech.inc` |
| Mid-battle trainer lines | `src/data/veldris_trainer_slides.h`, `design/trainer-slides.md` |
| Player customization (Costume Box) | `src/veldris_look.c`, `include/veldris_look.h`, `data/scripts/veldris_look.inc`, `design/player-customization.md`. Colour tables from `design/tools/sprites/player_look.py`, outfit sprites from `player_outfits.py` |
| DP sprites (70 overworlds `OBJ_EVENT_GFX_DP_*`, 94 pictures `Pic: DP ...`) | `design/dp-sprite-list.md`, `design/tools/sprites/import_dp.py`. Each DP overworld has its own palette: keep about 6 different DP people on screen at once |
| Journal key item | `data/scripts/veldris_journal.inc`, `src/veldris_journal.c`, `include/veldris_journal.h`, `design/journal.md`. **Every built TROGLODYTE fight needs one row in `VELDRIS_TROGLODYTE_FIGHTS`** and must not use `trainerbattle_earlyrival` |
| Config switches | `include/config/*.h` (summary in `design/engine-limits.md`) |

## Checklist for any content change

1. Read the relevant `design/` files.
2. Make the change.
3. Update `design/` (including `flags.md`, `engine-edits.md`), and `CREDITS.md` if an asset was added.
4. `make -j4` passes, and `python3 design/tools/dialogue_check.py` passes on any text you changed.
5. Check no ROM or save is staged, commit, push.
