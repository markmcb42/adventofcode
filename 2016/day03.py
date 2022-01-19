
import sys

file = open('input', 'r')
count = 0
col = {}
col[0] = []
col[1] = []
col[2] = []

for line in file:
  data = line.strip().split()

  for i in range(len(data)):
    col[i].append(int(data[i].strip()))

index = 0
for key in col.keys():
  index = 0
  while index < len(col[key]):
    tri = [col[key][index], col[key][index+1], col[key][index+2]]
    tri.sort()
    if tri[0] + tri[1] > tri[2]:
      count += 1
    index += 3

print(count)




