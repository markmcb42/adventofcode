
import sys
visited = []

def checklow(x, y, map, maxx, maxy):

  val = map[x][y]
  #print('Check {},{} val {}'.format(x,y,val))

  if x-1 >= 0:
    #if val == 0:
      #print('Test val {} at {},{}'.format(map[x-1][y], x-1,y))
    if map[x-1][y] <= val:
      return False

  if x+1 < maxx:
    #if val == 0:
      #print('Test val {} at {},{}'.format(map[x+1][y], x+1,y))
    if map[x+1][y] <= val:
      return False

  if y-1 >= 0:
    #if val == 0:
      #print('Test val {} at {},{}'.format(map[x][y-1], x,y-1))
    if map[x][y-1] <= val:
      return False

  if y+1 < maxy:
    #if val == 0:
      #print('Test val {} at {},{}'.format(map[x][y+1], x,y+1))
    if map[x][y+1] <= val:
      return False

  return True
  
def get_basin_size(x,y,map, maxx, maxy):

  global visited
  visited.append((x, y))

  size = 1
  xmin = 0
  ymin = 0
  xmax = maxx
  ymax = maxy

  print('Get basin size for {},{}'.format(x,y))

  # Go left 
  if (y-1 >= 0) and (map[x][y-1] != 9):
    point = (x,y-1)
    if point not in visited:
      # visited.append(point)
      print('Check {}'.format(point))
      get_basin_size(x, y-1, map, maxx, maxy)

  # Check right
  if (y+1 < maxy) and (map[x][y+1] != 9):
    point = (x,y+1)
    if point not in visited:
      # visited.append(point)
      print('Check {}'.format(point))
      get_basin_size(x, y+1, map, maxx, maxy)
   
  # Check up
  if (x-1 >= 0) and (map[x-1][y] != 9):
    point = (x-1,y)
    if point not in visited:
      print('Check {}'.format(point))
      get_basin_size(x-1, y, map, maxx, maxy)

  # Check down
  if (x+1 < maxx) and (map[x+1][y] != 9):
    point = (x+1,y)
    if point not in visited:
      print('Check {}'.format(point))
      get_basin_size(x+1, y, map, maxx, maxy)


file = open('input', 'r')

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

print('Height x: {} Col length Y; {}'.format(count, length))

total = 0
check = 0
basins = []

for x in range(count):
  for y in range(length):

    if checklow(x, y, heightmap, count, length):
      check += 1
      visited = []
      get_basin_size(x, y, heightmap, count, length)
      print('Low of {} at ({},{}) size {}'.format(heightmap[x][y], x, y, len(visited)))
      basins.append(len(visited))
      total += heightmap[x][y] + 1

basins.sort(reverse=True)
print(basins)

basin_total = 1
for i in basins[:3]:
  basin_total *= i

print('The total is {} size {}'.format(total, basin_total))
