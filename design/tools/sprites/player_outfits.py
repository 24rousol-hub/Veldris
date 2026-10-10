"""Overworld sprite sets for the player's unlockable outfits (design/player-customization.md).

Outfits: Ruby/Sapphire (vanilla RS walking + running) and Diamond/Pearl (Lucas/Dawn from the DP set, copied into
graphics/object_events/pics/people/dp_player/ by import_dp.py). Every state an outfit has art for gets a new
OBJ_EVENT_GFX_VELDRIS_<OUTFIT>_<GENDER>_<STATE>, built by copying the matching Emerald Brendan/May graphics info and
pic table and swapping the picture and palette. States without art fall back to Emerald in src/veldris_look.c.

Re-runnable: the generated blocks sit between // VELDRIS-LOOK markers. Run from the repo root:
  python3 design/tools/sprites/player_outfits.py
"""
import re
from pathlib import Path
from PIL import Image

V = Path(__file__).resolve().parents[3]
TAG_BASE = 0x11C0
STATES = {  # Emerald suffix -> sheet file (DP) ; Normal is walking + running
    "MachBike": "mach_bike", "Surfing": "surfing", "FieldMove": "field_move", "Fishing": "fishing", "Watering": "watering",
}
OUTFITS = [
    # (outfit, gender, Emerald name, art dir, palette (symbol, tag or None for new from art), states with art)
    ("RS", "MALE", "Brendan", "ruby_sapphire_brendan", ("gObjectEventPal_RubySapphireBrendan", "OBJ_EVENT_PAL_TAG_RS_BRENDAN"), []),
    ("RS", "FEMALE", "May", "ruby_sapphire_may", ("gObjectEventPal_RubySapphireMay", "OBJ_EVENT_PAL_TAG_RS_MAY"), []),
    ("DP", "MALE", "Brendan", "dp_player/lucas", None, ["MachBike", "Surfing", "Fishing"]),
    ("DP", "FEMALE", "May", "dp_player/dawn", None, ["MachBike", "Surfing", "FieldMove", "Fishing", "Watering"]),
]

def replace_block(path, name, anchor_re, lines, before=True):
    p = V / path; s = p.read_text()
    begin, end = f"// VELDRIS-LOOK {name} BEGIN (design/tools/sprites/player_outfits.py)\n", f"// VELDRIS-LOOK {name} END\n"
    body = begin + "".join(lines) + end
    m = re.search(re.escape(begin) + r".*?" + re.escape(end), s, re.S)
    if m: s = s[:m.start()] + body + s[m.end():]
    else:
        a = re.search(anchor_re, s, re.M); assert a, (path, anchor_re)
        i = a.start() if before else a.end(); s = s[:i] + body + s[i:]
    p.write_text(s)

info_src = (V / "src/data/object_events/object_event_graphics_info.h").read_text()
pic_src = (V / "src/data/object_events/object_event_pic_tables.h").read_text()
def block(src, pattern):
    m = re.search(pattern + r".*?\n\};\n", src, re.S); assert m, pattern; return m.group(0)

data, enums, tags, externs, pointers, palettes, rows = [], [], [], [], [], [], []
ntag = 0
for outfit, gender, em, art, pal, states in OUTFITS:
    G = "M" if gender == "MALE" else "F"
    base = f"Veldris{outfit}{G}"
    if pal is None:
        palsym, tag = f"gObjectEventPal_{base}", f"OBJ_EVENT_PAL_TAG_VELDRIS_{outfit}_{G}"
        data.append(f'const u16 {palsym}[] = INCGFX_U16("graphics/object_events/pics/people/{art}/walking.png", ".gbapal");\n')
        tags.append(f"#define {tag:<40} 0x{TAG_BASE + ntag:04X}\n"); ntag += 1
        palettes.append(f"    {{{palsym}, {tag}}},\n")
    else:
        palsym, tag = pal
    # Normal = walking (9 frames) + running (9 frames), like Emerald's walking+running sheet
    for sheet in ("walking", "running"):
        data.append(f'const u32 gObjectEventPic_{base}{sheet.capitalize()}[] = INCGFX_U32("graphics/object_events/pics/people/{art}/{sheet}.png", ".4bpp", "-mwidth 2 -mheight 4");\n')
    frames = [f"    overworld_frame(gObjectEventPic_{base}Walking, 2, 4, {i}),\n" for i in range(9)]
    frames += [f"    overworld_frame(gObjectEventPic_{base}Running, 2, 4, {i}),\n" for i in range(9)]
    data.append(f"static const struct SpriteFrameImage sPicTable_{base}Normal[] = {{\n" + "".join(frames) + "};\n")
    info = block(info_src, rf"const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_{em}Normal = ")
    info = info.replace(f"gObjectEventGraphicsInfo_{em}Normal", f"gObjectEventGraphicsInfo_{base}Normal")
    info = re.sub(r"\.paletteTag = \w+", f".paletteTag = {tag}", info).replace(f"sPicTable_{em}Normal", f"sPicTable_{base}Normal")
    data.append(info)
    made = [("Normal", "NORMAL")]
    for st in states:
        sheet = STATES[st]
        Image.open(V / f"graphics/object_events/pics/people/{art}/{sheet}.png")   # must exist
        w, h = (4, 4)
        data.append(f'const u32 gObjectEventPic_{base}{st}[] = INCGFX_U32("graphics/object_events/pics/people/{art}/{sheet}.png", ".4bpp", "-mwidth {w} -mheight {h}");\n')
        pt = block(pic_src, rf"static const struct SpriteFrameImage sPicTable_{em}{st}\[\] = ")
        data.append(pt.replace(f"sPicTable_{em}{st}", f"sPicTable_{base}{st}").replace(f"gObjectEventPic_{em}{st}", f"gObjectEventPic_{base}{st}"))
        info = block(info_src, rf"const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_{em}{st} = ")
        info = info.replace(f"gObjectEventGraphicsInfo_{em}{st}", f"gObjectEventGraphicsInfo_{base}{st}")
        info = re.sub(r"\.paletteTag = \w+", f".paletteTag = {tag}", info).replace(f"sPicTable_{em}{st}", f"sPicTable_{base}{st}")
        data.append(info)
        made.append((st, re.sub(r"(?<!^)([A-Z])", r"_\1", st).upper()))
    for st, ST in made:
        gid = f"OBJ_EVENT_GFX_VELDRIS_{outfit}_{G}_{ST}"
        enums.append(f"    {gid},\n")
        externs.append(f"extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_{base}{st};\n")
        pointers.append(f"    [{gid}] = &gObjectEventGraphicsInfo_{base}{st},\n")
        rows.append((outfit, gender, st, gid))

(V / "src/data/object_events/veldris_outfit_object_events.h").write_text(
    "// Player outfit sprite sets (design/player-customization.md). Generated by design/tools/sprites/player_outfits.py.\n\n" + "\n".join(data))
replace_block("include/constants/event_objects.h", "ENUM", r"^    NUM_OBJ_EVENT_GFX,", enums)
replace_block("include/constants/event_objects.h", "TAGS", r"^#define OBJ_EVENT_PAL_TAG_NONE", tags)
replace_block("src/data/object_events/object_event_graphics_info_pointers.h", "EXTERNS",
              r"^const struct ObjectEventGraphicsInfo \*const gObjectEventGraphicsInfoPointers", externs)
replace_block("src/data/object_events/object_event_graphics_info_pointers.h", "POINTERS", r"^};", pointers)
replace_block("src/event_object_movement.c", "INCLUDE", r'^#include "data/object_events/object_event_graphics_info_followers.h"\n',
              ['#include "data/object_events/veldris_outfit_object_events.h"\n'], before=False)
replace_block("src/event_object_movement.c", "PALETTES", r"^static const struct SpritePalette sObjectEventSpritePalettes\[\] = \{\n", palettes, before=False)

# table for src/veldris_look.c: [outfit][state][gender]
C_STATE = {"Normal": "PLAYER_AVATAR_STATE_NORMAL", "MachBike": "PLAYER_AVATAR_STATE_MACH_BIKE", "Surfing": "PLAYER_AVATAR_STATE_SURFING",
           "FieldMove": "PLAYER_AVATAR_STATE_FIELD_MOVE", "Fishing": "PLAYER_AVATAR_STATE_FISHING", "Watering": "PLAYER_AVATAR_STATE_WATERING"}
t = ["// Generated by design/tools/sprites/player_outfits.py: outfit sprite per avatar state (0 = use Emerald's).\n",
     "static const u16 sOutfitGfx[OUTFIT_COUNT][PLAYER_AVATAR_STATE_COUNT][GENDER_COUNT] = {\n"]
for outfit in ("RS", "DP"):
    t.append(f"    [OUTFIT_{outfit}] = {{\n")
    for st in C_STATE:
        m = [g for o, gg, s, g in rows if o == outfit and s == st and gg == "MALE"]
        f = [g for o, gg, s, g in rows if o == outfit and s == st and gg == "FEMALE"]
        if m or f:
            t.append(f"        [{C_STATE[st]}] = {{[MALE] = {m[0] if m else 0}, [FEMALE] = {f[0] if f else 0}}},\n")
    t.append("    },\n")
t.append("};\n\nstatic const u16 sOutfitFemaleGfx[] = {\n" + "".join(f"    {g},\n" for o, gg, s, g in rows if gg == "FEMALE") + "};\n")
(V / "src/data/veldris_outfit_gfx.h").write_text("".join(t))
print(len(rows), "outfit graphics")
