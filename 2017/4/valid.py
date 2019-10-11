#!/usr/bin/env python

from collections import Counter

file = open('phrases')

lines = [l.strip() for l in file.readlines()]

valid = invalid = total = 0

for line in lines:
    words = line.split(" ")
    # next line only for part 2
    #words = [ ''.join(sorted(word)) for word in words ]
    words.sort()
    frequencies = Counter(words)
    freqvals = set(frequencies.values())
    if freqvals == set([1]):
        valid += 1
    else:
        invalid += 1

print ""
print "Valid:   ",valid
print "Invalid: ",invalid
print "Total:   ",valid+invalid


