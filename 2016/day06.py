from collections import Counter
import hashlib

strs = {}
file = open('input.txt', 'r')
for line in file:
    line = line.strip()
    for i in range(len(line)):
        if i not in strs:
            strs[i] = ''
        strs[i] += line[i]

msg = ''
for i in range(len(line)):
    counts = Counter(strs[i])
    min_count = 1000000
    char = ''
    for key, val in counts.items():
        if val < min_count:
            min_count = val
            char = key
    msg += char

print(msg)





