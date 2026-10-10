| step | ROM used (bytes) | saved vs HEAD | free of 32 MiB |
|---|---:|---:|---:|
| A  leave as is (HEAD e250a8e6) | 26,822,384 | 0 | 6.420 MiB |
| B0 tag the 461 Hoenn maps in pure-Hoenn groups (stock tool) | 26,734,328 | 88,056 | 6.504 MiB |
| B0+ B0 + skip the 383 layouts only skipped maps use (stock tool) | 26,390,900 | 431,484 | 6.832 MiB |
| B1 all 518 Hoenn-only maps + 440 layouts, 7-line mapjson patch (NULL slots) | 26,036,744 | 785,640 | 7.169 MiB |
| B2 B1 + do not assemble 428 Hoenn map scripts (40 stay, C needs them) | 25,573,504 | 1,248,880 | 7.611 MiB |
| B3 B2 + drop the C data of 87 dead tilesets | 25,236,776 | 1,585,608 | 7.932 MiB |
| B4 B3 + drop the 124 Hoenn rows of gWildMonHeaders | 25,216,748 | 1,605,636 | 7.951 MiB |
| --- variants --- | | | |
| L1 apply_skip.sh level 1 (templates live) | 26,038,532 | 783,852 | 7.168 MiB |
| L2 apply_skip.sh level 2 (+ scripts not assembled) | 25,575,292 | 1,247,092 | 7.610 MiB |
| R  RECOMMENDED SKIP level 3 (apply_skip.sh 3 + Battle Tower kept): templates live, no tileset pruning | 25,559,560 | 1,262,824 | 7.625 MiB |
| H  hybrid: B2 + physically delete 253 unreferenced Hoenn maps + 421 FRLG folders (no tileset pruning) | 25,553,292 | 1,269,092 | 7.630 MiB |
| F  only delete the 421 FRLG map folders (zero code edits) | 26,822,232 | 152 | 6.420 MiB |

Re-measured on the current HEAD 04385f05 (author imported 70 overworld sprites and 94 battle pictures in between, +238,108 bytes):
| step | ROM used (bytes) | saved | free of 32 MiB |
|---|---:|---:|---:|
| A leave as is (HEAD 04385f05) | 27,060,492 | 0 | 6.193 MiB |
| R recommended SKIP (apply_skip.sh 3, Battle Tower kept) | 25,797,668 | 1,262,824 | 7.397 MiB |
