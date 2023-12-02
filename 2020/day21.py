
import sys

import numpy
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy
from collections import Counter


file = open('input21.txt', 'r')
foods = []
allergens = set()

for line in file:
  line = line.strip()
  if len(line) == 0:
    continue

  data = line.split('(')
  ingredients = data[0].strip().split(' ')
  allergies = data[1].strip().replace('contains ', '')
  allergies = allergies[:-1].split(',')
  allergies = [s.strip() for s in allergies]
  allergens.update(allergies)
  foods.append((ingredients, allergies))

# Find the frequency of each allergen
elements = []
for f in foods:
  elements.extend(f[1])
elem_count = {i: elements.count(i) for i in allergens}
elem_sorted = sorted(elem_count.items(), key=lambda x: x[1], reverse=True)

# For each allergen, get possible ingredients
allergy_map = {}
for elem in elem_sorted:
  ing_list = []
  food_count = 0
  a = elem[0]
  allergy_map[a] = []

  for f in foods:
    if a in f[1]:
      ing_list.extend(f[0])
      food_count += 1

  possible = { i:ing_list.count(i) for i in ing_list}
  for key, value in possible.items():
    if value == food_count:
      allergy_map[a].append(key)

# Reduce the allergies to single ingredients
final_map = {}

while True:
  cur_key = ''
  for key, value in allergy_map.items():
    if len(value) == 1:
      cur_key = key
      final_map[cur_key] = value[0]
      break

  # Remove this key from allergy_map
  del(allergy_map[cur_key])

  # if the allergy map is empty, we are done
  if len(allergy_map) == 0:
    break

  # Remove the ingredient from other foods
  for value in allergy_map.values():
    if final_map[cur_key] in value:
      value.remove(final_map[cur_key])

# Now, we have the final key, get all the ingredients and remove the allergens
all_ing = []
for f in foods:
  all_ing.extend(f[0])

for value in final_map.values():
  all_ing = list(filter(lambda a: a != value, all_ing))

print('Part 1: {}'.format(len(all_ing)))

# Sort allergens
final_sorted = sorted(final_map.items(), key=lambda x: x[0])
answer = ''
for item in final_sorted:
  answer += item[1]
  answer += ','

print('Part 2: {}'.format(answer[:-1]))