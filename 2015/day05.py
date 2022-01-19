
import sys

file = open('input', 'r')

total = 0
for line in file:

  if 'ab' in line:
    continue
  if 'cd' in line:
    continue
  if 'pq' in line:
    continue
  if 'xy' in line:
    continue

  vowels = 0;
  hasDouble = False
  prev = 'A'
  for c in line:
    if (c == 'a') or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u'):
      vowels += 1

    if prev == c:
      hasDouble = True

    prev = c

  if (vowels >= 3) and hasDouble:
    total += 1

print('There are {} nice names'.format(total))
