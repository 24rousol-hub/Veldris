# Debug presets and the tracked pre-commit hook

Status: BUILT 2026-10-08, upgraded the same day (author liked 'tracked dialogue-check hook + debug presets'). Debug-only, no effect on a normal game.

## Text checker and pre-commit hook

`design/tools/dialogue_check.py` (rewritten 2026-10-08, uses `design/tools/textwidth.py`) measures with the game's own glyph widths and now also knows the width-changing codes (`{FONT_NARROW}`, `{CLEAR n}`, `{SKIP n}`, `{SHIFT_RIGHT n}`, `{PKMN}`, button icons) and the line count: **a field or intro page whose third line is separated by `\n` instead of `\l` is an error.** The old tool treated every `{CODE}` except `{PLAYER}` as 0 px and counted no lines. Widths and error counts are identical on all 29 Veldris text files (checked before the swap).

| Box | Size | Where it applies |
|---|---|---|
| field, intro | 216 px x 2 lines | map scripts, `data/scripts/veldris_*.inc`, `data/text/birch_speech.inc`, `design/dialogue/*.inc` |
| battle | 208 px x 2 lines, auto line break | `src/data/veldris_trainer_slides.h` (through `slide_check.py`) |
| item description | 109 px x 3 lines | `src/data/items.h` |
| any other | `--box 120x1/narrow` or a `// box: NAME` comment on a C string | |

Options: `--staged` (only strings on lines the staged diff adds, what the hook uses), `--all`, `--box`. Opt one string out with `nocheck` in a comment (`@ nocheck` in `.inc`, `// nocheck` in C). A plain run on an upstream file (for example `items.h`) checks only lines changed since HEAD.

The tracked **`.githooks/pre-commit`** runs on every commit once you set `git config core.hooksPath .githooks` (git does not store this setting, so do it once per clone; a fresh web session needs it again):

| Check | Staged files |
|---|---|
| ROM / save / savestate guard (`.gba .sav .srm .sgm .ss0-9`, except the three `data/mb_*.gba` helpers). Never skip this one | all |
| `dialogue_check.py --staged` | every `.inc`, `.c`, `.h`. **Only the lines the commit adds are judged**, so vanilla text that already overflows does not block you |
| `design/tools/wild_lint.py` | `src/data/wild_encounters.json` |

A failure lists the strings and rules. Escape hatches: `nocheck` on the string, or `git commit --no-verify` (text and wild checks only). Needs `python3`; without it the text checks are skipped with a warning and the ROM guard still runs. A GitHub workflow was considered and dropped: Actions is off on this fork, and a workflow runs after the push so it could not stop a local commit.

## Rewind presets (R+START > Scripts, and Utilities > Cheat start)

Bodies live in the hack-owned `data/scripts/veldris_debug.inc`. In `data/scripts/debug.inc` each `Debug_EventScript_Script_N` and `Debug_CheatStart` is just `goto Veldris_Debug_...`, and `src/debug.c` carries the eight menu labels. **Presets 1 to 6 first reset the whole Veldris story** (every flag, var and trainer flag in [flags.md](flags.md), HM CUT, TM CRUNCH) **and replace or clear the party**, so they are for throw-away saves: using one on a save you care about loses progress.

| Slot | Name in the menu | Does |
|---|---|---|
| 1 | New game (bedroom) | Whole story back to new game, no Pokémon, no shoes, no Journal; warps to the 2F room. Walk down for Mom's scene |
| 2 | Lab scene (Trog 1) | State 1 (Mom's scene done, shoes given), no Pokémon; warps into the lab at (6,11). Press Up once for the lab scene |
| 3 | Trog fight 1 (door) | Starter chosen (Mudkip L5); arrives on the lab door tile, which fires Troglodyte's first fight |
| 4 | After Trog fight | Free roam, state 4, Mudkip L8, key items and a few consumables, in front of the player's house |
| 5 | Crestfall: redo gym | Gym 1 untouched (no badge, Greta/Dale/Wren unbeaten), team L11, inside the gym door |
| 6 | Crestfall done | Gym 1 as Greta leaves it (badge 1, HM CUT, TM CRUNCH), team L12, outside the Center |
| 7 | Next badge + team | Gives the next badge in table order (1 also runs Greta's rewards) and replaces the party with six test mons at that gym's ace level. Press again for the next one |
| 8 | All field moves | All nine badges and Swampert and Tropius added at L30. They can learn the field moves but know none, which tests the no-move-slot rule ([field-moves.md](field-moves.md)) |

**Utilities > Cheat start** is now 'everything unlocked': state after the first fight and Greta's gym, all nine badges, Pokédex, key items, six test Pokémon at L50 that know no field move. It also starts the daily clock as before. (An earlier version of this file described a smaller cheat start with HM moves taught; that is replaced.)

Rules for maintainers: a preset only sets flags, vars, trainer flags, items and the party (no code). **When you claim a new Veldris flag or var, add it to `Veldris_Debug_ResetStory` in the same commit**; `python3 design/tools/check_debug_reset.py` lists any name in the 'In use by the hack' table of `flags.md` that the file never mentions. Preset 8 and the test teams are test dummies, not canon.

Known limits: the Crestfall gym gates re-close only when the gym map loads, so running preset 6 while standing inside the gym leaves the old gate state until you leave and re-enter (preset 5 warps into the gym, so it is fine). Crestfall 'done' also counts Troglodyte's second fight as won although it is not scripted yet, so the Journal tally reads 2; delete that one line when the scene exists.

## Not adopted yet (needs the author)

A `.claude/hooks/session-start.sh` plus `.claude/settings.json` that would turn the tracked hook on by itself in every fresh web session (and could install the GBA toolchain). Written and tested in scratch but not added: it changes how every Claude session starts here.

## Other debug-menu aids worth knowing

- Utilities > Time Functions: 'Get time', 'Get time of day', 'Set wall clock' (see [time-of-day.md](time-of-day.md)).
- Trainers > Try Battle starts any trainer id (the Mugshot does not play there; see [trainer-slides.md](trainer-slides.md)).
- A copy of the ROM runs headless in mGBA (CLAUDE.md, 'Testing in an emulator'). Presets 1 to 3 were checked in mGBA after the rewrite (menu labels, the lab-scene trigger, Troglodyte's door fight).
