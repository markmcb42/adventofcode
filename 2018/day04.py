
import sys
import numpy as np
from datetime import datetime

schedule = []
file = open('input.txt', 'r')
for line in file:
  data = line.strip().split(']')
  date_str = data[0][1:]
  date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
  schedule.append((date, data[1]))

schedule.sort(key=lambda x: x[0])

guards = {}
cur = 0
start = 0
end = 0
for s in schedule:
  if 'shift' in s[1]:
    data = s[1].split()
    cur = int(data[1][1:])
    if cur not in guards:
      guards[cur] = []
    continue

  if 'asleep' in s[1]:
    start = s[0].minute
    continue

  if 'wakes' in s[1]:
    end = s[0].minute
    guards[cur].append((s[0].month, s[0].day, start, end))

sleeptime = 0
guard = 0
for key, val in guards.items():
  cur = 0
  for item in val:
    cur += (item[3] - item[2])
  if cur > sleeptime:
    sleeptime = cur
    guard = key

minutes = np.zeros(60, dtype=int)
for item in guards[guard]:
  for m in range(item[2], item[3]):
    minutes[m] += 1

max_minute = 0
max_minutes = 0
it = np.nditer(minutes)
for m in it:
  if m > max_minutes:
    max_minutes = m
    max_minute = it.iterindex

print(max_minute * guard)

max_minute = 0
max_minutes = 0
guard = 0
for key, val in guards.items():
  minutes = np.zeros(60, dtype=int)
  for item in val:
    for m in range(item[2], item[3]):
      minutes[m] += 1

  it = np.nditer(minutes)
  for m in it:
    if m > max_minutes:
      max_minutes = m
      max_minute = it.iterindex
      guard = key

print(max_minute * guard)




