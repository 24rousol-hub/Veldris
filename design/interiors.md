# Hollowbrook interiors (player house and Prof. Fennick's lab)

Built 2026-10-01 in a separate Claude thread (branch `gen4-interior-home`), at the author's direction, on the Gen 4 Interior Secondary tileset (credits in `CREDITS.md`). The author reviewed every render. **From here on they are normal maps: edit them in Porymap.**

| Map | Size | What is in it |
|---|---|---|
| `Hollowbrook_PlayersHouse_1F` | 13 x 9 | Kitchen (counter, stove, fridge, stools, trash can), bookshelf, TV with the flower table and two walkable cushions in front, up-staircase in the top-right corner (bottom step `160` is an east arrow warp to 2F), exit mat (2,8). Exit warp still points at `MAP_LITTLEROOT_TOWN` as a placeholder until Hollowbrook exists |
| `Hollowbrook_PlayersHouse_2F` | 13 x 8 | Bed, PC desk (PC, notebook, stool), TV, stairwell going down (tile `183`, entered walking west from (11,2)), rug, plants. PC: sit on the stool (4,3) and face the desk; it flickers on and opens the bedroom PC (engine edits in `engine-edits.md`). Notebook: from (5,3), the adventure rules text |
| `Hollowbrook_ProfFennickLab` | 14 x 12 | Bookshelves and Fennick's PC desk on the back wall, dome research machine (left), instrument cabinet (right), the 4-wide starter table (balls on (5..8,5), the front row is a counter so the player talks across it), two aide desks with stools, plants by the door. The four-starter scene lives in its `scripts.inc` (see `scripts/README.md`). Exits point at Littleroot as a placeholder |

## Tileset notes

- Source layers for Porytiles are in `data/tilesets/secondary/gen4_interior/porytiles_src/` (`bottom/middle/top.png`, `attributes.csv`). Recompile with Porytiles 2.0 (`compile-tileset`), then copy the output in. `tiles.png` must be padded to 128x256 for the `-num_tiles 502` rule in `src/data/tilesets/graphics.h`, and the palette bits in Porytiles' PNG have to be masked off (`& 15`).
- Metatiles added or changed over the artist's sheet (ids are secondary, add 0x200 in map data): fridge 424/428/432/436; PC off screen 421 (406 is the on screen); desk legs and fronts on other floors 422/423 (lab), 439/440 (lab tables), 437/438 (lab shelf bottoms), 441/442 (1F shelf bottoms on green); 30 rebaked onto the green strip; 406/407 cream backdrop replaced by the wall; the staircase's gray fringe (160/168/169) replaced by the floor. 425/426/433/434 are unused armchair rebakes.
- Stale behaviours from the artist's attributes were removed (an armchair slot read as a picture-book shelf, table legs as a vase, a stair tile as a picture-book shelf, a fridge corner as an arrow warp). Bookshelf behaviour added to 437/438/441/442, counter to the starter table front (328-330).
- Tile identities worth knowing: 414 is a **trash can**, not a chair; 168-172, 288-295 and 368-371 are **stair railings**, not shelves; the PC desk is 406/407 over 30/415; the dome machine is 326/327, 334/335, 342/343.
- The 1F staircase uses wall `6` above its left column instead of `144` (144 has half a window cut off at its edge).
