
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

def get_level(grid, startx, starty, size):
  total = 0
  for x in range(startx, startx + size):
    for y in range(starty, starty + size):
      total += grid[x][y]
  return total

serial = 1133
#serial = 18
grid = np.zeros((301, 301), dtype=int)

for x in range(1, 301):
  for y in range(1, 301):
    rid = x + 10
    level = ((rid * y) + serial) * rid
    level_str = str(level % 1000)
    if len(level_str) > 2:
      level = int(level_str[0]) - 5
    else:
      level = -5

    grid[x][y] = level

max_level = 0
point = (1,1)
size = 0

for i in range(1, 300):
  for x in range(1, 301 - i):
    for y in range(1, 301 - i):
      cur = get_level(grid, x, y, i)
      if cur > max_level:
        max_level = cur
        point = (x, y)
        size = i

print(max_level, point, size)
