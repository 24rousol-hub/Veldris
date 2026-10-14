#ifndef GUARD_VELDRIS_TRAINER_POOLS_H
#define GUARD_VELDRIS_TRAINER_POOLS_H

#include "global.h"
#include "data.h"

struct PoolRules;

// POOL_PRUNE_RIVAL_STARTER: keeps only the starter version that matches VAR_TROG_STARTER (hack-owned, not upstream).
// VAR_TROG_STARTER 0, 1, 2 = ball 1, 2, 3 on show = party-file tag Tag6, Tag7, Tag8 (Chikorita, Cyndaquil, Totodile).
void VeldrisRivalStarterPrune(const struct Trainer *trainer, u8 *poolIndexArray, const struct PoolRules *rules);

#endif // GUARD_VELDRIS_TRAINER_POOLS_H
