
import sys
from parse import *
import copy


class Dir:

  def __init__(self):
    self.dirs = []
    self.files = []

  def add_dir(self, d):
    self.dirs.append(d)

  def add_file(self, f):
    self.files.append(f)

  def calc_size(self):
    total = 0
    for d in self.dirs:
      total += d.calc_size()
    for f in self.files:
      total += f[1]
    return total


file = open('input07.txt', 'r')

pwd = '/'
dirs = {pwd: Dir()}

for line in file:

  data = line.strip().split()

  if data[0] == '$' and data[1] == 'cd':
    if data[2] == '..':
      pos = pwd.rfind('/', 0, len(pwd) - 1)
      pwd = pwd[:pos+1]
    else:
      pwd += data[2] + '/'
    continue

  if data[1] == 'ls':
    if pwd not in dirs:
      dirs[pwd] = Dir()

  cur_dir = dirs[pwd]
  while True:
    data = file.readline().strip().split()
    if len(data) == 0:
      break

    if data[0] == 'dir':
      child_dir = pwd + data[1] + '/'
      if child_dir not in dirs:
        dirs[child_dir] = Dir()
      cur_dir.add_dir(dirs[child_dir])
    elif data[0] == '$':
      if data[1] == 'cd':
        if data[2] == '..':
          pos = pwd.rfind('/', 0, len(pwd)-1)
          pwd = pwd[:pos+1]
        else:
          pwd += data[2] + '/'
      break
    else:
      cur_dir.add_file((data[1], int(data[0])))


free = 70000000 - dirs['/'].calc_size()
target = 30000000 - free
least = sys.maxsize
total = 0
for key, d in dirs.items():
  size = d.calc_size()
  if size < 100000:
    total += size
  if size > target:
    if size < least:
      least = size

print('Part 1: {} Part 2: {}'.format(total, least))






















