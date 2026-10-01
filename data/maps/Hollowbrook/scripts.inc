@ Hollowbrook (town exterior). Signs and the locked Goldsworth door for now.
@ NPCs, the grandfather timeline, Troglodyte's battle outside the lab and the fly flag come from
@ design/scripts/hollowbrook_scripts.inc in a later step (they need flags not yet claimed).

Hollowbrook_MapScripts::
	.byte 0

Hollowbrook_EventScript_TownSign::
	msgbox Hollowbrook_Text_TownSign, MSGBOX_SIGN
	end

Hollowbrook_EventScript_LabSign::
	msgbox Hollowbrook_Text_LabSign, MSGBOX_SIGN
	end

Hollowbrook_EventScript_GoldsworthSign::
	msgbox Hollowbrook_Text_GoldsworthSign, MSGBOX_SIGN
	end

Hollowbrook_EventScript_PlayerHouseSign::
	msgbox Hollowbrook_Text_PlayerHouseSign, MSGBOX_SIGN
	end

@ Locked until the League is beaten (the open-door warp comes with Hollowbrook_GoldsworthHouse).
@ The note is GrandpaBefore (signed 'GG').
Hollowbrook_EventScript_GoldsworthDoor::
	msgbox Hollowbrook_Text_GrandpaBefore, MSGBOX_SIGN
	end

Hollowbrook_Text_TownSign::
	.string "HOLLOWBROOK\n"
	.string "‘A quiet place. Mind the ZIGZAGOON.’$"

Hollowbrook_Text_LabSign::
	.string "FENNICK'S POKéMON LAB\n"
	.string "Knock. Then knock again.$"

Hollowbrook_Text_GoldsworthSign::
	.string "GOLDSWORTH HOUSE\n"
	.string "Please wipe your feet.$"

Hollowbrook_Text_PlayerHouseSign::
	.string "{PLAYER}'s house$"

Hollowbrook_Text_GrandpaBefore::
	.string "Nobody answers the door.\n"
	.string "A note is pinned to it.\p"
	.string "‘Out. Back when I'm back.\n"
	.string "Do feed the SKITTY. - GG’$"
