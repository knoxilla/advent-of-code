#!/usr/bin/env python3

from collections import namedtuple

import sys

sys.path.append("../")
from falala import tada

with open("input", "r") as f:
    input = f.read().splitlines()

mv = namedtuple("mv", "cmd units")

course_plan = [(i[0], int(i[1:])) for i in input]

moves = {
    "N": "North",
    "S": "South",
    "E": "East",
    "W": "West",
    "F": "Forward",
    "L": "Port",
    "R": "Starboard",
}

# just in case
headings = {"N": 0, "E": 90, "S": 180, "W": 270}
degrees = dict(map(reversed, headings.items()))

# so it begins...
waypoint = [10, 1]
ew = 0
ns = 0

for d in course_plan:
    move = mv(*d)

    # print(ew, ns, moves[move.cmd], move.units)

    if move.cmd == "N":
        waypoint[1] += move.units
    elif move.cmd == "S":
        waypoint[1] -= move.units
    elif move.cmd == "W":
        waypoint[0] -= move.units
    elif move.cmd == "E":
        waypoint[0] += move.units
    elif move.cmd == "F":
        ew += waypoint[0] * move.units
        ns += waypoint[1] * move.units
    elif move.cmd == "L":
        x, y = waypoint
        if move.units == 90:
            waypoint = [-y, x]
        elif move.units == 270:
            waypoint = [y, -x]
        elif move.units == 180:
            waypoint = [-x, -y]
    elif move.cmd == "R":
        x, y = waypoint
        if move.units == 90:
            waypoint = [y, -x]
        elif move.units == 270:
            waypoint = [-y, x]
        elif move.units == 180:
            waypoint = [-x, -y]
    else:
        print(f"🚨 unknown command: {move}")
        break

    # print(ew, ns, waypoint,"\n")

tada(f"Manhattan distance at end of course, Cap'n: {abs(ew) + abs(ns)} units")
