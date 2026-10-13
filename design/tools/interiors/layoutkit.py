"""Kit for the shared interior layout builders (the families live in fam_*.py).

A family module defines `SPECS`, a list of `Spec`. `python3 layoutkit.py fam_houses OUT_DIR` lints every spec and writes
its pictures. `install_layouts.py` collects every family, writes map.bin/border.bin and appends `layouts.json`.

Map block word (little endian u16): bits 0-9 metatile id, bits 10-11 collision, bits 12-15 elevation. Never strip the top
six bits. Primary ids are 0-511, secondary ids are 512 + index. Two classes are normal in an interior:
floor = `F_ | id` (walkable, elevation 3) and solid = `W_ | id` (collision 1, elevation 0).
"""
from __future__ import annotations

import json
import re
import sys
from collections import deque
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from mrender import TS, V, layout as vanilla_layout, render

W_, F_ = 0x0400, 0x3000
GEN4 = ("gTileset_Building", "gTileset_Gen4Interior")
MAX_AREA = 10240  # (w + 15) * (h + 14)


@dataclass
class Spec:
    layout_id: str                      # LAYOUT_VELDRIS_HOUSE_KITCHEN
    folder: str                         # data/layouts/<folder>; the layout name is <folder>_Layout
    grid: np.ndarray                    # H x W uint16 map blocks
    primary: str = GEN4[0]
    secondary: str = GEN4[1]
    doors: tuple = ()                   # exit mat tiles (x, y), the warp goes here; the cell above must be walkable
    npc: tuple = ()                     # tiles an object or the player must be able to stand on and reach
    closed: tuple = ()                  # walkable tiles that may stay unreachable on purpose (shut gates, pits)
    title: str = ""                     # one-line name for the docs
    uses: str = ""                      # which buildings of which cards will use it
    notes: str = ""                     # how it was built, what is left for Porymap
    border: tuple | None = None         # four metatile ids; None = same as a vanilla layout on this tileset pair

    @property
    def w(self) -> int:
        return int(self.grid.shape[1])

    @property
    def h(self) -> int:
        return int(self.grid.shape[0])

    @property
    def name(self) -> str:
        return self.folder + "_Layout"


# ---------------------------------------------------------------- helpers a builder uses

def blank(w: int, h: int, floor: int, wall_top: int | None = None, wall: int | None = None, wall_foot: int | None = None) -> np.ndarray:
    """Floor everywhere; with wall ids, rows 0-2 become the back wall (solid, solid, walkable foot row)."""
    g = np.full((h, w), F_ | floor, np.uint16)
    if wall_top is not None:
        g[0, :] = W_ | wall_top
        g[1, :] = W_ | wall
        g[2, :] = F_ | wall_foot
    return g


def put(g: np.ndarray, x: int, y: int, piece, solid: bool = True) -> None:
    """Stamp a tuple-of-rows piece of metatile ids; solid pieces block, others stay walkable."""
    for dy, row in enumerate(piece):
        for dx, m in enumerate(row):
            g[y + dy, x + dx] = (W_ if solid else F_) | m


def fill(g: np.ndarray, x: int, y: int, w: int, h: int, mid: int, solid: bool = False) -> None:
    g[y:y + h, x:x + w] = (W_ if solid else F_) | mid


def grab(layout_id: str, x: int, y: int, w: int, h: int) -> np.ndarray:
    """Copy a w x h block (collision and elevation bits included) out of any layout in layouts.json."""
    g, _ = vanilla_layout(layout_id)
    return g[y:y + h, x:x + w].copy()


def stamp(g: np.ndarray, x: int, y: int, block: np.ndarray) -> None:
    g[y:y + block.shape[0], x:x + block.shape[1]] = block


def passable(v: int) -> bool:
    return ((int(v) >> 10) & 3) == 0


# ---------------------------------------------------------------- lint

def _tileset_sizes(primary: str, secondary: str) -> tuple[int, int]:
    ts = TS(primary, secondary)
    return len(ts.pm) // 8, len(ts.sm) // 8


def reachable(spec: Spec) -> set[tuple[int, int]]:
    """Walkable cells reachable (4-way) from the cell above each door."""
    g = spec.grid
    seen: set[tuple[int, int]] = set()
    queue: deque[tuple[int, int]] = deque()
    for dx, dy in spec.doors:
        for sx, sy in ((dx, dy), (dx, dy - 1)):
            if 0 <= sy < spec.h and passable(g[sy, sx]) and (sx, sy) not in seen:
                seen.add((sx, sy))
                queue.append((sx, sy))
    while queue:
        x, y = queue.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < spec.w and 0 <= ny < spec.h and (nx, ny) not in seen and passable(g[ny, nx]):
                seen.add((nx, ny))
                queue.append((nx, ny))
    return seen


def lint(spec: Spec) -> tuple[list[str], list[str]]:
    """(errors, warnings). Errors must be fixed before a layout is installed."""
    errors: list[str] = []
    warnings: list[str] = []
    g = spec.grid
    if g.dtype != np.uint16 or g.ndim != 2:
        return [f"grid must be a 2-D uint16 array, got {g.dtype} {g.shape}"], warnings
    if not re.fullmatch(r"LAYOUT_[A-Z0-9_]+", spec.layout_id):
        errors.append(f"bad layout id {spec.layout_id}")
    if not re.fullmatch(r"[A-Za-z0-9_]+", spec.folder):
        errors.append(f"bad folder {spec.folder}")
    if (spec.w + 15) * (spec.h + 14) > MAX_AREA:
        errors.append(f"map too big: ({spec.w}+15)*({spec.h}+14) > {MAX_AREA}")
    try:
        prim_n, sec_n = _tileset_sizes(spec.primary, spec.secondary)
    except Exception as exc:  # unknown tileset name
        return errors + [f"cannot load tilesets {spec.primary}/{spec.secondary}: {exc}"], warnings
    ids = g & 0x3FF
    bad_prim = np.argwhere((ids < 512) & (ids >= prim_n))
    bad_sec = np.argwhere((ids >= 512) & (ids - 512 >= sec_n))
    for y, x in bad_prim[:5]:
        errors.append(f"({x},{y}) primary metatile {ids[y, x]} >= {prim_n} (the primary set has only {prim_n})")
    for y, x in bad_sec[:5]:
        errors.append(f"({x},{y}) secondary metatile {ids[y, x]} >= {512 + sec_n}")
    if len(bad_prim) > 5 or len(bad_sec) > 5:
        errors.append("... more out-of-range metatiles")
    cls = {(int((v >> 10) & 3), int(v >> 12)) for v in g.flatten()}
    odd = cls - {(0, 3), (1, 0)}
    if odd:
        warnings.append(f"unusual collision/elevation pairs (collision, elevation): {sorted(odd)} (normal: floor (0,3), solid (1,0))")
    if not spec.doors:
        errors.append("no exit door listed")
    for dx, dy in spec.doors:
        if not (0 <= dx < spec.w and 0 <= dy < spec.h):
            errors.append(f"door ({dx},{dy}) outside the map")
            continue
        if dy != spec.h - 1:
            warnings.append(f"door ({dx},{dy}) is not on the bottom row")
        if not passable(g[dy, dx]):
            errors.append(f"door ({dx},{dy}) is solid")
        if dy > 0 and not passable(g[dy - 1, dx]):
            errors.append(f"cell above door ({dx},{dy - 1}) is solid")
    seen = reachable(spec)
    closed = set(spec.closed)
    stranded = [(x, y) for y in range(spec.h) for x in range(spec.w)
                if passable(g[y, x]) and (x, y) not in seen and (x, y) not in closed]
    if stranded:
        warnings.append(f"{len(stranded)} walkable tiles cannot be reached from the door, e.g. {stranded[:8]}")
    for x, y in spec.npc:
        if not (0 <= x < spec.w and 0 <= y < spec.h):
            errors.append(f"npc tile ({x},{y}) outside the map")
        elif (x, y) not in seen:
            errors.append(f"npc tile ({x},{y}) is not walkable or not reachable")
    return errors, warnings


def ascii_map(spec: Spec) -> str:
    """'#' solid, '.' reachable floor, ',' walkable but cut off, 'D' door, 'o' reserved object tile, '~' closed on purpose."""
    seen = reachable(spec)
    rows = []
    for y in range(spec.h):
        row = ""
        for x in range(spec.w):
            if (x, y) in set(spec.doors):
                row += "D"
            elif (x, y) in set(spec.npc):
                row += "o"
            elif not passable(spec.grid[y, x]):
                row += "#"
            elif (x, y) in set(spec.closed):
                row += "~"
            elif (x, y) in seen:
                row += "."
            else:
                row += ","
        rows.append(row)
    return "\n".join(rows)


# ---------------------------------------------------------------- pictures

def pictures(spec: Spec, out: Path, scale: int = 3) -> None:
    """<folder>.png (what the player sees), <folder>_ids.png (metatile ids), <folder>_coll.png (red = collision)."""
    out.mkdir(parents=True, exist_ok=True)
    ts = TS(spec.primary, spec.secondary)
    render(spec.grid, ts, scale).save(out / f"{spec.folder}.png")
    render(spec.grid, ts, scale, ids=True).save(out / f"{spec.folder}_ids.png")
    render(spec.grid, ts, scale, coll=True).save(out / f"{spec.folder}_coll.png")
    (out / f"{spec.folder}.txt").write_text(ascii_map(spec) + "\n")


# ---------------------------------------------------------------- install helpers

def default_border(primary: str, secondary: str) -> tuple:
    for l in json.load(open(V / "data/layouts/layouts.json"))["layouts"]:
        if l["primary_tileset"] == primary and l["secondary_tileset"] == secondary and not l["id"].startswith("LAYOUT_VELDRIS"):
            b = np.frombuffer((V / l["border_filepath"]).read_bytes(), "<u2")
            if len(b) == 4:
                return tuple(int(v) for v in b)
    return (1, 1, 1, 1)


def collect(*modules) -> list[Spec]:
    specs: list[Spec] = []
    for m in modules:
        specs.extend(m.SPECS)
    return specs


def check_all(specs: list[Spec], verbose: bool = True) -> int:
    """Lint every spec plus cross-spec rules (unique ids, folders and names). Returns the number of errors."""
    errs = 0
    ids, folders = {}, {}
    existing = {l["id"] for l in json.load(open(V / "data/layouts/layouts.json"))["layouts"]}
    for s in specs:
        e, w = lint(s)
        if s.layout_id in ids:
            e.append(f"duplicate layout id {s.layout_id}")
        if s.folder in folders:
            e.append(f"duplicate folder {s.folder}")
        ids[s.layout_id] = folders[s.folder] = s
        if verbose:
            print(f"{s.layout_id:<44} {s.w:>2}x{s.h:<3} {'REPLACES existing' if s.layout_id in existing else 'new':<17} "
                  f"{len(e)} errors, {len(w)} warnings")
            for m in e:
                print("   ERROR  ", m)
            for m in w:
                print("   warning", m)
        errs += len(e)
    return errs


if __name__ == "__main__":
    import importlib

    mod = importlib.import_module(sys.argv[1])
    out = Path(sys.argv[2])
    specs = collect(mod)
    bad = check_all(specs)
    for s in specs:
        pictures(s, out)
    print(f"{len(specs)} specs, {bad} errors; pictures in {out}")
    sys.exit(1 if bad else 0)
