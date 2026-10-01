Veldris_Lab_MapScripts::
	.byte 0

Veldris_Lab_EventScript_StarterBall1::
	msgbox Veldris_Lab_Text_StarterBallPlaceholder, MSGBOX_NPC
	end

Veldris_Lab_EventScript_StarterBall2::
	msgbox Veldris_Lab_Text_StarterBallPlaceholder, MSGBOX_NPC
	end

Veldris_Lab_EventScript_StarterBall3::
	msgbox Veldris_Lab_Text_StarterBallPlaceholder, MSGBOX_NPC
	end

Veldris_Lab_Text_StarterBallPlaceholder:
	.string "A starter Poke Ball sits here.$"

Veldris_Lab_EventScript_ProfPC::
	msgbox Veldris_Lab_Text_ProfPC, MSGBOX_SIGN
	end

Veldris_Lab_EventScript_Notes::
	msgbox Veldris_Lab_Text_Notes, MSGBOX_SIGN
	end

Veldris_Lab_EventScript_Machine::
	msgbox Veldris_Lab_Text_Machine, MSGBOX_SIGN
	end

Veldris_Lab_Text_ProfPC:
	.string "It's the PROFESSOR's PC.\n"
	.string "Research data is scrolling by.$"

Veldris_Lab_Text_Notes:
	.string "Research notes on POKéMON habitats\n"
	.string "around the VELDRIS region.$"

Veldris_Lab_Text_Machine:
	.string "It's a machine for studying\n"
	.string "POKéMON. It's humming softly.$"
