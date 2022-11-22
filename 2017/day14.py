import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np


# Recursive function returns when l, r and down all are not 1
def update_point(grid, row, col, val):
    grid[row][col] = val
    if col > 0 and grid[row][col - 1] == '1':
        update_point(grid, row, col-1, val)
    if col < len(grid[row]) - 1 and grid[row][col + 1] == '1':
        update_point(grid, row, col + 1, val)
    if row < len(grid) - 1 and grid[row+1][col] == '1':
        update_point(grid, row + 1, col, val)
    if row > 0 and grid[row - 1][col] == '1':
        update_point(grid, row - 1, col, val)

# The starting point is always 1
def fill_region(grid, row, col, val):
  update_point(grid, row, col, val)
  return grid


def knot_hash(val_in):
    cir_list = []
    for i in range(256):
        cir_list.append(i)

    pos = 0
    skip = 0

    for _ in range(64):
        for l in val_in:
            rev_list = []
            if pos + l >= len(cir_list):
                rev_list = cir_list[pos:]
                rev_list += cir_list[:l - len(rev_list)]
            else:
                rev_list = cir_list[pos:pos + l]

            rev_list.reverse()
            for i in rev_list:
                cir_list[pos] = i
                pos += 1
                if pos == len(cir_list):
                    pos = 0

            pos += skip
            while pos >= len(cir_list):
                pos -= len(cir_list)
            skip += 1

    pos = 0
    hash_val = ''
    while pos < len(cir_list):
        val = cir_list[pos]
        for i in range(pos + 1, pos + 16):
            val ^= cir_list[i]
        hash_val += format(val, '02x')
        # print(format(val, 'x'))
        pos += 16
    return hash_val


base = 'amgozmfv'
total = 0
grid = []
for i in range(128):
    in_vals = []
    key = base + '-' + str(i)
    for c in key:
        in_vals.append(ord(c))

    in_vals += [17, 31, 73, 47, 23]
    hash_val = knot_hash(in_vals)
    row = []
    for c in hash_val:
        val = format(int(c,16), '04b')
        row += val
        total += val.count('1')
    grid.append(row)

print('Part 1: {}'.format(total))

num_regions = 0
for row in range(len(grid)):
  for col in range(len(grid[row])):
    if grid[row][col] != '1':
      continue
    num_regions += 1
    grid = fill_region(grid, row, col, str(num_regions+1))

print('Part 2: {}'.format(num_regions))





