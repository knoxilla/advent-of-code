#!/usr/bin/env python3

from collections import Counter
import sys

sys.path.append("../")

from falala import tada

input_file = sys.argv[1] if len(sys.argv) == 2 else "input"

with open(input_file, "r") as f:
    input = f.read().splitlines()

# sorted ints please
input = list(map(int, input))

# answers for test inputs
# test1: 7 @ 1, 5 @ 3, 7*5 = 35
# test2: 22 @ 1, 10 @ 3, 22*10 = 220

jolt_target = max(input) + 3
input.append(jolt_target)
input.sort()
deltas = []

jolt_level = 0
for idx, adapter in enumerate(input):

    diff = adapter - jolt_level
    if diff <= 3:
        deltas.append(diff)
        jolt_level = adapter
    else:
        print("🚨 No next adapter for jolt_level {adapter}!")

if jolt_level == jolt_target:
    jolt_distrib = Counter(deltas)
    print("Joltage Gap Distribion")
    for k, v in jolt_distrib.items():
        print(f"  Gap of {k}: {v} times")
    solution = jolt_distrib[1] * jolt_distrib[3]
    tada(f"We did it! The puzzle answer is {solution}")
else:
    print("Hmmm.")
    print(deltas)
    print(jolt_level, jolt_target)
