
import sys

file = open('input01.txt', 'r')

windowLens = []
curWindow = []
cur = 0
count = 0
for line in file:

  val = int(line.strip())
  if cur != 0:
    if val > cur:
      count += 1

  cur = val

  curWindow.append(val)
  if len(curWindow) < 3:
    continue

  curWindow = curWindow[-3:]
  sum = 0
  for i in curWindow:
    sum = sum + i
    
  windowLens.append(sum)

print('Part 1: {}'.format(count))

count = 0
cur = 0
prev = 0

for i in windowLens:

  if cur == 0:
    cur = i
  else:
    prev = cur
    cur = i

    if cur > prev:
      count += 1

print('Part 2: {}'.format(count))
