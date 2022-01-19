
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

wires = []
file = open('input.txt', 'r')
for line in file:
  x, y = 0, 0
  wire = []
  data = line.strip().split(',')
  for d in data:
    if d[0] == 'R':
      val = int(d[1:])
      for i in range(val):
        x += 1
        wire.append((x, y))
    elif d[0] == 'D':
      val = int(d[1:])
      for i in range(val):
        y -= 1
        wire.append((x, y))
    elif d[0] == 'U':
      val = int(d[1:])
      for i in range(val):
        y += 1
        wire.append((x, y))
    elif d[0] == 'L':
      val = int(d[1:])
      for i in range(val):
        x -= 1
        wire.append((x, y))
  wires.append(wire)

intersections = []
for i in range(len(wires[0])):
  pos = wires[0][i]
  if pos in wires[1]:
    intersections.append(pos)

closest = 1000000
steps = 1000000
for i in intersections:
  dist = abs(i[0]) + abs(i[1])
  if dist < closest:
    closest = dist
  # Walk the number of steps for each wire
  tot_steps = wires[0].index(i) + wires[1].index(i) + 2
  if tot_steps < steps:
    steps = tot_steps


print(closest, steps)


