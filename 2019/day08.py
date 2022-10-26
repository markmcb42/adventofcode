
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

layers = []
width = 25
height = 6
buffer = ''

file = open('input08.txt', 'r')
for line in file:
  data = line.strip()
  layers = list(map(''.join, zip(*[iter(data)]*(width*height))))

min = width * height
layer = ''
for l in layers:
  count = l.count('0')
  if count < min:
    min = count
    layer = l

ones = layer.count('1')
twos = layer.count('2')
print(ones*twos)

image = ''
# determine visible pixels
for i in range(len(layer)):
  for l in layers:
    if l[i] == '2':
      continue
    else:
      image += l[i]
      break

# print the image
for i in range(0, len(image), width ):
  print(image[i:i+width])















