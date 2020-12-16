#!/usr/bin/env python3

import re
import sys

sys.path.append("../")

from falala import tada


# the memory was zero to begin with
memory = [0] * 2 ** 16
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
            for idx, m in enumerate(reversed(mask)):
                if m == "0":
                    val = turn_bit_off(val, idx + 1)
                elif m == "1":
                    val = turn_bit_on(val, idx + 1)
            memory[mem_loc - 1] = val
        else:
            print(f"BOOM - unknown instruction at line {idx+1}: {cmd} {val}")
            exit(1)
    return sum(memory)


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        input_file_name = sys.argv[1]  # input or test%
    else:
        input_file_name = "input"

    testing = False
    if "test" in input_file_name:
        testing = True
        print(f"Evaluting test scenario...")
        solution = 165
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
