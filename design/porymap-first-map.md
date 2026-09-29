# Porymap: your first map (Hollowbrook)

For the author. Plain steps for someone who has never used Porymap. Status: **PROPOSED** (nobody has run this loop yet).

**How this was written.** From Porymap's own manual and source code (release 6.3.1, read on 2026-09-29) and from this repo. Porymap was **not run**, and the time estimates below are **estimates, not measurements**. If a step does not match what you see on screen, tell me and I will fix this file.

## The idea in three lines

1. You paint the map in Porymap on your own computer, then commit and push it to GitHub.
2. I pull it, do the warps, scripts, dialogue and wiring, build the ROM in the cloud and send it to you.
3. You play it in your emulator and tell me what is wrong. You never need a compiler.

## One-time setup (about 1.5 to 4 hours, mostly git and reading)

1. **Install GitHub Desktop** (or plain git) and sign in as `24rousol-hub`. Reading a public repo needs no login, pushing does.
2. **Clone** `24rousol-hub/Veldris` (File > Clone repository). It is about 141 MiB, so the first clone takes a few minutes. Keep the folder on a normal drive, not inside OneDrive or another synced folder.
3. **Switch to the branch** `claude/pokemon-pot-setup-evpysj` (Current Branch menu). Work on this branch only.
4. **Get Porymap** from the releases page: https://github.com/huderlem/porymap/releases. Windows and macOS need no installer, you unzip and run it. If there is no Windows zip, tell me. Linux would need building from source.
5. **Open the project:** File > Open Project, and pick the repo's root folder (the one that contains `data/`, `src/` and `include/`).
6. **First-launch question.** Porymap guesses the game from the folder name, and `Veldris` does not say emerald, so it will ask. Choose **pokeemerald**. If it says 'Your project may be incompatible', click **Try Anyway**.
7. **Check three settings** once, in Options > Project Settings: 'Use Poryscript' stays **off**, 'Create separate text file' stays **off**, 'Enable Custom Border Size' stays **off**.
8. **Learn the basics** by doing the manual's own first edit (pencil tool, click a metatile, click the map, Ctrl+S), then read the short manual pages: navigation, editing map tiles, editing map collisions, editing map events, editing map connections. About 30 to 45 minutes. Manual: https://huderlem.github.io/porymap/

## Every sitting

1. **Pull first.** In GitHub Desktop: Fetch origin, then Pull origin. Do this with Porymap **closed** (or use File > Reload Project afterwards). Two Claude sessions also push to this branch, so it moves under you. Porymap does not notice when a pull changes a `map.json`.
2. Open the project in Porymap and work.
3. **Save often.** Ctrl+S saves the current map and the shared data files. Ctrl+Shift+S saves every open map, which you need after editing connections on two maps. The title bar shows `*` when something is unsaved.
4. **Look at the changed files before committing.** Expect the new map's folders under `data/maps/` and `data/layouts/`, `data/layouts/layouts.json`, `data/maps/map_groups.json` and `data/event_scripts.s` (one appended `.include` line). Porymap also rewrites `src/data/region_map/region_map_sections.json`, `src/data/heal_locations.json` and `src/data/wild_encounters.json` on every save. If one of those changed a lot and you did not touch it, tell me before committing.
5. **Commit and push** to `claude/pokemon-pot-setup-evpysj`. Then tell me it is pushed, so I pull before I touch anything. If the push is rejected because I pushed first, pull again and push again. Only one of us should edit a given map at a time, because a map's block data cannot be merged.
6. **Close Porymap** (or reload the project) before I edit any `map.json`, and I will say when I do. Porymap does not watch `map.json`, and its next save would silently erase my change.

## Never commit a ROM or a save

No `.gba`, `.sav`, `.srm`, `.sgm` or emulator save-state files, ever. `.gitignore` blocks them (with three helper `.gba` files under `data/` allowed). The safety hook I use lives inside my own copy of the repo and is **not** on your computer, so only `.gitignore` protects you. Do not use 'force add'. If a `.gba` ever shows in the changed-files list, stop and ask me.

## Step 1: a smoke test (about 45 minutes to 2 hours)

Before you spend hours painting, prove the whole loop with a tiny change. Do it on the real map, so nothing is thrown away:

1. Open `LittlerootTown`. Choose **File > Duplicate Current Map**.
2. In the dialog: Map Name **`Hollowbrook`** (this gives `MAP_HOLLOWBROOK`), Location **`MAPSEC_HOLLOWBROOK`** (I added it already, it is in the dropdown), Map Group **`gMapGroup_TownsAndRoutes`**. **Leave the size alone.** Leave **Can Fly To unchecked**. Never type new sizes into this dialog: resize afterwards with the Change Dimensions button.
3. Change a dozen tiles (move a tree, add a path), then save.
4. Commit and push, then tell me.

I pull, clear the Littleroot events out of the copy (see below), build, and send you a ROM. This tells us the whole loop works while the stakes are low.

## Step 2: Hollowbrook (the real thing)

Reference: `Maps/Project Palladium/New Bark Town.png` in the asset repo. It is exactly 512 x 448 pixels, which is 32 x 28 tiles of 16 pixels, with no grid lines. The vanilla `LittlerootTown` is only 20 x 20.

- **Resize** with **Change Dimensions** (drag the edges or type 32 and 28). The new area arrives empty, with metatile 0, no collision and **elevation 0**. Normal ground is elevation 3, so repaint the new area in both the Metatiles and the Collision tabs.
- **Paint.** Click a metatile in the Metatile panel (drag to pick a block), then click or drag on the map with the pencil (`N`). The bucket (`B`) fills a region. Hold Ctrl with the bucket to fill every matching metatile, which is good for tree backgrounds. The eyedropper (`E`) or right-click-drag copies a rectangle **including collision and elevation**, which is how you copy a whole vanilla house. Smart Paths handle path and pond edges when you pick a 3 x 3 outline.
- **Collision matters.** The picture and the collision are separate. A house painted from the Metatile panel is walk-through until its walls get an impassable collision. Open the **Collision** tab after every building and pond and look for the red pattern on walls and water rims.
- **Buildings.** Copy the vanilla ones by right-click-dragging over them in another map, then paint. Prefabs (a tab next to Metatiles) hold ready-made buildings such as the Poké Mart.
- **Connections.** Routes join maps in the Connections tab (plus button, direction, offset). They are one-way, so tick 'Mirror to Connecting Maps' and then Save All.
- **Warps** (doors): Events tab, add a Warp, put it on the door tile, set the destination map and warp id, and make the return warp on the other side. It is fine to leave the warps to me: I can write them into `map.json` after you push.
- **Commit after every sitting.** Undo history only lasts while Porymap is open, and typing in the event fields has no undo at all. Git is your real undo.

**What the copy still contains.** A duplicate copies every event from the original: LittlerootTown's 8 NPCs, 3 warps, 9 triggers and 4 signs, all pointing at Littleroot scripts and flags, and the header still says `MAPSEC_LITTLEROOT_TOWN`. I strip those and set the header once you push. A duplicate does **not** copy connections.

## Interiors and shared layouts

- **Pokémon Center and Mart:** in the New Map dialog, pick an **existing Layout ID** (`LAYOUT_POKEMON_CENTER_1F`, `LAYOUT_POKEMON_CENTER_2F`, `LAYOUT_MART`). Nothing to paint. But painting in one then changes every map that uses that layout.
- **Goldsworth houses:** the same trick, one shared layout for all of them. See [map-plan.md](map-plan.md).
- **Houses and Fennick's lab:** Duplicate Map from the vanilla ones and keep them as they are for now. I re-point the warps. Repaint later if you want to match the Palladium pictures.
- **Tilesets:** never pick an FRLG tileset for a new map. This Emerald build skips them. Indoor maps take walls and floors from the secondary tileset.

## Pitfalls, short list

- **Map size limit:** `(width + 15) * (height + 14)` must be at most 10240. All planned sizes are far inside it, and Porymap enforces it.
- **A house painted from the panel has no walls** for the player until you set collision.
- **Elevation must match.** The player cannot step between elevations, and a trigger on a tile of a different elevation never fires.
- **Warps are one-way** and need a door-type tile. Warp ids are list positions, so deleting or reordering warps changes numbers other maps point to.
- **Never use the lock button in the map list** to reorder map groups. The `AA` in `[AA.BB]` is the group number that warps use.
- **The border** (what shows past the map edge) is only 2 x 2 tiles here. Toggle the Border checkbox to see and edit it.
- **The tile look:** Palladium's pine trees, green roofs and pale paths do not exist in the tilesets we have. See 'How close vanilla tiles get' in [map-plan.md](map-plan.md).

## How long will it take? (an estimate)

I could not run Porymap and nobody timed a first-time user, so these are counted from the number of tiles and steps. They assume you start from a duplicate, keep the tileset in the tree, and I do the events, scripts and wiring.

| Task | Estimate |
|---|---|
| Setup and learning the basics (install, clone, branch, open, the manual's first edit, the short pages) | 1.5 to 4 hours |
| Smoke test (duplicate, a few edits, commit, push, one round trip with me) | 45 minutes to 2 hours |
| **Hollowbrook exterior**, 32 x 28 (896 tiles), from a Littleroot duplicate | **5 to 11 hours**, in several sittings |
| One vanilla interior kept as a copy | 10 to 30 minutes |
| Pokémon Center or Mart with a shared layout | 5 to 15 minutes |
| One interior repainted to match a Palladium picture | about 45 minutes to 3.5 hours |
| A route from a vanilla copy (Route 1 is 60 x 25) | 3 to 8 hours |
| **First milestone in total** (setup, smoke test, Hollowbrook, and the vanilla interiors kept as copies) | **about 8 to 19 hours**, in 3 to 6 sittings |

**What moves the numbers:** how faithfully you trace (positions only, or tile by tile); whether you want new tiles (not estimated, since you do not plan to draw); collision and elevation mistakes, each of which costs one build-and-test loop with me; and git friction the first time. The first hour of Porymap is far slower than the fifth, and I would guess the second map takes about half as long as the first.

**Keeping the first try small:** get Hollowbrook playable with rough trees and paths first, keep every interior as a plain vanilla copy, then test and refine.

## Testing your map

I send you a ROM. If you would rather test between rounds, the ROM has a debug menu (open it with R+START in the emulator). It has 'Warp to map warp…' (map group, map number and warp id), 'Set Flag', 'Toggle All badges' and 'Fly to map'. Hollowbrook lives in map group 0 (`gMapGroup_TownsAndRoutes`); its map number is in `include/constants/map_groups.h` after a build, and I will tell you.

## What to send me when a sitting is done

Say that it is pushed, and which maps you touched. Mention anything odd you saw, especially any warning Porymap showed.
