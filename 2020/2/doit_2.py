#!/usr/bin/env python3

from collections import namedtuple
from operator import xor

with open("input", "r") as f:
    entries = f.read().splitlines()

# parse into list of lists
to_check = [e.replace("-", " ").replace(":", "").split(" ") for e in entries]

# ints are ints!
# also, make them python-style indices
for t in to_check:
    t[0] = int(t[0]) - 1
    t[1] = int(t[1]) - 1

# now we have a list of these: [pos1,pos2,letter,pword]

Checkable = namedtuple("Checkable", "pos1 pos2 letter pword")

tally = 0
for entry in to_check:
    this = Checkable(*entry)
    if this.letter not in this.pword:
        continue
    if xor(this.pword[this.pos1] == this.letter, this.pword[this.pos2] == this.letter):
        tally += 1

print(tally)
