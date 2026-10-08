#!/usr/bin/env python3
"""Shared text engine for the Veldris text checkers (hack tool, standard library only).

encode()  turns source text ("Hi {PLAYER}\\n{COLOR RED}x{CLEAR 8}") into game bytes the way tools/preproc does
          (charmap characters, escapes, {CONSTANT 12} groups where a number is a byte).
layout()  walks the bytes the way src/text.c prints them and returns the drawn width of every line:
          RenderText (text.c:1400-1545) for the pen, GetStringWidth (text.c:1819-1990) for the rules.
          Width-changing codes handled: {FONT_x} (switches the glyph table), {CLEAR n} (+n px), {SKIP n} and
          {SHIFT_RIGHT n} (pen = n), {CLEAR_TO n} (pen = max(pen, n)), {MIN_LETTER_SPACING n}, {PKMN},
          {A_BUTTON}-style keypad icons and {UP_ARROW}-style extra symbols. Colour, pause, sound codes draw nothing.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# include/constants/characters.h:176-185
KEYPAD, EXTRA, SCROLL, CLEAR, EXT, PLACEHOLDER, NEWLINE, EOS = 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF
# FC xx -> argument bytes that follow (include/constants/characters.h:212-242; text.c RenderText and GetStringWidth)
EXT_ARGS = {0x01: 1, 0x02: 1, 0x03: 1, 0x04: 3, 0x05: 1, 0x06: 1, 0x07: 0, 0x08: 1, 0x09: 0, 0x0A: 0, 0x0B: 2,
            0x0C: 1, 0x0D: 1, 0x0E: 1, 0x0F: 0, 0x10: 2, 0x11: 1, 0x12: 1, 0x13: 1, 0x14: 1, 0x15: 0, 0x16: 0,
            0x17: 0, 0x18: 0, 0x19: 1, 0x1A: 1, 0x1B: 1, 0x1C: 3}
X_FONT, X_SHIFT_RIGHT, X_CLEAR, X_SKIP, X_CLEAR_TO, X_MIN_SPACING = 0x06, 0x0D, 0x11, 0x12, 0x13, 0x14
# font id (include/text.h:17-31) -> glyph width table in src/fonts.c. 6 (braille) and 9 (bold) have no Latin table.
FONT_TABLE = {0: "Small", 1: "Normal", 2: "Short", 3: "Short", 4: "Short", 5: "Short", 7: "Narrow", 8: "SmallNarrow",
              10: "Narrower", 11: "SmallNarrower", 12: "ShortNarrow", 13: "ShortNarrower"}
FONT_IDS = {"small": 0, "normal": 1, "short": 2, "narrow": 7, "smallnarrow": 8, "narrower": 10,
            "smallnarrower": 11, "shortnarrow": 12, "shortnarrower": 13}
PLAYER_NAME_LENGTH = 7                       # include/constants/global.h:159
P_PLAYER, P_STR_VAR_1, P_STR_VAR_3, P_KUN, P_RIVAL, P_B_PLAYER_NAME = 0x01, 0x02, 0x04, 0x05, 0x06, 0x23


def _load():
    chars, consts = {}, {}
    for line in (ROOT / "charmap.txt").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^'(\\?.)'\s*=\s*((?:[0-9A-Fa-f]{2}\s*)+)(?:@.*)?$", line)
        if m:
            ch = m.group(1)
            # '\n' '\l' '\p' are escape codes and must not overwrite the letters n, l, p
            chars[ch if ch[:1] == "\\" and ch[1] in "nlp" else ch.lstrip("\\")] = [int(x, 16) for x in m.group(2).split()]
            continue
        m = re.match(r"^(\w+)\s*=\s*((?:[0-9A-Fa-f]{2}\s*)+)(?:@.*)?$", line)
        if m:
            consts[m.group(1)] = [int(x, 16) for x in m.group(2).split()]
    src = (ROOT / "src" / "fonts.c").read_text(encoding="utf-8")
    widths = {}
    for m in re.finditer(r"gFont(\w+?)LatinGlyphWidths\[\]\s*=\s*\{(.*?)\};", src, re.S):
        widths[m.group(1)] = [int(x) for x in re.findall(r"\b(\d+)\b", re.sub(r"//.*", "", m.group(2)))]
    text_c = (ROOT / "src" / "text.c").read_text(encoding="utf-8")
    keypad = [int(w) for w in re.findall(r"\[CHAR_\w+_(?:BUTTON|UP|DOWN|LEFT|RIGHT|UPDOWN|LEFTRIGHT|NONE)\]\s*=\s*\{\s*0x[0-9A-Fa-f]+,\s*(\d+),", text_c)]
    return chars, consts, widths, keypad


CHARS, CONSTS, WIDTHS, KEYPAD_W = _load()


def glyph_w(font, b):
    t = FONT_TABLE.get(font)
    return WIDTHS[t][b] if t and b < len(WIDTHS[t]) else 0


def name_w(font):
    """Widest plausible player name: 7 of the widest capitals in this font."""
    return PLAYER_NAME_LENGTH * max(glyph_w(font, CHARS[c][0]) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def encode(text):
    """Source text (quotes already removed) -> (bytes, problems). A '$' is the end-of-string byte, as in .string."""
    out, problems, i = [], [], 0
    while i < len(text):
        c = text[i]
        if c == "\\":
            esc = text[i:i + 2]
            if esc == '\\"':
                problems.append('escaped double quote (\\") has no charmap entry: build error')
            elif esc in CHARS:
                out += CHARS[esc]
            elif esc == "\\\\" and "\\" in CHARS:
                out += CHARS["\\"]
            else:
                problems.append(f"unknown escape {esc!r}")
            i += 2
        elif c == "{":
            j = text.find("}", i)
            if j < 0:
                problems.append("'{' without a closing '}'")
                break
            for w in text[i + 1:j].split():
                if re.fullmatch(r"0[xX][0-9A-Fa-f]+|\d+", w):
                    n = int(w, 0)
                    out += list(n.to_bytes(1 if n < 256 else 2 if n < 65536 else 4, "little"))
                elif w in CONSTS:
                    out += CONSTS[w]
                else:
                    problems.append(f"unknown constant {{{w}}}")
            i = j + 1
        else:
            if c in CHARS:
                out += CHARS[c]
            else:
                problems.append(f"character {c!r} is not in charmap.txt")
            i += 1
    return out, problems


def layout(b, font=1):
    """Bytes -> (pages, problems, warnings).

    pages = [[(width, width_if_buffers_long, terminator), ...], ...]. One entry per drawn line; terminator is
    NEWLINE (\\n), SCROLL (\\l), CLEAR (\\p, which also starts a new page) or None for the last line of the text."""
    pages, cur, problems, warnings = [], [], [], []
    pen = extra = min_w = 0
    i = 0
    while i < len(b) and b[i] != EOS:
        x = b[i]
        if x in (NEWLINE, SCROLL, CLEAR):
            cur.append((pen, pen + extra, x))
            pen = extra = 0
            if x == CLEAR:
                pages.append(cur)
                cur = []
            i += 1
        elif x == EXT:
            code = b[i + 1] if i + 1 < len(b) else 0
            n = EXT_ARGS.get(code)
            if n is None:
                problems.append(f"unknown control code FC {code:02X}")
                n = 0
            a = b[i + 2:i + 2 + n]
            if code == X_FONT:
                font = a[0]
                if font not in FONT_TABLE:
                    problems.append(f"font id {font} has no glyph width table")
            elif code == X_CLEAR:
                pen += a[0]
            elif code in (X_SKIP, X_SHIFT_RIGHT):
                pen = a[0]
            elif code == X_CLEAR_TO:
                pen = max(pen, a[0])
            elif code == X_MIN_SPACING:
                min_w = a[0]
            i += 2 + n
        elif x == PLACEHOLDER:
            pid = b[i + 1] if i + 1 < len(b) else 0
            if pid in (P_PLAYER, P_B_PLAYER_NAME):
                pen += name_w(font)
            elif pid == P_KUN:
                pass                                   # empty in English (src/strings.c:8-9)
            elif pid == P_RIVAL:
                problems.append("{RIVAL} expands to MAY or BRENDAN; write TROGLODYTE")
            else:                                      # {STR_VAR_n}, {DYNAMIC}, team names: length unknown
                extra += 10 * name_w(font) // PLAYER_NAME_LENGTH
            i += 2
        elif x == 0xF7:                                # {DYNAMIC n}: a buffer set at run time
            extra += 10 * name_w(font) // PLAYER_NAME_LENGTH
            i += 2
        elif x in (KEYPAD, EXTRA):
            n = b[i + 1] if i + 1 < len(b) else 0
            w = (KEYPAD_W[n] if n < len(KEYPAD_W) else 8) if x == KEYPAD else glyph_w(font, n | 0x100)
            pen += max(w, min_w)
            i += 2
        else:
            pen += max(glyph_w(font, x), min_w) if min_w else glyph_w(font, x)
            i += 1
    cur.append((pen, pen + extra, None))
    pages.append(cur)
    return pages, problems, warnings
