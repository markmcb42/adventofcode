
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
  def __init__(self, cards, bid, hand_type):
    self.cards = cards
    self.bid = bid
    self.type = hand_type


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
  if item1.type < item2.type:
    return -1
  if item1.type > item2.type:
    return 1

  for i in range(len(item1.cards)):
    rank1 = card_ranks[item1.cards[i]]
    rank2 = card_ranks[item2.cards[i]]
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
  hand = CamelHand(data[0], int(data[1]), rank)
  hands.append(hand)

sorted_hands = sorted(hands, key=cmp_to_key(lambda item1, item2: compare(item1, item2)))

count = 1
total = 0
for h in sorted_hands:
  total += h.bid * count
  count += 1

print('part 1:{}'.format(total))

card_ranks['J'] = 0
# Find the best hand if there is a 'J' in it
for h in hands:
  if 'J' not in h.cards:
    continue

  num_j = Counter(h.cards)['J']

  # If all the letters are j, can't be improved
  if num_j == 5:
    continue

  if num_j == 1:
    if h.type == HandType.HIGH_CARD:
      h.type = HandType.ONE_PAIR
    elif  h.type == HandType.ONE_PAIR:
      h.type = HandType.THREE_OF_KIND
    elif h.type == HandType.TWO_PAIR:
      h.type = HandType.FULL_HOUSE
    elif h.type == HandType.THREE_OF_KIND or h.type == HandType.FULL_HOUSE:
      h.type = HandType.FOUR_OF_KIND
    elif h.type == HandType.FOUR_OF_KIND:
      h.type = HandType.FIVE_OF_KIND
  elif num_j == 2:
    if h.type == HandType.ONE_PAIR:
      h.type = HandType.THREE_OF_KIND
    elif h.type == HandType.TWO_PAIR:
      h.type = HandType.FOUR_OF_KIND
    elif h.type == HandType.FULL_HOUSE:
      h.type = HandType.FIVE_OF_KIND
  elif num_j == 3:
    if h.type == HandType.THREE_OF_KIND:
      h.type = HandType.FOUR_OF_KIND
    elif h.type == HandType.FULL_HOUSE:
      h.type = HandType.FIVE_OF_KIND
  elif num_j == 4:
    h.type = HandType.FIVE_OF_KIND

sorted_hands = sorted(hands, key=cmp_to_key(lambda item1, item2: compare(item1, item2)))

count = 1
total = 0
for h in sorted_hands:
  total += h.bid * count
  count += 1

print('part 2:{}'.format(total))