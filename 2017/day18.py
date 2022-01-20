import sys
import time
from collections import Counter
from collections import deque
import hashlib

import numpy as np

class Prog:
  def __init__(self, pid, cmds):
    self.pid = pid
    self.data = []
    self.cmds = cmds.copy()
    self.prog = None
    self.index = 0
    self.num_sent = 0
    self.regs = {'p': self.pid, 'one':1}

  def receive(self, val):
    self.data.append(val)

  def set_prog(self, prog):
    self.prog = prog

  def send(self, val):
    if self.prog is not None:
      self.prog.receive(val)
      self.num_sent += 1

  # Run until either need to send data or if no data is avail
  def run(self):

    while 0 <= self.index < len(self.cmds):
      cmd = self.cmds[self.index]

      val = 0
      if len(cmd) == 3:
        if cmd[2].isalpha():
          val = self.regs[cmd[2]]
        else:
          val = int(cmd[2])

      if 'snd' in cmd[0]:
        if cmd[1].isalpha():
          val = self.regs[cmd[1]]
        else:
          val = int(cmd[1])
        self.send(val)
        self.index += 1

      elif 'set' in cmd[0]:
        if cmd[1] not in self.regs:
          self.regs[cmd[1]] = 0
        self.regs[cmd[1]] = val
        self.index += 1

      elif 'add' in cmd[0]:
        if cmd[1] not in self.regs:
          self.regs[cmd[1]] = 0
        self.regs[cmd[1]] += val
        self.index += 1

      elif 'mul' in cmd[0]:
        if cmd[1] not in self.regs:
          self.regs[cmd[1]] = 0
        self.regs[cmd[1]] *= val
        self.index += 1

      elif 'mod' in cmd[0]:
        if cmd[1] not in self.regs:
          self.regs[cmd[1]] = 0
        self.regs[cmd[1]] %= val
        self.index += 1

      elif 'rcv' in cmd[0]:
        if len(self.data) == 0:
          return

        self.regs[cmd[1]] = self.data[0]
        self.data.pop(0)
        self.index += 1

      elif 'jgz' in cmd[0]:
        if self.regs[cmd[1]] > 0:
          self.index += val
        else:
          self.index += 1


cmds = []
file = open('input18.txt', 'r')
for line in file:
  cmds.append(line.strip().split())

p0 = Prog(0, cmds)
p1 = Prog(1, cmds)
p0.set_prog(p1)
p1.set_prog(p0)

while True:
  p0.run()
  p1.run()

  if len(p0.data) == 0 and len(p1.data) == 0:
    break

print(p1.num_sent)




