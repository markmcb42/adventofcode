
import sys
import re
from collections import Counter
from enum import Enum

from functools import cmp_to_key

card_ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 15}


class HandType(Enum):
  HIGH_CARD = 1
  ONE_PAIR = 2
  TWO_PAIR = 3
  THREE_OF_KIND = 4
  FULL_HOUSE = 5
  FOUR_OF_KIND = 6
  FIVE_OF_KIND = 7

  def __lt__(self, other):
    if self.__class__ is other.__class__:
      return self.value < other.value
    return NotImplemented


class CamelHand:
  def __init__(self, cards, bid, type) :
    self.cards = cards
    self.bid = bid
    self.type = type


# Determine type of hand
def get_hand_type(hand):
  counter = Counter(hand)

  if len(counter) == 1:
    return HandType.FIVE_OF_KIND

  if len(counter) == 5:
    return HandType.HIGH_CARD

  if len(counter) == 3:
    for val in counter.values():
      if val == 3:
        return HandType.THREE_OF_KIND
    return HandType.TWO_PAIR

  if len(counter) == 4:
    return HandType.ONE_PAIR

  if len(counter) == 2:
    for val in counter.values():
      if val == 4:
        return HandType.FOUR_OF_KIND
    return HandType.FULL_HOUSE


# Return -1 if item2 is greater, 1 if item1 is greater
def compare(item1, item2):
  if item1[2] < item2[2]:
    return -1
  if item1[2] > item2[2]:
    return 1

  for i in range(len(item1[0])):
    rank1 = card_ranks[item1[0][i]]
    rank2 = card_ranks[item2[0][i]]
    if rank1 == rank2:
      continue
    if rank1 < rank2:
      return -1
    if rank1 > rank2:
      return 1


file = open('input07.txt', 'r')

hands = []

for line in file:
  data = line.strip().split()

  rank = get_hand_type(data[0])
  hands.append( (data[0], int(data[1]), rank))

sorted_hands = sorted(hands, key=cmp_to_key(lambda item1, item2: compare(item1, item2)))

count = 1
total = 0
for h in sorted_hands:
  total += h[1] * count
  count += 1

print('part 1:{}'.format(total))

card_ranks['J'] = 0
# Find the best hand if there is a 'J' in it
del_items = []
add_items = []
for h in hands:
  if 'J' not in h[0]:
    continue

  num_j = Counter(h[0])['J']

  # If all the letters are j, can't be improved
  if num_j == 5:
    continue

  # Remove this from the list
  del_items.append(h)

  cur_type = get_hand_type(h[0])

  if num_j == 1:
    if h[2] == HandType.HIGH_CARD:
      add_items.append((h[0], h[1], HandType.ONE_PAIR))
    elif  h[2] == HandType.ONE_PAIR:
      add_items.append((h[0], h[1], HandType.THREE_OF_KIND))
    elif h[2] == HandType.TWO_PAIR:
      add_items.append((h[0], h[1], HandType.FULL_HOUSE))
    elif h[2] == HandType.THREE_OF_KIND or h[2] == HandType.FULL_HOUSE:
      add_items.append((h[0], h[1], HandType.FOUR_OF_KIND))
    elif h[2] == HandType.FOUR_OF_KIND:
      add_items.append((h[0], h[1], HandType.FIVE_OF_KIND))
    else:
      print('Error with {}'.format(h[0]))
  elif num_j == 2:
    if h[2] == HandType.ONE_PAIR:
      add_items.append((h[0], h[1], HandType.THREE_OF_KIND))
    elif h[2] == HandType.TWO_PAIR:
      add_items.append((h[0], h[1], HandType.FOUR_OF_KIND))
    elif h[2] == HandType.FULL_HOUSE:
      add_items.append((h[0], h[1], HandType.FIVE_OF_KIND))
    else:
      print('Error with {}'.format(h[0]))
  elif num_j == 3:
    if h[2] == HandType.THREE_OF_KIND:
      add_items.append((h[0], h[1], HandType.FOUR_OF_KIND))
    elif h[2] == HandType.FULL_HOUSE:
      add_items.append((h[0], h[1], HandType.FIVE_OF_KIND))
    else:
      print('Error with {}'.format(h[0]))
  elif num_j == 4:
    add_items.append((h[0], h[1], HandType.FIVE_OF_KIND))

# Remove the updated hands
for h in del_items:
  hands.remove(h)

# Add new hands
for h in add_items:
  hands.append(h)

sorted_hands = sorted(hands, key=cmp_to_key(lambda item1, item2: compare(item1, item2)))

count = 1
total = 0
for h in sorted_hands:
  total += h[1] * count
  count += 1

print('part 2:{}'.format(total))