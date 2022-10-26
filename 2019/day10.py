
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import itertools
import copy
import math

def done(num, asteroid):
  print('{} removed {}'.format(num, asteroid))
  bet = (asteroid[0] * 100) + asteroid[1]
  print(bet)
  sys.exit()

def is_blocked(pt1, pt2):
  deltax = pt1[0] - pt2[0]
  deltay = pt1[1] - pt2[1]

  if abs(deltax) == 1 or abs(deltay) == 1:
    return False

  sx = 0
  sy = 0
  if deltax == 0 or deltay == 0:
    if 0 == deltax:
      if deltay > 0:
        sy = 1
      else:
        sy = -1
    if 0 == deltay:
      if deltax > 0:
        sx = 1
      else:
        sx = -1
  else:
    factor = math.gcd(abs(deltax), abs(deltay))
    sx = deltax // factor
    sy = deltay // factor

  is_blocked = False
  x = pt2[0] + sx
  y = pt2[1] + sy
  while (deltax == 0 or x != pt1[0]) and (deltay == 0 or y != pt1[1]):
    if (x, y) in points:
      is_blocked = True
      break
    x += sx
    y += sy

  return is_blocked


file = open('input10.txt', 'r')

points = []
y = 0
for line in file:
  line = line.strip()
  x = 0
  for c in line:
    if c == '#':
      points.append((x,y))
    x += 1
  y += 1

totals = []
for cur in points:
  total = 0
  for p in points:
    if p == cur:
      continue

    dx = p[0] - cur[0]
    dy = p[1] - cur[1]

    if abs(dx) == 1 or abs(dy) == 1:
      total += 1
      continue

    step_x = 0
    step_y = 0
    if dx == 0 or dy == 0:
      if 0 == dx:
        if dy > 0:
          step_y = 1
        else:
          step_y = -1
      if 0 == dy:
        if dx > 0:
          step_x = 1
        else:
          step_x = -1
    else:
      factor = math.gcd(abs(dx), abs(dy))
      step_x = dx // factor
      step_y = dy // factor

    blocked = False
    x = cur[0] + step_x
    y = cur[1] + step_y
    while (dx == 0 or x != p[0]) and (dy == 0 or y != p[1]):
      if (x,y) in points:
        blocked = True
        break
      x += step_x
      y += step_y
    if not blocked:
      total += 1

  totals.append((cur, total))

max_pt = None
max_tot = 0
for p in totals:
  if p[1] > max_tot:
    max_tot = p[1]
    max_pt = p[0]

print('Max point {} with a total of {}'.format(max_pt, max_tot))

#calculate the slopes for each point from max_pt
slopes = {'n': [], 's': [], 'e':[], 'w':[], 'ne':[], 'se':[], 'sw':[], 'nw':[]}

for p in points:
  if p == max_pt:
    continue

  if p[0] == max_pt[0]:
    if p[1] > max_pt[1]:
      slopes['s'].append(p)
    else:
      slopes['n'].append(p)
    continue

  if p[1] == max_pt[1]:
    if p[0] > max_pt[0]:
      slopes['e'].append(p)
    else:
      slopes['w'].append(p)
    continue

  dx = p[0] - max_pt[0]
  dy = p[1] - max_pt[1]
  slope = dx / dy
  if dx > 0:
    if dy > 0:
      slopes['se'].append((p, slope))
    else:
      slopes['ne'].append((p, slope))
  else:
    if dy > 0:
      slopes['sw'].append((p, slope))
    else:
      slopes['nw'].append((p, slope))

# sort the slopes
slopes['nw'].sort(key = lambda x: x[1] * -1)
slopes['ne'].sort(key = lambda x: x[1] * -1)
slopes['sw'].sort(key = lambda x: x[1] * -1)
slopes['se'].sort(key = lambda x: x[1] * -1)
slopes['n'].sort(key = lambda  x: x[1] * -1)
slopes['w'].sort(key = lambda  x: x[0] * -1)

count = 0
while True:
  vap = slopes['n'][0]
  slopes['n'].pop(0)
  points.remove(vap)
  count += 1

  # Go through 'ne' until done
  removed = []
  for item in slopes['ne']:

    if not is_blocked(item[0], max_pt):
      count += 1
      if count == 200:
        done(count, item[0])

      removed.append(item)

  # Remove all the vaporized asteroids
  for r in removed:
    points.remove(r[0])
    slopes['ne'].remove(r)

  vap = slopes['e'][0]
  slopes['e'].pop(0)
  points.remove(vap)
  count += 1
  if count == 200:
    done(count, vap)

  # Go through 'se' until done
  removed = []
  for item in slopes['se']:

    if not is_blocked(item[0], max_pt):
      count += 1
      if count == 200:
        done(count, item[0])
      removed.append(item)

  # Remove all the vaporized asteroids
  for r in removed:
    points.remove(r[0])
    slopes['se'].remove(r)

  vap = slopes['s'][0]
  slopes['s'].pop(0)
  points.remove(vap)
  count += 1
  if count == 200:
    done(count, vap)

  # Go through 'sw' until done
  removed = []
  for item in slopes['sw']:

    if not is_blocked(item[0], max_pt):
      count += 1
      if count == 200:
        done(count, item[0])
      removed.append(item)

  # Remove all the vaporized asteroids
  for r in removed:
    points.remove(r[0])
    slopes['sw'].remove(r)

  vap = slopes['w'][0]
  slopes['w'].pop(0)
  points.remove(vap)
  count += 1
  if count == 200:
    done(count, vap)

  # Go through 'nw' until done
  removed = []
  for item in slopes['nw']:

    if not is_blocked(item[0], max_pt):
      count += 1
      if count == 200:
        done(count, item[0])
      removed.append(item)

  # Remove all the vaporized asteroids
  for r in removed:
    points.remove(r[0])
    slopes['nw'].remove(r)












