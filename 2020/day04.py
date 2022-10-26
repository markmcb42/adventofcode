
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


passports = []
file = open('input04.txt', 'r')
passport = []
for line in file:
  line = line.strip()
  if len(line) == 0:
    passports.append(passport)
    passport = []
    continue

  items = line.split()
  for i in items:
    passport.append(i)

valid = []
count = 0
for p in passports:
  if len(p) == 8:
    count += 1
    valid.append(p)
  elif len(p) == 7:
    hasCid = False
    for field in p:
      if 'cid' in field:
        hasCid = True
        break
    if not hasCid:
      count += 1
      valid.append(p)

print(count)

count = 0
for p in valid:
  isValid = True
  for f in p:
    data = f.split(':')
    if 'byr' in data[0]:
      yr = int(data[1])
      if yr < 1920 or yr > 2002:
        isValid = False
        break
    elif 'iyr' in data[0]:
      yr = int(data[1])
      if yr < 2010 or yr > 2020:
        isValid = False
        break
    elif 'eyr' in data[0]:
      yr = int(data[1])
      if yr < 2020 or yr > 2030:
        isValid = False
        break
    elif 'hgt' in data[0]:
      if not('cm' in data[1] or 'in' in data[1]):
        isValid = False
        break
      hgt = int(data[1][:-2])
      if 'cm' in data[1]:
        if hgt < 150 or hgt > 193:
          isValid = False
          break
      else:
        if hgt < 59 or hgt > 76:
          isValid = False
          break
    elif 'hcl' in data[0]:
      if len(data[1]) != 7:
        isValid = False
        break
      if data[1][0] != '#':
        isValid = False
        break
      for c in data[1][1:]:
        if c.isnumeric():
          continue
        val = ord(c)
        if val < 97 or val > 102:
          isValid = False
          break
    elif 'ecl' in data[0]:
      if not ('amb' in data[1] or 'blu' in data[1] or 'brn' in data[1] or
              'gry' in data[1] or 'grn' in data[1] or 'hzl' in data[1] or
              'oth' in data[1]):
        isValid = False
        break
    elif 'pid' in data[0]:
      if len(data[1]) != 9 or not data[1].isnumeric():
        isValid = False
        break

  if isValid:
    count += 1

print(count)




