# Dialogue style guide

## Voice

- Deadpan and dry. The joke is in the situation, not in shouting.
- The player is silent. Their attitude shows through the choices offered.
- Troglodyte is pompous and clueless. Never cruel. Never swears. *(Under review: the author's 2026-09-29 note says the Goldsworths are rich frat guys who are assholes. Until open decisions 9 and 10 in [game-bible.md](game-bible.md) are answered, these limits stay.)*
- Locals are sincere and slightly odd.
- Keep speeches short. A grudge is funnier when it is brief.

Per-character voice notes are in [characters.md](characters.md).

## Hard technical rules

1. **No double quotes.** The charmap has no plain double quote, and even `\"` is a build error. Use single quotes for speech, and type the **curly** ones so the opening quote looks right: ‘Well, that went badly.’ The ASCII apostrophe `'` always shows the closing glyph, so it is fine inside words (who's) but wrong as an opening quote.
2. **Never use `{RIVAL}`.** It expands to MAY or BRENDAN, chosen by the player's gender (`src/string_util.c`). Write TROGLODYTE.
3. **Use `{PLAYER}`** for the player's name. `{STR_VAR_1}` to `{STR_VAR_3}` are the script buffers.
4. **Intro dialogue** is C-driven. Edit `data/text/birch_speech.inc` (used by `src/main_menu.c`). The 'This is what we call a POKéMON' line is in `src/strings.c` instead.
5. **Map scripts** are hand-written `scripts.inc`, not Poryscript.
6. **Cutscenes** start from `coord_event` triggers.

## Text format in `scripts.inc`

```
Crestfall_Text_GretaGreeting:
	.string "Well now. You must be the one\n"
	.string "who's been chasing that boy.\p"
	.string "I told him, ‘Not on my farm.’$"
```

The double quotes that wrap each `.string` line are assembler syntax and are correct. Rule 1 is about the text **inside** them: speech inside a line uses curly single quotes, as in the last line above.

Control codes:

| Code | Meaning |
|---|---|
| `\n` | New line in the same box |
| `\l` | Scroll to the next line |
| `\p` | New paragraph, waits for a button press |
| `$` | Ends the string. Every `.string` must end with it |

## Line length

**Measured from the source (2026-09-29), not a guess:**

- The ordinary overworld text box and the intro box are both **27 tiles wide, which is 216 px, and 2 lines tall** (`sStandardTextBox_WindowTemplates` in `src/menu.c`, `sNewGameBirchSpeechTextWindows` in `src/main_menu.c`). Battle text, shops and menus use other windows and are not covered here.
- `FONT_NORMAL` adds no letter spacing, so a line's width is just the sum of its glyph widths (`gFontNormalLatinGlyphWidths` in `src/fonts.c`). Letters differ in width, so "characters per line" is only a guide (about 34 for ordinary text).
- **Keep every line at 208 px or less.** The hard limit is 216 px. Vanilla's own widest intro line is 184 px.
- A page shows two lines. A third line scrolls in with `\l`. `\p` starts a new page.
- `{PLAYER}` counts as 42 px (seven wide letters). `{STR_VAR_1}` to `{STR_VAR_3}` have unknown length, so leave room.

**Check every dialogue file before committing:**

```
python3 design/tools/dialogue_check.py data/maps/<Map>/scripts.inc
```

It uses the game's own widths, and it also flags characters missing from the charmap, an escaped double quote, `{RIVAL}` and a missing `$`. It exits 1 on any error. Warnings (a line close to the limit, or one that only overflows if a `{STR_VAR}` is long) do not fail it.

To judge tone and fit without an emulator, screens can be rendered in the game's font from `graphics/fonts/latin_normal.png` (needs Pillow). That renderer is a throwaway, not a committed tool.

## Naming text labels

`<Map>_Text_<Speaker><Purpose>`, for example `Crestfall_Text_GretaGreeting`. Keep labels unique across the project.
