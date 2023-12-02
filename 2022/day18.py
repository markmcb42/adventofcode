
import sys
#from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz
import collections
import functools
import numpy as np
import time
import itertools as it

cubes = []
file = open('input18.txt', 'r')
for line in file:
  cube = [int(x) for x in line.strip().split(',')]
  cubes.append(cube)

min_x = min([x[0] for x in cubes])
max_x = max([x[0] for x in cubes])
min_y = min([x[1] for x in cubes])
max_y = max([x[1] for x in cubes])
min_z = min([x[2] for x in cubes])
max_z = max([x[2] for x in cubes])

total = 6 * len(cubes)
for i in range(len(cubes)-1):
  for j in range(i+1, len(cubes)):
    ci = cubes[i]
    cj = cubes[j]
    delta_x = abs(ci[0] - cj[0])
    if delta_x > 1:
      continue
    delta_y = abs(ci[1] - cj[1])
    if delta_y > 1:
      continue
    delta_z = abs(ci[2] - cj[2])
    if delta_z > 1:
      continue

    if delta_x == 1:
      if delta_y == 0 and delta_z == 0:
        total -= 2
    else:
      if delta_y == 0 or delta_z == 0:
        total -= 2

print(total)

pockets = []
for x in range(min_x-1, max_x + 1):
  for y in range(min_y-1, max_y + 1):
    for z in range(min_z-1, max_z + 1):
      if [x, y, z] in cubes:
        continue

      if [x, y, z+1] not in cubes:
        continue
      if [x, y, z-1] not in cubes:
        continue
      if [x, y+1, z] not in cubes:
        continue
      if [x, y-1, z] not in cubes:
        continue
      if [x+1, y, z] not in cubes:
        continue
      if [x-1, y, z] not in cubes:
        continue

      print('Found pocket at {},{},{}'.format(x, y, z))
      pockets.append([x,y,z])

pocket_tot = 6 * len(pockets)
for i in range(len(pockets)-1):
  for j in range(i+1, len(pockets)):
    ci = pockets[i]
    cj = pockets[j]
    delta_x = abs(ci[0] - cj[0])
    if delta_x > 1:
      continue
    delta_y = abs(ci[1] - cj[1])
    if delta_y > 1:
      continue
    delta_z = abs(ci[2] - cj[2])
    if delta_z > 1:
      continue

    if delta_x == 1:
      if delta_y == 0 and delta_z == 0:
        pocket_tot -= 2
    else:
      if delta_y == 0 or delta_z == 0:
        pocket_tot -= 2

print(total - pocket_tot)

