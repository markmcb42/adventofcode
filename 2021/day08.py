
import sys

digits = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
mapping = {'top': '', 'mid': '', 'bot': '', 'ul': '', 'ur': '', 'll': ''}


def check_digit(input, digit):

  ret = True
  for x in input:
    if x not in digit:
      ret = False
      break
  return ret


file = open('input08.txt', 'r')

total_p1 = 0
total = 0
for line in file:

  line = line.strip().split('|')

  input  = line[0].strip().split()
  output = line[1].strip().split()
  output.reverse()

  # Get the 1,4,7,8
  for data in input:
    if len(data) == 2:
      digits[1] = data
    elif len(data) == 4:
      digits[4] = data
    elif len(data) == 3:
      digits[7] = data
    elif len(data) == 7:
      digits[8] = data

  # find top from 1,7
  for x in digits[7]:
    if x not in digits[1]:
      mapping['top'] = x
      break

  # get digit 3 using 1
  for data in input:
    if len(data) == 5:
      if digits[1][0] in data and digits[1][1] in data:
        digits[3] = data
        input.remove(data)
        break

  # Get mid from 3, 4, and 1
  for x in digits[3]:
    if x in digits[1]:
      continue

    if x in digits[4]:
      mapping['mid'] = x    
      break

  # Determine digit 0 from 'mid'
  for data in input:
    if len(data) == 6:
      hasMid = False
      for x in data:
        if mapping['mid'] == x:
          hasMid = True
          break
      if not hasMid:
        digits[0] = data
        input.remove(data)
        break

  # Set 9 from 1
  for data in input:
    if len(data) == 6:
      if digits[1][0] in data and digits[1][1] in data:
        digits[9] = data
        input.remove(data)
        break

  # Set 6 now
  for data in input:
    if len(data) == 6:
      digits[6] = data
      input.remove(data)
      break  

  # Determine lr from 1 and 6
  for x in digits[6]:
    if x in digits[1]:
      mapping['lr'] = x
      break

  # using lr mapping, set 2 and 5
  for data in input:
    if len(data) == 5:
      if mapping['lr'] in data:
        digits[5] = data
      else:
        digits[2] = data

  # Now we have all the digits, see what the output is
  index = 0
  val = 0
  for data in output:
    digit = 0
    if len(data) == 2:
      digit = 1
      total_p1 += 1
    elif len(data) == 3:
      digit = 7
      total_p1 += 1
    elif len(data) == 4:
      digit = 4
      total_p1 += 1
    elif len(data) == 7:
      digit = 8
      total_p1 += 1

    elif len(data) == 5:
      if check_digit(data, digits[2]):
        digit = 2
      elif check_digit(data, digits[3]):
        digit = 3
      elif check_digit(data, digits[5]):
        digit = 5

    elif len(data) == 6:
      if check_digit(data, digits[0]):
        digit = 0
      elif check_digit(data, digits[6]):
        digit = 6
      elif check_digit(data, digits[9]):
        digit = 9

    val += digit * (10**index)
    index += 1 

  total += val

print('Part 1: {} Part 2: {}'.format(total_p1, total))
