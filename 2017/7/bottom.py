#!/usr/bin/env python

file = open('towerdata')

class Program:
    name = ""
    weight = 0
    stackers = []

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

parents = set()
children = set()
leaves = set()
progs = []
weights = {}

for line in file:
    line = line.strip().replace('-','')
    line = line.strip().replace(',','')
    line = line.strip().replace('(','')
    line = line.strip().replace(')','')
    items = line.split(" ")

    prog = Program( items[0], items[1] )
    weights[items[0]] = [int(items[1]),[]]

    if len(items) > 2:
        parents.add(items[0])
        for item in items[3:]:
            children.add(item)
            weights[items[0]][1].append(item)
    else:
        leaves.add(items[0])

    progs.append(prog)

print "Parents:    ",len(parents)
print "Children:   ",len(children)
print "Leaves:     ",len(leaves)

bottom = parents - children
print "Parentless: ",len(bottom)

if len(bottom) == 1:
    base = next(iter(bottom))
    print "Bottom:     ",base

print ""

stackers = children - leaves
print "Stackers:  ",len(stackers)

print ""

print len(progs)
#for p in progs:
#    print p.name,p.weight,p.stackers,len(p.stackers)

print len(weights)
#for k,v in weights.iteritems():
#    print k,v

#file.seek(0)
#for line in file:
#    print line

subtowersums = []
for key,value in weights.iteritems():
    heft = 0
    if len(value[1]) > 0:
        for v in value[1]:
            heft += weights[v][0]
        subtowersums.append(heft)

print len(subtowersums)
#for st in subtowersums:
#    print st
