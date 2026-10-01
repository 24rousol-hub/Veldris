#!/usr/bin/env python3
"""Convert a TRIPLE-layer secondary tileset (24 bytes per metatile) to this tree's DUAL-layer
format (16 bytes per metatile). A stand-in for Porytiles, which is not available here.

Usage (from the repo root):
    python3 design/tools/triple2dual.py SRC_DIR OUT_DIR [--primary data/tilesets/primary/building]
    python3 design/tools/triple2dual.py SRC_DIR OUT_DIR --verify-only   # re-check an existing OUT_DIR

SRC_DIR holds tiles.png (indexed), palettes/*.pal (JASC), metatiles.bin (u16 entries: tile id bits
0-9, hflip 10, vflip 11, palette 12-15; 12 entries per metatile: bottom[4], middle[4], top[4], each
in TL, TR, BL, BR order) and metatile_attributes.bin (u16: behaviour bits 0-7).
OUT_DIR gets tiles.png, palettes/00-15.pal, metatiles.bin, metatile_attributes.bin.

What it does, per metatile quadrant (8x8 px):
  * renders bottom and middle with their palettes and composites middle over bottom (index 0 is
    transparent); the top layer stays separate (it is drawn above the player);
  * result: layer 0 = composite (below the player), layer 1 = top. Layer type NORMAL (layer 0 on BG2,
    layer 1 on BG1, see DrawMetatile in src/field_camera.c). If the top layer is empty the type is
    COVERED (both layers below the player, same look);
  * a composited tile with more than 15 colours: if the top layer is empty the metatile is stored
    unmerged (layer 0 = bottom, layer 1 = middle, COVERED), which is lossless. Otherwise the tile is
    quantised to 15 colours (closest pair merged, repeatedly) and reported;
  * colours are cut to the GBA's 15-bit range; tiles are deduped including h/v flips; colour sets
    are packed into palettes 6-12 (15 colours + transparent each). Fails loudly if they do not fit.
Everything is deterministic. Only Pillow is needed.
"""
import argparse, os, random, struct, sys, itertools
from PIL import Image

NUM_PALS_PRIMARY = 6          # include/fieldmap.h
NUM_PALS_TOTAL = 13
SEC_PALS = list(range(NUM_PALS_PRIMARY, NUM_PALS_TOTAL))   # 6..12
TILE_BASE = 512               # NUM_TILES_IN_PRIMARY
NORMAL, COVERED, SPLIT = 0, 1, 2
T = -1                        # transparent pixel


def c15(r, g, b):
    return (r >> 3) | ((g >> 3) << 5) | ((b >> 3) << 10)


def rgb15(c):
    return ((c & 31) << 3 | (c & 31) >> 2, (c >> 5 & 31) << 3 | (c >> 5 & 31) >> 2, (c >> 10 & 31) << 3 | (c >> 10 & 31) >> 2)


def read_pal(path):
    if not os.path.exists(path):      # some sets ship only palettes 00-12: the rest are unused
        return [0] * 16
    lines = open(path).read().split()
    n = int(lines[2])
    vals = list(map(int, lines[3:3 + 3 * n]))
    return [c15(*vals[i * 3:i * 3 + 3]) for i in range(n)]


def load_tiles(png):
    im = Image.open(png)
    assert im.mode == 'P', png
    w, h = im.size
    px = list(im.getdata())
    tiles = []
    for ty in range(h // 8):
        for tx in range(w // 8):
            tiles.append(tuple(px[(ty * 8 + y) * w + tx * 8 + x] for y in range(8) for x in range(8)))
    return tiles


def flip(t, h, v):
    """t is a flat 64 tuple; flips like the GBA: h = mirror x, v = mirror y."""
    rows = [t[y * 8:y * 8 + 8] for y in range(8)]
    if v:
        rows.reverse()
    if h:
        rows = [r[::-1] for r in rows]
    return tuple(itertools.chain(*rows))


class Source:
    def __init__(self, d, primary_dir):
        self.tiles = load_tiles(os.path.join(d, 'tiles.png'))
        self.pals = [read_pal(os.path.join(d, 'palettes', '%02d.pal' % i)) for i in range(16)]
        self.ptiles = load_tiles(os.path.join(primary_dir, 'tiles.png'))
        self.ppals = [read_pal(os.path.join(primary_dir, 'palettes', '%02d.pal' % i)) for i in range(16)]
        raw = open(os.path.join(d, 'metatiles.bin'), 'rb').read()
        assert len(raw) % 24 == 0
        self.ents = struct.unpack('<%dH' % (len(raw) // 2), raw)
        self.n = len(raw) // 24
        raw = open(os.path.join(d, 'metatile_attributes.bin'), 'rb').read()
        self.attrs = struct.unpack('<%dH' % (len(raw) // 2), raw)
        assert len(self.attrs) == self.n
        self.warn = []
        self.primary_refs = set()

    def tile_px(self, e, mt=None):
        """Colour (15-bit) or T for each pixel of an entry, flips applied."""
        t = e & 0x3FF
        if t == 0:
            return (T,) * 64
        if t >= TILE_BASE:
            if t - TILE_BASE >= len(self.tiles):
                self.warn.append('metatile %s: tile %d beyond tiles.png (blank)' % (mt, t))
                return (T,) * 64
            idx, pal = self.tiles[t - TILE_BASE], self.pals[e >> 12]
        else:
            self.primary_refs.add((mt, t, e >> 12))
            idx, pal = self.ptiles[t], self.ppals[e >> 12]
        px = tuple(T if i == 0 else pal[i] for i in idx)
        return flip(px, e >> 10 & 1, e >> 11 & 1)


def blank(t):
    return all(p == T for p in t)


def count_cols(t):
    return len({p for p in t if p != T})


def quantise(t, limit=15):
    """Merge the closest pair of colours (rarer into commoner) until <= limit. Returns (tile, err)."""
    from collections import Counter
    cnt = Counter(p for p in t if p != T)
    cols = dict(cnt)
    m = {c: c for c in cols}
    while len(cols) > limit:
        best = None
        for a, b in itertools.combinations(cols, 2):
            ra, rb = rgb15(a), rgb15(b)
            d = sum((x - y) ** 2 for x, y in zip(ra, rb)) * cols[a] * cols[b] / (cols[a] + cols[b])
            if best is None or d < best[0]:
                best = (d, a, b)
        _, a, b = best
        if cols[a] < cols[b]:
            a, b = b, a            # keep a (commoner), drop b
        cols[a] += cols.pop(b)
        for k, v in m.items():
            if v == b:
                m[k] = a
    out = tuple(T if p == T else m[p] for p in t)
    err = max(max(abs(x - y) for x, y in zip(rgb15(p), rgb15(q))) for p, q in zip(t, out) if p != T)
    return out, err


def composite(bottom, middle):
    return tuple(m if m != T else b for b, m in zip(bottom, middle))


def convert_metatiles(src):
    """-> list of (layers[2][4] of 64-tuples, layer_type) and a report."""
    out, rep = [], dict(quantised=[], split=[], empty=0)
    for mt in range(src.n):
        e = src.ents[mt * 12:mt * 12 + 12]
        lay = [[src.tile_px(e[l * 4 + q], mt) for q in range(4)] for l in range(3)]
        top_empty = all(blank(t) for t in lay[2])
        comp = [composite(lay[0][q], lay[1][q]) for q in range(4)]
        if all(blank(t) for t in comp) and top_empty:
            rep['empty'] += 1
        if top_empty and any(count_cols(c) > 15 for c in comp):
            out.append(([lay[0], lay[1]], COVERED))
            rep['split'].append(mt)
            continue
        for q in range(4):
            if count_cols(comp[q]) > 15:
                before = count_cols(comp[q])
                comp[q], err = quantise(comp[q])
                rep['quantised'].append((mt, q, before, err))
        out.append(([comp, lay[2]], NORMAL if not top_empty else COVERED))
    return out, rep


def canon(t):
    return min(flip(t, h, v) for h in (0, 1) for v in (0, 1))


def pack_palettes(sets, maxpals, tries=4000):
    """sets: list of frozensets of colours (<=15 each). Greedy superset packing with random restarts."""
    sets = [s for s in set(sets) if s]
    maximal = [s for s in sets if not any(s < o for o in sets)]
    best = None
    rng = random.Random(1)
    for attempt in range(tries):
        order = sorted(maximal, key=lambda s: (-len(s), sorted(s)))
        if attempt:
            rng.shuffle(order)
            if attempt % 2:
                order.sort(key=lambda s: -len(s) + rng.random() * 3)
        pals = []
        for s in order:
            bi, bg = None, None
            for i, p in enumerate(pals):
                u = len(p | s)
                if u <= 15:
                    g = (u - len(p), -len(p & s))
                    if bg is None or g < bg:
                        bi, bg = i, g
            if bi is None:
                pals.append(set(s))
            else:
                pals[bi] |= s
        if best is None or len(pals) < len(best):
            best = pals
        if len(best) <= maxpals and attempt >= 50:
            break
    return best


def convert(src_dir, out_dir, primary_dir):
    src = Source(src_dir, primary_dir)
    metas, rep = convert_metatiles(src)
    # dedupe tiles
    canon_ids, tiles = {}, []     # canonical pixel tuple -> id
    inst = []                     # per metatile: list of 8 (id or None, h, v)
    for layers, ltype in metas:
        ents = []
        for layer in layers:
            for t in layer:
                if blank(t):
                    ents.append(None)
                    continue
                c = canon(t)
                if c not in canon_ids:
                    canon_ids[c] = len(tiles)
                    tiles.append(c)
                for h in (0, 1):
                    for v in (0, 1):
                        if flip(c, h, v) == t:
                            break
                    else:
                        continue
                    break
                ents.append((canon_ids[c], h, v))
        inst.append(ents)
    sets = [frozenset(p for p in t if p != T) for t in tiles]
    pals = pack_palettes(sets, len(SEC_PALS))
    if len(pals) > len(SEC_PALS):
        sys.exit('FAIL: colour sets need %d palettes, only %d (6-12) available' % (len(pals), len(SEC_PALS)))
    plist = []
    for p in pals:
        cols = sorted(p, key=lambda c: (sum(rgb15(c)), c))
        plist.append(cols)
    # assign each tile to the first palette containing its colour set
    tpal = []
    for s in sets:
        for i, p in enumerate(pals):
            if s <= p:
                tpal.append(i)
                break
        else:
            sys.exit('FAIL: internal, tile colour set fits no palette')
    # write
    os.makedirs(os.path.join(out_dir, 'palettes'), exist_ok=True)
    n = len(tiles)
    rows = (n + 15) // 16
    img = Image.new('P', (128, rows * 8), 0)
    gray = [248, 0, 248] + [v for i in range(1, 16) for v in (i * 16, i * 16, i * 16)]
    img.putpalette(gray + [0] * (768 - 48))
    for i, t in enumerate(tiles):
        cols = plist[tpal[i]]
        ix = {c: k + 1 for k, c in enumerate(cols)}
        for k, p in enumerate(t):
            img.putpixel(((i % 16) * 8 + k % 8, (i // 16) * 8 + k // 8), 0 if p == T else ix[p])
    img.save(os.path.join(out_dir, 'tiles.png'))

    def wpal(i, cols):
        cols = list(cols) + [0] * (15 - len(cols))
        body = ['248 0 248'] + ['%d %d %d' % rgb15(c) for c in cols]
        open(os.path.join(out_dir, 'palettes', '%02d.pal' % i), 'w', newline='').write(
            'JASC-PAL\r\n0100\r\n16\r\n' + '\r\n'.join(body) + '\r\n')
    for i in range(NUM_PALS_PRIMARY):          # shown by Porymap, unused in game
        wpal(i, [c for c in src.ppals[i][1:]])
        # primary palette 0 colour 0 is not magenta there, keep first line magenta like the Gen 4 set
    for k, i in enumerate(SEC_PALS):
        wpal(i, plist[k] if k < len(plist) else [])
    for i in range(NUM_PALS_TOTAL, 16):
        wpal(i, [])
    mb = bytearray()
    for ents, (layers, ltype) in zip(inst, metas):
        for e in ents:
            if e is None:
                mb += struct.pack('<H', 0)
            else:
                tid, h, v = e
                mb += struct.pack('<H', (TILE_BASE + tid) | h << 10 | v << 11 | (SEC_PALS[tpal[tid]] << 12))
    open(os.path.join(out_dir, 'metatiles.bin'), 'wb').write(mb)
    ab = bytearray()
    for mt, (layers, ltype) in enumerate(metas):
        a = src.attrs[mt]
        if a & 0xFF00:
            rep.setdefault('attr_warn', []).append((mt, a))
        ab += struct.pack('<H', (a & 0xFF) | ltype << 12)
    open(os.path.join(out_dir, 'metatile_attributes.bin'), 'wb').write(ab)
    rep.update(metatiles=src.n, tiles=n, palettes=len(pals), colours=[len(p) for p in plist],
               warn=src.warn, primary_refs=sorted(src.primary_refs))
    return rep


# ------------------------------------------------------------------ verification
def render_src(src, mt):
    """16x16 pixels of the triple-layer metatile, top over middle over bottom; T where empty."""
    img = [T] * 256
    e = src.ents[mt * 12:mt * 12 + 12]
    for l in range(3):
        for q in range(4):
            t = src.tile_px(e[l * 4 + q], mt)
            ox, oy = (q % 2) * 8, (q // 2) * 8
            for k, p in enumerate(t):
                if p != T:
                    img[(oy + k // 8) * 16 + ox + k % 8] = p
    return img


def render_out(out_dir, mt):
    """Read the written files only: 16x16 pixels, layer 1 over layer 0 (the player sits between them
    only for NORMAL, which does not change the flat picture)."""
    return render_out_cached(out_dir)(mt)


_cache = {}


def render_out_cached(out_dir):
    if out_dir in _cache:
        return _cache[out_dir]
    tiles = load_tiles(os.path.join(out_dir, 'tiles.png'))
    pals = [read_pal(os.path.join(out_dir, 'palettes', '%02d.pal' % i)) for i in range(16)]
    ents = struct.unpack('<%dH' % (os.path.getsize(os.path.join(out_dir, 'metatiles.bin')) // 2),
                         open(os.path.join(out_dir, 'metatiles.bin'), 'rb').read())

    def r(mt):
        img = [T] * 256
        for l in range(2):
            for q in range(4):
                e = ents[mt * 8 + l * 4 + q]
                t = e & 0x3FF
                if t == 0:
                    continue
                assert t >= TILE_BASE, 'primary tile %d referenced' % t
                assert e >> 12 in SEC_PALS, 'palette %d outside 6-12' % (e >> 12)
                px = flip(tuple(T if i == 0 else pals[e >> 12][i] for i in tiles[t - TILE_BASE]),
                          e >> 10 & 1, e >> 11 & 1)
                ox, oy = (q % 2) * 8, (q // 2) * 8
                for k, p in enumerate(px):
                    if p != T:
                        img[(oy + k // 8) * 16 + ox + k % 8] = p
        return img
    _cache[out_dir] = r
    return r


def verify(src_dir, out_dir, primary_dir, sheet=None):
    src = Source(src_dir, primary_dir)
    r = render_out_cached(out_dir)
    exact, diff = 0, []
    for mt in range(src.n):
        a, b = render_src(src, mt), r(mt)
        if a == b:
            exact += 1
        else:
            nd = sum(1 for p, q in zip(a, b) if p != q)
            mx = max([max(abs(x - y) for x, y in zip(rgb15(p), rgb15(q))) for p, q in zip(a, b)
                      if p != q and p != T and q != T] or [255 if any((p == T) != (q == T) for p, q in zip(a, b)) else 0])
            diff.append((mt, nd, mx))
    print('verify: %d/%d metatiles pixel-identical to the triple-layer source render; %d differ' %
          (exact, src.n, len(diff)))
    for d in diff[:40]:
        print('   metatile %d: %d px differ, max channel error %d' % d)
    if sheet:
        cols = 16
        rows = (src.n + cols - 1) // cols
        im = Image.new('RGB', (cols * 36, rows * 18 * 1), (255, 0, 255))
        # side by side: source 16x16 | output 16x16 per cell (36 px wide, 2 px gap)
        for mt in range(src.n):
            for side, img in enumerate((render_src(src, mt), r(mt))):
                ox, oy = (mt % cols) * 36 + side * 17, (mt // cols) * 18
                for k, p in enumerate(img):
                    col = (255, 0, 255) if p == T else rgb15(p)
                    im.putpixel((ox + k % 16, oy + k // 16), col)
        im = im.resize((im.width * 2, im.height * 2), Image.NEAREST)
        im.save(sheet)
    return diff


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src')
    ap.add_argument('out')
    ap.add_argument('--primary', default='data/tilesets/primary/building')
    ap.add_argument('--verify-only', action='store_true')
    ap.add_argument('--sheet', help='write a side-by-side comparison PNG (source | output)')
    a = ap.parse_args()
    if not a.verify_only:
        rep = convert(a.src, a.out, a.primary)
        print('metatiles %d, tiles after dedupe %d, palettes used %d (colours %s)' %
              (rep['metatiles'], rep['tiles'], rep['palettes'], rep['colours']))
        print('empty metatiles: %d' % rep['empty'])
        print('stored unmerged (layer0=bottom, layer1=middle, COVERED, lossless): %d %s' %
              (len(rep['split']), rep['split'][:30]))
        print('quantised quadrants: %d' % len(rep['quantised']))
        for q in rep['quantised'][:30]:
            print('   metatile %d quadrant %d: %d colours -> 15, max channel error %d (of 255)' % q)
        if rep['primary_refs']:
            print('references to primary tiles (rendered from the primary and copied): %s' % rep['primary_refs'])
        for w in rep['warn'] + [str(x) for x in rep.get('attr_warn', [])]:
            print('WARN', w)
    verify(a.src, a.out, a.primary, a.sheet)


if __name__ == '__main__':
    main()
