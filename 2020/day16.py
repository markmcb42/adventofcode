
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

rules = {}
fields = {}
actual = {}
tickets = []


def check_rules(value):
  for item in rules.values():
    for r in item:
      if r[0] <= value <= r[1]:
        return True
  return False


def check_rule(value, rules):
  for r in rules:
    if r[0] <= value <= r[1]:
      return True
  return False


file = open('input16.txt', 'r')


for line in file:
  line = line.strip()
  if len(line) == 0:
    continue

  if ':' in line:
    data = line.split(':')
    if len(data[1]) == 0:
      continue

    ranges = data[1].split('or')
    rules[data[0]] = []
    fields[data[0]] = []
    actual[data[0]] = []
    for r in ranges:
      vals = r.strip().split('-')
      rule = (int(vals[0]), int(vals[1]))
      rules[data[0]].append(rule)
  else:
    ticket = [int(x) for x in line.split(',')]
    tickets.append(ticket)

scan_error = 0
err_tickets = []
for t in tickets:
  remove = False
  for val in t:
    if not check_rules(val):
      scan_error += val
      remove = True
  if remove:
    err_tickets.append(t)

print('Part 1: {}'.format(scan_error))

for e in err_tickets:
  tickets.remove(e)

for key, value in rules.items():
  for i in range(len(tickets[0])):
    valid = True
    for t in tickets:
      if not check_rule(t[i], value):
        valid = False
        break
    if valid:
      fields[key].append(i)


done = False
while not done:
  val = -1
  field = ''
  for key, item in fields.items():
    if len(item) == 1:
      val = item[0]
      field = key
      actual[key] = val
      break

  if val == -1:
    break

  del fields[field]
  for key, item in fields.items():
    item.remove(val)

tot = 1
for key in rules.keys():
  if 'departure' in key:
    tot *= tickets[0][actual[key]]

print('Part 2: {}'.format(tot))


