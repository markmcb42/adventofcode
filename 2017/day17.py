import sys
import time
from collections import Counter
from collections import deque
import hashlib

import numpy as np


buf = [0, 1]
step = 355
pos = 1

for i in range(2, 2018):
  pos = ((pos + step) % i) + 1
  buf.insert(pos, i)

print('Part 1: {}'.format(buf[pos+1]))

pos = 1
val = 0
for i in range(2, 50000001):
  pos = ((pos + step) % i) + 1
  if pos == 1:
    val = i

print('Part 2: {}'.format(val))