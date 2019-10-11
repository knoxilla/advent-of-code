#!/usr/bin/env python

import os
import sys
from pprint import pprint as pp

# start up
safecount = 0
firstrow = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."
nextrow = firstrow

safecount += nextrow.count(".")
print(nextrow)
input = ".%s." % nextrow

rowcount = 40
#rowcount = 400000

def output(trio):
	if trio == "..^":
		return "^"
	elif trio == ".^^":
		return "^"
	elif trio == "^^.":
		return "^"
	elif trio == "^..":
		return "^"
	else:
		return "."

for row in range(1,rowcount):
	nextrowtiles = []
	for i, row in enumerate(input):
		trio = input[i:i+3]
		if len(trio) == 3:
			nextrowtiles.append(output(trio))
	nextrow = ''.join(nextrowtiles)
	safecount += nextrow.count(".")
	print(nextrow)
	input = ".%s." % nextrow

print("Safe tiles: %s" % safecount)