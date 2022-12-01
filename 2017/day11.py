import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

def get_steps(pos_x, pos_y):
  num_steps = 0
  if abs(y) > abs(x):
    num_steps = abs(y) + (abs(y) - abs(x))
  elif abs(x) > abs(y):
    num_steps = abs(y)
    diff = abs(x) - abs(y)
    num_steps += int(diff / 2)
    if diff % 2 == 1:
      num_steps += 1
  else:
    num_steps = abs(x)
  return num_steps

steps = []
file = open('input11.txt', 'r')
for line in file:
    steps = line.strip().split(',')

x = 0
y = 0
max_steps = 0

for s in steps:
  if len(s) == 1:
    if 'n' == s:
      x += 2
    if 's' == s:
      x -= 2
  else:
    if 'n' in s:
      x += 1
    if 's' in s:
      x -= 1
    if 'e' in s:
      y += 1
    if 'w' in s:
      y -= 1
  cur_steps = get_steps(x,y)
  if cur_steps > max_steps:
    max_steps = cur_steps

total = get_steps(x, y)


print('Part 1: {}  Part 2: {}'.format(total, max_steps))


