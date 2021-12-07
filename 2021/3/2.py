#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("../")

from falala import tada

def filter_array(arr,where,how,what):

    half = len(arr) // 2

    trans = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

    ones = trans[where].count('1')
    zeros = trans[where].count('0')

    if ones > zeros:
        what = '1'
        if how == 'min':
            what = '0'
    elif ones < zeros:
        what = '0'
        if how == 'min':
            what = '1'
    elif ones == zeros:
        print("EVEN")
        pass

    # print(trans[where], where+1, what, half)

    result = []
    for a in arr:
        # print(a,a[where],what)
        if a[where] == what:
            result.append(a)

    return result



def figure_it_out(data):

    # make data 2D array of single chars
    arr = [ list(d) for d in data ]

    # transpose that array
    trans = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

    # for t in trans:
    #     print(t)
    # print('----')

    # where is the breakpoint
    word_length = len(trans[0])
    half = word_length // 2

    oxy = co2 = '0'

    oxy_tiebreak = '1'
    co2_tiebreak = '0'

    filtered = arr.copy()
    idx = 0
    while True:
        print(len(filtered))
        filtered = filter_array(filtered,idx,'max',oxy_tiebreak)
        if len(filtered) == 1:
            break
        idx += 1

    oxy = "".join(filtered[0])
    print(oxy)

    filtered = arr.copy()
    idx = 0
    while True:
        print(len(filtered))
        filtered = filter_array(filtered,idx,'min',co2_tiebreak)
        if len(filtered) == 1:
            break
        idx += 1

    co2 = "".join(filtered[0])
    print(co2)

    print(int(oxy,2),int(co2,2))

    solution = int(oxy,2) * int(co2,2)

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
        solution = 230 # 23 * 10
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
