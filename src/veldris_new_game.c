#include "global.h"
#include "clock.h"
#include "event_data.h"
#include "item.h"
#include "rtc.h"
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
#if OW_USE_FAKE_RTC
    // The fake clock starts at 10:00 (author, 2026-10-09). CB2_NewGame repeats this RtcCalcLocalTimeOffset call right after
    // NewGameInitData with the same arguments, so the result is identical. InitTimeBasedEvents sets FLAG_SYS_CLOCK_SET and the
    // day / berry baselines now, so berries and daily events run without a trip to the wall clock. The wall clock in the
    // player's room can still reset the time.
    RtcCalcLocalTimeOffset(0, 10, 0, 0);
    InitTimeBasedEvents();
#endif
}
