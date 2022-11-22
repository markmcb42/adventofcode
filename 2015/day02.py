
import sys

file = open('input02.txt', 'r')

ribbon = 0
paper = 0
for line in file:

  data = line.split('x')
  dim = [int(x) for x in data]
  dim.sort()

  paper += (2 * dim[0] * dim[1]) + (2 * dim[1] * dim[2]) + (2 * dim[0] * dim[2]) + (dim[0] * dim[1])
  ribbon += (2 * (dim[0] + dim[1])) + (dim[0] * dim[1] * dim[2])

print('Part 1: {} Part 2: {}'. format(paper, ribbon))
