
import sys

file = open('input', 'r')

windowLens = []
curWindow = []

for line in file:

  curWindow.append(int(line))
  if len(curWindow) < 3:
    continue

  curWindow = curWindow[-3:]
  sum = 0
  for i in curWindow:
    sum = sum + i
    
  windowLens.append(sum)

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

print('Increased {} times'.format(count))
