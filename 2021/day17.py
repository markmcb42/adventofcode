import sys
import ctypes
import bitarray
import struct
import numpy
import numpy as np

def sim(xv, yv):
  range_x = [244,303]
  range_y = [-91,-54]

  x = 0
  y = 0
  while True:
    x += xv
    y += yv

    if xv > 0:
      xv -= 1
    yv -= 1

    if range_y[0] <= y <= range_y[1] and range_x[0] <= x <= range_x[1]:
      return True

    if y < range_y[0]:
      return False

    if x > range_x[1]:
      return False

xv = 22
count = 0
for xv in range(303,20,-1):
  for yv in range(-91, 2000):
    if sim(xv,yv):
      count += 1

print('Total is {}'.format(count))






