# Test and target devices: the phone (Delta) now, the Miyoo Mini Plus later (author 2026-10-09)

Status: **research and ROM checks done 2026-10-09; nothing has been run on either device yet.** Emulator facts below come from community reports and a look at Delta's public repository, not from running them, so treat them as 'likely' until tried.

## The phone: Delta (where the author tests now)

- **Delta's GBA core looks like VBA-M, not mGBA.** Its public repository (`GBADeltaCore`) pulls in `visualboyadvance-m` as a submodule; the README does not say so, so this is an inference. It matters because **the headless test tools in this project use mGBA**: the two emulators agree on almost everything, but a bug that shows only on the phone is worth reporting with the exact steps (what you pressed, where you were) because I cannot reproduce VBA-M here.
- **Save states break whenever the ROM is rebuilt** (the game's memory layout moves). Use **in-game saves** for progress and treat Delta save states as throwaway. In-game saves survive a rebuild as long as the save layout does not change: new flags and vars in spare slots are safe, new struct fields are not (the fake clock grew SaveBlock3 by 12 bytes once, 4 to 16; old test saves just read the clock as 00:00). Rule for the hack: **do not change `SaveBlock1/2/3` or the Pokémon storage layout without telling the author**; the debug presets (R+START, Scripts) are the fast way back to any scene after a rebuild.
- **The debug menu is on the dev ROM** (R+START, with Delta's on-screen R and START pressed together, or a controller). Presets 1 to 8 (new game, lab scene, Troglodyte fight 1, Crestfall gym and so on) rewind to a scene in a few taps: see [debug-presets.md](debug-presets.md). The title screen has a SELECT quickstart that skips the intro.
- **Getting a new build onto the phone:** I send `veldris_<date>.zip` (about 17 MB; the ROM inside is the usual 32 MiB padded file). Tap it in the chat, let Files unzip it, then share the `.gba` to Delta. I could not confirm how Delta pairs a save with a changed ROM file (by name or by a hash of the file); **check once** that your in-game save is still there after replacing the ROM, and if Delta lists it as a new game, import the old save file into the new entry. Keep the same file name each time.
- **Keep the ROM at its full 32 MiB size** (a power of two). A developer report says non-power-of-two ROMs can break the real clock in some emulators; we use the fake clock so it would not matter, but there is no reason to risk it, so I do not trim the padding.
- **Clock:** the fake clock is stored in the save, so it does not depend on the phone's time, the emulator or time zones. A real-clock hack on an emulator is a common source of stuck-at-night bugs.

## The Miyoo Mini Plus (later)

### The ROM size limit (both devices)

- **The 32 MiB cap is the Game Boy Advance itself** (the cartridge address space), not an emulator rule. Every GBA ROM, including this one, must fit in 32 MiB. The build always writes a 32 MiB file because the unused tail is padded with `FF`.
- **Used on 2026-10-10: 25.81 MiB. Free: 6.19 MiB** (measured on the dev build of that day as the length of `pokeemerald.gba` without its trailing `FF` padding, 27,060,492 bytes; it was 25.58 MiB on 2026-10-09, and the DP sprite import, 70 overworld sprites and 94 battle pictures, added about 0.23 MiB; the unmodified engine uses about 25.5 MiB, so the whole hack so far costs about 0.3 MiB). Re-measure after a build with `python3 -c "b=open('pokeemerald.gba','rb').read().rstrip(b'\xff'); print(len(b), len(b)/2**20)"`. The planned content (maps, scripts and dialogue for the other 16 towns and 32 routes) is text and small data, not new engine, so it should fit; watch it with `arm-none-eabi-size -A pokeemerald.elf` (script_data and .rodata).
- RAM is the other real limit and the hack barely touches it: EWRAM +8 bytes, IWRAM +0 bytes over the unmodified engine (EWRAM about 35 KB free, IWRAM about 4 KB free, same as vanilla expansion).

### What the Miyoo's emulators do with it (reports, not tests)

| Topic | What was found | What it means for Veldris |
|---|---|---|
| Cores | The Mini Plus ships with both gpSP and mGBA for GBA. One user reported mGBA is the default on the Plus and that gpSP was faster there | Try **mGBA first** (accurate), and gpSP if it stutters |
| 32 MB ROMs in gpSP | The gpSP compatibility list says a 32 MB ROM **only works unzipped** | Put the unzipped `.gba` on the card, never the `.zip` |
| Softpatching | Works in mGBA, not in gpSP | We ship a whole ROM, not a patch, so this does not matter |
| RTC (real-time clock) | A tester reported **gpSP's clock still does not work for Pokémon Emerald** on Onion 4.4.0-beta2; the workaround was to use mGBA | **Our fake clock removes this problem**: the in-game clock is saved in the save file and does not read the device (`OW_USE_FAKE_RTC`, see [time-of-day.md](time-of-day.md)) |
| Save type | The ROM contains the standard `FLASH1M_V103` marker near the start (offset 0x20E8), so cores that pick the save type from the ROM find it. Saves are 128 KiB | No 32 MB save is involved (the gpSP list says 32 MB saves are unsupported) |

Nobody found a report of a pokeemerald-expansion ROM on the Miyoo Mini Plus either way. The only real answer is a test.

### Build for the device

- Use **`make release`**. It turns on `RELEASE` (optimised, link-time optimisation, `NDEBUG`) and **removes the debug menu and the title-screen quickstart**, which sit on R+START and SELECT and are easy to hit by accident on a handheld. The output is `pokeemerald-release.gba` (a separate file, so the dev ROM is not overwritten).
- The dev ROM keeps the debug menu, which is what the test tools use. Never put the dev ROM on the device for real play.
- Release build check on 2026-10-09: see the table at the bottom.

### Things that could hurt on a slow core (not measured)

- **Day and night tint** (`OW_ENABLE_DNS`) blends the palettes when the time of day changes. A cheap fallback if the device stutters is to turn that one switch off in `include/config/overworld.h`; the night tables still work.
- **Followers, weather and light effects** are the other heavy overworld features of the engine; none is used by Veldris content beyond what the engine does by default.
- The **screen**: the Mini Plus is 640 x 480, so a 240 x 160 GBA picture scales to 2x with borders, or to a stretched fill. Text boxes were measured for the real GBA screen (216 px by 2 lines), so nothing needs redoing for the device.
- **Buttons**: the run toggle is on **L**, mapped to the Miyoo's L shoulder. Avoid giving anything a job on L2 or R2.

### Device test checklist (when you have the handheld)

1. Copy the unzipped `pokeemerald-release.gba` to the GBA folder. Start it in mGBA, then in gpSP.
2. Boot, new game: the intro plays, no debug menu, SELECT on the title does nothing.
3. Save, power off, load: the save survives and the clock still reads the time you set.
4. Walk Hollowbrook and Route 1: frame rate (no slowdown), the night tint, running by default.
5. Battle Troglodyte: the gold banner, the music, no audio crackle.
6. Open the Pokédex, the bag and the Journal; check the text is readable at the handheld's scale.

### Release build check

| Check | Result |
|---|---|
| `make release` builds the whole tree (2026-10-09, about 20 minutes with the link-time optimisation on 2 cores) | Pass, 0 errors; 7 warnings, all upstream link-time notes (for example `faraway_island.c` declares `GetMewMoveDirection` with two different types), none in hack code |
| Release ROM size | 25.68 MiB used on the 2026-10-09 build (the optimised code is bigger, the debug strings are gone), so 6.3 MiB free; still padded to 32 MiB; the Flash save marker is at the same offset, 0x20E8. Not re-measured since the DP sprite import, which grew the dev ROM by about 0.23 MiB, so expect about 25.9 MiB now; run `make release` and measure as above |
| RAM | EWRAM 226,414 bytes, IWRAM 28,312 bytes: the same as the dev build, nothing to worry about |
| Debug menu and quickstart in the release ROM | Compiled out by `DISABLED_ON_RELEASE`; not played on a device yet |
