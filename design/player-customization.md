# Player customization (Unbound style)

Status: **BUILT 2026-10-10** at the author's request ('full Unbound copy'). Colour names, unlock conditions and Mom's lines are **PROPOSED** until the author approves them.

## What Unbound does (research, 2026-10-10)

- Unbound's feature list: 'Choose from up to 300 different combinations of skin tones, hair colours, and outfit colours.'
- You get a **Costume Box** key item from Mom early on, after the first rival battle. At first it only recolours your base outfit. Later it switches between outfits you have unlocked (Marlon's costume from the story, a Champion outfit after the League, Red/Leaf from a trade sidequest, Ethan/Lyra from a mission).
- Sources: the PokéCommunity thread (feature list) and the Unbound wiki's Costume Box page.

## What Veldris does

**When.** Mom gives the **Costume Box** together with the Running Shoes on the first morning, and the picker opens right away ('have a look in the mirror'). After that, use the Costume Box from the bag (or SELECT) any time on the field.

**The picker.** A window on the field with the player's battle picture beside it. Up/Down picks a row, Left/Right changes it, and the overworld sprite and the picture change live. A or START on DONE keeps it; B puts everything back.

| Row | Options | What changes |
|---|---|---|
| Outfit | Emerald (start), Ruby/Sapphire, Diamond/Pearl (unlockable) | The whole sprite set and battle pictures |
| Skin | 5 tones | Palette indices 1-3 |
| Hair (Brendan: Hat) | 8 colours | May: indices 7-8 (her hair). Brendan: index 9 (his white cap; his hair is hidden under it) |
| Top | 8 colours | Indices 12-13 (May's shirt, Brendan's shirt trim) |
| Accent | 8 colours | Indices 10-11 (bandana and bag) |

5 x 8 x 8 x 8 = 2,560 colour combinations on the Emerald outfit. Like Unbound, the **colours apply to the base (Emerald) outfit only**; the other outfits keep their own colours. Rows that do not apply are greyed.

**One table drives every picture.** Brendan's and May's palettes use the same index for the same part on the overworld sheet, the water reflection, the battle back picture and the front picture (trainer card, HM cut-in, Hall of Fame), so one recolour table covers them all. The recolour ramps are made by `design/tools/sprites/player_look.py` (keeps each part's light-to-dark steps and moves them to the new colour) into `src/data/veldris_look_palettes.h`.

## Outfits

| Outfit | Overworld | Battle pictures | Unlock (PROPOSED) |
|---|---|---|---|
| Emerald | vanilla Brendan/May | vanilla | Start |
| Ruby/Sapphire | vanilla RS Brendan/May walking and running; bikes, surfing, fishing and the rest fall back to Emerald | vanilla RS front and back | 3 badges, or `FLAG_VELDRIS_OUTFIT_RS` |
| Diamond/Pearl | Lucas/Dawn (DP set): walking, running, Mach Bike, surfing, fishing (Dawn also Cut/Rock Smash pose and watering); acro bike, underwater and anything missing fall back to Emerald | DP Lucas/Dawn front, DP back (spilledpizza) | 6 badges, or `FLAG_VELDRIS_OUTFIT_DP` |

The unlock points are placeholders: `IsOutfitUnlocked` in `src/veldris_look.c` checks the flag or the badge count, so the outfit simply appears in the list. A scene that hands each outfit over (like Unbound's) can set the flag instead; that is a story point, so the author decides.

**Checked in mGBA (2026-10-10):** Mom's scene gives the box and opens the picker; every row changes the battle picture and the walking preview live; Ruby and Diamond swap the whole set and grey out the colour rows; the map sprite keeps the look after the picker and after a warp (Dawn runs with her own running frames); the trainer card shows the recoloured picture; in battle the VS banner and the back picture are Dawn's. **Not checked:** the RS/DP outfits on a bike, surfing or fishing, the water reflection, and the Costume Box from the bag (the same script as Mom's, without the gift).

## Save data

| What | Where |
|---|---|
| Outfit (2 bits), skin (3), hair (3), top (3), accent (3) | `VAR_VELDRIS_LOOK` (0x40FA), packed; 0 = Emerald outfit with the original colours |
| Outfit unlocks | `FLAG_VELDRIS_OUTFIT_RS` (0x883), `FLAG_VELDRIS_OUTFIT_DP` (0x885) |

No save-block change, so old saves keep working (they read as the default look).

## Code

Hack-owned: `src/veldris_look.c`, `include/veldris_look.h`, `src/data/veldris_look_palettes.h`, `src/data/object_events/veldris_outfit_object_events.h`, `data/scripts/veldris_look.inc`. Hooks in upstream files are one call each, logged in [engine-edits.md](engine-edits.md):

- `src/event_object_movement.c` `LoadSpritePaletteIfTagExists`: recolour Brendan/May overworld palettes as they load.
- `include/data.h` `GetTrainerFrontPicPalette` / `GetTrainerBackPicPalette`: the player's own picture gets the recoloured palette.
- `src/field_player_avatar.c` `GetPlayerAvatarGraphicsIdByStateIdAndGender` and `GetPlayerAvatarGenderByGraphicsId`: outfit sprite sets.
- `src/trainer.c` `GetPlayerTrainerPic`, `src/pokemon.c` `PlayerGenderToFrontTrainerPicId`, `src/trainer_card.c`: outfit battle pictures.

## Left out

- The **Coffee Cup** kit in Team-Aquas-Asset-Repo (`Trainer Back Sprites/Coffee Cup/`) has separate hair styles, tops and bottoms, which would allow Unbound-plus layered outfits. It is DS-sized RGBA layers in HGSS style, so every piece would need cutting, scaling and re-indexing. Not used; a possible later project.
- Hair **styles** (as opposed to colours) need new art per style.
