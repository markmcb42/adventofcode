
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

field = []
path = ''
max_col = 0
file = open('input22.txt', 'r')
for line in file:
  if len(line.strip()) == 0:
    continue

  if line[0].isdigit():
    path = line.strip()
    continue

  row = []
  for c in line[:-1]:
    if c == ' ':
      row.append('S')
    else:
      row.append(c)
  field.append(row)
  if len(row) > max_col:
    max_col = len(row)

# append spaces to each row
for r in field:
  while len(r) < max_col:
    r.append('S')

cmds = []
cur = ''
for c in path:
  if c.isdigit():
    cur += c
  else:
    cmds.append(cur)
    cmds.append(c)
    cur = ''
cmds.append(cur)

row = 0
col = 0
dirs = {0:'R', 1:'D', 2:'L', 3:'U'}
for c in field[row]:
  if c == '.':
    break
  col += 1

d = 0
for index in range(len(cmds)):
  c = cmds[index]
  if c == 'R':
    d = (d + 1) % len(dirs)
  elif c == 'L':
    d -= 1
    if d < 0:
      d = len(dirs) - 1
  else:
    steps = int(c)
    if dirs[d] == 'R':
      pos_col = col
      for x in range(steps):
        pos_col = (pos_col + 1) % len(field[row])
        while field[row][pos_col] == 'S':
          pos_col = (pos_col + 1) % len(field[row])
        if field[row][pos_col] == '.':
          col = pos_col
        elif field[row][pos_col] == '#':
          break

    elif dirs[d] == 'D':
      pos_row = row
      for x in range(steps):
        pos_row = (pos_row + 1) % len(field)
        while field[pos_row][col] == 'S':
          pos_row = (pos_row + 1) % len(field)
        if field[pos_row][col] == '.':
          row = pos_row
        elif field[pos_row][col] == '#':
          break

    elif dirs[d] == 'L':
      pos_col = col
      for x in range(steps):
        pos_col -= 1
        if pos_col < 0:
          pos_col = len(field[row]) - 1
        while field[row][pos_col] == 'S':
          pos_col -= 1
          if pos_col < 0:
            pos_col = len(field[row]) - 1
        if field[row][pos_col] == '.':
          col = pos_col
        elif field[row][pos_col] == '#':
          break

    elif dirs[d] == 'U':
      pos_row = row
      for x in range(steps):
        pos_row -= 1
        if pos_row < 0:
          pos_row = len(field) - 1
        while field[pos_row][col] == 'S':
          pos_row -= 1
          if pos_row < 0:
            pos_row = len(field) - 1
        if field[pos_row][col] == '.':
          row = pos_row
        elif field[pos_row][col] == '#':
          break

password = ((row + 1) * 1000) + ((col + 1) * 4) + d
print(password)
















