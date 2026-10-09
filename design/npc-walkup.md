# NPC walk-up and talk (recipe, not built anywhere yet)

Status: DOCUMENTED 2026-10-08 (author: 'NPC walk and talk looks great in theory'). Checked by reading `src/trainer_see.c` and `src/script.c`; **not yet run in the emulator**, so test the first one built.

## What it does

An ordinary NPC sees the player step into their line of sight, shows the '!' icon, walks up to the player and then talks, with no battle. It is the trainer-approach machinery with a non-battle script.

## Recipe

1. In `map.json`, give the object event `"trainer_type": "TRAINER_TYPE_NORMAL"` and set `"trainer_sight_or_berry_tree_id"` to the sight range in tiles (1 or more; the NPC looks the way its `movement_type` faces, as a normal trainer does). Close Porymap first (rule 2 in [CLAUDE.md](../CLAUDE.md)).
2. The object's script starts with a guard, then the visible part:

```
Map_EventScript_Walker::
	goto_if_set FLAG_MAP_WALKER_DONE, Map_EventScript_WalkerDone
	lock
	faceplayer
	msgbox Map_Text_Walker, MSGBOX_DEFAULT
	setflag FLAG_MAP_WALKER_DONE
	release
	end

Map_EventScript_WalkerDone::
	end
```

## How it works (what the code does)

- When the player moves, `CheckTrainer` (`src/trainer_see.c`) runs each trainer-type NPC's script **ahead of time, without showing anything**, until it reaches the first command with a visible effect (`lock`, `faceplayer`, `msgbox`, `setflag` and anything else that touches the screen or the save). If that command is a `trainerbattle`, it is an ordinary trainer. If it is anything else, the NPC counts as a 'non-battle approach' (return value 0xFF).
- The NPC then shows '!', walks to the player (`DoTrainerApproach`), and runs **its own script from the first line** (`LoadTrainerObjectScript`).
- If the run-ahead reaches `end` with no visible effect, nothing happens. That is what the leading `goto_if_set ... Done` is for: after the scene the guard jumps to a label that is just `end`, so the NPC no longer approaches.

## Traps

- **The Done branch must contain nothing visible.** A `msgbox` there would make the NPC walk up again every time the player crosses their line of sight. So after the scene this NPC says nothing when talked to. If a talk-after line is wanted, hide this object (`setflag FLAG_HIDE_...`, `removeobject`) and show a second ordinary NPC at the same tile, or make the NPC leave.
- Any command that changes the save (`setflag`, `setvar`, `giveitem`) also stops the run-ahead, so put the guard **first**.
- The walk is blocked if something stands between the NPC and the player (same as a trainer).
- Use `lock`/`faceplayer`/`release`, as for a normal NPC; `lockall` is not needed.
- A cutscene where the NPC must come from outside the sight range, or must be triggered once on entry, is better done with a `coord_event` trigger (see CLAUDE.md, Engine rules).

## Good uses

Troglodyte's drive-by insults on routes, a Goldsworth footman handing over a 'gift', a villager who simply must tell the player something. For key story beats (Troglodyte's fights, Goldsworth schemes) the author approves the wording first (rule 10).
