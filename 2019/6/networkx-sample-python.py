from collections import defaultdict
import math
from pprint import pprint as pp
import sys

import matplotlib.pyplot as plt
import networkx as nx

orbit_data = list()
input_file = open('input_6', 'r')
for line in input_file:
    orbit_data = [line.rstrip() for line in input_file]

# input_file.close()

g = nx.Graph()
g.add_node('COM')
# g.add_edge('B','COM')
g.add_edge('QST','COM')

# for k,v in orbit_dict.items():
#    g.add_edge(k,v)

keylist = []
vallist = []
for o in orbit_data:
   k,v = o.split(')')
   keylist.append(k)
   vallist.append(v)
   g.add_edge(v,k)

print(f'Nodes: {g.number_of_nodes()}')
print(f'Edges: {g.number_of_edges()}')