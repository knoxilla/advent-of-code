#!/usr/bin/env python3

from itertools import cycle

with open('numbers', 'r') as f:
    nums = f.read().splitlines()
vals = [int(num) for num in nums]

current_sum = 0
seen = [0]

print(len(vals))

for v in cycle(vals):
   current_sum = current_sum + v
   if current_sum not in seen:
      seen.append(current_sum)
#      print(seen)
   else:
      print(seen)
      print(len(seen))
      print(current_sum)
      break
   if len(seen) % len(vals) == 0:
      print('loop')
      print(seen)


