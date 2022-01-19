import sys

def getadj(point, max_val):
  points = []
  x = point[0]
  y = point[1]
  if x-1 >= 0:
    points.append((x-1,y))
    if y+1 < max_val:
      points.append((x-1,y+1))
    if y-1 >=0:
      points.append((x-1,y-1))
  if x + 1 < max_val:
    points.append((x+1,y))
    if y+1 < max_val:
      points.append((x+1,y+1))
    if y-1 >=0:
      points.append((x+1,y-1))
  if y-1 >=0:
    points.append((x,y-1))
  if y+1 < max_val:
    points.append((x, y+1))

  return points


def runflash(grid, points, flashpoints, max_val):

  cur = set()
  for point in points:
    affected = getadj(point, max_val)
    for a in affected:
      x,y = a[0],a[1]
      grid[x][y] += 1
      if grid[x][y] >= 10:
        if (x,y) not in flashpoints:
          cur.add((x,y))

  return list(cur)


grid = []
file = open('input', 'r')

max_val = 0
for line in file:
  line = line.strip()
  max_val = len(line)
  row = []
  for c in line:
    row.append(int(c))
  grid.append(row)

count = 0
index = 0
while True:
#for i in range(100):
  flashpoints = []
  for x in range(max_val):
    for y in range(max_val):
      grid[x][y] += 1
      if grid[x][y] >= 10:
        flashpoints.append((x,y))

  cur = flashpoints
  while len(cur) > 0:
    cur = runflash(grid, cur, flashpoints,  max_val)
    flashpoints.extend(cur)

  index += 1
  count += len(flashpoints)
  sync = True
  for x in range(max_val):
    for y in range(max_val):
      if grid[x][y] >= 10:
        grid[x][y] = 0
      else:
        sync = False

  if sync:
    print("Sync at {}".format(index))
    break

print('There were {} flashes'.format(count))

