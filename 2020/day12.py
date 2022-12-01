
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


cmds = []
file = open('input12.txt', 'r')
for line in file:
  line = line.strip()

  action = line[0]
  val = int(line[1:])
  cmds.append((action, val))

# Part 1
x, y = 0, 0
dir = 'E'

rdirs = ['N', 'E', 'S', 'W']
ldirs = ['N', 'W', 'S', 'E']

for c in cmds:
  action = c[0]
  val = c[1]

  # Move ship in indicated direction
  if (action == 'N') or ((action == 'F') and (dir == 'N')):
    x += val
  elif (action == 'S') or ((action == 'F') and (dir == 'S')):
    x -= val
  elif (action == 'E') or ((action == 'F') and (dir == 'E')):
    y += val
  elif (action == 'W') or ((action == 'F') and (dir == 'W')):
    y -= val

  elif action == 'R':
    index = rdirs.index(dir)
    if val == 90:
      delta = 1
    elif val == 180:
      delta = 2
    elif val == 270:
      delta = 3
    index += delta
    dir = rdirs[index % len(rdirs)]

  elif action == 'L':
    index = ldirs.index(dir)
    if val == 90:
      delta = 1
    elif val == 180:
      delta = 2
    elif val == 270:
      delta = 3
    index += delta
    dir = ldirs[index % len(ldirs)]


print('Part 1 {}'.format(abs(x) + abs(y)))

x, y = 0, 0
wp_x = 1
wp_y = 10

for c in cmds:
  action = c[0]
  val = c[1]

  # Move ship towards waypoint
  if action == 'F':
    x += (wp_x * val)
    y += (wp_y * val)

  # Move waypoint
  elif action == 'N':
    wp_x += val
  elif action == 'S':
    wp_x -= val
  elif action == 'E':
    wp_y += val
  elif action == 'W':
    wp_y -= val

  # Rotate waypoint around ship
  elif ((action == 'R') and (val == 90)) or ((action == 'L') and (val == 270)):
    tmp_x = -wp_y
    wp_y = wp_x
    wp_x = tmp_x
  elif (action == 'R' or action == 'L') and (val == 180):
    wp_y = -wp_y
    wp_x = -wp_x
  elif ((action == 'L') and (val == 90)) or ((action == 'R') and (val == 270)):
    tmp_y = -wp_x
    wp_x = wp_y
    wp_y = tmp_y

print('Part 2 {}'.format(abs(x) + abs(y)))
