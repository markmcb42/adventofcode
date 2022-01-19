
import sys
import numpy as np
from itertools import permutations
from string import ascii_lowercase as lc
import json

class Deer:
  def __init__(self, speed, fly, rest):
    self.speed = speed
    self.fly = fly
    self.rest = rest
    self.remain = fly
    self.isFlying = True
    self.dist = 0
    self.points = 0

  def __str__(self):
    str = f'''Remain: {self.remain}  isFlying: {self.isFlying} dist: {self.dist}  points: {self.points} '''
    return str

def getLeaders(deer):

  lead = []
  best = 0
  for key in deer:
    stats = deer[key]
    if stats.dist > best:
      best = stats.dist

  for key in deer:
    stats = deer[key]
    if stats.dist == best:
      lead.append(key)

  return lead

deer = {}
d = Deer(27, 5, 132)
deer['dancer'] = d

d = Deer(22, 2, 41)
deer['cupid'] = d

d = Deer(11, 5, 48)
deer['rudolf'] = d

d = Deer(28, 5, 134)
deer['donner'] = d

d = Deer(4, 16, 55)
deer['dasher'] = d

d = Deer(14, 3, 38)
deer['blitz'] = d

d = Deer(3, 21, 40)
deer['prancer'] = d

d = Deer(18, 6, 103)
deer['comet'] = d

d = Deer(18, 5, 84)
deer['vixen'] = d

race = 2503

count = 0
for i in range(2503):

  for key in deer:
    stats = deer[key]
    if stats.isFlying:
      stats.dist += stats.speed
      stats.remain -= 1
      if stats.remain == 0:
        stats.remain = stats.rest
        stats.isFlying = False
    else:
      stats.remain -= 1
      if stats.remain == 0:
        stats.remain = stats.fly
        stats.isFlying = True
    
  leaders = getLeaders(deer) 

  #print(deer['donner'])

  #count += 1
  #if count == 6:
  #  sys.exit()

  for key in deer:
    stats = deer[key]
    if key in leaders:
      stats.points += 1


best = 0
for key in deer:
  stats = deer[key]
  if stats.points > best:
    best = stats.points

print('Most points is {}'.format(best))
