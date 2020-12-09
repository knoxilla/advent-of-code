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

for idx, num in enumerate(message):
    foundit = False

    pairs = combinations(addends, 2)
    for p in pairs:
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

tada(f"The target number in the message is {num} at position {idx+1} of {len(message)}")

target = num

for start, num in enumerate(input):

    foundit = False
    for end in range(1, len(input) + 1):
        possible = input[start:end]
        if sum(possible) > target:
            # print("moving on - already too big!",start,num,len(possible),sum(possible))
            break
        if sum(possible) == target:
            foundit = True
            break
    if foundit:
        break

if foundit:
    answer_length = len(possible)
    start_value = possible[0]
    end_value = possible[-1]
    min_value = min(possible)
    max_value = max(possible)
    puzzle_answer = min_value + max_value
    tada(
        f"Found a {answer_length}-addend series running from {start_value} to {end_value} sums to the target. Boom!"
    )
    tada(f"The puzzle solution is {puzzle_answer}")
    # print(possible)
else:
    tada("Well, that didn't work at all.")
