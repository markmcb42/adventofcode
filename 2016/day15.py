import copy
import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

start = {}
start[1] = (11, 13)
start[2] = (0, 5)
start[3] = (11, 17)
start[4] = (0, 3)
start[5] = (2, 7)
start[6] = (17, 19)

final = [12, 3, 14, 2, 2, 13]
parts = [1, 2]

for p in parts:
  if p == 2:
    start[7] = (0, 11)
    final.append(4)

  discs = copy.deepcopy(start)

  time = 0
  while True:
    state = []
    for d in discs.values():
      state.append(d[0])

    if state == final:
      print('Part {} time {}'.format(p, time))
      break

    time += 1
    for item in discs.items():
        pos = item[1][0] + 1
        if pos == item[1][1]:
          pos = 0
        discs[item[0]] = (pos, item[1][1])










