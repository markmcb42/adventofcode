
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy

class Cart:

  choices = ['l', 's', 'r']
  def __init__(self, row, col, dir):
    self.row = row
    self.col = col
    self.dir = dir
    self.choice = 0
    self.crashed = False

  def move(self, grid):
    if self.dir == 'u':
      self.row -= 1
      if grid[self.row][self.col] == '\\':
        self.dir = 'l'
      elif grid[self.row][self.col] == '/':
        self.dir = 'r'
      elif grid[self.row][self.col] == '+':
        turn = Cart.choices[self.choice % len(Cart.choices)]
        if turn == 'l' or turn == 'r':
          self.dir = turn
        self.choice += 1

    elif self.dir == 'd':
      self.row += 1
      if self.row == 150:
        print(self.row)
      if grid[self.row][self.col] == '/':
        self.dir = 'l'
      elif grid[self.row][self.col] == '\\':
        self.dir = 'r'
      elif grid[self.row][self.col] == '+':
        turn = Cart.choices[self.choice % len(Cart.choices)]
        if turn == 'l':
          self.dir = 'r'
        elif turn == 'r':
          self.dir = 'l'
        self.choice += 1

    elif self.dir == 'r':
      self.col += 1
      if grid[self.row][self.col] == '/':
        self.dir = 'u'
      elif grid[self.row][self.col] == '\\':
        self.dir = 'd'
      elif grid[self.row][self.col] == '+':
        turn = Cart.choices[self.choice % len(Cart.choices)]
        if turn == 'l':
          self.dir = 'u'
        elif turn == 'r':
          self.dir = 'd'
        self.choice += 1

    elif self.dir == 'l':
      self.col -= 1
      if grid[self.row][self.col] == '/':
        self.dir = 'd'
      elif grid[self.row][self.col] == '\\':
        self.dir = 'u'
      elif grid[self.row][self.col] == '+':
        turn = Cart.choices[self.choice % len(Cart.choices)]
        if turn == 'l':
          self.dir = 'd'
        elif turn == 'r':
          self.dir = 'u'
        self.choice += 1


max_row = 0
max_col = 0
lines = []
file = open('input.txt', 'r')
for line in file:
  max_row += 1
  line = line[:len(line)-1]
  if len(line) > max_col:
    max_col = len(line)
  lines.append(line)

grid = np.zeros((max_row, max_col), dtype='U1')

carts = []
for row in range(len(lines)):
  line = lines[row]
  for col in range(len(line)):
    grid[row][col] = line[col]
    if line[col] == '>':
      cart = Cart(row, col, 'r')
      carts.append(cart)
      grid[row][col] = '-'
    elif line[col] == '<':
      cart = Cart(row, col, 'l')
      carts.append(cart)
      grid[row][col] = '-'
    elif line[col] == '^':
      cart = Cart(row, col, 'u')
      carts.append(cart)
      grid[row][col] = '|'
    elif line[col] == 'v':
      cart = Cart(row, col, 'd')
      carts.append(cart)
      grid[row][col] = '|'

while True:

  carts.sort(key=lambda x: (x.row, x.col))
  crashed = []

  # move the carts
  for cart in carts:
    cart.move(grid)
    for i in range(len(carts)):
      for j in range(i + 1, len(carts)):
        if carts[i].crashed or carts[j].crashed:
          continue

        if carts[i].row == carts[j].row and carts[i].col == carts[j].col:
          print('Crash: {},{}'.format(carts[i].col, carts[i].row))
          carts[i].crashed = True
          carts[j].crashed = True
          crashed.append(carts[i])
          crashed.append(carts[j])

  # Check for collision
  for i in range(len(carts)):
    for j in range(i+1, len(carts)):
      if carts[i].crashed or carts[j].crashed:
        continue

      if carts[i].row == carts[j].row and carts[i].col == carts[j].col:
        print('Crash: {},{}'.format(carts[i].col, carts[i].row))
        crashed.append(carts[i])
        crashed.append(carts[j])

  if len(crashed) > 0:
    for cart in crashed:
      carts.remove(cart)

  if len(carts) == 1:
    print('Last pos {},{}'.format(carts[0].col, carts[0].row))
    sys.exit()





