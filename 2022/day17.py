
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


class Piece:
  def __init__(self, config, height):
    self.config = config
    self.cur = config
    self.height = height
    self.max_h = 0

  def set_pos(self, x, y):
    self.cur = []
    for c in self.config:
      self.cur.append([c[0]+x, c[1]+y])
      if c[0] + x > self.max_h:
        self.max_h = c[0] + x

  # Given delta x and y, see if other obj is hit
  def check_hit(self, x, y, other):
    for c in self.cur:
      test = [c[0] + x, c[1] + y]
      if test in other.cur:
        return True
    return False

  def move(self, x, y):
    for c in self.cur:
      c[0] += x
      c[1] += y
    self.max_h += x

  def move_left(self):
    can_move = True
    for c in self.cur:
      if c[1] - 1 < 0:
        can_move = False
        break

    if can_move:
      for c in self.cur:
        c[1] -= 1

    return can_move

  def move_right(self):
    can_move = True
    for c in self.cur:
      if c[1] + 1 >= 7:
        can_move = False
        break

    if can_move:
      for c in self.cur:
        c[1] += 1

    return can_move

  def check_down(self, other):
    for c in self.cur:
      test = [c[0] - 1, c[1]]
      if test in other.cur:
        return False
    return True

  def move_down(self):
    for c in self.cur:
      c[0] -= 1
    self.max_h -= 1

  def hit_edge(self, y):
    for c in self.cur:
      if c[1] + y < 0:
        return True
      if c[1] + y > 6:
        return True
    return False


file = open('input17.txt', 'r')

move = ''
for line in file:
  move += line.strip()

pieces = 2022

pos = 0
dash = Piece([[0,0], [0,1], [0,2], [0,3]], 1)
plus = Piece([[0,1], [1,0], [1,1], [1,2], [2,1]], 3)
bend = Piece([[0,0], [0,1], [0,2], [1,2], [2,2]], 3)
line = Piece([[0,0], [1,0], [2,0], [3,0]], 4)
block = Piece([[0,0], [0,1], [1,0], [1,1]], 2)
blocks = [dash, plus, bend, line, block]

floor = Piece([[0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6]], 0)
ground = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

chamber = [floor]

height = 0
move_i = 0

for i in range(pieces):
  piece = copy.deepcopy(blocks[i % len(blocks)])
  piece.set_pos(height + 4, 2)

  # Handle first 3 moves
  delta_y = 0
  for _ in range(3):
    if move[move_i % len(move)] == '>':
      y = 1
    else:
      y = -1
    if not piece.hit_edge(y):
      piece.move(0, y)
    move_i += 1

  piece.move(-3, delta_y)

  while True:
    if move[move_i % len(move)] == '>':
      y = 1
    else:
      y = -1
    move_i += 1

    if not piece.check_hit(0, y, floor):
      if not piece.hit_edge(y):
        piece.move(0, y)
    #can_move = True
    #for p in reversed(chamber):
    #  if piece.check_hit(0, y, p):
    #    can_move = False
    #    break
    #if can_move:
    #  if not piece.hit_edge(y):
    #    piece.move(0, y)

    if not piece.check_hit(-1, 0, floor):
      piece.move(-1, 0)
    else:
      for c in piece.cur:
    can_move = True
    for p in reversed(chamber):
      if piece.check_hit(-1, 0, p):
        can_move = False
        break

    if can_move:
      piece.move(-1, 0)
    else:
      chamber.append(piece)
      for p in chamber:
        if p.max_h > height:
          height = p.max_h
      break

print(height)




