# Playing on a Miyoo Mini Plus (target device, author 2026-10-09)

Status: **research and ROM checks done 2026-10-09; nothing has been run on a real device.** All emulator facts below come from community reports, not from the emulator's source, so treat them as 'likely' until the ROM is tried on the handheld.

## The ROM size limit

- **The 32 MiB cap is the Game Boy Advance itself** (the cartridge address space), not an emulator rule. Every GBA ROM, including this one, must fit in 32 MiB. The build always writes a 32 MiB file because the unused tail is padded with `FF`.
- **Used today: 25.58 MiB. Free: 6.42 MiB** (measured on the 2026-10-09 build; the unmodified engine uses about 25.5 MiB, so the whole hack so far costs about 0.08 MiB). The planned content (maps, scripts and dialogue for the other 16 towns and 32 routes) is text and small data, not new engine, so it should fit; watch it with `arm-none-eabi-size -A pokeemerald.elf` (script_data and .rodata).
- RAM is the other real limit and the hack barely touches it: EWRAM +8 bytes, IWRAM +0 bytes over the unmodified engine (EWRAM about 35 KB free, IWRAM about 4 KB free, same as vanilla expansion).

## What the Miyoo's emulators do with it (reports, not tests)

| Topic | What was found | What it means for Veldris |
|---|---|---|
| Cores | The Mini Plus ships with both gpSP and mGBA for GBA. One user reported mGBA is the default on the Plus and that gpSP was faster there | Try **mGBA first** (accurate), and gpSP if it stutters |
| 32 MB ROMs in gpSP | The gpSP compatibility list says a 32 MB ROM **only works unzipped** | Put the unzipped `.gba` on the card, never the `.zip` |
| Softpatching | Works in mGBA, not in gpSP | We ship a whole ROM, not a patch, so this does not matter |
| RTC (real-time clock) | A tester reported **gpSP's clock still does not work for Pokémon Emerald** on Onion 4.4.0-beta2; the workaround was to use mGBA | **Our fake clock removes this problem**: the in-game clock is saved in the save file and does not read the device (`OW_USE_FAKE_RTC`, see [time-of-day.md](time-of-day.md)) |
| Save type | The ROM contains the standard `FLASH1M_V103` marker near the start (offset 0x20E8), so cores that pick the save type from the ROM find it. Saves are 128 KiB | No 32 MB save is involved (the gpSP list says 32 MB saves are unsupported) |

Nobody found a report of a pokeemerald-expansion ROM on the Miyoo Mini Plus either way. The only real answer is a test.

## Build for the device

- Use **`make release`**. It turns on `RELEASE` (optimised, link-time optimisation, `NDEBUG`) and **removes the debug menu and the title-screen quickstart**, which sit on R+START and SELECT and are easy to hit by accident on a handheld. The output is `pokeemerald-release.gba` (a separate file, so the dev ROM is not overwritten).
- The dev ROM keeps the debug menu, which is what the test tools use. Never put the dev ROM on the device for real play.
- Release build check on 2026-10-09: see the table at the bottom.

## Things that could hurt on a slow core (not measured)

- **Day and night tint** (`OW_ENABLE_DNS`) blends the palettes when the time of day changes. A cheap fallback if the device stutters is to turn that one switch off in `include/config/overworld.h`; the night tables still work.
- **Followers, weather and light effects** are the other heavy overworld features of the engine; none is used by Veldris content beyond what the engine does by default.
- The **screen**: the Mini Plus is 640 x 480, so a 240 x 160 GBA picture scales to 2x with borders, or to a stretched fill. Text boxes were measured for the real GBA screen (216 px by 2 lines), so nothing needs redoing for the device.
- **Buttons**: the run toggle is on **L**, mapped to the Miyoo's L shoulder. Avoid giving anything a job on L2 or R2.

## Device test checklist (when you have the handheld)

1. Copy the unzipped `pokeemerald-release.gba` to the GBA folder. Start it in mGBA, then in gpSP.
2. Boot, new game: the intro plays, no debug menu, SELECT on the title does nothing.
3. Save, power off, load: the save survives and the clock still reads the time you set.
4. Walk Hollowbrook and Route 1: frame rate (no slowdown), the night tint, running by default.
5. Battle Troglodyte: the gold banner, the music, no audio crackle.
6. Open the Pokédex, the bag and the Journal; check the text is readable at the handheld's scale.

## Release build check

| Check | Result |
|---|---|
| `make release` builds the whole tree | pending (see the log below when it finishes) |
