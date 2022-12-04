
import sys


def calc_score(num, board):

  total = 0;
  for i in range(0,5):
    for j in range(0,5):
      if 0 == board[i][j][1]:
        total += board[i][j][0]

  return total * num


# Check col
def check_col(col, board):

  for i in range(0,5):
    if board[i][col][1] == 0:
      return False
  return True


# Check row
def check_row(row, board):

  for j in range(0,5):
    if board[row][j][1] == 0:
      return False
  return True


# See if this board won
def check_win(board):

  # Check rows
  for i in range(0,5):
    if check_row(i, board):
      return True

  # Check cols
  for j in range(0,5):
    if check_col(j, board):
      return True

  return False
      

numbers = []
file = open('input04.txt', 'r')
line = file.readline()

line = line.strip()
numbers = [int(n) for n in line.split(',')]

boards = []
board = [] 
count = 0

for line in file:

  if len(line) == 1:
    continue

  if count == 5:
    boards.append(board)
    board = []
    count = 0

  data = line.strip().split()
  row = []
  for num in data:
    row.append((int(num), 0))

  board.append(row)
  count += 1

# Go through the numbers and mark each board with a 1
count = 0
firstWin = False
for num in numbers:
  wins = []
  for board in boards:

    for i in range(0,5):
      for j in range(0,5):
        if num == board[i][j][0]:
          board[i][j] = (num, 1)

    if check_win(board):
      if not firstWin:
        print('Part 1: {}'.format(calc_score(num, board)))
        firstWin = True
      wins.append(board)

  for w in wins:
    boards.remove(w)
    if len(boards) == 0:
      print('Part 2: {}'.format(calc_score(num, w)))