
import sys
from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz
import collections
import functools


def is_correct(l, r):
  if type(l) is int and type(r) is int:
    if l == r:
      return 0

    if l < r:
      return -1
    else:
      return 1

  if type(l) is int:
    l = [l]
  elif type(r) is int:
    r = [r]

  if l == [] and r == []:
    return 0

  if not l:
    return -1

  if not r:
    return 1

  ret = is_correct(l[0], r[0])
  if ret == 0:
    return is_correct(l[1:], r[1:])
  else:
    return ret


inputs = []
file = open('input13.txt', 'r')
packet = []
for line in file:
  if len(line.strip()) == 0:
    continue

  packet.append(line.strip())
  if len(packet) == 2:
    inputs.append(packet)
    packet = []


correct = []
index = 0
packets = []
for p in inputs:
  l_eval = eval(p[0])
  r_eval = eval(p[1])
  index += 1

  packets.append(l_eval)
  packets.append(r_eval)

  if is_correct(l_eval, r_eval) == -1:
    correct.append(index)

print(sum(correct))

d1 = '[[2]]'
d2 = '[[6]]'

packets.append(eval(d1))
packets.append(eval(d2))
packets.sort(key=functools.cmp_to_key(is_correct))
key = 1
index = 0
for p in packets:
  index += 1
  test = repr(p)
  if test == d1 or test == d2:
    key *= index

print(key)