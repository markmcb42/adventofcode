
import sys

file = open('input04.txt', 'r')

part1 = 0
part2 = 0
total = 0
for line in file:
  data = line.strip().split(',')
  section1 = [int(i) for i in (data[0].split('-'))]
  section2 = [int(i) for i in (data[1].split('-'))]
  total += 1

  # Number of sections which are subset of each other
  if section1[0] <= section2[0] and section1[1] >= section2[1]:
    part1 += 1
  elif section2[0] <= section1[0] and section2[1] >= section1[1]:
    part1 += 1

  # Number of non-over lapping sections
  if section1[1] < section2[0]:
    part2 += 1
  elif section2[1] < section1[0]:
    part2 += 1


print('Part 1: {} Part 2: {}'.format(part1, total - part2))




