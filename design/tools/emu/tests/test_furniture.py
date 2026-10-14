#!/usr/bin/env python3
"""Talking furniture (src/veldris_furniture.c): only checks the build contains it.

The lookup is unreachable in the game until the author gives metatiles a furniture behaviour in Porymap
(design/furniture-lines.md), so this does not start the emulator. It reads src/veldris_furniture.c and checks
the ELF: the lookup function, one script per table row, and valid, distinct behaviours.
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import testkit
from testkit import check, check_eq


@testkit.test("furniture lookup and its scripts are in the ROM", emulator=False)
def furniture_symbols(ctx):
    src = (ctx.repo / "src" / "veldris_furniture.c").read_text()
    L = ctx.layout
    check(L.has_symbol("VeldrisGetFurnitureScript"), "VeldrisGetFurnitureScript is not in the ELF")
    scripts = re.findall(r"extern const u8 (Veldris_EventScript_Furniture_\w+)\[\]", src)
    rows = re.findall(r"\{\s*(MB_\w+)\s*,\s*(Veldris_EventScript_Furniture_\w+)\s*\}", src)
    check(len(scripts) > 0, "found no furniture scripts in src/veldris_furniture.c")
    check_eq(len(rows), len(scripts), "table rows vs script declarations")
    missing = [s for s in scripts if not L.has_symbol(s)]
    check(not missing, "scripts declared but not in the ELF: %s" % ", ".join(missing))
    values = {}
    for behavior, script in rows:
        v = L.const(behavior)  # raises with a suggestion if the name is wrong
        check(v not in values, "%s and %s share behaviour value %d" % (behavior, values.get(v), v))
        values[v] = behavior
        check(script in scripts, "row for %s points at an undeclared script %s" % (behavior, script))


if __name__ == "__main__":
    testkit.main()
