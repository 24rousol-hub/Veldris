#include "global.h"
#include "battle.h"
#include "battle_transition.h"
#include "data.h"
#include "trainer_pools.h"
#include "event_data.h"
#include "field_move.h"
#include "pokemon.h"
#include "veldris_badges.h"
#include "veldris_field_moves.h"
#include "constants/abilities.h"
#include "constants/battle_ai.h"
#include "constants/field_move.h"
#include "constants/items.h"
#include "constants/moves.h"
#include "constants/opponents.h"
#include "constants/trainers.h"
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

// The AI ladder. The author asked on 2026-10-12 for a 'short AI ladder weak to better but not crazy good'; the rungs and who
// stands on which are my applied reading of that. Three rungs, and leaders 3 to 9, the Elite Four and Cynthia also get
// Ace Pokemon. Keep in step with LADDER in design/tools/trainer_lint.py and with the AI: lines in src/data/trainers.party.
// Not listed: Greta's two gym trainers and the Route 1 trio stay as they were built.
#define VELDRIS_AI_DIM   (AI_FLAG_CHECK_BAD_MOVE)
#define VELDRIS_AI_BASIC (AI_FLAG_BASIC_TRAINER)
#define VELDRIS_AI_SHARP (AI_FLAG_BASIC_TRAINER | AI_FLAG_HP_AWARE | AI_FLAG_TRY_TO_2HKO)
#define VELDRIS_AI_ACE   (AI_FLAG_ACE_POKEMON)
// 'Not crazy good': nothing outside the three rungs and Ace Pokemon may be set. This allowed mask is the same list as
// ALLOWED_AI in design/tools/trainer_lint.py, so any smart, omniscient, assuming or predicting flag fails the test.
#define VELDRIS_AI_ALLOWED ((u64)(VELDRIS_AI_DIM | VELDRIS_AI_BASIC | VELDRIS_AI_SHARP | VELDRIS_AI_ACE))

// The unit-test build swaps gTrainers (src/data.c) for a tiny stub in test/test_runner_battle.c, so
// GetTrainerAIFlagsFromId() cannot see the real trainers here. This compiles its own copy of the generated trainer
// data (src/data/trainers.h, built from trainers.party) and reads the AI flags from that. Only this file uses it.
static const struct Trainer sVeldrisTrainers[DIFFICULTY_COUNT][TRAINERS_COUNT] =
{
#include "../src/data/trainers.h"
};

// aiFlags is a u64, so compare with EXPECT (EXPECT_EQ would print it with %d). One line per trainer: a failure
// reports this file's line number, which names the trainer.
#define VELDRIS_AI_FLAGS_OF(trainer) (sVeldrisTrainers[DIFFICULTY_NORMAL][trainer].aiFlags)
#define EXPECT_AI_LADDER(trainer, flags) \
    do \
    { \
        EXPECT(VELDRIS_AI_FLAGS_OF(trainer) == (flags)); \
        EXPECT((VELDRIS_AI_FLAGS_OF(trainer) & ~VELDRIS_AI_ALLOWED) == 0); \
    } while (0)

TEST("Veldris: AI ladder gives the 16 ladder trainers exactly their rung and no smart flags")
{
    // Troglodyte: Dim, never Ace (his party order is random).
    EXPECT_AI_LADDER(TRAINER_TROGLODYTE_HOLLOWBROOK, VELDRIS_AI_DIM);
    EXPECT_AI_LADDER(TRAINER_TROGLODYTE_CRESTFALL, VELDRIS_AI_DIM);
    // Gyms 1 and 2 stay Basic with no Ace (two Pokemon each, so the second is always the last).
    EXPECT_AI_LADDER(TRAINER_CRESTFALL_GRETA, VELDRIS_AI_BASIC);
    EXPECT_AI_LADDER(TRAINER_HACHIMEL, VELDRIS_AI_BASIC);
    // Gym 3 is Basic, gyms 4 to 9 are Sharp, all with Ace.
    EXPECT_AI_LADDER(TRAINER_SANZUFORD, VELDRIS_AI_BASIC | VELDRIS_AI_ACE);
    EXPECT_AI_LADDER(TRAINER_HAGANE, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
    EXPECT_AI_LADDER(TRAINER_WAKASAGI, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
    EXPECT_AI_LADDER(TRAINER_TOBIN, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
    EXPECT_AI_LADDER(TRAINER_ASEBY, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
    EXPECT_AI_LADDER(TRAINER_SUZURAN, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
    EXPECT_AI_LADDER(TRAINER_MIZZLE, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
    // Elite Four and Champion: Sharp with Ace.
    EXPECT_AI_LADDER(TRAINER_OSSIAN, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
    EXPECT_AI_LADDER(TRAINER_HYACINTH, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
    EXPECT_AI_LADDER(TRAINER_DRAYDEN, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
    EXPECT_AI_LADDER(TRAINER_DUNMORE, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
    EXPECT_AI_LADDER(TRAINER_CYNTHIA, VELDRIS_AI_SHARP | VELDRIS_AI_ACE);
}
