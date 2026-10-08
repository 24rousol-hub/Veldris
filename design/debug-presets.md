# Debug presets and the tracked pre-commit hook

Status: BUILT 2026-10-08 (author liked 'tracked dialogue-check hook + debug presets'). Debug-only, no effect on a normal game.

## Pre-commit hook (`.githooks/pre-commit`)

Turn it on once per clone (git does not store this setting): `git config core.hooksPath .githooks`. The older local-only hook in `.git/hooks/` is replaced by it (same ROM guard, now also blocks `.ss1` savestates).

| Check | Runs on staged files |
|---|---|
| ROM / save / savestate guard (`.gba .sav .srm .sgm .ss0-9`, except the three `data/mb_*.gba` helpers) | every commit. Never skip this one |
| `design/tools/dialogue_check.py` (216 px, 2-line rule, the real font widths) | `data/maps/*/scripts.inc`, `data/scripts/veldris_*.inc`, `data/text/birch_speech.inc`, `design/dialogue/*.inc`, and `src/data/veldris_trainer_slides.h` (that one uses the battle-box rule, 208 px). Upstream script files such as `debug.inc` and `berry_tree.inc` are left out on purpose: they hold long debug text that does not fit and is never shown to the player |
| `design/tools/wild_lint.py` | `src/data/wild_encounters.json` |

A failing check prints the command to rerun. `git commit --no-verify` skips the text and wild checks; use it only with a reason. The hook needs `python3`; without it the text checks are skipped with a warning and the ROM guard still runs.

## Cheat start (Utilities > Cheat start)

`Debug_CheatStart` in `data/scripts/debug.inc` was the Hoenn cheat start (Littleroot flags, Hoenn badges and fly flags). It is now a **Veldris** cheat start: the state after the Hollowbrook lab scene and Troglodyte's first fight.

- Flags: Pokémon, adventure started, Pokédex and National Dex, Running Shoes (`FLAG_SYS_B_DASH`), `FLAG_VISITED_HOLLOWBROOK`.
- The lab hide flags as the lab scene leaves them, `FLAG_HIDE_HOLLOWBROOK_TROG` set, `VAR_HOLLOWBROOK_STATE` 4, `VAR_TROG_STARTER` 0.
- Party at level 20: Treecko, Torchic, Mudkip, plus Wailmer and Tropius carrying the HM moves (field moves no longer need the move, so the moves are only a convenience).
- Not given: badges, key items (use the Script presets).

It also starts the daily clock (`InitTimeBasedEvents`) and zeroes the clock offset, as before.

## Script presets (R+START > Scripts)

Only the labels `Debug_EventScript_Script_1` to `_8` were empty; the menu names stay 'Script 1' to 'Script 8'.

| Slot | Does |
|---|---|
| 1 | Journal, Exp. Share and Running Shoes (no messages) |
| 2 | Badges 1 to 3 and the Hollowbrook and Crestfall fly flags |
| 3 | All nine badges |
| 4 | Clears all nine badges |
| 5 | Warp to Hollowbrook (9,21) |
| 6 | Warp to Route 1 beside the guide (12,13) |
| 7 | Warp to Crestfall outside the Center (9,15) |
| 8 | Marks both Troglodyte fights as won (the Journal tally) and warps into the Crestfall gym |

All flags used are listed in [flags.md](flags.md). Keep a preset in step when a flag is renamed.

## Other debug-menu aids worth knowing

- Utilities > Time Functions: 'Get time', 'Get time of day', 'Set wall clock' (see [time-of-day.md](time-of-day.md)).
- Trainers > Try Battle starts any trainer id (the Mugshot does not play there; see [trainer-slides.md](trainer-slides.md)).
- A copy of the ROM runs headless in mGBA (CLAUDE.md, 'Testing in an emulator').
