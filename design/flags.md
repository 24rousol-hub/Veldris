# Flags and vars

**Rules**

1. Every flag or var the hack uses is recorded in the table below, in the same commit that first uses it.
2. Take unused ones from the spare pool. **Never overwrite or repurpose one that is in use.**
3. Before claiming a spare, grep its name and its numeric value across `include/`, `src/`, `data/` and `test/`. Then check the table below.
4. Never hand-allocate a flag in the trainer block. Those come from the trainer ID.
5. Claiming a flag = renaming its `FLAG_UNUSED_0x...` line in place in `include/constants/flags.h`, keeping the value. Do the same for vars in `vars.h`. Log each rename in [engine-edits.md](engine-edits.md). (Porymap fills its flag and var dropdowns from those two headers. A separate header would not show up there.)

Measured on 2026-09-29 against this tree, Emerald build (`IS_FRLG` is 0). Values come from the preprocessor (`arm-none-eabi-gcc -E -dM`), not from reading numbers by hand.

## How the flag space is laid out

| Block | Range (hex) | Range (dec) | Safe for story state? |
|---|---|---|---|
| Temp flags | 0x000-0x01F | 0-31 | **No.** Cleared every time a map loads |
| Story, hide/show, item, event flags | 0x020-0x4FF | 32-1279 | Yes. Most spare flags live here |
| Trainer flags | 0x500-0x85F | 1280-2143 | **No.** One flag per trainer ID, set by the engine |
| System flags | 0x860-0x91F | 2144-2335 | Yes, where spare. Holds the badges (0x867-0x86E) and the `FLAG_VISITED_*` fly flags starting at 0x86F |
| Daily flags | 0x920-0x95F | 2336-2399 | **No.** Reset by the daily-flag clear |
| Special flags | 0x4000-0x407F | 16384-16511 | **No.** Computed at runtime, not saved |

Vars: persistent vars are 0x4000-0x40FF (256 in total). `VAR_TEMP_0` to `VAR_TEMP_F` (0x4000-0x400F) reset on map load. Special vars 0x8000-0x8015 are volatile script arguments and are never saved.

## In use by the hack

| Name | Value | Kind | Purpose | Set by | Cleared by | Added in |
|---|---|---|---|---|---|---|
| _(none yet)_ | | | | | | |

## Spare pool: permanent flags

373 flags are named `FLAG_UNUSED_*`. **317 are safe to claim.** Excluded, with reasons:

- 52 sit in the daily range (0x920-0x95F). They reset every day. One of them, `FLAG_UNUSED_0x95F`, is also used by name: it defines `DAILY_FLAGS_END` in `flags.h`.
- `FLAG_UNUSED_0x91F`, just below the daily range, is used by name: it defines `DAILY_FLAGS_START`.
- `FLAG_UNUSED_RS_LEGENDARY_BATTLE_DONE` (0x71) is used by `data/maps/CaveOfOrigin_UnusedRubySapphireMap1/scripts.inc`.
- That is 54 excluded. The 2 reserved below bring the total to 56, and 373 - 56 = 317.
- `FLAG_UNUSED_0x1AA` and `FLAG_UNUSED_0x1AB` are **reserved as rematch headroom.** Trainer-registered flags run from 0x15C for `REMATCH_TABLE_ENTRIES` (78) entries, so 0x15C-0x1A9 are taken and the next two are the first to go if rematches are added. Beyond those two, the next flag (0x1AC) is `FLAG_DEFEATED_DEOXYS`.

The flags in `include/constants/flags_frlg.h` with the same names are the FRLG variant. They are not compiled into the Emerald build, so they do not count as uses.

Claimable ranges (each flag is named `FLAG_UNUSED_0x` plus its 3-digit hex value):

| Range | Count | Proposed block (PROPOSED) |
|---|---|---|
| 0x020-0x04F | 48 | **Fly visited flags** for Veldris towns (18 needed: 0x020-0x031). The rest general purpose, first-fit |
| 0x054-0x055 | 2 | General purpose |
| 0x068 | 1 | General purpose |
| 0x0E9 | 1 | General purpose |
| 0x1DA | 1 | General purpose |
| 0x1DE-0x1E3 | 6 | General purpose |
| **0x264-0x2BB** | 88 | **Story beats and cutscenes.** Note: config comments in `include/config/battle.h` and `pokemon.h` use 0x264 as their example toggle flag. Use 0x264 for a config toggle, or skip it |
| 0x2D9 | 1 | General purpose |
| 0x468, 0x470, 0x472, 0x479 | 1 each | General purpose |
| **0x493-0x4EF** | 93 | **Per-map one-shots** (talked-to flags, single pickups) for towns and routes |
| 0x4F9-0x4FA, 0x4FF | 2 + 1 | General purpose |
| 0x863 | 1 | General purpose |
| 0x881-0x887 | 7 | General purpose |
| 0x88E-0x88F | 2 | General purpose |
| 0x8E3 | 1 | General purpose |
| **0x8E5-0x91E** | 58 | **Late game:** gyms 5 to 9, Elite Four, post-game |

Reminder: the spare flags for ordinary game state are numerous but they are not unlimited. 317 flags for 18 towns, 33 routes, 9 gyms, the League and the post-game is enough only if boolean state is packed sensibly. Use `VAR_TEMP_*` for anything local to one map visit.

## Spare pool: permanent vars

23 vars are named `VAR_UNUSED_*`. **21 are safe to claim.** Excluded: `VAR_UNUSED_0x8014`, which is a volatile special var (0x8000 block, never saved). Also note `VAR_UNUSED_0x404E`: the config comment in `include/config/battle.h` names it as an example toggle. Claim it for a config switch, or skip it.

Claimable vars: 0x404E, 0x4083, 0x408B, 0x4091, 0x409B, 0x409D, 0x40A1, 0x40A8, 0x40B8, 0x40BB, 0x40DB, 0x40DC, 0x40E5, 0x40F7 to 0x40FF (9 in a row, 0x40F7-0x40FF).

**Only 21 spare persistent vars.** Use a var only for a state that has more than two values (a story chapter counter, a puzzle stage). Use a flag for anything yes/no. If we run short, the remaining Hoenn vars can be freed by removing the Hoenn maps that use them, but that is a decision for the author.

## Related limits worth knowing

- **Trainer slots.** `TRAINERS_COUNT` is 855 and `MAX_TRAINERS_COUNT` is 864, so only **9 new trainer IDs** fit before trainer flag space overflows (upstream's own note in `include/constants/opponents.h`). New trainers must reuse IDs of vanilla trainers you no longer need (rename them), or `MAX_TRAINERS_COUNT` is raised, which costs save block space. `TRAINER_CRESTFALL_GRETA` needs one of these. See open decision 6 in [game-bible.md](game-bible.md).
- **Badges.** Flags 0x867-0x86E, and 0x86F is already a `FLAG_VISITED_*`. See open decision 1 in [game-bible.md](game-bible.md).
- **Fly flags.** `FLAG_VISITED_*` are Hoenn-named and sit in the system block. See [region-map.md](region-map.md).
