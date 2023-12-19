import math
import sys
import re
from collections import Counter
from enum import Enum
import numpy as np

from functools import cmp_to_key


file = open('input11.txt', 'r')

image = {}
row = 0
cols = []
raw = []
for line in file:
  col = []
  for c in line.strip():
    col.append(c)
  raw.append(col)

image = np.array(raw)

# see which rows are empty
empty_rows = []
for row in range(image.shape[0]):
  empty = True
  for col in range(image.shape[1]):
    if image[row][col] != '.':
      empty = False
      break
  if empty:
    empty_rows.append(row)

# See which cols are empty
empty_cols = []
for col in range(image.shape[1]):
  empty = True
  for row in range(image.shape[0]):
    if image[row][col] != '.':
      empty = False
      break
  if empty:
    empty_cols.append(col)

factor = 1000000 - 1
# Get the address of each galaxy '#'
locations = []
for r in range(image.shape[0]):
  for c in range(image.shape[1]):
    if image[r][c] == '#':
      locations.append((r, c))

total = 0
for i in range(len(locations) - 1):
  for j in range(i+1, len(locations)):
    start_r = min(locations[i][0], locations[j][0])
    end_r = max(locations[i][0], locations[j][0])
    for r in range(start_r, end_r):
      total += 1
      if r in empty_rows:
        total += factor
    start_c = min(locations[i][1], locations[j][1])
    end_c = max(locations[i][1], locations[j][1])
    for c in range(start_c, end_c):
      total += 1
      if c in empty_cols:
        total += factor

print(total)

# Expand rows
ex_row = []
for i in range(image.shape[1]):
  ex_row.append('.')

empty_rows.reverse()
for r in empty_rows:
  row = np.array(ex_row)
  image = np.insert(image, r, row, axis=0)

# Expand columns
num_rows = image.shape[0]
ex_col = []
for i in range(num_rows):
  ex_col.append('.')

empty_cols.reverse()
for c in empty_cols:
  col = np.array(ex_col)
  col = col.reshape((num_rows, 1))
  image = np.insert(image, [c], col, axis=1)

# Get the address of each galaxy '#'
locations = []
for r in range(image.shape[0]):
  for c in range(image.shape[1]):
    if image[r][c] == '#':
      locations.append((r, c))

total = 0
for i in range(len(locations) - 1):
  for j in range(i+1, len(locations)):
    total += abs(locations[i][0] - locations[j][0]) + abs(locations[i][1] - locations[j][1])

print('Part 1: {}'.format(total))




