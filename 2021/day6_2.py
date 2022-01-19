
import sys

file = open('input', 'r')

line = file.readline().strip()
#line = '3,4,3,1,2'
data = line.split(',')

#print(data)

fish = {}

for x in data:
  val = int(x)
  if val in fish:
    fish[val] += 1
  else:
    fish[val] = 1

print(fish)

for i in range(256):
 
  new_fish = {}
  for x in fish:
    if x == 0:
      new_fish[8] = fish[x]
      if 6 in new_fish:
        new_fish[6] += fish[x]
      else:
        new_fish[6] = fish[x]
    else:
      if x-1 in new_fish:
        new_fish[x-1] += fish[x]
      else:
        new_fish[x-1] = fish[x]

  fish = new_fish
  #print(fish)
    
total = 0
for i in fish:
  total += fish[i]

print('There are {} fish'.format(total))

