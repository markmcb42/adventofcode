
import sys

file = open('input', 'r')
ins = []
for line in file:
  ins.append(line.strip())

cur = '5'
for i in ins:
  for c in i:
    if c == 'D':
      if cur == '1':
        cur = '3'
      elif cur == '2' or cur == '3' or cur == '4':
        cur = str(int(cur) + 4)
      elif cur == '6' or cur == '7' or cur == '8':
        cur = chr(ord(cur) + 11)
      elif cur == 'B':
        cur = 'D'

    elif c == 'U':
      if cur == 'D':
        cur = 'B'
      elif cur == 'A' or cur == 'B' or cur == 'C':
        cur = chr(ord(cur) - 11)
      elif cur == '6' or cur == '7' or cur == '8':
        cur = str(int(cur) - 4)
      elif cur == '3':
        cur = '1'

    elif c == 'R':
      if cur not in ['1', '4', '9', 'C', 'D']:
        cur = chr(ord(cur) + 1)

    elif c == 'L':
      if cur not in ['1', '2', '5', 'A', 'D']:
        cur = chr(ord(cur) - 1)
    
  print(cur)



