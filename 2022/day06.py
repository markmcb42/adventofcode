
import sys
from parse import *
import copy


file = open('input06.txt', 'r')

line = file.readline()

for i in range(0, len(line)):
  test = line[i:i+4]
  if len(set(test)) == len(test):
    print('Part 1: {}'.format(i+4))
    break

for i in range(0, len(line)):
  test = line[i:i+14]
  if len(set(test)) == len(test):
    print('Part 2: {}'.format(i+14))
    break













