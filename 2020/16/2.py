#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
import math
import re
import sys

sys.path.append("../")

from falala import tada


valid_tickets = []
invalid_tickets = []
errors = []


def figure_it_out(field_key, my_ticket, nearby_tickets):

    all_valid_nums = []
    field_valid_nums = defaultdict(list)

    for k, value in field_key.items():
        for rng in value:
            all_valid_nums.extend(list(range(rng[0], rng[1] + 1)))
            field_valid_nums[k].extend(list(range(rng[0], rng[1] + 1)))

    for tkt in nearby_tickets:
        invalid = list(set(tkt).difference(all_valid_nums))
        if invalid:
            errors.extend(invalid)
            invalid_tickets.append(tkt)
        else:
            valid_tickets.append(tkt)

    print(f"Ticket error rate for these tickets is {sum(errors)}...")
    print(f"Keeping only valid tickets - including my own...\n")
    valid_tickets.append(my_ticket)

    candidates = defaultdict(list)
    for idx in range(len(my_ticket)):
        for fld, values in field_valid_nums.items():
            # print(f"Field {idx+1}")
            possible = []
            for tkt in valid_tickets:
                could_be = tkt[idx] in values
                possible.append(could_be)
            if all(possible):
                candidates[idx + 1].append(fld)
                print(f"ticket field {idx+1} COULD BE {fld}")
        # print(dict(candidates))
        print("")

    best_candidates = sorted(candidates.keys(), key=lambda v: len(candidates.get(v)))

    final_field_list = []
    mapped = []
    final_field_map = {}

    for b in best_candidates:
        only_choices = [f for f in candidates[b] if f not in mapped]
        must_be = only_choices[0]
        final_field_list.append(must_be)
        mapped.append(must_be)
        # only care about the mapping for these fields
        if must_be.startswith("departure"):
            final_field_map[must_be] = b

    answer = 1
    for k, v in final_field_map.items():
        # v is 1-indexed for reading like a human
        # so we need v-1 to get the 0-indexed field from my_ticket
        print(f"{k} is recorded in field {v}: {my_ticket[v-1]}")
        answer = answer * my_ticket[v - 1]
    print("")

    return answer


def parse_data(data):

    field_key = {}
    my_ticket = []
    nearby_tickets = []
    section = 1

    for d in data:
        # print(section,d)
        if d == "":
            section += 1
            continue
        if section == 1:
            field, valid = d.split(":")
            findings = re.findall("\d+\-\d+", valid)
            findings = [tuple(map(int, f.split("-"))) for f in findings]
            field_key[field] = findings
        elif section == 2:
            if "ticket" in d:
                continue
            my_ticket = d.split(",")
            my_ticket = list(map(int, my_ticket))
        elif section == 3:
            if "ticket" in d:
                continue
            this_ticket = d.split(",")
            this_ticket = list(map(int, this_ticket))
            nearby_tickets.append(this_ticket)

    return (field_key, my_ticket, nearby_tickets)


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        input_file_name = sys.argv[1]  # input or test%
    else:
        input_file_name = "input"

    testing = False
    if "test" in input_file_name:
        testing = True
        print(f"Evaluting test scenario...")
        solution = 71  # 4 + 55 + 12
    else:
        solution = None

    with open(input_file_name, "r") as f:
        data = f.read().splitlines()

    field_key, mine, nearby = parse_data(data)

    result = figure_it_out(field_key, mine, nearby)

    tada(f"The product of the 'departure' fields is {result}")

    if testing == True:
        if result == int(solution):
            tada(f"Passed! {'✅'}")
        else:
            print(f"Nope! {'❌'}")
