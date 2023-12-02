
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


file = open('input14.txt', 'r')

memvals = {}

mask = ''
for line in file:
  data = line.strip().split('=')
  val = data[1].strip()
  if 'mask' in data[0]:
    mask = val
    continue

  binstr = format(int(val), '036b')
  newstr = ''
  for i in range(len(mask)):
    if mask[i] != 'X':
      newstr += mask[i]
    else:
      newstr += binstr[i]

  pos = data[0].find('[')
  loc = int(data[0][pos+1:-2])
  memvals[loc] = int(newstr, 2)

tot = 0
for val in memvals.values():
  tot += val

print('Part 1: {}'.format(tot))

memvals = {}

file.seek(0)
mask = ''

for line in file:
  data = line.strip().split('=')
  val = data[1].strip()

  if 'mask' in data[0]:
    mask = val
    continue

  pos = data[0].find('[')
  loc = int(data[0][pos+1:-2])
  binstr = format(loc, '036b')

  numx = mask.count('X')
  fmt = '0' + str(numx) + 'b'

  for i in range(2 ** numx):
    xstr = format(i, fmt)
    xpos = 0
    loc_str = ''

    for x in range(len(binstr)):
      if mask[x] == '1':
        loc_str += '1'
      elif mask[x] == 'X':
        loc_str += xstr[xpos]
        xpos += 1
      else:
        loc_str += binstr[x]

    loc = int(loc_str, 2)
    memvals[loc] = int(val)

tot = 0
for val in memvals.values():
  tot += val

print('Part 2: {}'.format(tot))




