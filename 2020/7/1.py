#!/usr/bin/env python3

import re

from falala import tada

with open("input", "r") as f:
    input = f.read().splitlines()

bag_types = set()
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
    simplified = re.sub(" \d+ ", "", simplified)
    simplified = simplified.replace(" ", "_").split(",")

    # add all bag types mentioned in this rule to the set of all
    bag_types.update(simplified)

    # unpack with * to get the head and tail of this list
    holder, *holdees = simplified
    bag_rules[holder] = holdees

# emptiness is not a bag type!
bag_types.remove("")
bags = sorted(list(bag_types))

# tada(f"There are {len(bag_rules.keys())} rules for {len(bags)} bag types")

# function to make comprehensions clearer
def can_hold_shiny_gold(bag):
    return "shiny_gold" in bag_rules[bag]


# gather up all bag types that can contain directrly
shiny_gold_parents = [k for k, v in bag_rules.items() if can_hold_shiny_gold(k)]
shiny_gold_ancestors = set(shiny_gold_parents.copy())

# now check the reminder of the bag types
bags_to_check = bag_types - shiny_gold_ancestors

# function to make comprehensions clearer
def can_hold_shiny_gold_ancestor(bag):
    # print(bag)
    # print(shiny_gold_ancestors)
    return any(item in shiny_gold_ancestors for item in bag_rules[bag])


# keep looking for bags that hold a known shiny_gold holder
while True:
    next_level_holders = [b for b in bags_to_check if can_hold_shiny_gold_ancestor(b)]
    if not next_level_holders:
        break
    shiny_gold_ancestors.update(set(next_level_holders))
    bags_to_check -= set(next_level_holders)


tada(
    f"There are {len(shiny_gold_ancestors)} bag types that can eventually contain a shiny gold bag"
)
