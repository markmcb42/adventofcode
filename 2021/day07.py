
import sys

file = open('input', 'r')

line = file.readline().strip()
#line = '3,4,3,1,2'

depth = [ int(x) for x in line.split(',')]

max = max(depth)
min = min(depth)

least = sys.maxsize

for i in range(min, max):

  cur = 0
  for x in depth:
    dif = abs(x - i)
    l = list(range(dif+1))
    cur += sum(l)

    #count = 1
    #for y in range(dif):
    #  cur += count
    #  count += 1
    #cur += abs(x - i)

  if cur < least:
    least = cur

print('Least fuel is {}'.format(least))
