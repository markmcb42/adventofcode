
import sys

import numpy
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


def play_sub_game(p1, p2):
  p1_prev = []
  p2_prev = []

  cur_p1 = copy.deepcopy(p1)
  cur_p2 = copy.deepcopy(p2)
  winner = 0
  done = False

  while not done:
    if cur_p1 in p1_prev and cur_p2 in p2_prev:
      return 1

    p1_prev.append(copy.deepcopy(cur_p1))
    p2_prev.append(copy.deepcopy(cur_p2))

    p1_card = cur_p1.pop(0)
    p2_card = cur_p2.pop(0)

    # See if a sub-game should be played
    if p1_card <= len(cur_p1) and p2_card <= len(cur_p2):
      winner = play_sub_game(cur_p1[:p1_card], cur_p2[:p2_card])
    else:
      if p1_card > p2_card:
        winner = 1
      else:
        winner = 2

    if winner == 1:
      cur_p1.append(p1_card)
      cur_p1.append(p2_card)
    else:
      cur_p2.append(p2_card)
      cur_p2.append(p1_card)

    if len(cur_p2) == 0:
      winner = 1
      done = True

    if len(cur_p1) == 0:
      winner = 2
      done = True

  return winner


file = open('input22.txt', 'r')
players = {}

get_cards = False
cur_player = 0

for line in file:
  line = line.strip()
  if len(line) == 0:
    get_cards = False
    cur_player = 0
    continue

  if 'Player' in line:
    line = line.replace('Player ', '')
    cur_player = int(line[:-1])
    players[cur_player] = []
  else:
    players[cur_player].append(int(line))

total_cards = 0
for deck in players.values():
  total_cards += len(deck)

orig_players = copy.deepcopy(players)

rounds = 0
done = False
winner = 0
while not done:
  rounds += 1
  p1_card = players[1].pop(0)
  p2_card = players[2].pop(0)

  if p1_card > p2_card:
    players[1].append(p1_card)
    players[1].append(p2_card)
  else:
    players[2].append(p2_card)
    players[2].append(p1_card)

  for p, deck in players.items():
    if len(deck) == total_cards:
      winner = p
      done = True
      break

total = 0
cur_tot_cards = total_cards
for c in players[winner]:
  total += (c * cur_tot_cards)
  cur_tot_cards -= 1

print('Part 1: {}'.format(total))

players = copy.deepcopy(orig_players)

rounds = 0
done = False
winner = 0
while not done:
  rounds += 1
  p1_card = players[1].pop(0)
  p2_card = players[2].pop(0)

  # See if a sub-game should be played
  if p1_card <= len(players[1]) and p2_card <= len(players[2]):
    winner = play_sub_game(players[1][:p1_card], players[2][:p2_card])
  else:
    if p1_card > p2_card:
      winner = 1
    else:
      winner = 2

  if winner == 1:
    players[1].append(p1_card)
    players[1].append(p2_card)
  else:
    players[2].append(p2_card)
    players[2].append(p1_card)

  for p, deck in players.items():
    if len(deck) == total_cards:
      winner = p
      done = True
      break

total = 0
for c in players[winner]:
  total += (c * total_cards)
  total_cards -= 1

print('Part 2: {}'.format(total))
