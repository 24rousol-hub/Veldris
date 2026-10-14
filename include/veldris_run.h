#ifndef GUARD_VELDRIS_RUN_H
#define GUARD_VELDRIS_RUN_H

// Veldris walk/run default toggle (hack-owned file, not upstream). See design/running-shoes.md.
// Flips FLAG_SYS_RUN_BY_DEFAULT when the player presses L in the overworld. Does nothing without the
// Running Shoes (FLAG_SYS_B_DASH) or in the L=A button mode (L is A there).
void VeldrisTryToggleRunDefault(void);

#endif // GUARD_VELDRIS_RUN_H
