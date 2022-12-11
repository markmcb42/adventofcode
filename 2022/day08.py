
import sys
from parse import *
import copy


def check_row(row, row_num):
  cur = []
  val = -1
  for i in range(len(row)):
    if row[i] > val:
      val = row[i]
      cur.append((row_num, i))

  val = -1
  for i in range(len(row) - 1, 0, -1):
    if row[i] > val:
      val = row[i]
      cur.append((row_num, i))

  return cur


def check_col(col, col_num):
  cur = []
  val = -1
  for i in range(len(col)):
    if col[i] > val:
      val = col[i]
      cur.append((i, col_num))

  val = -1
  for i in range(len(col) - 1, 0, -1):
    if col[i] > val:
      val = col[i]
      cur.append((i, col_num))

  return cur


file = open('input08.txt', 'r')

grid = []
for line in file:
  line = line.strip()
  row = [int(x) for x in line]
  grid.append(row)

# Check Rows
trees = set()
for r in range(len(grid)):
  cur_trees = check_row(grid[r], r)
  trees.update(cur_trees)

# Check columns
for c in range(len(grid[0])):
  col = []
  for r in range(len(grid)):
    col.append(grid[r][c])
  cur_trees = check_col(col, c)
  trees.update(cur_trees)

print('Part 1: {}'.format(len(trees)))

score = 0
for row in range(1, len(grid) - 1):
  for c in range(1, len(grid[row]) - 1):
    top = 0
    cur = grid[row][c]
    for t in range(row-1, -1, -1):
      top += 1
      if grid[t][c] >= cur:
        break

    bot = 0
    for b in range(row+1, len(grid)):
      bot += 1
      if grid[b][c] >= cur:
        break

    right = 0
    for r in range(c+1, len(grid[row])):
      right += 1
      if grid[row][r] >= cur:
        break

    left = 0
    for l in range(c-1, -1, -1):
      left += 1
      if grid[row][l] >= cur:
        break

    cur_score = top * bot * right * left
    if cur_score > score:
      score = cur_score

print('Part 2: {}'.format(score))
























