#!/usr/bin/env python

number = 77
ring = 4
side = 2*ring
start = 7**2 + 1
stop = 9**2 + 1

number = 325489
ring = 284
side = 2*ring
start = 569**2 + 1
stop = 571**2 + 1

min = side/2
max = side - 1
print "Min: ",min
print "Max: ",max

for x in range(start,number+1):
    print x, ring + abs(divmod(x-1,side)[1] - ring)

#print number, ring + abs(divmod(number-1,side)[1] - ring)
