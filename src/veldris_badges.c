#include "global.h"
#include "event_data.h"
#include "veldris_badges.h"

#define BADGE_ROW(flag, slot) { flag, slot },
#define BADGE_FLAG(flag, slot) flag,
#define BADGE_COUNT(flag, slot) + 1

STATIC_ASSERT(0 VELDRIS_BADGE_LIST(BADGE_COUNT) == NUM_BADGES, VeldrisBadgeListMatchesNumBadges);

const struct VeldrisBadge gVeldrisBadges[NUM_BADGES] =
{
    VELDRIS_BADGE_LIST(BADGE_ROW)
};

// Every "for each badge" loop in the engine goes through this array.
const u16 gBadgeFlags[NUM_BADGES] =
{
    VELDRIS_BADGE_LIST(BADGE_FLAG)
};

u32 GetBadgeCount(void)
{
    u32 i, count = 0;

    for (i = 0; i < NUM_BADGES; i++)
    {
        if (FlagGet(gBadgeFlags[i]))
            count++;
    }
    return count;
}
