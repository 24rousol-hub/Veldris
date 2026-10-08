# Dialogue style guide

## Voice

- Deadpan and dry. The joke is in the situation, not in shouting.
- The player is silent. Their attitude shows through the choices offered.
- Troglodyte is pompous and clueless. The Goldsworths are rich frat guys who are assholes (author, 2026-09-29), except the kind old grandfather.
- **Two kinds of Goldsworth asshole (author):** the wider family looks down on ordinary people on purpose. Troglodyte's parents are assholes by obliviousness: they live in luxury and do not understand the lower classes, and do not dislike them. Write the parents as well-meaning and patronising, and the rest as contemptuous. Troglodyte starts out contemptuous, like the wider family, and can change to oblivious and confused after certain story points that are not decided yet (author). Keep his lines easy to swap between the two modes (open decision 13 in [game-bible.md](game-bible.md)).
- **Swearing (author, 2026-09-29): only the Goldsworths can swear, and nothing '4chan level'.** Working limit, PROPOSED wording of that: everyday swearing at about the level of a PG-13 film. No slurs of any kind, nothing sexual or graphic, nothing hateful. A little goes a long way: a swear is funnier as punctuation than as every line. The grandfather does not swear. Everyone else (Fennick, Greta, the locals) stays clean unless the author says otherwise.
- Nobody in the family is cruel to innocent townsfolk (assumed, not yet confirmed). Being rude to the player is fine.
- Locals are sincere and slightly odd.
- **Pokémon only (author, 2026-09-29):** no real animals (no hens, cats or cows, even as jokes). Ambient creatures are Pokémon, common and Normal type where possible.
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

- The ordinary overworld text box and the intro box are both **27 tiles wide, which is 216 px, and 2 lines tall** (`sStandardTextBox_WindowTemplates` in `src/menu.c`, `sNewGameBirchSpeechTextWindows` in `src/main_menu.c`). Battle text uses another window (below); shops and menus use others and are not covered here.
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

## Battle text (trainer slides)

- The battle box is 26 tiles = **208 px**, 2 lines per page. The game wraps battle text itself (`BreakStringAutomatic`), so write one plain run of text with no `\n`. A line holds about 200 px of words (8 px is kept for the scroll arrow). More than 2 lines scrolls with an arrow.
- End every slide with `{PAUSE_UNTIL_PRESS}` (the `VELDRIS_SLIDE` macro does it for you). Player name: `{B_PLAYER_NAME}`, never `{PLAYER}` (that prints a battle buffer).
- Check with `python3 design/tools/dialogue_check.py src/data/veldris_trainer_slides.h`. Details: [trainer-slides.md](trainer-slides.md).
