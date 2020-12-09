#!/usr/bin/env python3

from itertools import combinations

import sys

sys.path.append("../")
from falala import tada

with open("input", "r") as f:
    input = f.read().splitlines()

input = [int(i) for i in input]
addends = input[:25]
message = input[25:]

calcs = 0
for idx, num in enumerate(message):
    foundit = False

    pairs = combinations(addends, 2)
    for p in pairs:
        calcs += 1
        if p[0] != p[1]:
            if sum(p) == num:
                foundit = True
                break

    if not foundit:
        # boom!
        break
    else:
        # move on to next num
        del addends[0]
        addends.append(num)

tada(
    f"The first invalid number in the message is {num} at position {idx} of {len(message)}"
)
