
import sys
import numpy as np
from itertools import permutations
from string import ascii_lowercase as lc
import json

def getRelation(g1, g2, relations):

  for r in relations:
    if g1 == r[0] and g2 == r[1]:
      return r[2]


guests = set()
relations = []
      
file = open('input', 'r')

for line in file:

  line = line.strip()
  data = line.split()
  guests.add(data[0])
  guests.add(data[10][:-1])

  # Create units
  unit = int(data[3])
  if 'lose' in line:
    unit = unit * -1
  
  relation = (data[0], data[10][:-1], unit)
  relations.append(relation)

for g in guests:
  relation = ('Mark', g, 0)
  relations.append(relation)
  relation = (g, 'Mark', 0)
  relations.append(relation)

guests.add('Mark')

#print(guests)
#print(relations)

seatings = list(permutations(guests))

final = 0
for seating in seatings:

  cur = 0
  for i in range(len(seating) -1):
    g1 = seating[i]
    g2 = seating[i+1]
 
    cur += getRelation(g1, g2, relations)
    cur += getRelation(g2, g1, relations)

  g1 = seating[0]
  g2 = seating[len(seating) -1]
  cur += getRelation(g1, g2, relations)
  cur += getRelation(g2, g1, relations)

  if cur > final:
    final = cur

print('Happiness is {}'.format(final))
