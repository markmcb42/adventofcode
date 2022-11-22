
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

def get_state(cur_grid):
  ret_str = ''
  for r in cur_grid:
    for i in r:
      ret_str += i

  return ret_str

grid = []
num_rows = 0
num_cols = 0

file = open('input24.txt', 'r')
for line in file:
  line = line.strip()
  num_rows += 1
  row = []
  cols = 0
  for c in line:
    cols += 1
    row.append(c)
  grid.append(row)
  if cols > num_cols:
    num_cols = cols

states = []
state = get_state(grid)
states.append(state)

new_grid = copy.deepcopy(grid)

while True:
  for row in range(num_rows):
    cur_row = grid[row]
    for col in range(num_cols):
      cur_val = grid[row][col]
      count = 0
      # Check col
      if col == 0:
        if grid[row][col+1] == '#':
          count += 1
      elif col == num_cols-1:
        if grid[row][col-1] == '#':
          count += 1
      else:
        if grid[row][col+1] == '#':
          count += 1
        if grid[row][col-1] == '#':
          count += 1

      # Check row
      if row == 0:
        if grid[row+1][col] == '#':
          count += 1
      elif row == num_rows - 1:
        if grid[row-1][col] == '#':
          count += 1
      else:
        if grid[row+1][col] == '#':
          count += 1
        if grid[row-1][col] == '#':
          count += 1

      new_grid[row][col] = grid[row][col]
      if grid[row][col] == '#' and count != 1:
        new_grid[row][col] = '.'
      if grid[row][col] == '.' and (count == 1 or count == 2):
        new_grid[row][col] = '#'

  cur_state = get_state(new_grid)
  if cur_state in states:
    print('found')
    total = 0
    for i in range(len(cur_state)):
      if cur_state[i] == '#':
        total += 2 ** i
    print(total)
    break
  else:
    states.append(cur_state)
    grid = copy.deepcopy(new_grid)











