
import sys
import re


file = open('input05.txt', 'r')

seeds = []
maps = {}
key = ''

for line in file:
  line = line.strip()

  if len(line) == 0:
    continue

  if line.startswith('seeds:'):
    seeds = [int(x) for x in line.split(':')[1].strip().split()]
    continue

  if line.endswith(':'):
    key = line.split()[0]
    maps[key] = []
    continue

  raw = [int(x) for x in line.split()]
  count = raw[2] - 1
  src = (raw[0], raw[0] + count)
  dest = (raw[1], raw[1] + count)
  maps[key].append((src, dest))


min_location = 0
dest = []
for s in seeds:

  # Get soil value
  soil = 0
  found = False
  for r in maps['seed-to-soil']:
    dst = r[0]
    src = r[1]
    if src[0] <= s <= src[1]:
      delta = s - src[0]
      soil = dst[0] + delta
      found = True
      break

  if not found:
    soil = s

  # Get Fertilizer value from soil
  fertilizer = 0
  found = False
  for r in maps['soil-to-fertilizer']:
    dst = r[0]
    src = r[1]
    if src[0] <= soil <= src[1]:
      delta = soil - src[0]
      fertilizer = dst[0] + delta
      found = True
      break

  if not found:
    fertilizer = soil

  water = 0
  found = False
  for r in maps['fertilizer-to-water']:
    dst = r[0]
    src = r[1]
    if src[0] <= fertilizer <= src[1]:
      delta = fertilizer - src[0]
      water = dst[0] + delta
      found = True
      break

  if not found:
    water = fertilizer

  light = 0
  found = False
  for r in maps['water-to-light']:
    dst = r[0]
    src = r[1]
    if src[0] <= water <= src[1]:
      delta = water - src[0]
      light = dst[0] + delta
      found = True
      break

  if not found:
    light = water

  temp = 0
  found = False
  for r in maps['light-to-temperature']:
    dst = r[0]
    src = r[1]
    if src[0] <= light <= src[1]:
      delta = light - src[0]
      temp = dst[0] + delta
      found = True
      break

  if not found:
    temp = light

  humidity = 0
  found = False
  for r in maps['temperature-to-humidity']:
    dst = r[0]
    src = r[1]
    if src[0] <= temp <= src[1]:
      delta = temp - src[0]
      humidity = dst[0] + delta
      found = True
      break

  if not found:
    humidity = temp

  location = 0
  found = False
  for r in maps['humidity-to-location']:
    dst = r[0]
    src = r[1]
    if src[0] <= humidity <= src[1]:
      delta = humidity - src[0]
      location = dst[0] + delta
      found = True
      break

  if not found:
    location = humidity

  if min_location == 0:
    min_location = location
  elif location < min_location:
    min_location = location

print('Part 1: {}'.format(min_location))

seed_ranges = []
for i in range(0, len(seeds), 2):
  seed_ranges.append((seeds[i], seeds[i + 1]))

# sort ranges by source for each map
for key, val in maps.items():
  val.sort(key = lambda x : x[1])
  start = val[0][1][0]
  end = val[len(val) - 1][1][1]
  val.insert(0, (start, end))

min_location = 0
for sr in seed_ranges:
  count = 0
  for s in range(sr[0], sr[0] + sr[1] + 1):
    count += 1

    # Get soil value
    soil = 0
    max_range = maps['seed-to-soil']
    if max_range[0][0] <= s <= max_range[0][1]:
      for i in range(1, len(maps['seed-to-soil'])):
        r = maps['seed-to-soil'][i]
        if s <= r[1][1]:
          soil = r[0][0] + (s - r[1][0])
          break
    else:
      soil = s

    # Get Fertilizer value from soil
    fertilizer = 0
    max_range = maps['soil-to-fertilizer']
    if max_range[0][0] <= soil <= max_range[0][1]:
      for i in range(1, len(maps['soil-to-fertilizer'])):
        r = maps['soil-to-fertilizer'][i]
        if soil <= r[1][1]:
          fertilizer = r[0][0] + (soil - r[1][0])
          break
    else:
      fertilizer = soil

    water = 0
    max_range = maps['fertilizer-to-water']
    if max_range[0][0] <= fertilizer <= max_range[0][1]:
      for i in range(1, len(maps['fertilizer-to-water'])):
        r = maps['fertilizer-to-water'][i]
        if fertilizer <= r[1][1]:
          water = r[0][0] + (fertilizer - r[1][0])
          break
    else:
      water = fertilizer

    light = 0
    max_range = maps['water-to-light']
    if max_range[0][0] <= water <= max_range[0][1]:
      for i in range(1, len(maps['water-to-light'])):
        r = maps['water-to-light'][i]
        if water <= r[1][1]:
          light = r[0][0] + (water - r[1][0])
          break
    else:
      light = water

    temp = 0
    max_range = maps['light-to-temperature']
    if max_range[0][0] <= light <= max_range[0][1]:
      for i in range(1, len(maps['light-to-temperature'])):
        r = maps['light-to-temperature'][i]
        if light <= r[1][1]:
          temp = r[0][0] + (light - r[1][0])
          break
    else:
      temp = light

    humidity = 0
    max_range = maps['temperature-to-humidity']
    if max_range[0][0] <= temp <= max_range[0][1]:
      for i in range(1, len(maps['temperature-to-humidity'])):
        r = maps['temperature-to-humidity'][i]
        if temp <= r[1][1]:
          humidity = r[0][0] + (temp - r[1][0])
          break
    else:
      humidity = temp

    location = 0
    max_range = maps['humidity-to-location']
    if max_range[0][0] <= humidity <= max_range[0][1]:
      for i in range(1, len(maps['humidity-to-location'])):
        r = maps['humidity-to-location'][i]
        if humidity <= r[1][1]:
          location = r[0][0] + (humidity - r[1][0])
          break
    else:
      location = humidity

    if min_location == 0:
      min_location = location
    elif location < min_location:
      min_location = location


print('Part 2: {}'.format(min_location))


