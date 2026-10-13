"""Metatile atlas for any primary/secondary tileset pair, so a layout can be built from pieces that exist.

    python3 atlas.py gTileset_Building gTileset_Gen4Interior OUT_DIR [scale]

Writes OUT_DIR/primary_N.png and secondary_N.png (16 x 16 metatiles per page, the metatile id in yellow, a non-zero
behaviour in cyan) and OUT_DIR/behaviours.txt (id -> behaviour name for every non-zero behaviour).
Ids are the ids a map block holds: primary 0-511, secondary 512 + index (so the first secondary tile is 512).
"""
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

from mrender import TS, V

COLS, ROWS = 16, 16


def behaviour_names():
    names = {}
    for line in (V / "include/constants/metatile_behaviors.h").read_text().splitlines():
        m = re.match(r"#define (MB_\w+)\s+(0x[0-9A-Fa-f]+|\d+)", line)
        if m:
            names.setdefault(int(m.group(2), 0), m.group(1))
    return names


def attributes(tsdir):
    f = Path(tsdir) / "metatile_attributes.bin"
    return np.frombuffer(f.read_bytes(), "<u2") if f.exists() else np.zeros(0, np.uint16)


def page(ts, first, count, attrs, scale, ids_offset):
    im = Image.new("RGB", (COLS * 16 * scale, ROWS * 16 * scale), (40, 40, 48))
    d = ImageDraw.Draw(im)
    for i in range(min(count - first, COLS * ROWS)):
        idx = first + i
        x, y = (i % COLS) * 16 * scale, (i // COLS) * 16 * scale
        tile = Image.fromarray(ts.meta(idx + ids_offset)).resize((16 * scale, 16 * scale), Image.NEAREST)
        im.paste(tile, (x, y))
        d.rectangle([x, y, x + 16 * scale - 1, y + 16 * scale - 1], outline=(70, 70, 90))
        d.text((x + 2, y + 1), str(idx + ids_offset), fill=(0, 0, 0))
        d.text((x + 1, y), str(idx + ids_offset), fill=(255, 255, 0))
        if idx < len(attrs) and (int(attrs[idx]) & 0xFF):
            d.text((x + 2, y + 16 * scale - 11), f"b{int(attrs[idx]) & 0xFF}", fill=(0, 255, 255))
    return im


def main(prim, sec, out, scale=3):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    ts = TS(prim, sec)
    names = behaviour_names()
    lines = []
    for label, tsdir, count, offset in (("primary", ts.pd, len(ts.pm) // 8, 0), ("secondary", ts.sd, len(ts.sm) // 8, 512)):
        attrs = attributes(tsdir)
        for n, first in enumerate(range(0, count, COLS * ROWS)):
            page(ts, first, count, attrs, scale, offset).save(out / f"{label}_{n}.png")
        for idx, a in enumerate(attrs):
            if int(a) & 0xFF:
                lines.append(f"{label} {idx + offset}: {names.get(int(a) & 0xFF, int(a) & 0xFF)}")
        print(f"{label}: {count} metatiles, {(count + COLS * ROWS - 1) // (COLS * ROWS)} page(s)")
    (out / "behaviours.txt").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 3)
