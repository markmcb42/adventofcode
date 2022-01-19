
import sys

raw_data = []
raw = dict()


def generateRaw(o2list):
  ret = dict()

  for line in o2list:
    for i in range(len(line)):
      if i not in ret:
        ret[i] = line[i]
      else:
        ret[i] = ret[i] + line[i]

  return ret


file = open('input', 'r')
for line in file:

  line = line.strip()
  raw_data.append(line)

  for i in range(len(line)):
    if i not in raw:
      raw[i] = line[i]
    else:
      raw[i] = raw[i] + line[i]
   
# Calculate gamma and epsilon
gamma = ''
epsilon = ''

for i in raw:
  count0 = raw[i].count('0')
  count1 = raw[i].count('1')

  if count0 > count1:
    gamma += '0'
    epsilon += '1'
  else:
    gamma += '1'
    epsilon += '0'

print('Gamma is {} dec {}'.format(gamma, int(gamma, 2)))
print('Epsilon is {} dec {}'.format(epsilon, int(epsilon, 2)))
print('power is {}'.format(int(gamma, 2) * int(epsilon, 2)))

o2list = raw_data
o2raw = raw
count = 0
o2val = 0

print('Original raw len {}'.format(len(o2raw[0])))
for i in range(0,12):
  count0 = o2raw[i].count('0')
  count1 = o2raw[i].count('1')

  if count0 > count1:
    print('Remove 1s from {}'.format(i))
    #print('len of original {}'.format(len(o2list)))
    o2list = [x for x in o2list if x[i] == '0']
    #print('len of new {}'.format(len(o2list)))
  else:
    print('Remove 0s from {}'.format(i))
    #print('len of original {}'.format(len(o2list)))
    o2list = [x for x in o2list if x[i] == '1']
    #print('len of new {}'.format(len(o2list)))

  o2raw = generateRaw(o2list)
  print('Element now is {}\n'.format(o2list[0]))

  if len(o2list) == 1:
    break

co2list = raw_data
co2raw = raw
co2val = 0

print('Original raw len {}'.format(len(co2raw[0])))
for i in range(0,12):
  count0 = co2raw[i].count('0')
  count1 = co2raw[i].count('1')

  if count0 > count1:
    print('Remove 0s from {}'.format(i))
    co2list = [x for x in co2list if x[i] == '1']
  else:
    print('Remove 1s from {}'.format(i))
    co2list = [x for x in co2list if x[i] == '0']

  co2raw = generateRaw(co2list)
  print('Element now is {}\n'.format(co2list[0]))

  if len(co2list) == 1:
    break

o2elem = o2list[0]
co2elem = co2list[0]
print('The final o2element is {}'.format(o2elem))
print('The final co2element is {}'.format(co2elem))
print('rating is {}'.format(int(o2elem, 2) * int(co2elem, 2)))
