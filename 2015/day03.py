
import sys

file = open('input', 'r')

total = 0
sx = 0
sy = 0

isSanta = True
rx = 0
ry = 0

curx = 0
cury = 0

houses = []
house = (curx, cury)
houses.append(house)

for line in file:
  for char in line:

    if isSanta:
      curx = sx
      cury = sy
    else:
      curx = rx
      cury = ry

    if char == '^':
      cury += 1
      house = (curx, cury)
      if house not in houses:
        houses.append(house)
      
    if char == 'v':
      cury -= 1
      house = (curx, cury)
      if house not in houses:
        houses.append(house)

    if char == '>':
      curx += 1
      house = (curx, cury)
      if house not in houses:
        houses.append(house)

    if char == '<':
      curx -= 1
      house = (curx, cury)
      if house not in houses:
        houses.append(house)

    if isSanta:
      sx = curx
      sy = cury
    else:
      rx = curx
      ry = cury

    isSanta = not isSanta

print('Santa visited {} houses'.format(len(houses)))
