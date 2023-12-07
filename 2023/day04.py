
import sys
import re

class Card:
  def __init__(self, number, count, matches):
    self.number = number
    self.count = count
    self.matches = matches

file = open('input04.txt', 'r')

cards = {}

total = 0
for line in file:
  line = line.strip()
  data = line.split(':')
  test = re.split(r'\s{1,}', data[0])
  num = int(test[1])

  winning = [int(x) for x in data[1].strip().split('|')[0].split()]
  numbers = [int(x) for x in data[1].strip().split('|')[1].split()]

  points = 0
  count = 0
  for n in winning:
    if n in numbers:
      count += 1
      if points == 0:
       points = 1
      else:
        points *= 2

  card = Card(num, 1, count)
  cards[num] = card
  total += points

print('Part 1: {}'.format(total))

for key, val in cards.items():
  for i in range(1, val.count + 1):
    for j in range(1, val.matches + 1):
      cur = key + j
      cards[cur].count += 1

total = 0
for key, val in cards.items():
  total += val.count

print('Part 2: {}'.format(total))







