#!/usr/bin/env python3

from collections import namedtuple

with open("input", "r") as f:
    entries = f.read().splitlines()

# parse into list of lists
to_check = [e.replace("-", " ").replace(":", "").split(" ") for e in entries]

# ints are ints!
for t in to_check:
    t[0] = int(t[0])
    t[1] = int(t[1])

# now we have list of these: [min,max,letter,pword]

Checkable = namedtuple("Checkable", "min max letter pword")

tally = 0
for entry in to_check:
    this = Checkable(*entry)
    if this.letter not in this.pword:
        continue
    occurences = this.pword.count(this.letter)
    if occurences < this.min or occurences > this.max:
        continue
    tally += 1

print(tally)
