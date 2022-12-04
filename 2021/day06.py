
import sys

file = open('input06.txt', 'r')

data = [int(x) for x in file.readline().strip().split(',')]

fish = {}
for x in data:
  if x in fish:
    fish[x] += 1
  else:
    fish[x] = 1

for i in range(256):
 
  new_fish = {}
  for x in fish:
    if x == 0:
      new_fish[8] = fish[x]
      if 6 in new_fish:
        new_fish[6] += fish[x]
      else:
        new_fish[6] = fish[x]
    else:
      if x-1 in new_fish:
        new_fish[x-1] += fish[x]
      else:
        new_fish[x-1] = fish[x]

  fish = new_fish

  if i == 79:
    total = 0
    for i in fish:
      total += fish[i]
    print('Part 1: {}'.format(total))


total = 0
for i in fish:
  total += fish[i]

print('Part 2: {}'.format(total))

