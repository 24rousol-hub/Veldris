# Furniture that talks (explained, not built)

Status: EXPLAINED 2026-10-08 (author asked what 'furniture tiles speaking' means). **Nothing is built and no engine edit is made** until the author says yes.

## What it is

Press A facing a cabinet, a dresser, a painting, a fridge, a TV or a bookshelf and a short line appears, with no NPC involved. Every map tile carries a hidden label called its **metatile behavior**. When the player presses A on a tile, the game checks that label and, for some labels, runs a stock script.

## What works in this tree today

`GetInteractedMetatileScript` in `src/field_control_avatar.c` is the lookup.

| Works now (Emerald block) | Stock script |
|---|---|
| PC, TV, bookshelf (plain, picture, Pokémon Center), vase, empty trash can, shop shelf, blueprint, region map | `data/scripts/check_furniture.inc`, `tv.inc` |

| Exists in the code but is switched off here (the `IS_FRLG` block) | Stock script |
|---|---|
| Cabinet, dresser, kitchen, painting, computer, food, snacks, video game, burglary, impressive machine, blueprints | `data/scripts/flavor_text.inc` (`EventScript_Cabinet`, `_Dresser`, `_Kitchen`, `_Painting`, `_Computer`, `_Food`, `_Snacks`, `_VideoGame`) |

The constants (`MB_CABINET`, `MB_DRESSER`, `MB_KITCHEN`, `MB_PAINTING`, `MB_COMPUTER`, `MB_FOOD`, `MB_SNACKS`, `MB_TELEPHONE`, `MB_ADVERTISING_POSTER`, `MB_VIDEO_GAME`) all exist in `include/constants/metatile_behaviors.h`.

## What it would take

1. **Engine (small):** move the FRLG lookups out of the `if (IS_FRLG)` block in `GetInteractedMetatileScript` so they also run for Emerald-format maps. One file, about 20 lines; log it in [engine-edits.md](engine-edits.md).
2. **Author, once per tileset, in Porymap:** open the tileset editor (Tileset, Edit Tileset), pick each furniture metatile and set its **Behavior** to the matching `MB_*` value. After that every map using the tileset has talking furniture, with no per-map events. This is the part that is the author's, because tileset files are not hand-edited (rule 2).
3. **Lines:** replace the stock text in `flavor_text.inc` with Veldris and Goldsworth jokes, one line per furniture type, so every cabinet in the game says the same thing (varying it per house needs a normal `bg_event` instead).

## PROPOSED example lines (not canon, each fits 216 px x 2 lines)

- Cabinet: 'The cabinet is full of silver. None of it is for eating.'
- Dresser: 'Fourteen identical waistcoats. He wears them in rotation.'
- Painting: 'A portrait of a Goldsworth. The frame cost more than the face.'
- Kitchen: 'A cook's apron, unused. Someone else does the cooking here.'
- Fridge or food: 'Imported cheese. Labelled in three languages, none of them yours.'
- TV: 'A programme about rich people being ordinary at length.'

(Widths are not yet measured; run `python3 design/tools/dialogue_check.py` on the real file.)

## Alternative with no engine edit

Per-furniture `bg_event` signposts in each map's `map.json` (Porymap's sign tool) with a script of their own. More work per map, but exact, and it can say something different in every house.
