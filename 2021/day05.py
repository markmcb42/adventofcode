
import sys

grid = []
for i in range(1000):
  col = []
  for j in range(1000):
    col.append(0)
  grid.append(col)

file = open('input', 'r')

for line in file:
  line = line.strip()

  #print(line)
  data = line.split(' -> ')
  p1 = data[0].split(',')
  p2 = data[1].split(',')

  # Check if this is a row
  if p1[0] == p2[0]:
    #print('row')
    x = int(p1[0])

    y1 = int(p1[1])
    y2 = int(p2[1])
    if y1 < y2:
      starty = y1
      endy = y2
    else:
      starty = y2
      endy = y1
       
    for j in range(starty, endy+1):
      grid[x][j] += 1

    #print('x {} starty {} endy {}'.format(x, starty, endy))
    #for i in range(1000):
    #  print(grid[i])

  # Check if this is a col
  elif p1[1] == p2[1]:
    #print('col')
    y = int(p1[1])

    x1 = int(p1[0])
    x2 = int(p2[0])

    if x1 < x2:
      startx = x1
      endx = x2
    else:
      startx = x2
      endx = x1

    for i in range(startx, endx+1):
      grid[i][y] += 1

    #print('y {} startx {} endx {}'.format(y, startx, endx))
    #for i in range(1000):
    #  print(grid[i])

  # This is a diagonal
  else:
    
    x1 = int(p1[0])
    y1 = int(p1[1])

    x2 = int(p2[0])
    y2 = int(p2[1])

    xlist = []
    ylist = []

    diff = 0
    if x1 < x2:
      diff = x2 - x1
    else:
      diff = x1 - x2

    for i in range(diff):
      if x1 < x2:
        xlist.append(x1+i)
      else: 
        xlist.append(x1-i)

      if y1 < y2:
        ylist.append(y1+i)
      else: 
        ylist.append(y1-i)

    xlist.append(x2)
    ylist.append(y2)

    for x,y in zip(xlist, ylist):
      grid[x][y] += 1
 
count = 0
for i in range(1000):
  for j in range(1000):
    if grid[i][j] > 1:
      count += 1

print('Count is {}'.format(count))
