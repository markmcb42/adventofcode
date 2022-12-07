
import sys
from parse import *
import copy


def part1(cmds, stacks):
  for c in cmds:
    for i in range(c[0]):
      stacks[c[2]].append(stacks[c[1]][-1])
      stacks[c[1]].pop()

  result = ''
  for key, data in stacks.items():
    result += data[-1]
  return result


def part2(cmds, stacks):
  for c in cmds:
    crates = stacks[c[1]][-c[0]:]
    stacks[c[2]] += crates

    for i in range(c[0]):
      stacks[c[1]].pop()

  result = ''
  for key, data in stacks.items():
    result += data[-1]
  return result


file = open('input05.txt', 'r')

orig = {1: ['T', 'D', 'W', 'Z', 'V', 'P'], 2: ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
        3: ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
        4: ['R', 'S', 'J'], 5: ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
        6: ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'], 7: ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
        8: ['P', 'T', 'B', 'Q'],
        9: ['H', 'G', 'Z', 'R', 'C']}

cmds = []
format_str = 'move {} from {} to {}'
for line in file:
  line = line.strip()
  cmds.append([int(x) for x in parse(format_str, line)])

parts = [1, 2]
for p in parts:
  stacks = copy.deepcopy(orig)

  if p == 1:
    print('Part 1: {}'.format(part1(cmds, stacks)))
  if p == 2:
    print('Part 2: {}'.format(part2(cmds, stacks)))








