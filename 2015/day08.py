
import sys
import numpy as np

file = open('input', 'r')

raw = 0
total = 0

for line in file:

  line = line.strip()
  orig = len(line)
  raw += orig

  newline = ''
  for char in line:
    if char == '\\':
      newline += '\\'
    elif char == '"':
      newline += '\\'

    newline += char

  # add double quotes back
  newline = '"' + newline +'"'

  print('Orig {} len {} \nNew {} len {}\n'.format(line, orig, newline, len(newline)))

  total += len(newline)

print('Raw chars {} encoded {} diff {}'.format(raw, total, (total - raw)))
