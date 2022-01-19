
import sys
import copy
import numpy as np
from itertools import permutations
from itertools import combinations
from string import ascii_lowercase as lc
from functools import reduce
import json

def factors(n):
  return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def sim_fight(damage, armor):

  player = 100
  boss = 103

  bd = max(1, 9 - armor)
  pd = max(1, damage - 2)

  #print('Boss damage {} player damage {}'.format(bd, pd))
  while True:
    boss -= pd
    if boss <= 0:
      return True

    player -= bd
    if player <=0:
      return False 
    
weapons = []
weapons.append((8,4,0))
weapons.append((10,5,0))
weapons.append((25,6,0))
weapons.append((40,7,0))
weapons.append((74,8,0))

armor = []
armor.append((13,0,1))
armor.append((31,0,2))
armor.append((53,0,3))
armor.append((75,0,4))
armor.append((102,0,5))

rings = []
rings.append((25,1,0))
rings.append((50,2,0))
rings.append((100,3,0))
rings.append((20,0,1))
rings.append((40,0,2))
rings.append((80,0,3))

index = list(combinations(list(range(0,6)), 2))
for i in range(6):
  index.append((i))
print('len of ring list {}'.format(len(index)))

# Build the list of combinations
equip = []
for w in weapons:
  e = []
  e.append(w)
  equip.append(e)

  for a in armor:
    e = []
    e.append(w)
    e.append(a)
    equip.append(e)

    for i in index:
      e = []
      e.append(w)
      if type(i) is int:
        e.append(rings[i])
      else:
        e.append(rings[i[0]])
        e.append(rings[i[1]])

      equip.append(e)
      e = copy.deepcopy(e)
      e.append(a)
      equip.append(e)

most = 0

# See what is the least
for e in equip:

  #print(e)
  offense = 0
  defense = 0
  gold    = 0

  for item in e:
    offense += item[1]
    defense += item[2]
    gold    += item[0]

  if not sim_fight(offense, defense):
    print(e)
    print('Player lost, cost {}'.format(gold))
    if gold > most:
      most = gold

print('Most gold is {}'.format(most))
