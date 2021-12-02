#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("../")

from falala import tada


def figure_it_out(data):

    initial_position = [0,0] # depth, horizontal
    moves = [initial_position]

    for d in data:
        axis, how_far = d.split(' ')
        how_far = int(how_far)
        if axis == 'forward':
            moves.append([0,how_far])
        elif axis == 'up':
            moves.append([-how_far,0])
        elif axis == 'down':
            moves.append([how_far,0])
        else:
            print('movement direction unclear!!!')

    current_position = list(map(sum, zip( * moves)))

    print(current_position)

    return current_position[0] * current_position[1]


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        input_file_name = sys.argv[1]  # input or test%
    else:
        input_file_name = "input"

    testing = False
    if "test" in input_file_name:
        testing = True
        print(f"Evaluting test scenario...")
        solution = 150
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
