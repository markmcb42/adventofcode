
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

class Bag:
  def __init__(self, name):
    self.name = name
    self.bags = []
    self.count = 0

  def add_bag(self, bag, number):
    self.bags.append((bag, number))
    self.count += number

  def contains(self, name):
    for b in self.bags:
      if b[0].name == name:
        return True

      if b[0].contains(name):
        return True

    return False

  def count_bags(self):
    count = self.count
    for b in self.bags:
      count += (b[0].count_bags() * b[1])
    return count

bags = {}

file = open('input07.txt', 'r')
for line in file:
  line = line.strip()

  items = line.split('contain')
  data = items[0].split()
  name = data[0] + data[1]
  if name not in bags:
    bags[name] = Bag(name)

  if 'no' in items[1]:
    continue

  bag = bags[name]
  tmp = items[1].strip().split(',')
  for t in tmp:
    data = t.strip().split()
    name = data[1] + data[2]
    if name not in bags:
      bags[name] = Bag(name)

    bag.add_bag(bags[name], int(data[0]))

count = 0
for key, value in bags.items():
  if value.contains('shinygold'):
    count += 1

print(count)
print(bags['shinygold'].count_bags())


