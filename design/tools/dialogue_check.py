#!/usr/bin/env python3
"""Check dialogue lines against the game's text box, using the game's own font widths.

Usage (from the repo root):
    python3 design/tools/dialogue_check.py data/text/birch_speech.inc
    python3 design/tools/dialogue_check.py data/maps/Hollowbrook/scripts.inc --warn 200

It reads every `.string "..."` block under a label, splits it into text-box lines
(`\\n` and `\\l` start a new line, `\\p` starts a new page), and adds up each line's width
from `gFontNormalLatinGlyphWidths` in src/fonts.c and the byte values in charmap.txt.

Limits (measured in this tree, see design/dialogue-style.md):
    - the overworld text box and the intro box are both 27 tiles wide = 216 px, 2 lines visible
    - FONT_NORMAL has no letter spacing, so a line is just the sum of its glyph widths

It treats {PLAYER} as 7 wide letters and {STR_VAR_n} (unknown length) as a warning, not an error.
It also flags: characters missing from the charmap, an escaped double quote (a build error),
{RIVAL} (expands to MAY or BRENDAN), and a label whose text has no `$` terminator.
Standard library only. Exit code 1 if anything is over the limit or otherwise wrong.

A .h or .c file is treated as battle text (trainer slide rows, 208 px, 2 lines) and handed to
design/tools/slide_check.py, for example:
    python3 design/tools/dialogue_check.py src/data/veldris_trainer_slides.h
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HARD_LIMIT = 216   # 27 tiles * 8 px
WARN_LIMIT = 208   # leave a little slack under the hard limit


def load_charmap():
    cm = {}
    for line in (ROOT / "charmap.txt").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^'(\\?.)'\s*=\s*([0-9A-Fa-f]{2})\s*(?:@.*)?$", line)
        if m:
            ch = m.group(1)
            if ch.startswith("\\") and ch[1] in "nlp":
                continue   # '\n' '\l' '\p' are escape codes (charmap.txt), not the letters n, l, p
            cm[ch[1:] if ch.startswith("\\") else ch] = int(m.group(2), 16)
    return cm


def load_widths():
    src = (ROOT / "src" / "fonts.c").read_text(encoding="utf-8")
    m = re.search(r"gFontNormalLatinGlyphWidths\[\]\s*=\s*\{(.*?)\};", src, re.S)
    if not m:
        sys.exit("could not find gFontNormalLatinGlyphWidths in src/fonts.c")
    body = re.sub(r"//.*", "", m.group(1))
    return [int(x) for x in re.findall(r"\b(\d+)\b", body)]


CHARMAP = load_charmap()
WIDTHS = load_widths()
MAX_GLYPH = max(WIDTHS[CHARMAP[c]] for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
PLAYER_W = 7 * MAX_GLYPH          # player names are at most 7 letters
BUFFER_W = 10 * MAX_GLYPH         # {STR_VAR_n}: unknown length, assume 10 wide letters


def line_width(line, problems, where):
    """Return (width, width_if_buffers_are_long). Buffers ({STR_VAR_n}) have unknown length."""
    width = extra = 0
    for tok in re.split(r"(\{[^}]*\})", line):
        if not tok:
            continue
        if tok.startswith("{"):
            name = tok[1:-1].split()[0] if tok[1:-1].split() else ""
            if name == "PLAYER":
                width += PLAYER_W
            elif name == "RIVAL":
                problems.append((where, "{RIVAL} expands to MAY or BRENDAN; write TROGLODYTE"))
            elif name.startswith("STR_VAR"):
                extra += BUFFER_W
            continue
        for ch in tok:
            if ch not in CHARMAP:
                problems.append((where, f"character {ch!r} is not in charmap.txt"))
            else:
                width += WIDTHS[CHARMAP[ch]]
    return width, width + extra


def blocks(path):
    """Yield (label, first_line_number, text) for each label's concatenated .string data."""
    label, start, text = None, 0, ""
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = re.match(r"^(\w+)::?\s*$", raw)
        if m:
            if label and text:
                yield label, start, text
            label, start, text = m.group(1), n, ""
            continue
        m = re.match(r'^\s*\.string "(.*)"\s*(?:@.*)?$', raw)
        if m and label:
            text += m.group(1)
    if label and text:
        yield label, start, text


def check(path, hard, warn):
    problems, warnings, widest = [], [], (0, "")
    for label, start, text in blocks(path):
        where = f"{path}:{start} {label}"
        if '\\"' in text:
            problems.append((where, 'escaped double quote (\\") is a build error'))
            text = text.replace('\\"', "'")      # do not let one bad quote cascade into more errors
        if not text.endswith("$"):
            problems.append((where, "text does not end with $"))
        for page_no, page in enumerate(text.rstrip("$").split("\\p"), 1):
            for line_no, line in enumerate(re.split(r"\\n|\\l", page), 1):
                w, w_buf = line_width(line, problems, where)
                if w > widest[0]:
                    widest = (w, line)
                spot = f"{where} page {page_no} line {line_no}"
                if w > hard:
                    problems.append((spot, f"{w} px is over the {hard} px text box: {line!r}"))
                elif w_buf > hard:
                    warnings.append((spot, f"fits ({w} px) but a long {{STR_VAR}} value could overflow: {line!r}"))
                elif w > warn:
                    warnings.append((spot, f"{w} px is close to the {hard} px limit: {line!r}"))
    return problems, warnings, widest


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--limit", type=int, default=HARD_LIMIT, help="hard limit in px (default 216)")
    ap.add_argument("--warn", type=int, default=WARN_LIMIT, help="warn above this many px (default 208)")
    args = ap.parse_args()
    bad = 0
    for f in args.files:
        if f.suffix in (".h", ".c"):      # battle text: trainer slide rows in C (design/tools/slide_check.py)
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            import slide_check
            bad += slide_check.check_file(str(f))
            continue
        problems, warnings, widest = check(f, args.limit, args.warn)
        for where, msg in problems:
            print(f"ERROR   {where}: {msg}")
        for where, msg in warnings:
            print(f"warning {where}: {msg}")
        print(f"{f}: widest line {widest[0]} px of {args.limit} ({widest[1]!r}); "
              f"{len(problems)} error(s), {len(warnings)} warning(s)")
        bad += len(problems)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
