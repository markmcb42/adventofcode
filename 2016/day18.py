import copy
import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

from bitarray import bitarray
from textwrap import wrap


floors = []
floors.append('^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^')

for i in range(400000 - 1):

  if i == 39:
    total = 0
    for f in floors:
      total += f.count('.')
    print('Part 1: {}'.format(total))

  cur = floors[i]
  next = ''

  for t in range(len(cur)):
    l, c, r = '.', '.', '.'
    if t == 0:
      c = cur[0]
      r = cur[1]
    elif t == len(cur) - 1:
      l = cur[t - 1]
      c = cur[t]
    else:
      l = cur[t - 1]
      c = cur[t]
      r = cur[t + 1]

    if l == '^' and c == '^' and r == '.':
      next += '^'
    elif c == '^' and r == '^' and l == '.':
      next += '^'
    elif l == '^' and r == '.' and c == '.':
      next += '^'
    elif r == '^' and c == '.' and l == '.':
      next += '^'
    else:
      next += '.'

  floors.append(next)



total = 0
for f in floors:
  total += f.count('.')

print('Part 2: {}'.format(total))




