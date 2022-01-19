
import sys

file = open('input', 'r')

line = file.readline().strip()
#line = '3,4,3,1,2'
data = line.split(',')

print(data)

fish = []

for x in data:
  fish.append(int(x))

print('number of fish is {}'.format(len(fish)))

for i in range(256):
 
  count = 0
  for x in range(len(fish)):
    if fish[x] == 0:
      fish[x] = 6
      count += 1
    else:
      fish[x] -= 1

  for j in range(count):
    fish.append(8)

  if i % 3 == 0:
    print(i)
print('There are {} fish'.format(len(fish)))

