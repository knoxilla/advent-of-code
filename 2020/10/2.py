#!/usr/bin/env python3

from collections import defaultdict
from functools import lru_cache
from pprint import pprint
import sys

sys.path.append("../")

from falala import tada

input_file = sys.argv[1] if len(sys.argv) == 2 else "input"

with open(input_file, "r") as f:
    input = f.read().splitlines()

# ints please
input = list(map(int, input))

# add the wall and the device joltages to our node list
input.append(0)
input.append(max(input) + 3)
input.sort()

# there are no duplicate joltages, so I'll just
# use the joltage value as the label for each

def get_edges(source, remaining_adapters):
    possibles = [ a for a in remaining_adapters if a - source <= 3 ]
    return(possibles)

# make a graph in dict > list form
graph = defaultdict(list)
for idx, adapter in enumerate(input):
    edges = get_edges(adapter,input[idx+1:])
    for e in edges:
        graph[adapter].append(e)

# ok, now have a graph, time to start counting paths!
# pprint(graph)

@lru_cache(maxsize=None)
def count_paths_from_here_to_there(start, end):
    paths = 0
    for edge in graph[start]:
        if edge == end:
            paths += 1
        else:
            subpaths = count_paths_from_here_to_there(edge, end)
            paths += subpaths
    return paths

start = min(input)
end = max(input)

paths = count_paths_from_here_to_there(start, end)

tada(f"Woot! There are {paths} ways to connect up our adapters for a joltage span of {end}")

# answers for test inputs
# test1: 8 ways to connect ✅
# test2: 19208 ways to connect ✅
