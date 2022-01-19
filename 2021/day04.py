
import sys

def calc_score(num, board):

  
  sum = 0;
  for i in range(0,5):
    for j in range(0,5):
      if 0 == board[i][j][1]:
        sum += board[i][j][0]

  print('Sum is {} num {} total {}'.format(sum, num, (sum*num)))
  sys.exit()

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

# See if any boards have won
def check_win(boards, num):

  for board in boards:

    # Check rows
    for i in range(0,5):
      if check_row(i, board):
        print('Found row in {}'.format(board))
        #calc_score(num, board)
        return board

    # Check cols
    for j in range(0,5):
      if check_col(j, board):
        print('Found col in {}'.format(board))
        #calc_score(num, board)
        return board

  return None
      

numbers = []

file = open('input', 'r')
line = file.readline()

line = line.strip()
numbers = [ int(n) for n in line.split(',')]

boards = []
board = [] 
count = 0

for line in file:

  if len(line) == 1:
    continue

  if count == 5:
    boards.append(board)
    #print(board)
    board = []
    count = 0

  line = line.strip()
  data = line.split()
  col = []
  for num in data:
    col.append((int(num), 0))

  board.append(col)
  count += 1

board = []
for i in range(0,5):
  col = []
  for j in range(0,5):
    if j == 2:
      col.append((200,1))
    else:
      col.append((200,0))
  board.append(col)
#boards.append(board)

# Go through the numbers and mark each board with a 1
count = 0
isLast = False
for num in numbers:

  print('Check {}'.format(num))
  for board in boards:

    for i in range(0,5):
      for j in range(0,5):
        if num == board[i][j][0]:
          board[i][j] = (num, 1)

  card = check_win(boards, num)
  if card is not None:
    if isLast:
      calc_score(num, boards[0])

    while card is not None:

      if len(boards) == 1:
        isLast = True
        break

      boards.remove(card)
      card = check_win(boards, num)


print('Failed to find a win')
