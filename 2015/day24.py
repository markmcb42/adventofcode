
import sys
import numpy as np
from itertools import permutations
from itertools import combinations

file = open('input', 'r')

weights = []
total = 0
for line in file:

  w = int(line.strip())
  weights.append(w)
  total += w

target = total / 4
qe = sys.maxsize
#for i in range(5,10):
possible = []
data = list(combinations(weights, 5))
for d in data:
  test = sum(d)
  if sum(d) == target:
    possible.append(d)

for p in possible:
  remain = [x for x in weights if x not in p]
  max_group = int(len(remain) / 2)
  found = False
  for x in range(6, max_group):
    if found:
      break

    g2 = list(combinations(remain, x))
    for g in g2:
      if sum(g) == target:
        cur = np.prod(p)
        if cur < qe:
          qe = cur
        found = True
        break


print('QE is {}'.format(qe))
