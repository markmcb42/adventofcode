
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy


class Node:
  def __init__(self):
    self.childs = []
    self.meta = []

  def meta_sum(self):
    total = 0
    for c in self.childs:
      total += c.meta_sum()
    for m in self.meta:
      total += m
    return total

  def root_val(self):
    total = 0
    if len(self.childs) == 0:
      for m in self.meta:
        total += m
    else:
      for m in self.meta:
        if m <= len(self.childs):
          total += self.childs[m-1].root_val()
    return total


def create_node(data, pos):
  # Get the header
  num_child = data[pos]
  pos += 1
  num_meta = data[pos]
  pos += 1
  node = Node()
  for _ in range(num_child):
    pos, n = create_node(data, pos)
    node.childs.append(n)
  for _ in range(num_meta):
    node.meta.append(data[pos])
    pos += 1
  return pos, node


file = open('input.txt', 'r')
for line in file:
  data = [int(x) for x in line.strip().split()]

i = 0
i, node = create_node(data, i)

print(node.meta_sum(), node.root_val())

















