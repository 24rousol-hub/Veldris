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

- **`Maps/Project Palladium`** (127 PNGs, 1 GIF): Johto layouts from a cancelled GSC remake. Screenshots only. The README says the team released everything for free use and asks for the whole team to be credited, **but its source URL is dead**, several files have other authors (for example `lostimpact`) or none, and the layouts are Game Freak's. **The author decided on 2026-09-29 to rely on that README and use these maps as tracing references** (see [map-plan.md](map-plan.md)), with the whole team credited. The provenance caveats above still stand, so a few files are left out. Useful facts: 56 of the images are 17N+1 by 17M+1 pixels, which is 16 px tiles with a 1 px grid line (all 16 routes, Cianwood, `bobhx7.png`). Stripping every 17th row and column would probably recover tile-exact layouts (untested).
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


---

## Free community map and tileset resources beyond the two repos (PROPOSED, nothing used)

Searched 2026-09-29 by a read-only agent. **Nothing was downloaded and nothing is approved for use.** Licence text is quoted from pages the agent fetched. Items marked "not read" were not. `CREDITS.md` currently links the asset repo as `Pawkkie/Team-Aquas-Asset-Repo`, while the agent read `TeamAquasHideout/Team-Aquas-Asset-Repo`: the author should confirm which is the right upstream link.
Researched 2026-09-29. Nothing was downloaded into /home/user/Veldris. "Read" means I fetched the page and quote it; "snippet only" means I saw it only in a search-result summary.

### Headline finding

**No Porymap-ready free maps with a stated licence were found.** I found no public repo of importable Gen 3 `map.json` maps under a stated licence, and no hack author's permission. GitHub repo search ("pokeemerald tileset porymap", "gen3 tilesets porymap") returned only Porymap itself. The only Gen 3-format tilesets found are on Team Aqua's Hideout's Great Tileset Exchange (already covered in `design/asset-inventory.md`), and none of those carries a licence. So for maps the answer is unchanged: rework vanilla maps in the tree, or draw in Porymap.

Free **generic** 16x16 tilesets with real licences (CC0 / CC-BY) do exist. They are not Gen 3 format: they need recolouring to a GBA 16-colour palette, splitting into 8x8 tiles, and conversion (Porytiles, MIT, can compile them). They are also not in Game Freak's style, so they would clash with the vanilla tiles unless redrawn.

### Table

| # | Resource | Link | Contains | Porymap-ready? | Licence / permission (quoted, where) | Credit terms | Lifted from other work? | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | Team Aqua's Asset Repo (upstream of the author's copy) | https://github.com/TeamAquasHideout/Team-Aquas-Asset-Repo | Sprites, tilesets, UI, music, from many creators | Some tilesets yes (see the Great Tileset Exchange), no maps | README (read): "All assets are both free to use and edit by default, but if any assets specifically mention _not_ being free to edit, please respect the author's wishes." | Credit to original creator; folder READMEs name creators | Yes, many entries derive from official or other-fan-game art (see `asset-inventory.md`). Not re-audited here | Already covered. Blanket licence is a repo norm, not a per-asset grant. Use per-folder README only |
| 2 | The Great Tileset Exchange (repo wiki) | https://github.com/TeamAquasHideout/Team-Aquas-Asset-Repo/wiki/The-Great-Tileset-Exchange | Community full tilesets | Yes, but all **triple-layer** (needs the pret patch, which this tree lacks) | Wiki page (read): "Credits are definitely still required." Only two criteria: "formatted to be readily inserted into pokeemerald" and credits included. It gives no licence and no check for ripped art | Credit each tileset's creators | Page does not say. Earlier inventory found Reborn, Rejuvenation, Glazed, Dawn and official rips in some sets | Per set only. Nothing new beyond `asset-inventory.md` |
| 3 | Team Aqua's Hideout wiki (46 pages) | https://github.com/TeamAquasHideout/Team-Aquas-Asset-Repo/wiki | Tutorials, tool links (Porymap, Poryscript, Porytiles), Sprite and Art Gallery, links to a "Relic Castle Resource Archive" | Not an asset host for maps | Home page (read): no licensing information on it. I did not open the other 44 pages | n/a | n/a | Reference only. I found no map resources there. Sub-pages **not read** |
| 4 | Porytiles | https://github.com/grunt-lucas/porytiles | Tool: turns RGBA tile art into `metatiles.bin`, attributes, indexed `tiles.png`, palettes | Produces Porymap-ready output | README (read): "released under the MIT license". This licenses the tool, not any art | None for output you draw yourself | No | Usable as a tool. Handy if a CC0/CC-BY tileset is adapted |
| 5 | Puny World Tileset, by Shade | https://merchant-shade.itch.io/16x16-puny-world | 16x16 overworld tileset | No. Needs conversion and a GBA palette | itch page (read): "Creative Commons Zero v1.0 Universal (CC0)"; "Feel free to use this for your game (commercially or not)"; "Feel free to creatively modify these sprites however you like"; "No need to give me credit but I would appreciate it :D" | Not required. Credit anyway | Not stated. It is described (snippet only) as a rework of a "Miniworld" base tileset. I did not open that source | Usable, with a CC0 grant. Style is not Gen 3 |
| 6 | Town Tiles, by Surt | https://opengameart.org/content/town-tiles | Small 16x16 fantasy town tiles (one 2.9 KB png) | No | OGA page (read): "License: CC0" | Not required, appreciated | No | Usable but tiny and medieval, so it is a poor fit for Veldris |
| 7 | 16x16 Town Remix, by Lanea "Sharm" Zimmerman (with Redshrike, Surt, Jetrel) | https://opengameart.org/content/16x16-town-remix | Town buildings and structures, castle start | No | OGA page (read): "CC-BY 4.0, CC-BY 3.0, OGA-BY 3.0" | Required: "Art by Lanea 'Sharm' Zimmerman, Stephen 'Redshrike' Challener, Carl 'Surt' Olsson, and Jetrel, for OpenGameArt.org" | Built on edits of Surt's and Redshrike's sets, credited | Usable with the credit line. Medieval look |
| 8 | Roguelike/RPG Pack, by Kenney | https://kenney.nl/assets/roguelike-rpg-pack | 1,700 16x16 assets: town/dungeon blocks, furniture, UI | No | Kenney page (read): "Creative Commons CC0" | Not required | No | Usable. Style is roguelike, not Gen 3 |
| 9 | Pokemon-like Top Down Tile Set, by maciaz | https://maciaz.itch.io/pokemon-like-top-down-tile-set | 37 floor tiles and 51 misc tiles (16x16), 3 houses, trees, 3 NPCs, 2 creatures | No | itch page (read): "You are free to use the assets from the pack in all your projects with credit. You are not allowed to modify and resell the contents in any form." | Required | Says "pokemon inspired" and "No generative AI was used". I did not check for official art | Usable with credit. "Not allowed to modify and resell" needs care: it is a personal, non-sold hack, but a public repo with edits is a grey area. Ask the creator before redistributing edits |
| 10 | AxulArt's Beach and caves tileset | https://axulart.itch.io/axularts-beach-and-caves-tileset | Cave, mountain, water, beach tiles (RPG Maker style) | No | itch page (read): "Creative Commons Attribution 4.0 International License"; "You can modify it to suit your own needs, as long as you give appropriate credit." | Required | Not stated | Usable with credit. Not GBA style. Useful only as reference or base for beach and cave tiles |
| 11 | OGA "CC0 Tiles & Tilesets" collection | https://opengameart.org/content/cc0-tiles-tilesets | Curated list of 90+ CC0 tilesets by n1ght4ngel19 | No | Page (read): a collection page. OGA says attribution and licence checking "remains your responsibility". Individual entries must be checked one by one | Per entry | Per entry | A finding aid only. I checked no individual entry beyond #6 and #7 |
| 12 | itch.io "pokemon" tileset tags (free and paid) | https://itch.io/game-assets/free/tag-pokemon | Lists The Pixel Nook GB Studio Overworld Tileset and Retro RPG buildings pack, maciaz, AxulArt | No | Listing page only (read). Licences are on each asset page; I read only #9 and #10 | Per asset | Per asset | Finding aid only. The Pixel Nook packs **not read**: licence unknown |
| 13 | pokeemerald-expansion tilesets and maps (already in the tree) | https://github.com/rh-hideout/pokeemerald-expansion | 129 secondary tilesets (Hoenn + FRLG), 5 primary (building, building_frlg, general, general_frlg, secret_base), 944 map folders in `data/maps` | Yes, native | CREDITS page (read): no art licence stated. `LICENSE` file: WebFetch returned 404 and the GitHub tool was denied (repo not in this session's allowlist), so **not read**. The tree has no LICENSE file at its root | Credit upstream once, already in `CREDITS.md` | These **are Game Freak's assets**, an official rip. Upstream ships them, but reuse in a public repo is the author's own risk call, as `asset-inventory.md` already says | Usable as-is in the tree. It is the only Porymap-ready set at zero extra work. Not "free licensed" |
| 14 | pret/pokeemerald | https://github.com/pret/pokeemerald | Vanilla maps and tilesets | Yes | Repo page (read): no licence statement visible. LICENSE not read (tool denied) | n/a | Game Freak assets | Same status as #13 |
| 15 | Porymap | https://github.com/huderlem/porymap | Map editor | n/a | Licence file: 404 on the path I tried, **not read** | n/a | n/a | Tool only. Has no sample map library that I found |
| 16 | Relic Castle Resource Archive | (no link) | Old Pokémon Essentials tilesets | No, Essentials format | Search result (snippet only): the archive stopped hosting in January 2019 | n/a | Essentials packs are usually official rips | **Do not use**. Wrong engine and dead |

### Not read (listed by URL only)

- PokéCommunity: not fetched, per instruction (403 to fetch tools).
  - https://www.pokecommunity.com/tags/tilesets/
  - https://www.pokecommunity.com/tags/tileset/
  - https://www.pokecommunity.com/threads/tile-inserting-animating-tutorial.422362/ (a tutorial, not a resource pack)
  - https://www.pokecommunity.com/threads/gen-4-hgss-tileset.421403/ (an HGSS tileset thread, so probably official rips. Contents unknown)
- Porymap docs and changelog pages: appeared in search only, not opened.
- Pixel Nook GB Studio Overworld Tileset / Retro RPG buildings pack (itch.io): only seen in a listing.
- The other 44 pages of the Team Aqua's Hideout wiki.
- The upstream `LICENSE` files of pokeemerald, pokeemerald-expansion and Porymap (see table).

### Things I could not find

- Any repo or thread with Porymap-ready **maps** under a stated licence or with the creator's permission. The searches turned up none. The Team Aqua repos hold tileset packs and screenshots, not maps.
- Any Aseprite-based GBA tileset with a licence. Not found in search.
- Whether the pokeemerald-expansion tree added anything new in tilesets. The tree's directories match what pret ships plus FRLG sets (`*_frlg`), which are official. FRLG map folders are not built into this ROM. I did not diff against pret to find expansion-only additions, so I cannot say none exist.
- The search tool gave answers in summary form. Only pages I fetched (marked "read") are quoted.

### Points to note

- `CREDITS.md` links the asset repo as `Pawkkie/Team-Aquas-Asset-Repo`. The repo I read is at `TeamAquasHideout/Team-Aquas-Asset-Repo`. The task and CLAUDE.md call it `24rousol-hub/Team-Aquas-Asset-Repo`. The URL in `CREDITS.md` may need checking.
- `/home/user/Veldris` currently contains a built `pokeemerald.gba`, `.elf` and `.map` at the root. `.gitignore` reportedly blocks them (rule 1), but confirm before committing.

### Recommendation

1. For towns and routes: rework vanilla maps in Porymap (no new credit needed beyond upstream).
2. For a farm look, the licensed options are #5 (Puny World, CC0), #8 (Kenney, CC0) and #10 (AxulArt, CC-BY), all as base art to be redrawn to a GBA palette (Porytiles can compile it). Expect a manual pass to match the Gen 3 style.
3. Anything from #9 needs the creator's OK before edited copies go into the public repo.
4. Add a `CREDITS.md` row per asset used, with the licence quoted from the page above.
