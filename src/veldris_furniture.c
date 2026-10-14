#include "global.h"
#include "veldris_furniture.h"
#include "constants/metatile_behaviors.h"

// Scripts and text: data/scripts/veldris_furniture.inc
extern const u8 Veldris_EventScript_Furniture_Cabinet[];
extern const u8 Veldris_EventScript_Furniture_Kitchen[];
extern const u8 Veldris_EventScript_Furniture_Dresser[];
extern const u8 Veldris_EventScript_Furniture_Snacks[];
extern const u8 Veldris_EventScript_Furniture_Food[];
extern const u8 Veldris_EventScript_Furniture_Painting[];
extern const u8 Veldris_EventScript_Furniture_Computer[];
extern const u8 Veldris_EventScript_Furniture_Telephone[];
extern const u8 Veldris_EventScript_Furniture_AdvertisingPoster[];
extern const u8 Veldris_EventScript_Furniture_VideoGame[];
extern const u8 Veldris_EventScript_Furniture_ImpressiveMachine[];
extern const u8 Veldris_EventScript_Furniture_Blueprints[];
extern const u8 Veldris_EventScript_Furniture_PowerPlantMachine[];
extern const u8 Veldris_EventScript_Furniture_TastyFood[];
extern const u8 Veldris_EventScript_Furniture_Cup[];
extern const u8 Veldris_EventScript_Furniture_BlinkingLights[];
extern const u8 Veldris_EventScript_Furniture_NeatlyLinedUpTools[];

struct VeldrisFurniture
{
    u8 behavior;
    const u8 *script;
};

// The pure-flavour FRLG behaviours. Left out on purpose: MB_BURGLARY (FRLG story), MB_TRAINER_TOWER_MONITOR,
// MB_CABLE_CLUB_WIRELESS_MONITOR, MB_BATTLE_RECORDS and the two MB_INDIGO_PLATEAU_SIGN values (FRLG features).
static const struct VeldrisFurniture sFurniture[] =
{
    { MB_CABINET,               Veldris_EventScript_Furniture_Cabinet },
    { MB_KITCHEN,               Veldris_EventScript_Furniture_Kitchen },
    { MB_DRESSER,               Veldris_EventScript_Furniture_Dresser },
    { MB_SNACKS,                Veldris_EventScript_Furniture_Snacks },
    { MB_FOOD,                  Veldris_EventScript_Furniture_Food },
    { MB_PAINTING,              Veldris_EventScript_Furniture_Painting },
    { MB_COMPUTER,              Veldris_EventScript_Furniture_Computer },
    { MB_TELEPHONE,             Veldris_EventScript_Furniture_Telephone },
    { MB_ADVERTISING_POSTER,    Veldris_EventScript_Furniture_AdvertisingPoster },
    { MB_VIDEO_GAME,            Veldris_EventScript_Furniture_VideoGame },
    { MB_IMPRESSIVE_MACHINE,    Veldris_EventScript_Furniture_ImpressiveMachine },
    { MB_BLUEPRINTS,            Veldris_EventScript_Furniture_Blueprints },
    { MB_POWER_PLANT_MACHINE,   Veldris_EventScript_Furniture_PowerPlantMachine },
    { MB_FOOD_SMELLS_TASTY,     Veldris_EventScript_Furniture_TastyFood },
    { MB_CUP,                   Veldris_EventScript_Furniture_Cup },
    { MB_BLINKING_LIGHTS,       Veldris_EventScript_Furniture_BlinkingLights },
    { MB_NEATLY_LINED_UP_TOOLS, Veldris_EventScript_Furniture_NeatlyLinedUpTools },
};

const u8 *VeldrisGetFurnitureScript(u8 metatileBehavior)
{
    u32 i;

    for (i = 0; i < ARRAY_COUNT(sFurniture); i++)
    {
        if (sFurniture[i].behavior == metatileBehavior)
            return sFurniture[i].script;
    }
    return NULL;
}
