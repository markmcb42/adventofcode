
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

total = 0
file = open('input.txt', 'r')
for line in file:
  fuel = 0
  cur = (int(line.strip()) // int(3)) - 2
  while cur >= 0:
    if cur > 0:
      fuel += cur
    cur = (int(cur) // int(3)) - 2

  total += fuel

print(total)