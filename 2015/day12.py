
import sys
import numpy as np
from itertools import permutations
from string import ascii_lowercase as lc
import json

count = 0
prtCount = 0

def parse_json(json_obj):
  
  global prtCount
  global count

  if prtCount > 10:
    sys.exit()

  if type(json_obj) is dict:
    for key in json_obj:
      if key == 'red':
        print('Found red in key')
        return
      parse_json(json_obj[key])

  elif type(json_obj) is list:
    for item in json_obj:
      if type(item) is list:
        print('List item is {}'.format(item))
        prtCount += 1
        parse_json(item)
      elif type(item) is dict:
        print('Dict item is {}'.format(item))
        if 'red' in item:
          print('Found red in dict {}'.format(item))
          return
        parse_json(item)
      elif type(item) is int:
        count += item
        #print('Count is {} prtCount {}'.format(count, prtCount))
      else:
        print('Item {} is {}'.format(item, type(item)))

  else:
    if type(json_obj) is int:
      count += json_obj
      #print('Count is {} prtCount {}'.format(count, prtCount))
      
file = open('input', 'r')
line = file.readline()

from json import loads

def n(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([n(j) for j in j])
    if type(j) != dict:
        return 0
    if 'red' in j.values():
        return 0
    return n(list(j.values()))

print(n(loads(line)))

#jsonObj = json.loads(line)
#parse_json(jsonObj)

print('Final count is {}'.format(count))
