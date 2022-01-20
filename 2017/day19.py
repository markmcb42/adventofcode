import sys
import time
from collections import Counter
from collections import deque
import hashlib

import numpy as np


max_row = 0
max_col = 0
lines = []
file = open('input19.txt', 'r')
for line in file:
  max_row += 1
  line = line[:len(line) - 1]
  if len(line) > max_col:
    max_col = len(line)
  lines.append(line)

grid = np.zeros((max_row + 1, max_col + 1), dtype='U1')
for row in range(len(lines)):
  line = lines[row]
  for col in range(len(line)):
    grid[row][col] = line[col]

start = (0,0)
for col in range(max_col):
  if grid[0][col] == '|':
    start = (0, col)
    break

cur_row = start[0]
cur_col = start[1]
dir = 'd'
path = ''
steps = 0
while True:
  c = grid[cur_row][cur_col]

  if c == ' ' or c == '':
    print(path)
    break

  steps += 1
  if c == '+':
    if dir == 'd' or dir == 'u':
      if grid[cur_row][cur_col-1] == '-' or grid[cur_row][cur_col-1].isalpha():
        dir = 'l'
        cur_col -= 1
      elif grid[cur_row][cur_col+1] == '-' or grid[cur_row][cur_col+1].isalpha():
        dir = 'r'
        cur_col += 1
      else:
        print(path)
        break
    else:
      if grid[cur_row+1][cur_col] == '|' or grid[cur_row+1][cur_col].isalpha():
        dir = 'd'
        cur_row += 1
      elif grid[cur_row-1][cur_col] == '|' or grid[cur_row-1][cur_col].isalpha():
        dir = 'u'
        cur_row -= 1
      else:
        print(path)
        break
  else:
    if dir == 'd':
      cur_row += 1
    elif dir == 'u':
      cur_row -= 1
    elif dir == 'l':
      cur_col -= 1
    elif dir == 'r':
      cur_col += 1
    if c.isalpha():
      path += c

print(steps)