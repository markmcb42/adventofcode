
import sys

import numpy
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

tiles = {}

class Tile:

  def __init__(self, num):
    self.num = num
    self.edges = []
    self.lines = []

  def add_line(self, line):
    self.lines.append(line)

  def generate_edges(self):
    self.edges.append(self.lines[0])
    self.edges.append(self.lines[-1])
    left = ''
    right = ''
    for line in self.lines:
      left += line[0]
      right += line[-1]
    self.edges.append(left)
    self.edges.append(right)

  # See if this edge matches any, including reverse
  def check_edge(self, edge):
    for e in self.edges:
      if e == edge:
        return True
      if e[::-1] == edge:
        return True
    return False


file = open('input20.txt', 'r')

cur_tile = 0
for line in file:
  line = line.strip()
  if len(line) == 0:
    continue

  if 'Tile' in line:
    data = line.split(' ')
    num = int(data[1][:-1])
    t = Tile(num)
    cur_tile = num
    tiles[num] = t
  else:
    tiles[cur_tile].add_line(line)

# Generate edges for each tile
for t in tiles.values():
  t.generate_edges()

corners = {}
borders = {}
for cur_key, cur_val in tiles.items():
  matched = []
  for e in cur_val.edges:
    # See if this edge matches at least one other
    for key, val in tiles.items():
      if key == cur_key:
        continue
      if val.check_edge(e):
        matched.append((e, key))
        break

  # If only 2 matched, this is a corner
  if len(matched) == 2:
    corners[cur_key] = matched
  # If only 3 matched, this is a border
  if len(matched) == 3:
    borders[cur_key] = matched

total = 1
for c in corners.keys():
  total *= c

print('Part 1: {}'.format(total))

# Start with 1st corner and move to right
image_vals = numpy.zeros((12, 12), dtype=int)
cur_row = 0
cur_col = 0

top_right_corner = list(corners.keys())[0]
image_vals[cur_row][cur_col] = top_right_corner
cur_col += 1
cur_val = corners[top_right_corner][0][1]
image_vals[cur_row][cur_col] = cur_val
cur_col += 1
found_corner = False
prev_val = top_right_corner
while not found_corner:

  # Find the next border
  for i in borders[cur_val]:
    if i[1] == prev_val:
      continue

    if i[1] in corners:
      image_vals[cur_row][cur_col] = i[1]
      found_corner = True
      break
    if i[1] in borders:
      image_vals[cur_row][cur_col] = i[1]
      prev_val = cur_val
      cur_val = i[1]
      break
  cur_col += 1


print(next_val)

















