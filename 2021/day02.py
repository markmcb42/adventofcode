
import sys


file = open('input', 'r')

depth = 0
pos = 0
aim = 0

for line in file:

  data = line.split(' ')
  val = int(data[1])
  if 'forward' in data[0]:
    pos += val
    depth += (aim * val)
    
  if 'down' in data[0]:
    aim += val
    
  if 'up' in data[0]:
    aim -= val

print('Final pos {}'.format(depth*pos))
