
import sys
from parse import *
import copy


file = open('input09.txt', 'r')

cmds = []
for line in file:
  data = line.strip().split()
  cmds.append((data[0], int(data[1])))

pos = set()
pos.add((0, 0))

hx, hy = 0, 0
tx, ty = 0, 0

for c in cmds:
  for i in range(c[1]):
    if c[0] == 'D':
      hy -= 1
    elif c[0] == 'U':
      hy += 1
    elif c[0] == 'R':
      hx += 1
    elif c[0] == 'L':
      hx -= 1

    if (abs(hx - tx)) <= 1 and (abs(hy - ty) <= 1):
      continue

    # check if diagonal move needed
    if hx != tx and hy != ty:
      if hx > tx:
        tx += 1
      else:
        tx -= 1
      if hy > ty:
        ty += 1
      else:
        ty -= 1
    elif hx == tx:
      if hy > ty:
        ty += 1
      else:
        ty -= 1
    else:
      if hx > tx:
        tx += 1
      else:
        tx -= 1
    pos.add((tx, ty))

print('Part 1: {}'.format(len(pos)))


knots = {}
for i in range(10):
  knots[i] = (0, 0)
pos = set()
pos.add((0, 0))

for c in cmds:
  for i in range(c[1]):
    # Move the first knot
    cur = knots[0]
    if c[0] == 'D':
      knots[0] = (cur[0], cur[1] - 1)
    elif c[0] == 'U':
      knots[0] = (cur[0], cur[1] + 1)
    elif c[0] == 'R':
      knots[0] = (cur[0] + 1, cur[1])
    elif c[0] == 'L':
      knots[0] = (cur[0] - 1, cur[1])

    for key in range(1, len(knots)):

      # If the distance between this knot and prev is
      # less than one, break since no other knots will move
      prev = knots[key - 1]
      cur = knots[key]
      if (abs(cur[0] - prev[0])) <= 1 and (abs(cur[1] - prev[1]) <= 1):
        break

      # See how the previous knot should move
      # check if diagonal move needed
      if cur[0] != prev[0] and cur[1] != prev[1]:
        cx = cur[0]
        cy = cur[1]
        if prev[0] > cur[0]:
          cx += 1
        else:
          cx -= 1
        if prev[1] > cur[1]:
          cy += 1
        else:
          cy -= 1
        knots[key] = (cx, cy)
      elif prev[0] == cur[0]:
        if prev[1] > cur[1]:
          knots[key] = (cur[0], cur[1] + 1)
        else:
          knots[key] = (cur[0], cur[1] - 1)
      else:
        if prev[0] > cur[0]:
          knots[key] = (cur[0] + 1, cur[1])
        else:
          knots[key] = (cur[0] - 1, cur[1])

      if key == len(knots) - 1:
        pos.add(knots[key])

print('Part 2: {}'.format(len(pos)))


























