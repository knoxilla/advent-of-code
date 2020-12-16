#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

sys.path.append("../")

from falala import tada


valid_tickets = []
invalid_tickets = []
errors = []


def figure_it_out(field_key, my_ticket, nearby_tickets):

    all_valid_nums = []
    for k, value in field_key.items():
        for rng in value:
            all_valid_nums.extend(list(range(rng[0], rng[1] + 1)))

    for tkt in nearby_tickets:
        invalid = list(set(tkt).difference(all_valid_nums))
        if invalid:
            errors.extend(invalid)
            invalid_tickets.append(tkt)
        else:
            valid_tickets.append(tkt)

    # print(f"\nError-causing nums: {errors}\n")

    return sum(errors)


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

    tada(f"The ticket error rate for these tickets is {result}")

    if testing == True:
        if result == int(solution):
            tada(f"Passed! {'✅'}")
        else:
            print(f"Nope! {'❌'}")
