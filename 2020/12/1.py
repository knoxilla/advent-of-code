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
heading = 90
ew = 0
ns = 0

for d in course_plan:
    move = mv(*d)

    # print(ew, ns, moves[move.cmd], move.units, f"(heading: {heading})")

    if move.cmd == "N":
        ns += move.units
    elif move.cmd == "S":
        ns -= move.units
    elif move.cmd == "W":
        ew -= move.units
    elif move.cmd == "E":
        ew += move.units
    elif move.cmd == "F":
        if heading == 0:
            ns += move.units
        elif heading == 180:
            ns -= move.units
        elif heading == 270:
            ew -= move.units
        elif heading == 90:
            ew += move.units
    elif move.cmd == "L":
        heading = (heading - move.units) % 360
    elif move.cmd == "R":
        heading = (heading + move.units) % 360

tada(f"Manhattan distance at end of course, Cap'n: {abs(ew) + abs(ns)} units")
