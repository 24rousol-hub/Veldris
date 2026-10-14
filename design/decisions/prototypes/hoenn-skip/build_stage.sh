#!/bin/sh
# build_stage.sh <clone> <label> [make flags...]  - build in a clone, keep going on errors, log, time, size.
# Writes <label>.log, <label>.time, <label>.size (arm-none-eabi-size -A) next to this script's results dir.
CL="$1"; L="$2"; shift; shift
OUT="$(cd "$(dirname "$0")" && pwd)/results"
mkdir -p "$OUT"
case "$(cd "$CL" && pwd)" in /home/user/Veldris) echo "refusing: real repo"; exit 1;; esac
cd "$CL"
s=$(date +%s)
make -k -j4 "$@" > "$OUT/$L.log" 2>&1
rc=$?
e=$(date +%s)
echo "exit=$rc seconds=$((e-s)) load=$(cut -d' ' -f1-3 /proc/loadavg)" > "$OUT/$L.time"
[ -f pokeemerald.elf ] && arm-none-eabi-size -A pokeemerald.elf > "$OUT/$L.size"
if [ $rc -eq 0 ] && [ -f pokeemerald.gba ]; then
  python3 - "$CL/pokeemerald.gba" >> "$OUT/$L.time" <<'PY'
import sys
d=open(sys.argv[1],'rb').read(); e=len(d)
while e and d[e-1]==0xFF: e-=1
print('rom_used_bytes',e)
PY
fi
