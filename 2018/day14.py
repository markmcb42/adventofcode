
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

e1 = 3
e2 = 7
e1_pos = 0
e2_pos = 1

r_num = 157901
r_num = 18
recipes = [3, 7]
while len(recipes) < r_num + 10:
  r1 = recipes[e1_pos]
  r2 = recipes[e2_pos]
  new_r = str(r1 + r2)
  for c in new_r:
    recipes.append(int(c))
  e1_pos += r1 + 1
  e1_pos %= len(recipes)
  e2_pos += r2 + 1
  e2_pos %= len(recipes)

print(''.join(str(x) for x in recipes[r_num:r_num+10]))

r_num = 18
recipes = [3, 7]
while True:




