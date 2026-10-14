#ifndef GUARD_VELDRIS_FURNITURE_H
#define GUARD_VELDRIS_FURNITURE_H

#include "global.h"

// Talking furniture (hack-owned file, not upstream). See design/furniture-lines.md.
// Returns the flavour script for a furniture metatile behaviour (cabinet, dresser, kitchen, painting, computer...),
// or NULL when the behaviour is not one of them. GetInteractedMetatileScript calls it so the lookups work on
// Emerald-format maps; the stock lookups for the same behaviours sit behind IS_FRLG and never run in this build.
const u8 *VeldrisGetFurnitureScript(u8 metatileBehavior);

#endif // GUARD_VELDRIS_FURNITURE_H
