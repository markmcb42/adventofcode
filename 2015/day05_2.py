
import sys

file = open('input', 'r')

total = 0
for line in file:

  hasPair = False
  hasRepeat = False

  for i in range(len(line) - 2):
    pair = line[i:i+2]
    rem = line[i+2:]

    if pair in rem:
      hasPair = True
      #print('Found pair {} in {}'.format(pair, line))
      break

  for i in range(len(line) - 2):
    if line[i] == line[i+2]:
      hasRepeat = True
  
  if hasPair and hasRepeat:
    total += 1

print('There are {} nice names'.format(total))
