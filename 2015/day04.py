
import sys
import hashlib

base = 'bgvyzdsv'
count = 0

while True:

  line = base + str(count)
  res = hashlib.md5(line.encode())
  test = res.hexdigest()[0:6]
  
  if test == '000000':
    break

  count += 1

print('Positon is {}'.format(count))
