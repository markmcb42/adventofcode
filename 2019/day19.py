
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy


class Intcode:

  def __init__(self, cmds):
    self.input = []
    self.cmds = cmds
    self.index = 0
    self.modes = [0, 0, 0]
    self.rel_base = 0

  def set_input(self, val):
    self.input.append(val)

  def get_ptrs(self):
    ret = []

    for m in range(len(self.modes)):
      if self.modes[m] == 0:
        ret.append(self.cmds[self.index+ + 1 + m])
      elif self.modes[m] == 1:
        ret.append(self.index + 1 + m)
      else:
        ret.append(self.rel_base + self.cmds[self.index + 1 + m])

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
        self.cmds[ptrs[0]] = self.input[0]
        self.input.pop(0)
        self.index += 2

      elif opcode == 4:
        ret_val = self.cmds[ptrs[0]]
        self.index += 2
        if not complete:
          return ret_val
        else:
          print(self.cmds[ptrs[0]])

      elif opcode == 5 or opcode == 6:
        val1 = self.cmds[ptrs[0]]
        val2 = self.cmds[ptrs[1]]

        if opcode == 5 and val1 != 0:
          self.index = val2
        elif opcode == 6 and val1 == 0:
          self.index = val2
        else:
          self.index += 3

      elif opcode == 99:
        return None


def get_pos(x, y, cmds):
  new_cmds = copy.copy(cmds)
  cur = Intcode(new_cmds)
  cur.set_input(x)
  cur.set_input(y)
  cur_pos = cur.run(False)
  del cur
  return cur_pos


orig = []
file = open('input19.txt', 'r')
for line in file:
  orig = [int(x) for x in line.strip().split(',')]

zeros = [0] * 100
orig.extend(zeros)

# Part 1
total = 0
for x in range(50):
  for y in range(50):

    pos = get_pos(x, y, orig)
    if pos == 1:
      total += 1

print(total)

# Part 2
start_y = 589
start_x = 935

for x in range(start_x, 10000):
  bFirst = True
  for y in range(start_y, 10000):
    pos = get_pos(x, y, orig)
    if pos == 0:
      continue

    if bFirst:
      start_y = y
      bFirst = False

    # Check y + 100
    pos = get_pos(x, y+99, orig)
    if pos == 0:
      break

    # Check x + 100
    pos = get_pos(x+99, y, orig)
    if pos == 0:
      continue

    # Check x + 100, y + 100
    pos = get_pos(x+99, y+99, orig)
    if pos == 1:
      res = (x * 10000) + y
      print(x, y, res)
      sys.exit()






