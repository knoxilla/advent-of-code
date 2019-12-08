#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = [line.rstrip() for line in f]

origin = (0,0,0)

def next_p(curr, adj):
   x, y, hops = curr[0], curr[1], curr[2]
   step = 1
   dir, val = adj[0], int(adj[1:])
   if dir in "LD":
      val = -val
      step = -1
   if dir in "LR":
      xadj, yadj = val, 0,
      points_traversed =[(i, y, abs(i)+abs(y)) for i in range(x, x+xadj, step)]
   else:
      xadj, yadj = 0, val
      points_traversed =[(x, i, abs(x)+abs(i)) for i in range(y, y+yadj, step)]
   # print(curr, p, dir, val, xadj, yadj)
   new_position = (x + xadj, y + yadj, hops)
#   if xadj < 0:
#      print(points_traversed)
   return(points_traversed, new_position, abs(val))

path1 = data[0].split(",")
path2 = data[1].split(",")

coords1 = []
coords2 = []

curr_p = origin
tally = 0
for p in path1:
    traversed, curr_p, hops = next_p(curr_p, p)
    coords1.extend( traversed )

curr_p = origin
tally = 0
for p in path2:
    traversed, curr_p, hops = next_p(curr_p, p)
    coords2.extend( traversed )

intersect = set(coords1).intersection(set(coords2))
print(len(coords1), len(coords2))

print(list(intersect))

#abspoints = [(abs(i[0]), abs(i[1])) for i in intersect]

#distances = [ sum(x) for x in list(abspoints) ]
#distances.sort()
#print(distances)

hoppies = []
for point in list(intersect):
    hops1 = coords1.index( point )
    #print(hops1)
    hops2 = coords2.index( point )
    #print(hops2)
    hoppies.append( hops1+hops2 )
    #print()

hoppies.sort()

print(hops1)
print(hops2)
print(hoppies)
