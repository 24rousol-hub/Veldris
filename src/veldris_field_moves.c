#include "global.h"
#include "field_effect.h"
#include "field_move.h"
#include "overworld.h"
#include "party_menu.h"
#include "pokemon.h"
#include "veldris_field_moves.h"
#include "constants/battle.h"
#include "constants/field_move.h"

// Veldris field moves (hack-owned file, not upstream). See design/field-moves.md.
// A field move in this set works when a party Pokemon KNOWS it or CAN LEARN it (no move slot used).
// Everything not listed keeps the vanilla rule: a party Pokemon must know the move.
// Dig, Teleport, Milk Drink, Soft-Boiled, Secret Power, Rock Climb and Defog are deliberately NOT here.
#define COMPAT_BIT(fieldMove) (1u << (fieldMove))
#define VELDRIS_COMPAT_FIELD_MOVES \
    (COMPAT_BIT(FIELD_MOVE_CUT) | COMPAT_BIT(FIELD_MOVE_FLASH) | COMPAT_BIT(FIELD_MOVE_ROCK_SMASH) \
   | COMPAT_BIT(FIELD_MOVE_STRENGTH) | COMPAT_BIT(FIELD_MOVE_SURF) | COMPAT_BIT(FIELD_MOVE_FLY) \
   | COMPAT_BIT(FIELD_MOVE_DIVE) | COMPAT_BIT(FIELD_MOVE_WATERFALL) | COMPAT_BIT(FIELD_MOVE_SWEET_SCENT))

static bool32 IsCompatFieldMove(u32 fieldMove)
{
    return (VELDRIS_COMPAT_FIELD_MOVES >> fieldMove) & 1;
}

// Sweet Scent is not a TM/HM/tutor move, so it is missing from the generated teachable list;
// the level-up learnset (any level) covers it. Egg moves are not counted.
static bool32 SpeciesLevelUpLearns(enum Species species, enum Move move)
{
    const struct LevelUpMove *learnset = GetSpeciesLevelUpLearnset(species);

    for (u32 i = 0; learnset[i].move != LEVEL_UP_MOVE_END; i++)
    {
        if (learnset[i].move == move)
            return TRUE;
    }
    return FALSE;
}

static bool32 MonCanLearnFieldMove(struct Pokemon *mon, u32 fieldMove)
{
    enum Species species = GetMonData(mon, MON_DATA_SPECIES);
    enum Move move = FieldMove_GetMoveId(fieldMove);

    return CanLearnTeachableMove(species, move) || SpeciesLevelUpLearns(species, move);
}

u32 FindMonForFieldMove(enum FieldMove fieldMove)
{
    enum Move move = FieldMove_GetMoveId(fieldMove);
    u32 firstLearner = PARTY_SIZE;

    for (u32 i = 0; i < PARTY_SIZE; i++)
    {
        struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][i];

        if (GetMonData(mon, MON_DATA_SPECIES) == SPECIES_NONE)
            break;
        if (GetMonData(mon, MON_DATA_IS_EGG))
            continue;
        if (MonKnowsMove(mon, move))
            return i; // a Pokemon that knows the move always wins
        if (firstLearner == PARTY_SIZE && IsCompatFieldMove(fieldMove) && MonCanLearnFieldMove(mon, fieldMove))
            firstLearner = i;
    }
    return firstLearner;
}

// Dry run of the vanilla SetUpFieldMove_*: TRUE if the move is usable right here, right now, by the Pokemon in userSlot.
// Saves and restores gFieldCallback2 / gPostMenuFieldCallback. Some SetUp functions also leave scratch state
// (gSpecialVar_Result, Cut's tile tables, the dive warp); all of it is rewritten when the move is really used.
static bool32 CanUseFieldMoveHere(enum FieldMove fieldMove, u32 userSlot)
{
    bool8 (*savedFieldCallback2)(void) = gFieldCallback2;
    void (*savedPostMenuCallback)(void) = gPostMenuFieldCallback;
    s8 savedSlot = gPartyMenu.slotId;
    bool32 usable;

    gPartyMenu.slotId = userSlot; // SetUpFieldMove_Cut reads the user's Ability through GetCursorSelectionMonId()
    usable = SetUpFieldMove(fieldMove);
    gPartyMenu.slotId = savedSlot;
    gFieldCallback2 = savedFieldCallback2;
    gPostMenuFieldCallback = savedPostMenuCallback;
    return usable;
}

u32 GetFieldMoveUserSlot(enum FieldMove fieldMove, u32 selectedSlot)
{
    u32 slot;

    if (!IsCompatFieldMove(fieldMove) || MonKnowsMove(&gParties[B_TRAINER_PLAYER][selectedSlot], FieldMove_GetMoveId(fieldMove)))
        return selectedSlot; // vanilla: the picked Pokemon knows it
    slot = FindMonForFieldMove(fieldMove);
    return (slot == PARTY_SIZE) ? selectedSlot : slot;
}

u32 AppendCompatFieldMoveActions(u8 *actions, u32 numActions, u32 maxActions, u32 actionBase)
{
    for (u32 fieldMove = 0; fieldMove < FIELD_MOVES_COUNT && numActions < maxActions; fieldMove++)
    {
        u32 i, user;

        if (!IsCompatFieldMove(fieldMove) || !IsFieldMoveUnlocked(fieldMove))
            continue;
        for (i = 0; i < numActions; i++) // the picked Pokemon knows it: vanilla already listed it
        {
            if (actions[i] == actionBase + fieldMove)
                break;
        }
        if (i < numActions)
            continue;
        user = FindMonForFieldMove(fieldMove);
        if (user == PARTY_SIZE || !CanUseFieldMoveHere(fieldMove, user))
            continue;
        actions[numActions++] = actionBase + fieldMove;
    }
    return numActions;
}
