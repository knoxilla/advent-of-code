#!/usr/bin/env python

from math import ceil,floor,sqrt

number = 325489
print "Number: ",number

side = int(floor(sqrt(number)))
side = side - 1 if side % 2 == 0 else side
print "Side: ",side

print "Ring Total: ",side**2

leftover = number - side**2
print "Remainder: ",leftover

nextside = side + 2
print "Max Distance: ", nextside - 1

ring = (side + 2//2) // 2
print ring
print "Distance: ",ring + abs(divmod(number-1,side)[1] - ring)



exit(1)

def odds():
    start = 1
    while True:
        yield start
        start += 2

tot = 0
rings = 0
for x in odds():
    if x**2  > number:
        break
    tot = x**2
    rings = rings + 1
    side = x
    print tot,side,rings

print tot
leftover = number - tot
print leftover

#perimeter = side*4 - 4
#print perimeter
#print perimeter - leftover
