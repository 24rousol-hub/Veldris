#!/bin/sh
# apply_skip.sh <repo_root> <level> [keep_maps_comma_list]   - "Option B / SKIP", non-destructive (never runs `restore`).
#   level 1  patch tools/mapjson (NULL slots), tag every Hoenn-only map REGION_HOENN_SKIPPED, tag the layouts only those maps use
#            (the template layouts below stay live).  No C and no assembler edits.            ~ -0.75 MiB
#   level 2  + do not assemble the Hoenn map scripts C does not need (results/keep_scripts.txt: 40 stay)  ~ -1.19 MiB
#   level 3  + drop the Hoenn rows of gWildMonHeaders (the Pokedex Area page reads every row's map header) ~ -1.21 MiB
# Maps in keep_maps_comma_list are never tagged (use it for the Battle Tower if Aldermere will reuse it:
#   BattleFrontier_BattleTowerLobby,BattleFrontier_BattleTowerElevator,BattleFrontier_BattleTowerCorridor,BattleFrontier_BattleTowerBattleRoom,
#   BattleFrontier_BattleTowerMultiBattleRoom,BattleFrontier_BattleTowerMultiCorridor,BattleFrontier_BattleTowerMultiPartnerRoom).
# Tileset pruning (prune_tilesets.py) is NOT part of any level: it deletes the vanilla tilesets the author draws from.
# In the real repo (/home/user/Veldris) run only after the author has approved, with PURGE_ALLOW_REAL_REPO=1, and tell
# the author to close Porymap first (it rewrites layouts.json and map.json).  Then: make -j4, python3 skip_lint.py <repo> ...
set -e
R="$1"; LV="${2:-1}"; KEEP="${3:-}"
HERE="$(cd "$(dirname "$0")" && pwd)"
TEMPLATES="LAYOUT_POKEMON_CENTER_1F,LAYOUT_POKEMON_CENTER_2F,LAYOUT_MART,LAYOUT_HOUSE1,LAYOUT_HOUSE2,LAYOUT_HARBOR"
P="python3 $HERE/purge_experiment.py $R"
$P patch-mapjson
$P tag-maps --scope all --keep "$KEEP"
$P tag-layouts --keep "$KEEP" --keep-layouts "$TEMPLATES"
if [ "$LV" -ge 2 ]; then
  KS="$HERE/results/keep_scripts.txt"
  # a kept (untagged) map keeps its script too
  if [ -n "$KEEP" ]; then (cat "$KS"; echo "$KEEP" | tr ',' '\n') | sort -u > "$HERE/results/keep_scripts_effective.txt"; KS="$HERE/results/keep_scripts_effective.txt"; fi
  $P skip-scripts --keep-scripts "$KS"
fi
if [ "$LV" -ge 3 ]; then $P prune-wild --keep "$KEEP"; fi
echo "applied level $LV; now build, run skip_lint.py, run the emulator tests"
