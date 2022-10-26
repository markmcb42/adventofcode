
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

x, y = 0, 0

dir = 'E'
file = open('input12.txt', 'r')
for line in file:
  line = line.strip()

  action = line[0]
  val = int(line[1:])

  if action == 'N':
    x += val
  elif action == 'S':
    x -= val
  elif action == 'E':
    y += val
  elif action == 'W':
    y -= val

  elif action == 'F':
    if dir == 'N':
      x += val
    elif dir == 'S':
      x -= val
    elif dir == 'E':
      y += val
    elif dir == 'W':
      y -= val

  elif action == 'R':
    if val == 90:
      if dir == 'N':
        dir = 'E'
      elif dir == 'E':
        dir = 'S'
      elif dir == 'S':
        dir = 'W'
      elif dir == 'W':
        dir = 'N'
    elif val == 180:
      if dir == 'N':
        dir = 'S'
      elif dir == 'E':
        dir = 'W'
      elif dir == 'S':
        dir = 'N'
      elif dir == 'W':
        dir = 'E'
    elif val == 270:
      if dir == 'N':
        dir = 'W'
      elif dir == 'W':
        dir = 'S'
      elif dir == 'S':
        dir = 'E'
      elif dir == 'E':
        dir = 'N'

  elif action == 'L':
    if val == 90:
      if dir == 'N':
        dir = 'W'
      elif dir == 'W':
        dir = 'S'
      elif dir == 'S':
        dir = 'E'
      elif dir == 'E':
        dir = 'N'
    elif val == 180:
      if dir == 'N':
        dir = 'S'
      elif dir == 'E':
        dir = 'W'
      elif dir == 'S':
        dir = 'N'
      elif dir == 'W':
        dir = 'E'
    elif val == 270:
      if dir == 'N':
        dir = 'E'
      elif dir == 'E':
        dir = 'S'
      elif dir == 'S':
        dir = 'W'
      elif dir == 'W':
        dir = 'N'

print(abs(x) + abs(y))