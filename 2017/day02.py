
import sys

count = 0
file = open('input.txt', 'r')
for line in file:
  data = [int(i) for i in line.strip().split()]
  data.sort(reverse=True)
  for i in range(len(data) - 1):
    for j in range(i+1, len(data)):
      if data[i] % data[j] == 0:
        count += int(data[i] / data[j])

print(count)




