
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

max_row = 0
max_col = 0

def occupied2(grid, row, col):
  count = 0

  # Check north
  cur_row = row - 1
  while cur_row >= 0:
    if grid[cur_row][col] == '.':
      cur_row -= 1
      continue
    if grid[cur_row][col] == '#':
      count += 1
    break

  # Check south
  cur_row = row + 1
  while cur_row < max_row:
    if grid[cur_row][col] == '.':
      cur_row += 1
      continue
    if grid[cur_row][col] == '#':
      count += 1
    break

  # Check east
  cur_col = col + 1
  while cur_col < max_col:
    if grid[row][cur_col] == '.':
      cur_col += 1
      continue
    if grid[row][cur_col] == '#':
      count += 1
    break

  # Check west
  cur_col = col - 1
  while cur_col >= 0:
    if grid[row][cur_col] == '.':
      cur_col -= 1
      continue
    if grid[row][cur_col] == '#':
      count += 1
    break

  # Check NE
  cur_row = row - 1
  cur_col = col + 1
  while cur_row >= 0 and cur_col < max_col:
    if grid[cur_row][cur_col] == '.':
      cur_row -= 1
      cur_col += 1
      continue
    if grid[cur_row][cur_col] == '#':
      count += 1
    break

  # Check NW
  cur_row = row - 1
  cur_col = col - 1
  while cur_row >= 0 and cur_col >= 0:
    if grid[cur_row][cur_col] == '.':
      cur_row -= 1
      cur_col -= 1
      continue
    if grid[cur_row][cur_col] == '#':
      count += 1
    break

  # Check SW
  cur_row = row + 1
  cur_col = col - 1
  while cur_row < max_row and cur_col >= 0:
    if grid[cur_row][cur_col] == '.':
      cur_row += 1
      cur_col -= 1
      continue
    if grid[cur_row][cur_col] == '#':
      count += 1
    break

  # Check SE
  cur_row = row + 1
  cur_col = col + 1
  while cur_row < max_row and cur_col < max_col:
    if grid[cur_row][cur_col] == '.':
      cur_row += 1
      cur_col += 1
      continue
    if grid[cur_row][cur_col] == '#':
      count += 1
    break

  return count


def occupied(grid, row, col):
  rows = [row]
  if row - 1 >= 0:
    rows.append(row-1)
  if row + 1 < max_row:
    rows.append(row + 1)
  cols = [col]
  if col - 1 >= 0:
    cols.append(col - 1)
  if col + 1 < max_col:
    cols.append(col + 1)

  count = 0
  for cur_row in rows:
    for cur_col in cols:
      if cur_row == row and cur_col == col:
        continue
      if grid[cur_row][cur_col] == '#':
        count += 1

  return count


lines = []
file = open('input11.txt', 'r')
for line in file:
  max_row += 1
  line = line.strip()
  if len(line) > max_col:
    max_col = len(line)
  lines.append(line)

orig = np.zeros((max_row, max_col), dtype='U1')
for row in range(len(lines)):
  line = lines[row]
  for col in range(len(line)):
    orig[row][col] = line[col]

grid = np.copy(orig)
while True:
  changed = False
  new_grid = np.zeros((max_row, max_col), dtype='U1')
  for row in range(max_row):
    for col in range(max_col):
      char = grid[row][col]
      if char == '.':
        new_grid[row][col] = char
      elif char == 'L':
        count = occupied(grid, row, col)
        if count == 0:
          new_grid[row][col] = '#'
          changed = True
        else:
          new_grid[row][col] = char
      elif char == '#':
        count = occupied(grid, row, col)
        if count > 3:
          new_grid[row][col] = 'L'
          changed = True
        else:
          new_grid[row][col] = char

  grid = np.copy(new_grid)
  if not changed:
    break

count = 0
for row in range(max_row):
  for col in range(max_col):
    if grid[row][col] == '#':
      count += 1

print(count)

grid = np.copy(orig)
while True:
  changed = False
  new_grid = np.zeros((max_row, max_col), dtype='U1')
  for row in range(max_row):
    for col in range(max_col):
      char = grid[row][col]
      if char == '.':
        new_grid[row][col] = char
      elif char == 'L':
        count = occupied2(grid, row, col)
        if count == 0:
          new_grid[row][col] = '#'
          changed = True
        else:
          new_grid[row][col] = char
      elif char == '#':
        count = occupied2(grid, row, col)
        if count > 4:
          new_grid[row][col] = 'L'
          changed = True
        else:
          new_grid[row][col] = char

  grid = np.copy(new_grid)
  if not changed:
    break

count = 0
for row in range(max_row):
  for col in range(max_col):
    if grid[row][col] == '#':
      count += 1

print(count)