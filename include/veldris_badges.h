#ifndef GUARD_VELDRIS_BADGES_H
#define GUARD_VELDRIS_BADGES_H

// Veldris badge table (hack-owned file, not upstream). See design/badges.md.
//
// One row per badge, in display order on the trainer card:
//   X(flag, iconSlot)
// flag:     the badge's flag. Badges 1-8 keep the vanilla contiguous flags,
//           badge 9 is FLAG_BADGE09_GET. Any flag may be used.
// iconSlot: which 16x16 cell of graphics/trainer_card/badges.png to draw
//           (0-7 = top row of the sheet, 8-15 = bottom row). Reorder or
//           reuse slots to mix and match badge art.
// The row count must equal NUM_BADGES (include/constants/flags.h).
// All badges share one 16-colour palette (BG palette bank 3 on the card).
#define VELDRIS_BADGE_LIST(X) \
    X(FLAG_BADGE01_GET, 0) \
    X(FLAG_BADGE02_GET, 1) \
    X(FLAG_BADGE03_GET, 2) \
    X(FLAG_BADGE04_GET, 3) \
    X(FLAG_BADGE05_GET, 4) \
    X(FLAG_BADGE06_GET, 5) \
    X(FLAG_BADGE07_GET, 6) \
    X(FLAG_BADGE08_GET, 7) \
    X(FLAG_BADGE09_GET, 8)

#define BADGE_ICON_SLOTS_PER_SHEET_ROW 8
#define NUM_BADGE_ICON_SLOTS           16

struct VeldrisBadge
{
    u16 flag;
    u8 iconSlot;
};

extern const struct VeldrisBadge gVeldrisBadges[NUM_BADGES];

u32 GetBadgeCount(void);

#endif // GUARD_VELDRIS_BADGES_H
