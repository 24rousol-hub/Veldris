#ifndef GUARD_VELDRIS_JOURNAL_H
#define GUARD_VELDRIS_JOURNAL_H

#include "global.h"

// Veldris Journal (hack-owned file, not upstream). See design/journal.md.
// Using the Journal (bag USE, or SELECT when registered) runs Veldris_EventScript_Journal
// (data/scripts/veldris_journal.inc), which calls VeldrisJournal_FillVars and prints three pages.

// One row per TROGLODYTE fight, in story order (design/troglodyte-arc.md lists eight).
// Add a row when the fight's trainer block and map script are built. Script each fight with
// trainerbattle_single or trainerbattle_no_intro: the tally reads the defeated flag, and
// trainerbattle_earlyrival also sets that flag when the player LOSES (CB2_EndTrainerBattle).
#define VELDRIS_TROGLODYTE_FIGHTS(X) \
    X(TRAINER_TROGLODYTE_HOLLOWBROOK) \
    X(TRAINER_TROGLODYTE_CRESTFALL)

extern const u8 Veldris_EventScript_Journal[];

// callnative from the script. Sets VAR_0x8004 = badges earned, VAR_0x8005 = TROGLODYTE fights won.
void VeldrisJournal_FillVars(void);

#endif // GUARD_VELDRIS_JOURNAL_H
