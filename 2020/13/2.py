#!/usr/bin/env python3

import sys

sys.path.append("../")
from falala import tada


def figure_it_out(data):

    buses = [b for b in data.split(",")]

    offsets = {}
    num_buses = 0
    for idx, b in enumerate(buses):
        if b != "x":
            num_buses += 1
            buses[idx] = int(b)
            offsets[int(b)] = idx

    max_route_time = max(offsets.keys())
    min_route_time = min(offsets.keys())

    print(f"Minimum route time: {min_route_time}")
    print(f"Maximum route time: {max_route_time}")
    print(f"Evaluating for {num_buses} bus routes")
    print(f"Stand by...")

    print(offsets)

    departure = 0
    iterations = 0  # 1000000000000
    while True:
        iterations += 1

        # iterate on multiples of the big one
        departure = max_route_time * iterations

        # _but_ check the moduli of that multiple minus this bus' offset
        departure -= offsets[max_route_time]

        matched = 0
        for b in buses:
            if b != "x":
                if (departure + offsets[b]) % b == 0:
                    matched += 1
                else:
                    continue

        if iterations % 1000000 == 0:
            print(iterations, departure)

        if matched == num_buses:
            break

    tada(f"Earliest departure timestamp meeting the criteria: {departure}")

    return departure


if __name__ == "__main__":

    input_file_name = sys.argv[1]  # input or tests

    testing = False
    if "test" in input_file_name:
        testing = True

    with open(input_file_name, "r") as f:
        input = f.read().splitlines()

    # skip first line
    del input[0]

    for idx, line in enumerate(input):
        if testing:
            print(f"Evaluting test scenario {idx + 1}...")
            data, solution = line.split(" ")
        else:
            data, solution = line, None

        result = figure_it_out(data)

        if solution and result == int(solution):
            tada(f"Passed! {'✅'*(idx+1)}")
        else:
            print("...")

        print("-----\n")
