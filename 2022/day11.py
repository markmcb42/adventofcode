
import sys
from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz


class Operation(Enum):
  MULT = 1
  ADD = 2
  SQUARE = 3


class Monkey:

  decrease = 1

  def __init__(self):
    self.items = []
    self.oper = Operation.MULT
    self.val = 0
    self.test = 1
    self.true = 0
    self.false = 0
    self.count = 0

  def inspect(self, part):
    ret_list = []
    for i in self.items:
      self.count += 1
      worry = i
      if self.oper == Operation.ADD:
        worry += self.val
      elif self.oper == Operation.MULT:
        worry *= self.val
      elif self.oper == Operation.SQUARE:
        worry *= worry

      if part == 1:
        worry = int(worry/3)
      elif part == 2:
        if worry > Monkey.decrease:
          worry = worry % Monkey.decrease

      if (worry % self.test) == 0:
        ret_list.append((worry, self.true))
      else:
        ret_list.append((worry, self.false))
    self.items = []
    return ret_list


orig = {}
file = open('input11.txt', 'r')
cur = 0
for line in file:

  line = line.strip()
  if line.startswith('Monkey'):
    cur = int(line[:-1].split()[1])
    orig[cur] = Monkey()
    continue

  if line.startswith('Starting'):
    orig[cur].items = [int(x) for x in line.split(':')[1].split(',')]

  if line.startswith('Operation'):
    if '+' in line:
      orig[cur].oper = Operation.ADD
      orig[cur].val = int(line.split('+')[1])
    elif '*' in line:
      count = line.count('old')
      if count == 2:
        orig[cur].oper = Operation.SQUARE
      elif count == 1:
        orig[cur].oper = Operation.MULT
        orig[cur].val = int(line.split('*')[1])

  if line.startswith('Test'):
    val = int(line.split()[3])
    orig[cur].test = val
    Monkey.decrease *= val

  if 'true' in line:
    orig[cur].true = int(line.split()[5])
  if 'false' in line:
    orig[cur].false = int(line.split()[5])

for p in range(1,3):
  monkeys = copy.deepcopy(orig)
  rounds = 20
  if p == 2:
    rounds = 10000

  for i in range(rounds):
    for key, m in monkeys.items():
      items = m.inspect(p)
      for it in items:
        monkeys[it[1]].items.append(it[0])

  counts = []
  for key, m in monkeys.items():
    counts.append(m.count)

  counts.sort(reverse=True)
  print('Part {}: {}'.format(p, (counts[0] * counts[1])))





















