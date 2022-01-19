import sys

import numpy
import numpy as np

file = open('input', 'r')

base = []
row_count = 0
col_count = 0
for line in file:

    line = line.strip()
    row_count = len(line)
    row = []
    for c in line:
        row.append(int(c))
    base.append(row)
    col_count += 1

#grid = base
max_val = row_count


# Create the first row
maps = {0: base}


for i in range(1,5):
  next = []
  for x in range(row_count):
    row = []
    for y in range(row_count):
      val = base[x][y] + 1
      if val == 10:
        val = 1
      row.append(val)

    next.append(row)
  maps[i] = next
  base = next
  max_val += row_count

print('max_val is now {}'.format(max_val))

base = []

for i in range(row_count):
  row = []
  for key, val in maps.items():
    for y in range(row_count):
      row.append(val[i][y])
  base.append(row)

print('Len of row is {}'.format(len(base[0])))

# Create the rest of the rows
maps = {0: base}
for i in range(1, 5):
  next = []
  for x in range(row_count):
    row = []
    for y in range(max_val):
      val = base[x][y] + 1
      if val == 10:
        val = 1
      row.append(val)

    next.append(row)
  maps[i] = next
  base = next

# build final grid
grid = []
for key, val in maps.items():
  for i in range(row_count):
    row = []
    for y in range(max_val):
      row.append(val[i][y])
    grid.append(row)

print('There are {} col {} row'.format(len(grid), len(grid[0])))

distmap = np.ones((max_val, max_val), dtype=int) * np.Infinity
distmap[0, 0] = 0

originmap = np.ones((max_val, max_val), dtype=int) * numpy.nan
visited = np.zeros((max_val, max_val), dtype=bool)

finished = False
x, y = int(0), int(0)
count = 0

while not finished:
    # Check down
    if x < max_val - 1:
        if distmap[x + 1, y] > grid[x + 1][y] + distmap[x, y] and not visited[x + 1, y]:
            distmap[x + 1, y] = grid[x + 1][y] + distmap[x, y]
            originmap[x + 1, y] = np.ravel_multi_index([x, y], (max_val, max_val))

    # Check up
    if x > 0:
        if distmap[x - 1, y] > grid[x - 1][y] + distmap[x, y] and not visited[x - 1, y]:
            distmap[x - 1, y] = grid[x - 1][y] + distmap[x, y]
            originmap[x - 1, y] = np.ravel_multi_index([x, y], (max_val, max_val))

    # Check right
    if y < max_val - 1:
        if distmap[x, y+1] > grid[x][y+1] + distmap[x, y] and not visited[x, y+1]:
            distmap[x, y+1] = grid[x][y+1] + distmap[x, y]
            originmap[x, y+1] = np.ravel_multi_index([x, y], (max_val, max_val))

    # Check Left
    if y > 0:
        if distmap[x, y-1] > grid[x][y-1] + distmap[x, y] and not visited[x, y-1]:
            distmap[x, y-1] = grid[x][y-1] + distmap[x, y]
            originmap[x, y-1] = np.ravel_multi_index([x, y], (max_val, max_val))

    visited[x,y] = True
    tmp = distmap
    tmp[np.where(visited)] = np.Infinity

    minpost = np.unravel_index(np.argmin(tmp),np.shape(tmp))
    x,y = minpost[0],minpost[1]
    if x == max_val-1 and y == max_val-1:
      finished = True
    count += 1


print('The path length is: '+np.str(distmap[max_val-1,max_val-1]))
print('Len is {} diff {}'.format(total_len, most - least))
