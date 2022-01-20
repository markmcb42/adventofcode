import copy
import sys
import time
from collections import Counter
from collections import deque
import hashlib

import numpy as np


class Particle:
  def __init__(self, p, v, a, pid):
    self.id = pid
    self.p = p
    self.v = v
    self.a = a
    self.dist = 0

  def __eq__(self, other):
    for i in range(len(self.p)):
      if self.p[i] != other.p[i]:
        return False
    return True

  def __hash__(self):
    return hash(repr(self))

  def update(self):
    for i in range(len(self.a)):
      self.v[i] += self.a[i]
      self.p[i] += self.v[i]
    self.set_dist()

  def set_dist(self):
    self.dist = 0
    for p in self.p:
      self.dist += abs(p)

orig = []
index = 0
file = open('input20.txt', 'r')
for line in file:
  line = line.strip()

  start = line.find('<')
  end = line.find('>', start)
  data = line[start+1:end]
  p = [int(x) for x in data.split(',')]

  start = line.find('<', end)
  end = line.find('>', start)
  data = line[start+1:end]
  v = [int(x) for x in data.split(',')]

  start = line.find('<', end)
  end = line.find('>', start)
  data = line[start+1:end]
  a = [int(x) for x in data.split(',')]

  part = Particle(p, v, a, index)
  orig.append(part)
  index += 1

count = 0
cur_low = 0
particles = copy.deepcopy(orig)

while True:
  if count == 200:
    break

  for p in particles:
    p.update()

  particles.sort(key=lambda x: x.dist)
  low = particles[0].id
  if low == cur_low:
    count += 1
  else:
    cur_low = low
    count = 1

print(cur_low)

# Part 2
particles = copy.deepcopy(orig)
count = 0
length = 0
while True:
  if count == 100 or length == 1:
    break

  for p in particles:
    p.update()

  collisions = set()
  for i in range(len(particles) - 1):
    for j in range(i + 1, len(particles)):
      if particles[i] == particles[j]:
        collisions.add(particles[i])
        collisions.add(particles[j])

  for c in collisions:
    particles.remove(c)

  if length == len(particles):
    count += 1
  else:
    length = len(particles)
    count = 1

print(length)





