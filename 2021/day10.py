import sys

file = open('input10.txt', 'r')

open_chars = '([{<'
close_chars = ')]}>'
scores = [3,57,1197,25137]
comp_val = [1, 2, 3, 4]
score = 0
comp_scores = []

for line in file:

  line = line.strip()
  cur_open = []
  error = False
  for c in line:
    if c in open_chars:
      cur_open.append(c)
    else:
      pos = close_chars.find(c)
      cur = cur_open[-1]
      if cur != open_chars[pos]:
        score += scores[pos]
        error = True
        break
      else:
        cur_open.pop()

  if error:
    continue

  cur_open.reverse()
  cur_close = []
  for c in cur_open:
    pos = open_chars.find(c)
    cur_close.append(close_chars[pos])

  cur_score = 0
  for c in cur_close:
    cur_score *= 5
    pos = close_chars.find(c)
    cur_score += comp_val[pos]

  comp_scores.append(cur_score)

comp_scores.sort()
mid = int(len(comp_scores) / 2)
winner = comp_scores[mid]
print('Part 1: {}'.format(score))
print('Part 2: {}'.format(winner))

