
import sys
#from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz
import collections
import functools
import numpy as np
import time
import itertools as it

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
    self.epath = []
    self.open = []
    self.info = []
    self.pressure = 0
    self.tot_pressure = 0


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

num_valves = 0
for key, value in nodes.items():
  if value.rate > 0:
    num_valves += 1

start = 'AA'
turns = 30
turns = 1
queue = collections.deque()
states = []

for i in range(turns, 0, -1):
  if not states:
    node = nodes['AA']

    for t in node.tunnels:
      state = State()
      state.path.append('AA')
      state.path.append(t)
      state.info.append(0)
      states.append(state)
  else:
    new_states = []
    if len(states) > 1000:
      states = states[:300]
    for s in states:
      s.info.append(s.pressure)
      s.tot_pressure += s.pressure

      # If we just opened a valve, set node to previous
      v = s.path[-1]
      if 'Open' in v:
        v = s.path[-2]
      #print('Base path {}'.format(s.path))
      node = nodes[v]
      for t in node.tunnels:
        cur = copy.deepcopy(s)
        if cur.path[-2] == t:
          continue

        # Check for loops with no open
        if 'Open' not in cur.path and t in cur.path:
          continue

        cur.path.append(t)
        new_states.append(cur)

      # if the last action was open, continue
      if s.path[-1] == 'Open':
        continue

      # If this node has a rate and not already open, open it
      if node.rate != 0 and v not in s.open:
        cur = copy.deepcopy(s)
        cur.path.append('Open')
        p = node.rate * (i - 1)
        cur.pressure += node.rate
        cur.open.append(v)
        #cur.info.append((v, p))
        new_states.append(cur)

    states = copy.deepcopy(new_states)
    states.sort(key=lambda x: x.tot_pressure, reverse=True)

print(states[0].tot_pressure)

states = []
turns = 26
for i in range(turns, 0, -1):
  if not states:
    node = nodes['AA']
    p_list = it.permutations(node.tunnels, 2)
    for p in p_list:
      state = State()
      state.path.append('AA')
      state.epath.append('AA')
      state.path.append(p[0])
      state.epath.append(p[1])
      states.append(state)
    continue

  new_states = []
  if len(states) > 5000:
    print('Best {} least {} cutoff {}'.format(states[0].tot_pressure,
                                              states[-1].tot_pressure,
                                              states[800].tot_pressure))
    states = states[:900]
  for s in states:
    s.info.append(s.pressure)
    s.tot_pressure += s.pressure
    if len(s.open) == num_valves:
      new_states.append(s)
      continue

    v = s.path[-1]
    if 'Open' in v:
      v = s.path[-2]

    node = nodes[v]
    pos_paths = []
    for t in node.tunnels:
      if s.path[-2] == t:
        continue

      # Check for loops with no open
      if 'Open' not in s.path and t in s.path:
        continue
      pos_paths.append(t)

    # If this node has a rate and not already open, open it
    if node.rate != 0 and v not in s.open:
      pos_paths.append('Open')

    for p in pos_paths:
      v = s.epath[-1]
      if 'Open' in v:
        v = s.epath[-2]
      # print('Base path {}'.format(s.path))
      node = nodes[v]

      for t in node.tunnels:
        if t == p:
          continue
        cur = copy.deepcopy(s)
        if cur.epath[-2] == t:
          continue

        # Check for loops with no open
        if 'Open' not in cur.epath and t in cur.epath:
          continue

        cur.path.append(p)
        if 'Open' in p:
          o_node = nodes[cur.path[-2]]
          cur.pressure += o_node.rate
          cur.open.append(cur.path[-2])
        cur.epath.append(t)
        new_states.append(cur)

      if node.rate != 0 and v not in s.open:
        cur = copy.deepcopy(s)
        cur.epath.append('Open')
        cur.path.append(p)
        if 'Open' in p:
          o_node = nodes[cur.path[-2]]
          cur.pressure += o_node.rate
          cur.open.append(cur.path[-2])
        cur.pressure += node.rate
        cur.open.append(v)
        new_states.append(cur)

  states = copy.deepcopy(new_states)
  states.sort(key=lambda x: x.tot_pressure, reverse=True)

print(states[0].tot_pressure)





