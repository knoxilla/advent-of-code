#!/usr/bin/env python3

from collections import defaultdict
import itertools
import re
import sys

sys.path.append("../")

from falala import tada


# the memory was zero to begin with
# defaultdict will work, but this isn't really bitwise AT ALL
memory = defaultdict(int)
mask = 0


def turn_bit_on(num, bit):
    return num | (1 << (bit - 1))


def turn_bit_off(num, bit):
    return num & ~(1 << (bit - 1))


def figure_it_out(data):
    for idx, d in enumerate(data):
        d = d.replace(" ", "")
        cmd, val = d.split("=")

        if cmd == "mask":
            mask = val
        elif cmd.startswith("mem"):
            mem_loc = int(re.search("\d+", cmd).group())
            val = int(val)
            fbits = []
            for idx, m in enumerate(reversed(mask)):
                if m == "1":
                    mem_loc = turn_bit_on(mem_loc, idx + 1)
                elif m == "X":
                    # zero out these bits - we'll cycle through all possible
                    # combinations of values just below
                    mem_loc = turn_bit_off(mem_loc, idx + 1)
                    # keep track of floating bits
                    fbits.append(idx + 1)

            # how many ways can we set N bits to 1s and 0s?
            combos = list(itertools.product([0, 1], repeat=len(fbits)))
            # to hold our actual mem_locs
            mem_locs = []

            for combo in combos:
                new_loc = mem_loc
                for idx, bit in enumerate(combo):
                    if bit == 0:
                        new_loc = turn_bit_off(new_loc, fbits[idx])
                    else:
                        new_loc = turn_bit_on(new_loc, fbits[idx])
                mem_locs.append(new_loc)

            for m in mem_locs:
                memory[m - 1] = val
        else:
            print(f"BOOM - unknown instruction at line {idx+1}: {cmd} {val}")
            exit(1)

    # now it's a dict, loc -> val, so sum the values
    return sum(memory.values())


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        input_file_name = sys.argv[1]  # input or test%
    else:
        input_file_name = "input"

    testing = False
    if "test" in input_file_name:
        testing = True
        print(f"Evaluting test scenario...")
        solution = 208
    else:
        solution = None

    with open(input_file_name, "r") as f:
        data = f.read().splitlines()

    result = figure_it_out(data)

    tada(f"{result}")

    if solution is not None and result == int(solution):
        tada(f"Passed! {'✅'*(1)}")
    # else:
    #     print("...")
    # print("-----\n")
