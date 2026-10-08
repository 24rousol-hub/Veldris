#ifndef GUARD_VELDRIS_FIELD_MOVES_H
#define GUARD_VELDRIS_FIELD_MOVES_H

#include "global.h"
#include "constants/field_move.h"

// Veldris field moves (hack-owned file, not upstream). See design/field-moves.md.
// Rule (author, 2026-10-08): a field move works in the open world when
//   (1) its badge is earned (gFieldMoveInfo[].unlockType, src/field_move.c), AND
//   (2) a party Pokemon KNOWS the move or CAN LEARN it. No move slot is needed.
// Rule (2) applies to the moves in VELDRIS_COMPAT_FIELD_MOVES (src/veldris_field_moves.c);
// every other field move keeps the vanilla rule (a party Pokemon knows it).

// Party slot of the user: a non-egg Pokemon that knows the move first, else (compat moves only)
// the first non-egg Pokemon that can learn it. PARTY_SIZE if there is none.
u32 FindMonForFieldMove(enum FieldMove fieldMove);

// Dry run of the vanilla SetUpFieldMove_*: TRUE if the move is usable right here, right now.
// Saves and restores gFieldCallback2 / gPostMenuFieldCallback.
bool32 CanUseFieldMoveHere(enum FieldMove fieldMove);

// Party menu: who really uses the move picked in the menu of selectedSlot.
u32 GetFieldMoveUserSlot(enum FieldMove fieldMove, u32 selectedSlot);

// Party menu: append menu entries (actionBase + fieldMove) for compat moves that are unlocked,
// not already listed, have a user in the party and are usable here. Stops at maxActions entries.
// Returns the new entry count.
u32 AppendCompatFieldMoveActions(u8 *actions, u32 numActions, u32 maxActions, u32 actionBase);

#endif // GUARD_VELDRIS_FIELD_MOVES_H
