
import sys

file = open('input', 'r')

cur = 0
pos = 1
for line in file:
  for char in line:

    if char == '(':
      cur += 1
    if char == ')':
      cur -= 1

    if cur == -1:
      break

    pos += 1

print('basement position  {}'.format(pos))
