
import sys
from parse import *
import copy


file = open('input10.txt', 'r')

cmds = []
for line in file:
  data = line.strip().split()
  if len(data) == 2:
    cmds.append((data[0], int(data[1])))
  else:
    cmds.append((data[0], 0))

cycles = [20, 60, 100, 140, 180, 220]

reg = 1
cycle = 0
signal = 0
count = 0
for c in cmds:
  if c[0] == 'noop':
    cycle += 1
    if cycle in cycles:
      signal += cycle * reg
      count += 1
      if count == 6:
        break

  elif c[0] == 'addx':
    cycle += 1
    if cycle in cycles:
      signal += cycle * reg
      count += 1
      if count == 6:
        break
    cycle += 1
    if cycle in cycles:
      signal += cycle * reg
      count += 1
      if count == 6:
        break
    reg += c[1]

print(signal)

grid = []
reg = 1
sprite = [0, 1, 2]
cycle = 0
row = ''
for c in cmds:
  if c[0] == 'noop':
    cycle += 1
    if cycle == 41:
      grid.append(row)
      row = ''
      cycle = 1

    if (cycle - 1) in sprite:
      row += '#'
    else:
      row += '.'

  elif c[0] == 'addx':
    cycle += 1
    if cycle == 41:
      grid.append(row)
      row = ''
      cycle = 1
    if (cycle - 1) in sprite:
      row += '#'
    else:
      row += '.'

    cycle += 1
    if cycle == 41:
      grid.append(row)
      row = ''
      cycle = 1
    if (cycle - 1) in sprite:
      row += '#'
    else:
      row += '.'

    reg += c[1]
    sprite = [reg - 1, reg, reg + 1]

grid.append(row)
print(grid)





















