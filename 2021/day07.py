
import sys

file = open('input07.txt', 'r')

line = file.readline().strip()
depth = [int(x) for x in line.split(',')]

max_depth = max(depth)
min_depth = min(depth)

least_p1 = sys.maxsize
least_p2 = sys.maxsize

costs = {}

for i in range(min_depth, max_depth):

  cur_p1 = 0
  cur_p2 = 0
  for x in depth:
    dif = abs(x - i)

    # Part 1
    cur_p1 += dif

    # Part 2
    if dif+1 not in costs:
      costs[dif+1] = sum(list(range(dif+1)))
    cur_p2 += costs[dif+1]

  if cur_p1 < least_p1:
    least_p1 = cur_p1

  if cur_p2 < least_p2:
    least_p2 = cur_p2

print('Part 1: {} Part 2: {}'.format(least_p1, least_p2))
