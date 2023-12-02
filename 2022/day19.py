
import sys
#from parse import *
import copy
from enum import Enum
#import gmpy2
#from gmpy2 import mpz
import collections
import functools
import numpy as np
import time
import itertools as it


class Material(Enum):
  ORE = 1
  CLAY = 2
  OBSIDIAN = 3
  GEODE = 4


class Factory:
  def __init__(self):
    self.materials = {Material.ORE: 0, Material.CLAY: 0,
                      Material.OBSIDIAN: 0, Material.GEODE: 0}
    self.robots = {Material.ORE: 1, Material.CLAY: 0,
                   Material.OBSIDIAN: 0, Material.GEODE: 0}
    self.costs = {Material.ORE: [], Material.CLAY: [],
                  Material.OBSIDIAN: [], Material.GEODE: []}

  def get_actions(self):
    actions = []
    for key, item in self.costs.items():
      can_create = True
      for i in item:
        if self.materials[i[0]] < i[1]:
          can_create = False
          break
      if can_create:
        actions.append(key)
    return actions

  def generate(self):
    for key, item in self.robots.items():
      self.materials[key] += item

class Blueprint:
  def __init__(self):
    self.costs = {Material.ORE: [], Material.CLAY: [],
                  Material.OBSIDIAN: [], Material.GEODE: []}

bps = {}
file = open('input19.txt', 'r')
for line in file:
  data = line.strip().split(':')
  num = int(data[0].split()[1])
  data = data[1].split('.')
  bp = Blueprint()
  for d in data:
    items = d.strip().split()
    if len(items) == 0:
      continue

    if items[1] == 'ore':
      bp.costs[Material.ORE].append([Material.ORE, int(items[4])])
    elif items[1] == 'clay':
      bp.costs[Material.CLAY].append([Material.ORE, int(items[4])])
    elif items[1] == 'obsidian':
      bp.costs[Material.OBSIDIAN].append([Material.ORE, int(items[4])])
      bp.costs[Material.OBSIDIAN].append([Material.CLAY, int(items[7])])
    elif items[1] == 'geode':
      bp.costs[Material.GEODE].append([Material.ORE, int(items[4])])
      bp.costs[Material.GEODE].append([Material.OBSIDIAN, int(items[7])])
  bps[num] = bp


for key, item in bps.items():
  states = []
  f = Factory()
  f.costs = item.costs
  states.append(f)
  for i in range(24):
    for s in states:
      actions = s.get_actions()
      if len(actions) == 0:
        s.generate()





