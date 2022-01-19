
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

orig = []
file = open('input.txt', 'r')
for line in file:
  orig = [int(x) for x in line.strip().split(',')]

for x in range(100):
  for y in range(100):

    codes = orig.copy()
    codes[1] = x
    codes[2] = y

    i = 0
    while i < len(codes):
      if codes[i] == 1:
        op1 = codes[i+1]
        op2 = codes[i+2]
        val = codes[op1] + codes[op2]
        dest = codes[i+3]
        codes[dest] = val
      elif codes[i] == 2:
        op1 = codes[i + 1]
        op2 = codes[i + 2]
        val = codes[op1] * codes[op2]
        dest = codes[i+3]
        codes[dest] = val
      elif codes[i] == 99:
        break
      i += 4
    if codes[0] == 19690720:
      print((100*x) + y)
      sys.exit()


