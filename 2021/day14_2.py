
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
poly = 'CP'
rules = {}

for line in file:

  line = line.strip()
  data = line.split(' -> ')
  rules[data[0]] = data[1]

subs = {}
for i in range(40):
  new_poly = ''
  for x in range(len(poly)-1):
    new_poly += poly[x]
    #new_poly = "".join(poly[x])
    check = poly[x:x + 2]
    if check in rules:
      #new_poly = "".join(rules[check])
      new_poly += rules[check]

  new_poly += poly[-1]
  print('Index {} len {}'.format(i,len(new_poly)))

  #print(new_poly)

  #subs = {}

   # for pos in list(find_all(poly, key)):
    #  subs[pos+1] = value


  #for c in range(len(poly)):
   # new_poly += poly[c]
    #if c+1 in subs:
     # new_poly += subs[c+1]

  poly = new_poly

poly_len = len(poly)

most = 0
least = sys.maxsize

for c in ascii_uppercase:
  num = len(list(find_all(poly, c)))
  if num == 0:
    continue

  if num > most:
    most = num
  if num < least:
    least = num

print('Len is {} diff {}'.format(len(poly), most-least))



