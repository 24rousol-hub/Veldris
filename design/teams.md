# Trainer teams

Status: **PROPOSED** unless marked. Levels and the number of Pokémon per trainer are the author's (2026-09-29). Species and moves are my proposal. Blocks use the `src/data/trainers.party` format so they can be pasted in later. **Built 2026-10-01 for DALE, WREN, GRETA and Troglodyte fights 1 and 2** (see [trainer-roster.md](trainer-roster.md)); DALE, WREN and Troglodyte use placeholder pictures and classes.

**No IVs or EVs on any trainer (author, 2026-09-29): they belong to the player only.** **CORRECTION (2026-10-01, checked by building):** leaving out the `IVs:` line does NOT give zero IVs. The build tool (`tools/trainerproc`) then writes `TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31)`, so every Pokémon would be maxed. To honour the rule, **every Pokémon needs `IVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe`** (the 13 leader, Elite Four and Champion blocks in `src/data/trainers.party` have it). Leaving out `EVs:` is correct: no EV field is written, so EVs are 0. The blocks drafted below were written before this correction, so add the IVs line when pasting them. A trainer with 0 IVs is a little weaker than vanilla's, so tune levels or moves if it feels soft.

**AI line (from the author's 'short ladder' answer of 2026-10-12; the rung contents are my applied reading and stay changeable).** The `AI:` line of every block comes from the short ladder in [ai-ladder.md](ai-ladder.md): Dim `Check Bad Move`, Basic `Basic Trainer`, Sharp `Basic Trainer / Hp Aware / Try To 2hko`, plus `/ Ace Pokemon` for gym leaders 3 to 9, the Elite Four and Cynthia (never for Troglodyte). In this file Greta, DALE and WREN stay `Basic Trainer`; Troglodyte's fights 1 and 2 are `Check Bad Move` (Dim). Later Troglodyte fights follow the table in [ai-ladder.md](ai-ladder.md). Never `Smart Trainer`, `Prediction` or `Omniscient`.

Moves are checked against the learnsets this ROM actually uses (`P_LVL_UP_LEARNSETS` is `GEN_LATEST`, so `gen_9.h`). Each move is learned by that species at or below its level.

## Crestfall gym (gym 1, Normal type, STANDARD BADGE)

| Trainer | Pokémon | Level | Author fixed |
|---|---|---|---|
| Gym trainer 1 | 1 | 9 | count and level |
| Gym trainer 2 | 1 | 10 | count and level |
| Greta | 2 | 10 and 12 | count and levels |

Greenery in the gym is aesthetic only. Every Pokémon here is Normal type.

### Gym trainer 1: ZIGZAGOON, level 9
```
=== TRAINER_CRESTFALL_GYM_1 ===
Name: DALE
Class: (TBD: must already exist)
Pic: (TBD: must already exist)
Gender: (TBD)
Music: (TBD)
Double Battle: No
AI: Basic Trainer

Zigzagoon
Level: 9
- Tackle
- Sand Attack
- Tail Whip
- Covet
```
The obvious first opponent: a quick Normal type that blinds you with Sand Attack.

### Gym trainer 2: SLAKOTH, level 10
```
=== TRAINER_CRESTFALL_GYM_2 ===
Name: WREN
Class: (TBD: must already exist)
Pic: (TBD: must already exist)
Gender: (TBD)
Music: (TBD)
Double Battle: No
AI: Basic Trainer

Slakoth
Level: 10
- Scratch
- Yawn
- Encore
- Slack Off
```
It fits his draft lines ('I've been in here for three years. It's very relaxing.'). It is sleepy rather than dangerous, so Yawn is the trap.

### Greta: SKITTY level 10, MILTANK level 12
```
=== TRAINER_CRESTFALL_GRETA ===
Name: GRETA
Class: Leader
Pic: (her ORAS lass picture, see characters.md: needs the engine edits)
Gender: Female
Music: Female
Items: Potion / Potion
Double Battle: No
AI: Basic Trainer

Skitty
Level: 10
- Fake Out
- Tackle
- Sing
- Attract

Miltank @ Oran Berry
Level: 12
- Tackle
- Growl
- Rollout
- Defense Curl
```
- **Skitty opens with Fake Out** (a flinch), then Sing and Attract make it annoying rather than deadly.
- **Miltank is the ace.** Rollout plus Defense Curl is the classic early-game Miltank problem, and she learns nothing better by level 12. With no IVs she is a little weaker than a vanilla leader's Pokémon, so this may land about right for a player at level 10 to 12. Tell me if you want it softer (drop Defense Curl) or harder.
- The Oran Berry copies the vanilla first gym leader, Roxanne. Greta's two Pokémon are a level 10 and a level 12, as you asked.

## Troglodyte

His Pokémon is one of the three starters on show, at random. **One trainer entry per fight** (the pool prune, see [story-outline.md](story-outline.md)). **The three are Chikorita (ball 1, Grass, tag `Tag6`), Cyndaquil (ball 2, Fire, `Tag7`) and Totodile (ball 3, Water, `Tag8`), chosen by the author on 2026-10-12 (set A, Johto plus Togepi).** The fourth, Togepi, is the player's alone: Troglodyte never has it. Emerald's Treecko, Torchic and Mudkip were stand-ins until then. The four lines, their evolution levels and a balance note are in 'The four starter lines' at the end of this file.

### Fight 1: right outside the lab in Hollowbrook (author: one Pokémon, the usual rival opener)
The level is my proposal: 5, the same as your starter. No IVs or EVs, as for every trainer.
```
=== TRAINER_TROGLODYTE_HOLLOWBROOK ===
Name: (TBD: see note below)
Class: (TBD: must already exist)
Pic: (TBD: must already exist)
Gender: Male
Music: (TBD)
Double Battle: No
AI: Check Bad Move
Party Size: 1
Pool Prune: Rival Starter

Chikorita
Level: 5
Tags: Tag6
- Tackle
- Growl

Cyndaquil
Level: 5
Tags: Tag7
- Tackle
- Leer

Totodile
Level: 5
Tags: Tag8
- Scratch
- Leer
```
All three versions are tagged and Party Size is 1, so exactly one survives the prune. The moves are each starter's level-up moves at level 5 (checked against `gen_9.h`, the learnsets this ROM uses): Chikorita learns Razor Leaf only at 6, Cyndaquil gets Smokescreen at 6 and Ember at 10, Totodile gets Water Gun at 6, so each has two moves now. **The built block** in `src/data/trainers.party` is the source of truth: it also carries `Ball: Luxury`, the zero IVs and `Lead` (`Tags: Lead / Tag6` and so on), which this draft leaves out. The 2026-10-12 swap replaced Treecko (Pound, Leer, Leafage), Torchic (Scratch, Growl, Ember) and Mudkip (Tackle, Growl, Water Gun), the stand-ins used in every earlier test.

**Gag: a level 1 LILLIPUP pet (APPROVED by the author, 2026-09-30).** Add this block, change `Party Size` to 2, and leave it untagged so it is always picked. LILLIPUP is in this build (Gen 5 Pokémon are on). It faints to anything, which is the joke. Its dialogue is in `design/dialogue/hollowbrook.inc` (`TrogPetIntro`, `TrogPetAfter`).
```
Lillipup
Nickname: SIR BISCUIT
Level: 1
- Tackle
- Leer
```
Kept (author, 2026-09-30): it shows a sheltered rich boy who brought his pampered pet to a fight.

### Fight 2: Crestfall (Scheme 1), PROPOSED
His starter again (random, same pool prune) at level 8, plus SIR BISCUIT, now level 7 and no longer a joke. Party Size is 2: one fixed Pokémon plus one survivor of the prune. No IVs or EVs. Dialogue: `design/dialogue/crestfall.inc` (`TrogBattleIntro` and onward). Moves are each species' level-up moves at level 8 (checked against `gen_9.h`).
```
=== TRAINER_TROGLODYTE_CRESTFALL ===
Name: (TBD: same as fight 1)
Class: (TBD: must already exist)
Pic: (TBD: must already exist)
Gender: Male
Music: (TBD)
Double Battle: No
AI: Check Bad Move
Party Size: 2
Pool Prune: Rival Starter

Lillipup
Nickname: SIR BISCUIT
Level: 7
- Tackle
- Leer

Chikorita
Level: 8
Tags: Tag6
- Tackle
- Growl
- Razor Leaf

Cyndaquil
Level: 8
Tags: Tag7
- Tackle
- Leer
- Smokescreen

Totodile
Level: 8
Tags: Tag8
- Scratch
- Leer
- Water Gun
```
At level 8 each Johto starter knows only three level-up moves (the old Treecko and Torchic versions had four, with Quick Attack; Cyndaquil gets Quick Attack only at 13). Nothing is padded with a move the species cannot know at that level. The built block in `src/data/trainers.party` is the source of truth.
It costs one more trainer id (two for Troglodyte in total so far, five brand-new ids with Greta and the gym trainers, or none if he reuses a vanilla entry).

## The four starter lines (author, 2026-10-12: set A, Johto plus Togepi)

Evolution data read from `src/data/pokemon/species_info/gen_2_families.h` (the Togepi line sits there too) on 2026-10-12. `P_FRIENDSHIP_EVO_THRESHOLD` is `GEN_LATEST`, so the friendship needed is 160.

| Ball | Species | Type | Stage 2 | Stage 3 | Whose |
|---|---|---|---|---|---|
| 1 | Chikorita | Grass | Bayleef at level 16 | Meganium at level 32 | on show; Troglodyte's pick `Tag6` |
| 2 | Cyndaquil | Fire | Quilava at level 14 | Typhlosion at level 36 | on show; Troglodyte's pick `Tag7` |
| 3 | Totodile | Water | Croconaw at level 18 | Feraligatr at level 30 | on show; Troglodyte's pick `Tag8` |
| 4 | Togepi | Fairy | Togetic on any level-up while friendship is 160 or more (Fairy and Flying) | Togekiss when Togetic is given a Shiny Stone (Fairy and Flying) | revealed by Fennick; the player's only. A normal level 5 Pokémon, not an egg |

Troglodyte's later fights write the stage that fits the level ([troglodyte-arc.md](troglodyte-arc.md)). The Togepi line has no Troglodyte version.

**Balance note (honest).** Matchups below use this ROM's own type chart (`src/data/types_info.h`) against the gym's type only, with the gym order Normal, Bug, Ghost, Steel, Ice, Flying, Poison, Fairy, Water ([gyms.md](gyms.md)). The gym teams mix other types, so this is a first guide, not a promise.

| Line | Strong into | Weak into | Plain |
|---|---|---|---|
| Chikorita (Grass) | gym 9 (Water) | gyms 2, 5, 6 and 7 (Bug, Ice, Flying and Poison all hit Grass for double); gym 4 (Steel) resists its Grass moves | gyms 1, 3, 8 |
| Cyndaquil (Fire) | gyms 2, 4 and 5 (Bug, Steel, Ice: Fire hits them for double and Fire resists their moves), and it resists Fairy moves at gym 8 | gym 9 (Water) | gyms 1, 3, 6, 7 |
| Totodile (Water) | gyms 4 and 5 on defence (it resists Steel and Ice) | none by type; its Water moves are resisted at gym 9 | gyms 1, 2, 3, 6, 7, 8 |
| Togepi (Fairy) | gym 2 on defence (it resists Bug) | gyms 4 and 7 (Steel and Poison hit Fairy for double and resist Fairy moves) | the rest |
| Togetic and Togekiss (Fairy and Flying) | gym 2 (Flying hits Bug for double, and Bug does a quarter) | gyms 4, 5 and 7 (Steel, Ice and Poison all hit for double) | the rest |

- **The Grass starter has the roughest road**: four of the first seven gyms are bad for it (gyms 2, 5, 6 and 7), and Steel resists its moves at gym 4. Its payoff is gym 9.
- **The Fire starter has the easiest early game** (gyms 2, 4 and 5), then meets the Water gym last.
- **The Water starter is the safe middle**: no gym from 1 to 8 punishes it by type. It evolves into Feraligatr at 30, earlier than the other two reach their last stage (32 and 36).
- **Togepi is the odd one out and the weakest fighter.** Its base Attack is 20, it knows Growl, Pound and Sweet Kiss at level 5, its only attacking moves before level 32 are Pound and (from level 16) Ancient Power (Double-Edge comes at 32, Last Resort at 48), and Togetic needs friendship (160) on a level-up rather than a set level. No gym is weak to Fairy, so by type it never hits a gym for double. It is a gift more than a fighter, and a Togepi player should expect to catch a second attacker early. Togepi cannot learn Cut (it is not in its teachable list; the other three starters all can), so a Togepi-only party cannot use the Cut field move until it catches a Pokémon that can. That costs little: Route 1 is full of Cut learners and nothing in the built maps is locked behind Cut ('Cut and the early catches' in [field-moves.md](field-moves.md)).
- This corrects an earlier line in the decision brief, which called Togepi strong into gym 7: Fairy is **weak** into Poison.
