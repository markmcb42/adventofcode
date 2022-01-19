
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc


file = open('input.txt', 'r')
for line in file:
  orig = line.strip()

lowest = len(orig)

for l, u in zip(lc, uc):
  line = orig.replace(l, '')
  line = line.replace(u, '')
  cur = len(line)
  found = True
  while found:
    found = False
    newline = ''
    i = 0
    while i < len(line):
      if i + 1 == len(line):
        newline += line[i]
        break

      c = line[i]
      if abs(ord(line[i]) - ord(line[i+1])) == 32:
        i += 2
        found = True
      else:
        newline += line[i]
        i += 1

    line = newline

  if len(line) < lowest:
    lowest = len(line)

print(lowest)







