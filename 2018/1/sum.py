#!/usr/bin/env python3

with open('numbers', 'r') as f:
    nums = f.read().splitlines()

print(sum([int(num) for num in nums]))
