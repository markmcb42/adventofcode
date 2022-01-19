import sys
from itertools import product
from collections import Counter

import time

file = open('input.txt', 'r')

ids = []
for line in file:
    ids.append(line.strip())

count2 = 0
count3 = 0
for id in ids:
    cur2 = 0
    cur3 = 0
    counts = Counter(id)
    for count in counts:
        if counts[count] == 2:
            cur2 += 1
        if counts[count] == 3:
            cur3 += 1
    if cur2 > 0:
        count2 += 1
    if cur3 > 0:
        count3 += 1

print(count2 * count3)


for i in range(len(ids) - 1):
    for j in range(1, len(ids)):
        first = ids[i]
        sec = ids[j]
        diff = 0
        common = ''
        for f, s in zip(first, sec):
            if f != s:
                diff += 1
                if diff > 1:
                    break
            else:
                common += f
        if diff == 1:
            print(common)







