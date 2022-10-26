
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter

max_seat_id = 0
seat_ids = []
file = open('input05.txt', 'r')
for line in file:
  line = line.strip()
  row = line[:7]
  seat = line[7:]

  cur = (0, 127)
  for c in row:
    diff = ((cur[1] - cur[0]) + 1) // 2
    if c == 'F':
      cur = (cur[0], cur[1] - diff)
    else:
      cur = (cur[0] + diff, cur[1])
  row = cur[0]

  cur = (0, 7)
  for c in seat:
    diff = ((cur[1] - cur[0]) + 1) // 2
    if c == 'L':
      cur = (cur[0], cur[1] - diff)
    else:
      cur = (cur[0] + diff, cur[1])

  seat = cur[0]
  seat_id = (row * 8) + seat
  seat_ids.append(seat_id)
  if seat_id > max_seat_id:
    max_seat_id = seat_id

print(max_seat_id)

seat_ids.sort()
for i in range(len(seat_ids)-1):
  if seat_ids[i+1] - seat_ids[i] == 2:
    print(seat_ids[i] + 1)
    break




