
import sys
import re


file = open('input02.txt', 'r')

games = []
cubes = { 'red': 12, 'green': 13, 'blue': 14}
total_id = 0
total_power = 0

for line in file:
  line = line.strip()
  data = line.split(':')
  num = int(data[0].split(' ')[1])
  min_vals = {'red': 0, 'blue': 0, 'green': 0}

  sets = data[1].strip().split(';')
  is_possible = True
  for s in sets:
    rounds = s.strip().split(',')
    for r in rounds:
      elem = r.split()
      val = int(elem[0])
      color = elem[1]
      if val > min_vals[color]:
        min_vals[color] = val

      if val > cubes[color]:
        is_possible = False

  if is_possible:
    total_id += num

  power = 1
  for k, v in min_vals.items():
    power *= v
  total_power += power

print('Part 1: {} Part 2: {}'.format(total_id, total_power))








