
import sys
from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz
import collections
import functools
import numpy as np
import time

class Node:
  def __init__(self, name, rate):
    self.name = name
    self.rate = rate
    self.tunnels = []

    self.valve_on = False
    self.tot_pressure = 0

class State:
  def __init__(self):
    self.path = []
    self.open = []
    self.pressure = 0


file = open('input16.txt', 'r')
nodes = {}

for line in file:
  data = line.strip().split(';')
  rate = int(data[0].split("=")[1])
  valve = data[0].split()[1]
  node = Node(valve, rate)

  tunnels = []
  if 'valves' in data[1]:
    elems = data[1].split(',')
    tunnels.append(elems[0].split()[4])
    for i in range(1, len(elems)):
      tunnels.append(elems[i].strip())
  else:
    tunnels.append(data[1].split()[4])

  for t in tunnels:
    node.tunnels.append(t)

  nodes[valve] = node

start = 'AA'
turns = 30
queue = collections.deque()
states = []

for i in range(turns, 0, -1):
  if not states:
    node = nodes['AA']

    for t in node.tunnels:
      state = State()
      state.path.append('AA')
      state.path.append(t)
      states.append(state)
  else:
    new_states = []
    for s in states:

      # If we just opened a valve, set node to previous
      v = s.path[-1]
      if v == 'Open':
        v = s.path[-2]

      node = nodes[v]
      for t in node.tunnels:
        cur = copy.deepcopy(s)
        if cur.path[-2] == t:
          continue
        cur.path.append(t)
        new_states.append(cur)

      # If this node has a rate and not already open, open it
      if node.rate != 0 and v not in s.open:
        cur = copy.deepcopy(s)
        cur.path.append('Open')
        cur.pressure += node.rate * i
        new_states.append(cur)

    states = copy.deepcopy(new_states)







