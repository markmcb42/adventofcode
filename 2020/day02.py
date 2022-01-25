
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


rules = []
file = open('input02.txt', 'r')
for line in file:
  data = line.strip().split()
  count_range = data[0].split('-')
  char = data[1][:-1]
  rule = (int(count_range[0]), int(count_range[1]), char, data[2])
  rules.append(rule)

p1_valid = 0
p2_valid = 0
for r in rules:
  counts = Counter(r[3])
  if r[2] in counts:
    if r[0] <= counts[r[2]] <= r[1]:
      p1_valid += 1
  count = 0

  if r[3][r[0]-1] == r[2]:
    count += 1

  if r[1]-1 < len(r[3]):
    if r[3][r[1]-1] == r[2]:
      count += 1

  if count == 1:
    p2_valid += 1

print(p1_valid)
print(p2_valid)



