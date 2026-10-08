#!/usr/bin/env python3
"""Battle-text check for trainer-slide strings (hack tool).

Mirrors the real battle pipeline for a slide string:
  BufferStringBattle -> BattleStringExpandPlaceholders -> BreakStringAutomatic(208 px, 2 lines, scroll prompt)
(src/battle_message.c:2800-2816, 3690; src/line_break.c; include/battle_message.h:14-15)

Usage (from the repo root):
    python3 design/tools/slide_check.py src/data/veldris_trainer_slides.h
    python3 design/tools/dialogue_check.py src/data/veldris_trainer_slides.h      (same thing)

The line-break port was fuzzed against a host-compiled copy of src/line_break.c (86,000 random strings,
0 mismatches). Exit code 1 on any ERROR.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAX_W, MAX_LINES, PROMPT_W = 208, 2, 8
CHAR_SPACE, CHAR_ZWS, CHAR_NBSP = 0x00, 0x3A, 0x39
SCROLL, CLEAR, NEWLINE, CTRL = 0xFA, 0xFB, 0xFE, 0xFC
EOS = 0xFF


def load_tables():
    chars, consts = {}, {}
    for line in (ROOT / "charmap.txt").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^'(\\?.)'\s*=\s*([0-9A-Fa-f]{2})\s*(?:@.*)?$", line)
        if m:
            ch, code = m.group(1), [int(m.group(2), 16)]
            if ch.startswith("\\") and ch[1] in "nlp":
                chars[ch] = code            # escape codes \n \l \p: NOT the letters n, l, p
            elif ch.startswith("\\"):
                chars[ch[1:]] = code        # \' is the apostrophe
            else:
                chars[ch] = code
            continue
        m = re.match(r"^(\w+)\s*=\s*((?:[0-9A-Fa-f]{2}\s*)+)(?:@.*)?$", line)
        if m:
            consts[m.group(1)] = [int(x, 16) for x in m.group(2).split()]
    src = (ROOT / "src" / "fonts.c").read_text(encoding="utf-8")
    m = re.search(r"gFontNormalLatinGlyphWidths\[\]\s*=\s*\{(.*?)\};", src, re.S)
    body = re.sub(r"//.*", "", m.group(1))
    widths = [int(x) for x in re.findall(r"\b(\d+)\b", body)]
    return chars, consts, widths


CHARS, CONSTS, WIDTHS = load_tables()


def glyph_w(b):
    return 0 if b == CHAR_ZWS else WIDTHS[b]


def encode(text, name_letters="W" * 7):
    """C-string text (already unquoted) -> game bytes, expanding {B_PLAYER_NAME} to a sample name."""
    out, i, problems = [], 0, []
    while i < len(text):
        c = text[i]
        if c == "\\":
            esc = text[i:i + 2]
            if esc in ("\\n", "\\l", "\\p"):
                out += CHARS[esc]
            elif esc == "\\\\":
                out += CHARS["\\"] if "\\" in CHARS else []
            else:
                problems.append(f"unknown escape {esc!r}")
            i += 2
        elif c == "{":
            j = text.index("}", i)
            tok = text[i + 1:j]
            if tok == "B_PLAYER_NAME":
                for ch in name_letters:
                    out += CHARS[ch]
            elif tok == "PLAYER":
                problems.append("{PLAYER} is FD 01 = B_TXT_BUFF2 in battle text; use {B_PLAYER_NAME}")
                out += CONSTS["PLAYER"]
            elif tok == "RIVAL":
                problems.append("{RIVAL} expands to MAY or BRENDAN; write TROGLODYTE")
            elif tok in CONSTS:
                out += CONSTS[tok]
            else:
                problems.append(f"unknown token {{{tok}}}")
            i = j + 1
        else:
            if c not in CHARS:
                problems.append(f"character {c!r} is not in charmap.txt")
            else:
                out += CHARS[c]
            i += 1
    return out, problems


def has_manual(b):
    return any(x in (SCROLL, NEWLINE) for x in b)


def break_sub(src, show_prompt=True, max_w=MAX_W, max_lines=MAX_LINES):
    """Python port of BreakSubStringAutomatic (src/line_break.c:187-353) + BuildNewString (411-430).
    Returns (new_bytes, info) where info['empty_line'] marks the planner over-estimate case."""
    src = list(src)
    info = {"empty_line": False, "est_lines": 1, "lines": 1}
    if has_manual(src) or not src:
        return src, info
    split = lambda b: b in (CHAR_ZWS, CHAR_SPACE)
    n_chars, n_words, prev = 1, 1, False
    while n_chars < len(src):
        cur = split(src[n_chars])
        if cur and not prev:
            n_words += 1
        prev = cur
        n_chars += 1
    words = [{"start": 0, "length": 0, "width": 0} for _ in range(n_words)]
    cw, wl, prev = 0, 1, False
    for i in range(1, n_chars):
        cur = split(src[i])
        if cur and not prev:
            words[cw]["length"] = wl
            cw += 1
            wl = 0
        elif (not cur) and prev:
            words[cw]["start"] = i
            words[cw]["width"] = 0
            wl += 1
        else:
            wl += 1
        prev = cur
    words[cw]["length"] = wl
    for w in words:
        w["width"] = sum(glyph_w(src[w["start"] + j]) for j in range(w["length"]))
    space = glyph_w(CHAR_SPACE)
    total = words[0]["width"] + sum(w["width"] + space for w in words[1:])
    if show_prompt:
        total += PROMPT_W
    if total <= max_w:
        return src, info
    cur_w, total_lines = 0, 1
    for idx, w in enumerate(words):
        if show_prompt and idx + 1 == n_words:
            cur_w += PROMPT_W
        if cur_w + w["length"] > max_w:          # sic: compares the byte length, as upstream does
            total_lines += 1
            cur_w = w["width"]
        else:
            cur_w += w["width"] + space
    if cur_w > max_w:
        total_lines += 1
    info["est_lines"] = total_lines
    while True:
        retry = False
        target = (total // total_lines) & 0xFFFF
        lines = [{"first": 0, "n": 0} for _ in range(total_lines)]
        li = 0
        lines[0] = {"first": 0, "n": 1}
        cur_w = words[0]["width"]
        wi = 1
        while wi < n_words:
            over = cur_w + space + words[wi]["width"] + (PROMPT_W if show_prompt else 0) > max_w
            if over or cur_w > target:
                li += 1
                if li == total_lines:
                    total_lines += 1
                    retry = True
                    break
                lines[li] = {"first": wi, "n": 1}
                cur_w = words[wi]["width"]
                wi += 1
            else:
                cur_w += space + words[wi]["width"]
                lines[li]["n"] += 1
                wi += 1
        if not retry:
            break
    info["lines"] = total_lines
    out = src[:]
    idx = 0
    for k in range(total_lines):
        if lines[k]["n"] == 0:
            info["empty_line"] = True
            return src, info
        idx += words[lines[k]["first"]]["length"]
        for j in range(1, lines[k]["n"]):
            idx += words[lines[k]["first"] + j]["length"] + 1
        if k + 1 < total_lines:
            val = SCROLL if (k >= max_lines - 1 and total_lines > max_lines and show_prompt) else NEWLINE
            if idx >= len(out):
                out.append(val)          # real code overwrites the EOS byte (dst was pre-filled with EOS, so it is harmless)
            else:
                out[idx] = val
            idx += 1
    return out, info


def break_string(b, **kw):
    """Port of BreakStringAutomatic: split at \\p (CHAR_PROMPT_CLEAR) and break each page alone."""
    pages, cur = [], []
    for x in b:
        if x == CLEAR:
            pages.append(cur)
            cur = []
        else:
            cur.append(x)
    pages.append(cur)
    out, infos = [], []
    for k, p in enumerate(pages):
        nb, inf = break_sub(p, **kw)
        out += nb
        infos.append(inf)
        if k + 1 < len(pages):
            out.append(CLEAR)
    return out, infos


def drawn_lines(b):
    """Split final bytes into screen lines and measure the drawn width (control codes draw nothing)."""
    lines, cur, w, i = [], [], 0, 0
    while i < len(b):
        x = b[i]
        if x == CTRL:
            i += 2
            continue
        if x in (NEWLINE, SCROLL, CLEAR):
            lines.append((w, x))
            w = 0
        else:
            w += glyph_w(x)
        i += 1
    lines.append((w, None))
    return lines


# ---------- C header parsing ----------
STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def load_ids():
    """Resolve TRAINER_* names to numbers from include/constants/opponents.h (+ PARTNER_* and the TRAINER_PARTNER() macro)."""
    defs = {}
    for f in ("opponents.h", "battle_partner.h"):
        for m in re.finditer(r"^#define\s+((?:TRAINER|PARTNER)_\w+)\s+(\S+)", (ROOT / "include/constants" / f).read_text(encoding="utf-8"), re.M):
            defs[m.group(1)] = m.group(2)
    def val(tok, depth=0):
        if depth > 8:
            return None
        if tok.isdigit():
            return int(tok)
        if tok in defs:
            return val(defs[tok], depth + 1)
        return None
    return defs, val


def slide_names():
    txt = (ROOT / "include/constants/trainer_slide.h").read_text(encoding="utf-8")
    body = txt.split("enum TrainerSlideType")[1].split("};")[0]
    return re.findall(r"TRAINER_SLIDE_([A-Z_]+)", body)


def parse_header(path):
    """Yield (trainer_key, slide_name, text, line_no).

    Token based, so one-line rows work. Understands both row forms:
      [TRAINER_SLIDE_X] = COMPOUND_STRING("a" "b")      (upstream style; text is used as written)
      VELDRIS_SLIDE(X, "a" "b")                          (hack macro; it appends {PAUSE_UNTIL_PRESS})
    """
    raw = Path(path).read_text(encoding="utf-8")
    text = re.sub(r"/\*.*?\*/", lambda m: " " * len(m.group(0)), raw, flags=re.S)
    text = re.sub(r"//[^\n]*", lambda m: " " * len(m.group(0)), text)
    lits = r'((?:\s*"(?:[^"\\]|\\.)*")+)\s*\)'
    trainer_re = re.compile(r"\[(TRAINER_[A-Z0-9_]+(?:\([A-Z0-9_]+\))?)\]\s*=\s*\{")
    row_re = re.compile(r"\[(TRAINER_SLIDE_[A-Z_]+)\]\s*=\s*COMPOUND_STRING\(" + lits + "|VELDRIS_SLIDE\\(\\s*(\\w+)\\s*," + lits)
    events = [(m.start(), "T", m) for m in trainer_re.finditer(text)] + [(m.start(), "S", m) for m in row_re.finditer(text)]
    trainer, block = None, 0
    for pos, kind, m in sorted(events, key=lambda e: e[0]):
        line = text.count("\n", 0, pos) + 1
        if kind == "T":
            trainer, block = m.group(1), block + 1
        elif m.group(1):
            yield trainer, m.group(1), "".join(STR_RE.findall(m.group(2))), line, block
        else:
            yield trainer, "TRAINER_SLIDE_" + m.group(3), "".join(STR_RE.findall(m.group(4))) + "{PAUSE_UNTIL_PRESS}", line, block


def analyse(text):
    res = {"problems": [], "warnings": []}
    results = []
    for label, letters in (("wide name", "W" * 7), ("narrow name", "i" * 7)):
        b, probs = encode(text, letters)
        if label == "wide name":
            res["problems"] += probs
        nb, infos = break_string(b)
        lines = drawn_lines(nb)
        results.append((label, nb, infos, lines))
    worst = results[0]
    for label, nb, infos, lines in results:
        if any(i["empty_line"] for i in infos):
            res["problems"].append(f"{label}: upstream break planner over-estimates the line count (unused line, undefined behaviour in BuildNewString): reword")
        for w, term in lines:
            if w > MAX_W:
                res["problems"].append(f"{label}: a final line is {w} px, over {MAX_W}")
        screens = 1
        n_in_screen = 1
        for w, term in lines[:-1]:
            if term == NEWLINE:
                n_in_screen += 1
            elif term == SCROLL:
                n_in_screen += 1
                screens = max(screens, 99)
        n_lines = len(lines)
        pages = sum(1 for w, t in lines if t == CLEAR) + 1
        scroll = any(t == SCROLL for w, t in lines)
        if scroll:
            res["warnings"].append(f"{label}: needs a scroll (more than {MAX_LINES} lines on one page)")
        if pages > 1:
            res["warnings"].append(f"{label}: {pages} pages")
    res["layout"] = [(r[0], [(w, "\\n" if t == NEWLINE else "\\l" if t == SCROLL else "\\p" if t == CLEAR else "") for w, t in r[3]]) for r in results]
    if not text.rstrip().endswith("{PAUSE_UNTIL_PRESS}"):
        res["warnings"].append("no {PAUSE_UNTIL_PRESS} at the end: the box closes as soon as the text finishes printing")
    if has_manual(encode(text)[0]):
        res["warnings"].append("manual \\n or \\l found: automatic wrapping is OFF for that page, you own the line widths")
    return res


def check_file(path):
    """Print one line per slide string; return the number of errors."""
    bad = 0
    n = 0
    defs, val = load_ids()
    names = set(slide_names())
    seen_keys = {}
    block_of_id, slide_seen = {}, set()
    for trainer, slide, text, ln, block in parse_header(path):
        n += 1
        tid = None
        if trainer:
            m = re.match(r"TRAINER_PARTNER\((\w+)\)", trainer)
            tid = (864 + val(m.group(1))) if m and val(m.group(1)) is not None else val(trainer)
            if tid is None:
                print(f"ERROR {path}:{ln} trainer key {trainer} is not defined in opponents.h"); bad += 1
            elif tid >= 866:
                print(f"ERROR {path}:{ln} trainer id {tid} is outside sTrainerSlides (0..865)"); bad += 1
            else:
                first = block_of_id.setdefault(tid, (block, trainer, ln))
                if first[0] != block:
                    print(f"ERROR {path}:{ln} {trainer} is id {tid}, already keyed as {first[1]} at line {first[2]} (aliases share one id; the compiler rejects the second block: -Werror -Woverride-init)"); bad += 1
                if (block, slide) in slide_seen:
                    print(f"ERROR {path}:{ln} {trainer} {slide} appears twice in one block (build error under -Woverride-init)"); bad += 1
                slide_seen.add((block, slide))
        if slide.replace("TRAINER_SLIDE_", "") not in names:
            print(f"ERROR {path}:{ln} unknown slide {slide}"); bad += 1
        r = analyse(text)
        wide = r["layout"][0][1]
        shape = " | ".join(f"{w}{t}" for w, t in wide)
        flag = "ERROR" if r["problems"] else ("warn " if r["warnings"] else "ok   ")
        print(f"{flag} {path}:{ln} {trainer} {slide}: {shape}")
        for p in r["problems"]:
            print(f"      ERROR {p}")
            bad += 1
        for w in r["warnings"]:
            print(f"      warning {w}")
    print(f"{path}: {n} slide string(s), {bad} error(s)")
    return bad


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(1 if check_file(sys.argv[1]) else 0)


if __name__ == "__main__":
    main()
