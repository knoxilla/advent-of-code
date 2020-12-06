#!/usr/bin/env python3

from collections import Counter

from falala import tada

with open("input", "r") as f:
    groups = f.read().replace("\n\n", "|").split("|")

all_group_totals = []

for g in groups:
    member_answers = g.splitlines()
    answer_counts = Counter("".join(member_answers))
    # print(answer_counts)
    all_said_yes = {
        answer: count
        for answer, count in answer_counts.items()
        if count == len(member_answers)
    }
    # print(all_said_yes)

    all_group_totals.append(len(all_said_yes))

tada(f"The sum of common yeses for all {len(groups)} groups is {sum(all_group_totals)}")
