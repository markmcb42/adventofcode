import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

def get_next(val, is_a):
    a_factor = 16807
    b_factor = 48271

    while True:
        if is_a:
            val = (val * a_factor) % 2147483647
            if val % 4 == 0:
                return val
        else:
            val = (val * b_factor) % 2147483647
            if val % 8 == 0:
                return val


a = 699
b = 124
#a = 65
#b = 8921

count = 0
for i in range(5000000):

    a = get_next(a, True)
    b = get_next(b, False)

    a_bin = bin(a)
    b_bin = bin(b)

    if a_bin[len(a_bin) - 16:] == b_bin[len(b_bin) - 16:]:
        count += 1

print(count)


