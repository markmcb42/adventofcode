
import sys

import numpy
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


#card_pk = 5764801
card_pk = 9789649
card_loop = 0
#door_pk = 17807724
door_pk = 3647239
door_loop = 0
subject = 8

value = 1
card_loop = 1
while pow(7, card_loop, 20201227) != card_pk:
  card_loop += 1

door_loop = 1
while pow(7, door_loop, 20201227) != door_pk:
  door_loop += 1

subject = door_pk
door_val = 1
for i in range(card_loop):
  door_val *= subject
  door_val = door_val % 20201227

print('Part 1: {}'.format(door_val))




