
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


nums = []

file = open('input09.txt', 'r')
for line in file:
  line = line.strip()
  nums.append(int(line))

invalid = 0
index = 0
for i in range(25, len(nums)):
  val = nums[i]
  found = False
  for x in range(index, index + 24):
    if found:
      break
    for y in range(index + 1, index + 25):
      if val == nums[x] + nums[y]:
        found = True
        break

  index += 1
  if not found:
    print(val)
    invalid = val
    break

weakness = []
for i in range(len(nums)):
  length = 1
  total = nums[i]
  while total < invalid:
    total += nums[i + length]
    length += 1

  if total == invalid:
    for x in range(i, i + length):
      weakness.append(nums[x])
    break

weakness.sort()
print(weakness[0] + weakness[-1])


