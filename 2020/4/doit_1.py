#!/usr/bin/env python3

from falala import tada

with open("data", "r") as f:
    raw = f.read()

clean = raw.replace("\n\n", "|").replace("\n", " ").split("|")

valid = 0
for row in clean:
    parts = row.split(" ")
    d = {k: v for (k, v) in [tuple(p.split(":")) for p in parts]}
    fields = set(d.keys())
    if len(fields) == 8 or (len(fields) == 7 and "cid" not in fields):
        valid += 1

tada(f"{valid} out of {len(clean)} passports are valid-ish.")
