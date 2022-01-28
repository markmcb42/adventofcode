
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


nums = []
max_jolt = 0
file = open('input10.txt', 'r')
for line in file:
  line = line.strip()
  jolt = int(line)
  nums.append(jolt)
  if jolt > max_jolt:
    max_jolt = jolt

max_jolt += 3
nums.append(max_jolt)
nums.append(0)
nums.sort()
jolt1 = 0
jolt3 = 0
for i in range(len(nums) -1):
  diff = nums[i+1] - nums[i]
  if diff == 1:
    jolt1 += 1
  elif diff == 3:
    jolt3 += 1

print(jolt1, jolt3, jolt3 * jolt1)

lengths = []
i = 0
length = 1
for i in range(len(nums) - 1):
  diff = nums[i+1] - nums[i]
  if diff == 1:
    length += 1
  elif diff == 3:
    if length > 1:
      lengths.append(length)
    length = 1

total = 1
for l in lengths:
  if l == 4:
    total *= 4
  elif l == 5:
    total *= 7
  elif l == 3:
    total *= 2

print(total)