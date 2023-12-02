
import sys

import numpy
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

tiles = {}

def move_in_direction(position, direction):
  """
  Move from the current position to a new position in the specified direction.
  """
  x, y = position
  if direction == 'e':
    return x + 1, y
  elif direction == 'se':
    if y % 2 == 0:
      return x, y - 1
    else:
      return x + 1, y - 1
  elif direction == 'sw':
    if y % 2 == 0:
      return x - 1, y - 1
    else:
      return x, y - 1
  elif direction == 'w':
    return x - 1, y
  elif direction == 'nw':
    if y % 2 == 0:
      return x - 1, y + 1
    else:
      return x, y + 1
  elif direction == 'ne':
    if y % 2 == 0:
      return x, y + 1
    else:
      return x + 1, y + 1
  else:
    raise ValueError("Invalid direction: " + direction)


def get_dirs(line):
  dirs = []

  direction = ''
  done = False
  for c in line:
    direction += c
    if c == 'e' or c == 'w':
      done = True
    if done:
      dirs.append(direction)
      direction = ''
      done = False

  return dirs


lines = []
file = open('input24.txt', 'r')
for line in file:
  lines.append(line.strip())


for l in lines:
  x, y = 0, 0

  dirs = get_dirs(l)
  for d in dirs:
    x, y = move_in_direction((x, y), d)

  # If this is in the tile list, flip, otherwise, add it
  cur = (x, y)
  if cur in tiles:
    if tiles[cur] == 'b':
      tiles[cur] = 'w'
    else:
      tiles[cur] = 'b'
  else:
    tiles[cur] = 'b'

total = 0
for t in tiles.values():
  if t == 'b':
    total += 1

print('Part 1: {}'.format(total))

dirs = ['e', 'se', 'sw', 'w', 'ne', 'nw']

# Add white tiles around black tiles
white = []
for key, value in tiles.items():
  if value == 'b':
    for d in dirs:
      x, y = move_in_direction(key, d)
      if (x, y) not in tiles and (x, y) not in white:
        white.append((x, y))

for w in white:
  tiles[w] = 'w'

for i in range(100):

  black = []
  white = []
  for key, value in tiles.items():
    b_tiles = 0
    for d in dirs:
      x,y = move_in_direction(key, d)
      if (x, y) in tiles:
        if tiles[(x, y)] == 'b':
          b_tiles += 1
    if value == 'b' and (b_tiles == 0 or b_tiles > 2):
      white.append(key)
    if value == 'w' and b_tiles == 2:
      black.append(key)
  for b in black:
    tiles[b] = 'b'
  for w in white:
    tiles[w] = 'w'

  # Add white tiles around black tiles
  white = []
  for key, value in tiles.items():
    if value == 'b':
      for d in dirs:
        x, y = move_in_direction(key, d)
        if (x, y) not in tiles and (x, y) not in white:
          white.append((x, y))

  for w in white:
    tiles[w] = 'w'


total = 0
for t in tiles.values():
  if t == 'b':
    total += 1

print('Part 2: {}'.format(total))



