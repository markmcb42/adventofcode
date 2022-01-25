
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

costs = []
file = open('input01.txt', 'r')
for line in file:
  costs.append(int(line.strip()))

for i in range(len(costs) - 2):
  for j in range(i + 1, len(costs)-1):
    for k in range(j + 1, len(costs)):
      if costs[i] + costs[j] + costs[k] == 2020:
        print(costs[i] * costs[j] * costs[k])
        sys.exit()
