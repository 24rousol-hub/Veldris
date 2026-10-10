#!/usr/bin/env python3
"""Route 1 tall grass gives the Night table at night (design/time-of-day.md). Slow: it needs real wild battles.

The species come from src/data/wild_encounters.json (labels gVeldrisRoute1 and gVeldrisRoute1_Night), so changing
the tables does not break the test. A species that is in both tables proves nothing and is ignored. One only in the
Day table must never show at night; one only in the Night table is what the test waits for.

The test sets the fake clock to 22:00, walks in the grass and runs away from every wild Pokemon until it has seen
enough, then checks that no Day-only species showed up and that at least one Night-only species did.
EMU_DAY_CONTROL=1 repeats the walk at noon as a control (Day-only seen, no Night-only).
"""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import facts
import testkit
from testkit import check

ROUTE1 = "MAP_VELDRIS_ROUTE1"
DAY_LABEL, NIGHT_LABEL = "gVeldrisRoute1", "gVeldrisRoute1_Night"
WANTED = int(os.environ.get("EMU_ENCOUNTERS", "8"))


def grass_pair(g):
    """Two side-by-side tall-grass tiles with grass on the far side too: (x, y) and (x + 1, y)."""
    grass = set(g.find_tiles("MB_TALL_GRASS"))
    for (x, y) in sorted(grass, key=lambda p: (p[1], p[0])):
        if (x - 1, y) in grass and (x + 1, y) in grass and (x + 2, y) in grass:
            return (x, y)
    return None


def sample(emu, hour, wanted):
    """Step back and forth between two grass tiles at the given hour; return the species ids of `wanted` encounters.

    Every step lands on tall grass, so each one is a roll of the wild table (about 1 in 9 on Route 1).
    """
    g = emu.game
    spot = grass_pair(g)
    check(spot is not None, "no stretch of tall grass on Route 1 to walk in")
    a, b = spot, (spot[0] + 1, spot[1])
    g.warp(ROUTE1, a[0], a[1])
    seen = []
    deadline = time.time() + 900
    while len(seen) < wanted:
        check(time.time() < deadline, "only %d wild encounters in 15 minutes. %s" % (len(seen), g.summary()))
        c = g.clock()
        if c["hour"] != hour or c["minute"] >= 50:  # the clock keeps ticking (20 game seconds a second): keep it in the hour
            g.set_clock(hour, 0, 0)
        pos = g.player_pos()
        if pos not in (a, b):  # something moved us (a trainer, a script): start again from the first tile
            g.warp(ROUTE1, a[0], a[1])
            continue
        emu.walk("R" if pos == a else "L")  # normal speed, exactly one tile
        if g.battle_pending():
            seen.append(fight_or_flee(emu))
    return seen


def fight_or_flee(emu):
    """A wild battle is starting: note the species, then run away. Returns the species id."""
    g = emu.game
    g.wait_until(g.in_battle, 60, what="the battle screen")
    party = g.enemy_party()
    check(party and party[0]["species_id"], "the wild Pokemon could not be read. %s" % g.summary())
    species = party[0]["species_id"]
    end = time.time() + 120
    while time.time() < end and g.battle_pending():
        # action menu: Fight / Bag over Pokemon / Run. Down then Right lands on Run; A confirms and clears text.
        # (Stop pressing the moment the battle is over, or the player would walk off in the overworld.)
        emu.press("DOWN", hold=0.08)
        emu.press("RIGHT", hold=0.08)
        emu.press("A", hold=0.08)
        time.sleep(0.25)
    check(not g.battle_pending(), "could not get out of the battle. %s" % g.summary())
    g.wait_overworld_idle(30)
    return species


@testkit.test("Route 1 tall grass gives the Night table at night", slow=True)
def route1_night(emu):
    g = emu.game
    g.debug_preset(4)  # Mudkip L8, story state 4, standing outside the house (the debug menu's Scripts 4)
    party = [m["species_id"] for m in g.party()]
    check(party == [g.L.const("SPECIES_MUDKIP")], "preset 4 should leave one Mudkip in the party, got %s" % party)
    g.warp(ROUTE1, 5, 5, check_tile=False)  # any tile: we only need the map loaded to look for grass
    L = g.L
    day = facts.wild_land_species(g.L.repo, DAY_LABEL)
    night = facts.wild_land_species(g.L.repo, NIGHT_LABEL)
    check(day and night, "src/data/wild_encounters.json needs land tables %s and %s" % (DAY_LABEL, NIGHT_LABEL))
    day_only = {L.const(n) for n in day - night}
    night_only = {L.const(n) for n in night - day}
    check(day_only and night_only, "the Day and Night tables share every species, so this test cannot tell them apart")
    print("      Day-only: %s | Night-only: %s" % (", ".join(sorted(day - night)), ", ".join(sorted(night - day))))

    def names(ids):
        return ", ".join(sorted(L.name_of("SPECIES_", i) or str(i) for i in ids))

    seen = sample(emu, 22, WANTED)
    print("      night encounters (%d): %s" % (len(seen), names(set(seen))))
    check(not (set(seen) & day_only),
          "Day-only species appeared at 22:00: %s (the Night table is not being used)" % names(set(seen) & day_only))
    check(set(seen) & night_only, "no Night-only species in %d night encounters: %s" % (len(seen), names(set(seen))))
    if os.environ.get("EMU_DAY_CONTROL"):
        seen = sample(emu, 12, WANTED)
        print("      day encounters (%d): %s" % (len(seen), names(set(seen))))
        check(not (set(seen) & night_only), "Night-only species appeared at noon: %s" % names(set(seen) & night_only))
        check(set(seen) & day_only, "no Day-only species in %d day encounters" % len(seen))


if __name__ == "__main__":
    testkit.main()
