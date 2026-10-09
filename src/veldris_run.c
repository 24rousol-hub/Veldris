#include "global.h"
#include "event_data.h"
#include "sound.h"
#include "veldris_run.h"
#include "constants/songs.h"

// Veldris walk/run default toggle (hack-owned). FLAG_SYS_RUN_BY_DEFAULT set: the player runs unless B is held.
// Set is the new-game default (VeldrisNewGameDefaults, author 2026-10-09); clear is vanilla, B runs. Called from FieldGetPlayerInput when L is pressed and the
// field controls are not locked.
void VeldrisTryToggleRunDefault(void)
{
    if (!FlagGet(FLAG_SYS_B_DASH))
        return; // no Running Shoes yet
    if (gSaveBlock2Ptr->optionsButtonMode == OPTIONS_BUTTON_MODE_L_EQUALS_A)
        return; // L is A in this mode (src/main.c)

    FlagToggle(FLAG_SYS_RUN_BY_DEFAULT);
    PlaySE(FlagGet(FLAG_SYS_RUN_BY_DEFAULT) ? SE_PC_LOGIN : SE_PC_OFF);
}
