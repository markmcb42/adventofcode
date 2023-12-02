
import sys
visited = []


def checklow(x, y, map, maxx, maxy):

  val = map[x][y]

  if x-1 >= 0:
    if map[x-1][y] <= val:
      return False

  if x+1 < maxx:
    if map[x+1][y] <= val:
      return False

  if y-1 >= 0:
    if map[x][y-1] <= val:
      return False

  if y+1 < maxy:
    if map[x][y+1] <= val:
      return False

  return True


def get_basin_size(x, y, map, maxx, maxy):

  global visited
  visited.append((x, y))

  # Go left
  if (y-1 >= 0) and (map[x][y-1] != 9):
    if (x, y-1) not in visited:
      get_basin_size(x, y-1, map, maxx, maxy)

  # Check right
  if (y+1 < maxy) and (map[x][y+1] != 9):
    if (x, y+1) not in visited:
      get_basin_size(x, y+1, map, maxx, maxy)
   
  # Check up
  if (x-1 >= 0) and (map[x-1][y] != 9):
    if (x-1, y) not in visited:
      get_basin_size(x-1, y, map, maxx, maxy)

  # Check down
  if (x+1 < maxx) and (map[x+1][y] != 9):
    if (x+1, y) not in visited:
      get_basin_size(x+1, y, map, maxx, maxy)


file = open('input09.txt', 'r')

heightmap = []
count = 0
length = 0

for line in file:

  line = line.strip()
  length = len(line)

  col = []
  for c in line:
    col.append(int(c))

  heightmap.append(col)
  count += 1

total = 0
check = 0
basins = []

for x in range(count):
  for y in range(length):

    if checklow(x, y, heightmap, count, length):
      check += 1
      visited = []
      get_basin_size(x, y, heightmap, count, length)
      basins.append(len(visited))
      total += heightmap[x][y] + 1

basins.sort(reverse=True)

basin_total = 1
for i in basins[:3]:
  basin_total *= i

print('Part 1: {} Part 2: {}'.format(total, basin_total))
