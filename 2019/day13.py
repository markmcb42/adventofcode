
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy


class Intcode:

  def __init__(self, cmds):
    self.input = 1
    self.cmds = cmds
    self.index = 0
    self.modes = [0, 0, 0]
    self.rel_base = 0

  def set_input(self, input):
    self.input = input

  def get_ptrs(self):
    ret = []

    for m in range(len(self.modes)):
      if self.modes[m] == 0:
        ret.append(self.cmds[self.index+ + 1 + m])
      elif self.modes[m] == 1:
        ret.append(self.index + 1 + m)
      else:
        ret.append(self.rel_base + codes[self.index + 1 + m])

    return ret

  def run(self, complete):

    while self.index < len(self.cmds):
      cur_cmd = self.cmds[self.index]

      opcode = self.cmds[self.index] % 100
      self.modes = [0, 0, 0]
      if cur_cmd > 100:
        mode_str = str(cur_cmd - opcode)[::-1][2:]
        for c in range(len(mode_str)):
          self.modes[c] = int(mode_str[c])

      ptrs = self.get_ptrs()

      if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:

        val1 = self.cmds[ptrs[0]]
        val2 = self.cmds[ptrs[1]]

        # Calculate the result
        res = 0
        if opcode == 1:
          res = val1 + val2
        elif opcode == 2:
          res = val1 * val2
        elif opcode == 7:
          if val1 < val2:
            res = 1
          else:
            res = 0
        elif opcode == 8:
          if val1 == val2:
            res = 1
          else:
            res = 0

        # Save the result
        self.cmds[ptrs[2]] = res
        self.index += 4

      elif opcode == 9:
        self.rel_base += self.cmds[ptrs[0]]
        self.index += 2

      elif opcode == 3:
        self.cmds[ptrs[0]] = self.input
        self.index += 2

      elif opcode == 4:
        val = self.cmds[ptrs[0]]
        self.index += 2
        if not complete:
          return val
        else:
          print(codes[ptrs[0]])

      elif opcode == 5 or opcode == 6:
        val1 = codes[ptrs[0]]
        val2 = codes[ptrs[1]]

        if opcode == 5 and val1 != 0:
          self.index = val2
        elif opcode == 6 and val1 == 0:
          self.index = val2
        else:
          self.index += 3

      elif opcode == 99:
        return None


orig = []
file = open('input13.txt', 'r')
for line in file:
  orig = [int(x) for x in line.strip().split(',')]

parts = [1, 2]
for part in parts:

  codes = copy.copy(orig)
  zeros = [0] * 10000
  codes.extend(zeros)
  if part == 2:
    codes[0] = 2

  test = Intcode(codes)
  num_blocks = 0
  paddle = None
  ball = None
  active = False
  score = 0
  while True:

    # get the x position
    x = test.run(False)
    if x is None:
      break

    # get the y position
    y = test.run(False)

    # Get the tile type
    tile = test.run(False)
    if x == -1 and y == 0:
      active = True
      score = tile
      if ball[0] < paddle[0]:
        test.set_input(-1)
      elif ball[0] > paddle[0]:
        test.set_input(1)
      else:
        test.set_input(0)
      continue

    if tile == 2:
      num_blocks += 1
    elif tile == 3:
      paddle = (x, y)
    elif tile == 4:
      ball = (x,y)
      if active:
        if ball[0] < paddle[0]:
          test.set_input(-1)
        elif ball[0] > paddle[0]:
          test.set_input(1)
        else:
          test.set_input(0)

  if part == 1:
    print('The number of block tiles {}'.format(num_blocks))
  if part == 2:
    print('The final score is {}'.format(score))




