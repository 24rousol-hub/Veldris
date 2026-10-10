# Emulator tests (`design/tools/emu/`)

A robot player. It starts the game in a hidden mGBA window, plays it for you and checks that things happened (a flag
is set, Mom's scene runs, the Night table shows up). It replaces driving screenshots by hand. Nothing here changes the
game or the repo: it only runs a **copy** of the ROM.

Two ways to use it:

* **Tests** (`run_tests.py`): a list of checks, one `PASS` or `FAIL` line each. Run them after a change.
* **`scene.py`**: no test to write. Say what you want to see (`preset:4 warp:... shot:x.png`) and it plays it and saves
  a picture. This replaces the 40-tool-call walk to one NPC.

## Run it

```
make -j4                                   # the robot needs the built game: pokeemerald.gba and pokeemerald.elf
apt-get install -y mgba-sdl xvfb xdotool imagemagick     # once per fresh container
python3 design/tools/emu/run_tests.py              # the quick tests, about 75 seconds
python3 design/tools/emu/run_tests.py --slow       # also the Route 1 night walk, about 2 more minutes (3 in all)
python3 design/tools/emu/run_tests.py --list       # what exists
python3 design/tools/emu/run_tests.py --only Mom   # one test, by part of its name
python3 design/tools/emu/tests/test_new_game.py    # or run one file on its own
```

It prints one line per test and ends with a count. **Exit code 0 means everything passed**, anything else means a
failure. A failure says what was expected, where the game was (map, tile, script state) and saves a screenshot to
`/tmp/veldris_emu_fail/`.

```
PASS  new game defaults  (4.3 s)
FAIL  L toggles run-by-default only after the shoes  (8.3 s)
      the game never saw the L key
      game: [state=overworld map=MAP_HOLLOWBROOK_PLAYERS_HOUSE_2F pos=(2, 4) script=2 tasks=...]
      screenshot: /tmp/veldris_emu_fail/L_toggles_run_by_default_only_after_the_shoes.png
```

The first run after a new build works out where everything lives in the new ROM (see "How it works") and remembers
the answer in `pokeemerald.elf.emu-layout.json` next to the ELF. That takes about 2 seconds, or about 40 seconds on a
tree where `make` has never run. **That file is generated; add `*.emu-layout.json` to `.gitignore`.**

## What the tests check

| Test | What it proves |
|---|---|
| new game defaults | Exp. Share in the Key Items pocket and switched on, run-by-default on, no shoes yet, `FLAG_SYS_CLOCK_SET` set, fake clock about 10:00, bedroom start tile, empty party |
| Mom's scene only fires while `VAR_HOLLOWBROOK_STATE` is 0 | pokes the var to 1: the trigger does nothing; pokes it back to 0: the scene runs and ends with the Running Shoes and state 1 |
| Mom picks her line from the story state | walks up to Mom, presses A, and the text on screen is the line the script file says for state 1 |
| Mom's talk path hands over the Running Shoes | the second way into the gift (talking, without the walk-up scene), which had never been run: shoes, run-by-default and state 1 afterwards |
| L toggles run-by-default only after the shoes | L does nothing before `FLAG_SYS_B_DASH`, flips the flag after it, and is dead again if the shoes go away. It checks the game really saw the key |
| wall clock: running, stopped, and set again | the stopped-clock branch (reachable only by clearing `FLAG_SYS_CLOCK_SET`): the game offers to start it, NO leaves it stopped, YES goes through the set screen and the flag comes back; the running-clock branch offers a reset and shows the clock face. Reads the text the game really printed |
| Hollowbrook east exit is gated until the player has a starter | at `VAR_HOLLOWBROOK_STATE` 1 stepping onto (30,10) starts the gate script and pushes the player back; at state 4 the same step does nothing |
| Lab: both side tiles of the doorway row start the Troglodyte scene | stepping onto (5,10) and (8,10) at state 1 runs the scene (state becomes 2), so the 4-tile doorway cannot be used to skip it |
| Lab: the exit is blocked at state 2 | stepping onto the mat (6,11) at state 2 runs the exit blocker and the player stays in the lab |
| Respawn point: set once at the start, and walking into Hollowbrook does not overwrite a later one | the heal location is Hollowbrook on a new game and stays at a pretend Crestfall heal point after re-entering the town |
| furniture lookup and its scripts are in the ROM | only that the symbols exist (the lookup cannot fire until you give tiles a furniture behaviour in Porymap). Starts no emulator |
| Route 1 tall grass gives the Night table at night (`--slow`) | sets the clock to 22:00, walks in the grass, runs from 8 wild Pokemon: no species that is only in the Day table and at least one that is only in the Night table. The species come from `wild_encounters.json`, so changing the tables does not break it |
| harness: ... (4 tests) | the robot's own plumbing: memory reads and writes, flag and var maths, party and bag decoding, script injection. If one of these fails the robot is wrong, not the game |
| gdb client: checksums, resends, ... | the debugger-port client against a pretend server (bad checksum, lost reply, odd data, error reply, interrupt, the quiet time). Starts no emulator, takes a second |

With `EMU_DAY_CONTROL=1 ... --slow` the Route 1 test also repeats the walk at noon (Day-only species appear, no
Night-only ones).

## Look at the game without a test: `scene.py`

```
python3 design/tools/emu/scene.py preset:4 map shot:town.png
python3 design/tools/emu/scene.py preset:4 warp:MAP_VELDRIS_ROUTE1,13,11 clock:22:00 shot:night.png
python3 design/tools/emu/scene.py var:VAR_HOLLOWBROOK_STATE=1 warp:MAP_HOLLOWBROOK_PLAYERS_HOUSE_1F,#1 talk:LOCALID_HOLLOWBROOK_MOM
python3 design/tools/emu/scene.py --help           # every step
```

It starts a new game in the bedroom (about 4 seconds), does the steps in the order you give them, prints what it saw
and saves pictures to `/tmp/veldris_emu_shots/`. Useful steps: `preset:N` (the debug menu's Scripts 1 to 8), `warp:`,
`walk:RRUU`, `walkto:x,y`, `talk:LOCALID_...` (walks up to the NPC and prints everything it says), `map` (the map as
text, with warps, triggers, grass and NPCs), `objects`, `state`, `party`, `items`, `var:`, `flag:`, `clock:HH:MM`,
`shot:`. If a step fails it says why, with the game's position, and saves `failed.png`.

## How it works (short)

1. **A hidden screen and mGBA.** It starts `Xvfb` on display `:97` (or uses the one already there) and `mgba -g` on a
   copy of the ROM in a temporary folder. The `-g` switch opens mGBA's debugger port (2345) and the robot connects.
2. **Reading and writing the game's memory.** Through that port the robot reads and writes RAM while the game runs
   (`gdbclient.py`). A read takes under a millisecond and costs the game nothing. No addresses are typed in by hand:
   symbol addresses come from `arm-none-eabi-nm` on the ELF, and struct layouts (where `flags`, `vars`, the bag, a
   Pokemon's species live) and every `FLAG_`, `VAR_`, `ITEM_`, `SPECIES_`, `MAP_` and `LOCALID_` number come from the
   compiler: it compiles a tiny generated C file against the repo's own headers with the Makefile's flags
   (`layout.py`). If the headers no longer match the ELF the robot says so and asks for a rebuild instead of reading
   garbage.
3. **Pressing buttons.** `xdotool` holds keys (X = A, Z = B, Return = Start, Backspace = Select, a = L, s = R). The
   robot plays at turbo speed (mGBA's Tab key, about 8 times real time) and drops to normal speed for exact walking.
   After every press it checks that the game really saw the button.
4. **Shortcuts that use the game's own code.** `game.warp(...)` and `game.debug_preset(4)` point the game's script
   engine at a few script bytes, or at the debug menu's preset scripts already in the ROM, so a test can skip to
   Route 1 with Mudkip in the party in a fraction of a second.

## Limits (honest list)

- **One run at a time.** mGBA's debugger port is fixed at 2345 (`-C gdb.port=` is ignored, tried) and serves one
  client, so only one emulator can run on the machine. Two runs queue up (a lock file); a different program holding the
  port stops the run with a clear message.
- **The trap that looks like a hang.** The debugger port freezes the game if the robot sends anything within
  about 0.1 s after telling it to continue, and keeps it frozen while packets keep coming. The robot therefore waits
  0.15 s after every continue (`gdbclient.py` explains). Reading is free, so it normally never stops the game; it stops
  it only to write several things as one unit (a flag, a script, the party).
- **Buttons are real key presses.** The game re-reads the pad every frame, so a button cannot be written into
  memory. Tests need the X display and about one core, and a key press can be lost when the machine is busy (a build
  running next to the test). Where one press has one visible result use `emu.press_until(...)`; the `press` call tells
  you whether the game saw the key.
- **Walking is at normal speed.** At 8 times speed one tile lasts 35 ms, shorter than a key release can be timed, so
  exact walking drops to normal speed: about 0.3 s per tile (0.17 s with `run=True`). Everything else runs fast.
- **It looks at memory, not at the picture.** It cannot see wrong colours, a cut-off sprite or text that does not fit
  (`dialogue_check.py` does the text). Failure screenshots are for you to look at.
- **The Costume Box picker.** Mom's gift opens the player-look menu (`Task_LookMenu`, `src/veldris_look.c`). `read_dialogue` and `mash` press B to leave it; a new test that walks past the gift must do the same or it will wait forever for the overworld to be idle.
- **It is mGBA, not Delta.** Your phone's emulator (VBA-M based) can differ in timing and drawing. This tests the
  game's logic, not how Delta shows it.
- **Wild encounters are random.** The Route 1 test is a sample. A wrong table fails it at once (a Day-only species
  at night is impossible with the right table). A right table fails only by bad luck, about 1 run in 2000 (no
  Night-only species in 8 night encounters).
- **It follows the current build.** Variable names, maps and species must exist in this build, and the Mom tests name
  Veldris story things, so they need updating when the story changes. It tests the dev ROM (`pokeemerald.gba`), not
  the `make release` one (that has no debug scripts).
- The first layout step asks `make -n` for the compile flags (it only prints, but `make` first rebuilds its own
  dependency files, which is what the 40 seconds on a never-built tree are). `EMU_NO_MAKE=1` skips that and uses a
  built-in copy of the flags (identical today, checked).
- Not covered: sound, saving and loading, link features, anything that needs a real clock (the game uses its fake
  clock and the robot sets it directly).

## How fast is it (measured 2026-10-09, 4 cores shared with other builds, so on a quiet machine it is faster)

| What | Time |
|---|---|
| Work out the layout of a new build (first run only) | 1.6 s (about 40 s on a tree where `make` has never run) |
| Start mGBA, boot, title screen, quickstart, bedroom ready | about 3 s |
| One memory read or write | under 1 ms, and the game does not slow down |
| `warp` or `debug_preset` | 0.2 to 1 s |
| Walking one tile at normal speed | 0.29 s (0.17 s with `run=True`) |
| The quick tests (12) | 74 s |
| Everything including the Route 1 night walk | about 190 s (the walk alone 100 s: about 9 steps and one battle per wild Pokemon) |

## Adding a test

Create `design/tools/emu/tests/test_<topic>.py`:

```python
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import testkit
from testkit import check, check_eq

@testkit.test("Preset 4 leaves Mudkip and ten Potions")   # the name shown in the output
def preset4(emu):                                         # `emu` starts as a fresh new game in the bedroom
    g = emu.game
    g.debug_preset(4)                                     # the debug menu's Scripts 4, run for you
    check_eq(g.party()[0]["level"], 8, "Mudkip's level")
    check(g.bag_count("ITEM_POTION") >= 10, "preset 4 should stock Potions")
    g.warp("MAP_VELDRIS_ROUTE1", 13, 11)                  # teleport (map tiles, as Porymap shows them)
    ok, steps = emu.walk("UU")                            # walk tile by tile (U D L R); stops early if blocked
    emu.press("A")                                        # hold a button briefly: A B START SELECT L R UP DOWN LEFT RIGHT
    shown = emu.talk_to("LOCALID_HOLLOWBROOK_MOM")        # walk up to an NPC, press A, click through, return the texts

if __name__ == "__main__":
    testkit.main()
```

Options on `@testkit.test`: `boot="title"` (stop at the title screen) or `boot=None` (start the emulator and do
everything yourself), `slow=True` (only with `--slow`), `emulator=False` (no emulator, just the ELF: the test gets
`ctx.repo` and `ctx.layout`), `turbo=False` (start at normal speed). `check(cond, message)` and
`check_eq(actual, expected, what)` fail the test with a readable message. A test that raises or hangs is reported as
a failure (hang limit: 3 minutes, 15 for slow tests). Pick free tiles for `warp` with `scene.py ... map`; `warp`
refuses a wall tile.

What `emu.game` can do (all of it reads the live game):

| Ask | Methods |
|---|---|
| Flags and vars | `flag_get`, `flag_set`, `flag_clear`, `var_get`, `var_set` (names or numbers) |
| Items and party | `bag()`, `bag_count(item)`, `bag_where(item)`, `party()`, `enemy_party()` (species, level, hp, moves) |
| Where am I | `map_name()`, `map_id()`, `player_pos()`, `saved_pos()`, `player_facing()`, `read_map()`, `ascii_map()`, `find_tiles("MB_TALL_GRASS")`, `special_tiles()`, `objects()`, `object("LOCALID_...")`, `find_path((x, y))` |
| Clock | `clock()`, `set_clock(hour, minute)` |
| What is it doing | `state()`, `overworld_idle()`, `script_running()`, `battle_pending()`, `busy()`, `tasks()`, `callback2()`, `keys_held()`, `message_text()` (what the last message box said), `summary()`, `wait_until(fn, timeout, settle=3)` |
| Skip ahead | `warp(map, x, y)` or `warp(map, warp_id=1)`, `debug_preset(n)`, `run_rom_script("Label")`, `run_script(bytes)` |

`emu` itself: `new_game()`, `boot_to_title()`, `quickstart()`, `press(button)`, `press_until(button, fn)`,
`walk("RRUU")`, `walk_to(x, y)`, `face("N")`, `approach(npc)`, `talk_to(npc)`, `read_dialogue()`, `mash("A")`,
`turbo(True/False)`, `screenshot(path)`.

## Environment variables

`EMU_DISPLAY` (virtual screen number, default 97), `EMU_KEEP=1` (keep the temporary folder with mGBA's log),
`EMU_NO_MAKE=1`, `EMU_ENCOUNTERS` (wild fights in the Route 1 test, default 8), `EMU_DAY_CONTROL=1`,
`VELDRIS_REPO` (repo root, if the scripts are not inside it), `MGBA` (path to mGBA, default `/usr/games/mgba`).

## If something goes wrong

| Message | Do this |
|---|---|
| `is missing. Build the game first` | `make -j4` |
| `The headers have changed since the ELF was built` | `make -j4`, then run again |
| `port 2345 is in use by a program that is not this harness` | stop the other mGBA that was started with `-g` |
| `no symbol 'X' in the ELF (did you mean ...)` | the name changed or was optimised out; the message suggests near matches |
| `mGBA exited at start-up` | read the log it prints; usually a missing ROM or display |
| `warped onto a blocked tile` | pick a free tile; `scene.py ... map` draws the map |
| Many `Xvfb`/`mgba` processes left over | a run was killed with `kill -9`; stop only those pids by number |
