import sys
from collections import Counter
from collections import deque
import hashlib

import numpy as np

grid = np.zeros((50,50))
for x in range(50):
    for y in range(50):
        val = ((x*x) + (3*x) + (2*x*y) + y + (y*y)) + 1352
        tmp = format(val, 'b')
        if tmp.count('1') % 2 == 1:
            grid[x][y] = 1

print(grid)








