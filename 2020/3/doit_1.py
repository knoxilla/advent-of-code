#!/usr/bin/env python3

with open("forest", "r") as f:
    pattern = f.read().splitlines()

startfile = 3
step = 3
rank = 0
trees = 0

# our modulo for loopin' 'round the pattern lines
pattern_width = len(pattern[0])

print(pattern[rank])

for pos in range(startfile, 3 * len(pattern), step):
    rank += 1

    if rank == len(pattern):
        break

    over = pos % pattern_width

    pattern_list = list(pattern[rank])

    if pattern[rank][over] == "#":
        pattern_list[over] = "X"
        trees += 1
    else:
        pattern_list[over] = "O"

    sled_track = "".join(pattern_list)
    print(sled_track)

print(f"\n{trees} trees encountered!")
