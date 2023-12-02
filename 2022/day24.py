
import sys
#from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz
import collections
import functools
import numpy as np
import time
import itertools as it


def bfs(states, start, end, walls, time):

  queue = collections.deque([[start]])
  pos = (start, time)
  seen = {pos}
  while queue:
    path = queue.popleft()
    row, col = path[-1]
    if (row, col) == end:
      return path

    minute = len(path) + time
    if minute not in states:
      print('Must add more')

    cur = states[minute]

    if (row, col) not in cur:
      pos = ((row, col), minute)
      if pos not in seen:
        queue.append(path + [(row, col)])
        seen.add(pos)

    for row2, col2 in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
      if (row2, col2) in walls or row2 < 0 or row2 > 36:
        continue

      pos = ((row2, col2), minute)
      if pos in seen:
        continue

      if ((row2, col2) not in cur) and ((row2, col2) != start):
        queue.append(path + [(row2, col2)])
        seen.add(pos)

    # If we get stuck, back track until we have a place with no blizzard
    if not queue:
      while True:
        path = path[:-1]
        row, col = path[-1]
        t = len(path)
        pos = ((row, col), t)
        if (row, col) not in states[t] and pos not in seen:
          queue.append(path + [(row, col)])
          break


class Blizzard:
  def __init__(self, x, y, delta_x, delta_y):
    self.x = x
    self.y = y
    self.delta_x = delta_x
    self.delta_y = delta_y
    self.max_x = 0
    self.max_y = 0

  def move(self):
    cur_x = self.x + self.delta_x
    cur_y = self.y + self.delta_y
    if cur_x == 0:
      cur_x = self.max_x - 2
    elif cur_x == self.max_x - 1:
      cur_x = 1
    self.x = cur_x
    if cur_y == 0:
      cur_y = self.max_y - 2
    elif cur_y == self.max_y - 1:
      cur_y = 1
    self.y = cur_y


width = 0
height = 0
blizzards = []
walls = []
file = open('input24.txt', 'r')
for line in file:
  line = line.strip()
  if width == 0:
    width = len(line)

  for pos in range(len(line)):
    c = line[pos]
    if c == '.':
      continue
    if c == '#':
      walls.append((height, pos))
      continue

    dx = 0
    dy = 0

    if c == '>':
      # Moving right
      dy = 1
    elif c == '<':
      # Moving left
      dy = -1
    elif c == 'v':
      # Moving down
      dx = 1
    elif c == '^':
      # Moving up
      dx = -1

    blizzards.append(Blizzard(height, pos, dx, dy))
  height += 1

for b in blizzards:
  b.max_x = height
  b.max_y = width

states = {}
for i in range(1, 1000):
  cur = set()
  for b in blizzards:
    b.move()
    cur.add((b.x, b.y))
  states[i] = cur

start = (0, 1)
end = (height - 1, width - 2)
time = 0
path = bfs(states, start, end, walls, time)
print('Min number of steps: {}'.format(len(path) - 1))

# Go back to start
time += len(path) - 1
path = bfs(states, end, start, walls, time)

time += len(path) - 1
print('steps to go back: {} total: {}'.format((len(path) - 1), time))

# Go back to end
path = bfs(states, start, end, walls, time)
time += len(path) - 1
print('steps to go end: {} total: {}'.format((len(path) - 1), time))