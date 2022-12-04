
import copy

grid_p1 = []
grid_p2 = []
for i in range(1000):
  col = []
  for j in range(1000):
    col.append(0)
  grid_p1.append(col)
  grid_p2.append(copy.deepcopy(col))

file = open('input05.txt', 'r')

for line in file:
  data = line.strip().split(' -> ')
  p1 = [int(x) for x in data[0].split(',')]
  p2 = [int(x) for x in data[1].split(',')]

  # Check if this is a row
  if p1[0] == p2[0]:
    x = p1[0]
    starty = min(p1[1], p2[1])
    endy = max(p1[1], p2[1])

    for j in range(starty, endy+1):
      grid_p1[x][j] += 1
      grid_p2[x][j] += 1

  # Check if this is a col
  elif p1[1] == p2[1]:
    y = p1[1]
    startx = min(p1[0], p2[0])
    endx = max(p1[0], p2[0])

    for i in range(startx, endx+1):
      grid_p1[i][y] += 1
      grid_p2[i][y] += 1

  # This is a diagonal
  else:
    xlist = []
    ylist = []

    diff = abs(p1[0] - p2[0])

    for i in range(diff):
      if p1[0] < p2[0]:
        xlist.append(p1[0]+i)
      else: 
        xlist.append(p1[0]-i)

      if p1[1] < p2[1]:
        ylist.append(p1[1]+i)
      else: 
        ylist.append(p1[1]-i)

    xlist.append(p2[0])
    ylist.append(p2[1])

    for x,y in zip(xlist, ylist):
      grid_p2[x][y] += 1
 
p1_count = 0
p2_count = 0
for i in range(1000):
  for j in range(1000):
    if grid_p1[i][j] > 1:
      p1_count += 1
    if grid_p2[i][j] > 1:
      p2_count += 1

print('Part 1: {} Part 2: {}'.format(p1_count, p2_count))
