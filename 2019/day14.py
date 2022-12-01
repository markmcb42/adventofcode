
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

class Reaction:

  def __init__(self, name):
    self.reactions = []
    self.name = name

  def add_reaction(self, r):
    self.reactions.append(r)

  def calc(self):
    total = 0
    for r in self.reactions:
      total += r.calc()
    return total

reactions = {}
ores = {}
file = open('input14.txt', 'r')
for line in file:
  items = line.strip().split('=>')
  if 'ORE' in items[0]:
    source = items[0].split()
    prod = items[1].split()
    ores[prod[1]] = (int(source[0]), int(prod[0]))
    continue

  data = items[1].split()
  source = items[0].split(',')
  rules = []
  for s in source:
    rule = s.split()
    rules.append((int(rule[0]), rule[1]))

  reactions[data[1]] = (int(data[0]), rules)


parts = [1]
for part in parts:
  ore_fuel = []
  new_fuel = (1, [])
  fuel = reactions['FUEL']
  while True:

    for r in fuel[1]:
      if r[1] not in ores:
        new_r = reactions[r[1]]
        if r[0] % new_r[0] == 0:
          quant = r[0] // new_r[0]
        elif r[0] < new_r[0]:
          quant = 1
        else:
          quant = (r[0] // new_r[0]) + 1
        #fuel[1].remove(r)
        for nr in new_r[1]:
          num = quant * nr[0]
          new_fuel[1].append((num, nr[1]))
      else:
        ore_fuel.append(r)

    if len(new_fuel[1]) == 0:
      break

    fuel[1].clear()
    # Get set of items
    items = set()
    for r in new_fuel[1]:
      items.add(r[1])

    for i in items:
      total = 0
      for r in new_fuel[1]:
        if i == r[1]:
          total += r[0]
      fuel[1].append((total, i))

    print('Next round')
    new_fuel[1].clear()

  totals = {}
  for r in ore_fuel:
    if r[1] not in totals:
      totals[r[1]] = 0
    totals[r[1]] += r[0]

  ore = 0
  for key in totals:
    amount = totals[key]
    while amount > 0:
      data = ores[key]
      ore += data[0]
      amount -= data[1]

  print('Total ore needed: {}'.format(ore))



