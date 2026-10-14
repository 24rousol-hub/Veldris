@ Player customization (hack-owned script file). See design/player-customization.md.
@ PROPOSED text, not yet approved by the author.

@ Using the Costume Box from the bag or with SELECT.
Veldris_EventScript_CostumeBox::
	lockall
	callnative VeldrisLook_CanOpen
	goto_if_eq VAR_RESULT, FALSE, Veldris_Look_NotOnFoot
	callnative VeldrisLook_OpenMenu
	waitstate
	releaseall
	end

Veldris_Look_NotOnFoot::
	msgbox Veldris_Look_Text_NotOnFoot, MSGBOX_DEFAULT
	releaseall
	end

@ Mom gives the box once, then the picker opens straight away. Silent if it is already in the bag.
Veldris_EventScript_GiveCostumeBox::
	checkitem ITEM_COSTUME_BOX
	goto_if_eq VAR_RESULT, TRUE, Veldris_Look_GiveDone
	msgbox Veldris_Look_Text_MomBox, MSGBOX_DEFAULT
	giveitem ITEM_COSTUME_BOX
	msgbox Veldris_Look_Text_MomMirror, MSGBOX_DEFAULT
	closemessage
	callnative VeldrisLook_OpenMenu
	waitstate
	msgbox Veldris_Look_Text_MomAfter, MSGBOX_DEFAULT
Veldris_Look_GiveDone::
	return

Veldris_Look_Text_NotOnFoot:
	.string "You can only change clothes\n"
	.string "with both feet on the ground.$"

Veldris_Look_Text_MomBox:
	.string "Oh! And take this. It's your\n"
	.string "COSTUME BOX.\p"
	.string "A trainer should look the part.\n"
	.string "The shop said so, anyway.$"

Veldris_Look_Text_MomMirror:
	.string "Go on, have a look in the mirror.\n"
	.string "Pick whatever you like.$"

Veldris_Look_Text_MomAfter:
	.string "Very smart. You can change it\n"
	.string "any time from your BAG.$"
