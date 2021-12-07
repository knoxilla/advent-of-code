#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("../")

from falala import tada


def figure_it_out(data):

    # make data 2D array of single chars
    arr = [ list(d) for d in data ]

    # transpose that array
    trans = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

    word_length = len(trans[0])
    half = word_length // 2

    gamma_bits = epsilon_bits = ""

    for arr in trans:
        # print(int("".join(arr),2)) # decimal number
        ones = arr.count('1')
        if ones > half:
            gamma_bits += "1"
            epsilon_bits += "0"
        else:
            gamma_bits += "0"
            epsilon_bits += "1"

    solution = int(gamma_bits,2) * int(epsilon_bits,2)

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
        solution = 198 # 22 x 9
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
