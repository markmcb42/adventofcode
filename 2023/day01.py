
import sys
import re


def get_digits(line):

  mapping = {'one' : 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
             'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
  pos_list = []
  for k, v in mapping.items():
    m = re.finditer(k, line)
    for i in m:
      pos_list.append((v, i.span()[0]))

  pattern = '[0-9]'
  m = re.finditer(pattern, line)
  for i in m:
    pos_list.append((int(i.group()), i.span()[0]))

  vals = []
  pos_list = sorted(pos_list, key=lambda x: x[1])
  for v in pos_list:
    vals.append(v[0])
  return vals


file = open('input01.txt', 'r')

values = []
p2_vals = []

for line in file:
  line = line.strip()
  value = ''
  for c in line:
    if c.isdigit():
      value += c
      break

  for c in reversed(line):
    if c.isdigit():
      value += c
      break

  if len(value) > 0:
    values.append(int(value))

  digits = get_digits(line)
  val = 10 * digits[0] + digits[-1]
  p2_vals.append(val)


print('Part 1: {}  Part 2: {}'.format(sum(values), sum(p2_vals)))






