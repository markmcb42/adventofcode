import math
import sys
import re
from collections import Counter
from enum import Enum

from functools import cmp_to_key


file = open('input09.txt', 'r')

reports = []

for line in file:
  reports.append([int(x) for x in line.strip().split()])

next_val = []
prev_val = []
for r in reports:
  cur = r
  sequences = [cur]
  while True:
    sequence = []
    for i in range(len(cur) - 1):
      sequence.append(cur[i+1] - cur[i])

    done = True
    for s in sequence:
      if s != 0:
        done = False
        break

    if not done:
      cur = sequence
      sequences.append(sequence)
    else:
      break

  next_v = 0
  for s in sequences:
    next_v += s[-1]
  next_val.append(next_v)

  sequences.reverse()
  prev_v = sequences[1][0] - sequences[0][0]
  for i in range(2, len(sequences)):
    prev_v = sequences[i][0] - prev_v
  prev_val.append(prev_v)

print('Part 1: {} Part 2: {}'.format(sum(next_val), sum(prev_val)))