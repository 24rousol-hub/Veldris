#!/usr/bin/env python3
"""The four-starter scene in Prof. Fennick's lab, played through the game's own scripts (design/scripts/README.md,
design/flags.md for VAR_STARTER_MON and VAR_TROG_STARTER).

The author's decision of 2026-10-12 ("A: Johto + Togepi", design/decisions/story.md):

    ball 1   VAR_STARTER_MON 0   Grass   CHIKORITA   (trainers.party tag Tag6)
    ball 2   VAR_STARTER_MON 1   Fire    CYNDAQUIL   (Tag7)
    ball 3   VAR_STARTER_MON 2   Water   TOTODILE    (Tag8)
    ball 4   VAR_STARTER_MON 3   the one Prof. Fennick reveals as an apology: TOGEPI, an ordinary level 5 Pokemon (not an egg)

The species are written out in STARTERS on purpose: this file is what stops a later edit from quietly changing them. If
the author ever picks other starters, change STARTERS and nothing else. Troglodyte takes one of the three on-show balls
at random (VAR_TROG_STARTER 0, 1 or 2), so the player always chooses from the three that are left.

What the tests do (six tests, run them with `--only starters`):

1. "tables and name helpers": reads the ROM table sStarterMon (src/starter_choose.c: the four species in ball order, the
   fourth last) and runs the two name-buffering helper scripts that are already in the ROM, once per value:
   Hollowbrook_EventScript_BufferTrogSpecies for VAR_TROG_STARTER 0 to 2 (the name the lab and the aides print for
   Troglodyte's pick) and Hollowbrook_EventScript_BufferPlayerStarter for VAR_STARTER_MON 0 to 3 (the name the house,
   the neighbour and later scenes print for the player's pick). The text they leave in the game's string buffers is read back.
2. "lab ball 1/2/3/4 gives ...": for each ball, the state the Troglodyte scene leaves (story state 2, Troglodyte's ball
   gone, ball 4 revealed) is set up, the player stands in front of the ball on the player's side of the counter, presses A
   and answers the game's own YES/NO boxes (YES to 'Choose the X?', NO to the nickname). Checks: the question names the
   right species, the party is exactly that species at level 5 (not an egg), VAR_STARTER_MON is the ball's value, the story
   state is 3, and only that ball left the table.
3. "the lab scene end to end": the real scene from the doorway (state 1): Troglodyte takes one ball at random, Fennick
   reveals the fourth, then the player takes a ball Troglodyte did not take. Checks: VAR_TROG_STARTER is 0 to 2 and his
   ball is the one that is gone, ball 4 was hidden before and is on the table after, the name the scene printed for him
   (STR_VAR_2) is his species, VAR_STARTER_MON differs from VAR_TROG_STARTER, and the same party/state checks as in 2.
   Troglodyte's roll is random, so this test follows whatever he rolled (the player takes the next ball round), and over
   several runs every ball gets taken.

Not covered here: Troglodyte's own fights (the robot never plays them; for his three starter versions in
trainers.party see design/tools/teamcheck.py, trainer_lint.py and the unit tests in test/veldris.c), the nickname
screen, the lines in the player's house and the neighbour's house, and the picture shown with the question (the robot
reads memory, not pixels).
"""
import os
import struct
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import facts
import testkit
from game import decode_text, load_charmap
from testkit import check, check_eq

LAB = "MAP_HOLLOWBROOK_PROF_FENNICK_LAB"
LAB_FOLDER = "Hollowbrook_ProfFennickLab"
LEVEL = 5

# (ball number, VAR_STARTER_MON value, species, role)
STARTERS = [
    (1, 0, "SPECIES_CHIKORITA", "Grass starter"),
    (2, 1, "SPECIES_CYNDAQUIL", "Fire starter"),
    (3, 2, "SPECIES_TOTODILE", "Water starter"),
    (4, 3, "SPECIES_TOGEPI", "the fourth starter"),
]
ON_SHOW = STARTERS[:3]
SPECIES_ORDER = [s[2] for s in STARTERS]

_CHARMAPS = {}


def shown_name(species):
    """What the game prints for a species, in lower case: SPECIES_TOTODILE -> 'totodile'.

    The game's species names are written in mixed case ('Totodile'), so every comparison is made in lower case.
    """
    return species[len("SPECIES_"):].replace("_", " ").lower()


def ball_id(n):
    return "LOCALID_HOLLOWBROOK_LAB_BALL_%d" % n


def hide_flag(n):
    return "FLAG_HIDE_HOLLOWBROOK_LAB_BALL_%d" % n


def species_names(g, ids):
    return [g.L.name_of("SPECIES_", i) or i for i in ids]


def check_species(g, got_ids, want_species, what):
    want = [g.L.const(s) for s in want_species]
    check(list(got_ids) == want, "%s: expected %s, got %s" % (what, want_species, species_names(g, got_ids)))


def buffer_text(g, symbol):
    """The game text held in a string buffer such as gStringVar1, as readable text."""
    path = g.L.repo / "charmap.txt"
    if path not in _CHARMAPS:
        _CHARMAPS[path] = load_charmap(path)
    return decode_text(g.gdb.read(g.a(symbol), 48), _CHARMAPS[path])


def run_name_helper(g, label, buffer_symbol):
    """Run a name-buffering helper script that lives in the ROM and return the name it left in `buffer_symbol`.

    The buffer is emptied first (a terminator in its first byte), so a name left over from earlier cannot pass.
    The helpers end with `return` and no caller: with an empty call stack the script engine simply stops.
    """
    g.gdb.put_u8(g.a(buffer_symbol), 0xFF)
    g.run_rom_script(label)
    g.wait_until(lambda: not g.script_running() and g.overworld_idle(), 30, what="%s to finish" % label)
    return buffer_text(g, buffer_symbol)


def read_starter_table(g):
    """The u16 species ids of sStarterMon in the ROM (the table src/starter_choose.c indexes by VAR_STARTER_MON)."""
    L = g.L
    names = sorted(n for n in L.symbols if n == "sStarterMon" or n.startswith("sStarterMon."))
    check(names, "there is no sStarterMon in the ELF (renamed or optimised out); it is the table in src/starter_choose.c")
    size = L.size(names[0])
    check(size % 2 == 0 and size > 0, "sStarterMon has an odd size: %d bytes" % size)
    return list(struct.unpack("<%dH" % (size // 2), g.gdb.read(g.a(names[0]), size)))


def ball_tile(repo, n):
    """(x, y) of ball n, from the lab's map.json."""
    for o in facts.map_json(repo, LAB_FOLDER)["object_events"]:
        if o["local_id"] == ball_id(n):
            return o["x"], o["y"]
    check(False, "no object %s in the lab's map.json" % ball_id(n))


def balls_present(g):
    """The ball numbers (1 to 4) that are on the table right now (a taken or still hidden ball is not an object)."""
    return {n for n in (1, 2, 3, 4) if g.object(ball_id(n)) is not None}


def stand_before_ball(emu, n, warp):
    """Stand on the player's side of the counter (two tiles below the ball) and face it. The counter row sits between."""
    g = emu.game
    bx, by = ball_tile(g.L.repo, n)
    spot = (bx, by + 2)
    if warp:
        g.warp(LAB, *spot)
    else:
        check(emu.walk_to(*spot), "could not walk to %s in front of ball %d; at %s" % (spot, n, g.player_pos()))
    check(emu.face("N"), "could not turn to face the counter in front of ball %d. %s" % (n, g.summary()))
    return spot


def click_through(emu, answers=("A", "B"), timeout=90.0):
    """Click through the script that is running, like Emulator.read_dialogue, but with the answers for the YES/NO boxes.

    The boxes are answered from `answers` in order ('A' = YES, 'B' = NO); when the list is used up the answer is B.
    A box is only counted once: the answer is pressed again if the box is still there (a lost key press).
    Returns the text that was on screen at each YES/NO box, in order. Waits until the player is free again.
    """
    g = emu.game
    queue = list(answers)
    prompts = []
    end = time.time() + timeout
    while g.script_running():
        check(time.time() < end, "the script did not end within %d s. %s" % (timeout, g.summary()))
        names = g.task_names()
        if "Task_LookMenu" in names:  # the Costume Box picker: B leaves it
            emu.press("B", hold=0.1)
        elif "Task_HandleYesNoInput" in names:
            prompts.append(g.message_text())
            answer = queue.pop(0) if queue else "B"
            emu.press_until(answer, lambda: "Task_HandleYesNoInput" not in g.task_names(), hold=0.1)
        else:
            emu.press("A", hold=0.1)
        time.sleep(0.25)
    g.wait_overworld_idle(30)
    return prompts


def take_ball(emu, n, species):
    """Press A on ball n (the player already faces it) and say YES to it, NO to the nickname. Checks what it leaves."""
    g = emu.game
    name = shown_name(species)
    before = balls_present(g)
    check(n in before, "ball %d is not on the table (balls there: %s)" % (n, sorted(before)))
    emu.press_until("A", g.script_running, wait=2.0)
    prompts = click_through(emu)
    check(prompts, "ball %d never showed its YES/NO question" % n)
    check(name in prompts[0].lower(), "ball %d should ask about the %s, the game asked %r" % (n, name, prompts[0]))
    party = g.party()
    check_species(g, [m["species_id"] for m in party], [species], "party after taking ball %d" % n)
    check_eq(party[0]["level"], LEVEL, "level of the starter from ball %d" % n)
    check(not party[0]["is_egg"], "the starter from ball %d must be an ordinary Pokemon, not an egg" % n)
    check_eq(g.var_get("VAR_STARTER_MON"), n - 1, "VAR_STARTER_MON after taking ball %d" % n)
    check_eq(g.var_get("VAR_HOLLOWBROOK_STATE"), 3, "story state after choosing (Troglodyte waits outside)")
    check(g.flag_get(hide_flag(n)), "%s should be set once ball %d is taken" % (hide_flag(n), n))
    check_eq(sorted(balls_present(g)), sorted(before - {n}), "balls left on the table after taking ball %d" % n)


# ---------------------------------------------------------------------------------------------------------------------
# 1. The tables and the name helpers
# ---------------------------------------------------------------------------------------------------------------------

@testkit.test("starters: the species table and the name helpers say Chikorita, Cyndaquil, Totodile, Togepi")
def tables_and_helpers(emu):
    g = emu.game
    check_species(g, read_starter_table(g), SPECIES_ORDER,
                  "sStarterMon (three on show in ball order, the fourth last; VAR_STARTER_MON indexes it)")
    # Troglodyte's pick (0 to 2) as the lab scene and the aides print it.
    for idx, (ball, _, species, role) in enumerate(ON_SHOW):
        g.var_set("VAR_TROG_STARTER", idx)
        said = run_name_helper(g, "Hollowbrook_EventScript_BufferTrogSpecies", "gStringVar2")
        check_eq(said.lower(), shown_name(species), "name buffered for VAR_TROG_STARTER %d (ball %d, %s)" % (idx, ball, role))
    # The player's pick (0 to 3) as the house and the neighbour print it; 3 is the fourth starter.
    for ball, idx, species, role in STARTERS:
        g.var_set("VAR_STARTER_MON", idx)
        said = run_name_helper(g, "Hollowbrook_EventScript_BufferPlayerStarter", "gStringVar1")
        check_eq(said.lower(), shown_name(species), "name buffered for VAR_STARTER_MON %d (ball %d, %s)" % (idx, ball, role))


# ---------------------------------------------------------------------------------------------------------------------
# 2. Each ball, taken through the game's own ball script
# ---------------------------------------------------------------------------------------------------------------------

def _register_ball_test(ball, idx, species, role):
    title = "starters: lab ball %d gives %s (VAR_STARTER_MON %d)" % (ball, shown_name(species).title(), idx)

    @testkit.test(title)
    def take_one_ball(emu):
        g = emu.game
        # What the Troglodyte scene leaves behind, set before the lab loads so its objects are built from the flags:
        # story state 2 (the player is choosing), Troglodyte gone with one of the three on-show balls, ball 4 revealed.
        # He takes a ball other than the one under test (ball 4 is not one he can take: any of 1 to 3 will do).
        trog = (idx + 1) % 3 if idx < 3 else 1
        g.var_set("VAR_TROG_STARTER", trog)
        g.var_set("VAR_HOLLOWBROOK_STATE", 2)
        g.flag_set("FLAG_HIDE_HOLLOWBROOK_LAB_TROG")
        g.flag_set(hide_flag(trog + 1))
        g.flag_clear(hide_flag(4))
        stand_before_ball(emu, ball, warp=True)
        check_eq(sorted(balls_present(g)), sorted({1, 2, 3, 4} - {trog + 1}),
                 "balls on the table when the player arrives (Troglodyte took ball %d)" % (trog + 1))
        take_ball(emu, ball, species)
        if idx < 3:
            check(g.var_get("VAR_STARTER_MON") != g.var_get("VAR_TROG_STARTER"),
                  "the player and Troglodyte both ended up with ball %d" % ball)

    return take_one_ball


for _ball, _idx, _species, _role in STARTERS:
    _register_ball_test(_ball, _idx, _species, _role)


# ---------------------------------------------------------------------------------------------------------------------
# 3. The whole scene, from the doorway
# ---------------------------------------------------------------------------------------------------------------------

@testkit.test("starters: the lab scene end to end (Troglodyte takes a ball, Fennick reveals the fourth, the player picks)",
              timeout=240)
def whole_scene(emu):
    g = emu.game
    # State 1 = Mom's scene is over and no Pokemon was chosen. The doorway row (y 10) starts the scene; step onto (6,10).
    g.var_set("VAR_HOLLOWBROOK_STATE", 1)
    g.warp(LAB, 6, 9)
    before = balls_present(g)
    check(4 not in before, "ball 4 should be hidden until Fennick reveals it, balls on the table: %s" % sorted(before))
    check({1, 2, 3} <= before, "the three on-show balls should all be on the table before the scene: %s" % sorted(before))
    check(g.object("LOCALID_HOLLOWBROOK_LAB_TROG") is not None, "Troglodyte should be waiting in the lab")
    ok, _ = emu.walk("D")
    check(ok, "could not step onto the scene trigger (6,10); at %s" % (g.player_pos(),))
    g.wait_until(g.script_running, 5, what="the Troglodyte scene to start")
    emu.mash("A", until=lambda: g.var_get("VAR_HOLLOWBROOK_STATE") == 2 and g.overworld_idle(), timeout=150)

    # Troglodyte's roll and what it left on the table.
    check_eq(g.var_get("VAR_HOLLOWBROOK_STATE"), 2, "story state after the scene (the player is choosing)")
    trog = g.var_get("VAR_TROG_STARTER")
    check(trog in (0, 1, 2), "VAR_TROG_STARTER should be 0, 1 or 2 after the scene, it is %d" % trog)
    taken_ball, _, taken_species, _ = ON_SHOW[trog]
    after = balls_present(g)
    check_eq(sorted(after), sorted({1, 2, 3, 4} - {taken_ball}),
             "balls on the table after the scene (Troglodyte rolled %d, so he took ball %d)" % (trog, taken_ball))
    check(g.object("LOCALID_HOLLOWBROOK_LAB_TROG") is None, "Troglodyte should have left the lab")
    check(g.flag_get(hide_flag(taken_ball)), "%s should be set: Troglodyte took that ball" % hide_flag(taken_ball))
    said = buffer_text(g, "gStringVar2")
    check_eq(said.lower(), shown_name(taken_species), "Troglodyte's species as the scene printed it (STR_VAR_2)")

    # The player takes the next ball round, so over several runs every ball gets taken.
    ball, idx, species, role = ON_SHOW[(trog + 1) % 3]
    print("      Troglodyte rolled %d (%s); the player takes ball %d (%s)"
          % (trog, shown_name(taken_species), ball, shown_name(species)))
    stand_before_ball(emu, ball, warp=False)
    take_ball(emu, ball, species)
    check(g.var_get("VAR_STARTER_MON") != g.var_get("VAR_TROG_STARTER"),
          "the player (VAR_STARTER_MON) and Troglodyte (VAR_TROG_STARTER) both ended up with ball %d" % ball)


if __name__ == "__main__":
    testkit.main()
