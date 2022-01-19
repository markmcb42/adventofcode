
import sys
import numpy as np
from itertools import permutations
from string import ascii_lowercase as lc
import json

class Item:
  def __init__(self, capacity, durability, flavor, texture, calories):
    self.c = capacity
    self.d = durability
    self.f = flavor
    self.t = texture
    self.calories = calories

  #def __str__(self):
  #  str = f'''Remain: {self.remain}  isFlying: {self.isFlying} dist: {self.dist}  points: {self.points} '''
  #  return str

def sums(len, total):
  if len == 1:
    yield (total,)
  else:
    for value in range(total +1):
      for perm in sums(len-1, total - value):
        yield (value,) + perm

L = list(sums(4,100))

ingredients = []
i = Item(2, 0, -2, 0, 3)
ingredients.append(i)
i = Item(0, 5, -3, 0, 3)
ingredients.append(i)
i = Item(0, 0, 5, -1, 8)
ingredients.append(i)
i = Item(0, -1, 0, 5, 8)
ingredients.append(i)

best = 0
count = 0
for i in L:
  
  capacity = (i[0] * ingredients[0].c) + (i[1] * ingredients[1].c) + \
             (i[2] * ingredients[2].c) + (i[3] * ingredients[3].c) 

  if capacity <= 0:
    continue

  dur = (i[0] * ingredients[0].d) + (i[1] * ingredients[1].d) + \
        (i[2] * ingredients[2].d) + (i[3] * ingredients[3].d) 

  if dur <= 0:
    continue

  flavor = (i[0] * ingredients[0].f) + (i[1] * ingredients[1].f) + \
           (i[2] * ingredients[2].f) + (i[3] * ingredients[3].f) 

  if flavor <= 0:
    continue

  texture = (i[0] * ingredients[0].t) + (i[1] * ingredients[1].t) + \
            (i[2] * ingredients[2].t) + (i[3] * ingredients[3].t) 

  if texture <= 0:
    continue

  calories = (i[0] * ingredients[0].calories) + (i[1] * ingredients[1].calories) + \
            (i[2] * ingredients[2].calories) + (i[3] * ingredients[3].calories) 

  if calories != 500:
    continue

  total = capacity * dur * flavor * texture
  if total > best:
    best = total

print('The best total is {}'.format(best))
