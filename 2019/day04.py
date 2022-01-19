import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

low = 272091
high = 815432
count_part1 = 0
count_part2 = 0
for i in range(low, high):
    test = str(i)
    adj = False
    increase = True
    repeats = {}
    for c in range(len(test) - 1):
        if test[c] == test[c+1]:
            adj = True
            if test[c] not in repeats:
                repeats[test[c]] = 2
            else:
                repeats[test[c]] += 1

        elif test[c] > test[c+1]:
            increase = False
            break

    if adj and increase:
        count_part1 += 1
        pair = False
        for value in repeats.values():
            if value == 2:
                pair = True
                break

        if pair:
            count_part2 += 1


print('Part 1 count: {} Part 2 count: {}'.format(count_part1, count_part2))











