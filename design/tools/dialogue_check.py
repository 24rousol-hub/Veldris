#!/usr/bin/env python3
"""Check game text against its text box, using the game's own glyph widths (hack tool).

Usage (from the repo root):
    python3 design/tools/dialogue_check.py data/maps/Hollowbrook/scripts.inc
    python3 design/tools/dialogue_check.py src/data/items.h              # upstream file: only lines changed since HEAD
    python3 design/tools/dialogue_check.py FILE --staged                  # only lines the staged diff adds (the hook)
    python3 design/tools/dialogue_check.py src/strings.c --box 120x1/narrow   # force one box for every string

What it reads
    .inc   every `.string "..."` block under a label (field box unless the path says otherwise).
    .c .h  every COMPOUND_STRING("...") and _("...") literal, but ONLY in the files listed in PATH_RULES, for a
           string marked `// box: NAME` (same line or the line above), or when --box is given. Any other C file is
           skipped: a C string does not say which box it is printed in.
    src/data/veldris_trainer_slides.h goes to design/tools/slide_check.py (battle box, automatic line breaking).

Boxes (px wide x lines): field 216x2 and intro 216x2 (27 tiles: src/menu.c:81-90, src/main_menu.c:395-405);
    battle 208x2 through the game's own line breaker (src/battle_bg.c:156-163, slide_check.py);
    itemdesc 102x3 (14-tile window is 105 px inside, text starts at x=3: src/item_menu.c:437-444,1048, src/shop.c:287-294,634);
    or `WIDTHxLINES[/font]` for anything else, for example `96x1/narrow`.
Encoding and measuring live in design/tools/textwidth.py: every {CODE} is expanded as tools/preproc does, and the
width-changing ones count ({FONT_NARROW}, {CLEAR n}, {SKIP n}, {SHIFT_RIGHT n}, {CLEAR_TO n}, {MIN_LETTER_SPACING n},
{PKMN}, {A_BUTTON}, {UP_ARROW}...). {PLAYER} is 7 wide capitals; {STR_VAR_n} and {DYNAMIC n} are unknown, so they only warn.

Also an error: a character missing from the charmap, an escaped double quote, {RIVAL}, a .string without its final `$`,
a `$` in the middle, and a field/intro page whose second line break is \\n (a third line needs \\l).
Opt out of one string with `nocheck` in a comment (`@ nocheck` in .inc, `// nocheck` in C) on its label line, one of
its .string lines, or the line above. Exit code 1 if anything is wrong. Standard library only.
A `box: NAME` directive is read only from comments, never from inside a string literal.

--staged judges the STAGED blob (`git show :path`), not the working tree, and only the lines the index adds over HEAD.
While a merge is being concluded (MERGE_HEAD exists) it also drops lines that are identical to the merged branch's, so
taking upstream's text in a conflict does not block the commit; text you wrote by hand in the resolution is still judged.
slide_check (veldris_trainer_slides.h) and wild_lint still read the working tree.
"""
import argparse
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import textwidth as tw

ROOT = Path(__file__).resolve().parents[2]


class Box:
    def __init__(self, width, lines, scroll=True, slack=0, font=1):
        self.width, self.lines, self.scroll, self.slack, self.font = width, lines, scroll, slack, font


BOXES = {
    "field": Box(216, 2, True, 8),       # warn 8 px under the limit (dialogue-style.md: keep lines at 208 or less)
    "intro": Box(216, 2, True, 8),
    "itemdesc": Box(102, 3, False),     # bag/shop description frame: 105 px interior minus the 3 px text origin (upstream test/text.c)
    "battle": None,                      # slide_check.analyse breaks the line itself, like the battle code
}
# (path pattern, box, upstream). First match wins; paths are relative to the repo root. An upstream file also holds
# vanilla text that would not pass, so a plain run checks only the lines changed since HEAD (--all for everything).
PATH_RULES = [
    ("src/data/veldris_trainer_slides.h", "slides", False),
    ("src/data/items.h", "itemdesc", True),
    ("data/text/birch_speech.inc", "intro", False),
    ("data/scripts/veldris_*.inc", "field", False),
    ("data/scripts/*.inc", "field", True),
    ("data/text/*.inc", "field", True),
    ("data/maps/*/scripts.inc", "field", False),
    ("design/dialogue/*.inc", "field", False),
    ("design/scripts/*.inc", "field", False),
]
C_STR = re.compile(r'(?<![A-Za-z0-9_])(?:COMPOUND_STRING|_)\(\s*((?:"(?:[^"\\]|\\.)*"\s*)+)\)')
DIRECTIVE = re.compile(r"\bbox:\s*(\S+)")


def rel(path):
    try:
        return Path(path).resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return Path(path).as_posix()


def rule_for(path):
    r = rel(path)
    for pat, box, upstream in PATH_RULES:
        if fnmatch.fnmatch(r, pat):
            return box, upstream
    return ("field" if path.suffix == ".inc" else None), False


def parse_box(spec):
    if spec in BOXES:
        return BOXES[spec]
    m = re.fullmatch(r"(\d+)x(\d+)(?:/(\w+))?", spec)
    if not m or (m.group(3) and m.group(3) not in tw.FONT_IDS):
        sys.exit(f"unknown box {spec!r}: use field, intro, battle, itemdesc or WIDTHxLINES[/font]")
    return Box(int(m.group(1)), int(m.group(2)), True, 0, tw.FONT_IDS.get(m.group(3), 1))


def _added_lines(path, base):
    """Line numbers (in the new side) that `git diff <base> -U0 -- path` adds. None = git could not say."""
    cmd = ["git", "diff"] + base + ["-U0", "--no-color", "--", str(path)]
    try:
        out = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    lines = set()
    for m in re.finditer(r"^@@ -\S+ \+(\d+)(?:,(\d+))? @@", out, re.M):
        start, n = int(m.group(1)), int(m.group(2) or 1)
        lines.update(range(start, start + n))
    return lines


_merging = None


def merge_in_progress():
    """True while `git commit` is concluding a merge (MERGE_HEAD exists)."""
    global _merging
    if _merging is None:
        try:
            r = subprocess.run(["git", "rev-parse", "-q", "--verify", "MERGE_HEAD"], cwd=ROOT, capture_output=True)
            _merging = r.returncode == 0
        except OSError:
            _merging = False
    return _merging


def changed_lines(path, staged):
    """Line numbers added in the staged diff (staged=True) or changed since HEAD (git diff HEAD). None = unknown.

    Concluding a merge, the staged diff against HEAD holds every line the other side added. Only lines that differ from
    BOTH parents are new in this commit, so staged mode intersects the diff against HEAD with the one against MERGE_HEAD."""
    mine = _added_lines(path, ["--cached"] if staged else ["HEAD"])
    if mine and staged and merge_in_progress():
        theirs = _added_lines(path, ["--cached", "MERGE_HEAD"])
        if theirs is not None:
            return mine & theirs
    return mine


def read_source(path, staged):
    """The text to check: in --staged mode the staged blob (what the commit will contain), else the file on disk."""
    if staged:
        try:
            return subprocess.run(["git", "show", ":" + rel(path)], cwd=ROOT, capture_output=True,
                                  check=True).stdout.decode("utf-8").replace("\r\n", "\n")
        except (OSError, subprocess.CalledProcessError, UnicodeDecodeError):
            pass                                  # untracked, unmerged or outside the repo: the file on disk
    return Path(path).read_text(encoding="utf-8")


def code_view(src, blank_strings):
    """src with the string literals (blank_strings) or the comments (otherwise) blanked to spaces, every offset kept.
    One left-to-right tokenizer, so a stray quote inside a comment, or a // inside a string, cannot pair up wrongly."""
    def blank(m):
        is_string = m.group(0)[0] == '"'
        return re.sub(r"[^\n]", " ", m.group(0)) if is_string == blank_strings else m.group(0)
    return re.sub(r'"(?:[^"\\\n]|\\.)*"|//[^\n]*|/\*.*?\*/', blank, src, flags=re.S)


# ---------- readers: yield (label, first_line, last_line, text, box_name_or_None, nocheck) ----------
def inc_blocks(src):
    label = start = last = box = None
    text, skip, note, cond = "", False, "", False

    def done():
        if not (label and text):
            return None
        if cond:        # .if/.else: the variants sit one after another, each ends in `$`; check them one by one
            return [(label, start, last, t + "$", box, skip) for t in text.split("$") if t]
        return [(label, start, last, text.rstrip("$") + "$" if text.endswith("$") else text, box, skip)]

    for n, raw in enumerate(src.splitlines(), 1):
        m = re.match(r"^(\w+)::?\s*(?:@(.*))?$", raw)
        if m:
            yield from done() or []
            comment = (m.group(2) or "") + " " + note
            label, start, last, text, cond = m.group(1), n, n, "", False
            d = DIRECTIVE.search(comment)
            box, skip, note = (d.group(1) if d else None), "nocheck" in comment, ""
            continue
        m = re.match(r'^\s*\.string "((?:[^"\\]|\\.)*)"\s*(?:@(.*))?$', raw)
        if m and label:
            text += m.group(1)
            last = n
            if m.group(2):
                d = DIRECTIVE.search(m.group(2))
                box = box or (d.group(1) if d else None)
                skip = skip or "nocheck" in m.group(2)
            continue
        if re.match(r"^\s*\.(if|ifdef|ifndef|else|elseif)\b", raw):
            cond = True
        note = raw.split("@", 1)[1] if re.match(r"^\s*@", raw) else ""
    yield from done() or []


def c_strings(src):
    clean = code_view(src, blank_strings=False)    # comments blanked, string literals kept: where the strings are
    rows = code_view(src, blank_strings=True).split("\n")   # string literals blanked, comments kept: where `box:` may be
    for m in C_STR.finditer(clean):
        first, last = clean.count("\n", 0, m.start()) + 1, clean.count("\n", 0, m.end()) + 1
        near = " ".join(rows[max(first - 2, 0):first])
        d = DIRECTIVE.search(near)
        yield (f"line {first}", first, last, "".join(re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(1))),
               d.group(1) if d else None, "nocheck" in near)


# ---------- the check ----------
def check_text(where, text, box, limit, is_inc, problems, warnings):
    """Append to problems/warnings; return (widest_px, where_it_is)."""
    body = text
    if is_inc:
        if not text.endswith("$"):
            problems.append((where, "text does not end with $"))
        else:
            body = text[:-1]
    if "$" in body:
        problems.append((where, "a '$' in the middle ends the string early (the rest is never shown)"))
        body = body.split("$")[0]
    if box is None:                      # battle: the game wraps it; slide_check ports the game's line breaker
        import slide_check
        r = slide_check.analyse(body + "{PAUSE_UNTIL_PRESS}")
        problems += [(where, p) for p in r["problems"]]
        warnings += [(where, w) for w in r["warnings"]]
        return max([w for w, _t in r["layout"][0][1]] or [0]), "battle"
    data, probs = tw.encode(body)
    pages, lprobs, _ = tw.layout(data, box.font)
    problems += [(where, p) for p in probs + lprobs]
    widest = (0, "")
    for pn, page in enumerate(pages, 1):
        for ln, (w, w_long, _term) in enumerate(page, 1):
            spot = f"{where} page {pn} line {ln}"
            if w > widest[0]:
                widest = (w, f"page {pn} line {ln}")
            if w > limit:
                problems.append((spot, f"{w} px is over the {limit} px text box"))
            elif w_long > limit:
                warnings.append((spot, f"fits ({w} px) but a long {{STR_VAR}}/{{DYNAMIC}} value could overflow"))
            elif box.slack and w > limit - box.slack:
                warnings.append((spot, f"{w} px is close to the {limit} px limit"))
        breaks = [t for _w, _wl, t in page if t in (tw.NEWLINE, tw.SCROLL)]
        ends = [t for _w, _wl, t in page if t in (tw.SCROLL, tw.CLEAR)]
        if not box.scroll:
            if len(page) > box.lines or ends:
                problems.append((f"{where} page {pn}", f"has {len(page)} lines/pages; this box shows {box.lines} plain lines and cannot scroll"))
        elif breaks:
            if breaks[0] == tw.SCROLL:
                warnings.append((f"{where} page {pn}", "first line break is \\l (scrolls with one line on screen): use \\n"))
            if tw.NEWLINE in breaks[1:]:
                problems.append((f"{where} page {pn}", f"line {breaks.index(tw.NEWLINE, 1) + 2} would print below the {box.lines}-line box: after the first \\n use \\l"))
    return widest


def check_file(path, forced, limit, staged, everything):
    kind, upstream = rule_for(path)
    kind = forced or kind
    if kind == "slides":
        import slide_check
        return slide_check.check_file(str(path))
    is_inc = path.suffix == ".inc"
    source = read_source(path, staged)   # --staged: the index blob, so the line numbers below match the text
    filtered = staged or (upstream and not everything and not forced)     # judge only the lines the diff touches
    added = None                         # computed on the first string that needs it: most files in a big commit have none
    problems, warnings, widest, n = [], [], (0, ""), 0
    for label, first, last, text, override, skip in (inc_blocks(source) if is_inc else c_strings(source)):
        name = forced or override or kind
        if skip or name is None:
            continue
        if filtered:
            if added is None:
                added = changed_lines(path, staged)
                if added is None:
                    added = set()        # git could not say: check nothing rather than the whole upstream file
            if not added.intersection(range(first, last + 1)):
                continue
        box = parse_box(name)
        lim = limit if (limit and box and box.width == 216) else (box.width if box else 208)
        w = check_text(f"{rel(path)}:{first} {label}", text, box, lim, is_inc, problems, warnings)
        n += 1
        widest = max(widest, (w[0], f"{label} {w[1]}"))
    for where, msg in problems:
        print(f"ERROR   {where}: {msg}")
    for where, msg in warnings:
        print(f"warning {where}: {msg}")
    if n or problems or warnings or not staged:        # a hook run stays quiet about files with no text to check
        scope = " (changed lines only)" if filtered else ""
        print(f"{rel(path)}: {n} string(s) checked{scope}, widest line {widest[0]} px ({widest[1]}); "
              f"{len(problems)} error(s), {len(warnings)} warning(s)")
    return len(problems)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--box", help="force one box for every string: field, intro, battle, itemdesc or WIDTHxLINES[/font]")
    ap.add_argument("--limit", type=int, help="hard limit in px for 216 px boxes (default 216)")
    ap.add_argument("--warn", type=int, help="warn above this many px in 216 px boxes (default 208)")
    ap.add_argument("--staged", action="store_true", help="check only strings on lines the staged diff adds (pre-commit)")
    ap.add_argument("--all", action="store_true", help="check every string, even in upstream files")
    args = ap.parse_args()
    if args.warn:
        BOXES["field"].slack = BOXES["intro"].slack = max(0, 216 - args.warn)
    bad = sum(check_file(f, args.box, args.limit, args.staged, args.all) for f in args.files)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
