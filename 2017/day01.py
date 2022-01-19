
import sys

count = 0
file = open('input.txt', 'r')
dirs = []
for line in file:
  line = line.strip()

dist = int(len(line)/2)
wrap = 0
for i in range(len(line)):
  if i + dist >= len(line):
    if line[i] == line[wrap]:
      count += int(line[i])
    wrap += 1
  else:
    if line[i] == line[i+dist]:
      count += int(line[i])

print(count)

