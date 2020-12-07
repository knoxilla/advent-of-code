#!/usr/bin/env python3

# from pprint import pprint
import re

from falala import tada

with open("input", "r") as f:
    input = f.read().splitlines()

bag_rules = dict()

for i in input:
    simplified = (
        i.replace(" contain", ",")
        .replace(" bags.", "")
        .replace(" bag.", "")
        .replace(" bags", "")
        .replace(" bag", "")
        .replace(" no other", "")
    )
    simplified = simplified.split(",")

    holder, *holdees = simplified

    holdee_tuples = []
    for h in holdees:
        if h is not "":
            h = h.lstrip().split(" ")
            quantity = int(h[0])
            which_type = "_".join(h[1:])
            parsed = (quantity, which_type)
            holdee_tuples.append(parsed)

    holder = holder.replace(" ", "_")
    bag_rules[holder] = holdee_tuples

# ok, finally we have the rules, this time with counts

# just curious
# terminal_bags = [ k for k,v in bag_rules.items() if v == []]
# print("Bags of no holding:")
# pprint(terminal_bags)

running_tally = 0


def tally_bags_within(bag):
    global running_tally
    rule = bag_rules[bag]

    # create list of next-level bags to check
    inner_bags = []
    for r in rule:
        running_tally += r[0]
        inner_bags.extend([r[1]] * r[0])

    # keep checking those bags - pun intended.
    for b in inner_bags:
        tally_bags_within(b)


# do the thing
tally_bags_within("shiny_gold")

tada(f"Wow: a single shiny gold bag holds {running_tally} inner bags. 😜")
