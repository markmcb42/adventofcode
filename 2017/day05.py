import sys
import numpy as np
from collections import Counter

file = open('input.txt', 'r')

count = 0
offsets = []
for line in file:
    offsets.append(int(line.strip()))

i = 0
while 0 <= i < len(offsets):
    count += 1
    prev = i
    i += offsets[i]
    if offsets[prev] >= 3:
        offsets[prev] -= 1
    else:
        offsets[prev] += 1

print(count)


