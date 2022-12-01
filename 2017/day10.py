import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

#lens = [97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190]
#lens = [3, 4, 1, 5]
lens = []
file = open('input10.txt', 'r')
for line in file:
    line = line.strip()
    for c in line:
        lens.append(ord(c))

lens += [17, 31, 73, 47, 23]

cir_list = []
for i in range(256):
    cir_list.append(i)

pos = 0
skip = 0

for _ in range(64):
    for l in lens:
        rev_list = []
        if pos + l >= len(cir_list):
            rev_list = cir_list[pos:]
            rev_list += cir_list[:l - len(rev_list)]
        else:
            rev_list = cir_list[pos:pos + l]

        rev_list.reverse()
        for i in rev_list:
            cir_list[pos] = i
            pos += 1
            if pos == len(cir_list):
                pos = 0

        pos += skip
        while pos >= len(cir_list):
            pos -= len(cir_list)
        skip += 1

pos = 0
hash_val = ''
while pos < len(cir_list):
    val = cir_list[pos]
    for i in range(pos+1, pos+16):
        val ^= cir_list[i]
    hash_val += format(val, 'x')
    #print(format(val, 'x'))
    pos += 16

print(hash_val, len(hash_val))

