#ifndef GUARD_VELDRIS_TRAINER_POOLS_H
#define GUARD_VELDRIS_TRAINER_POOLS_H

#include "global.h"
#include "data.h"

struct PoolRules;

// POOL_PRUNE_RIVAL_STARTER: keeps only the starter version that matches VAR_TROG_STARTER (hack-owned, not upstream).
void VeldrisRivalStarterPrune(const struct Trainer *trainer, u8 *poolIndexArray, const struct PoolRules *rules);

#endif // GUARD_VELDRIS_TRAINER_POOLS_H
