# Porymap walkthrough: Hollowbrook, the lab and Route 1

For the author. Very detailed, click by click. Status: **PROPOSED**. Companion to the shorter [porymap-first-map.md](porymap-first-map.md) (setup, git loop, time estimates) and to [map-plan.md](map-plan.md) (which maps, which bases).

**How this was written.** From Porymap's manual and source code (release 6.3.1) and this repo. **Porymap was not run.** Menu names and button places are from the manual and source and may be a little off in your version: if something does not match the screen, tell me and I will fix this file. Tile positions in Part 6 are **measured from the Palladium pictures by eye and can be off by 1 or 2 tiles**. They tell you roughly where things go, not exact coordinates.

**The preview:** [art/first_maps_preview.png](art/first_maps_preview.png). Left is the picture you trace (Palladium). Right is a render of the vanilla map you start from (Littleroot, Birch's lab, Route 101). It is a **picture only**, made by a read-only script that draws existing vanilla maps. **No map file was written.** It shows where you start, not the finished look: the pine trees, green roofs and pale paths on the left do not exist in our tilesets (see 'How close vanilla tiles get' in map-plan.md).

---

## Part 1: What you are looking at (the window)

Open Porymap with the project loaded. The window has these parts:

- **Left panel, the map list.** Three tabs at the bottom: **Groups** (maps by group), **Areas** (by map section), **Layouts** (the painted grids). Double-click a map name to open it. Hollowbrook will live in the group `gMapGroup_TownsAndRoutes`.
- **Centre, the map view.** Above it a row of tabs: **Map**, **Events**, **Header**, **Connections**, **Wild Pokémon**. You spend nearly all your time in Map and Events.
- **Right panel, the tile picker.** Tabs: **Metatiles**, **Collision**, **Prefabs**. A *metatile* is one 16 x 16 square (four 8 x 8 tiles). Pick one here, then paint it on the map.
- **Bottom bar / status line.** Shows the tile under the mouse as `X: 12 Y: 9`. This is how you find exact coordinates. **Use it constantly.**
- **Toolbar buttons above the map:** the Pencil, Bucket, Eyedropper, Move, Smart Paths toggle, zoom, and (in Events) the object-type buttons.

Two words you need:
- **Elevation** and **collision** are stored with every tile. Collision 0 = walkable, 1 = blocked. Elevation 3 = normal ground. Elevation 0 = a special "transition" level. A tile with the wrong elevation stops cutscene triggers and movement. More in Part 4.
- **Layout** is the painted grid. **Map** is a layout plus events plus a header. Two maps may share one layout.

## Part 2: The five things you do, in order

For every map the loop is the same. Do them in this order:

1. **Create or duplicate the map** (Part 3).
2. **Paint the tiles** (Map tab, Metatiles).
3. **Paint collision and elevation** (Map tab, Collision).
4. **Place events** (Events tab): doors (warps), signs, NPCs, triggers. You can leave most of this to me, see Part 5.
5. **Save, commit, push, tell me** (Part 7).

---

## Part 3: Making the maps

### 3.1 Hollowbrook (the village)
Do the smoke test in porymap-first-map.md first if you have not. Then:

1. Open `LittlerootTown` (Groups tab, `gMapGroup_TownsAndRoutes`).
2. **File > Duplicate Current Map.**
3. Fill in the dialog: Map Name `Hollowbrook`, Map Group `gMapGroup_TownsAndRoutes`, Location `MAPSEC_HOLLOWBROOK` (click the small arrow by **Header Data** to reveal Location). Leave **Can Fly To** unticked. Size and tileset boxes are greyed out in a duplicate, which is normal.
4. Click OK. You now have a Hollowbrook that is an exact copy of Littleroot.
5. **Before you touch anything else: Events tab, select both Heal Location events, press Delete.** (The copy brings Littleroot's two with their old ids. If they survive the first save the build breaks.)
6. **Resize:** in the Map tab use **Change Dimensions** (a button near the top right of the map view; the Map > Change Dimensions menu item also exists). Type width **32**, height **28**. The new ground comes in empty, elevation 0. You repaint it in Part 4.

### 3.2 The interiors

| Map to create | Start from | How |
|---|---|---|
| `Hollowbrook_ProfessorFennicksLab` | `LittlerootTown_ProfessorBirchsLab` | Duplicate Current Map. Repaint the table later (3.4) |
| `Hollowbrook_PlayersHouse_1F` | `LittlerootTown_BrendansHouse_1F` | Duplicate |
| `Hollowbrook_PlayersHouse_2F` | `LittlerootTown_BrendansHouse_2F` | Duplicate |
| `Hollowbrook_NeighboursHouse` | `LittlerootTown_MaysHouse_1F` | Duplicate |
| `Hollowbrook_GoldsworthHouse` | `LAYOUT_HOUSE1` (shared) | **Do this last.** Layouts tab > right-click the layout > Add New Map with Layout |

Every duplicate copies the source's events, including heal locations. **Delete heal locations in each copy before its first save.** Exact steps, per map:

1. Open the vanilla source map.
2. File > Duplicate Current Map.
3. Name it as in the table. The group is `gMapGroup_IndoorLittleroot` for now; I will tell you if a different group is better. Location stays `MAPSEC_HOLLOWBROOK` so the town name shows indoors.
4. Events tab: delete every Heal Location event. Leave the rest.
5. Save (Ctrl+S).

I clean the leftover events and re-point the warps after you push.

### 3.3 Route 1
1. Open `Route101`.
2. File > Duplicate Current Map.
3. Name `VeldrisRoute1`. Group `gMapGroup_TownsAndRoutes`. Location `MAPSEC_VELDRIS_ROUTE_1`.
4. Change Dimensions to **60 x 25**.
5. Delete heal locations (Route 101 has none; check anyway).
6. The copy has no connections, which is right: you make them in Part 5.

### 3.4 Making the lab table four wide
Open the lab map. The vanilla table is the long desk on the right with the red ball machine. Copy a table segment: Metatiles tab, find the table tile pieces, and paint the table until it is **at least 4 tiles wide**, with one free floor tile **in front** of each ball spot (the player stands there to interact). Place the table against the top wall, centred, so the player can walk up to it. Then open the Collision tab and mark the table tiles blocked.

---

## Part 4: Painting (the skills)

### 4.1 Tools
| Tool | Key | Does |
|---|---|---|
| Pencil | `N` | Click or drag to paint the selected metatile |
| Bucket | `B` | Fill a connected region. Ctrl + click fills every matching metatile in the map |
| Eyedropper | `E` | Click a tile to pick it. Right-click-drag in the map copies a rectangle **with collision and elevation**. This is how you copy a whole house |
| Smart Paths | checkbox, or hold Shift | With a 3 x 3 outline selected, edges and corners fill in automatically. Use for paths and the pond |
| Undo / Redo | Ctrl+Z / Ctrl+Y | Works while Porymap is open |

### 4.2 The working rhythm for a village
1. **Fill the whole map with the background** first (bucket with plain grass).
2. **Forest border:** fill the outer rows with the tree tile. Leave the gaps where routes leave the town.
3. **Paths:** Smart Paths with the path outline. Trace from the picture.
4. **Pond:** Smart Paths with the water outline.
5. **Buildings last.** Copy from the vanilla maps with the right-click copy (houses from Littleroot, the lab style from Petalburg's or Littleroot's lab exterior). Paste with left-click.
6. **Decoration:** flowers, fences, signs' tiles.

### 4.3 Collision and elevation (do this every time)
1. Click the **Collision** tab in the right panel.
2. The map now shows the collision overlay. Walkable tiles show nothing special, blocked tiles show a red-ish pattern.
3. Paint **Collision 1, Elevation 3** on walls, trees, water and fences. Paint **Collision 0, Elevation 3** on everything the player should walk on.
4. **Elevation 3 everywhere the player can walk.** Especially the area added by Change Dimensions (elevation 0 there) and especially the tiles where I will put cutscene triggers.
5. Click back to the Metatiles tab to keep painting.

**Quick check:** walk the player's route in your head: house door > path > lab door > route exit. Every tile on it should be elevation 3, collision 0.

### 4.4 What you will not get
Pine trees, green roofs, pale-green paths, and the grey-brick lab are not in our tilesets. Use the nearest (round trees, orange roofs, light grass). Do not draw new tiles. If you want the closer look later, that is a separate decision (map-plan.md).

---

## Part 5: Events, and what is yours versus mine

The Events tab shows the object buttons (NPC, Warp, Trigger, Sign, Hidden Item, Heal Location and so on). Click one, then click the map to place it. Select an event to edit its fields in the panel on the right.

**My suggestion: you paint, I place events.** After you push, I write every warp, sign, NPC, trigger and ball into `map.json` from the list in Part 6, and you then reload. This avoids typing into Porymap's event fields (which has no undo). If you want to place them yourself, the fields are:

| Event | Fields you set |
|---|---|
| **Warp** (door) | X, Y, Elevation 3, Destination Map, Destination Warp ID. Put it on the door tile and **make a matching warp on the other side**. Warp IDs are list positions: do not delete or reorder |
| **Sign** | X, Y, Script label (for example `Hollowbrook_EventScript_TownSign`) |
| **NPC (object)** | X, Y, Graphics (sprite), Movement type, Script label, Flag (hide flag, if any), Trainer type if a trainer |
| **Trigger** (coord event) | X, Y, Elevation **3**, Var, Var Value, Script. Tile must be walkable at that elevation |
| **Heal Location** | Do not add one by hand. I wire those (two traps, see CLAUDE.md) |

**Connections (Route 1 to Hollowbrook):** Connections tab on Hollowbrook: click **+**, choose direction (Right, for the east exit), map `VeldrisRoute1`, set the offset so the two openings line up. Leave 'Mirror to Connecting Maps' ticked. Then use **File > Save All** (Ctrl+Shift+S). Until Wendlebury exists, Route 1's far end stays open or blocked by trees.

---

## Part 6: Where everything goes

All coordinates are (x, y) in tiles, origin top-left, **approximate**. Confirm each with the status bar before placing.

### 6.1 Hollowbrook (32 x 28), from `New Bark Town.png`

```
 x: 0         10        20        30
y0  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   trees all around the edge
y6       [  LAB  ]   
y8  sign  [ door ]     [ GOLDSWORTH ]        Lab approx x9-16, y6-10
y10        ...path...   [  house  ]          Goldsworth approx x19-24, y8-12
y12                              ~~~~~~      Pond approx x26-31, y12-17
y16              (town sign)    ~~~~~~
y17   [PLAYER]                               Player house approx x6-11, y17-20
y18   [ HOUSE ]      [NEIGHBOUR]             Neighbour approx x16-21, y18-21
y27  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  (bottom edge stays solid trees)
                                         exit gap to Route 1 on the RIGHT edge, approx y9-10, north of the pond
```

| Thing | Approx position | Notes |
|---|---|---|
| Professor Fennick's lab | x9-16, y6-10 | Door on the bottom wall near x12. Lab sign just left of it, about (8, 9) |
| Goldsworth house | x19-24, y8-12 | Door bottom centre. Locked with the note until the post-game. Sign beside it |
| Bench (the old man) | just outside the Goldsworth door, about (22, 13) | Paint a bench or use an NPC sitting. He shows only after the lab scene |
| Town sign | about (14, 16) | Text: `Hollowbrook_Text_TownSign` |
| Player's house | x6-11, y17-20 | Door bottom wall. Sign beside it |
| Neighbour's house | x16-21, y18-21 | Door bottom wall |
| Pond | x26-31, y12-17 | Blocked collision. Fence along the bottom edge |
| Exit to Route 1 | a 2-tile gap in the forest on the **right (east) edge**, approx (31, 9) and (31, 10), north of the pond | Author-decided 2026-09-30. Extend the path to it. Connection: direction **Right**. The bottom edge stays solid trees |
| Ambient Pokémon (three) | on the paths, about (12, 12), (18, 15), (10, 15) | Normal-type stand-ins, see dialogue file |
| Farmer, kid, laundry woman | the open grass west of the pond, and beside the neighbour's house | Positions are loose, put them where they look right |
| **Troglodyte trigger** | on the path just **outside the lab door**, about (12, 11), elevation 3 | `coord_event` on the tile the player must cross after leaving the lab |

NPC and dialogue labels are all in [dialogue/hollowbrook.inc](dialogue/hollowbrook.inc). The grandfather's timeline is in [story-outline.md](story-outline.md).

### 6.2 Player's house (1F and 2F)
Keep the vanilla layout. After the copy:
- 1F: the mom NPC stands by the table, the door warps to Hollowbrook, the stairs warp to 2F.
- 2F: the bed/player start. Nothing to paint.
- I re-point every warp. You do not need to edit them.

### 6.3 Fennick's lab (from `Elm's Lab.png` and the vanilla lab)

```
   bookshelf bookshelf  [computer]
        [ TABLE, 4+ wide, ball ball ball ball ]
        (free floor in front of each ball)
   aide                          aide
   bookshelf                     bookshelf
                [ door mat ]
```

| Thing | Notes |
|---|---|
| Table | At least 4 wide, centred on the top wall (Part 3.4) |
| Four Poké Ball spots | One per tile of the table's top row. I place the ball objects |
| Fennick | Standing behind the table |
| Two aides | One each side, about two tiles in from the walls |
| Bookshelf and computer | Keep vanilla. Their texts are in the dialogue file |
| Door | Bottom centre mat, warps to Hollowbrook's lab door |

### 6.4 Route 1 (60 x 25), from `Route 29.png`
- Runs **east-west**: Hollowbrook on the west end, Wendlebury on the east end (PROPOSED, see towns-and-routes.md). Hollowbrook's exit is on its right edge (author, 2026-09-30), so Route 1's **left** edge joins it: make the opening on Route 1's west edge at the same height (about y9-10 on Hollowbrook; set the Connections offset so they line up).
- Keep the tall-grass patches where the picture shows them; these are the wild-Pokémon tiles. Everything Normal-type, gentle.
- Ledges (the one-way hops) are metatiles with a ledge behavior. Copy them from `Route101` rather than painting new ones.
- Leave 2 or 3 spots for trainers. I place them.
- Elevation 3 on all walkable ground, collision on trees and water.

### 6.5 Map section and name popups
The town name popup uses `MAPSEC_HOLLOWBROOK` from the header. If it says Littleroot, open the **Header** tab and fix Location. I also check this after every push.

---

## Part 7: Saving and sending it to me

1. **Ctrl+S** saves the current map and shared data. **Ctrl+Shift+S** saves every open map. Do it often.
2. Look at the changed-files list in GitHub Desktop. Expected: new folders under `data/maps/`, new entries in `data/layouts/layouts.json`, `data/maps/map_groups.json`, one new line at the end of `data/event_scripts.s`. Also expected, and harmless: `region_map_sections.json`, `heal_locations.json`, `wild_encounters.json` rewritten, and a large reorder in the FRLG part of `layouts.json`. **If anything else changed a lot, tell me before you commit.**
3. **Never** commit `.gba`, `.sav`, `.srm` or `.sgm` files.
4. Commit to `claude/pokemon-pot-setup-evpysj`, push, and message me the map names.
5. **Close Porymap** (or File > Reload Project) whenever I say I am editing a `map.json`.

## Part 8: Common mistakes

| Symptom | Cause | Fix |
|---|---|---|
| Player walks through a house | Collision is 0 on the walls | Collision tab, paint 1 |
| Player cannot step onto new ground | Elevation 0 from Change Dimensions | Repaint elevation 3 |
| Cutscene never fires | Trigger tile has wrong elevation or is blocked | Elevation 3, collision 0 |
| Build error 'duplicate heal location' | Heal locations copied by Duplicate Map survived | Delete the copies, tell me |
| Door does nothing | Warp not on a door tile, or no matching warp back | Tell me, I check |
| Name popup says Littleroot | Header Location unchanged | Header tab |
| Porymap shows `*` and asks about reloading | File changed on disk after a pull | Answer Yes |
| A wall of red text when the build runs | Usually a bad map or a missing include | Send me the error |

## Part 9: Suggested order of work

1. Smoke test (porymap-first-map.md, Step 1).
2. Hollowbrook exterior, rough: border, paths, pond, buildings. Push.
3. Collision and elevation pass. Push.
4. Interiors as plain duplicates (player's house, neighbour). Push.
5. The lab with the four-wide table. Push. **Tell me, and I wire the lab scene, balls and Troglodyte's first fight.**
6. Route 1, rough, then connect it. Push.
7. Goldsworth house last (post-game only).

You can stop after any step. I build and send a ROM so you can walk what exists.
