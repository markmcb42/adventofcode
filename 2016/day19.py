import copy
import sys
from collections import Counter, OrderedDict
from collections import deque
import hashlib

import numpy as np

from bitarray import bitarray
from textwrap import wrap

elves = 5

circle = dict.fromkeys(range(1, elves + 1), 1)
order_circle = OrderedDict(sorted(circle.items(), key=lambda t : t[0]))

done = False
cur_max = elves
while not done:
  delete = []
  for key, value in order_circle.items():
    if value == 0:
      delete.append(key)
    else:
      if key == cur_max:
        first = next(iter(order_circle.items()))[0]
        order_circle[key] += order_circle[first]
        order_circle[first] = 0
      else:
        order_circle[key] += order_circle[key + 1]







