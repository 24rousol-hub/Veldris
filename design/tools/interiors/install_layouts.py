"""Install the shared interior layouts: write data/layouts/<folder>/map.bin + border.bin and append layouts.json.

    python3 install_layouts.py            # lint everything, then install (re-runnable: a layout with the same id is replaced in place)
    python3 install_layouts.py --check    # lint only
    python3 install_layouts.py --doc      # print the index table and per-layout sections for design/maps/interiors/layouts-built.md

Families are the fam_*.py modules next to this file (each defines SPECS). Run from this folder, or anywhere (paths are repo-relative).
Layouts are installed WITHOUT a map: the author adds each one as a map in Porymap (Layouts tab, right-click, Add New Map with Layout).
"""
import importlib
import json
import sys
from pathlib import Path

import numpy as np

import layoutkit as K
from mrender import V


def families():
    here = Path(__file__).resolve().parent
    sys.path.insert(0, str(here))
    return [importlib.import_module(p.stem) for p in sorted(here.glob("fam_*.py"))]


def install(specs):
    path = V / "data/layouts/layouts.json"
    data = json.load(open(path))
    for s in specs:
        border = s.border or K.default_border(s.primary, s.secondary)
        d = V / "data/layouts" / s.folder
        d.mkdir(exist_ok=True)
        s.grid.astype("<u2").tofile(d / "map.bin")
        (d / "border.bin").write_bytes(np.array(border, "<u2").tobytes())
        entry = {"id": s.layout_id, "name": s.name, "width": s.w, "height": s.h, "primary_tileset": s.primary,
                 "secondary_tileset": s.secondary, "border_filepath": f"data/layouts/{s.folder}/border.bin",
                 "blockdata_filepath": f"data/layouts/{s.folder}/map.bin", "layout_version": "emerald"}
        for i, l in enumerate(data["layouts"]):
            if l["id"] == s.layout_id:
                data["layouts"][i] = entry
                break
        else:
            data["layouts"].append(entry)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


FAMILY_TITLES = {
    "fam_houses": "Shared houses H2, H4, H6",
    "fam_homes": "Character homes, inn, apiary, penthouse",
    "fam_shops": "Cafes, canteen and shop",
    "fam_offices": "Offices, reading room, archive, workshop",
    "fam_halls": "Playhouse, tower room, lounge, champions' hall, shrine hall, casino",
    "fam_gym_briarwick": "Gym 2 Bug: Briarwick",
    "fam_gym_gloomsby": "Gym 3 Ghost: Gloomsby",
    "fam_gym_smeltham": "Gym 4 Steel: Smeltham",
    "fam_gym_hoarfell": "Gym 5 Ice: Hoarfell",
    "fam_gym_gildhaven": "Gym 6 Flying: Gildhaven",
    "fam_gym_hemlock": "Gym 7 Poison: Hemlock Reach",
    "fam_gym_primrose": "Gym 8 Fairy: Primrose Vale",
    "fam_gym_beaconmouth": "Gym 9 Water: Beaconmouth Lighthouse (three floors)",
}


def doc(mods):
    """The markdown body of design/maps/interiors/layouts-built.md (index table plus one section per layout), from the specs."""
    out = ["| Layout id | Size | Tilesets | Exit mat | Used by |", "|---|---|---|---|---|"]
    body = []
    count = 0
    for m in mods:
        specs = m.SPECS
        count += len(specs)
        body.append(f"\n## {FAMILY_TITLES.get(m.__name__, m.__name__)} (`{m.__name__}.py`)\n")
        for s in specs:
            mats = ", ".join(f"({x},{y})" for x, y in s.doors)
            out.append(f"| `{s.layout_id}` | {s.w} x {s.h} | `{s.primary}` + `{s.secondary}` | {mats} | {s.uses} |")
            body.append(f"### `{s.layout_id}`: {s.title}\n")
            body.append(f"{s.w} x {s.h}, `{s.primary}` + `{s.secondary}`, folder `data/layouts/{s.folder}`, exit mat {mats}. "
                        f"Used by: {s.uses}\n")
            body.append(f"{s.notes.strip()}\n")
    return count, "\n".join(out), "\n".join(body)


if __name__ == "__main__":
    mods = families()
    specs = K.collect(*mods)
    errors = K.check_all(specs, verbose="--doc" not in sys.argv)
    if "--doc" in sys.argv:
        n, table, body = doc(mods)
        print(f"{n} layouts\n\n{table}\n{body}")
    elif errors:
        sys.exit(f"{errors} errors, nothing installed")
    elif "--check" not in sys.argv:
        install(specs)
        print(f"installed {len(specs)} layouts")
