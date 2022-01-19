
import sys
import numpy as np
from itertools import permutations

input = '3113322113'
for i in range(50):

  line = ''
  prev = input[0]
  print(prev)
  count = 1
  for j in range(1, len(input)):
     
    # If this char is different from prev, update line
    if input[j] != prev: 
      line += str(count)
      line += prev
      prev = input[j]
      count = 1
    else:
      count += 1

  # Addthe last value
  line += str(count)
  line += prev

  input = line

  print('Next line len is {}'.format(len(line)))
