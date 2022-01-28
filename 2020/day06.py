
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

answers = ''
count = 0
groups = []
group = []
file = open('input06.txt', 'r')
for line in file:
  line = line.strip()
  if len(line) == 0:
    counts = Counter(answers)
    count += len(counts)
    answers = ''
    groups.append(group)
    group = []
    continue

  answers += line
  group.append(line)

print(count)

count = 0
for group in groups:
  counters = {}
  for g in group:
    counts = Counter(g)
    for key in counts.keys():
      if key not in counters:
        counters[key] = 0
      counters[key] += 1

  for val in counters.values():
    if val == len(group):
      count += 1

print(count)
