
import sys
import numpy as np

wires = dict()
vals = dict()

def checkSingle(index, elems):

  if elems[0].isnumeric():
    value = np.uint16(elems[0])
    vals[index] = value
  else:
    if elems[0] in vals:
      vals[index] = vals[elems[0]]

def checkNot(index, elems):

  if elems[1] in vals:
    print('Found value for {}'.format(elems[1]))
    value = vals[elems[1]]
    value = ~value
    vals[index] = value 

def checkBinaryOp(index, elems):

  if 'd' == index:
    print('d is {}'.format(elems))

  lh = 0
  rh = 0
  if elems[0].isnumeric():
    lh = np.uint16(elems[0])
  elif elems[0]  in vals:
    lh = vals[elems[0]]
  else:
    return

  if elems[2].isnumeric():
    rh = np.uint16(elems[2])
  elif elems[2] in vals:
    rh = vals[elems[2]]
  else:
    return

  if 'LSHIFT' in elems[1]:
    print(index, elems)
    vals[index] = lh << rh
  if 'RSHIFT' in elems[1]:
    print(index, elems)
    vals[index] = lh >> rh
  if 'OR' in elems[1]:
    print(index, elems)
    vals[index] = lh | rh
  if 'AND' in elems[1]:
    print(index, elems)
    vals[index] = lh & rh


def evaluate(index, str):

  #print(str)
  elems = str.split(' ')
  if len(elems) == 1:
    checkSingle(index, elems)

  elif len(elems) == 2:
    checkNot(index, elems)

  elif len(elems) == 3:
    checkBinaryOp(index, elems)

  else:
    print('Failed len check')
    sys.exit()
  

file = open('input', 'r')


for line in file:

  data = line.split(' -> ')
  wires[data[1].strip()] = data[0]

count = 0
while True:

  if 'a' in vals:
    print(vals['a'])
    break

  for key in sorted(wires):
    if key not in vals:
      #print('Found val {} for {}'.format(vals[key], key));
    #else:
      print('Evaluate {}'.format(key))
      evaluate(key, wires[key])
  count += 1

  #if count == 3:
  #  vals['a'] = 4

