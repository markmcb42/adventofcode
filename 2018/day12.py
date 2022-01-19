
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

orig = []
rules = []

file = open('input.txt', 'r')
for line in file:
  line = line.strip()
  if 'initial' in line:
    pos = line.find(':')
    for c in line[pos+1:]:
      if c == '#' or c == '.':
        orig.append(c)
  else:
    pos = line.find('=>')
    if pos == -1:
      continue

    cond = line[:pos].strip()
    result = line[-1]
    rules.append((cond, result))

overflow = ['.'] * 25
state = overflow + orig + overflow

for _ in range(20):

#  print(''.join(state))
  newstate = state.copy()
  for i in range(2, len(state) - 2):
    comp = ''.join(state[i-2:i+3])
    found = False
    for rule in rules:
      if comp == rule[0]:
        found = True
        newstate[i] = rule[1]
        break
    if not found:
      newstate[i] ='.'
#  state = newstate.copy()

#print(''.join(state))

total = 0
for c in range(len(state)):
  if state[c] == '#':
    total += (c-25)

print(total)