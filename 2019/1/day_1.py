#!/usr/bin/env python3

import math
import sys

total = 0
fuels = []

input = open(sys.argv[1], "r")
for item in input:
    fuels = []
    fuel = (math.floor(int(item) / 3)) - 2
    # total = total + fuel
    # fuel takes fuel!
    fuels.append(fuel)
    while fuel >= 0:
       fuel = (math.floor(fuel / 3)) - 2
       if fuel > 0:
           fuels.append(fuel)
    total = total + sum(fuels)

input.close()

print(total)
