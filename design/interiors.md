# Hollowbrook maps (town, player house, Prof. Fennick's lab, neighbour's house)

Built 2026-10-01 in a separate Claude thread (branch `gen4-interior-home`), at the author's direction, on the Gen 4 Interior Secondary tileset (credits in `CREDITS.md`). The author reviewed every render. **From here on they are normal maps: edit them in Porymap.**

| Map | Size | What is in it |
|---|---|---|
| `Hollowbrook_PlayersHouse_1F` | 13 x 9 | Kitchen (counter, stove, fridge, stools, trash can), bookshelf, TV with the flower table and two walkable cushions in front, up-staircase in the top-right corner (bottom step `160` is an east arrow warp to 2F), exit mat (2,8). Exit warps to Hollowbrook |
| `Hollowbrook_PlayersHouse_2F` | 13 x 8 | Bed, PC desk (PC, notebook, stool), TV, stairwell going down (tile `183`, entered walking west from (11,2)), rug, plants. PC: sit on the stool (4,3) and face the desk; it flickers on and opens the bedroom PC (engine edits in `engine-edits.md`). Notebook: from (5,3), the adventure rules text |
| `Hollowbrook` | 32 x 28 | Town exterior on the LeoB ORAS General + Petalburg tilesets, placed per [porymap-walkthrough.md](porymap-walkthrough.md) 6.1: lab top-left (door (13,10)), Goldsworth house top-right (door (22,12), locked: a sign on the door tile, no warp), player's house (door (9,20)) and neighbour's house (door (17,21)) below, pond on the right running off the edge, pale paths, pines all round, exit to Route 1 on the east edge at y9-10 (no connection yet). Signs: town (15,16), lab (8,10), Goldsworth (18,12), player house (11,20). Bench spot for the grandfather: (22,13). Warps: 0 player house, 1 lab, 2 neighbour. Buildings are raw copies of Littleroot's and Oldale's |
| `Hollowbrook_NeighboursHouse` | 11 x 8 | One-floor family house from `Elm's House.png`: stove and fridge on the kitchen floor, window, bookshelf, TV with the flower table and cushions in front, plant, exit mat (2,7) |
| `Hollowbrook_ProfFennickLab` | 14 x 12 | Bookshelves and Fennick's PC desk on the back wall, dome research machine (left), instrument cabinet (right), the 4-wide starter table (balls on (5..8,5), the front row is a counter so the player talks across it), two aide desks with stools, plants by the door. The four-starter scene lives in its `scripts.inc` (see `scripts/README.md`). Exits warp to Hollowbrook |

## Tileset notes

- Source layers for Porytiles are in `data/tilesets/secondary/gen4_interior/porytiles_src/` (`bottom/middle/top.png`, `attributes.csv`). Recompile with Porytiles 2.0 (`compile-tileset`), then copy the output in. `tiles.png` must be padded to 128x256 for the `-num_tiles 502` rule in `src/data/tilesets/graphics.h`, and the palette bits in Porytiles' PNG have to be masked off (`& 15`).
- Metatiles added or changed over the artist's sheet (ids are secondary, add 0x200 in map data): fridge 424/428/432/436; PC off screen 421 (406 is the on screen); desk legs and fronts on other floors 422/423 (lab), 439/440 (lab tables), 437/438 (lab shelf bottoms), 441/442 (1F shelf bottoms on green); 30 rebaked onto the green strip; 406/407 cream backdrop replaced by the wall; the staircase's gray fringe (160/168/169) replaced by the floor. 425/426/433/434 are unused armchair rebakes.
- Stale behaviours from the artist's attributes were removed (an armchair slot read as a picture-book shelf, table legs as a vase, a stair tile as a picture-book shelf, a fridge corner as an arrow warp). Bookshelf behaviour added to 437/438/441/442, counter to the starter table front (328-330).
- Tile identities worth knowing: 414 is a **trash can**, not a chair; 168-172, 288-295 and 368-371 are **stair railings**, not shelves; the PC desk is 406/407 over 30/415; the dome machine is 326/327, 334/335, 342/343.
- The 1F staircase uses wall `6` above its left column instead of `144` (144 has half a window cut off at its edge).

- Hollowbrook is in `gMapGroup_TownsAndRoutes` (`MAP_HOLLOWBROOK`); the interiors are in `gMapGroup_IndoorVeldris` with `MAPSEC_HOLLOWBROOK`.

## Characters and scripts (built 2026-10-01)

The drafts in `design/scripts/hollowbrook_scripts.inc` are now built into each map's `scripts.inc` (those files are the source of truth). Text comes from `design/dialogue/hollowbrook.inc` and `hollowbrook_houses.inc`.

- **Town:** farmer (5,12), wandering kid (20,16), woman hanging laundry (20,20), a wandering Zigzagoon, a Skitty, a Slakoth by the pond, the grandfather on the bench (22,13, appears after the lab scene, two talk topics), and Troglodyte outside the lab (13,13). Signs and the locked Goldsworth door read their texts.
- **Troglodyte's first battle** starts from `MAP_SCRIPT_ON_FRAME_TABLE` when `VAR_HOLLOWBROOK_STATE` is 3, not from a `coord_event`: stepping out of a door is an automatic move and does not fire coord triggers. Win or lose, he walks off and the state becomes 4. Known quirk: after a whiteout before beating him, the battle fires the next time the player enters the town, wherever they enter.
- **Player's house 1F:** Mom (first object, `local_id` 1, which the whiteout heal script needs), the house Zigzagoon, the wake-up trigger, TV, fridge and bookshelf. Mom's 'you have a POKéMON' speech runs once.
- **Neighbour's house:** mother, father, a wandering girl and a Skitty, plus the bookshelf.
- **Fly point and respawn:** `HEAL_LOCATION_HOLLOWBROOK` lands on (9,21) outside the player's door; whiting out sends the player home to Mom (engine edit in `engine-edits.md`). Town `OnTransition` sets `FLAG_VISITED_HOLLOWBROOK` and the respawn. Tested in mGBA with the debug menu's Fly to map.

Not done yet: the new-game start point (still the Littleroot truck), the Route 1 connection, Hollowbrook on the region map picture (the grid cell is set, the art is still Hoenn), and the Goldsworth house interior.
