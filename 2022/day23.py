
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

lines = []
max_col = 0
max_row = 0

check_all = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
checks = {'n': [(-1, -1), (-1, 0), (-1, 1)], 's': [(1, -1), (1, 0), (1, 1)],
          'w': [(-1, -1), (0, -1), (1, -1)], 'e': [(-1, 1), (0, 1), (1, 1)]}

order = ['n', 's', 'w', 'e']
start_check = 0

row = 0
elves = {}
count = 0
file = open('input23.txt', 'r')
for line in file:
  line = line.strip()
  for c in range(len(line)):
    if line[c] == '#':
      elves[count] = (row, c)
      count += 1
  row += 1

rounds = 0
for _ in range(10000):
#while True:
  proposed = {}
  for num, e in elves.items():
    propose = False
    for c in check_all:
      if (c[0] + e[0], c[1] + e[1]) in elves.values():
        propose = True
        break

    if not propose:
      continue

    for x in range(start_check, start_check + 4):
      i = x % len(order)
      check = checks[order[i]]

      move = True
      for c in check:
        if (c[0] + e[0], c[1] + e[1]) in elves.values():
          move = False
          break
      if move:
        if order[i] == 'n':
          proposed[num] = (e[0] - 1, e[1])
        elif order[i] == 's':
          proposed[num] = (e[0] + 1, e[1])
        elif order[i] == 'w':
          proposed[num] = (e[0], e[1] - 1)
        elif order[i] == 'e':
          proposed[num] = (e[0], e[1] + 1)
        break

  for num, p in proposed.items():
    if list(proposed.values()).count(p) == 1:
      elves[num] = p

  rounds += 1
  if len(proposed) == 0:
    print('No movement')
    break
  start_check = (start_check + 1) % len(order)

print(rounds)
sys.exit()


min_row = min(x[0] for x in elves.values())
max_row = max(x[0] for x in elves.values())
min_col = min(x[1] for x in elves.values())
max_col = max(x[1] for x in elves.values())

count = 0
for r in range(min_row, max_row + 1):
  for c in range(min_col, max_col + 1):
    if (r,c) not in elves.values():
      count += 1

print(count)












