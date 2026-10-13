"""Install the shared interior layouts: write data/layouts/<folder>/map.bin + border.bin and append layouts.json.

    python3 install_layouts.py            # lint everything, then install (re-runnable: a layout with the same id is replaced in place)
    python3 install_layouts.py --check    # lint only
    python3 install_layouts.py --doc      # print the markdown table for design/maps/interiors/layouts-built.md

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


def doc(specs):
    rows = ["| Layout id | Size | Tilesets | Exit mat | Used by |", "|---|---|---|---|---|"]
    for s in specs:
        rows.append(f"| `{s.layout_id}` | {s.w} x {s.h} | `{s.primary}` + `{s.secondary}` | "
                    f"{', '.join(f'({x},{y})' for x, y in s.doors)} | {s.uses} |")
    return "\n".join(rows)


if __name__ == "__main__":
    specs = K.collect(*families())
    errors = K.check_all(specs)
    if "--doc" in sys.argv:
        print(doc(specs))
    elif errors:
        sys.exit(f"{errors} errors, nothing installed")
    elif "--check" not in sys.argv:
        install(specs)
        print(f"installed {len(specs)} layouts")
