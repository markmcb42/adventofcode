
import sys

import numpy
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


#cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
cups = [5, 8, 9, 1, 7, 4, 2, 6, 3]
cur_pos = 0

for i in range(100):

  label = cups[cur_pos]
  rem_cups = []
  del_pos = cur_pos
  for i in range(3):
    del_pos += 1
    if del_pos == len(cups):
      del_pos = 0
    rem_cups.append(cups[del_pos])
  #rem_cups = cups[cur_pos + 1:cur_pos + 4]
  for r in rem_cups:
    cups.remove(r)
  #del(cups[cur_pos+1:cur_pos+4])
  cur_pos += 1
  if cur_pos >= len(cups):
    cur_pos = 0
  next_label = cups[cur_pos]

  done = False
  dst = -1
  while not done:
    label -= 1
    if label == 0:
      label = max(cups)
    if label not in rem_cups:
      dst = cups.index(label)
      done = True

  cups[dst+1:dst+1] = rem_cups
  cur_pos = cups.index(next_label)

pos = cups.index(1)
cur_pos = pos + 1
out_str = ''
while cur_pos != pos:
  if cur_pos == len(cups):
    cur_pos = 0
  out_str += str(cups[cur_pos])
  cur_pos += 1

print('Part 1: {}'.format(out_str))








