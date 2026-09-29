# Asset inventory

What is usable in `24rousol-hub/Team-Aquas-Asset-Repo` and `24rousol-hub/sprites` for this hack. Inventoried by read-only agents, then **each inventory was independently re-checked against the real files by a second agent**. The verdicts below are the corrected ones. Nothing has been imported, built or loaded in Porymap yet.

## The short version

| Kind | Best usable | Verdict |
|---|---|---|
| **Maps** | None. The repo has **no importable Porymap maps** | The `Maps/` folder is screenshots only (no `map.json`, no `map.bin`). The tree itself holds every vanilla Hoenn map to copy and rework in Porymap |
| **Tilesets** | `Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS` | **Yes.** Emerald dual-layer, same slots as vanilla, drop-in |
| | `.../Valencia Island` (FRLG format) | Maybe. Format fits, permission is weak |
| | `.../Small town with lab Secondary` (best farm look) | Maybe, and **blocked**: triple-layer, needs an engine patch (ask first) |
| **Sprites** | `Overworld Trainer Sprites/RavePossum/Poffin-Case-Overworlds-Converted` | **Yes.** 130 NPC sheets in vanilla filenames, drop-in. Has `prof_birch`, `rich_boy`, `old_woman` |
| | `Trainer Front Sprites/Pawkkie` and about 75 more single-creator 64x64 fronts | **Yes.** Indexed 16-colour, convert as they are |
| | `Overworld Trainer Sprites/spilledpizza` (DP rancher, cowgirl, socialite, rich boy) | Maybe. Best low-effort farm cast, official-derived |
| **`sprites` repo** | Almost nothing | Pokémon art only. The Emerald Gen 3 art **is already in the tree**, one config switch away |
| **Other** | Cookie Softcore HM icons, Lhea type icons, RavePossum battle backgrounds, Lykae `farm_tune` | Small, mostly drop-in, credit needed |

## Read this before importing anything: the repo is PUBLIC

Almost everything here is **derived from official Nintendo / Game Freak art** (redraws, recolours, rips) or from **other fan games**. Committing converted copies to a public repo publishes them. Upstream expansion already ships a lot of official art, so this is a matter of degree, and it is your call. The safe course is to import only assets with a clear free licence or the creator's permission, and label the rest `official` in `CREDITS.md`. Your rule stands: **no maps from other hacks without the author's permission.**

## Maps

- **`Maps/Project Palladium`** (127 PNGs, 1 GIF): Johto layouts from a cancelled GSC remake. Screenshots only. The README says the team released everything for free use and asks for the whole team to be credited, **but its source URL is dead**, several files have other authors (for example `lostimpact`) or none, and the layouts are Game Freak's. **Permission is unresolved, so treat as look-only.** Useful facts: 56 of the images are 17N+1 by 17M+1 pixels, which is 16 px tiles with a 1 px grid line (all 16 routes, Cianwood, `bobhx7.png`). Stripping every 17th row and column would probably recover tile-exact layouts (untested).
- **`Projects/Leob0505 PokeZelda Minish Quest`**: no map data. The map renders are look references. `5 - PetalburgCity_new.png` is 480x480, the vanilla 30x30 Petalburg size. Zelda art, includes a rupee icon.
- **`Projects/FFVII_Sprites`**: Square Enix IP, wrong setting. No.
- **Practical route for towns 1 to 3:** duplicate vanilla maps already in this tree (Littleroot, Oldale, Route 101, Petalburg) in Porymap and rework them. Nothing to credit beyond upstream.
- **Are community maps still the plan? Yes.** The rule stands: reuse existing community maps and tilesets instead of drawing from scratch, with credit, and never another hack's maps without the author's permission. But the two repos hold **no importable maps**, so the next step is to look for free-to-use community map resources elsewhere (a stated licence or the creator's permission), record what is found here, and add a `CREDITS.md` row for anything used. Until then, use the vanilla maps in this tree.

## Tilesets

This engine draws **dual-layer** metatiles only (`NUM_TILES_PER_METATILE` is 8, checked in `include/fieldmap.h`). Most of the Great Tileset Exchange is **triple-layer**, so it needs the pret triple-layer patch (a big engine edit) or flattening per set.

| Set | Format | Verdict |
|---|---|---|
| `Full Tilesets/LeoB ORAS` | Emerald dual-layer, same metatile counts as vanilla | **Yes.** ORAS-style edit of Game Freak's Emerald tiles. Credit leob0505 (inspired by TheDeadHeroAlistair). Folder has only `credits.md` |
| `Full Tilesets/Valencia Island` | FRLG format (supported natively) | Maybe. Permission is a Discord screenshot between other people. Credit Kalarie and all five tile artists on the credits image. **Do not use its example map.** Primary needs a secondary with palette 7 |
| `Other Tilesets/Pokemon Crystal - G2S_Ports` | Emerald dual-layer, GBC art | Maybe. Official Game Freak art, style mismatch, attributes incomplete |
| `Full Tilesets/Small town with lab Secondary` | Triple-layer | Maybe, **blocked**. Best farm look (crop plots, pond, fences, dock). Ekat's non-commercial terms, possible FRLG/RSE rips |
| `Individual Tiles/Rahtak`, `KyuZee` | Indexed tile sheets / RGBA fence | Maybe. Trees, greenery and a fence to paste into a tileset. Credit FM, Zeikaro, Rahtak / KyuZee |
| `Projects/Leob0505 .../datafolder_tilesets` | 7 Emerald-style tilesets | Maybe. **Not self-contained:** the primary's tile and palette slots depend on the matching secondary. Full Zelda restyle, Zelda IP, 8 people to credit |
| `Other/Pokemon LIFE/tilesets` | AdvanceMap FRLG format, not Porymap-ready | Maybe. Another hack's assets. Only `mainTileset REVAMP` says 'feel free to use it'. Needs conversion and the author's permission |
| Sets built from Reborn, Rejuvenation, Glazed, Dawn (Caves Alt, Dojo, Shady Forest, Gen 4 Interior and others) | Triple-layer | **Avoid** in a public repo. Other fan games' art, no permission noted |
| `Desert Pyramid Exterior Secondary`, `Hidden Grotto Primary FRLG` | Broken or mixed | **No.** Traps: empty metatile data, mixed formats |

## Sprites

**NPC overworlds and trainer pictures**

- **RavePossum `Poffin-Case-Overworlds-Converted`:** 130 sheets under vanilla filenames, and sizes match vanilla. **Use `prof_birch` for Prof. Fennick, `rich_boy` for Troglodyte, and `old_woman` for Greta** (a grey-haired old woman in FRLG style; `hyo/old_woman.png` is another). Derived from official RSE sprites. Credit Poffin_Case and RavePossum. The README's `field_effect.c` note applies only to the `brendan/` and `may/` folders, so skip those and no engine edit is needed.
- **`hyo`, `Kasen`:** alternative FRLG-style sets. Player sheets and extra characters need extra object-event entries.
- **Farm cast, lowest effort:** `spilledpizza` `DP_rancher`, `DP_cowgirl`, `DP_socialite`, `DP_rich_boy` are indexed and need no re-indexing. Official DPPt-derived, and the credits mix in other hacks. Delta231's HGSS rancher and cowgirl are RGBA and `gbagfx` rejects them.
- **Greta's front picture:** no old-woman-farmer front exists anywhere. Stand-ins: `DP_Rancher` or `DP_Socialite` (an elderly woman). Otherwise custom art.
- **Route trainers:** `Trainer Front Sprites/Pawkkie` (26, HGSS-derived, 64x64 indexed) and about 75 more in the single-creator folders.
- **Avoid:** `Rahtak` followers (expansion already ships an `overworld.png` for 1025 species), `kwenio` (unknown creator, heavy recolouring), `Poffin_Case` originals (truecolour, superseded), `SurfingPokemon` (needs C injection), `Pokemon LIFE` overworlds (other hack, official Unova characters), Pokémon Essentials packs (wrong engine).

**Pokémon:** Fakemon in `Pokemon/Fakemon` are in the expansion folder layout. `Nico/Calfling` is a calf that would suit Greta's farm.

## The `sprites` repo (PokeAPI fork)

Pokémon art only: no maps, tilesets, overworlds or trainers. **It adds almost nothing.**

- **Gen 3 Emerald art (64x64, 16 colours) is already in this tree.** `P_GBA_STYLE_SPECIES_GFX`, `P_GBA_STYLE_SPECIES_ICONS` and `P_GBA_STYLE_SPECIES_FOOTPRINTS` in `include/config/pokemon.h` (all currently FALSE) switch to it. It is a config switch, not an import.
- **FireRed/LeafGreen Gen 1** fronts and backs: 141 of 151 fronts differ from what the tree ships, and they need no conversion. An alternate Kanto look only. Maybe.
- **Gen 5 item icons** (583, 24x24 indexed): maybe. The rest are recolours of icons the tree already has.
- **Everything else** (Gen 4 and up, 3D renders, animated GIFs) is the wrong size or true-colour. No.
- **Licence:** `LICENCE.txt` line 1 says all images are Copyright The Pokémon Company, and line 3 says the repository is CC0. CC0 grants no rights in the artwork, and section 4(c) says nobody cleared them. So there is **no licence for the art**. Personal use is your own risk call, not a permission. The Black/White-style sprites above ID 650 are fan-made (Smogon community spriters, given to PokeAPI to serve, not to hack authors).

## Other assets

| Asset | Verdict |
|---|---|
| `Items/Cookie Softcore` (6 HM icons, 24x24 4bpp) | Yes. Exact match for item icons |
| `User Interface/Lhea/Modern-Style Type Icons` | Yes. 32x16, drop-in |
| `User Interface/Kaixer` | Maybe. Type icons lack `none` and `stellar`. Badge sheet replaces `graphics/trainer_card/badges.png` (8 badges only) |
| `Battle Backgrounds/RavePossum`, `PurrfectDoodle` | Maybe. Not every folder has the full file set, some need palette trimming. Derived from Ruki's HGSS/DPPt ports |
| `Audio/Lykae/farm_tune` | Maybe. Technically fits (converts with `mid2agb`). **Originality is unstated**, and its `voicegroup191` clashes with another pack's |
| `User Interface/Fonts/PurrfectDoodle` (FRLG font) | Maybe. Two glyphs (a star and a triangle) are blank in it |
| Other audio (`nmm-lequietriot`, `jorts`, `nehochupechatat`, others) | Arrangements of official or other games' music. Personal use only, some need sound-engine changes |
| `Other/Pokemon LIFE` (rest) | No. Another hack's story and art, no licence, mixes in Ragnarok Online art |

## Suggested starting kit for the first 3 towns and 3 routes

1. **Maps and tiles:** copy vanilla maps and use the tree's own tilesets, or restyle with **LeoB ORAS** (drop-in). Farm feel: paste in KyuZee's fence and Rahtak's greens.
2. **Cast:** RavePossum's `prof_birch`, `rich_boy`, `old_woman`, plus `DP_rancher` and Pawkkie fronts for route trainers.
3. **Music:** Lykae's `farm_tune`, once someone confirms it is original.
4. **Decision needed:** the triple-layer engine patch unlocks the best farm tilesets but is a multi-file engine edit.

## Not checked

Nothing was built, loaded in Porymap, or run in an emulator. Only a sample of each large folder was opened (for example about 14 of the 127 Palladium images). Per-species READMEs in `Pokemon/` were mostly unread. The Pokémon LIFE forum thread could not be opened (the host is blocked by the network policy).

## Rules for using any asset

- Reuse existing maps and tilesets before drawing anything new.
- Every asset that comes from outside this repo gets an entry in [`CREDITS.md`](../CREDITS.md) in the same commit.
- Do not use maps from other hacks without the original author's permission.
