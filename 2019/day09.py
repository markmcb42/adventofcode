
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy


def get_index(index_, modes):
  ret = []

  for m in range(len(modes)):
    if modes[m] == 0:
      ret.append(codes[index_ + 1 + m])
    elif modes[m] == 1:
      ret.append(index_ + 1 + m)
    else:
      ret.append(rel_base + codes[index_ + 1 + m])

  return ret


orig = []
file = open('input09.txt', 'r')
for line in file:
  orig = [int(x) for x in line.strip().split(',')]

  parts = [1,2]
  for part in parts:
    if part == 1:
      input_val = 1
    else:
      input_val = 2

    codes = orig.copy()
    zeros = [0] * 10000
    codes.extend(zeros)
    i = 0
    rel_base = 0

    while i < len(codes):
      cur_code = codes[i]

      opcode = codes[i] % 100
      modes = [0, 0, 0]
      if codes[i] > 100:
        mode_str = str(codes[i] - opcode)[::-1][2:]
        for c in range(len(mode_str)):
          modes[c] = int(mode_str[c])

      ptrs = get_index(i, modes)

      if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:

        val1 = codes[ptrs[0]]
        val2 = codes[ptrs[1]]

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
        codes[ptrs[2]] = res
        i += 4

      elif opcode == 9:
        rel_base += codes[ptrs[0]]
        i += 2

      elif opcode == 3:
        codes[ptrs[0]] = input_val
        i += 2

      elif opcode == 4:
        print(codes[ptrs[0]])
        i += 2

      elif opcode == 5 or opcode == 6:
        val1 = codes[ptrs[0]]
        val2 = codes[ptrs[1]]

        if opcode == 5 and val1 != 0:
          i = val2
        elif opcode == 6 and val1 == 0:
          i = val2
        else:
          i += 3

      elif opcode == 99:
        break