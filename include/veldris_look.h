#ifndef GUARD_VELDRIS_LOOK_H
#define GUARD_VELDRIS_LOOK_H

// Player customization, Unbound style (hack-owned). See design/player-customization.md.

#include "constants/trainers.h"

#define LOOK_PART_COUNT  4   // skin, hair (Brendan: clothes), top, accent
#define LOOK_KIND_COUNT  3   // overworld, reflection, trainer picture
#define LOOK_OPTIONS     8
#define LOOK_MAX_SHADES  4

enum { LOOK_PART_SKIN, LOOK_PART_HAIR, LOOK_PART_TOP, LOOK_PART_ACCENT };
enum { LOOK_KIND_OW, LOOK_KIND_REFL, LOOK_KIND_TRAINER };
enum { OUTFIT_EMERALD, OUTFIT_RS, OUTFIT_DP, OUTFIT_COUNT };

#define PLAYER_AVATAR_STATE_COUNT (PLAYER_AVATAR_STATE_VSSEEKER + 1)

u32 VeldrisLook_GetOutfit(void);
// Hooks (one call each in upstream files, see design/engine-edits.md)
void VeldrisLook_TintObjectPalette(u16 paletteTag, u8 paletteNum);
const u16 *VeldrisLook_TrainerPalette(enum TrainerPicID trainerPic, const u16 *palette);
u16 VeldrisLook_PlayerGfx(u8 state, u8 gender, u16 emeraldGfx);
bool32 VeldrisLook_IsFemaleOutfitGfx(u16 graphicsId);
enum TrainerPicID VeldrisLook_PlayerTrainerPic(u8 gender, enum TrainerPicID emeraldPic);
// Script entry (callnative + waitstate): the Costume Box picker
void VeldrisLook_OpenMenu(void);
// Script entry: VAR_RESULT = TRUE if the player is on foot (the box only works on foot)
void VeldrisLook_CanOpen(void);

extern const u8 Veldris_EventScript_CostumeBox[];

#endif // GUARD_VELDRIS_LOOK_H
