# Engine edits log

The rule: keep edits to upstream (pokeemerald-expansion) files minimal, and prefer config switches in `include/config/*.h`, so upstream updates can still be pulled with few conflicts.

**Every edit to a file that exists upstream is logged here, in the same commit.** Hack-only files (everything under `design/`, new maps, new scripts) do not need a row.

Before pulling upstream, read this list. Each row is a place a merge could conflict.

| Date | File | Change | Why | Config switch instead? |
|---|---|---|---|---|
| 2026-09-29 | `.gitignore` | Appended a Veldris block at the end (ROMs, saves, build output). No upstream lines changed. | Public repo: never commit a ROM or save | n/a |
| 2026-09-29 | `CREDITS.md` | Added a hack credits section above the upstream one. Upstream content is untouched. | Credit every third-party asset | n/a |

## Planned edits (not yet made)

| File | Change | Waiting on |
|---|---|---|
| `include/constants/flags.h`, `vars.h` | One-line renames of `FLAG_UNUSED_*` / `VAR_UNUSED_*` as flags and vars are claimed. See [flags.md](flags.md) | First flag use |
| `include/constants/opponents.h` | Trainer slot changes (only 9 free) | Open decision 6 in [game-bible.md](game-bible.md) |
| Badge handling (`flags.h`, `src/event_data.c`, trainer card, main menu) | 9th badge, if chosen | Open decision 1 in [game-bible.md](game-bible.md) |
