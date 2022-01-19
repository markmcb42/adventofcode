import sys
from itertools import product
import time

file = open('input.txt', 'r')

cur = 0
freq = []
cmds = []
for line in file:
    cmds.append(int(line.strip()))

while True:
    for cmd in cmds:
        cur += cmd
        if cur in freq:
            print(cur)
            sys.exit()
        freq.append(cur)







