import copy
import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

from bitarray import bitarray
from textwrap import wrap

def gen_data(a):
  b = a[::-1]
  tmp = bitarray(b)
  tmp = ~tmp

  return a + '0' + tmp.to01()


length = 272
parts = [1, 2]
for p in parts:
  if p == 2:
    length = 35651584

  cur = '10010000000110000'

  while len(cur) < length:
    cur = gen_data(cur)

  cur = cur[:length]

  while (len(cur) % 2) == 0:
    tmp = bitarray(cur)
    cur = ''
    for i in range(0, len(tmp), 2):
      test = tmp[i:i+2]
      if not (test[0] ^ test[1]):
        cur += '1'
      else:
        cur += '0'

  print('Part {} checksum {}'.format(p, cur))









