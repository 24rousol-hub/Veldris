#include "global.h"
#include "event_data.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "field_weather.h"
#include "main.h"
#include "menu.h"
#include "palette.h"
#include "script.h"
#include "sound.h"
#include "sprite.h"
#include "strings.h"
#include "task.h"
#include "text.h"
#include "trainer.h"
#include "trainer_pokemon_sprites.h"
#include "window.h"
#include "veldris_badges.h"
#include "veldris_look.h"
#include "constants/event_objects.h"
#include "constants/songs.h"

// Player customization, Unbound style (hack-owned file). See design/player-customization.md.
//
// VAR_VELDRIS_LOOK packs the choice: bits 0-1 outfit, 2-4 skin, 5-7 hair, 8-10 top, 11-13 accent.
// 0 is the Emerald outfit with the original colours, so old saves and new games look vanilla until changed.

#include "data/veldris_look_palettes.h"
#include "data/veldris_outfit_gfx.h"

extern const u16 gObjectEventPal_Brendan[];
extern const u16 gObjectEventPal_May[];

#define OUTFIT_SHIFT 0
#define OUTFIT_MASK  0x3
static const u8 sPartShift[LOOK_PART_COUNT] = {2, 5, 8, 11};
static const u8 sPartOptions[GENDER_COUNT][LOOK_PART_COUNT] = {
    [MALE]   = {5, 8, 8, 8},
    [FEMALE] = {5, 8, 8, 8},
};

static u32 GetPart(u32 look, u32 part) { return (look >> sPartShift[part]) & 7; }
static u32 SetPart(u32 look, u32 part, u32 value) { return (look & ~(7 << sPartShift[part])) | ((value & 7) << sPartShift[part]); }
static u32 GetOutfitOf(u32 look) { return (look >> OUTFIT_SHIFT) & OUTFIT_MASK; }

u32 VeldrisLook_GetOutfit(void)
{
    u32 outfit = GetOutfitOf(VarGet(VAR_VELDRIS_LOOK));
    return outfit < OUTFIT_COUNT ? outfit : OUTFIT_EMERALD;
}

static bool32 IsOutfitUnlocked(u32 outfit)
{
    switch (outfit)
    {
    case OUTFIT_EMERALD: return TRUE;
    // PROPOSED unlock points (design/player-customization.md): the flag, or enough badges
    case OUTFIT_RS:      return FlagGet(FLAG_VELDRIS_OUTFIT_RS) || GetBadgeCount() >= 3;
    case OUTFIT_DP:      return FlagGet(FLAG_VELDRIS_OUTFIT_DP) || GetBadgeCount() >= 6;
    }
    return FALSE;
}

// Recolour a 16-colour palette in place for the given gender and picture kind.
static void ApplyLook(u16 *pal, u32 gender, u32 kind, u32 look)
{
    u32 part, n;

    if (GetOutfitOf(look) != OUTFIT_EMERALD || gender >= GENDER_COUNT)
        return;
    for (part = 0; part < LOOK_PART_COUNT; part++)
    {
        u32 option = GetPart(look, part);
        if (option == 0 || option >= LOOK_OPTIONS)
            continue;
        for (n = 0; n < LOOK_MAX_SHADES && sLookIndices[gender][part][n] != 0; n++)
            pal[sLookIndices[gender][part][n]] = sLookColours[gender][kind][part][option][n];
    }
}

// Hook in LoadSpritePaletteIfTagExists (event_object_movement.c): the player's Emerald overworld palette as it loads.
void VeldrisLook_TintObjectPalette(u16 paletteTag, u8 paletteNum)
{
    u32 gender = gSaveBlock2Ptr->playerGender, kind;
    u16 *pal = &gPlttBufferUnfaded[OBJ_PLTT_ID(paletteNum)];

    if (paletteTag == (gender == MALE ? OBJ_EVENT_PAL_TAG_BRENDAN : OBJ_EVENT_PAL_TAG_MAY))
        kind = LOOK_KIND_OW;
    else if (paletteTag == (gender == MALE ? OBJ_EVENT_PAL_TAG_BRENDAN_REFLECTION : OBJ_EVENT_PAL_TAG_MAY_REFLECTION))
        kind = LOOK_KIND_REFL;
    else
        return;
    ApplyLook(pal, gender, kind, VarGet(VAR_VELDRIS_LOOK));
    CpuCopy16(pal, &gPlttBufferFaded[OBJ_PLTT_ID(paletteNum)], PLTT_SIZE_4BPP);
}

// Hook in GetTrainerFrontPicPalette / GetTrainerBackPicPalette (include/data.h): the player's own pictures.
const u16 *VeldrisLook_TrainerPalette(enum TrainerPicID trainerPic, const u16 *palette)
{
    static EWRAM_DATA u16 sBuffer[16] = {0};
    u32 gender = gSaveBlock2Ptr->playerGender;
    u32 look = VarGet(VAR_VELDRIS_LOOK);

    if (look == 0 || GetOutfitOf(look) != OUTFIT_EMERALD)
        return palette;
    if (trainerPic != (gender == MALE ? TRAINER_PIC_BRENDAN : TRAINER_PIC_MAY))
        return palette;
    CpuCopy16(palette, sBuffer, sizeof(sBuffer));
    ApplyLook(sBuffer, gender, LOOK_KIND_TRAINER, look);
    return sBuffer;
}

// Hook in GetPlayerAvatarGraphicsIdByStateIdAndGender: the outfit's sprite for this state, or Emerald's.
u16 VeldrisLook_PlayerGfx(u8 state, u8 gender, u16 emeraldGfx)
{
    u32 outfit = VeldrisLook_GetOutfit();

    if (outfit == OUTFIT_EMERALD || state >= PLAYER_AVATAR_STATE_COUNT || gender >= GENDER_COUNT
     || gender != gSaveBlock2Ptr->playerGender)
        return emeraldGfx;
    if (sOutfitGfx[outfit][state][gender] == 0)
        return emeraldGfx;
    return sOutfitGfx[outfit][state][gender];
}

// Hook in GetPlayerAvatarGenderByGraphicsId: the female outfit sprites count as female.
bool32 VeldrisLook_IsFemaleOutfitGfx(u16 graphicsId)
{
    u32 i;
    for (i = 0; i < ARRAY_COUNT(sOutfitFemaleGfx); i++)
    {
        if (sOutfitFemaleGfx[i] == graphicsId)
            return TRUE;
    }
    return FALSE;
}

// Hook in GetPlayerTrainerPic / PlayerGenderToFrontTrainerPicId / the trainer card: the outfit's battle pictures.
enum TrainerPicID VeldrisLook_PlayerTrainerPic(u8 gender, enum TrainerPicID emeraldPic)
{
    if (gender != gSaveBlock2Ptr->playerGender)
        return emeraldPic;
    switch (VeldrisLook_GetOutfit())
    {
    case OUTFIT_RS: return gender == MALE ? TRAINER_PIC_RS_BRENDAN : TRAINER_PIC_RS_MAY;
    case OUTFIT_DP: return gender == MALE ? TRAINER_PIC_DP_LUCAS : TRAINER_PIC_DP_DAWN;
    }
    return emeraldPic;
}

// ---------------------------------------------------------------------------------------------------------------
// The Costume Box picker: a field window plus the battle picture, with the overworld sprite changing live.

enum { ROW_OUTFIT, ROW_SKIN, ROW_HAIR, ROW_TOP, ROW_ACCENT, ROW_DONE, ROW_COUNT };

static const u8 *const sOutfitNames[OUTFIT_COUNT] = {
    COMPOUND_STRING("Emerald"), COMPOUND_STRING("Ruby"), COMPOUND_STRING("Diamond"),
};
static const u8 *const sSkinNames[] = {
    COMPOUND_STRING("Light"), COMPOUND_STRING("Pale"), COMPOUND_STRING("Tan"), COMPOUND_STRING("Brown"), COMPOUND_STRING("Deep"),
};
static const u8 *const sHairNames[GENDER_COUNT][LOOK_OPTIONS] = {
    [MALE]   = {COMPOUND_STRING("Navy"), COMPOUND_STRING("Black"), COMPOUND_STRING("Brown"), COMPOUND_STRING("Green"),
                COMPOUND_STRING("Red"), COMPOUND_STRING("Purple"), COMPOUND_STRING("Grey"), COMPOUND_STRING("Khaki")},
    [FEMALE] = {COMPOUND_STRING("Brown"), COMPOUND_STRING("Black"), COMPOUND_STRING("Blonde"), COMPOUND_STRING("Red"),
                COMPOUND_STRING("Blue"), COMPOUND_STRING("Green"), COMPOUND_STRING("Pink"), COMPOUND_STRING("Silver")},
};
static const u8 *const sTopNames[LOOK_OPTIONS] = {
    COMPOUND_STRING("Red"), COMPOUND_STRING("Blue"), COMPOUND_STRING("Green"), COMPOUND_STRING("Yellow"),
    COMPOUND_STRING("Purple"), COMPOUND_STRING("Orange"), COMPOUND_STRING("Black"), COMPOUND_STRING("White"),
};
static const u8 *const sAccentNames[LOOK_OPTIONS] = {
    COMPOUND_STRING("Green"), COMPOUND_STRING("Red"), COMPOUND_STRING("Blue"), COMPOUND_STRING("Yellow"),
    COMPOUND_STRING("Purple"), COMPOUND_STRING("Orange"), COMPOUND_STRING("Black"), COMPOUND_STRING("White"),
};
static const u8 *const sRowLabels[GENDER_COUNT][ROW_COUNT] = {
    [MALE]   = {COMPOUND_STRING("OUTFIT"), COMPOUND_STRING("SKIN"), COMPOUND_STRING("CLOTHES"),
                COMPOUND_STRING("TRIM"), COMPOUND_STRING("BANDANA"), COMPOUND_STRING("DONE")},
    [FEMALE] = {COMPOUND_STRING("OUTFIT"), COMPOUND_STRING("SKIN"), COMPOUND_STRING("HAIR"),
                COMPOUND_STRING("SHIRT"), COMPOUND_STRING("BANDANA"), COMPOUND_STRING("DONE")},
};

#define tRow        data[0]
#define tWindowId   data[1]
#define tPicSprite  data[2]
#define tOldLook    data[3]
#define tOwSprite   data[4]

#define WIN_WIDTH   16
#define VALUE_X     60

static const struct WindowTemplate sWindowTemplate = {
    .bg = 0,
    .tilemapLeft = 1,
    .tilemapTop = 1,
    .width = WIN_WIDTH,
    .height = ROW_COUNT * 2,
    .paletteNum = 15,
    .baseBlock = 0x139, // the start menu's spot; no message box is up while the picker is open
};

static const u8 sTextColors[][3] = {
    {TEXT_COLOR_WHITE, TEXT_COLOR_DARK_GRAY, TEXT_COLOR_LIGHT_GRAY},
    {TEXT_COLOR_WHITE, TEXT_COLOR_LIGHT_GRAY, TEXT_COLOR_WHITE},
};

static const u8 *RowValue(u32 row, u32 look, u32 gender)
{
    switch (row)
    {
    case ROW_OUTFIT: return sOutfitNames[GetOutfitOf(look)];
    case ROW_SKIN:   return sSkinNames[GetPart(look, LOOK_PART_SKIN)];
    case ROW_HAIR:   return sHairNames[gender][GetPart(look, LOOK_PART_HAIR)];
    case ROW_TOP:    return sTopNames[GetPart(look, LOOK_PART_TOP)];
    case ROW_ACCENT: return sAccentNames[GetPart(look, LOOK_PART_ACCENT)];
    }
    return gText_EmptyString2;
}

static void DrawMenu(struct Task *task)
{
    u32 look = VarGet(VAR_VELDRIS_LOOK), gender = gSaveBlock2Ptr->playerGender, row;
    bool32 colours = (GetOutfitOf(look) == OUTFIT_EMERALD);
    u8 windowId = task->tWindowId;

    FillWindowPixelBuffer(windowId, PIXEL_FILL(1));
    for (row = 0; row < ROW_COUNT; row++)
    {
        u32 y = row * 16;
        bool32 grey = (row >= ROW_SKIN && row <= ROW_ACCENT && !colours);
        AddTextPrinterParameterized3(windowId, FONT_NORMAL, 8, y, sTextColors[grey], TEXT_SKIP_DRAW, sRowLabels[gender][row]);
        if (row != ROW_DONE)
        {
            AddTextPrinterParameterized3(windowId, FONT_NORMAL, VALUE_X, y, sTextColors[grey], TEXT_SKIP_DRAW, COMPOUND_STRING("{LEFT_ARROW}"));
            AddTextPrinterParameterized3(windowId, FONT_NORMAL, VALUE_X + 10, y, sTextColors[grey], TEXT_SKIP_DRAW, RowValue(row, look, gender));
            AddTextPrinterParameterized3(windowId, FONT_NORMAL, WIN_WIDTH * 8 - 10, y, sTextColors[grey], TEXT_SKIP_DRAW, COMPOUND_STRING("{RIGHT_ARROW}"));
        }
    }
    AddTextPrinterParameterized(windowId, FONT_NORMAL, gText_SelectorArrow, 0, task->tRow * 16, TEXT_SKIP_DRAW, NULL);
    CopyWindowToVram(windowId, COPYWIN_GFX);
}

static void ShowPicture(struct Task *task)
{
    u32 gender = gSaveBlock2Ptr->playerGender;
    enum TrainerPicID pic = VeldrisLook_PlayerTrainerPic(gender, gender == MALE ? TRAINER_PIC_BRENDAN : TRAINER_PIC_MAY);

    if (task->tPicSprite != SPRITE_NONE)
        FreeAndDestroyTrainerPicSprite(task->tPicSprite);
    task->tPicSprite = CreateTrainerPicSprite(pic, TRUE, 184, 60, 0, GetTrainerPicTag(pic, TRUE));

    // The window covers the player in the middle of the screen, so show a walking copy of the overworld sprite too.
    if (task->tOwSprite != SPRITE_NONE)
        DestroySprite(&gSprites[task->tOwSprite]);
    task->tOwSprite = CreateObjectGraphicsSprite(GetPlayerAvatarGraphicsIdByStateId(PLAYER_AVATAR_STATE_NORMAL), SpriteCallbackDummy, 184, 124, 0);
    if (task->tOwSprite != MAX_SPRITES)
        StartSpriteAnim(&gSprites[task->tOwSprite], ANIM_STD_GO_SOUTH);
    else
        task->tOwSprite = SPRITE_NONE;
}

// Re-apply the look to the player sprite on the map: the outfit's sprite set, then the recoloured palette.
static void RefreshPlayer(void)
{
    struct ObjectEvent *player = &gObjectEvents[gPlayerAvatar.objectEventId];
    u32 gender = gSaveBlock2Ptr->playerGender;
    u16 tag = gender == MALE ? OBJ_EVENT_PAL_TAG_BRENDAN : OBJ_EVENT_PAL_TAG_MAY;
    u16 gfx = GetPlayerAvatarGraphicsIdByStateId(PLAYER_AVATAR_STATE_NORMAL);
    u8 slot;

    if (player->graphicsId != gfx)
        ObjectEventSetGraphicsId(player, gfx);
    slot = IndexOfSpritePaletteTag(tag);
    if (slot != 0xFF)
    {
        CpuCopy16(gender == MALE ? gObjectEventPal_Brendan : gObjectEventPal_May, &gPlttBufferUnfaded[OBJ_PLTT_ID(slot)], PLTT_SIZE_4BPP);
        VeldrisLook_TintObjectPalette(tag, slot);
        UpdateSpritePaletteWithWeather(slot, FALSE);
    }
}

static void CloseMenu(u8 taskId)
{
    struct Task *task = &gTasks[taskId];

    if (task->tPicSprite != SPRITE_NONE)
        FreeAndDestroyTrainerPicSprite(task->tPicSprite);
    if (task->tOwSprite != SPRITE_NONE)
        DestroySprite(&gSprites[task->tOwSprite]);
    ClearStdWindowAndFrameToTransparent(task->tWindowId, TRUE);
    RemoveWindow(task->tWindowId);
    ScriptContext_Enable();
    DestroyTask(taskId);
}

static u32 NextOutfit(u32 outfit, s32 step)
{
    u32 i;
    for (i = 0; i < OUTFIT_COUNT; i++)
    {
        outfit = (outfit + OUTFIT_COUNT + step) % OUTFIT_COUNT;
        if (IsOutfitUnlocked(outfit))
            return outfit;
    }
    return OUTFIT_EMERALD;
}

static bool32 ChangeRow(u32 row, s32 step)
{
    u32 look = VarGet(VAR_VELDRIS_LOOK), gender = gSaveBlock2Ptr->playerGender, part, count, value;

    if (row == ROW_OUTFIT)
    {
        u32 outfit = NextOutfit(GetOutfitOf(look), step);
        if (outfit == GetOutfitOf(look))
            return FALSE;
        look = (look & ~OUTFIT_MASK) | outfit;
    }
    else if (row >= ROW_SKIN && row <= ROW_ACCENT)
    {
        if (GetOutfitOf(look) != OUTFIT_EMERALD)
            return FALSE;
        part = row - ROW_SKIN;
        count = sPartOptions[gender][part];
        value = (GetPart(look, part) + count + step) % count;
        look = SetPart(look, part, value);
    }
    else
    {
        return FALSE;
    }
    VarSet(VAR_VELDRIS_LOOK, look);
    return TRUE;
}

static void Task_LookMenu(u8 taskId)
{
    struct Task *task = &gTasks[taskId];

    if (JOY_NEW(DPAD_UP))
    {
        PlaySE(SE_SELECT);
        task->tRow = (task->tRow + ROW_COUNT - 1) % ROW_COUNT;
        DrawMenu(task);
    }
    else if (JOY_NEW(DPAD_DOWN))
    {
        PlaySE(SE_SELECT);
        task->tRow = (task->tRow + 1) % ROW_COUNT;
        DrawMenu(task);
    }
    else if (JOY_NEW(DPAD_LEFT | DPAD_RIGHT))
    {
        if (ChangeRow(task->tRow, JOY_NEW(DPAD_LEFT) ? -1 : 1))
        {
            PlaySE(SE_SELECT);
            RefreshPlayer();
            ShowPicture(task);
            DrawMenu(task);
        }
    }
    else if (JOY_NEW(START_BUTTON) || (JOY_NEW(A_BUTTON) && task->tRow == ROW_DONE))
    {
        PlaySE(SE_SELECT);
        CloseMenu(taskId);
    }
    else if (JOY_NEW(B_BUTTON))
    {
        PlaySE(SE_SELECT);
        VarSet(VAR_VELDRIS_LOOK, (u16)task->tOldLook);
        RefreshPlayer();
        CloseMenu(taskId);
    }
}

void VeldrisLook_CanOpen(void)
{
    gSpecialVar_Result = TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_ON_FOOT) ? TRUE : FALSE;
}

void VeldrisLook_OpenMenu(void)
{
    u8 taskId = CreateTask(Task_LookMenu, 80);
    struct Task *task = &gTasks[taskId];

    task->tRow = 0;
    task->tOldLook = VarGet(VAR_VELDRIS_LOOK);
    task->tPicSprite = SPRITE_NONE;
    task->tOwSprite = SPRITE_NONE;
    LoadMessageBoxAndBorderGfx();
    task->tWindowId = AddWindow(&sWindowTemplate);
    DrawStdWindowFrame(task->tWindowId, FALSE);
    PutWindowTilemap(task->tWindowId);
    DrawMenu(task);
    CopyWindowToVram(task->tWindowId, COPYWIN_FULL);
    ShowPicture(task);
}
