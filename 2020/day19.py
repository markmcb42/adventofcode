
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

rules = {}

class Rule:

  def __init__(self, num):
    self.num = num
    self.matches = []
    self.rules = []

  def set_rules(self, cur_rules):
    cur = [int(x) for x in cur_rules.strip().split(' ')]
    self.rules.append(cur)

  def finished(self):
    return len(self.rules) == 0

  # replace rule num with matches
  def update(self, val):
    new_rules = []

    for i in self.rules:
      if val in i:
        new_rules.extend(self.expand(val, i))
      else:
        new_rules.append(i)

    for r in new_rules:
      if isinstance(r, str):
        self.matches.append(r)

    self.rules = [x for x in new_rules if isinstance(x, list)]

  def expand(self, val, cur_rule):
    n_rules = []
    if cur_rule.count(val) == 2:
      for m in rules[val].matches:
        n_rules.append(m + m)
    else:
      pos = cur_rule.index(val)
      for m in rules[val].matches:
        copy_rule = copy.deepcopy(cur_rule)
        copy_rule[pos] = m
        if all(isinstance(i, str) for i in copy_rule):
          n_rules.append(''.join(copy_rule))
        else:
          n_rules.append(copy_rule)

    return n_rules


msgs = []

file = open('input19.txt', 'r')
for line in file:
  line = line.strip()
  if len(line) == 0:
    continue

  if ':' in line:
    data = line.split(':')
    num = int(data[0])
    r = Rule(num)

    if '|' in data[1]:
      items = data[1].split('|')
      for i in items:
        r.set_rules(i)
    elif 'a' in data[1]:
      r.matches.append('a')
    elif 'b' in data[1]:
      r.matches.append('b')
    else:
      r.set_rules(data[1])

    rules[num] = r
  else:
    msgs.append(line)

# Expand the rules
while True:
  if len(rules) == 1:
    break

  only_match = False
  cur = 0
  for key, val in rules.items():
    if val.finished():
      cur = key
      break

  for key, val in rules.items():
    if cur == key:
      continue
    val.update(cur)

  # Remove this since it has been expanded
  del(rules[cur])

count = 0
for m in msgs:
  if m in rules[0].matches:
    count += 1

print(count)







