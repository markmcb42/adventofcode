import copy
import sys
import time
from collections import Counter
from collections import deque
import hashlib

import numpy as np


max_row = 0
max_col = 0
lines = []
file = open('input22.txt', 'r')
for line in file:
  max_row += 1
  line = line[:len(line) - 1]
  if len(line) > max_col:
    max_col = len(line)
  lines.append(line)

grid = np.zeros((max_row, max_col), dtype='U1')
for row in range(len(lines)):
  line = lines[row]
  for col in range(len(line)):
    grid[row][col] = line[col]

dirs = ['u', 'l', 'd', 'r']
row = 1
col = 1
dir_index = 0
count = 0
for i in range(10000000):
    if grid[row][col] == '#':
        grid[row][col] = 'F'
        if dir_index == 0:
            dir_index = len(dirs) - 1
        else:
            dir_index -= 1
    elif grid[row][col] == '.':
        grid[row][col] = 'W'
        #count += 1
        if dir_index == len(dirs) - 1:
            dir_index = 0
        else:
            dir_index += 1
    elif grid[row][col] == 'W':
        grid[row][col] = '#'
        count += 1
    elif grid[row][col] == 'F':
        grid[row][col] = '.'
        dir_index = (dir_index + 2) % len(dirs)

    if dirs[dir_index] == 'u':
        row -= 1
    elif dirs[dir_index] == 'd':
        row += 1
    elif dirs[dir_index] == 'r':
        col += 1
    elif dirs[dir_index] == 'l':
        col -= 1

    if row < 0 or row == max_row:
        new_row = list(['.'] * max_col)
        max_row += 1
        if row < 0:
            grid = np.append([new_row], grid, axis=0)
            row = 0
        else:
            grid = np.append(grid, [new_row], axis=0)

    if col < 0 or col == max_col:
        new_col = list([['.']] * max_row)
        max_col += 1
        if col < 0:
            grid = np.append(new_col, grid, axis=1)
            col = 0
        else:
            grid = np.append(grid, new_col, axis=1)


print(count)