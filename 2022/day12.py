
import sys
from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz
import collections


def bfs(grid, start, end):
  height = len(grid)
  width = len(grid[0])

  queue = collections.deque([[start]])
  seen = {start}
  while queue:
    path = queue.popleft()
    row, col = path[-1]
    if (row, col) == end:
      return path

    cur = grid[row][col]
    if cur == 'S':
      cur = 'a'

    for row2, col2 in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
      if 0 <= row2 < height and 0 <= col2 < width:
        target = grid[row2][col2]
        if target == 'E':
          target = 'z'
        if (ord(target) <= ord(cur) + 1) and ((row2,col2) not in seen):
          queue.append(path + [(row2, col2)])
          seen.add((row2, col2))


grid = []
file = open('input12.txt', 'r')
cur = 0
for line in file:
  row = line.strip()
  grid.append(row)

start = ()
end = ()
for r in range(len(grid)):
  for c in range(len(grid[r])):
    if grid[r][c] == 'S':
      start = (r, c)
    if grid[r][c] == 'E':
      end = (r, c)

start_path = bfs(grid, start, end)
print(len(start_path) - 1)

paths = []
starts = []
for r in range(len(grid)):
  for c in range(len(grid[r])):
    if grid[r][c] == 'a':
      starts.append((r, c))

for s in starts:
  p = bfs(grid, s, end)
  paths.append(p)

least = sys.maxsize
for p in paths:
  if not p:
    continue

  if len(p) < least:
    least = len(p)

print(least - 1)

