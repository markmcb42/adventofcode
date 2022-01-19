import sys
from collections import Counter
from collections import deque
import hashlib


cmds = []
file = open('input.txt', 'r')
for line in file:
    line = line.strip()

    cmd = list(line.split())
    cmds.append(cmd)

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
i = 0
while i < len(cmds):

    cmd = cmds[i]
    if len(cmd) == 2:
        i += 1
        if 'inc' in cmd[0]:
            registers[cmd[1]] += 1
        else:
            registers[cmd[1]] -= 1
        continue

    val = 0
    if cmd[1].isalpha():
        val = registers[cmd[1]]
    else:
        val = int(cmd[1])

    if 'cpy' in cmd[0]:
        i += 1
        registers[cmd[2]] = val
        continue

    if val != 0:
        jmp = int(cmd[2])
        i += jmp
    else:
        i += 1


print(registers)






