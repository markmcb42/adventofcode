
import sys
#from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz
import collections
import functools
import numpy as np
import time
import itertools as it

values = {}
for i in range(10):
  cur = []
  for p in range(2, -3, -1):
    cur.append(p * (5 ** i))
  values[i] = cur

total = 0
file = open('input25.txt', 'r')
for line in file:
  line = line.strip()

  line = line[::-1]
  val = 0
  for i in range(len(line)):
    digit = 0
    if line[i] == '-':
      digit = -1
    elif line[i] == '=':
      digit = -2
    else:
      digit = int(line[i])

    val += digit * (5 ** i)
  total += val

print(total)

cur = total
digits = {}
exp = 0
neg_tot = 0
while cur != 0:
  q, r = divmod(cur, 5)

  if r < 3:
    if exp not in digits:
      digits[exp] = str(r)
    cur = q
    exp += 1
  elif r == 3:
    digits[exp] = '='
    neg_tot += 2 * (5 ** exp)
    cur = total + neg_tot
    exp = 0
  elif r == 4:
    digits[exp] = '-'
    neg_tot += (5 ** exp)
    cur = total + neg_tot
    exp = 0

val_str = ''
for i in range(len(digits) - 1, -1, -1):
  val_str += digits[i]
print('Snafu for {} is {}'.format(total, val_str))






