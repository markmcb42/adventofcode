
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

cubes = {}

def get_active(cur_cube):
  count = 0
  chk_count = 0
  for x in range(cur_cube[0] - 1, cur_cube[0] + 2):
    for y in range(cur_cube[1] - 1, cur_cube[1] + 2):
      for z in range(cur_cube[2] - 1, cur_cube[2] + 2):
        for w in range(cur_cube[3] -1, cur_cube[3] + 2):
          cur = (x, y, z, w)
          if cur == cur_cube:
            continue
          chk_count += 1

          if cur in cubes:
            if cubes[cur][0] == 1:
              count += 1
  return count



file = open('input17.txt', 'r')
minz = -1
maxz = 1
miny = -1
maxy = 1
minx = -1
maxx = 1
minw = -1
maxw = 1

cury = 0
for line in file:
  curx = 0
  line = line.strip()
  for c in line:
    cur = (cury, curx, 0, 0)
    if c == '#':
      cubes[cur] = (1, 0)
    else:
      cubes[cur] = (0, 0)
    curx += 1
  cury += 1

maxx = curx
maxy = cury

for c in range(6):
  for x in range(minx, maxx + 1):
    for y in range(miny, maxy + 1):
      for z in range(minz, maxz + 1):
        for w in range(minw, maxw + 1):
          cur = (x, y, z, w)
          active = get_active(cur)

          if cur not in cubes:
            if active == 3:
              cubes[cur] = (0, 1)
          elif cubes[cur][0] == 0 and active == 3:
            cubes[cur] = (0, 1)
          elif cubes[cur][0] == 1 and (active != 2 and active != 3):
            cubes[cur] = (1, 1)

  for key, val in cubes.items():
    if val[1] == 1:
      if val[0] == 0:
        cubes[key] = (1, 0)
      else:
        cubes[key] = (0, 0)

  total = 0
  for c in cubes.values():
    if c[0] == 1:
      total += 1

  print(total)
  minx -= 1
  miny -= 1
  minz -= 1
  maxx += 1
  maxy += 1
  maxz += 1
  minw -= 1
  maxw += 1








