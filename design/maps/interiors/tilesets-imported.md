# Imported interior tilesets (Team Aqua repo, triple-layer to dual-layer)

Status: built, `make -j4` passes, not yet used by any map (2026-10-01). Source: the Team Aqua repo's `Tilesets/The Great Tileset Exchange/Full Tilesets/`. Where each set is meant to be used: [catalogue.md](catalogue.md), [README.md](README.md).

## How they were converted

These sets are **triple-layer** (12 entries per metatile: bottom, middle, top). This tree is **dual-layer** (8 entries). Porytiles is not available here, so `design/tools/triple2dual.py` does the job (run it from the repo root: `python3 design/tools/triple2dual.py <source folder> <output folder>`; it also re-renders and verifies, `--sheet out.png` writes a source | output comparison picture).

- Per 8x8 quadrant the middle layer is composited over the bottom (colour index 0 is transparent) into **layer 0**; the **top** layer stays as **layer 1**, drawn above the player. Layer type is NORMAL when the top layer has anything in it, otherwise COVERED (both layers below the player, same picture). Behaviour bits are copied unchanged.
- Colours are cut to the GBA's 15 bits, tiles are deduplicated including flips, and the colour sets are packed into **secondary palettes 6 to 12** (the primary `gTileset_Building` owns 0 to 5; 13 to 15 are not available). Palette files 00 to 05 are copies of the Building ones for Porymap's display only. A composite tile with more than 15 colours would be stored unmerged (bottom and middle as two below-player layers) if its top is empty, else quantised to 15 and reported; **no tile in any of the four sets needed either**.
- Metatile ids are kept exactly as in the source (blank metatiles stay blank), so the source's `example.png` can be rebuilt id for id.
- Every output metatile was re-rendered from the written files and compared pixel by pixel with the triple-layer source render: **all metatiles are identical in all four sets**. Side-by-side sheets were also looked at against each set's `example.png`.
- **Not tested in game or in Porymap yet.** The converter's layer order and the dual-layer draw order come from `DrawMetatile` in `src/field_camera.c`.

Caveats that apply to all sets: tiles.png is padded to a multiple of 16 tiles (the gfx rule `-num_tiles N -Wnum_tiles` uses the real count); the PNG palette is a placeholder grey ramp, Porymap shows the colours from `palettes/*.pal`; behaviour values above 8 bits are not supported by this tree (none occur).


## Zelda House (`gTileset_ZeldaHouse`, `data/tilesets/secondary/zelda_house/`)

Source: Legend of Zelda House Secondary (Hek-el-grande buildings, assembled by Yumekua, reformat by Rahtak, many creators in the folder's `credits.md`).

- **512 metatile slots, 82 filled** (ids 0 to 95 with gaps). 133 tiles after dedupe (source art was 512 tile slots). **Palettes 6 to 9** used, 10 to 12 free.
- Gives a stone and timber rustic home: pink stone floor, cream plaster wall with brick base, wooden plank hall runner, wall and corner trims, two beds (white), stove and fireplace with a cooking pot, shelf with bowls, chest, clay pots, grey bottles, tree-stump stools, a lattice window and a wide wooden table, a sword on the wall, a green mat.
- Behaviours: metatiles 8 and 9 `MB_SOUTH_ARROW_WARP` (the mat), 14 and 15 `MB_VASE`.
- Converter notes: no quantisation, no unmerged metatiles, 0 of 512 differ from the source render. Layer type: 16 NORMAL, 496 COVERED (mostly the blank slots).
