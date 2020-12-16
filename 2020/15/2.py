#!/usr/bin/env python3

from collections import defaultdict
import operator
import sys

sys.path.append("../")

from falala import tada

checkpoint = 30000000


def figure_it_out(data):

    start_nums = [int(x) for x in data.split(",")]

    times_seen = defaultdict(int)
    indices = defaultdict(list)

    for turn in range(0, checkpoint):

        if turn < len(start_nums):
            next_val = start_nums[turn]
        else:
            if times_seen[last_uttered] == 1:
                next_val = 0
            else:
                seen_at = indices[last_uttered][-2:]
                next_val = seen_at[1] - seen_at[0]

        times_seen[next_val] += 1
        indices[next_val].append(turn + 1)
        last_uttered = next_val

        # SLOW, but it works!
        if turn > 0 and turn % 5000000 == 0:
            print(f"Now at turn {turn}...")

    return last_uttered


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

        print("Humoring the elves. Please stand by...\n")
        result = figure_it_out(data)

        tada(f"The {checkpoint}th utterance will be {result}")
    else:
        input = input[:1]
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
