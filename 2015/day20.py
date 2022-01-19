
import sys
import numpy as np
from itertools import permutations
from itertools import combinations
from string import ascii_lowercase as lc
from functools import reduce
import json

def factors(n):
  return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

weapons = []
weapons.append((8,4,0)
weapons.append((10,5,0)
weapons.append((25,6,0)
weapons.append((40,7,0)
weapons.append((74,8,0)

armor = []
armor.append(13,0,1)
armor.append(31,0,2)
armor.append(53,0,3)
armor.append(75,0,4)
armor.append(102,0,5)

rings = list(range(0,7)
print(rings)


