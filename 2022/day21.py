
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

monkeys = {}


class Monkey:
  def __init__(self, name):
    self.name = name
    self.oper = ''
    self.val = 0
    self.rh = ''
    self.lh = ''
    self.prevr = 0
    self.curr = 0
    self.rdiff = []
    self.lval = 0

  def check_diff(self):

    if self.curr > 0 and self.prevr > 0:
      return True
    if self.curr < 0 and self.prevr < 0:
      return True

    return False

  def check(self):
    rh = monkeys[self.rh].shout()
    if self.curr == 0:
      self.prevr = rh
      self.curr = rh
    else:
      self.prevr = self.curr
      self.curr = rh

    if self.lval == 0:
      self.lval = monkeys[self.lh].shout()
    return rh == self.lval

  def shout(self):
    if len(self.oper) == 0:
      return self.val

    rhm = monkeys[self.rh]
    rh = rhm.shout()

    lhm = monkeys[self.lh]
    lh = lhm.shout()

    if self.oper == '+':
      return rh + lh
    if self.oper == '-':
      return rh - lh
    if self.oper == '*':
      return rh * lh
    if self.oper == '/':
      print('Val {} int {}'.format((rh / lh), round((rh / lh))))
      return round((rh / lh))

    return None


file = open('input21.txt', 'r')
for line in file:
  data = line.strip().split(':')
  m = Monkey(data[0])
  if data[1].strip().isdigit():
    m.val = int(data[1])
  else:
    oper = ''
    if '+' in data[1]:
      oper = '+'
    elif '-' in data[1]:
      oper = '-'
    elif '*' in data[1]:
      oper = '*'
    elif '/' in data[1]:
      oper = '/'
    elems = data[1].split(oper)
    m.oper = oper
    m.rh = elems[0].strip()
    m.lh = elems[1].strip()

  monkeys[data[0]] = m

#print(monkeys['root'].shout())

i = 0
count = 0
step = 1000000000
prev_diff = 0
root = monkeys['root']
monkeys['humn'].val = 3423279932938
if root.check():
  print('1 passed')
monkeys['humn'].val = 3423279932937
if root.check():
  print('2 passed')
sys.exit()
lh = monkeys[root.lh].shout()

while True:
  count += 1
  monkeys['humn'].val = i
  root.check()

  rh = monkeys[root.rh].shout()
  diff = rh - lh
  if diff == 0:
    print(i)
    break

  ch_dir = False
  if prev_diff != 0:
    if prev_diff < 0 and diff > 0:
      ch_dir = True
    elif prev_diff > 0 and diff < 0:
      ch_dir = True
  prev_diff = diff

  if ch_dir:
    step = int(step/2)

  if diff > 0:
    i += step + 1
  else:
    i -= step + 1


  #if root.check_diff():
  #  i += step
  #else:
    #step = int(step / 2)
    #i -= step

  #diff = root.check_diff()
  #if diff == 0:
  #  i += 1
  #elif diff < 0:
  #  i += abs(diff)
  #else:
  #  i -= diff

