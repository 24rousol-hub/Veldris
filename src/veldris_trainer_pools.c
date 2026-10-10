#include "global.h"
#include "event_data.h"
#include "trainer_pools.h"
#include "veldris_trainer_pools.h"
#include "constants/vars.h"

// Veldris trainer pool pruning (hack-owned file, not upstream). Called from the POOL_PRUNE_RIVAL_STARTER case in
// PrunePool (src/trainer_pools.c). See design/trainer-roster.md.

//  Veldris: Troglodyte's starter is random, so his pool lists his other Pokemon plus three starter versions
//  tagged TAG6, TAG7 and TAG8 (the 1st, 2nd and 3rd starter on show). VAR_TROG_STARTER holds 0, 1 or 2.
//  Drop the starter versions that do not match. Untagged members stay in the pool.
void VeldrisRivalStarterPrune(const struct Trainer *trainer, u8 *poolIndexArray, const struct PoolRules *rules)
{
    u32 starterTags = MON_POOL_TAG_TAG6 | MON_POOL_TAG_TAG7 | MON_POOL_TAG_TAG8;
    u32 keepTag = MON_POOL_TAG_TAG6;
    u32 choice = VarGet(VAR_TROG_STARTER);

    if (choice == 1)
        keepTag = MON_POOL_TAG_TAG7;
    else if (choice == 2)
        keepTag = MON_POOL_TAG_TAG8;

    for (u32 i = 0; i < trainer->poolSize; i++)
    {
        u32 tags = trainer->party[poolIndexArray[i]].tags;
        if ((tags & starterTags) && !(tags & keepTag))
            poolIndexArray[i] = POOL_SLOT_DISABLED;
    }
}
