#!/usr/bin/env python3

from itertools import combinations

with open("report", "r") as f:
    info = f.read().splitlines()

entries = [int(i) for i in info]

# itertools ftw!

iterations = 0
for (a, b, c) in combinations(entries, 3):
    iterations += 1
    if a + b + c == 2020:
        print(a, b, c, a * b * c)
        break

print(iterations)
