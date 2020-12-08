#!/usr/bin/env python3

import sys
sys.path.append("../")
from falala import tada

with open("input", "r") as f:
    input = f.read().splitlines()

tada(len(input))
