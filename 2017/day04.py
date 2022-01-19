import sys
import numpy as np
from collections import Counter


count = 0
set_count = 0
valid = []
valid_set = []
line_num = 0
file = open('input.txt', 'r')

for line in file:
    line_num += 1
    counts = {}
    data = line.strip().split()
    test_list = []
    test_set = set()
    for item in data:
        sorted_item = "".join(sorted(item))
        test_list.append(sorted_item)
        test_set.add(sorted_item)
        cnt = Counter(item)
        counts[item] = cnt
    if len(test_list) == len(test_set):
        set_count += 1
        valid_set.append(line_num)

    isMatch = False
    keys = list(counts.keys())
    #for i_key in keys:
    for i in range(len(keys) - 1):
        if isMatch:
            break

        for j in range(i + 1, len(keys)):
            i_key = keys[i]
            j_key = keys[j]
            #if i_key == j_key:
            #    continue
            if len(counts[i_key]) != len(counts[j_key]):
                continue

            isMatch = True
            for char, val in counts[i_key].items():
                if char not in counts[j_key]:
                    isMatch = False
                    break
                if counts[i_key][char] != counts[j_key][char]:
                    isMatch = False
            if isMatch:
                break
    if not isMatch:
        count += 1
        valid.append(line_num)

print(count)
print(set_count)