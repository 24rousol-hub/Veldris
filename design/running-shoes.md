# Running Shoes and the L-button run toggle

Status: BUILT 2026-10-08 at the author's request (running shoes given by the player's mother, plus an L-button toggle). **2026-10-09 (author): run-by-default is ON, and the shoes stay in Mom's first scene ('sooner is better').** The Mom wording is **PROPOSED** (author has not read it yet).

## What the player gets

- **Running Shoes from Mom** in the player's house 1F, the first time she talks to the player (`Hollowbrook_PlayersHouse_1F`).
- **The player runs all the time from then on, and holding B walks instead** (inverted). That is the default: a new game starts with `FLAG_SYS_RUN_BY_DEFAULT` set.
- **L toggles it.** Press L in the overworld to go back to vanilla (B runs); press it again to run all the time. Two short sounds tell the player which way it went (`SE_PC_LOGIN` = on, `SE_PC_OFF` = off).
- The toggle does nothing before the shoes are given, and nothing in the **L=A** button mode (there L is the A button, `src/main.c`).
- Biking, Surfing and underwater are untouched: the run check only runs on foot, and `IsRunningDisallowed` still blocks running on tiles that forbid it.

## How it works

| Piece | Where |
|---|---|
| Shoes owned | `FLAG_SYS_B_DASH` (vanilla flag, already read by the engine). Set by Mom's script |
| Run-by-default | `FLAG_SYS_RUN_BY_DEFAULT` (0x881, was `FLAG_UNUSED_0x881`). Set = run unless B is held. Saved with the game |
| Run condition | `src/field_player_avatar.c`, `PlayerNotOnBikeMoving`: `(B held) != FlagGet(FLAG_SYS_RUN_BY_DEFAULT)` replaces plain `B held` |
| L press | `src/field_control_avatar.c`, `FieldGetPlayerInput`: one hook calling `VeldrisTryToggleRunDefault()` when L is newly pressed and field controls are not locked. Read every frame, not only at a tile centre, so a mid-step press is not lost |
| Toggle code | New hack-owned `src/veldris_run.c` / `include/veldris_run.h` |
| Gift | `data/maps/Hollowbrook_PlayersHouse_1F/scripts.inc`: `MomGiveRunningShoes` (text, fanfare `MUS_OBTAIN_ITEM`, `setflag FLAG_SYS_B_DASH`, instructions) |

### The two paths into the gift

1. **Trigger path (first wake-up).** The coord event at (10,2) starts the wake-up scene. After Mom's line, `MomBringsShoes` walks her across the room to the player, gives the shoes, and walks her back to the kitchen.
2. **Talk path.** If the player gets past the trigger, talking to Mom runs the same gift without the walk.

Both are guarded with `call_if_unset FLAG_SYS_B_DASH`, so the shoes are never given twice, and a debug-menu shoes toggle is respected.

If Mom's walk looks wrong in the game (it was written from the map's coordinates), delete `MomBringsShoes` and its two movements and point the trigger's call at `MomGiveRunningShoes`; the gift still works from a distance.

## What is not done (PROPOSED options)

- ~~Shoes before the lab?~~ **Decided 2026-10-09: yes, keep Mom's first scene ('sooner is better').**
- ~~Default on or off?~~ **Decided 2026-10-09: on.** Two places set it: `VeldrisNewGameDefaults()` (`src/veldris_new_game.c`, called from `NewGameInitData`) and `setflag FLAG_SYS_RUN_BY_DEFAULT` in Mom's gift script, so the box text is always true. The shoes flag still gates running, so nothing runs before Mom's scene.
- **Options-menu entry** instead of or beside the L toggle: would be a bigger edit (`src/option_menu.c`), not done.

## Tests (mGBA, headless, 2026-10-08)

| Check | Result |
|---|---|
| Wake-up trigger at (10,2): Mom walks across the room, speaks, hands over the shoes, walks back to the kitchen | Pass |
| Gift text, fanfare, 'put on' line, box instructions (3 pages), send-off | Pass (see trap below) |
| Walk 0.55 s without B: about 2.5 tiles; with B held: about 4.7 tiles (vanilla run unchanged) | Pass |
| L pressed once: runs without B, **walks while B is held** | Pass |
| L pressed again: back to vanilla (B runs) | Pass |
| The two toggle sounds (`SE_PC_LOGIN`, `SE_PC_OFF`) | Not listened to; both constants exist and the build links |
| Talk path (`MomWakeUp` without the walk) | Not run; it calls the same gift script |
| L=A button mode | Not run; the guard is one `if` |

**Trap found in testing.** A `message` command is silently dropped while an earlier message is still printing. The first version went `playfanfare` / `message` / `waitfanfare` / `msgbox`, and the fanfare ended before the text finished printing, so the whole 'hold B to run, press L' box was skipped. The gift script now has `waitmessage` and `waitbuttonpress` after `waitfanfare`. Use the same three lines after any fanfare message that is followed by another message.

## Change log

| Date | Change |
|---|---|
| 2026-10-08 | Built: Mom's gift, `FLAG_SYS_RUN_BY_DEFAULT`, L toggle |
| 2026-10-09 | Run-by-default on at new game (`src/veldris_new_game.c`) and in the gift script; box text rewritten (B walks, L flips it); debug preset 1 'New game' matches |
