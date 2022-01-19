
import sys
import numpy as np
from itertools import permutations
from string import ascii_lowercase as lc
import json

file = open('input', 'r')

sues = {}
count = 0
for line in file:
  line = line.strip()

  pos = line.find(':')
  #name = line[:pos]
  num = int(line[:pos].split()[1])

  line = line[pos+1:]
  data = line.split(',')

  items = [] 
  for item in data:
    elem = item.split(':')
    name = elem[0].strip()
    val = int(elem[1])
    items.append((name,val))

  sues[num] = items


msg = []
msg.append(('children', 3))
msg.append(('cats', 7))
msg.append(('samoyeds', 2))
msg.append(('pomeranians', 3))
msg.append(('akitas', 0))
msg.append(('vizslas', 0))
msg.append(('goldfish', 5))
msg.append(('trees', 3))
msg.append(('cars', 2))
msg.append(('perfumes', 1))

for num in sues:
  sue = sues[num]

  isAll = True
  for i in sue:
    for j in msg:
      if i[0] in j[0]:
        if 'cats' == i[0] or 'trees' == i[0]:
          if i[1] < j[1]:
            isAll = False
            break
        elif 'pomeranians' == i[0] or 'goldfish' == i[0]:
          if i[1] > j[1]:
            isAll = False
            break
        else:
           if i[1] != j[1]:
            isAll = False
            break

  if isAll:
    print(num)


#print('The best total is {}'.format(best))
