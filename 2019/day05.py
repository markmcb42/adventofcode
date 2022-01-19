
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

orig = []
file = open('input05.txt', 'r')
for line in file:
  orig = [int(x) for x in line.strip().split(',')]

  parts = [2, 1]
  for part in parts:
    if part == 1:
      input_val = 1
    else:
      input_val = 5

    codes = orig.copy()
    i = 0
    while i < len(codes):
      opcode = codes[i] % 100
      modes = [0, 0, 0]
      if codes[i] > 100:
        mode_str = str(codes[i] - opcode)[::-1][2:]
        for c in range(len(mode_str)):
          modes[c] = int(mode_str[c])

      if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        val1, val2 = 0, 0
        # Get the first parameter value
        if modes[0] == 0:
          index = codes[i + 1]
          val1 = codes[index]
        else:
          val1 = codes[i + 1]

        # Get the 2nd parameter value
        if modes[1] == 0:
          index = codes[i + 2]
          val2 = codes[index]
        else:
          val2 = codes[i + 2]

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

        # Destination is always a pointer
        dest = codes[i + 3]
        codes[dest] = res
        i += 4

      elif opcode == 3:
        index = codes[i + 1]
        codes[index] = input_val
        i += 2
      elif opcode == 4:
        index = codes[i + 1]
        print(codes[index])
        i += 2

      elif opcode == 5 or opcode == 6:
        val1, val2 = 0, 0
        # Get the first parameter value
        if modes[0] == 0:
          index = codes[i + 1]
          val1 = codes[index]
        else:
          val1 = codes[i + 1]

        # Get the 2nd parameter value
        if modes[1] == 0:
          index = codes[i + 2]
          val2 = codes[index]
        else:
          val2 = codes[i + 2]

        if opcode == 5 and val1 != 0:
          i = val2
        elif opcode == 6 and val1 == 0:
          i = val2
        else:
          i += 3

      elif opcode == 99:
        break




