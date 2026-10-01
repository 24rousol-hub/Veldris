# Interior and detail design rules (PROPOSED, 2026-10-01)

Status: **PROPOSED.** The brief for the detailed design pass: turn each place and road card into instructions the author can follow in Porymap. Built from three sources: the Team Aqua repo's tilesets, the base game (vanilla Hoenn layouts in this tree), and the Project Palladium renders. Catalogue of everything available: [catalogue.md](catalogue.md). Existing cards: [../index.md](../index.md). Hollowbrook is already built and sets the house style: [../../interiors.md](../../interiors.md).

## Decisions

1. **House style.** Every ordinary home, lab and small shop interior uses the **Gen 4 Interior Secondary** tileset already in the tree (`data/tilesets/secondary/gen4_interior/`), so the whole region's homes match Hollowbrook's. Use the same furniture vocabulary: kitchen counter, stove, fridge, stools, bookshelf, TV with flower table and cushions, cosy rug, plant, stairs.
2. **Function buildings keep vanilla layouts.** **Pokémon Centers and Marts use `LAYOUT_POKEMON_CENTER_1F`/`_2F` and `LAYOUT_MART` unchanged** (the nurse, heal and shop scripts and the link counters depend on their positions). Their look can be swapped by the `Alternative Pokecenter Secondary` tileset later; never move the nurse or counter.
3. **Special buildings use a themed Team Aqua tileset** (Little Office for Gildhaven's offices, Brick Cafe for eateries, Gatehouse for gates, Dojo for halls, Zelda House for huts). Import each only in the commit that first needs it, with a `CREDITS.md` row.
4. **Gyms:** trace the matching Palladium gym image (table in [../../region-names.md](../../region-names.md)), paint with the vanilla gym tilesets (`gTileset_Building` plus a Rustboro, Dewford, Mauville or Petalburg gym secondary) and add theme tiles only where the card says so. Keep each gym map to 15 live objects.
5. **Elite Four, Champion, Hall of Fame:** the Palladium E4 rooms, painted with the vanilla Ever Grande tilesets, colour-matched per member.
6. **Caves and forests:** Palladium images plus the vanilla cave tilesets (Granite, Meteor Falls, Shoal, Seafloor) or the Team Aqua cave sets for the special ones.
7. **Keep the door rule.** Every interior door is one warp pair on a door mat at the bottom, the exit warp lands outside the door, buildings are entered from the south, unless a card says otherwise.
8. **Size rules.** A house is 9 to 13 wide and 8 to 11 tall, a shop 10 to 14 by 8 to 10, a lab 14 x 12, a gym 13 to 15 by 17 to 23. Max map size `(w + 15) * (h + 14) <= 10240`. Object limit: the engine keeps at most about 16 objects alive near the camera (`TrySpawnObjectEvents`, 64 templates per map), so tall roads can hold more than 15 in total; keep any one screen to 15 or fewer.
9. **Everything borrowed is credited** in `CREDITS.md` in the same commit that imports it.

## What the detailed documents must contain

**Per settlement** (`design/maps/detail/<name>.md`):
- **Description:** the first-glance picture (what the player sees on entering from each road), mood, colour, sound and time of day, the one memorable view.
- **Street layout in words:** a numbered walk through the town, with named districts, paths, landmarks, water, trees, ledges and tile palettes.
- **Every building:** its purpose, which layout and tileset to use (vanilla layout, Palladium image to trace, Team Aqua tileset), size, floors, an interior plan in words (where the door, counter, stairs, furniture and each NPC stand, as x, y tile coordinates where sensible), the warps, and what the player does there.
- **Door and warp table:** map, tile, destination.
- **Palette and tile notes:** tilesets, how to dress the Palladium render with the tiles in this tree, what has to be redrawn.
- **Build checklist** in order.

**Per road** (`design/maps/detail/<group>-routes.md`):
- **Description and walk-through:** the opening view from each end, the main path shape, set pieces and pacing, then a segment-by-segment layout (about 4 to 8 segments per road) with terrain, grass patches, ledges, water, trees, signposts.
- **Trainers:** position, facing and sight range of each one, so the walk makes the fights feel earned. Items and hidden items with positions in words.
- **Visual identity:** tilesets, colours, weather, music suggestion (an existing Hoenn track), landmark silhouettes.
- **Connections:** edge, offset in tiles, matching door or gate.

Keep to the facts already in the cards (species, levels, trainer lists, items, flags). Add detail, do not change canon.
