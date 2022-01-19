
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

orbits = {}
file = open('input06.txt', 'r')
for line in file:
  data = line.strip().split(')')
  orbits[data[1]] = data[0]

total = 0
paths = { 'YOU':'', 'SAN':''}

for key, value in orbits.items():
  total += 1
  orbit = value
  while 'COM' not in orbit:
    if key in paths:
      paths[key] += orbit
    total += 1
    orbit = orbits[orbit]

print(total)

for key in paths.keys():
  paths[key] = paths[key][::-1]

count = 0
for i in range(max(len(paths['YOU']), len(paths['SAN']))):
  if paths['YOU'][i] != paths['SAN'][i]:
    break
  count += 1

total = len(paths['YOU']) + len(paths['SAN']) - (2 * count)
print(total // 3)







