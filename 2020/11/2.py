#!/usr/bin/env python3

from copy import deepcopy
import sys
sys.path.append("../")
from falala import tada

source_file = "input"

with open(source_file, "r") as f:
    input = f.read().splitlines()

crowded_threshhold = 5

rows = len(input)
cols = len(input[0])

# pad out the layout for convenience in the helpers
for idx, i in enumerate(input):
    input[idx] = f"L{i}L"
    input[idx] = [c for c in input[idx]]
pad = [c for c in "L" * (cols + 2)]
input.append(pad.copy())
input.insert(0, pad.copy())

for idx,i in enumerate(input):
  # if idx > 0 and idx < len(input)-1:
    print("".join(i)) #[1:-1])
print("")

def crowded(r,c):
    return clearview(r,c)

def clearview(r, c):
    clear = True
    neighbors = 0

    value = input[r][c]

    # horizontal
    row = [i for i in input[r]]
    row[c] = "X"
    tester = "".join(row).replace('.',"")
    if "LXL" not in tester:
        clear = False
    if "#X#" in tester:
        neighbors += 2
    elif "#X" in tester or "X#" in tester:
        neighbors += 1

    # if (r,c) in [(2,1),(2,9),(8,10),(9,1)]:
        # print(r,c,value,clear,neighbors)

    # vertical
    col = [input[r][c] for r in range(0,len(input))]
    col[r] = "X"
    tester = "".join(col).replace('.',"")
    if "LXL" not in tester:
        clear = False
    if "#X#" in tester:
        neighbors += 2
    elif "#X" in tester or "X#" in tester:
        neighbors += 1

    # if (r,c) in [(2,1),(2,9),(8,10),(9,1)]:
        # print(r,c,value,clear,neighbors)

    # falling diagonal
    # up and left
    # go up and over until c or r is 0, i.e subtract the MIN or r and c
    # down and right
    # go down and over until c or r is len, i.e. add the MIN of len-c or len-r
    start = (r - min(c,r),c - min(c,r))
    offset = len(input) - max(r,c)
    end = (r + offset, c + offset)
    diag_falling = []
    for idx,i in enumerate(range(start[0],end[0],1)):
        j = [v for v in range(start[1],end[1],1)][idx]
        if (i,j) == (r,c):
            diag_falling.append('X')
        else:
            diag_falling.append(input[i][j])
    tester = "".join(diag_falling).replace('.',"")
    if "LXL" not in tester:
        clear = False
    if "#X#" in tester:
        neighbors += 2
    elif "#X" in tester or "X#" in tester:
        neighbors += 1

    # if (r,c) in [(2,1),(2,9),(8,10),(9,1)]:
        # print(r,c,value,clear,neighbors)

    # rising diagonal
    # down and left
    # go down and over until c is 0 or r is len
    #  i.e. if r-to-len < c, start at row = len, col = c - r-to-len
    #  else r = c, start at row = len, col = 0
    #  else r-to-len > c, start at row = , col =
    # up and right
    # go up and over until c is len or r is 0
    # i.e.

    if r + c <= len(input):
        start = (r + c, 0)
        end = (0, r + c)
    elif r + c > len(input):
        start = (len(input), c - (len(input) - r))
        end = (r - (len(input) - c),len(input))
    diag_rising = []
    # neighbors += 1
    # print(start,end)
    for idx,i in enumerate(range(start[0],end[0],-1)):
        j = [v for v in range(start[1],end[1],1)][idx]
        # print(idx,i,j,'-',r,c)
        if (i,j) == (r,c):
            diag_rising.append('X')
        else:
            try:
                diag_rising.append(input[i][j])
                # print("".join(diag_rising))
            except:
                # print("--",r,c)
                # print("".join(diag_rising))
                pass
            #     print('WOWOWOWOWWO')
            #     print("".join(diag_rising))
                # diag_rising.append(input[i][j])
                # diag_rising.append('%')
    tester = "".join(diag_rising).replace('.',"")
    # if (r,c) in [(2,1),(2,9),(8,10),(9,1)]:
    # print(r,c,value,"".join(diag_rising))
    # if "LXL" not in tester:
    #     clear = False
    if "#X#" in tester:
        neighbors += 2
    elif "#X" in tester or "X#" in tester:
        neighbors += 1

    if (r,c) in [(2,1),(2,9),(8,10),(9,1)]:
        print(r,c,value,clear,neighbors)
        # print("")

    if value == 'L':
        return clear
    elif value == "#":
        return neighbors >= 5


hashable = tuple([tuple(i) for i in input])
input_hash = hash(hashable)
# start with an all floor and just flip the #s and Ls
floor = [c for c in "." * (cols)]
floor.append("L")
floor.insert(0,"L")
output = [floor.copy() for x in range(rows)]
output.append(pad.copy())
output.insert(0, pad.copy())
output_hash = 0

for idx,o in enumerate(output):
  # if idx > 0 and idx < len(output)-1:
    print("".join(o)) #[1:-1])
print("")

print("Please stand by...\n")

iterations = 0
while True:

    iterations += 1

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):

            status = input[r][c]

            # occupied...
            if status == "#":
                if crowded(r, c):
                    output[r][c] = "L"
                    continue

            # empty...
            if status == "L":
                if clearview(r, c):
                    output[r][c] = "#"

    hashable = tuple([tuple(i) for i in output])
    output_hash = hash(hashable)
    input = deepcopy(output)

    print("")
    for idx,o in enumerate(output):
        if idx > 0 and idx < len(output) -1:
            print("".join(o)[1:-1])
    print(f"\nIterations: {iterations}\n")

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
