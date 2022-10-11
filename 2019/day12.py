
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from math import gcd
from functools import reduce


class Planet:

  def __init__(self, x, y, z):
    self.pos_x = x
    self.pos_y = y
    self.pos_z = z

    self.vel_x = 0
    self.vel_y = 0
    self.vel_z = 0

  def update(self, other):
    if self.pos_x > other.pos_x:
      self.vel_x -= 1
    elif self.pos_x < other.pos_x:
      self.vel_x += 1

    if self.pos_y > other.pos_y:
      self.vel_y -= 1
    elif self.pos_y < other.pos_y:
      self.vel_y += 1

    if self.pos_z > other.pos_z:
      self.vel_z -= 1
    elif self.pos_z < other.pos_z:
      self.vel_z += 1

  def move(self):
    self.pos_x += self.vel_x
    self.pos_y += self.vel_y
    self.pos_z += self.vel_z

  def energy(self):
    potential = abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)
    kinetic = abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)
    return potential * kinetic


def lcm(a, b):
  return a * b // gcd(a, b)


def lcm_n(*args):
  return reduce(lcm, args)


planets = []
file = open('input12.txt', 'r')
for line in file:
  pos = line.strip().lstrip(line[0]).rstrip('>').split(',')

  vals = []
  for p in pos:
    vals.append(int(p.split('=')[1]))

  planet = Planet(vals[0], vals[1], vals[2])
  planets.append(planet)

orig = copy.deepcopy(planets)

count = 0
cycle_x = 0
cycle_y = 0
cycle_z = 0
while True:

  # Update velocities
  for i in range(len(planets)):
    for j in range(i+1, len(planets)):
      planets[i].update(planets[j])
      planets[j].update(planets[i])

  # Move planets
  for p in planets:
    p.move()

  count += 1

  # See if cycles have completed
  if cycle_x == 0:
    match = True
    for i in range(len(planets)):
      if orig[i].pos_x != planets[i].pos_x or orig[i].vel_x != planets[i].vel_x:
        match = False
        break
    if match:
      cycle_x = count

  if cycle_y == 0:
    match = True
    for i in range(len(planets)):
      if orig[i].pos_y != planets[i].pos_y or orig[i].vel_y != planets[i].vel_y:
        match = False
        break
    if match:
      cycle_y = count

  if cycle_z == 0:
    match = True
    for i in range(len(planets)):
      if orig[i].pos_z != planets[i].pos_z or orig[i].vel_z != planets[i].vel_z:
        match = False
        break
    if match:
      cycle_z = count

  if count == 1000:
    total = 0
    for p in planets:
      total += p.energy()
    print('Total is {}'.format(total))

  if count > 1000:
    if cycle_x != 0 and cycle_y != 0 and cycle_z != 0:
      print('Found cycle x {} cycle y {} cycle z {}'.format(cycle_x, cycle_y, cycle_z))
      lcm_val = lcm_n(cycle_x, cycle_y, cycle_z)
      print('Number of cycles {}'.format(lcm_val))
      break





