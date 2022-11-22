import sys
import numpy as np
from collections import Counter

regs = {}
max_val = 0
file = open('input09.txt', 'r')
for line in file:
    line = line.strip()

#line = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
groups = []
chars = 0
cur_group = 0
isCancel = False
inGarbage = False

for c in line:

  if isCancel:
    isCancel = False
    continue

  if c == '!':
    isCancel = True
    continue

  if inGarbage:
    if c == '>':
      inGarbage = False
    else:
     chars += 1
    continue

  if c == '{':
    cur_group += 1
    groups.append(cur_group)
  elif c == '}':
    cur_group -= 1
  elif c == '<':
    inGarbage = True

total = 0
for g in groups:
  total += g

print('Part 1: {} Part 2: {}'.format(total, chars))
