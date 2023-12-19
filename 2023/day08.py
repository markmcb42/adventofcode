import math
import sys
import re
from collections import Counter
from enum import Enum

from functools import cmp_to_key


file = open('input08.txt', 'r')

nodes = {}
first = True

instructions = file.readline().strip()
for line in file:
  if len(line.strip()) == 0:
    continue

  data = line.strip().split('=')
  dirs = data[1].strip().split(',')
  l_dir = dirs[0][1:]
  r_dir = dirs[1][:-1].strip()
  nodes[data[0].strip()] = (l_dir, r_dir)

cur_node = 'AAA'
steps = 0
found = False
while not found:
  for c in instructions:
    steps += 1
    if c == 'R':
      cur_node = nodes[cur_node][1]
    else:
      cur_node = nodes[cur_node][0]

    if cur_node == 'ZZZ':
      found = True
      break

print('Part 1: {}'.format(steps))

cur_nodes = []
for n in nodes.keys():
  if n.endswith('A'):
    cur_nodes.append(n)

steps = []
for n in cur_nodes:
  found = False
  cur_node = n
  count = 0
  while not found:
    for c in instructions:
      count += 1
      if c == 'R':
        cur_node = nodes[cur_node][1]
      else:
        cur_node = nodes[cur_node][0]

      if cur_node.endswith('Z'):
        found = True
        break

  steps.append(count)

total = math.lcm(*steps)
print('Part 2: {}'.format(total))














