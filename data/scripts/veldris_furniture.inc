@ Talking furniture (hack-owned script file). One script per furniture metatile behaviour; the lookup is VeldrisGetFurnitureScript
@ in src/veldris_furniture.c, called from GetInteractedMetatileScript. See design/furniture-lines.md. PROPOSED text, not canon.
@ Claims no flag or var. A bg_event sign on the same tile beats these (GetInteractionScript tries bg events first).

Veldris_EventScript_Furniture_Cabinet::
	msgbox Veldris_Text_Furniture_Cabinet, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_Kitchen::
	msgbox Veldris_Text_Furniture_Kitchen, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_Dresser::
	msgbox Veldris_Text_Furniture_Dresser, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_Snacks::
	msgbox Veldris_Text_Furniture_Snacks, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_Food::
	msgbox Veldris_Text_Furniture_Food, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_Painting::
	msgbox Veldris_Text_Furniture_Painting, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_Computer::
	msgbox Veldris_Text_Furniture_Computer, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_Telephone::
	msgbox Veldris_Text_Furniture_Telephone, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_AdvertisingPoster::
	msgbox Veldris_Text_Furniture_AdvertisingPoster, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_VideoGame::
	msgbox Veldris_Text_Furniture_VideoGame, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_ImpressiveMachine::
	msgbox Veldris_Text_Furniture_ImpressiveMachine, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_Blueprints::
	msgbox Veldris_Text_Furniture_Blueprints, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_PowerPlantMachine::
	msgbox Veldris_Text_Furniture_PowerPlantMachine, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_TastyFood::
	msgbox Veldris_Text_Furniture_TastyFood, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_Cup::
	msgbox Veldris_Text_Furniture_Cup, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_BlinkingLights::
	msgbox Veldris_Text_Furniture_BlinkingLights, MSGBOX_SIGN
	end

Veldris_EventScript_Furniture_NeatlyLinedUpTools::
	msgbox Veldris_Text_Furniture_NeatlyLinedUpTools, MSGBOX_SIGN
	end

Veldris_Text_Furniture_Cabinet:
	.string "The plates all match. Somebody\n"
	.string "here does not trust surprises.$"

Veldris_Text_Furniture_Kitchen:
	.string "Something is simmering. It smells\n"
	.string "of patience and one onion.$"

Veldris_Text_Furniture_Dresser:
	.string "Folded clothes. One sleeve has been\n"
	.string "mended so well it looks proud.$"

Veldris_Text_Furniture_Snacks:
	.string "A bowl of snacks. They have been\n"
	.string "counted. You can tell.$"

Veldris_Text_Furniture_Food:
	.string "A pot, a loaf and a lot of hope.\n"
	.string "It smells better than it looks.$"

Veldris_Text_Furniture_Painting:
	.string "A painting of a POKéMON. The artist\n"
	.string "clearly loved it. Or was paid to.$"

Veldris_Text_Furniture_Computer:
	.string "A computer. The screen says it is\n"
	.string "thinking. It has said so for hours.$"

Veldris_Text_Furniture_Telephone:
	.string "A telephone. It rings so rarely\n"
	.string "that it sounds like an accident.$"

Veldris_Text_Furniture_AdvertisingPoster:
	.string "A poster for a tonic that cures\n"
	.string "every ailment. Read the small print.$"

Veldris_Text_Furniture_VideoGame:
	.string "A game console. Someone has been\n"
	.string "losing on it with great dignity.$"

Veldris_Text_Furniture_ImpressiveMachine:
	.string "A machine, humming with total\n"
	.string "confidence. You do not touch it.$"

Veldris_Text_Furniture_Blueprints:
	.string "Plans for something very large.\n"
	.string "The margins are full of tea rings.$"

Veldris_Text_Furniture_PowerPlantMachine:
	.string "A big machine. The sign says DO NOT\n"
	.string "TOUCH. Under it: ‘Too late.’$"

Veldris_Text_Furniture_TastyFood:
	.string "Something smells wonderful. Your\n"
	.string "stomach files a formal complaint.$"

Veldris_Text_Furniture_Cup:
	.string "A chipped cup. It has seen things\n"
	.string "and is still in daily use.$"

Veldris_Text_Furniture_BlinkingLights:
	.string "Little lights blink on and off.\n"
	.string "You feel very slightly watched.$"

Veldris_Text_Furniture_NeatlyLinedUpTools:
	.string "Tools in a neat row, one per hook.\n"
	.string "A missing one would be noticed.$"

