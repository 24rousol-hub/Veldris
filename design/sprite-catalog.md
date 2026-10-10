# Sprite catalogue

A read-only survey of the two sprite sources, counted with `find` on 2026-10-01 (PNG counts are real; sizes and modes were read with Pillow, by folder, so a few odd files per folder are not listed). Nothing was copied, imported or credited. This adds detail to [asset-inventory.md](asset-inventory.md) (verdicts and maps/tilesets) and [gym-leader-art.md](gym-leader-art.md) (the gym picks); it does not replace them. Everything here is a PROPOSAL until the author picks.

Paths are relative to `/home/user/Team-Aquas-Asset-Repo` (call it TAAR) unless marked `sprites/` (`/home/user/sprites`). In this catalogue 'P' means an indexed PNG (fits 16 colours if the palette has 16 or fewer entries), 'RGB/RGBA' means truecolour, which `gbagfx` rejects until it is re-indexed.

## GBA constraints used for the 'fits' column

| Kind | Size | Colours | Notes |
|---|---|---|---|
| Pokemon front / back | 64x64 (front is stacked frames, 64x128 in expansion) | 16 incl. transparent, 4bpp | Index 0 is the background colour |
| Pokemon icon | 32x64 (two frames) | 16 | One palette from the shared icon palettes |
| Overworld (people) | 16x32 frames, sheets 144x32 (9 frames) or 160x32 | 16 | Must use a vanilla palette slot or add one; 32x32 frames and 64x64 need object-event info edits |
| Trainer pic | 64x64 | 16 | In expansion, `Pic` entries in `trainers.party` |
| Trainer back pic | 64x64 per frame, sheets 64x256 (4 frames) or 64x320 (5) | 16 | |
| Item icon | 24x24 | 16 | |
| Battle terrain | 256x256 tiles, plus a 128x? entry and an animated palette | 16 | Several files per terrain |

## What the ROM already ships

- **Pokemon:** `graphics/pokemon/` has 1029 species folders. Default art is the Gen 4/5-style set (`anim_front.png` is 64x128, `back.png` 64x64, `icon.png` 32x64, `overworld.png` 192x32). The GBA-style set is already in the same folders (`anim_front_gba.png`, `back_gba.png`, `icon_gba.png`, `*_gba.pal`). Three switches in `include/config/pokemon.h`, all currently FALSE, pick it: `P_GBA_STYLE_SPECIES_GFX`, `P_GBA_STYLE_SPECIES_ICONS`, `P_GBA_STYLE_SPECIES_FOOTPRINTS`. A source with Pokemon art therefore only matters for Fakemon or redesigns.
- **People overworlds:** `graphics/object_events/pics/people/` has 161 PNGs (vanilla plus a few Veldris swaps such as `prof_birch.png`).
- **Trainer pics:** `graphics/trainers/front_pics/` has 194 files, 14 of them Veldris (`veldris_leader_*`, `veldris_elite_four_*`, `veldris_champion_cynthia`), all credited in `CREDITS.md`. Back pics are in `graphics/trainers/back_pics/`.
- **Items:** `graphics/items/icons/` has 619 icons at 24x24.

## Source 1: `/home/user/sprites` (PokeAPI sprites, 'PokeSprites')

Licence: `LICENCE.txt` line 1 says all image contents are Copyright The Pokemon Company; the repo is CC0 1.0. CC0 gives no right in the art, so there is no licence for the images. Credit norm: none stated. `CREDITS.md` already lists it as personal-use fan material. `CONTRIBUTING_SPRITES.md` says the default `sprites/pokemon/` set is meant to be Gen 5 style.

| Path (under `sprites/sprites/`) | Holds | Count (files) | Size and format | Style | GBA fit |
|---|---|---|---|---|---|
| `pokemon/` (root numbered files) | Default front/back/shiny/female per form | 87,902 files under `pokemon/` in total | 96x96 P | Gen 5 (BW) style | No. Wrong size, more colours; the ROM already has this style |
| `pokemon/versions/generation-iii/emerald` | Emerald front/back/shiny | 3,348 PNG | 64x64 P | Official GBA | Yes, as is. Already in the ROM as `*_gba.png`. Use only to compare |
| `.../generation-iii/firered-leafgreen`, `ruby-sapphire` | FRLG and RS fronts/backs | 1,676 and 1,671 PNG | 64x64 P | Official GBA | Yes as is. FRLG Gen 1 art differs from Emerald's (alt look only) |
| `.../generation-iii/icons` | Gen 3 party icons | 417 PNG | 32x32 P | Official | Needs re-framing to 32x64 |
| `pokemon/versions/generation-iv` | DP, Platinum, HGSS, icons | 12,341 PNG | 80x80 (RGBA for HGSS) | Official DS | No. Downscale and re-index by hand |
| `.../generation-v` | BW fronts/backs, animated, icons | 8,081 PNG, 4,886 GIF | 96x96 P; animated GIFs about 37x38 | Official DS | No |
| `.../generation-vi` to `-viii` | 3D-model sprites and icons | gen 7: 1,303 PNG; gen 8: 2,815 PNG | 43x48 to 68x56 | Official 3DS/Switch | No |
| `pokemon/other/official-artwork` | Large art | in 6,731 PNG for `other/` | 475x475 RGBA | Official render | No |
| `pokemon/other/home`, `showdown`, `dream-world` | HOME 3D (512 RGBA), Showdown GIFs (1,146 GIF), SVG art (6,300 SVG) | see left | RGBA, GIF, vector | Official | No |
| `items/` | Item icons | 2,035 files, 905 in the root plus `berries/` and `underground/` | about 30x30 P | Gen 5 style | Needs 24x24 redraw; many already exist in the ROM |
| `badges/` | Badge art | 77 files | 85x85 official | Official | No (too big) |
| `types/` | Type icons | 468 files | various | Official | No; the ROM has its own |

Verdict: nothing to import except possibly Gen 5 item icons for items the ROM lacks. No trainers, no overworlds, no maps.

## Source 2: Team-Aquas-Asset-Repo (TAAR)

Licence and credit norm (TAAR `README.md`): assets are 'free to use and edit by default' unless a folder says it is not free to edit; any asset not wholly one person's must carry a README naming the original creators and anyone who modified it; credit to the creator is required. The README gives no per-asset licence, and a lot of the art is a redraw, recolour or rip of official art or of other hacks. Folders with no README have no stated credit line beyond the creator's folder name. See the licence warning in `asset-inventory.md` (this repo is public).

### Trainer Front Sprites (`Trainer Front Sprites/`)

186 files, 146 PNG, 28 creator folders. Almost all are 64x64 P and ready as they are. Exceptions (need cutting, indexing or are references, not sprites): `Kasen` one 329x456, `KyuZee` and `hyo` 367x229 previews, `Project Palladium` four large sheets, `Rubire4` 646x651, `kwenio` mixed RGB/RGBA (needs indexing) and one 130x64, `Pillowsledder`, `PurrfectDoodle` and `RafaelSanna` have a few RGBA 64x64.

| Path | Holds | PNG | Style / notes |
|---|---|---|---|
| `Pawkkie/` (3 subfolders) | `HGSS Resized to 64 x 64` (11), `Recolours` (11), `Redraws` (4): youngster, lass, hiker, fisher, picnicker, bug catcher, breeder, aroma lady, beauty, guards, psychic, twins | 26 | HGSS-derived, recoloured to RSE-style palettes. Safest, no named characters except Red and Leaf in `Recolours` |
| `Black Fragrant/` | Johto leaders and admins: falkner, bugsy, whitney, morty, chuck, jasmine, pryce, clair, janine, will, karen, archer, ariana, petrel, proton | 15 | From the hack Pokemon FireGold. Pryce, Falkner, Karen, Chuck already used |
| `Galaxeeh/` | Galactic, Plasma and Rocket grunts, Cyrus, Jupiter, Mars, Saturn, leaders Bugsy, Giovanni, Roxie. Has `.pal` files | 13 | Gen 5 influenced; Giovanni already used |
| `Kasen/` | acerola, drayden, iris, jasmine, clay, korrina, mina, skyla, volkner, BW ace trainers, hex maniac | 15 | Redraws of newer leaders. Acerola, Mina, Drayden already used |
| `iriv24/` | byron, candice, cynthia, dawn, fantina, gardenia, maylene, volkner, wake | 9 | Sinnoh leaders. Gardenia, Byron, Cynthia already used |
| `Kalarie/` | anthony, aya, damian, giselle, mandi, otoshi, ritchie | 7 | Original (non-official) characters; damian has goggles and jacket |
| `ShinyDragonHunter/` | ethan, Red_DS, little_girl, scout_f, scout_m | 5 | Official-derived |
| `Ringloom/` | GSC cooltrainer F, pokemaniac, HGSS Ethan, Lyra, Silver (names have spaces) | 5 | GBA-fitted DS art |
| `mudskip/` (`Custom Redraws`) | Hex maniac and others | 4 | Redraws |
| `hyo/` | brendan, may, red, gold fronts, `assorted.png` | 6 | Player pics, FRLG look; one 367x229 preview |
| `kwenio/` | kris, leaffront, masters_beauty_collector, oras_cooltrainer_m, oras_lass | 5 | ORAS style; truecolour (index first). `oras_lass` is Greta's pic |
| `RafaelSanna/` | lacey, magma_adm, punk, raihan | 4 | Mixed modes (some RGB) |
| `Project Palladium/` | big reference sheets | 4 | Not usable as pics; read its README for credit |
| `Nico/` | builder, devon_employee, miner | 3 | Original workers. Good for foreman and NPC pics |
| `Gygablastre/`, `KyuZee/`, `ryuujiryu/` | hooligans and medium; brendan/may ORAS; nurse, psychic F/M | 3 each | ryuujiryu `PsychicM` already used (Poison leader) |
| `BrandonXL/`, `Kumatora/`, `Lhea/`, `Twinleaf Logan/` | darach/thorton; phoebe, looker; Platinum Dawn/Lucas; Dawn/Lucas | 2 each | Kumatora/Lhea are Gen 4 player pics |
| `Estellar/`, `Francis III/`, `pokeruby/`, `yoshord/`, `Rubire4/`, `PurrfectDoodle/`, `Pillowsledder/` | one to two pics each | 1-2 | Pillowsledder has `scott` (used for gym 9, indexed by us) |

### Trainer Back Sprites (`Trainer Back Sprites/`)

1,772 files, 1,749 PNG. 1,730 of those are in `Coffee Cup/`, which is a customisation kit (RGBA 256x256, 160x160 and 875x196 layers, plus GIMP files), not finished pics. The rest are finished sheets.

| Path | Holds | Format | GBA fit |
|---|---|---|---|
| `Coffee Cup/` (`Images/`, `GIMP Files/`) | Clothes/body parts for building back, front and walk sprites; folders for walk, run, bike, female back | RGBA 256x256, 160x160, 875x196, no 16-colour limit | No, a toolkit. Needs hand assembly and indexing. README names Coffee Cup and links a PokeCommunity thread |
| `hyo/` | brendan, may, red, gold back pics, RSE variants (7) | P 64x256 or 64x320 | Yes. Note 64x320 is a five-frame sheet |
| `Lhea/`, `ShinyDragonHunter/` | pt_dawn, pt_lucas, one more | P 64x320 | Yes |
| `Kumatora/`, `KyuZee/`, `mudskip/` (phoebe), `yoshord/` (Lance, Lets Go) | 1-2 sheets each | P 64x256 or 64x384 | Yes. 384 high means six frames; check the frame count |
| `kwenio/` | calem, hilbert, leaf, noland | RGB/RGBA 64x64, 64x256, 64x320 | Needs indexing |

### Overworld Trainer Sprites (`Overworld Trainer Sprites/`)

1,415 files, 1,219 PNG. Sheets are mostly 144x32 (nine 16x32 frames) or 160x32, as the engine expects; a few are 288x32 or 864x32 (extra frames for run, bike or surf), and 16x16 or 48x32 files are small objects.

| Path | Holds | PNG | Format and notes |
|---|---|---|---|
| `RavePossum/Poffin-Case-Overworlds-Converted/` | Every vanilla NPC file name, FRLG style, vanilla palettes, plus subfolders `gym_leaders` (9 Hoenn leaders), `elite_four`, `frontier_brains`, `team_aqua`, `team_magma`, `brendan`, `may`, rs variants | 130 | P 144x32, drag and drop. README explains the `brendan/may` caveat. Includes `rich_boy`, `gentleman`, `old_woman`, `old_man`, `lass`, `youngster`, `fisherman`, `hiker`, `nurse`, `scientist_1/2`, `sailor`, `mom`, `prof_birch`, `steven`, `wallace`, `wally` |
| `hyo/` | A separate FRLG-style RSE reworked set; player folders include `.pal` and region-map icon | 164 | P 144x32 (93), 48x32, 192x32. Creator asks for credit if used or edited |
| `Poffin_Case/` | Original FRLG overworld set | 196 | RGB truecolour; superseded by RavePossum's conversion |
| `spilledpizza/` | Gen 4 (Diamond/Pearl) overworlds as 64x64 (95) and 144x32 (74), plus a whole `graphics/trainers/` tree with 97 matching front pics | 180 | P. Drag-and-drop pokeemerald tree with `src/`, `include/`, `spritesheet_rules.mk`. README lists credits (spilledpizza, TheWiggliestJiggliest, RichardPT, robloxmaster376, The Spriters Resource, Radiant Quartz/Prismatic Platinum team). Dawn/Lucas have no reflection palettes. The 64x64 files are the 4x16 facing sheets for 32x32 object events and may need extra object-event info |
| `Delta231s Collaborative HGSS Resource/` | HGSS-style sheets, many contributor subfolders | 82 | Mixed: RGB 160x32 (24), RGBA, P. `gbagfx` rejects RGBA; index first |
| `Kasen/` | gen4 breeder, Drayden, Clay, Iris, Skyla, Korrina, hex maniac, player sets | 53 | P 144x32 (22), 192x32, 288x32 |
| `SurfingPokemon/` | Surf-rider sprites (needs C injection) | 224 | P 32x384 and 64x768; not drop-in |
| `Galaxeeh/` | Galactic/Plasma/Rocket grunts and bosses, with `.pal` | 18 | P 288x32 |
| `PurrfectDoodle/`, `Bivurnum/` (Hoenn gym leaders, E4, nurse, cook, old man), `Black Fragrant/` (15 Johto), `Horo/` (Kanto leaders, 14), `Pawkkie/` (24: recolours, player skins, Elesa, Jasmine) | Leader and NPC sheets | 18, 16, 15, 14, 24 | P 144x32 mostly (Horo has some RGBA) |
| `kwenio/`, `mudskip/`, `grintoul/`, `Francis III/`, `Twinleaf Logan/` (1152x256 sheets), `Young-Dante/` (RGBA 720x384), `aveontrainer/` (RGBA 128x192) | Player skins, extras, bike or skate sets | 28, 10, 8, 4, 4, 2, 3 | Mixed. The big sheets need slicing; RGBA needs indexing |
| `Project Palladium/`, `Fan of 4869/`, `Oomer/`, `Turtleye/`, `Space Shaman/` | References or a few sheets | 2 each, 1, 2 | Mostly large reference images, not sheets |

### Overworld Pokemon Sprites (`Overworld Pokemon Sprites/`)

3,231 files, 1,123 PNG. `Rahtak/` has 1,119 PNG: P 192x32 (1,053), P 384x64 (43), plus small ones; follower-style overworlds for all species. Expansion already ships `overworld.png` for every species (192x32), so this adds little. `Kasen/` (one 864x32 sheet) and `KyuZee/` (3) are singles. Credit Rahtak, Kasen, KyuZee. Fits, with palette work per species.

### Overworld Other Sprites (`Overworld Other Sprites/`)

41 files, 29 PNG. `Berry trees/PurrfectDoodle` (17 sheets, 96x32 P, plus two reference images), `Graion Dilach` (apricorn tree and sapling), `KyuZee` (Tyrantrum fossil and statue), `Pawkkie` (GameCube 16x16), `Oomer` (pokeball), `Pokemon Inclement Emerald` (gold item ball, mega stone), `Project Palladium` (large references). 16x16 or 16x32 P objects fit directly. Credit by folder; Palladium needs its team credited.

### Official Pokemon Assets (`Official Pokemon Assets/`)

1,068 files, 541 PNG. Official Nintendo art, ripped. Same public-repo risk as anything derived from it.

| Path | Holds | Format |
|---|---|---|
| `HGSS Overworld Pokemon/sprites` | 536 PNG, 512 at P 192x32 | Fits as is; palettes folder alongside. Compiled by WiserVisor (README) |
| `Trainer Spritesheets/` | `Gen3_Front_Sprites.png` (RGBA 3899x800) and `HGSS_Front_Sprites.png` (973x1798): every official trainer pic on one sheet | Needs cutting to 64x64 and indexing. Sources named in README: The Spriters Resource, MufasaKong, Nx-Kun, kmie821. The only place the official Gen 3 rich boy, gentleman and lady pics live |
| `Pokemon Garden/` | Front and overworld sheets from the fan game Pokemon Garden (RGBA, 485x1771 and 660x1315) | Needs cutting; credit Bascule and Mvit |
| `Item Icons/` | `poffin_case` icon, 24x24 P | Fits |

### Pokemon (`Pokemon/`)

611 files, 445 PNG. `Beta Revamps` (230 PNG, mostly RGBA 64x64, 32x64, 256x64), `Sprite Redesigns` (132, P 64x64 and 64x128, Kaixer, Oomer, others), `New Megas` (51, P 64x64, 32x64 icons), `Fakemon` (26, P 64x64 / 64x128, creators Bivurnum, Nico, Sylph), `Icon Sprites` (6). Per-species READMEs name creators. Fits when P 64x64; RGBA needs indexing. Nico's `Calfling` (calf) suits Greta's farm.

### Items (`Items/`)

23 files, 10 PNG, all P 24x24, so they fit as is: `Cookie Softcore` (axe, lantern, pickaxe, power glove, scuba gear, surfboard: HM icons), `AGSMGMaster64` (geyser water, unagi lunch), `Graion Dilach` (running shoes), `Pawkkie` (candy jar). Each has a `.pal`.

### Battle Backgrounds (`Battle Backgrounds/`)

373 files, 120 PNG. `CFRU` (48; P 256x512 tilesheets), `Leob0505` (22; P 128x128), `PurrfectDoodle` (20; P 128x128, 128x48), `RavePossum` (22; P 128x128, 128x32), `Chairry` (5; RGB 240x112 previews), `Ruki` (a reference image), `ShinyDragonHunter` (2). Several are Ruki's HGSS/DPPt ports. Partial file sets exist; check each terrain has tiles, tilemap and palette. Credit the folder creator.

### Battle effects and Field Effects

`Battle effects/` has 4 files: `Oome` (P 32x160), `PurrfectDoodle` (16x48 and a 720x480 preview). `Field Effects/Overworld Emotes` has 4 files: `emotes.png` (P 96x16), a 288x48 sheet and a preview. All small, fit as is.

### User Interface (`User Interface/`)

188 files, 135 PNG. `Fonts` (a 256x512 P font and a 960x320 preview), `Kaixer` (type icons 32x16 and trainer card badges; the badge sheet is used in the ROM), `Lhea` (26 modern type icons 32x16), `m` (28 type icons), `missiri` (24), `Zatsu` (20 Tera icons 16x16), `Mudskip` (shop menu, 240x160), `Oomer`, `Project Palladium`. Type icons fit as is; screens need layout work.

### Pokemon Essentials Packs and Projects

- `Pokemon Essentials Packs/` has 3 files: `Generation_8_Pack.zip`, `Generation_9_Pack_v3.2.0.rar`, README (credit: AsparagusEduardo for sharing). Pokemon Essentials format, contents not unpacked here. Wrong engine; not for this ROM.
- `Projects/` has 1,379 files, 354 PNG. `Leob0505 PokeZelda Minish Quest` has `credits.md`, 21 sheets at P 144x32, 36 P 64x64, 36 P 16x16, 21 P 24x24: Zelda-restyled Emerald art (Zelda IP, many credits). `FFVII_Sprites` is Square Enix art, RGBA, not for this setting.

## Shortlist for Veldris

Everything below is a candidate; paths relative to TAAR. 'Used' means already imported.

**Troglodyte (the Goldsworth rival and family), overworld**
- `Overworld Trainer Sprites/RavePossum/Poffin-Case-Overworlds-Converted/rich_boy.png` (vanilla palette, drop-in; the proposed Troglodyte sheet).
- `.../spilledpizza/graphics/object_events/pics/people/` : `DP_rich_boy`, `DP_rich_lady`, `DP_socialite`, `DP_gentleman`, `DP_lady`, `DP_parasol_lady`, `DP_barry` for cousins and parents (check the extra frames work first).
- `.../RavePossum/.../gentleman.png`, `old_man.png`, `old_woman.png`, `man_1.png` to `man_5.png`, `woman_1.png` to `woman_5.png` for butlers and housekeeper.

**Troglodyte and Goldsworth, battle pictures**
- `Overworld Trainer Sprites/spilledpizza/graphics/trainers/front_pics/DP_Rich_Boy.png`, `DP_Gentleman.png`, `DP_Lady.png`, `DP_Socialite.png`, `DP_Barry.png`, `DP_Collector.png` (97 DP-style 64x64 P pics; the folder has no Gen 3 rich boy, but see below).
- `Official Pokemon Assets/Trainer Spritesheets/Gen3_Front_Sprites.png` (cut out Rich Boy, Gentleman, Lady; needs cutting).
- A rival look: `Trainer Front Sprites/Kalarie/` (original characters: anthony, damian, ritchie), or `Trainer Front Sprites/Twinleaf Logan/Lucas.png`.

**Gym leaders, E4, Champion**
- Picks are made (see `gym-leader-art.md`). Spare alternates: `Trainer Front Sprites/Pawkkie/Recolours/` (beauty_pp, bug_catcher_f_pp, fisherman_pp), `Trainer Front Sprites/Kalarie/` (all original), `.../Nico/` (builder, miner, devon_employee), and `.../spilledpizza/graphics/trainers/front_pics/` (DP_Candice, DP_Fantina, DP_Cheryl, DP_Rancher for farm people).

**Player and rival back pics**
- `Trainer Back Sprites/hyo/` (brendan, may, red, gold, P 64x256 or 64x320), `Trainer Back Sprites/Lhea/pt_dawn.png`, `pt_lucas.png` (P 64x320), `Trainer Back Sprites/kwenio/calem.png` (needs indexing).

**NPC overworlds**
- Whole set: `Overworld Trainer Sprites/RavePossum/Poffin-Case-Overworlds-Converted/` (130 sheets, all vanilla names).
- Gym leaders in FRLG style: `.../RavePossum/.../gym_leaders/` (9 Hoenn), `Overworld Trainer Sprites/Black Fragrant/` (Johto, with `.pal`), `Overworld Trainer Sprites/Horo/` (Kanto), `Overworld Trainer Sprites/Bivurnum/` (Hoenn leaders and E4), `Overworld Trainer Sprites/Kasen/` (Drayden, Clay, Iris, Skyla, Korrina).
- Ranch and farm: `.../spilledpizza/.../DP_rancher.png`, `DP_cowgirl.png`, `DP_breeder_f.png`, `Delta231s Collaborative HGSS Resource/` (cowgirl, old_woman, boy, girl).
- Overworld objects: `Overworld Other Sprites/Berry trees/PurrfectDoodle/`, `Overworld Other Sprites/Graion Dilach/` (apricorn trees).

**Item icons**
- `Items/Cookie Softcore/` (6 HM icons), `Items/Graion Dilach/running_shoes.png`, `Items/Pawkkie/candy_jar.png`, `Items/AGSMGMaster64/` (2 icons), all 24x24 P.
- `sprites/sprites/items/` for a 30x30 Gen 5 style fallback (redraw to 24x24; the ROM already has 619 icons).

**Pokemon**
- Switch `P_GBA_STYLE_SPECIES_GFX` to TRUE for GBA-style art (no import). Fakemon: `Pokemon/Fakemon/Nico/Calfling`.

## Open questions

1. Licence risk: which 'official-derived' sources does the author accept for the public repo? The rule is currently case by case (`CREDITS.md` labels them), and TAAR gives only a blanket 'free to use, credit required'.
2. Is spilledpizza's DP-style set (overworld 64x64 sheets plus 97 front pics) acceptable as a whole, or only individual files? Its 64x64 overworld sheets may need extra object-event info and palette slots; this has not been tested.
3. Troglodyte's battle picture: DP `Rich_Boy`, cut from the Gen 3 sheet, or custom art? Does his overworld match (`rich_boy` from RavePossum)?
4. Is the GBA-style Pokemon art preferred over the Gen 4/5 style (the config switch)?
5. Do the Goldsworth cousins get distinct pictures (needs unique ids and sheets) or shared looks? See `goldsworth.md`.
6. The TAAR URL: `CREDITS.md` links `Pawkkie/Team-Aquas-Asset-Repo`, the author's copy is `24rousol-hub/Team-Aquas-Asset-Repo`. Which to cite?
7. Other free resources I know for sure are limited: the Spriters Resource (rips, no licence), PokeCommunity threads linked in TAAR READMEs (permission per post), and the asset repo itself. No other source is claimed here; none was checked online.
8. Not verified: palettes inside each sheet (some P files may carry more than 16 entries), frame counts of 288x32 or 864x32 sheets, and per-species Pokemon READMEs.

## Imported (2026-10-10)

The whole spilledpizza DP set is in the ROM (author's choice): 70 overworlds as `OBJ_EVENT_GFX_DP_*` and 94 battle pictures as `Pic: DP ...` in `trainers.party`. Full name list: [dp-sprite-list.md](dp-sprite-list.md). Tool: `design/tools/sprites/import_dp.py`. Lucas and Dawn player sheets and back pics are copied for the outfit system ([player-customization.md](player-customization.md)) but not registered as NPCs. **Each DP overworld has its own palette**, unlike vanilla NPCs which share four, so a screen with many different DP people can run out of sprite palettes (the GBA has 16, shared with the player, followers and effects). Keep it to about 6 different DP people in view at once; repeats of the same person cost nothing extra.
