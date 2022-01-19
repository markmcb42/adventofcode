import sys
import time
from collections import Counter
from collections import deque
import hashlib

import numpy as np


buf = [0, 1]
step = 355
pos = 1

for i in range(2, 50000001):
  pos = ((pos + step) % len(buf)) + 1
  buf.insert(pos, i)


print(buf[pos], buf[pos+1], buf[0], buf[1])