
import sys

file = open('input', 'r')
dirs = []
for line in file:
  data = line.strip().split(',')
  for d in data:
    dirs.append(d.strip())

start = (0,0)
cur_x = 0
cur_y = 0
points = [start]
seen = False
facing = 'N'
for dir in dirs:
  if seen:
    break

  if 'R' == dir[0]:
    if facing == 'N':
      facing = 'E'
    elif facing == 'E':
      facing = 'S'
    elif facing == 'S':
      facing = 'W'
    elif facing == 'W':
      facing = 'N'
  elif 'L' == dir[0]:
    if facing == 'N':
      facing = 'W'
    elif facing == 'W':
      facing = 'S'
    elif facing == 'S':
      facing = 'E'
    elif facing == 'E':
      facing = 'N'

  length = int(dir[1:])

  for i in range(0, length):
    if facing == 'E':
      cur_x += 1
    elif facing = 'S':
      cur_y -= 1

      point = (cur_x, cur_y)
      if point in points:
        seen = True
        break
      points.append(point)
  elif facing == 'S':
    for i in range(0, length):
      cur_y -= 1
      point = (cur_x, cur_y)
      if point in points:
        seen = True
        break
      points.append(point)
  elif facing == 'W':
    for i in range(0, length):
      cur_x -= 1
      point = (cur_x, cur_y)
      if point in points:
        seen = True
        break
      points.append(point)
  elif facing == 'N':
    for i in range(length):
      cur_y += 1
      point = (cur_x, cur_y)
      if point in points:
        seen = True
        break
      points.append(point)


dist = abs(0 - cur_x) + abs(0 - cur_y)
print('Final pos ({},{}) dist from origin {}'.format(cur_x, cur_y, dist))

