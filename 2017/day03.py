
import sys
import numpy as np

def sum_n(grid, row, col):
    total = 0
    for x in range(row-1, row+2):
        for y in range(col-1, col+2):
            total += grid[x][y]
    return total


grid = np.zeros((1000, 1000), dtype=int)

startx = row = 500
starty = col = 500
val = 1
grid[startx][starty] = val

while val <= 289326:
    # Move to the right
    col += 1
    val = sum_n(grid, row, col)
    grid[row][col] = val
    if val > 289326:
        print(val)
        break

    while grid[row-1][col] != 0:
        col += 1
        val = sum_n(grid, row, col)
        grid[row][col] = val
        if val > 289326:
            print(val)
            break

    # Move up
    row -= 1
    val = sum_n(grid, row, col)
    grid[row][col] = val
    if val > 289326:
        print(val)
        break
    while grid[row][col-1] != 0:
        row -= 1
        val = sum_n(grid, row, col)
        grid[row][col] = val
        if val > 289326:
            print(val)
            break

    # Move to the left
    col -= 1
    val = sum_n(grid, row, col)
    grid[row][col] = val
    if val > 289326:
        print(val)
        break

    while grid[row+1][col] != 0:
        col -= 1
        val = sum_n(grid, row, col)
        grid[row][col] = val
        if val > 289326:
            print(val)
            break

    # Move down
    row += 1
    val = sum_n(grid, row, col)
    grid[row][col] = val
    if val == 289326:
        break
    while grid[row][col+1] != 0:
        row += 1
        val = sum_n(grid, row, col)
        grid[row][col] = val
        if val == 289326:
            break


print(abs(startx - row) + abs(starty, col))

