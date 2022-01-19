import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

pipes = {}


def get_progs(groups, pipes, id):
    ids = []

    if len(pipes[id]) == 1:
        ids.append(pipes[id][0])
        return ids

    for i in pipes[id]:
        if i in groups:
            continue

        groups.add(i)
        ids += get_progs(groups, pipes, i)

    return ids


file = open('input.txt', 'r')
for line in file:
    data = line.strip().split('<->')
    progs = [int(x) for x in data[1].split(',')]
    pipes[int(data[0])] = progs

count = 0
while len(pipes) > 0:
    count += 1
    start = next(iter(pipes))
    group = set()
    group.add(start)
    for i in pipes[start]:
        group.add(i)
        ids = get_progs(group, pipes, i)
        for id in ids:
            group.add(id)

    for i in group:
        del pipes[i]

print(count)

