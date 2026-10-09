# Hollowbrook maps (town, player house, Prof. Fennick's lab, neighbour's house)

Built 2026-10-01 in a separate Claude thread (branch `gen4-interior-home`), at the author's direction, on the Gen 4 Interior Secondary tileset (credits in `CREDITS.md`). The author reviewed every render. **From here on they are normal maps: edit them in Porymap.**

| Map | Size | What is in it |
|---|---|---|
| `Hollowbrook_PlayersHouse_1F` | 13 x 9 | Kitchen (counter, stove, fridge, stools, trash can), bookshelf, TV with the flower table and two walkable cushions in front, up-staircase in the top-right corner (bottom step `160` is an east arrow warp to 2F), exit mat (2,8). Exit warps to Hollowbrook |
| `Hollowbrook_PlayersHouse_2F` | 13 x 8 | Bed, PC desk (PC, notebook, stool), TV, stairwell going down (tile `183`, entered walking west from (11,2)), rug, plants. PC: sit on the stool (4,3) and face the desk; it flickers on and opens the bedroom PC (engine edits in `engine-edits.md`). Notebook: from (5,3), the adventure rules text |
| `Hollowbrook` | 32 x 28 | **LeoB ORAS** General + Petalburg (author 2026-10-01; a Gen 4 repaint was tried the same day and dropped). Same plan and doors: lab top-left (door (13,10)), Goldsworth house top-right (door (22,12), locked: a sign on the door tile, no warp), player's house (door (9,20)) and neighbour's house (door (17,21)) below, pond (rows 12-16) on the right running off the edge, pale paths, pine forest all round, 3-row exit path on the east edge at y9-11 joining Route 1. The player's and Goldsworth houses are New Bark Town's house mirrored so their doors stay put; the lab is New Bark Town's lab one tile right of the old one. Signs: town (15,16), lab (8,10), Goldsworth (18,12), player house (11,20). Bench spot for the grandfather: (22,13). Warps: 0 player house, 1 lab, 2 neighbour. Doors are non-animated (walk onto them) |
| `Hollowbrook_NeighboursHouse` | 11 x 8 | One-floor family house from `Elm's House.png`: stove and fridge on the kitchen floor, window, bookshelf, TV with the flower table and cushions in front, plant, exit mat (2,7) |
| `Hollowbrook_ProfFennickLab` | 14 x 12 | Bookshelves and Fennick's PC desk on the back wall, dome research machine (left), instrument cabinet (right), the 4-wide starter table (balls on (5..8,5), the front row is a counter so the player talks across it), two aide desks with stools, plants by the door. The four-starter scene lives in its `scripts.inc` (see `scripts/README.md`). Exits warp to Hollowbrook |

## Tileset notes

- Source layers for Porytiles are in `data/tilesets/secondary/gen4_interior/porytiles_src/` (`bottom/middle/top.png`, `attributes.csv`). Recompile with Porytiles 2.0 (`compile-tileset`), then copy the output in. `tiles.png` must be padded to 128x256 for the `-num_tiles 502` rule in `src/data/tilesets/graphics.h`, and the palette bits in Porytiles' PNG have to be masked off (`& 15`).
- Metatiles added or changed over the artist's sheet (ids are secondary, add 0x200 in map data): fridge 424/428/432/436; PC off screen 421 (406 is the on screen); desk legs and fronts on other floors 422/423 (lab), 439/440 (lab tables), 437/438 (lab shelf bottoms), 441/442 (1F shelf bottoms on green); 30 rebaked onto the green strip; 406/407 cream backdrop replaced by the wall; the staircase's gray fringe (160/168/169) replaced by the floor. 425/426/433/434 are unused armchair rebakes.
- Stale behaviours from the artist's attributes were removed (an armchair slot read as a picture-book shelf, table legs as a vase, a stair tile as a picture-book shelf, a fridge corner as an arrow warp). Bookshelf behaviour added to 437/438/441/442, counter to the starter table front (328-330).
- Tile identities worth knowing: 414 is a **trash can**, not a chair; 168-172, 288-295 and 368-371 are **stair railings**, not shelves; the PC desk is 406/407 over 30/415; the dome machine is 326/327, 334/335, 342/343.
- **Furniture behaviours (2026-10-09):** talking furniture is wired (see [furniture-lines.md](furniture-lines.md)), but this tileset carries none of those behaviours yet; the author sets them in Porymap (fridge `MB_FOOD`, stove `MB_KITCHEN` and so on). A Porytiles recompile needs the same rows in `attributes.csv`, or they are lost.
- The 1F staircase uses wall `6` above its left column instead of `144` (144 has half a window cut off at its edge).

- Hollowbrook is in `gMapGroup_TownsAndRoutes` (`MAP_HOLLOWBROOK`); the interiors are in `gMapGroup_IndoorVeldris` with `MAPSEC_HOLLOWBROOK`.

## Characters and scripts (built 2026-10-01)

The drafts in `design/scripts/hollowbrook_scripts.inc` are now built into each map's `scripts.inc` (those files are the source of truth). Text comes from `design/dialogue/hollowbrook.inc` and `hollowbrook_houses.inc`.

- **Town:** farmer (5,12), wandering kid (20,16), woman hanging laundry (20,20), a wandering Zigzagoon, a Skitty, a Slakoth by the pond, the grandfather on the bench (22,13, appears after the lab scene, two talk topics), and Troglodyte outside the lab (13,13). Signs and the locked Goldsworth door read their texts.
- **Troglodyte's first battle** starts from `MAP_SCRIPT_ON_FRAME_TABLE` when `VAR_HOLLOWBROOK_STATE` is 3, not from a `coord_event`: stepping out of a door is an automatic move and does not fire coord triggers. Win or lose, he walks off and the state becomes 4. Known quirk: after a whiteout before beating him, the battle fires the next time the player enters the town, wherever they enter.
- **Player's house 1F:** Mom (first object, `local_id` 1, which the whiteout heal script needs), the house Zigzagoon, the wake-up trigger, TV, fridge and bookshelf. Mom's 'you have a POKéMON' speech runs once.
- **Neighbour's house:** mother, father, a wandering girl and a Skitty, plus the bookshelf.
- **Fly point and respawn:** `HEAL_LOCATION_HOLLOWBROOK` lands on (9,21) outside the player's door; whiting out sends the player home to Mom (engine edit in `engine-edits.md`). Town `OnTransition` sets `FLAG_VISITED_HOLLOWBROOK` and the respawn. Tested in mGBA with the debug menu's Fly to map.

- **New game:** starts in the bedroom at the foot of the bed (2,4), no truck. Going downstairs fires Mom's wake-up (engine edits in `engine-edits.md`).

Not done yet: Hollowbrook on the region map picture (the grid cell is set, the art is still Hoenn), and the Goldsworth house interior.

## After-badge lines wired (2026-10-01, merged branch)

The 11 'after the first badge' lines from `design/dialogue/hollowbrook.inc` and `hollowbrook_houses.inc` are now in the map scripts, switched on `FLAG_BADGE01_GET` (no new flag): town sign, farmer (plus the empty-bench remark `BenchOldManAfterBadge`, spoken by the farmer because the bench has no separate old man), kid, laundry woman; Mom and the TV in the player's house; the neighbour, her husband, the kid and the Skitty next door; the two aides and Fennick in the lab. Builds; **not yet played** (an emulator check was attempted but the debug warp menu did not open the map). Still unwired: the League-day grandfather lines (the Goldsworth house interior is not built), `BenchOldMan` (a separate old man was never placed), and `TrogOutsideIntro`.

## Gen 4 outdoor tiles (tried and dropped, 2026-10-01)

Hollowbrook and Route 1 were repainted in Gen 4 tiles cut from Palladium's pictures, then the author chose to stay with **LeoB ORAS** for every exterior. The Gen 4 tilesets were removed from the build; they are in git history (commit `a00ee004`) and the tools are in `design/tools/gen4_tiles/`. Route 1 is now built in LeoB by `design/tools/gen4_tiles/route1_leob.py` (same layout, vanilla Route 102 pieces).
