#!/usr/bin/env python3

import sys

sys.path.append("../")
from falala import tada

input_file = "input"

with open(input_file, "r") as f:
    input = f.read().splitlines()


dep_time = int(input[0])

buses = sorted([int(b) for b in input[1].split(",") if b != "x"])

wait_times = {}
for b in buses:
    # inverted dict here - wait_time: bus_id
    wait_times[b - (dep_time % b)] = b

# they said there woudl be only one
min_time = min(wait_times.keys())
bus_id = wait_times[min_time]

tada(
    f"Bus {bus_id} arrives {min_time} minute(s) after my earliest departure: {bus_id * min_time}"
)
