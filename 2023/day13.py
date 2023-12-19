import itertools
import math
import sys
import re
from collections import Counter
from enum import Enum
import numpy as np

from functools import cmp_to_key


file = open('input13.txt', 'r')

patterns = []
pattern = []
for line in file:
  if len(line.strip()) == 0:
    patterns.append(pattern)
    pattern = []
    continue

  pattern.append([x for x in line.strip()])

# Append last patter
patterns.append(pattern)
vertical_cols = []
horizontal_rows = []
count = 0
orig_mirrors = {}
for p in patterns:
  rows = len(p)
  cols = len(p[0])

  # Check vertical first
  vert_valid = False
  for i in range(cols - 1):
    lc = i
    rc = i + 1
    cols_to_check = min(rc, (cols - rc))
    valid = True
    for j in range(cols_to_check):
      check_l = lc - j
      check_r = rc + j
      for index in range(rows):
        if p[index][check_l] != p[index][check_r]:
          valid = False
          break
      if not valid:
        break

    if valid:
      vert_valid = True
      break

  if vert_valid:
    vertical_cols.append(rc)
    orig_mirrors[count] = ('v', rc)
    count += 1
    continue

  # If we get here, there was no vertical match, find horizontal match
  for i in range(rows - 1):
    tr = i
    lr = i + 1
    rows_to_check = min(lr, (rows - lr))
    valid = True
    for j in range(rows_to_check):
      check_top = tr - j
      check_lower = lr + j
      for index in range(cols):
        if p[check_top][index] != p[check_lower][index]:
          valid = False
          break
      if not valid:
        break

    if valid:
      break

  if valid:
    horizontal_rows.append(lr)
    orig_mirrors[count] = ('h', lr)
    count += 1
    continue

print('Part 1: {}'.format(sum(vertical_cols) + (100 * sum(horizontal_rows))))


vertical_cols = []
horizontal_rows = []
count = 0
for p in patterns:
  rows = len(p)
  cols = len(p[0])

  # Check vertical first
  vert_valid = False
  for i in range(cols - 1):
    lc = i
    rc = i + 1
    cols_to_check = min(rc, (cols - rc))
    valid = True
    smudge = False
    for j in range(cols_to_check):
      check_l = lc - j
      check_r = rc + j
      for index in range(rows):
        if p[index][check_l] != p[index][check_r]:
          if smudge:
            valid = False
            break
          else:
            smudge = True
      if not valid:
        break

    if valid:
      if orig_mirrors[count] == ('v', rc):
        continue
      vert_valid = True
      break

  if vert_valid:
    vertical_cols.append(rc)
    count += 1
    continue

  # If we get here, there was no vertical match, find horizontal match
  for i in range(rows - 1):
    tr = i
    lr = i + 1
    rows_to_check = min(lr, (rows - lr))
    valid = True
    smudge = False
    for j in range(rows_to_check):
      check_top = tr - j
      check_lower = lr + j
      for index in range(cols):
        if p[check_top][index] != p[check_lower][index]:
          if smudge:
            valid = False
            break
          else:
            smudge = True
      if not valid:
        break

    if valid:
      if orig_mirrors[count] == ('h', lr):
        continue
      break

  if valid:
    horizontal_rows.append(lr)
    count += 1
    continue

print('Part 2: {}'.format(sum(vertical_cols) + (100 * sum(horizontal_rows))))