import sys
from itertools import product
from collections import Counter

import time

from blist import blist

file = open('input.txt', 'r')

claims = []
for line in file:
    data = line.strip().split()
    id = int(data[1:])
    pos = data[2].split(',')
    row = int(pos[0])
    col = int(pos[1][:len(pos[1]-1)])
    dim = data[3].split('x')









