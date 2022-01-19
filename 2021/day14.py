
import sys
from string import ascii_uppercase

def find_all(orig, key):
  start = 0
  while True:
    start = orig.find(key, start)
    if start == -1:
      return
    yield start
    start += 1

file = open('input', 'r')

poly = 'CPSSSFCFOFVFNVPKBFVN'
#poly = 'NNCB'

rules = {}
pairs = {}

for line in file:

  line = line.strip()
  data = line.split(' -> ')
  p1 = data[0][0] + data[1]
  p2 = data[1] + data[0][1]
  rules[data[0]] = (p1, p2)
  pairs[data[0]] = 0

# Get the initial pairs
for x in range(len(poly)-1):
  pair = poly[x:x+2]
  pairs[pair] += 1

last_c = poly[-1]
subs = {}
for i in range(40):

  new_pairs = {}
  for key, value in pairs.items():
    if value == 0:
      continue

    for y in rules[key]:
      if y in new_pairs:
        new_pairs[y] += value
      else:
        new_pairs[y] = value

  pairs = new_pairs

counts = {}
for key, value in pairs.items():
  if key[0] in counts:
    counts[key[0]] += value
  else:
    counts[key[0]] = value

# Add the last char
counts[last_c] += 1

total_len = 0
most = 0
least = sys.maxsize
for value in counts.values():
  total_len += value
  if value > most:
    most = value
  if value < least:
    least = value

print('Len is {} diff {}'.format(total_len, most-least))



