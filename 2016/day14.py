import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

def get_hash(key_str, part):

  if part == 1:
    return hashlib.md5(key_str.encode()).hexdigest()

  tmp_hash = key_str
  for i in range(2017):
    tmp_hash = hashlib.md5(tmp_hash.encode()).hexdigest()

  return tmp_hash


def find_first_triple(test_str):
  count = 0
  test_c = ''
  for c in test_str:
    if c != test_c:
      test_c = c
      count = 1
    else:
      count += 1
      if count == 3:
        break
  ret_str = ''
  if count == 3:
    ret_str = test_c
  return ret_str


salt = 'jlmsuwbz'

part = [1,2]

for p in part:
  index = 0
  count = 0
  hash_map = {}

  while True:
    key = salt + str(index)
    result = ''
    if key in hash_map:
      result = hash_map[key]
    else:
      result = get_hash(key, p)
      hash_map[key] = result

    c = find_first_triple(result)

    if len(c) == 1:
      # Test the next 1000
      test = c * 5
      found = False
      for i in range(index+1, index+1001):
        key = salt + str(i)
        if key in hash_map:
          result = hash_map[key]
        else:
          result = get_hash(key, p)
          hash_map[key] = result

        if test in result:
          found = True
          break

      if found:
        count += 1
        if count == 64:
          print('Index for part {} is {}'.format(p, index))
          break
    index += 1












