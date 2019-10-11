#!/usr/bin/env python

import itertools

file = open('sheet')

# part 2
checksum = 0
for line in file:
    items = map(int, line.split("\t") )
    for dividend,divisor in itertools.product(items, items):
        if dividend == divisor:
            continue
#        if dividend < divisor:
#            dividend,divisor = divisor,dividend
        if dividend % divisor == 0:
            quotient, remainder = divmod(dividend,divisor)
            checksum += quotient
            print dividend, divisor, quotient, remainder, checksum
print ""
print checksum
print ""



exit(0)

# part 1
checksum = 0
for line in file:
    items = map(int, line.split("\t") )
    checksum += max(items) - min(items)
print checksum
print ""


