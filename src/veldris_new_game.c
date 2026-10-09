#include "global.h"
#include "event_data.h"
#include "item.h"
#include "veldris_new_game.h"
#include "constants/flags.h"
#include "constants/items.h"

// Things every new Veldris save starts with (author, 2026-10-09):
// - the Exp. Share key item is in the bag and switched on (the whole party gains Exp),
// - run-by-default is on, so the player runs the moment Mom hands over the Running Shoes
//   (the shoes flag, FLAG_SYS_B_DASH, still gates running; holding B walks, L flips it back).
void VeldrisNewGameDefaults(void)
{
    AddBagItem(ITEM_EXP_SHARE, 1);
    FlagSet(FLAG_SYS_EXP_SHARE_ON);
    FlagSet(FLAG_SYS_RUN_BY_DEFAULT);
}
