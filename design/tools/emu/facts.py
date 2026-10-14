"""Facts the tests need that live in the repo's source files (map events, layout sizes, the new-game start tile).

Reading them from the source instead of typing them into the tests means a test does not break just because the author
moved a door in Porymap; it only breaks when the thing it is really about changes.
"""

import json
import re
from pathlib import Path


def map_json(repo, folder):
    """The parsed data/maps/<folder>/map.json."""
    return json.loads((Path(repo) / "data" / "maps" / folder / "map.json").read_text())


def layout_size(repo, layout_id):
    """(width, height) of a layout from data/layouts/layouts.json, in tiles."""
    layouts = json.loads((Path(repo) / "data" / "layouts" / "layouts.json").read_text())["layouts"]
    for lay in layouts:
        if lay.get("id") == layout_id:
            return lay["width"], lay["height"]
    raise KeyError("no layout %s in layouts.json" % layout_id)


def new_game_start(repo):
    """(map constant, x, y) of the Emerald-branch new-game warp in src/new_game.c (WarpToTruck)."""
    text = (Path(repo) / "src" / "new_game.c").read_text()
    body = text[text.index("static void WarpToTruck(void)"):]
    body = body[:body.index("WarpIntoMap();")]
    m = re.findall(r"SetWarpDestination\(MAP_GROUP\((MAP_\w+)\),\s*MAP_NUM\(\1\),\s*WARP_ID_NONE,\s*(\d+),\s*(\d+)\)", body)
    # the first match is the FRLG branch, the last is the Emerald one
    name, x, y = m[-1]
    return name, int(x), int(y)


def opposite(direction):
    return {"U": "D", "D": "U", "L": "R", "R": "L"}[direction]


def wild_land_species(repo, base_label):
    """Species names (SPECIES_...) in the land table `base_label` of src/data/wild_encounters.json, or None if absent."""
    data = json.loads((Path(repo) / "src" / "data" / "wild_encounters.json").read_text())
    for group in data["wild_encounter_groups"]:
        for entry in group["encounters"]:
            if entry["base_label"] == base_label and "land_mons" in entry:
                return {m["species"] for m in entry["land_mons"]["mons"]}
    return None


def script_text(repo, folder, label):
    """The plain text of a `<label>::` .string block in data/maps/<folder>/scripts.inc, with the codes cut out.

    Joins the quoted pieces and turns \\n, \\l and \\p into the same markers Game.message_text() shows. Returns
    None if the label is not there. Placeholders such as {PLAYER} stay as written, so compare only the part before one.
    """
    text = (Path(repo) / "data" / "maps" / folder / "scripts.inc").read_text()
    m = re.search(r"^%s::?\s*\n((?:\s*\.string\s+\".*\"\s*\n)+)" % re.escape(label), text, re.M)
    if not m:
        return None
    parts = re.findall(r'\.string\s+"((?:[^"\\]|\\.)*)"', m.group(1))
    out = "".join(parts)
    return out[:-1] if out.endswith("$") else out


def same_text(shown, source):
    """True if the text the game showed starts with the first part of the source text (up to the first {placeholder}).

    Curly and straight quotes count as equal, and so do the two line-break markers that a single box can use.
    """
    def norm(t):
        for a, b in (("\u2018", "'"), ("\u2019", "'"), ("\u201c", "'"), ("\u201d", "'")):
            t = t.replace(a, b)
        return t
    head = norm(source).split("{")[0]
    return bool(head) and norm(shown).startswith(head)
