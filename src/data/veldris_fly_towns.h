#ifndef GUARD_VELDRIS_FLY_TOWNS_H
#define GUARD_VELDRIS_FLY_TOWNS_H

// Hack-owned (not upstream). The one place to touch to add a Veldris fly town. See design/region-map.md.
//
// X(mapsec, visited_flag, map, heal_location)
// Add a row only after: the map exists, its heal location exists in src/data/heal_locations.json
// (with BOTH respawn_map and respawn_npc, written in that order), the visited flag is claimed in
// design/flags.md, and the town's OnTransition does `setflag <flag>`. The full checklist is in
// design/region-map.md. New section ids go at the very END of region_map_sections.json (they must
// stay after MAPSEC_TRAINER_HILL), so they stay clear of the Kanto block.
// Example row (do not enable until those exist):
//     X(MAPSEC_HOLLOWBROOK, FLAG_VISITED_HOLLOWBROOK, MAP_HOLLOWBROOK, HEAL_LOCATION_HOLLOWBROOK)
// Write the rows as continuation lines: every row ends with a backslash except the last one.
// The table is empty for now.
#define VELDRIS_FLY_TOWNS(X)

#define VELDRIS_HEAL_ROW(sec, visited, map, heal) \
    [sec] = {MAP_GROUP(map), MAP_NUM(map), heal},
#define VELDRIS_FLY_ROW(sec, visited, map, heal) \
    { .regionMapType = REGION_MAP_HOENN, .mapsec = sec, .flag = visited },
#define VELDRIS_TYPE_CASE(sec, visited, map, heal) \
    case sec: return FlagGet(visited) ? MAPSECTYPE_CITY_CANFLY : MAPSECTYPE_CITY_CANTFLY;

#define VELDRIS_HEAL_LOCATION_ROWS VELDRIS_FLY_TOWNS(VELDRIS_HEAL_ROW)
#define VELDRIS_FLY_LOCATION_ROWS  VELDRIS_FLY_TOWNS(VELDRIS_FLY_ROW)
#define VELDRIS_MAPSEC_TYPE_CASES  VELDRIS_FLY_TOWNS(VELDRIS_TYPE_CASE)

// Fails the build if the section ids grow into the met-location codes (43 new sections fit in total over the vanilla 209).
STATIC_ASSERT(MAPSEC_NONE < METLOC_SPECIAL_EGG, VeldrisTooManyMapSections);

#endif // GUARD_VELDRIS_FLY_TOWNS_H
