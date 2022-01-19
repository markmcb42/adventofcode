
import sys
import numpy as np
from itertools import permutations

file = open('input', 'r')

cmds = []
for line in file:

  # Save the unique cities
  data = line.strip().split()
  cmd = []
  for d in data:
    cmd.append(d)
  cmds.append(cmd)

regs = {}
regs['a'] = 1
regs['b'] = 0

max_ins = len(cmds)
i = 0
while len(cmds) > i >= 0:
  cmd = cmds[i]
  if 'jio' == cmd[0]:
    reg = cmd[1][0]
    if regs[reg] == 1:
      i += int(cmd[2])
    else:
      i += 1
  elif 'inc' == cmd[0]:
    regs[cmd[1][0]] += 1
    i += 1
  elif 'tpl' == cmd[0]:
    regs[cmd[1][0]] *= 3
    i += 1
  elif 'jmp' == cmd[0]:
    i += int(cmd[1])
  elif 'hlf' == cmd[0]:
    regs[cmd[1][0]] /= 2
    i += 1
  elif 'jie' == cmd[0]:
    if regs[cmd[1][0]] % 2 == 0:
      i += int(cmd[2])
    else:
      i += 1


print('The longest distance is {}'.format(len(cmds)))
