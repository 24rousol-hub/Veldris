#include "global.h"
#include "event_data.h"
#include "field_move.h"
#include "pokemon.h"
#include "veldris_badges.h"
#include "veldris_field_moves.h"
#include "constants/field_move.h"
#include "test/test.h"

// Hack-owned tests (not upstream). Run with: make check TESTS='Veldris'

TEST("Veldris: GetBadgeCount counts the 9th badge even though its flag is not contiguous")
{
    u32 i;

    for (i = 0; i < NUM_BADGES; i++)
        FlagClear(gBadgeFlags[i]);
    EXPECT_EQ(GetBadgeCount(), 0);
    FlagSet(FLAG_BADGE09_GET);
    EXPECT_EQ(GetBadgeCount(), 1);
    for (i = 0; i < NUM_BADGES; i++)
        FlagSet(gBadgeFlags[i]);
    EXPECT_EQ(GetBadgeCount(), NUM_BADGES);
}

TEST("Veldris: Dive is gated by badge 9 and Flash by badge 3")
{
    u32 i;

    for (i = 0; i < NUM_BADGES; i++)
        FlagClear(gBadgeFlags[i]);
    EXPECT(!IsFieldMoveUnlocked(FIELD_MOVE_DIVE));
    EXPECT(!IsFieldMoveUnlocked(FIELD_MOVE_FLASH));
    FlagSet(FLAG_BADGE03_GET);
    EXPECT(IsFieldMoveUnlocked(FIELD_MOVE_FLASH));
    EXPECT(!IsFieldMoveUnlocked(FIELD_MOVE_DIVE));
    FlagSet(FLAG_BADGE09_GET);
    EXPECT(IsFieldMoveUnlocked(FIELD_MOVE_DIVE));
}

TEST("Veldris: a party Pokemon that can learn Sweet Scent is the field move user, a non-compat move still needs a knower")
{
    ZeroPlayerPartyMons();
    CreateMon(&gParties[B_TRAINER_PLAYER][0], SPECIES_ODDISH, 10, 0, OTID_STRUCT_PLAYER_ID);
    EXPECT_EQ(FindMonForFieldMove(FIELD_MOVE_SWEET_SCENT), 0);
    EXPECT_EQ(FindMonForFieldMove(FIELD_MOVE_TELEPORT), PARTY_SIZE);
}
