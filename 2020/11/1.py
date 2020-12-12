#!/usr/bin/env python3

from copy import deepcopy
import sys
sys.path.append("../")
from falala import tada

source_file = "input"

with open(source_file, "r") as f:
    input = f.read().splitlines()

rows = len(input)
cols = len(input[0])

# pad out the layout for convenience in the helpers
for idx, i in enumerate(input):
    input[idx] = f".{i}."
    input[idx] = [c for c in input[idx]]
pad = [c for c in "." * (cols + 2)]
input.append(pad)
input.insert(0, pad)

# helpers
def crowded(r, c):
    neighbors = 0
    for subc in [c - 1, c, c + 1]:
        for subr in [r - 1, r, r + 1]:
            if input[subr][subc] == "#":
                if (r, c) != (subr, subc):
                    neighbors += 1
    return neighbors >= 4


def neighborless(r, c):
    for subc in [c - 1, c, c + 1]:
        for subr in [r - 1, r, r + 1]:
            if input[subr][subc] == "#":
                return False
    return True


hashable = tuple([tuple(i) for i in input])
input_hash = hash(hashable)
# start with an all floor and just flip the #s and Ls
output = [pad.copy() for x in range(rows + 2)]
output_hash = 0

print("Please stand by...")

iterations = 0
while True:

    iterations += 1

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):

            status = input[r][c]

            # occupied...
            if status == "#":
                if crowded(r, c):
                    # flip
                    output[r][c] = "L"
                    continue

            # empty...
            if status == "L":
                if neighborless(r, c):
                    # flip
                    output[r][c] = "#"

    hashable = tuple([tuple(i) for i in output])
    output_hash = hash(hashable)
    input = deepcopy(output)

    if output_hash == input_hash:
        tally = 0
        for idx, r in enumerate(output):
            for c in r:
                if c == "#":
                    tally += 1
            if idx == 0 or idx == len(output) - 1:
                continue
        break

    # keep going until things quiet down
    input_hash = output_hash


tada(f"After {iterations} rounds, we settled down to {tally} occupied seats")
