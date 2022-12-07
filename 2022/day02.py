
import sys

file = open('input02.txt', 'r')

part1 = 0
part2 = 0

for line in file:
  data = line.strip().split()
  if data[1] == 'X':
    part1 += 1
    if data[0] == 'A':
      part1 += 3
      part2 += 3
    elif data[0] == 'B':
      part2 += 1
    elif data[0] == 'C':
      part1 += 6
      part2 += 2
  elif data[1] == 'Y':
    part1 += 2
    part2 += 3
    if data[0] == 'A':
      part1 += 6
      part2 += 1
    elif data[0] == 'B':
      part1 += 3
      part2 += 2
    elif data[0] == 'C':
      part2 += 3

  elif data[1] == 'Z':
    part1 += 3
    part2 += 6
    if data[0] == 'A':
      part2 += 2
    elif data[0] == 'B':
      part1 += 6
      part2 += 3
    elif data[0] == 'C':
      part1 += 3
      part2 += 1


print('Part1: {} Part 2: {}'.format(part1, part2))


