# WENDLEBURY: detailed town design (PROPOSED, 2026-10-01)

Status: **PROPOSED.** The build brief for the author's Porymap work. Facts come from [../../wendlebury.md](../../wendlebury.md) (role, buildings, flavour), [../../dialogue/wendlebury.inc](../../dialogue/wendlebury.inc) (every NPC and sign), [../interiors/README.md](../interiors/README.md) (house style) and [../interiors/catalogue.md](../interiors/catalogue.md). Roads: [routes-west-a.md](routes-west-a.md) (R2 arrives at the south edge, R8 at the north edge). The name is approved; everything else here is a suggestion. New minor names are marked PROPOSED. Nothing is built.

Quick facts: **town**, no gym, no Goldsworth house, the third place. Pokémon Center, Mart, the market square and the sea. Gossip about the Goldsworths and about Crestfall's scheme. A blocked road to the west (the barricade) and, after the League, the water route R27 to Vesperhaven from its beach. Fly point and heal location: yes.

Coordinates are `(x, y)` in tiles from the top-left and are **read off the render, so they are right to about one tile**; confirm with Porymap's status bar. **Trace the render mirrored left to right** (reason below). Map size **51 x 29** (the render is 816 x 465 px, no grid, `px / 16`). Size check: (51 + 15) x (29 + 14) = 2,838 of 10,240.

**Mirroring.** Palladium's `Cherrygrove City.png` has the sea on the west and south-west. The sketch puts Wendlebury's only water (R27 to Vesperhaven, post-game) to the east and south-east, and the land towns to the west. So flip the picture left to right while tracing: every x in this document is already the **mirrored** x (`50 - x_render`). Houses and signs mirror cleanly (chimneys end up on the other side, which does not matter).

---

## 1. Description

**First glance from Route 2 (south edge).** You climb out of a pine wall onto a small sand yard in front of a red-roofed house, with a second red roof above it and a third to the left. The sand widens into a street and, to the right of it, the whole east side of the map is open water with a little sand island and a rock in the middle of it. Above, two roofs side by side, one red and one blue, under a row of pines: the Center and the Mart.

**First glance from Route 8 (north edge).** You come down a straight 3-wide sand path with the pines on both sides and arrive in the middle of the market street, with the Mart on your left and the water at the end of the street on your right.

**Mood and colour.** Salt, sun, haggling. Red roofs, sand, blue sea, orange flowers in the berry patch. Bright late morning, `WEATHER_SUNNY`. The one calm place on the road before the first real forest city.

**Sound.** `MUS_SLATEPORT` (Slateport's tune is the Hoenn market track; `MUS_OLDALE` is the plainer fallback). Pokémon cries only: WINGULL, WINGULL again, a distant SLAKOTH that is not making a sound. No real animals.

**Time of day.** Late morning on market day. Everything is for sale. Mostly.

**The one memorable view.** Standing on the shore end of the market street, at about (32, 8): the sea opens on your right, the red Center roof and blue Mart roof sit above the stalls on your left, and the sand island with its rock floats out in the water ahead, exactly the tableau the render gives from the other side. Keep the beach and the island uncluttered so this view reads.

**What the player does here.** Heals, shops, hears the Goldsworth gossip and the Crestfall hay-maze rumour, meets the barricade man, and chooses R8 (north) toward Briarwick, or back down R2. No battle and no scheme here.

---

## 2. Street layout in words (numbered walk)

Roads: **R2 enters the south edge** at x 10 to 12; **R8 enters the north edge** at x 24 to 26; the **west edge** (y 8 to 9) is the barricade; the **east edge** is the sea (post-game water route R27).

1. **South gap (x 10 to 12, y 17 to 28).** R2 arrives at the bottom edge. The render's SW is a solid pine forest (mirrored: x 0 to 23, y 17 to 28); cut a 3-wide sand lane through it at x 10 to 12 up to the sand yard.
2. **The sand yard (x 6 to 14, y 15 to 18).** A square of sand with two flower clumps (x 14 to 16, y 17 to 18). **House 3** (the Inn, PROPOSED) stands at its top-left (x 6 to 10, y 13 to 16, door (9, 16)). A sign at (10, 11) is the Inn's sign (the render's sign at (40, 11)).
3. **The west lane (x 0 to 13, y 6 to 9).** The main street's west half. It reaches the **barricade** at the west edge (0 to 3, y 8 to 9): orange-and-white barrier tiles or fence at (2, 8) and (2, 9), 'ROAD CLOSED' objects, and the barricade man at (3, 8). The pond (x 2 to 5, y 0 to 3) is behind pines at the top-left, decoration only.
4. **The Center and Mart (y 2 to 5).** Pokémon Center x 8 to 12 (door (10, 5)), Mart x 16 to 19 (door (17, 5)), with a low hedge of round bushes at (13 to 14, y 2 to 5) between them (the render's four round shrubs). Both open south onto the main street at y 6.
5. **The main street (y 6 to 9, x 8 to 32).** A 4-row sand band, wider than any other road in the game so far (the market street). West of x 8 it narrows to two rows (y 8 to 9) toward the barricade.
6. **The north path (x 24 to 26, y 0 to 6).** A 3-wide sand column running north off the top edge to R8. A town sign at (24, 7).
7. **House 1 (x 22 to 26, y 8 to 11, door (25, 11)), House 2 (x 14 to 18, y 11 to 14, door (17, 14)).** Red-roofed houses with chimneys, set in the sand with a **berry flower patch** (x 14 to 20, y 9 to 10) between them (the render's red flower clump). A sign at (19, 14) is House 2's name plate.
8. **The market square (x 26 to 32, y 7 to 13).** The sand shelf between the houses and the water. Three stalls along y 9. A lamp or crate cluster in the middle. The shoreline is at x 33 for y 6 to 13, x 28 for y 14 to 16, x 24 for y 17 onward.
9. **The beach and the island.** The sand island (x 34 to 39, y 15 to 19) with its rock at (37, 15), ringed by water rocks; the sea rocks in the render (white-capped stones) stay as decoration. **This is where R27 will leave from after the League**: leave a plain sand tile at (31, 12) that is walkable to the water, and nothing else; no dock yet.
10. **Pines.** The whole south-west is forest (x 0 to 23, y 17 to 28). A clump of pines at the far west (x 0 to 7, y 6 to 7) squeezes the street to two rows (y 8 to 9) where it reaches the barricade.

**Water.** The sea east and south-east (surf only after badge 5; no encounters planned until R27 in the post-game). **Trees.** Round trees (or the LeoB pine look if the set has it). **Ledges.** None in the render. **Palettes.** `gTileset_General` + `gTileset_Petalburg`, the same pair as Hollowbrook.

---

## 3. Buildings

| Building | Map name | Layout / source | Size | Floors | Notes |
|---|---|---|---|---|---|
| Pokémon Center | `Wendlebury_PokemonCenter_1F`, `_2F` | **`LAYOUT_POKEMON_CENTER_1F` / `_2F`, unchanged** | 14 x 9, 14 x 10 | 2 | Nurse, two visitors, a 2F counter clerk |
| Mart | `Wendlebury_Mart` | **`LAYOUT_MART`, unchanged** | 11 x 8 | 1 | Clerk plus a shopper |
| House 1 | `Wendlebury_House1` | Gen 4 Interior Secondary, after `Elm's House.png` | 10 x 8 | 1 | Resident and a SLAKOTH |
| House 2 | `Wendlebury_House2` | Gen 4 Interior Secondary, after `Hero's House 1st Floor.png` | 11 x 8 | 1 | Resident, child, TV |
| House 3, the Inn (PROPOSED) | `Wendlebury_Inn` | **Gen 4 Interior Secondary** (already in tree) | 14 x 9 | 1 | Innkeeper and a guest |
| Market square, stalls | none | exterior objects | - | - | Three sellers |

The cards give two houses, and the render has **three**. `Wendlebury_Text_ResidentB` says 'We have one inn', so a third building makes sense as the inn. **Recommended: build the Inn** (on the Gen 4 Interior set, the author's call). **Fallback:** House 3 is scenery with a sign on the door ('CLOSED FOR THE SEASON'), no interior, no import.

**Building outlines on the outdoor map** (mirrored):

| Building | Footprint (x, y) | Door tile | Tile you stand on to enter |
|---|---|---|---|
| Pokémon Center | 8 to 12, 2 to 5 | (10, 5) | (10, 6) |
| Mart | 16 to 19, 2 to 5 | (17, 5) | (17, 6) |
| House 1 | 22 to 26, 8 to 11 | (25, 11) | (25, 12) |
| House 2 | 14 to 18, 11 to 14 | (17, 14) | (17, 15) |
| House 3 (Inn) | 6 to 10, 13 to 16 | (9, 16) | (9, 17) |

### 3.1 Pokémon Center (`LAYOUT_POKEMON_CENTER_1F` and `_2F`)

Do not repaint or move anything. Vanilla positions (read from `OldaleTown_PokemonCenter_*/map.json`, the same layouts):

| Map | Warp | Tile | Destination |
|---|---|---|---|
| 1F | 0 and 1 | (7, 8) and (6, 8), door mat | `Wendlebury` warp 0 |
| 1F | 2 | (1, 6), stairs | 2F warp 0 |
| 2F | 0 | (1, 6) | 1F warp 2 |
| 2F | 1, 2 | (5, 1), (9, 1) | Union Room, Trade Center (vanilla) |

1F objects: **nurse (7, 2)** facing down (`CenterNurse`, `CenterNurseDone`); **visitor** at (4, 4) facing right (`CenterVisitor`: the free soup); **visitor 2** at (9, 6) facing left (`CenterVisitor2`: 'I have been waiting an hour'). 2F: the vanilla Union Room attendant (6, 2) speaks `Center2FCounter` ('Trades and battles are done upstairs, when the cables are untangled'); the other attendants and the Mystery Gift man stay vanilla.

**Heal location and fly.** `HEAL_LOCATION_WENDLEBURY` lands at **(10, 6)** below the Center door. In `heal_locations.json` write `respawn_map` **before** `respawn_npc`, and always give both. One new row in `src/data/veldris_fly_towns.h` plus the data steps in [../../region-map.md](../../region-map.md). `OnTransition` sets `FLAG_VISITED_WENDLEBURY` (proposed name).

### 3.2 Mart (`LAYOUT_MART`)

Unchanged. Vanilla: warps (3, 7) and (4, 7) to `Wendlebury` warp 1; **clerk (1, 3)** (`MartClerk`: 'Everything here is priced fairly. Mostly to me'); **shopper (5, 5)** facing up (`MartShopper`: 'I came for one POTION. I'm leaving with eleven things'). Stock (first stock, proposed): POKé BALL, POTION, ANTIDOTE, PARALYZE HEAL.

### 3.3 House 1 (resident and SLAKOTH): `Wendlebury_House1`, 10 x 8

Gen 4 Interior Secondary, after `Elm's House.png` (13 x 10 render, room 11 x 8, trim to 10 x 8). Warm, cluttered, a house of someone who keeps everything.

- **Back wall (y 1 to 2):** window (1), **bookshelf of receipts (2 to 3)**, stove (4 to 5), fridge (6 to 7), a hanging clock or plant at (8).
- **Floor:** a rug at (3 to 6, 4 to 6) with a flower table (4 to 5, 4 to 5) and cushions (3, 5) and (6, 5); a plant at (9, 6).
- **Door mat and warp:** (6, 7) to `Wendlebury` warp 2. Arrive at (25, 12).

| Who | Tile | Facing | Text |
|---|---|---|---|
| Resident | (7, 5) | left | `House1Resident` ('Mind the doormat. It's a SLAKOTH...') |
| SLAKOTH | (5, 3) | up (by the stove) | `House1Pokemon` ('SLAKOTH: ...Kyu.') |

bg events: bookshelf (2 and 3, 2) `House1Shelf`. 2 objects.

### 3.4 House 2 (resident, child, TV): `Wendlebury_House2`, 11 x 8

Gen 4 Interior Secondary, after `Hero's House 1st Floor.png` (13 x 9: stove, fridge, bookshelf, TV, stairs-like block, rug). Noisy house: a TV always on.

- **Back wall (y 1 to 2):** stove (0 to 1), fridge (2 to 3), window (4), **TV on its cabinet (5 to 6)**, bookshelf (8 to 9), plant (10, 2).
- **Floor:** two cushions (4, 5) and (7, 5) either side of a low table (5 to 6, 4 to 6); rug (3 to 8, 4 to 7).
- **Door mat and warp:** (4, 7) to `Wendlebury` warp 3. Arrive at (17, 15).

| Who | Tile | Facing | Text |
|---|---|---|---|
| Resident | (3, 3) | down | `House2Resident` ('the market shouts outside my window') |
| Child | (7, 4) | left | `House2Child` ('the secret of the market is: haggle') |

bg events: TV (5 and 6, 2) `House2TV` ('It ends with a boat. It always ends with a boat'). 2 objects.

### 3.5 House 3, the Inn: `Wendlebury_Inn`, 14 x 9 (Gen 4 Interior, author's call 2026-10-01)

The author likes the Inn and wants it **Gen 4**. So it uses the **Gen 4 Interior Secondary** tileset like every other home (already in the tree and credited), **not Brick Cafe**: no import, no new `CREDITS.md` row. It is a single-floor special layout (the one exception to the shared house layouts in [../interiors/house-layouts.md](../interiors/house-layouts.md), because a reception counter and two guest beds are not a home), and later inns (Kingsquay, Gildhaven) can reuse it with Add New Map with Layout. Primary is `gTileset_Building`, `layout_version` `emerald`.

Furniture, all from the Gen 4 set (see its `example.png`): the L-shaped kitchen counter as the reception desk, stove and fridge as the kitchen behind it, the stools, two beds (the bedroom set), the TV with the flower table and cushions as the lounge, bookshelves, the blue rug, plants. `K` counter, `S` stool, `b` bed, `B` bookshelf, `T` TV and flower table, `R` rug, `p` plant, `W` window, `m` door mat.

```
      0 1 2 3 4 5 6 7 8 9 a b c d
y1    # W K K K B B W b b W b b #     stove/fridge wall, shelves, two guest beds (x 8-9 and 11-12)
y2    # . . . . . . . b b . b b #
y3    # K K K K . . . . . . . . #     reception counter (L) x 1-4, y 3
y4    # . S . S . . . . . R R . #     guest stools at (2, 4) and (4, 4)
y5    # . . . . . . . . . R R . #
y6    # p . . . . T T . . . . p #     lounge: TV and flower table (6-7, 6), cushions below
y7    # . . . . . . . . . . . . #
y8    # # # # # # m # # # # # # #     door mat (6, 8)
```

Note: the Gen 4 counter blocks from one side only. Build it so the innkeeper stands at (3, 2) behind the counter row at y 3 and the player talks from (3, 4); then the stools at (2, 4) and (4, 4) are the guests' seats. Tweak freely in Porymap, the plan is a sketch.

- **Door mat and warp:** (6, 8) to `Wendlebury` warp 4. Arrive at (9, 17).
- **Beds** are scenery (the Inn offers no sleep or heal; the Center does that).

| Who | Tile | Facing | Notes |
|---|---|---|---|
| Innkeeper (name PROPOSED: Mrs Tuppence) | (3, 2) | down (behind the counter) | new lines needed: welcome, 'we have one inn', Troglodyte asked for the best table and was given a stool |
| Guest | (3, 4) | up (at the counter) | gossip, one of the three Goldsworth lines |

No heal, no shop; it is flavour and a place to hear the gossip. **New dialogue is needed** (nothing is drafted for the inn), written in the dialogue pass.

---

## 4. Market square and the barricade (exterior objects)

**Market square (x 26 to 32, y 7 to 13).** Three stalls in a row, a counter tile at y 10 for each, the seller standing behind at y 9 facing down, a 1-tile gap between stalls so the crowd flows.

| Stall | Seller tile | Counter tile | Text |
|---|---|---|---|
| Market trader (POKé BALLS) | (27, 9) | (27, 10) | `Trader` / `TraderAfterCrestfall` |
| Berry seller | (29, 9) | (29, 10) | `BerrySeller` |
| Tea seller | (31, 9) | (31, 10) | `TeaSeller` |

Stall art is not in the vanilla sets. Use a wooden fence or crate tile as the counter; a real awning is new art (open question 3). Coloured flags would be a nice touch if the author draws them.

**Berry flower patch (x 14 to 20, y 9 to 10).** Decoration. A hidden POKé BALL (PROPOSED) at (16, 10).

**The barricade (x 0 to 3, y 8 to 9).** Orange and white barrier tiles at (2, 8) and (2, 9), 'ROAD CLOSED' signs, the **barricade man** at (3, 8) facing left, the **kid** at (5, 9) facing left (the kid who is not allowed past). Nothing opens this: it never becomes a road (the sketch gives no road west). Note the pines at (0 to 1, 8 to 9) behind it so the edge is solid.

---

## 5. NPC placement (outdoors)

All text labels use the prefix `Wendlebury_Text_`. 11 NPCs outdoors, comfortably under the live limit.

| Who | Tile | Facing / movement | Label | When |
|---|---|---|---|---|
| Barricade man | (3, 8) | face left | `BarricadeMan` | always |
| Kid | (5, 9) | face left | `Kid` / `KidAfterCrestfall` | always (after the first badge uses the second line) |
| Gossip | (20, 7) | face right (near the Mart) | `Gossip` / `GossipAfterCrestfall` | always |
| Traveller from the north | (25, 2) | face down (on the north path) | `TravellerNorth` / `TravellerNorthAfter` | always |
| Resident A | (21, 12) | face right (beside House 1) | `ResidentA` / `ResidentAAfterCrestfall` | always |
| Resident B | (8, 17) | face right (by the Inn) | `ResidentB` | always |
| Trader | (27, 9) | face down | `Trader` / `TraderAfterCrestfall` | always |
| Berry seller | (29, 9) | face down | `BerrySeller` | always |
| Tea seller | (31, 9) | face down | `TeaSeller` | always |
| Troglodyte sighting | (28, 12) | face down | `TrogSighting` | optional, can be cut; only after the lab fight |

**Signs.** Town sign (24, 7) `TownSign`; Pokémon Center sign (13, 6) `CenterSign`; Mart sign (20, 6) `MartSign`; House 2 name plate (19, 14); Inn sign (10, 11) new text, PROPOSED. The vanilla Center and Mart signs are two tiles each; place both halves.

**No triggers, no new flags** beyond the visited flag (as in the existing card). The 'after' lines use `FLAG_BADGE01_GET`.

---

## 6. Door and warp table

| Map | Warp # | Tile | Destination | Arrive at |
|---|---|---|---|---|
| `Wendlebury` | 0 | (10, 5) | `Wendlebury_PokemonCenter_1F` warp 0 | (6 to 7, 8) |
| `Wendlebury` | 1 | (17, 5) | `Wendlebury_Mart` warp 0 | (3 to 4, 7) |
| `Wendlebury` | 2 | (25, 11) | `Wendlebury_House1` warp 0 | (6, 7) |
| `Wendlebury` | 3 | (17, 14) | `Wendlebury_House2` warp 0 | (4, 7) |
| `Wendlebury` | 4 | (9, 16) | `Wendlebury_Inn` warp 0 (if built) | (7, 8) |
| `Wendlebury_PokemonCenter_1F` | 0, 1 | (6, 8), (7, 8) | `Wendlebury` warp 0 | (10, 6) |
| `Wendlebury_PokemonCenter_1F` | 2 | (1, 6) | `Wendlebury_PokemonCenter_2F` warp 0 | (1, 6) |
| `Wendlebury_PokemonCenter_2F` | 0 | (1, 6) | `Wendlebury_PokemonCenter_1F` warp 2 | (1, 6) |
| `Wendlebury_PokemonCenter_2F` | 1, 2 | (5, 1), (9, 1) | Union Room, Trade Center (vanilla) | vanilla |
| `Wendlebury_Mart` | 0, 1 | (3, 7), (4, 7) | `Wendlebury` warp 1 | (17, 6) |
| `Wendlebury_House1` | 0 | (6, 7) | `Wendlebury` warp 2 | (25, 12) |
| `Wendlebury_House2` | 0 | (4, 7) | `Wendlebury` warp 3 | (17, 15) |
| `Wendlebury_Inn` | 0 | (7, 8) | `Wendlebury` warp 4 | (9, 17) |

**Map connections** (leave 'Mirror to Connecting Maps' ticked):

| Edge | Neighbour | Opening here | Opening there | Offset on `Wendlebury` |
|---|---|---|---|---|
| Up | `VeldrisRoute8` | x 24 to 26 | R8 bottom edge x 12 to 14 | **+12** (R8's left edge is 12 columns right of Wendlebury's) |
| Down | `VeldrisRoute2` | x 10 to 12 | R2 top edge x 10 to 12 | **0** |
| Left | none | barricade | - | - |

The west side is a wall of pines and the barricade, not a connection. The east side is open sea, not a connection yet.

---

## 7. Palette, tiles and what has to be redrawn

- **Outdoor tilesets:** `gTileset_General` + `gTileset_Petalburg` (the LeoB ORAS recolour already in the tree). **No import and no new `CREDITS.md` row for the outdoor map**, except the Palladium credit that goes in with the first traced map ('credit the Project Palladium team naming the files used'). Files used by Wendlebury: `Cherrygrove City.png`, `Elm's House.png`, `Hero's House 1st Floor.png`.
- **What the vanilla tiles do not have** ([../../map-plan.md](../../map-plan.md)): the red roofs with a chimney and a yellow door (Hoenn roofs are different colours and have no chimney), the pine look, and the two-tone sea with white-capped rocks. The layout matches; the colours will be about 70 per cent. Keep the red Center roof and blue Mart roof, so the colour code stays readable.
- **Sea:** use the General tileset's sea tiles. The render's sand island with a rock becomes a small sandbar (Hoenn has sandbar tiles in `gTileset_Petalburg`/General). **Decoration only**: there are no wild encounters on this beach before R27.
- **Interiors:** Houses on `gTileset_Gen4Interior` (already imported and credited). Center and Mart: vanilla. **Inn: Gen 4 Interior too (author wants Gen 4), no import**, see 3.5.
- **Mirroring check:** if the author would rather not mirror, the sea ends up on the west and the barricade on the east, and R8 and R2 keep their top and bottom edges. Nothing else changes. Mirroring is a recommendation, not a requirement.

---

## 8. Items and secrets (the existing card has none; all PROPOSED)

| Item | Where | Gate |
|---|---|---|
| POKé BALL (hidden) | berry flower patch (16, 10) | none |
| POTION (hidden) | the beach (31, 13) | none |

Flags (not claimed): `FLAG_VISITED_WENDLEBURY`, `FLAG_WENDLEBURY_ITEM_*` per item. No triggers. Reused: `FLAG_BADGE01_GET` for the 'after Crestfall' lines.

---

## 9. Build checklist (in this order)

1. In Porymap create `Wendlebury`: layout 51 x 29, `gTileset_General` + `gTileset_Petalburg`, region `REGION_HOENN`, `layout_version` emerald, section `MAPSEC_WENDLEBURY`, can fly to yes.
2. Trace `Cherrygrove City.png` **mirrored**: pines, sea and sandbar, the sand street and the south and north lanes, then the five buildings, then the flower patches, then the scenery.
3. Create the Center 1F and 2F and the Mart as **Add New Map with Layout** (shared vanilla layouts). **Check `data/event_scripts.s` has each `.include` exactly once.**
4. After a Duplicate Map: grep `src/data/heal_locations.json` for duplicate ids and delete the extras.
5. Paint House 1 and House 2 (Gen 4 Interior), then the Inn (Gen 4 Interior, no import needed).
6. Place warps from section 6, then connections (R2 and R8 as those maps exist).
7. Tell Claude: objects, signs, the Center/Mart scripts, the two heal-location traps and the dialogue are wired afterwards. The author must close or reload Porymap first.
8. Update `design/flags.md` and `CREDITS.md`; `make -j4`; `python3 design/tools/dialogue_check.py` on any new Inn text.
9. Check no ROM or save is staged.

---

## Open questions

1. **Mirrored render, edges moved.** The earlier cards put R8 on Wendlebury's west edge and the barricade on the east. With the render mirrored and the Route 32 render being a north-south road, R8 reaches the **north** edge, the barricade is on the **west**, the east is sea. R2 reaches the **south** edge. Confirm, or tell me which edge the author wants for each.
2. **The Inn.** The render has three houses and the card has two. RESOLVED 2026-10-01: build the Inn, on Gen 4 Interior.
3. **Stall art.** No stall tile exists; fence or crate counters until the author draws one.
4. **Sea access.** Nothing here is Surfable until badge 5. Is a sand tile at (31, 12) that leads into the water enough of a hook for the post-game R27, or should a dock be painted now and hidden?
5. **Barricade man's lines** ('Road's closed. Official reasons. They keep changing') stay the same; he now blocks the west rather than the east. No text change needed.
6. **Object limit.** 11 outdoor objects here; the README's '15 per map' is really 15 in view (`TrySpawnObjectEvents`). Fine either way.
