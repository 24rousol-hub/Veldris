# Furniture that talks

Status: **BUILT 2026-10-09** (author: 'turn on the talking furniture stuff'). 17 furniture behaviours now speak on Emerald-format maps through one hack-owned lookup (`src/veldris_furniture.c`) called from `GetInteractedMetatileScript`; the lines live in `data/scripts/veldris_furniture.inc`. **Nothing speaks yet:** no tile in any compiled tileset carries these behaviours (scanned: 18,859 metatile entries in 76 tilesets, 0 hits), so the author has to set a **Behavior** on furniture metatiles in Porymap (guide below). All 17 lines are **PROPOSED**. No flag or var is used. Author's direction: 'lines here and there, not everything needs details or lines, but a lot does in order to fill out the game'.

## What it is

Press A facing a cabinet, a dresser, a painting, a fridge or a bookshelf and a short line appears, with no NPC involved. Every map tile carries a hidden label called its **metatile behavior**. When the player presses A on a tile, the game checks that label and, for some labels, runs a script. Setting the label once on a metatile makes every piece of that furniture, in every map that uses the tileset, say the same line.

## Two ways to give furniture a line

| | General (behaviour) | Specific (sign) |
|---|---|---|
| Who does it | The author, in Porymap's tileset editor, once per tileset | Claude (or the author in Porymap's Events tab), one per spot |
| Text | One line per furniture **type**, the same in every house | Any text per spot; can depend on flags |
| Use it for | Filling out the game fast; every cabinet, fridge and painting talks | Goldsworth rooms, gym leaders' homes, story objects, jokes |
| Priority | Used when nothing else is on the tile | **Beats** the general line (use facing 'any') |

Recommended: both. The general lines are written in a neutral small-village voice, so they fit any house; a rich or story-specific room should override with a sign.

## What works today

| Behaviour | Stock script | State |
|---|---|---|
| Bookshelf, picture book shelf, Pokémon Center bookshelf, vase, trash can, shop shelf, blueprint, PC | `data/scripts/check_furniture.inc` and others (Emerald block, always compiled) | **Already talks** where a tileset carries the behaviour. The Gen 4 Interior secondary has bookshelf x9 and trash can x1 (the lab bookshelf says 'It's filled with all sorts of books.'), `gTileset_Building` has TV x2 and PC x2, the Shop tileset has shop shelf x18 |
| Cabinet, kitchen, dresser, snacks, food, painting, computer, telephone, advertising poster, video game, impressive machine, blueprints, power plant machine, tasty food, cup, blinking lights, neatly lined up tools | Hack-owned `Veldris_EventScript_Furniture_*` in `data/scripts/veldris_furniture.inc` | **BUILT, waiting for Porymap behaviours** |
| Burglary, Trainer Tower monitor, Cable Club monitor, battle records, Indigo Plateau signs | Stock FRLG scripts | Left off on purpose (FRLG story or features) |

The stock FRLG lines (`data/scripts/flavor_text.inc`) are **not** used: that file is only assembled when building FireRed or LeafGreen, so moving the C lookups out of `if (IS_FRLG)` would have failed at link time. The hack has its own scripts and its own text instead.

## What was built

| Piece | Where |
|---|---|
| 17-row table, behaviour to script, plus a lookup | `src/veldris_furniture.c`, `include/veldris_furniture.h` (hack-owned) |
| 17 scripts and their text | `data/scripts/veldris_furniture.inc` (hack-owned), included once from `data/event_scripts.s` |
| Hook | `src/field_control_avatar.c`: one `#include`, one local variable and a 3-line lookup just before the `if (IS_FRLG)` block of `GetInteractedMetatileScript`. Nothing was moved or deleted |

To add or drop a furniture type later: one table row in `src/veldris_furniture.c` and one script in the `.inc`.

## The 17 lines (PROPOSED, each 2 lines, widest 186 px)

| Furniture (behaviour) | Line |
|---|---|
| Cabinet (`MB_CABINET`) | The plates all match. Somebody here does not trust surprises. |
| Kitchen: stove, sink, counter (`MB_KITCHEN`) | Something is simmering. It smells of patience and one onion. |
| Dresser, wardrobe (`MB_DRESSER`) | Folded clothes. One sleeve has been mended so well it looks proud. |
| Snacks (`MB_SNACKS`) | A bowl of snacks. They have been counted. You can tell. |
| Food, fridge, pot (`MB_FOOD`) | A pot, a loaf and a lot of hope. It smells better than it looks. |
| Painting (`MB_PAINTING`) | A painting of a POKéMON. The artist clearly loved it. Or was paid to. |
| Computer (`MB_COMPUTER`) | A computer. The screen says it is thinking. It has said so for hours. |
| Telephone (`MB_TELEPHONE`) | A telephone. It rings so rarely that it sounds like an accident. |
| Advertising poster (`MB_ADVERTISING_POSTER`) | A poster for a tonic that cures every ailment. Read the small print. |
| Video game (`MB_VIDEO_GAME`) | A game console. Someone has been losing on it with great dignity. |
| Impressive machine (`MB_IMPRESSIVE_MACHINE`) | A machine, humming with total confidence. You do not touch it. |
| Blueprints (`MB_BLUEPRINTS`) | Plans for something very large. The margins are full of tea rings. |
| Power plant machine (`MB_POWER_PLANT_MACHINE`) | A big machine. The sign says DO NOT TOUCH. Under it: 'Too late.' |
| Tasty food (`MB_FOOD_SMELLS_TASTY`) | Something smells wonderful. Your stomach files a formal complaint. |
| Cup (`MB_CUP`) | A chipped cup. It has seen things and is still in daily use. |
| Blinking lights (`MB_BLINKING_LIGHTS`) | Little lights blink on and off. You feel very slightly watched. |
| Neatly lined up tools (`MB_NEATLY_LINED_UP_TOOLS`) | Tools in a neat row, one per hook. A missing one would be noticed. |

Optional extras, **not** built (all pass the width check): a burglary line ('Drawers hang open and the floor is scuffed. Someone left in a hurry.', needs one table row), a Veldris TV line ('A programme about rich people being ordinary at length.', needs one more C edit: the stock TV script says 'MOM/DAD might like this program' and drives the Hoenn TV shows; the Hollowbrook houses avoid it with TV signs), and a restyle of the stock bookshelf, trash can and shop shelf text in `data/text/check_furniture.inc`.

## Porymap guide for the author (PROPOSED; written without running Porymap, so tell me if a screen differs)

Which behaviour for which furniture: fridge, pot or food on a table = `MB_FOOD`; food that should smell = `MB_FOOD_SMELLS_TASTY`; stove, sink, kitchen counter = `MB_KITCHEN`; dish cupboard = `MB_CABINET`; wardrobe or chest of drawers = `MB_DRESSER`; framed picture = `MB_PAINTING`; computer = `MB_COMPUTER`; phone = `MB_TELEPHONE`; wall poster = `MB_ADVERTISING_POSTER`; console or arcade = `MB_VIDEO_GAME`; snack bowl = `MB_SNACKS`; mug = `MB_CUP`; panel of lights = `MB_BLINKING_LIGHTS`; tool rack = `MB_NEATLY_LINED_UP_TOOLS`; lab or workshop machine = `MB_IMPRESSIVE_MACHINE` or `MB_POWER_PLANT_MACHINE`; plans on a table = `MB_BLUEPRINTS`. Bookshelf (`MB_BOOKSHELF`), trash can (`MB_TRASH_CAN`), PC (`MB_PC`) and TV (`MB_TELEVISION`) already work with stock lines. **Do not pick** `MB_BURGLARY`, `MB_TRAINER_TOWER_MONITOR`, `MB_CABLE_CLUB_WIRELESS_MONITOR`, `MB_BATTLE_RECORDS` or `MB_INDIGO_PLATEAU_SIGN_1/2` (not wired).

1. In Porymap open any map that uses the tileset (for the Gen 4 Interior: `Crestfall_HouseA`, `Hollowbrook_NeighboursHouse`).
2. Open the secondary tileset editor (menu bar, Tools, Edit Secondary Tileset). Tiles are on the left, the metatiles (16 x 16 building blocks) on the right.
3. Click the metatile you want, for example the fridge. Its number is shown (the secondary numbers in `design/interiors.md` are these).
4. In the properties box set **Behavior** to the matching `MB_` name.
5. Repeat for each furniture metatile (a big piece is several metatiles; set the ones the player can face). Save the tileset, then the project.
6. In the map, make sure the furniture is blocked (Collision: 'cannot walk'). Pressing A works from any side; there is no direction rule.
7. Tell me which metatiles you set and I rebuild and test. If the Behavior list does not show `MB_` names, stop and tell me; do not type numbers.

**Warning:** if the Gen 4 Interior is ever rebuilt with Porytiles, behaviours set only in Porymap are lost unless the same rows go into `data/tilesets/secondary/gen4_interior/porytiles_src/attributes.csv`. Tell me before rebuilding.

## Per-spot sign (no engine edit, any text, can depend on flags)

In Porymap: Events tab, Sign button, click the tile, set Facing to **any** (so it also wins from the side), and give a script label. Or let Claude write it in `data/maps/<Map>/map.json` (close or reload Porymap first):

```
{ "type": "sign", "x": 3, "y": 2, "elevation": 0, "player_facing_dir": "BG_EVENT_PLAYER_FACING_ANY", "script": "Crestfall_HouseA_EventScript_Fridge" }
```

and in that map's `scripts.inc` (same shape as `Hollowbrook_PlayersHouse_1F_EventScript_TV`, text checked by `dialogue_check.py`):

```
Crestfall_HouseA_EventScript_Fridge::
	msgbox Crestfall_HouseA_Text_Fridge, MSGBOX_SIGN
	end
```

Interaction order is object event, then sign, then metatile behaviour. A sign facing only north would let the general line show from the side, so use 'any' on tiles that also carry a behaviour. **Seen in game 2026-10-09:** the neighbour's bookshelf had a north-only sign, and from the window-alcove tile beside it the stock bookshelf line ('It's filled with all sorts of books.') replaced the cookbooks line. All furniture signs in the Hollowbrook houses (bookshelves, TVs, fridge) now face 'any'. In the player's house 1F the stove, sink and counter sit behind blocked floor ((1..3,3)), so a behaviour set on them can never be reached; the fridge is only reachable from (4,3).

## Limits

- One line per furniture **type** for the general version. A metatile has one behaviour in every map that uses its tileset, so a rich Goldsworth room that reuses a cabinet needs a sign to say something richer.
- The Goldsworth jokes from the earlier draft (silver cabinet, fourteen waistcoats, portrait frame) are better as signs in their own rooms than as general lines. Still PROPOSED.

## Tests

| Check | Result |
|---|---|
| Throwaway COPY of the tree (not the repo), 17 Gen 4 Interior metatiles given behaviours in the copy only: build passes, the 17-row table is right in the ELF; in mGBA the poster and blinking-lights tiles speak the new lines and the lab bookshelf still speaks the stock one | Pass (planner, 2026-10-09) |
| Collision scan of every compiled tileset for the 25 behaviours | 0 hits, so nothing speaks by itself |
| In-repo build (2026-10-09): `VeldrisGetFurnitureScript` and `Veldris_EventScript_Furniture_*` are in the ELF | Pass |
| An in-game check in the real tree after the author sets real behaviours | Not run yet |
