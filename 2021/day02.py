
import sys

def part1(data_in):
  depth = 0
  pos = 0

  for d in data_in:
    val = int(d[1])
    if 'forward' in d[0]:
      pos += val

    if 'down' in d[0]:
      depth += val

    if 'up' in d[0]:
      depth -= val

  return depth * pos


def part2(data_in):
  depth = 0
  pos = 0
  aim = 0

  for d in data_in:
    val = int(d[1])
    if 'forward' in d[0]:
      pos += val
      depth += (aim * val)

    if 'down' in d[0]:
      aim += val

    if 'up' in d[0]:
      aim -= val

  return depth * pos


file = open('input02.txt', 'r')
data = []
for line in file:
  data.append(line.strip().split(' '))

print('Part 1: {}'.format(part1(data)))
print('Part 2: {}'.format(part2(data)))