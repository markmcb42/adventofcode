
import sys
from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz
import collections
import functools
import numpy as np
import time

sequence = []

file = open('input20.txt', 'r')
for line in file:
  sequence.append(int(line.strip()))

mix = copy.deepcopy(sequence)

for s in sequence:
  if s == 0:
    continue

  o_index = mix.index(s)
  i_index = o_index + s
  i_index = i_index % (len(mix) - 1)
  print('Val {} Orig index {} new {}'.format(s, o_index, i_index))
  mix.insert(i_index, mix.pop(o_index))

x = mix.index(0)

total = 0
nums = [1000, 2000, 3000]
for n in nums:
  i = (n + x) % len(mix)
  val = mix[i]
  total += val

print(total)
