
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy


class Intcode:

  def __init__(self, cmds):
    self.input = None
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
        #print('Setting input val')
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


class Panel:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.color = 'black'
    self.painted = False

  def __eq__(self, other):
    return (self.x, self.y) == (other.x, other.y)

  def set_color(self, color):
    self.color = color

  def set_painted(self, flag):
    self.painted = flag

def turn(pos, direction):
  dirs = ['n', 'e', 's', 'w']
  cur_dir = dirs.index(pos)
  new_dir = None
  if direction == 0:
    # Turn left
    if cur_dir == 0:
      new_dir = dirs[3]
    else:
      new_dir = dirs[cur_dir - 1]

  elif direction == 1:
    # Turn right
    if cur_dir == 3:
      new_dir = dirs[0]
    else:
      new_dir = dirs[cur_dir + 1]

  else:
    print('Error invalid value {}'.format(direction))
    sys.exit()

  return new_dir


orig = []
file = open('input11.txt', 'r')
for line in file:
  orig = [int(x) for x in line.strip().split(',')]

  codes = orig.copy()
  zeros = [0] * 10000
  codes.extend(zeros)

  parts = [1,2]
  for part in parts:
    r_dir = 'n'
    panels = []
    cur = Panel(70, 70)

    if part == 2:
      cur.set_color('white')
    panels.append(cur)

    test = Intcode(codes)
    while True:
      input_val = 1
      if cur.color == 'black':
        input_val = 0
      test.set_input(input_val)

      # get the color to paint
      val = test.run(False)
      if val is None:
        break

      if val == 0:
        cur.set_color('black')
      elif val == 1:
        cur.set_color('white')
      else:
        print('Error, invalid val {}'.format(val))
        sys.exit()
      cur.set_painted(True)

      # Get the direction to turn and move one
      val = test.run(False)
      r_dir = turn(r_dir, val)

      x = cur.x
      y = cur.y
      if r_dir == 'n':
        x -= 1
      elif r_dir == 'e':
        y += 1
      elif r_dir == 's':
        x += 1
      elif r_dir == 'w':
        y -= 1

      # See if this panel has already been visited
      next = Panel(x,y)
      if next in panels:
        cur = panels[panels.index(next)]
      else:
        cur = next
        panels.append(cur)

    if part == 1:
      print('There are {} panels'.format(len(panels)))

      total = 0
      for p in panels:
        if p.painted:
         total += 1

      print('There are {} painted panels'.format(total))

    else:
      grid = np.zeros((200,200))
      for p in panels:
        if p.color == 'white':
          grid[p.x, p.y] = 1
      print('This is part 2')




