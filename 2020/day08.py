
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


orig = []

file = open('input08.txt', 'r')
for line in file:
  line = line.strip()

  data = line.split()
  instruction = [data[0], int(data[1]), 0]
  orig.append(instruction)

acc = 0
index = 0
ins = copy.deepcopy(orig)
while True:
  if index >= len(ins):
    break

  i = ins[index]
  i[2] += 1
  if i[2] == 2:
    print(acc)
    break

  if i[0] == 'acc':
    acc += i[1]
    index += 1
  elif i[0] == 'nop':
    index += 1
  elif i[0] == 'jmp':
    index += i[1]

chg_index = 0
while True:
  ins = copy.deepcopy(orig)
  for x in range(chg_index, len(ins)):
    check = ins[x]
    if check[0] == 'nop':
      chg_index = x + 1
      check[0] = 'jmp'
      break
    elif check[0] == 'jmp':
      chg_index = x + 1
      check[0] = 'nop'
      break

  index = 0
  acc = 0
  normal = True
  while True:
    if index >= len(ins):
      break

    i = ins[index]
    i[2] += 1
    if i[2] == 2:
      normal = False
      break

    if i[0] == 'acc':
      acc += i[1]
      index += 1
    elif i[0] == 'nop':
      index += 1
    elif i[0] == 'jmp':
      index += i[1]

  if normal:
    print(acc)
    break


