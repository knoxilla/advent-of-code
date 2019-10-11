#!/usr/bin/env python

from collections import Counter

file = open('jumps')

jumps = [int(line.strip()) for line in file.readlines()]

position = times = 0

print len(jumps)

while True:
    try:
        howfar = jumps[position]
        if howfar >= 3:
            jumps[position] += -1
        else:
            jumps[position] += 1
        position += howfar
        times += 1
        if times % 10000 == 0:
            print times,position,jumps[position]
    except IndexError:
        print "out of range..."
        break

print ""
print position
print times
