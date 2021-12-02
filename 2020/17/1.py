#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from itertools import chain, permutations
import operator
from pprint import pprint
import sys

sys.path.append("../")

from falala import tada

cycles = 6
cycles = 2


def cubify(cell):
        sweeper = [-1,0,1]
        neighbors = []
        for sx in sweeper:
            for sy in sweeper:
                for sz in sweeper:
                    # print(sx,sy,sz)
                    n = [ x+y for x,y in zip(cell,[sx,sy,sz])]
                    neighbors.append(n)
        return neighbors

def flatten(input):
    try:
        it_is = iter(input)
    except TypeError:
        yield input
    else:
        for i in it_is:
            for j in flatten(i):
                yield j

def pad_span(input):
    xspan,yspan,zspan = [len(input[0]),len(input[0][0]),len(input)]

def figure_it_out(input):

    for c in range(cycles):
        print(f"Cycle {c+1}...")

        pprint(input)
        xspan,yspan,zspan = [len(input[0]),len(input[0][0]),len(input)]
        print([xspan,yspan,zspan])

        actives = sum(flatten(input))
        print(f"Entering cycle with {actives} active cells")

        cells = []
        for x in range(xspan):
            for y in range(yspan):
                for z in range(zspan):
                    cell_addr = [x+1,y+1,z+1]
                    cells.append(cell_addr)

        output = []
        for cell in cells:
            neighbors = cubify(cell)
            output.extend(neighbors)
        output = [tuple(o) for o in output]
        output = set(output)
        output = sorted(output, key=operator.itemgetter(0,1,2))

        # if # and exactly 2 or 3 neighbors are #, remain #, else become .
        # if . and exactly 3 neighbors are #, become #, else remain .

        active = 0
        for r in data:
            for c in r:
                if c == '#':
                    active += 1

        # actives = sum(flatten(output))
        print(f"Leaving cycle with {len(output)} cells to consider")

        input = deepcopy(list(input))

    return active


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        input_file_name = sys.argv[1]  # input or test%
    else:
        input_file_name = "input"

    testing = False
    if "test" in input_file_name:
        testing = True
        print(f"Evaluting test scenario...")
        solution = 112
    else:
        solution = None

    with open(input_file_name, "r") as f:
        data = f.read().splitlines()

    parsed = []
    for r in data:
        row = []
        for c in str(r):
            if c == "#":
                row.append(1)
            else:
                row.append(0)
        parsed.append(row)
    # send it as a 3D array of z length 1
    result = figure_it_out([parsed])

    tada(f"{result}")

    if solution is not None and result == int(solution):
        tada(f"Passed! {'✅'*(1)}")
    else:
        print(f"Nope! {'❌'}")
