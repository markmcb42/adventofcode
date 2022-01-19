
import sys

file = open('input', 'r')

total = 0
rows, cols = (1000,1000)
lights=[]

for i in range(rows):
  col = []
  for j in range(cols):
    col.append(0)
  lights.append(col)

for line in file:

  toggle = False
  switch = False
  startx = 0
  starty = 0
  endx = 0
  endy = 0

  data = line.split(' ')

  # toggle does not have switch
  if 'toggle' in data[0]:
    print('Toggle is true')
    toggle = True
    first = data[1].split(',')
    startx = int(first[0])
    starty = int(first[1])

    second = data[3].split(',')
    endx = int(second[0]) + 1
    endy = int(second[1]) + 1

    print('First is ({},{}) second is ({},{})'.format(startx, starty, endx, endy))
  else:
    # This is a turn, get the switch
    if 'on' in data[1]:
      print('Turn on')
      switch = True

    first = data[2].split(',')
    startx = int(first[0])
    starty = int(first[1])

    second = data[4].split(',')
    endx = int(second[0]) + 1
    endy = int(second[1]) + 1

    print('First is ({},{}) second is ({},{})'.format(startx, starty, endx, endy))
  # If this a toggle, flip the light
  if toggle:
    for i in range(startx, endx):
      for j in range(starty, endy):
        lights[i][j] += 2 
  elif switch:
    print('Turning lights {}'.format(switch))
    for i in range(startx, endx):
      for j in range(starty, endy):
        lights[i][j] += 1
  else:
    for i in range(startx, endx):
      for j in range(starty, endy):
        if lights[i][j] > 0:
          lights[i][j] -= 1
    
count = 0  
for i in range(rows):
  for j in range(cols):
    count += lights[i][j]

print('There are {} lights lit'.format(count))
