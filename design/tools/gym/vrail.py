"""North-south railing for the Petalburg gym, drawn the Gen 3 way (Route 117's fence): seen from above, an 8 px
handrail with baluster tops, a front-facing end post, and T-junctions where an east-west railing joins.
Only the railing's own colours."""
import numpy as np
C = dict(out=(98, 98, 123), dark=(65, 74, 106), wood=(172, 106, 65), hi=(205, 139, 98), shade=(139, 74, 41),
         cap=(255, 213, 156), white=(255, 255, 255), blue=(180, 213, 238), blue2=(106, 180, 230))
X0, X1 = 4, 11            # rail occupies columns 4..11 (8 px), centred
def mid(floor):
    t = floor.copy()
    for y in range(16):
        t[y, X0] = C["out"]; t[y, X1] = C["dark"]
        t[y, X0 + 1] = C["hi"]; t[y, X0 + 2:X1 - 1] = C["wood"]; t[y, X1 - 1] = C["shade"]
        if y % 4 == 1:                                    # baluster tops, like the east-west railing's top row
            t[y, X0 + 2:X1 - 1] = [C["white"], C["blue"], C["blue"], C["blue2"]]
        if y % 4 == 2:
            t[y, X0 + 2:X1 - 1] = [C["blue"], C["blue2"], C["blue2"], C["shade"]]
    return t
def end_top(floor):
    t = mid(floor); t[0:2, X0:X1 + 1] = floor[0:2, X0:X1 + 1]; t[2, X0:X1 + 1] = C["out"]; return t
def end_bottom(rail_front, floor):
    """Top half handrail; bottom half the end post seen from the front (the railing's own front face, 8 px wide)."""
    t = mid(floor)
    t[8:16, X0:X1 + 1] = rail_front[8:16, 0:8]
    t[8:16, X0] = C["out"]; t[8:16, X1] = C["dark"]
    return t
def junction(floor, rail, side):
    """Vertical rail with an east-west railing attached on one side ('r' or 'l')."""
    t = floor.copy()
    if side == "r": t[:, X1:16] = rail[:, X1:16]
    else: t[:, 0:X0 + 1] = rail[:, 0:X0 + 1]
    v = mid(floor)
    t[:, X0:X1 + 1] = v[:, X0:X1 + 1]
    return t
