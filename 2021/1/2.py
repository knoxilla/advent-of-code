#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("../")

from falala import tada


def figure_it_out(data):

    data = [ int(d) for d in data ]


    prior_total = None
    solution = 0
    for start in range(len(data)-2):
        measuring_window = data[start:start+3]
        current_total = sum(measuring_window)
        if prior_total and current_total > prior_total:
            # print('increased')
            solution += 1
        prior_total = current_total

    return solution

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        input_file_name = sys.argv[1]  # input or test%
    else:
        input_file_name = "input"

    testing = False
    if "test" in input_file_name:
        testing = True
        print(f"Evaluting test scenario...")
        solution = 5
    else:
        solution = None

    with open(input_file_name, "r") as f:
        data = f.read().splitlines()

    result = figure_it_out(data)

    tada(f"{result}")

    if solution is not None and result == int(solution):
        tada(f"Passed! {'✅'*(1)}")
    # else:
    #     print("...")
    # print("-----\n")
