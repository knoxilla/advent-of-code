#!/usr/bin/env python3

import sys

sys.path.append("../")

from falala import tada

checkpoint = 2020


def last_index(value, lst):
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1


def figure_it_out(data):

    start_nums = [int(x) for x in data.split(",")]

    utterances = []

    for turn in range(0, checkpoint):

        if turn < len(start_nums):
            utterances.append(start_nums[turn])
        else:
            if utterances[-1] not in utterances[:-1]:
                utterances.append(0)
            else:
                last = last_index(utterances[-1], utterances[:-1])
                utterances.append((turn - 1) - last)
        # print(turn+1, utterances[-1])

    return utterances[-1]


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        input_file_name = sys.argv[1]  # input or test%
    else:
        input_file_name = "input"

    testing = False
    if "test" in input_file_name:
        testing = True
        solution = 0
    else:
        solution = None

    with open(input_file_name, "r") as f:
        input = f.read().splitlines()

    if not testing:
        data = input[0]
        result = figure_it_out(data)
        tada(f"{result}")
    else:
        # input = input[:1]
        for idx, line in enumerate(input):
            if testing:
                print(f"Evaluting test scenario {idx + 1}...")
                data, solution = line.split(":")
            else:
                data, solution = line, None

            result = figure_it_out(data)

            tada(result)

            if solution and result == int(solution):
                tada(f"Passed! {'✅'*(idx+1)}")
                print("")
            else:
                print("Nope")
