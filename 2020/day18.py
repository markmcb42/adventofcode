
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

# Calculate the value of the expression
def calc(data):
  val = 0
  op = '.'
  for d in data:
    if d.isnumeric():
      if op == '.':
        val = int(d)
      elif op == '*':
        val *= int(d)
      elif op == '+':
        val += int(d)
    else:
      op = d

  return val

# Calculate with precedence
def precedence(data):

  while '+' in data:
    # Find the location of +
    for i in range(len(data) - 1):
      if data[i] == '+':
        break
    val = int(data[i-1]) + int(data[i+1])
    new_data = data[:i-1]
    new_data.append(str(val))
    new_data.extend(data[i+2:])
    data = new_data

  val = calc(data)
  return val

# Replace the parens with the value contained inside it
def reduce(line, pos, is_p1):

  lpos = line[:pos].rfind('(')
  exp = line[lpos+1:pos]
  data = exp.split()
  if is_p1:
    val = calc(data)
  else:
    val = precedence(data)
  ret_line = line[:lpos] + str(val) + line[pos+1:]

  return ret_line


lines = []
file = open('input18.txt', 'r')
for line in file:
  line = line.strip()
  lines.append(line)

p1_total = 0
p2_total = 0

for line in lines:
  reduced = False
  while not reduced:
    pos = line.find(')')
    if pos != -1:
      line = reduce(line, pos, True)
    else:
      reduced = True

  data = line.split()
  cur = calc(data)
  p1_total += cur

p2_total = 0
for line in lines:
  reduced = False
  while not reduced:
    pos = line.find(')')
    if pos != -1:
      line = reduce(line, pos, False)
    else:
      reduced = True
  data = line.split()
  cur = precedence(data)
  p2_total += cur

print(p1_total, p2_total)
