
import sys
import numpy as np
from itertools import permutations
from itertools import combinations
from string import ascii_lowercase as lc
import json

def  checklight(x, y, max, grid):

  cur = grid[x][y]
  #print('\nCheck {},{} which is {}'.format(x,y,cur))
  count = 0
  for i in range(x-1, x + 2):
    for j in range(y-1, y+2): 
      if i == x and j == y:
        #print('{},{} match, skip'.format(i,j))
        continue
      if i < 0 or j < 0:
        #print('{},{} less than 0, skip'.format(i,j))
        continue
      if i >= max or j >= max:
        #print('{},{} more than max, skip'.format(i,j))
        continue
      
      if grid[i][j] == 1:
        count += 1
        #print('{},{} is on count {}'.format(i, j, count))
      #else:
        #print('{},{} is off count {}'.format(i, j, count))

  if cur == 1:
    if count == 2 or count == 3:
      cur = 1   
    else:
      #print('Count is {} switch off'.format(count))
      cur = 0
  else:
    if count == 3:
      #print('Count is {} switch on'.format(count))
      cur = 1

  return cur

row = 100
column = 100
steps = 100

file = open('input', 'r')

grid = []

for line in file:
  line = line.strip()

  col = []
  for c in line:
    if c == '#':
      col.append(1)
    else:
      col.append(0)
  grid.append(col)

grid[0][0] = 1
grid[0][row-1] = 1
grid[row-1][0] = 1
grid[row-1][row-1] = 1

#print('Grid 0')
#for x in range(row):
  #print(grid[x])

for i in range(steps):

  # Create the new grid
  new_grid = []
  for i in range(row):
    col = []
    for j in range(column):
      col.append(0)
    new_grid.append(col)

  new_grid[0][0] = 1
  new_grid[0][row-1] = 1
  new_grid[row-1][0] = 1
  new_grid[row-1][row-1] = 1

  for x in range(row):
    for y in range(column):
      # skip corners
      if (x == 0)  and (y == 0) or (x == 0)  and (y == row-1) or   \
         (x == row-1) and (y == 0) or (x == row-1) and (y == row-1):
        continue

      new_grid[x][y] = checklight(x, y, row, grid) 

  grid = new_grid
  #print('Grid {}'.format(i +1))
  #for x in range(row):
    #print(grid[x])

total = 0
for x in range(row):
  for y in range(column):
    if grid[x][y] == 1:
      total += 1

print('There are {} lights on'.format(total))
