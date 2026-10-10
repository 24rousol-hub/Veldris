#include "global.h"
#include "rtc.h"
#include "veldris_badges.h"
#include "constants/field_move.h"
#include "constants/flags.h"
#include "constants/opponents.h"

// Veldris build-time guards (hack-owned, no code is emitted). Each line pins something a doc, a tool or the
// author's saves rely on. If one fires, read the message, then either undo the change or update the pin AND the doc.

// Save layout is frozen (design/devices.md): any change breaks every dev save and Delta / Miyoo save.
// Measured 2026-10-09; only SaveBlock3 differs from upstream (4 to 16 bytes, OW_USE_FAKE_RTC).
STATIC_ASSERT(sizeof(struct SaveBlock1) == 15568, VeldrisSaveBlock1LayoutChanged);
STATIC_ASSERT(sizeof(struct SaveBlock2) == 3884, VeldrisSaveBlock2LayoutChanged);
STATIC_ASSERT(sizeof(struct SaveBlock3) == 16, VeldrisSaveBlock3LayoutChanged);
STATIC_ASSERT(MAX_TRAINERS_COUNT == 864, VeldrisTrainerFlagSpaceChanged);

// design/time-of-day.md and design/tools/wild_lint.py assume a plain wild table is the Day table.
STATIC_ASSERT(OW_USE_FAKE_RTC == TRUE, VeldrisFakeClockOff);
STATIC_ASSERT(OW_TIME_OF_DAY_FALLBACK == TIME_DAY, VeldrisTimeOfDayFallbackNotDay);

// src/veldris_field_moves.c keeps one bit per field move in a u32.
STATIC_ASSERT(FIELD_MOVES_COUNT <= 32, VeldrisFieldMoveMaskTooSmall);

// Every badge's icon slot must be a real art slot and not the empty socket (include/veldris_badges.h).
#define BADGE_SLOT_OK(flag, slot) && (slot) < BADGE_ICON_SLOT_EMPTY
STATIC_ASSERT(1 VELDRIS_BADGE_LIST(BADGE_SLOT_OK), VeldrisBadgeIconSlotOutOfRange);
