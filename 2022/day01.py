
import sys

file = open('input01.txt', 'r')

elves = []
food = []
for line in file:
  line = line.strip()
  if len(line) == 0:
    elves.append(food)
    food = []
  else:
    food.append(int(line))


max_cal = 0
cal_totals = []
for e in elves:
  total = 0
  for c in e:
    total += c

  cal_totals.append(total)
  if total > max_cal:
    max_cal = total

# Get top 3 totals
cal_totals.sort(reverse=True)
top_3 = 0
for i in range(3):
  top_3 += cal_totals[i]

print('Part 1: {} Part 2: {}'.format(max_cal, top_3))

