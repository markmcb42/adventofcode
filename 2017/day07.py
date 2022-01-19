import sys
import numpy as np
from collections import Counter

class Node:
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def getWeight(self):
        total = self.weight
        for node in self.nodes:
            total += node.getWeight()
        return total


file = open('input.txt', 'r')
nodes = {}
towers = {}
for line in file:
    line = line.strip()

    pos = line.find('(')
    name = line[:pos-1]

    weight = int(line[pos+1:line.find(')')])
    nodes[name] = Node(weight, name)

    if '->' not in line:
        continue

    data = line.split('->')
    towers[data[0].split()[0]] = [item.strip() for item in data[1].split(',')]

# We have the list of all the nodes and the towers for them
# add the nodes from each tower to each node
for key, val in towers.items():
    for tower in val:
        nodes[key].addNode(nodes[tower])

root = ''
keys = list(towers.keys())
for key in keys:
    found = False
    for val in list(towers.values()):
        if key in val:
            found = True
            break
    if not found:
        root = key

cur = root
nxt = ''
while True:
  weights = {}
  print(cur)
  for node in nodes[cur].nodes:
    w = node.getWeight()
    print(node.name, w)
    if w not in weights:
        weights[w] = 1
    else:
        weights[w] += 1
  bad_weight = 0
  for w, cnt in weights.items():
      if cnt == 1:
          bad_weight = w
          break

  for node in nodes[cur].nodes:
      if node.getWeight() == bad_weight:
          nxt = node.name
          print(bad_weight, nxt)
          break

  if len(nodes[nxt].nodes) == 0:
      print('finished')
      sys.exit()

  cur = nxt






