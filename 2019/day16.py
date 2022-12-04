
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

orig = []
file = open('input16.txt', 'r')
for line in file:
  orig = [int(x) for x in line.strip()]

for i in range(2):
  orig += orig

base = [0, 1, 0, -1]

for p in range(1,101):

  output = []
  for pos in range(1, len(orig)+1):
    pattern = {}

    #while len(pattern) < (len(orig) + 1):
    #  for b in base:
    #    for i in range(pos):
    #      pattern.append(b)

    total = 0
    index = 1
    for o in orig:
     total += o * pattern[index]
     index += 1

    output.append(abs(total) % 10)

  orig = copy.copy(output)

final = []
for i in range(8):
  final.append(orig[i])

print(final)

