
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc


def get_dist(points, row, col):
  chars = []
  total = 0
  min_dist = 100000
  for p in points:
    dist = abs(p[1][0] - row) + abs(p[1][1] - col)
    total += dist
    if dist < min_dist:
      min_dist = dist
      chars = [p[0]]
    elif dist == min_dist:
      chars.append(p[0])
  return chars, total


points = []
loc = []
max_row = 0
min_row = 10000
max_col = 0
min_col = 10000

num = 0
file = open('input.txt', 'r')
for line in file:
  data = line.strip().split(',')
  col = int(data[0])
  row = int(data[1])
  if col > max_col:
    max_col = col
  if col < min_col:
    min_col = col
  if row > max_row:
    max_row = row
  if row < min_row:
    min_row = row
  points.append((str(num), (row, col)))
  loc.append(str(num))
  num += 1

grid = np.zeros((max_row + 1, max_col + 1), dtype='U2')
for p in points:
  grid[p[1][0]][p[1][1]] = p[0]

region = 0
for row in range(max_row + 1):
  for col in range(max_col + 1):
    chars, dist = get_dist(points, row, col)
    if dist < 10000:
      region += 1

    if len(chars) > 1:
      grid[row][col] = '.'
    else:
      grid[row][col] = chars[0]

# Remove infinite areas
for col in range(max_col + 1):
  if grid[0][col] in loc:
    loc.remove(grid[0][col])
  if grid[max_row][col] in loc:
    loc.remove(grid[max_row][col])
for row in range(max_row + 1):
  if grid[row][0] in loc:
    loc.remove(grid[row][0])
  if grid[row][max_col] in loc:
    loc.remove(grid[row][max_col])

counts = {}
for l in loc:
  counts[l] = 0

for row in range(max_row + 1):
  for col in range(max_col + 1):
    if grid[row][col] in counts:
      counts[grid[row][col]] += 1

size = 0
for key, value in counts.items():
  if value > size:
    size = value

print(size, region)









