
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from blist import blist

max_players = 403
marble = 7192000
#max_players = 13
#marble = 7999
field = [0]

players = {p: 0 for p in list(range(1, max_players+1))}
pos = 0
cur = 0
for i in range(1,marble+1):
  cur += 1
  if cur == max_players + 1:
    cur = 1

  if i % 23 == 0:
    players[cur] += i
    pos -= 7
    if pos < 0:
      pos += len(field)
    players[cur] += field[pos]
    field.pop(pos)
    continue

  pos += 2
  if pos > len(field):
    pos = 1
  field.insert(pos, i)

high = 0
for key, value in players.items():
  if value > high:
    high = value

print(high)

















