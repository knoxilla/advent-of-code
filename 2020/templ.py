#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("../")

from falala import tada


def figure_it_out(data):

    return len(data)


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        input_file_name = sys.argv[1]  # input or test%
    else:
        input_file_name = "input"

    testing = False
    if "test" in input_file_name:
        testing = True
        print(f"Evaluting test scenario...")
        solution = 0
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
