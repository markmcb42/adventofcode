
import sys

file = open('input03.txt', 'r')

groups = []
group = []
count = 0
total = 0
for line in file:

  line = line.strip()
  group.append(line)
  count += 1
  if count == 3:
    groups.append(group)
    group = []
    count = 0

  size = int(len(line)/2)
  comp1 = line[size:]
  comp2 = line[:size]

  item = ''
  for c in comp1:
    if c in comp2:
      item = c
      break

  if item.islower():
    total += ord(item) - 96
  else:
    total += ord(item) - 38

print('Part1: {}'.format(total))

total = 0
# For each group, find the common item
for g in groups:
  for c in g[0]:
    if c not in g[1]:
      continue
    if c in g[2]:
      item = c
      break

  if item.islower():
    total += ord(item) - 96
  else:
    total += ord(item) - 38

print('Part2: {}'.format(total))

