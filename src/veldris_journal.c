#include "global.h"
#include "battle_setup.h"
#include "event_data.h"
#include "veldris_badges.h"
#include "veldris_journal.h"
#include "constants/opponents.h"

// Veldris Journal (hack-owned file, not upstream). See design/journal.md.

#define TROGLODYTE_FIGHT_ROW(trainerId) trainerId,

static const u16 sTroglodyteFights[] =
{
    VELDRIS_TROGLODYTE_FIGHTS(TROGLODYTE_FIGHT_ROW)
};

void VeldrisJournal_FillVars(void)
{
    u32 i, losses = 0;

    for (i = 0; i < ARRAY_COUNT(sTroglodyteFights); i++)
    {
        if (HasTrainerBeenFought(sTroglodyteFights[i]))
            losses++;
    }

    gSpecialVar_0x8004 = GetBadgeCount();
    gSpecialVar_0x8005 = losses;
}
