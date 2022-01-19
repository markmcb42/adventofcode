import sys
import time
from collections import Counter
from collections import deque
import hashlib

import numpy as np

def get_string(data):
    order = []
    for key, val in data.items():
        order.append((key, val))

    order.sort(key=lambda x: x[1])
    out = ''
    for item in order:
        out += item[0]
    return out

dance = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9,  \
         'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15}


moves = []
file = open('input.txt', 'r')
for line in file:
    items = line.strip().split(',')
    for item in items:
        if item[0] == 'x':
            data = item[1:].split('/', 1)
            a = int(data[0])
            b = int(data[1])
            moves.append((item[0], a, b))
        elif item[0] == 's':
            num = int(item[1:])
            moves.append((item[0], num))
        elif item[0] == 'p':
            pos = item.find('/')
            a = item[pos-1:pos]
            b = item[pos+1:]
            moves.append((item[0], a, b))

states = []
start = time.time()

for i in range(1000):
    state = get_string(dance)
    if state in states:
        print('Duplicate {} already exists'.format(state))
    states.append(state)

    for move in moves:
        if move[0] == 'x':
            apos = 0
            bpos = 0
            for key, val in dance.items():
                if val == move[1]:
                    apos = key
                if val == move[2]:
                    bpos = key
            tmp = dance[apos]
            dance[apos] = dance[bpos]
            dance[bpos] = tmp
        elif move[0] == 's':
            num = move[1]
            for key, value in dance.items():
                dance[key] = (value + num) % 16
                #if dance[key] >= len(dance):
                #    dance[key] -= len(dance)
        elif move[0] == 'p':
            tmp = dance[move[1]]
            dance[move[1]] = dance[move[2]]
            dance[move[2]] = tmp

end = time.time()
order = []
for key, val in dance.items():
    order.append((key, val))

order.sort(key = lambda x: x[1])
out = ''
for item in order:
    out += item[0]

print(end - start)
print(out)
