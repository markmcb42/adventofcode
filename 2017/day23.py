import copy
import sys
import time
from collections import Counter
from collections import deque
import hashlib

import numpy as np


cmds = []
file = open('input23.txt', 'r')
for line in file:
  line = line.strip()
  cmds.append(line.split())

index = 0
mul_count = 0
reg = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}

while index < len(cmds):

  cmd = cmds[index]
  val = 0
  if cmd[2].isalpha():
    val = reg[cmd[2]]
  else:
    val = int(cmd[2])

  if 'jnz' in cmd[0]:
    test = 0
    if cmd[1].isalpha():
      test = reg[cmd[1]]
    else:
      test = int(cmd[1])

    if test != 0:
      index += val
    else:
      index += 1
    continue

  if 'set' in cmd[0]:
    reg[cmd[1]] = val
  elif 'sub' in cmd[0]:
    reg[cmd[1]] -= val
  elif 'mul' in cmd[0]:
    reg[cmd[1]] *= val
    mul_count += 1
  index += 1

print(mul_count, reg['h'])