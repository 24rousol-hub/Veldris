# Imported interior tilesets (Team Aqua repo, triple-layer to dual-layer)

> **Status note (author, 2026-10-01):** the converter (`design/tools/triple2dual.py`) is parked. The author is doing tileset conversion with Porytiles in a separate chat that is making maps. The four sets below were already converted with it and are in the tree. If the Porytiles chat imports the same sets, **keep only one copy**: a second `gTileset_ZeldaHouse`, `gTileset_LittleOffice`, `gTileset_GatePlatinum` or `gTileset_BrickCafe` breaks the build. Porytiles output wins; remove the converter version (its folder, its blocks in `src/data/tilesets/`, `include/tilesets.h`, and its `CREDITS.md` and `engine-edits.md` rows) before adding the other.


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


## Little Office (`gTileset_LittleOffice`, `data/tilesets/secondary/little_office/`)

Source: Little Office Interior Secondary (Ekat99's "Little Office" tileset, imported to pokeemerald by Kumatora).

- **120 metatile slots, 68 filled.** 129 tiles after dedupe. **Palettes 6 to 9** used, 10 to 12 free.
- Gives a bright office or shop interior in Gen 3 style: cream walls with window panes and a gabled-roof facade, light wood plank floors, desks with monitors and office chairs, counters with green-trimmed panels, shelves with files, an orange carpet strip, glass walls and a glass door pane, potted plants, a reception-style counter with a round emblem.
- Behaviours: none set (every metatile is `MB_NORMAL`). **Add doors, warps and collision in Porymap; the source ships no warp metatiles.** Layer type: 3 NORMAL, 117 COVERED.
- Converter notes: no quantisation, no unmerged metatiles, 0 of 120 differ from the source render.


## Gate Platinum (`gTileset_GatePlatinum`, `data/tilesets/secondary/gate_platinum/`)

Source: Gate Platinum Secondary (blloop, redrawn from Platinum gameplay screenshots).

- **128 metatile slots, 52 filled** (ids 0 to 59). 73 tiles after dedupe. **Palettes 6 to 10** used, 11 and 12 free.
- Gives the Sinnoh route-gate interior: slate and grey-blue floor tiles, a beige wall with window panes and an orange counter or rail, a white-and-grey bench or stair edge, potted shrubs, railings and a dark exit area with grey stair railings.
- Behaviours: metatile 44 `MB_WEST_ARROW_WARP`, 45 `MB_EAST_ARROW_WARP`, 52 `MB_NORTH_ARROW_WARP`, 53 `MB_SOUTH_ARROW_WARP`. Layer type: 11 NORMAL, 117 COVERED.
- Converter notes: no quantisation, no unmerged metatiles, 0 of 128 differ from the source render. The source calls itself a Platinum redraw, so the art derives from GAME FREAK's.


## Brick Cafe (`gTileset_BrickCafe`, `data/tilesets/secondary/brick_cafe/`)

Source: Brick Cafe Interior Secondary (Ekat99's "Brick Cafe" tileset; FRLG rips by Vurtax, RSE rips by Heartlessdragoon; imported to pokeemerald by Kumatora).

- **512 metatile slots, 282 filled** (ids 0 to 303 with gaps). 353 tiles after dedupe. **All seven palettes, 6 to 12, are used** (15, 15, 15, 15, 15, 14 and 13 colours), so this set has no spare palette room: do not add tiles with new colours without re-running the converter.
- Gives a brick cafe: red-brick walls with arched windows, grey checkerboard and plank floors, wooden counters with stools, coffee cups, cake stands and bowls, kitchen shelving, stairs, green chairs and armchairs round tables, blue carpets, plants, a wall lantern, roof-beam trims and doors.
- Behaviours: metatiles 3 and 4 `MB_SOUTH_ARROW_WARP`, 118 and 119 `MB_TRASH_CAN`, 290 `MB_NON_ANIMATED_DOOR`. Layer type: 75 NORMAL, 437 COVERED.
- Converter notes: no quantisation, no unmerged metatiles, 0 of 512 differ from the source render. **Metatiles 282 and 290 reference four primary-tileset tiles (490, 491, 506, 507, palette 2)** in the source, which assumed a primary with a wall lantern. They were rendered from this tree's `gTileset_Building` and copied into the secondary, so the set does not depend on the primary (checked by eye: a lantern on brick). If the set is ever used with a different primary, nothing changes.
