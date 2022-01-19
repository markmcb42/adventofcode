
import sys
import numpy as np

claims = []
file = open('input.txt', 'r')
for line in file:
  data = line.strip().split()
  id = int(data[0][1:])
  pos = data[2].split(',')
  col = int(pos[0])
  row = int(pos[1][:len(pos[1]) - 1])
  dim = data[3].split('x')
  width = int(dim[0])
  height = int(dim[1])
  claims.append((id, col, row, width, height))

max_row = 1010
max_col = 1010

grid = np.zeros((max_row, max_col), dtype=int)
for claim in claims:
  for row in range(claim[2], claim[2] + claim[4]):
    for col in range(claim[1], claim[1] + claim[3]):
      grid[row][col] += 1

count = 0
for row in range(max_col):
  for col in range(max_row):
    if grid[row][col] > 1:
      count += 1

print(count)

claim = 0
for c in claims:
  intact = True
  for row in range(c[2], c[2] + c[4]):
    for col in range(c[1], c[1] + c[3]):
      if grid[row][col] != 1:
        intact = False
  if intact:
    print(c[0])




