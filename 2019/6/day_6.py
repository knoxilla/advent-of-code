#!/usr/bin/env python3

from collections import defaultdict
import math
from pprint import pprint as pp
import sys

import matplotlib.pyplot as plt
import networkx as nx
from treelib import Node, Tree

orbit_data = list()
input_file = open(sys.argv[1], "r")
for line in input_file:
    orbit_data = [line.rstrip() for line in input_file]
input_file.close()


lines = list(x.rstrip().split(")") for x in open(sys.argv[1]))
orbits = dict(reversed(x) for x in lines)
cnt = 0
for obj in orbits.keys():
  x = obj
  while x in orbits:
    x = orbits[x]
    cnt += 1
print(cnt)

print(orbits['YOU'])
print(orbits['SAN'])

ulist = []
x = orbits['YOU']
while x in orbits:
  x = orbits[x]
  ulist.append(x)
print(len(ulist))
print(ulist[:3])
print()

slist = []
x = orbits['SAN']
while x in orbits:
  x = orbits[x]
  slist.append(x)
print(len(slist))
print(slist[:3])
print()

common = [x for x in ulist if x in slist]
print(len(common))
print(common[:3])
print()

stally = len(slist) - len(common)
utally = len(ulist) - len(common)
print(utally, stally, stally + utally)

slist.extend(ulist)
print(len(slist))

print(len(set(slist)))

exit(1)

# orbit_data.sort()
# print(len(orbit_data))

# orbit_dict = dict()
# for o in reversed(orbit_data):
#    k,v = o.split(')')
#    orbit_dict[k] = v
# print(orbit_dict['COM'])
# print(len(orbit_dict))

orbits_by_center = defaultdict(list)
# for center in orbit_dict.keys():
for thing in orbit_data:
    k,v = thing.split(')')
    # if k == 'COM':
    #    print(f'hello: {v}')
    orbits_by_center[k].append(v)
# print(orbits_by_center['COM'])
# print(orbits_by_center['QST'])
# pp(orbits_by_center)

g = nx.Graph()
# g.add_node('COM')
# g.add_edge('QST','COM')

# for k,v in orbit_dict.items():
#    g.add_edge(k,v)

# keylist = []
# vallist = []
for o in orbit_data:
   k,v = o.split(')')
   # keylist.append(k)
   # vallist.append(v)
   g.add_edge(v,k)

for o in orbit_data:
   k,v = o.split(')')
   # keylist.append(k)
   # vallist.append(v)
   g.add_edge(v,k)

# print(keylist)
# print(vallist)

# print(len(keylist),len(vallist))
# print(len( set(keylist + vallist) ))

print(f'Nodes: {g.number_of_nodes()}')
print(f'Edges: {g.number_of_edges()}')

print(nx.is_connected(g))
comps = nx.connected_components(g)
c = [ x for x in comps ]
print(len(c))

# print(g.nodes())
# print(g.edges())

exit(1)

nx.draw(g, with_labels=True)
plt.savefig("path.png")

total_orbits =  0
for n in g.nodes():
    try:
        print(n, nx.shortest_path_length(g, n, 'COM'))
        total_orbits += nx.shortest_path_length(g, n, 'COM')
    except:
        print("       ", n)
print(total_orbits)

# print(g.nodes())

# orbit_tree = Tree()
# orbit_tree.create_node("COM", "COM")
# orbit_tree.create_node('one', 'one', parent="COM")
# print(orbit_tree.show())
