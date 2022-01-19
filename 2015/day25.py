
import sys

# Get the value of 1, 3019
val = 1

#for i in range(2,6):
for i in range(2,3020):
  val += i
  #print('Value at 1,{} is {}'.format(i, val))    

print('Value at 1,{} is {}'.format(i, val))    

col = i
row = 2
#for i in range(0,4):
for i in range(0,3009):
  val += (col + i) 

print('value at {},{} is {}'.format(i+2,col,val))

code = 20151125
for i in range(0,val-1):
  cur = code * 252533
  code = cur % 33554393

print('The code is {}'.format(code))

