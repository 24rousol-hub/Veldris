Crestfall_Mart_MapScripts::
	.byte 0

Crestfall_Mart_EventScript_Clerk::
	lock
	faceplayer
	message Crestfall_Mart_Text_Clerk
	waitmessage
	pokemart Crestfall_Mart_Pokemart
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end

	.align 2
Crestfall_Mart_Pokemart:
	.2byte ITEM_POKE_BALL
	.2byte ITEM_POTION
	.2byte ITEM_ANTIDOTE
	.2byte ITEM_PARALYZE_HEAL
	.2byte ITEM_AWAKENING
	pokemartlistend

Crestfall_Mart_EventScript_Shopkeeper::
	lock
	faceplayer
	goto_if_set FLAG_BADGE01_GET, Crestfall_Mart_EventScript_ShopkeeperAfter
	msgbox Crestfall_Mart_Text_ShopkeeperBefore, MSGBOX_DEFAULT
	release
	end

Crestfall_Mart_EventScript_ShopkeeperAfter::
	msgbox Crestfall_Mart_Text_ShopkeeperAfter, MSGBOX_DEFAULT
	release
	end

Crestfall_Mart_Text_Clerk:
	.string "Welcome! Hay is not for sale.\n"
	.string "Everything else is.$"

Crestfall_Mart_Text_ShopkeeperBefore:
	.string "I stock POTIONS, POKé BALLS,\n"
	.string "and a few things for hay fever.\p"
	.string "I'd advise a few POTIONS.\n"
	.string "GRETA's SKITTY hits harder\l"
	.string "than it purrs.$"

Crestfall_Mart_Text_ShopkeeperAfter:
	.string "A STANDARD BADGE! Fine work.\n"
	.string "I'll say what I tell everyone:\p"
	.string "The next town is further than\n"
	.string "it looks. Bring more POTIONS.$"
