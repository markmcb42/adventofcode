
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

file = open('input14.txt', 'r')
lines = [line for line in file.read().splitlines()]
##print(lines)
paths = [ [list(map(int, s.split(","))) for s in line.split(" ->")] for line in lines ]
##print(paths)

st = time.time()
max_y = 0
blocks = set()
for path in paths:

  s_x, s_y = path[0]
  for p_x, p_y in path[1:]:
    if p_x == s_x:
      for y in range(min(s_y, p_y), max(s_y, p_y)+1):
        blocks.add((p_x, y))
        max_y = max(max_y, y)
    else:
      for x in range(min(s_x, p_x), max(s_x, p_x)+1):
        blocks.add((x, p_y))
      max_y = max(max_y, p_y)
    s_x, s_y = p_x, p_y


##print(sorted(blocks))
blocks0 = blocks.copy()

max_y += 2
print("max_y =", max_y)

src_x, src_y = (500, 0)

num_units = 0
abyss = False
while not abyss:
  # place a unit
  p_x, p_y = src_x, src_y
  while True:
    # check if in abyss
    down_blocks = any(b_x == p_x and b_y >= p_y for b_x, b_y in blocks)
    if not down_blocks:
      abyss = True
      break
    # move down
    if (p_x, p_y+1) not in blocks:
      p_y += 1; continue
    if (p_x-1, p_y+1) not in blocks:
      p_x -= 1; p_y += 1; continue
    if (p_x+1, p_y+1) not in blocks:
      p_x += 1; p_y += 1; continue
    # here stops
    blocks.add((p_x, p_y))
    num_units += 1
    break
  ##print(p_x, p_y)

blocks = blocks0

num_units = 0
blocked = False
while not blocked:
  # place a unit
  p_x, p_y = src_x, src_y
  while True:
    if p_y+1 < max_y:
      # move down
      if (p_x, p_y+1) not in blocks:
        p_y += 1; continue
      if (p_x-1, p_y+1) not in blocks:
        p_x -= 1; p_y += 1; continue
      if (p_x+1, p_y+1) not in blocks:
        p_x += 1; p_y += 1; continue
    # here stops
    if p_y == src_y:
      blocked = True
      break
    blocks.add((p_x, p_y))
    num_units += 1
    break
  ##print(p_x, p_y)

et = time.time()
print('Exec {}'.format(et - st))
print(num_units)
print(num_units+1)

def go_down(p, grid, max_row):
  cur = p
  bottom = True
  while grid[cur[1]+1][cur[0]] == '.':
    cur[1] += 1
    if cur[1] == max_row:
      return None

  return cur


file = open('input14.txt', 'r')
data = []
max_row = 0
max_col = 0
for line in file:
  items = line.strip().split('->')
  item = []
  for i in items:
    point = [int(x) for x in i.split(',')]
    if point[0] > max_col:
      max_col = point[0]
    if point[1] > max_row:
      max_row = point[1]
    item.append(point)
  data.append(item)

max_row += 2
max_col += 200
print('Max row {} max col {}'.format(max_row, max_col))


orig = np.full((max_row+2, max_col), '.', dtype='U1')


for path in data:
  prev = []

  for p in path:
    if not prev:
      orig[p[1]][p[0]] = '#'
    else:
      if p[0] == prev[0]:
        start = min(prev[1], p[1])
        end = max(prev[1], p[1])
        for i in range(start, end+1):
          orig[i][p[0]] = '#'
      elif p[1] == prev[1]:
        start = min(prev[0], p[0])
        end = max(prev[0], p[0])
        for i in range(start, end+1):
          orig[p[1]][i] = '#'
    prev = p

st = time.time()
for p in [1,2]:
  grid = copy.deepcopy(orig)
  count = 0
  forever = False
  if p == 2:
    for x in range(max_col):
      grid[max_row][x] = '#'

  while not forever:
    cur = [500, 0]
    # Move until blocked
    blocked = False
    while not blocked:
      cur = go_down(cur, grid, max_row)
      if not cur:
        forever = True
        blocked = True
        break

      # Check left
      if grid[cur[1] + 1][cur[0] - 1] == '.':
        cur[1] += 1
        cur[0] -= 1
        continue

      # Check right
      if grid[cur[1] + 1][cur[0] + 1] == '.':
        cur[1] += 1
        cur[0] += 1
        continue

      blocked = True
      grid[cur[1]][cur[0]] = 's'
      count += 1

      if cur == [500, 0]:
        forever = True
        break

  #print('Part {}: {}'.format(p, count))
et = time.time()
print('My Exec {}'.format(et - st))
