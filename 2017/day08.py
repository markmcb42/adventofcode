import sys
import numpy as np
from collections import Counter

regs = {}
max_val = 0
file = open('input.txt', 'r')
for line in file:
    line = line.strip()

    data = line.split('if')
    cmd = data[0].split()
    if cmd[0] not in regs:
        regs[cmd[0]] = 0

    cond = data[1].split()
    if cond[0] not in regs:
        regs[cond[0]] = 0

    val = regs[cond[0]]
    check = int(cond[2])
    isValid = False
    if '>=' == cond[1]:
        isValid = val >= check
    elif '>' == cond[1]:
        isValid = val > check
    elif '<' == cond[1]:
        isValid = val < check
    elif '<=' == cond[1]:
        isValid = val <= check
    elif '!=' == cond[1]:
        isValid = val != check
    elif '==' == cond[1]:
        isValid = val == check

    if isValid:
        if 'inc' == cmd[1]:
            regs[cmd[0]] += int(cmd[2])
        else:
            regs[cmd[0]] -= int(cmd[2])
        if regs[cmd[0]] > max_val:
            max_val = regs[cmd[0]]

print(max_val)
max_val = 0
for val in regs.values():
    if val > max_val:
        max_val = val

print(max_val)




