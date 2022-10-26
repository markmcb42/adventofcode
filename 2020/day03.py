
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

max_row = 0
max_col = 0
lines = []
file = open('input03.txt', 'r')
for line in file:
  max_row += 1
  line = line.strip()
  for i in range(2):
    line += line

  if len(line) > max_col:
    max_col = len(line)
  lines.append(line)

orig = np.zeros((max_row, max_col), dtype='U1')
for row in range(len(lines)):
  line = lines[row]
  for col in range(len(line)):
    orig[row][col] = line[col]

row = 0
col = 0
count = 0
while row < max_row:
  if orig[row][col] == '#':
    count += 1

  row += 1
  col += 3

stdout.print()
print(count)
