
import sys

file = open('input01.txt', 'r')

cur = 0
pos = 1
basement = 0
for line in file:
  for char in line:

    if char == '(':
      cur += 1
    if char == ')':
      cur -= 1

    if cur == -1 and basement == 0:
      basement = pos

    pos += 1

print('Part 1: {} Part 2: {}'.format(cur, basement))
