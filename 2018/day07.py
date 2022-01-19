
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy


class Task:
  def __init__(self, name):
    self.name = name
    self.req = []
    self.time = ord(name) - 4
    self.running = False
    self.done = False

  def is_ready(self, tasks):
    if self.done or self.running:
      return False

    ready = True
    for r in self.req:
      if r not in tasks:
        ready = False
        break
    return ready

  def start(self):
    self.running = True

  def advance(self):
    if self.running:
      self.time -= 1
      if self.time == 0:
        self.done = True
        self.running = False

  def is_done(self):
    return self.done


tasks = {}

file = open('input.txt', 'r')
for line in file:
  data = line.strip().split()
  if data[7] not in tasks:
    tasks[data[7]] = Task(data[7])
  if data[1] not in tasks:
    tasks[data[1]] = Task(data[1])

  tasks[data[7]].req.append(data[1])

orig_tasks = copy.deepcopy(tasks)

order = ''
while len(tasks) > 0:
  possible = []
  for t in tasks.values():
    if t.is_ready(order):
      possible.append(t.name)

  possible.sort()
  order += possible[0]
  tasks.pop(possible[0])

print(order)

order = ''
workers = []
time = 0
tasks = orig_tasks

while len(tasks) > 0:
  # Get next tasks that are ready
  possible = []
  for t in tasks.values():
    if t.is_ready(order):
      possible.append(t.name)

  possible.sort()
  for p in possible:
    if len(workers) < 5:
      tasks[p].start()
      workers.append(p)

  workers.sort()
  completed = False
  while not completed:
    time += 1
    #print(workers)
    for w in workers:
      tasks[w].advance()
      if tasks[w].is_done():
        completed = True
        order += w

    if completed:
      for key, value in tasks.items():
        if value.is_done():
          if key in workers:
            workers.remove(key)

  if len(order) == len(tasks):
    break

print(time)











