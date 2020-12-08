#!/usr/bin/env python3

import sys
sys.path.append("../")
from falala import tada

with open("input", "r") as f:
    input = f.read().splitlines()

code = []
for ptr, instr in enumerate(input):
    op, arg = instr.split(" ")
    code.append((ptr, op, int(arg)))

seen_ptrs = []
current_ptr = accumulator = 0

while current_ptr not in seen_ptrs:
    ptr, op, arg = code[current_ptr]
    # print(f"{ptr}\t{op}\t{str(arg).rjust(4)}\t{accumulator}")
    seen_ptrs.append(current_ptr)
    if op == "nop":
        current_ptr += 1
    elif op == "jmp":
        current_ptr += arg
    elif op == "acc":
        accumulator += arg
        current_ptr += 1
    else:
        print(f"Oops: {code[curent_ptr]}")
        break

tada(f"Before starting infinite loop, accumulator is {accumulator}")
