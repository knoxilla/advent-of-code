#!/usr/bin/env python3

import sys
sys.path.append("../")
from falala import tada

with open("input", "r") as f:
    input = f.read().splitlines()

original_code = []
for ptr, instr in enumerate(input):
    op, arg = instr.split(" ")
    original_code.append((ptr, op, int(arg)))


for idx in range(len(original_code)):
    ptr, op, arg = original_code[idx]

    if op == "nop":
        op = "jmp"
    elif op == "jmp":
        op = "nop"
    else:
        continue

    code = original_code.copy()
    code[idx] = (ptr, op, arg)

    found_it = False
    seen_ptrs = []
    current_ptr = accumulator = 0

    print(f"Trying variant {idx}...")

    while current_ptr not in seen_ptrs:
        ptr, op, arg = code[current_ptr]
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

        if current_ptr == len(code):
            found_it = True
            print(f"{ptr}\t{op}\t{str(arg).rjust(4)}\t{accumulator}")
            tada(f"Variant {idx} halted with accumator value {accumulator}!")
            break

    if found_it:
        break
