
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


file = open('input13.txt', 'r')
depart = int(file.readline())

line = file.readline()
data = line.split(',')

times = []
buses = []
interval = 0
first = 0
for d in data:
  if d == 'x':
    interval += 1
  else:
    if first == 0:
      first = int(d)
      continue

    times.append((int(d), interval+1))
    buses.append(int(d))
    interval = 0

min = 1000000
bus = 0

for b in buses:
  num = int(depart / b)
  delta = ((num + 1) * b) - depart
  if delta < min:
    min = delta
    bus = b

print(min * bus)

timestamp = first * 100000000000000
found = False

count = 0
while not found:
  count += 1
  timestamp += first
  found = True
  cur = timestamp
  for t in times:
    cur += t[1]
    test = cur % t[0]
    if cur % t[0] != 0:
      found = False
      break

  if found:
    print(timestamp)


