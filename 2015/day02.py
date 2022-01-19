
import sys

file = open('input', 'r')

total = 0

for line in file:

  data = line.split('x')
  dim = [int(x) for x in data]
  dim.sort()

  cur = (2 * (dim[0] + dim[1])) + (dim[0] * dim[1] * dim[2])
  total += cur

print('Total square feet needed {}'.format(total))
