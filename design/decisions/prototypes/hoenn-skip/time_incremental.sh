#!/bin/bash
# time_incremental.sh <clone> <label> : seconds for (a) re-assembling event_scripts.o and (b) a full 'make' after touching one map script.
CL="$1"; L="$2"; cd "$CL"
for i in 1 2 3; do
  touch data/event_scripts.s; s=$(date +%s.%N); make build/emerald/data/event_scripts.o >/dev/null 2>&1; e=$(date +%s.%N)
  printf "%s event_scripts.o %.2f s\n" "$L" "$(echo "$e - $s" | bc)"
done
for i in 1 2 3; do
  touch data/maps/Hollowbrook/scripts.inc; s=$(date +%s.%N); make -j4 >/dev/null 2>&1; e=$(date +%s.%N)
  printf "%s make after editing one map script %.2f s\n" "$L" "$(echo "$e - $s" | bc)"
done
