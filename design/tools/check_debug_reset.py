#!/usr/bin/env python3
"""Does the debug presets file still mention every flag and var in design/flags.md? (hack tool, optional)

Reads the 'In use by the hack' table of design/flags.md (expanding the table's short forms: `X_1` to `_3`, and
`X_TALKED1`, `_TALKED2`) and lists every FLAG_/VAR_ name that data/scripts/veldris_debug.inc never mentions, so a new
flag cannot be forgotten in Veldris_Debug_ResetStory. A mention anywhere in the file counts; it does not check that
the flag is really cleared. A name that appears only in prose is never checked, so keep every flag and var in the table.

Run from the repo root:  python3 design/tools/check_debug_reset.py      Exit code 1 if a name is missing.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def expand(cell):
    """One table cell -> full names."""
    cell = re.sub(r"\(.*?\)", "", cell)                          # drop '(alias of ...)' notes
    toks = re.findall(r"`([A-Za-z0-9_]+)`", cell)
    if not toks:
        return []
    first, names = toks[0], [toks[0]]
    for t in toks[1:]:
        m = re.fullmatch(r"(.*_)(\d+)", first)
        if not t.startswith("_"):
            names.append(t)
        elif " to " in cell and m and re.fullmatch(r"_\d+", t):  # `X_1` to `_3`
            names += [f"{m.group(1)}{i}" for i in range(int(m.group(2)) + 1, int(t[1:]) + 1)]
        else:                                                      # `X_TALKED1`, `_TALKED2`
            names.append(first.rsplit("_", 1)[0] + t)
    return names


def main():
    flags_md = (ROOT / "design" / "flags.md").read_text(encoding="utf-8")
    block = flags_md.split("## In use by the hack", 1)[1].split("\n## ", 1)[0]
    names = []
    for row in block.splitlines():
        if row.startswith("|") and not row.startswith(("|---", "| Name")):
            names += expand(row.split("|")[1])
    inc = (ROOT / "data" / "scripts" / "veldris_debug.inc").read_text(encoding="utf-8")
    missing = [n for n in dict.fromkeys(names) if n not in inc]
    for n in missing:
        print(f"MISSING from veldris_debug.inc: {n}")
    print(f"{len(names)} name(s) in flags.md, {len(missing)} missing from veldris_debug.inc")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
