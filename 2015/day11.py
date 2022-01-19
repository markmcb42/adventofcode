
import sys
import numpy as np
from itertools import permutations
from string import ascii_lowercase as lc

def increment(line):

  l = list(line)
  for i in range(len(l)-1, 0, -1):
    if l[i] != 'z':
      l[i] = chr(ord(l[i]) + 1)
      return ''.join(l)
    else:
      l[i] = 'a'
 
input = 'hepxxyzz'
while True:

  input = increment(input)

  # Check invalid letters
  if 'i' in input or 'o' in input or 'l' in input:
    continue

  # Check for pairs
  count = 0
  hasPairs = False
  for c in lc:
    test = c + c
    if test in input:
      #print('{} found in {}'.format(test, input))
      count += 1

    if count == 2:
      hasPairs = True
      break

  if not hasPairs:
    continue
      
  hasRun = False
  count = 0
  for c in lc:
    if c == 'y':
      break

    test = c + chr(ord(c) + 1) + chr(ord(c) + 2)
    if test in input:
      hasRun = True

  if hasRun:
    print('password is {}'.format(input))
    sys.exit()
