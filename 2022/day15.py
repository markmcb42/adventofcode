
import sys
from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz
import collections
import functools
import numpy as np
import time


file = open('input15.txt', 'r')
pairs = []
beacons = []
min_x, min_y = sys.maxsize, sys.maxsize
max_x, max_y = 0, 0
max_dist = 0

for line in file:
  data = line.strip().split(':')
  sensor = data[0].split(',')
  pos = sensor[0].find('x=')
  sx = int(sensor[0][pos+2:])
  pos = sensor[1].find('y=')
  sy = int(sensor[1][pos+2:])

  beacon = data[1].split(',')
  pos = beacon[0].find('x=')
  bx = int(beacon[0][pos + 2:])
  pos = beacon[1].find('y=')
  by = int(beacon[1][pos + 2:])

  dist = abs(sx - bx) + abs(sy - by)
  if dist > max_dist:
    max_dist = dist

  pairs.append(([sx,sy], [bx,by], dist))
  beacons.append([bx, by])

  if min(sx, bx) < min_x:
    min_x = min(sx, bx)
  if min(sy, by) < min_y:
    min_y = min(sy, by)
  if max(sx, bx) > max_x:
    max_x = max(sx, bx)
  if max(sy, by) > max_y:
    max_y = max(sy, by)


y = 10
no_beacon = set()
for p in pairs:
  y_diff = abs(y - p[0][1])
  x_diff = p[2] - y_diff
  for x in range(p[0][0] - x_diff, p[0][0] + x_diff):
    no_beacon.add(x)
print(len(no_beacon))

max_val = 4000001

for y in range(0, max_val):
  ranges = []
  invalid = False
  for p in pairs:
    y_diff = abs(y - p[0][1])
    x_diff = p[2] - y_diff
    if x_diff < 0:
      continue
    start = p[0][0] - x_diff
    if start < 0:
      start = 0
    end = p[0][0] + x_diff
    if end > max_val:
      end = max_val

    ranges.append([start, end])

  ranges.sort()
  start = -1
  end = -1
  for r in ranges:
    if start == -1 and end == -1:
      start = r[0]
      end = r[1]
      continue

    if r[0] == end + 2:
      end += 1
      break

    if r[1] <= end:
      continue

    end = r[1]

  if end != max_val:
    val = (end * 4000000) + y
    print(val)
    break









