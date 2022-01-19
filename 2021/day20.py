import sys
import ctypes
import bitarray
import struct
import numpy
import numpy as np
from collections import deque

def get_val_digits(data):

  start = -1
  end = -1
  for x in range(len(data)):
    if data[x].isdigit():
      if start == -1:
        start = x
    else:
      if end == -1 and start != -1:
        end = x
        break

  val = int(data[start:end])
  return val, (end-start)


def check_split(val):

  for i in range(len(val)):
    if val[i].isdigit() and val[i+1].isdigit():
      num = int(val[i:i+2])
      lnum = int(num/2)
      rnum = num - lnum

      cur = val[:i]
      cur += '[' + str(lnum) + ',' + str(rnum) + ']'
      cur += val[i+2:]

      return True, cur

  return False, val

def check_explode(val):
  count = 0
  for i in range(len(val)):
    if val[i] == '[':
      count += 1
    elif val[i] == ']':
      count -= 1

    # See if we need to explode
    if count == 5:
      pair = val[i:val.find(']', i) + 1]
      #print('Exploding {} i = {}'.format(pair, i))
      rpos = 0
      lpos = 0
      lval, ld2 = get_val_digits(val[i:])

      # Find the left value to update
      count = 0
      lpos = 0
      for x in range(i, 0, -1):
        if val[x].isdigit():
          count += 1
          lpos = x
        if not val[x].isdigit() and count > 0:
          break

      if count > 0:
        lval += int(val[lpos:lpos+count])

      # Get starting right value
      rpos = i + 2 + ld2
      rval, rd2 = get_val_digits(val[rpos:])
      rcut = i + 2 + ld2 + rd2

      # Find the next number to update
      rpos += rd2
      rupdated = False
      rd = 0
      for x in range(rpos, len(val)):
        if val[x].isdigit():
          rup, rd = get_val_digits(val[rpos:])
          if rd != 0:
            rupdated = True
            rval += rup
            rpos = x
            break

      # Build the new value string
      cur = ''
      if lpos == 0:
        cur = val[:i]
      else:
        cur = val[:lpos]
        cur += str(lval)
        cur += val[lpos+count:i]

      cur += '0'
      cur += val[rcut+1:rpos]
      if rupdated:
        cur += str(rval)
        cur += val[rpos+rd:]
      else:
        cur += val[rpos+rd+1:]

      return True, cur

  return False, val


snums = []

def get_left(pos, line):

  if line[pos] == '[':
    pos += 1
    pos, lnum = get_left(pos, line)
    sn = SnailNum()
    sn.left = lnum
    pos += 1
    pos, sn.right = get_right(pos, line)
    return pos, sn

  elif line[pos].isdigit():
    num = int(line[pos])
    pos += 1
    return pos, num

def get_right(pos, line):

  while line[pos] == ']':
    pos += 1

  if line[pos] == ',':
    pos += 1

  if line[pos] == '[':
    pos += 1
    pos, lnum = get_left(pos, line)
    sn = SnailNum()
    sn.left = lnum
    pos += 1
    pos, sn.right = get_right(pos, line)
    return pos, sn
  elif line[pos].isdigit():
    num = int(line[pos])
    return pos, num

class SnailNum:

  def __init__(self):
    self.left = []
    self.right = []

  def get_lvalue(self):
    if type(self.left) == int:
      total = self.left * 3
      return total

    #total = self.left.get_lvalue()
    return self.left.calc_magnitude() * 3

  def get_rvalue(self):
    if type(self.right) == int:
      total = self.right * 2
      return total

    #total = self.right.get_rvalue()
    return self.right.calc_magnitude() * 2

  def calc_magnitude(self):
    return self.get_lvalue() + self.get_rvalue()

def get_int(val):
  i = 0
  for bit in val:
    i = (i << 1) | bit
  return i

def get_snail_num(line):
  pos = 1
  pos, lnum = get_left(pos, result)

  sn = SnailNum()
  sn.left = lnum

  # Once we have the left value, should be at a ',' or ']'
  # if a ']' increment until we find ','
  while result[pos] != ',':
    pos += 1

  if result[pos] == ',':
    pos += 1
    pos, sn.right = get_right(pos, result)

  return sn

def get_alg_val(x, y, max, grid):
  if x == 0 or y == 0 or x == max -1 or y == max -1:
    return 0

  val = ''
  for i in range(x-1,x+2):
    for j in range(y-1, y+2):
      if grid[i][j] == '.':
        val += '0'
      else:
        val += '1'

  tmp = int(val, base=2)
  #ba = bitarray.bitarray()
  #ba.frombytes(bytes(bytearray.fromhex(val)))
  #tmp = get_int(ba)
  return tmp


image = []
file = open('input', 'r')
alg = ''
row_len = 0
for line in file:
  line = line.strip()
  if alg == '':
    alg = line
    continue

  if len(line) == 0:
    continue

  row = []
  row_len = len(line)
  for c in line:
    row.append(c)

  image.append(row)


print('HI')

new_grid = []
cur_max = row_len + 4
line = '.' * (cur_max)
new_grid.append(line)
new_grid.append(line)
for row in image:
  new_row = deque(row)
  new_row.appendleft('.')
  new_row.appendleft('.')

  new_row.append('.')
  new_row.append('.')

  new_grid.append(list(new_row))

new_grid.append(line)
new_grid.append(line)

new_image = []
for i in range(cur_max):
  row = []
  for j in range(cur_max):
    row.append('.')
  new_image.append(row)

for x in range(cur_max):
  for y in range(cur_max):
    alg_val = get_alg_val(x, y, cur_max, new_grid)
    if alg_val == 0:
      continue
    print('alg val {}'.format(alg_val))
    new_image[x][y] = alg[alg_val]

    #new_image[x][y] == check_pixel(x, y, cur_max, new_grid)

count = 0
for x in range(cur_max):
  for y in range(cur_max):
    if new_image[x][y] == '#':
      count += 1
print('HI')
