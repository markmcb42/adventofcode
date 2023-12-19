import math
import sys
import re
from collections import Counter
from enum import Enum

from functools import cmp_to_key


file = open('input10.txt', 'r')

tiles = {}
row = 0

start = ()
path = []

for line in file:
  col = 0
  tiles[row] = {}
  for c in line.strip():
    tiles[row][col] = c
    if c == 'S':
      start = (row, col)
    col += 1
  row += 1

path.append(start)
moves = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

# Find the next part of the path
cur_d = ''
for k, v in moves.items():
  cur = (start[0] + v[0], start[1] + v[1])
  if k == 'N':
    if tiles[cur[0]][cur[1]] == '|' or tiles[cur[0]][cur[1]] == '7' or tiles[cur[0]][cur[1]] == 'F':
      cur_d = k
      break
  elif k == 'E':
    if tiles[cur[0]][cur[1]] == '-' or tiles[cur[0]][cur[1]] == 'J' or tiles[cur[0]][cur[1]] == '7':
      cur_d = k
      break
  elif k == 'S':
    if tiles[cur[0]][cur[1]] == '|' or tiles[cur[0]][cur[1]] == 'L' or tiles[cur[0]][cur[1]] == 'J':
      cur_d = k
      break
  elif k == 'W':
    if tiles[cur[0]][cur[1]] == '-' or tiles[cur[0]][cur[1]] == 'L' or tiles[cur[0]][cur[1]] == 'F':
      cur_d = k
      break

print('Cur {} dir {}'.format(cur, cur_d))
length = 1
while tiles[cur[0]][cur[1]] != 'S':
  path.append(cur)
  tile = tiles[cur[0]][cur[1]]
  if tile == '7':
    if cur_d == 'E':
      cur_d = 'S'
    else:
      cur_d = 'W'
  elif tile == 'J':
    if cur_d == 'E':
      cur_d = 'N'
    else:
      cur_d = 'W'
  elif tile == 'L':
    if cur_d == 'S':
      cur_d = 'E'
    else:
      cur_d = 'N'
  elif tile == 'F':
    if cur_d == 'N':
      cur_d = 'E'
    else:
      cur_d = 'S'
  length += 1
  cur = (cur[0] + moves[cur_d][0], cur[1] + moves[cur_d][1])

  #print(cur)

print('Part 1: {}'.format(length // 2))

# For part 2, determine what type of bend is at start
bend = ''
start_dirs = []
for k, v in moves.items():
  cur = (start[0] + v[0], start[1] + v[1])
  if k == 'N':
    if tiles[cur[0]][cur[1]] == '|' or tiles[cur[0]][cur[1]] == '7' or tiles[cur[0]][cur[1]] == 'F':
      start_dirs.append(k)
  elif k == 'E':
    if tiles[cur[0]][cur[1]] == '-' or tiles[cur[0]][cur[1]] == 'J' or tiles[cur[0]][cur[1]] == '7':
      start_dirs.append(k)
  elif k == 'S':
    if tiles[cur[0]][cur[1]] == '|' or tiles[cur[0]][cur[1]] == 'L' or tiles[cur[0]][cur[1]] == 'J':
      start_dirs.append(k)
  elif k == 'W':
    if tiles[cur[0]][cur[1]] == '-' or tiles[cur[0]][cur[1]] == 'L' or tiles[cur[0]][cur[1]] == 'F':
      start_dirs.append(k)

if 'N' in start_dirs and 'E' in start_dirs:
  bend = 'L'
if 'N' in start_dirs and 'W' in start_dirs:
  bend = 'J'
if 'S' in start_dirs and 'E' in start_dirs:
  bend = 'F'
if 'S' in start_dirs and 'W' in start_dirs:
  bend = '7'

in_tiles = set()
look_in = True
for i in range(1, len(path)):
  cur = path[i]
  search_dirs = []
  tile = tiles[cur[0]][cur[1]]
  if tile == '-':
    search = True
    if bend == 'L' or bend == 'J':
      if look_in:
        search_dirs.append('N')
      else:
        search_dirs.append('S')
    else:
      if look_in:
        search_dirs.append('S')
      else:
        search_dirs.append('N')
  elif tile == '|':
    search = True
    if bend == 'L' or bend == 'F':
      if look_in:
        search_dirs.append('E')
      else:
        search_dirs.append('W')
    else:
      if look_in:
        search_dirs.append('W')
      else:
        search_dirs.append('E')
  else:
    if bend == 'L' and tile == '7':
      look_in = not look_in
    elif bend == '7' and tile == 'L':
      look_in = not look_in
    elif bend == 'J' and tile == 'F':
      look_in = not look_in
    elif bend == 'F' and tile == 'J':
      look_in = not look_in
    bend = tile

    if bend == 'L':
      if look_in:
        search_dirs.append('N')
        search_dirs.append('E')
      else:
        search_dirs.append('S')
        search_dirs.append('W')
    elif bend == 'J':
      if look_in:
        search_dirs.append('N')
        search_dirs.append('W')
      else:
        search_dirs.append('S')
        search_dirs.append('E')
    elif bend == '7':
      if look_in:
        search_dirs.append('S')
        search_dirs.append('W')
      else:
        search_dirs.append('N')
        search_dirs.append('E')
    elif bend == 'F':
      if look_in:
        search_dirs.append('S')
        search_dirs.append('E')
      else:
        search_dirs.append('N')
        search_dirs.append('W')

  for d in search_dirs:
    check = cur
    while True:
      check = (check[0] + moves[d][0], check[1] + moves[d][1])
      if check in path:
        break
      in_tiles.add(check)

print('Part 2: {}'.format(len(in_tiles)))










