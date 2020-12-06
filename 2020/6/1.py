#!/usr/bin/env python3

from falala import tada

with open("input", "r") as f:
    groups = f.read().replace("\n\n", "|").split("|")

all_group_yeses = []

for g in groups:
    member_answers = g.splitlines()
    unique_yeses = set("".join(member_answers))
    # print("".join(sorted(unique_yeses)))
    all_group_yeses.append(len(unique_yeses))

tada(f"The sum of 'yeses' for all {len(groups)} groups is {sum(all_group_yeses)}")
