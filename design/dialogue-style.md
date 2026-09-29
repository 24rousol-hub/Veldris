# Dialogue style guide

## Voice

- Deadpan and dry. The joke is in the situation, not in shouting.
- The player is silent. Their attitude shows through the choices offered.
- Troglodyte is pompous and clueless. Never cruel. Never swears.
- Locals are sincere and slightly odd.
- Keep speeches short. A grudge is funnier when it is brief.

Per-character voice notes are in [characters.md](characters.md).

## Hard technical rules

1. **No double quotes.** The charmap has no plain double quote, and even `\"` is a build error. Use single quotes for speech, and type the **curly** ones so the opening quote looks right: ‘Well, that went badly.’ The ASCII apostrophe `'` always shows the closing glyph, so it is fine inside words (who's) but wrong as an opening quote.
2. **Never use `{RIVAL}`.** It expands to MAY or BRENDAN, chosen by the player's gender (`src/string_util.c`). Write TROGLODYTE.
3. **Use `{PLAYER}`** for the player's name. `{STR_VAR_1}` to `{STR_VAR_3}` are the script buffers.
4. **Intro dialogue** is C-driven. Edit `data/text/birch_speech.inc`.
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

Rule of thumb: about 34 characters per line, 2 lines per box. **Unverified.** Measure in game before treating this as a limit, and correct this line once measured.

## Naming text labels

`<Map>_Text_<Speaker><Purpose>`, for example `Crestfall_Text_GretaGreeting`. Keep labels unique across the project.
