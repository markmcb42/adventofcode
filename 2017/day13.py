import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

pipes = {}

class Layer:
    def __init__(self, depth):
        self.depth = depth
        self.cur = 0
        self.goingDown = True

    def advance(self):
        if self.goingDown:
            if self.cur + 1 == self.depth:
                self.cur -= 1
                self.goingDown = False
            else:
                self.cur += 1
        else:
            if self.cur -1 < 0:
                self.cur += 1
                self.goingDown = True
            else:
                self.cur -= 1



layers = {}
levels = {}
file = open('input.txt', 'r')
for line in file:
    data = line.strip().split(':')
    l = Layer(int(data[1]))
    layers[int(data[0])] = l
    levels[int(data[0])] = (int(data[1]) * 2) - 2

delay = 0
while True:
    delay += 1
    caught = False
    #for key in layers.keys():
    #    layers[key].cur = 0

    #for i in range(delay):
     #   for key in layers.keys():
     #       layers[key].advance()

    for i in range(93):
        if i in levels:
            if ((delay + i) % levels[i]) == 0:
                caught = True
                break

        #for key in layers.keys():

    if not caught:
        print(delay)

print(total)

