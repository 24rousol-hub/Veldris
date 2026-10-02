# Shared house layouts (PROPOSED, 2026-10-01)

Author direction (2026-10-01, repeated twice): **no custom layout for each house; a MINIMUM of 5 different single-floor house interiors (5 is the floor, not the target).** So every ordinary house in Veldris is one of the layouts below, all on the **Gen 4 Interior Secondary** tileset with `gTileset_Building` as primary, `layout_version` `emerald`. Nothing here is built: the author paints each layout once in Porymap, then every house reuses it (Layouts tab, right-click the layout, **Add New Map with Layout**, so painting one changes all of them). Per-house differences come from objects (NPCs, a Skitty, an item ball) and from the sign outside, not from the floor plan.

Scope: homes, small shops-as-homes and the Goldsworth houses. **Not covered (unchanged):** Pokémon Centers and Marts (vanilla), gyms, the lab, the League. Hollowbrook's built maps (player's house 13 x 9 two floors, neighbour 11 x 8) stay as they are.

Common rules: door mat at the bottom, exit warp lands outside the door, every layout is **1 floor, no stairs**. Coordinates are tiles from the top-left, (0,0). `D` = door mat, `#` = wall row, `K` kitchen counter/stove/fridge, `B` bookshelf, `T` TV with flower table and two cushions, `b` bed, `R` rug, `p` plant, `S` stool, `W` window. Furniture vocabulary is only what the Gen 4 set already has (see its `example.png`).

## The six layouts

### H1 Cottage, 9 x 8
```
x: 0 1 2 3 4 5 6 7 8
y0 # # # # # # # # #
y1 # W K K B # W # #     kitchen top-left, bookshelf, window
y2 . . . S . . . . .
y3 . R R R . T T . .     rug centre, TV right
y4 . R R R . . . . .
y5 . . . . . . p . .
y6 . . . . . . . . .
y7 # # D # # # # # #     door (2,7)
```
Smallest home: villagers, single elders, farm cottages. One NPC plus a pet.

### H2 Kitchen house, 10 x 8
```
y1 # K K K K B B W # #   long kitchen wall, two bookshelves
y2 . . . . . . . . . .
y3 . S . S . . T T . .   two stools at a counter, TV right
y4 . . . . . . . . . .
y5 . R R R . . . p . .
y6 . . . . . . . . . .
y7 # D # # # # # # # #   door (1,7)
```
Cooking-family house; the stove is the story prop (a woman mid-recipe).

### H3 Family house, 11 x 8 (the Hollowbrook neighbour's plan; already built)
Use the built `Hollowbrook_NeighboursHouse` as this layout (stove and fridge, window, bookshelf, TV with cushions, plant, mat (2,7)). Only reuse it; do not repaint.

### H4 Studio, 10 x 9
```
y1 # B B W K K W B B #   shelves both ends
y2 . . . . . . . . . .
y3 . . R R R R R . . .   large central rug (a hobby table can sit on it)
y4 . S . R R R . S . .
y5 . . . . . . . . . .
y6 p . . . . . . . . p
y7 . . . . . . . . . .
y8 # # # # D # # # # #   door (4,8), centred
```
Workshop, collector's den, painter's studio. Good for item-giver NPCs.

### H5 Bedroom house, 11 x 8
```
y1 # b b W K K B B W # #   bed top-left, kitchen right of it
y2 . b b . . . . . . . .
y3 . . . . . R R . T T .
y4 . . p . . R R . . . .
y5 . . . . . . . . . . .
y6 . . . . . . . . . . .
y7 # # D # # # # # # # #   door (2,7)
```
Anywhere a character sleeps in view: sick kid, night-shift worker, travelling trainer's rest.

### H6 Big house, 13 x 9 (the Goldsworth plan)
```
y1 # B B W K K K W T T W B B #
y2 . . . . . . . . . . . . .
y3 . R R R R . . . . S S . .
y4 . R R R R . p . . . . . .
y5 . . . . . . . . . . . . .
y6 . . . . . . . . . . . . .
y7 . . . . . . . . . . . . .
y8 # # # # # # D # # # # # #   door (6,8)
```
The roomiest, one floor, symmetrical and a little too grand. It replaces the 13 x 11 Goldsworth plan proposed in `../detail/kingsquay.md` 6.10 (the 11-high version is not needed). Every Goldsworth house uses it; cousins differ by object placement (see [../detail/index.md](../detail/index.md), the Goldsworth resolution).

## Which town uses which (PROPOSED rule)

Rotate H1 to H5 so no two adjacent buildings in a town, and no two neighbouring towns, show the same plan. Suggested start: Briarwick H2 + H4, Crestfall H1 + H5, Gloomsby H5, Smeltham H4 + H1, Hoarfell H1, Gildhaven H4 + H2, Hemlock Reach H2, Primrose Vale H5, Brinecombe H1 + H2, Ebbsworth H4, Kingsquay H5 + H3, Driftsands H1, Beaconmouth H4, Wendlebury H5 + H2. Goldsworth houses: H6 only. Final pick is the author's per card.

## Minimum rule

**At least 5 distinct single-floor house interiors must exist at all times** (author, 2026-10-01). Six are drawn up here (H1 to H6; H3 is already built as Hollowbrook's neighbour). If one is cut or merged, add another so the count never drops below five. Distinct means a different floor plan, not just different furniture or NPCs.

## Open questions

1. Is six enough? Add H7 (long hall 15 x 8) if two houses in a town still feel alike after painting.
2. H3 is the Hollowbrook neighbour's house. Hollowbrook's own two houses stay unique because they exist already.
