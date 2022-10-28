
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
  line = line.strip()
  lines.append(line)

col = len(lines[0])
row = len(lines)


while col < row * 7:
  lines = [line + line for line in lines]
  col = len(lines[0])

col = 0
total = 0
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_e = 0

for row in range(1, len(lines)):
  # a is R1 D1
  if lines[row][row] == '#':
    count_a += 1

  # b is Col 3 row 1
  if lines[row][row*3] == '#':
    count_b += 1

  # c is row 1 col 5
  if lines[row][row*5] == '#':
    count_c += 1

  # d is row 1 col 7
  if lines[row][row*7] == '#':
    count_d += 1

  # e is row 2 col 1
  if row * 2 > len(lines):
    continue

  if lines[row*2][row] == '#':
    count_e += 1

total = count_a  * count_b * count_c * count_d * count_e
print(count_a, count_b, count_c, count_d, count_e)
print('Part 1 {}'.format(count_b))
print('Part 2 {}'.format(total))
