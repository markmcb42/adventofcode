
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


start = [15, 12, 0, 14, 3, 1]
spoken = {}
turn = 1
prev = 0
for s in start:
  spoken[s] = [turn]
  turn += 1
  prev = s


while turn < 30000001:
  if len(spoken[prev]) == 1:
    prev = 0
    spoken[prev].append(turn)
  else:
    prev = spoken[prev][-1] - spoken[prev][-2]
    if prev in spoken:
      spoken[prev].append(turn)
    else:
      spoken[prev] = [turn]
  turn += 1
  if turn == 2021:
    print('Part 1 {}'.format(prev))

print('Part 2: {}'.format(prev))




