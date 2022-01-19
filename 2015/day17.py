
import sys
import numpy as np
from itertools import permutations
from itertools import combinations
from string import ascii_lowercase as lc
import json

file = open('input', 'r')

sizes = []

count = 0
for line in file:
  val = int(line.strip())

  sizes.append(val)

print(len(sizes))
smallest = False
for i in range(1, len(sizes)):
  combs = list(combinations(sizes, i))

  for comb in combs:
    if sum(comb) == 150:
      count += 1
      smallest = True

  if not smallest:
    count = 0
  else:
    print('Smallest number is {} count {}'.format(i, count))
    sys.exit()

print('There are {} combinations'.format(count))
