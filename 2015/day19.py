
import sys
import numpy as np
from itertools import permutations
from itertools import combinations
from string import ascii_lowercase as lc
import json


molecules = set()
replace = []

input = ''

file = open('input', 'r')

for line in file:
  
  if '=>' not in line:
    input = line.strip()
    continue

  data = line.strip().split(' => ')
  elem = (data[0], data[1])
  replace.append(elem)

output = input
total = 0
count = 0
while output != 'e':

  sub = 0
  replace_item = ('','')
  for data in replace:

    diff = abs(len(data[0]) - len(data[1]))
    save = output.count(data[1]) * diff
    #print('There are {} instances of {}'.format(count, data[1]))
    if save > sub:
      sub = save
      replace_item = data

  print('Save {} using {} len {}'.format(sub, replace_item, len(output)))
  output = output.replace(replace_item[1], replace_item[0])
  print('New len is {}'.format(len(output)))

  count += 1
  if count == 30:
    print('Line is currently {}'.format(output))
    sys.exit()
  
  #print(data[0])
  #pos = input.find(data[0])
  #while pos != -1:
    #newstr = input[:pos] + data[1] + input[pos + len(data[0]):]
    #pos = input.find(data[0], pos + 1)
    #print('new string is {}'.format(newstr))
    #molecules.add(newstr)

print('There are {} instance from len {} '.format(total, len(input)))


