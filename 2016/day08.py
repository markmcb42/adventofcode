from collections import Counter
from collections import deque
import hashlib


# cmds: (rect, x, y)
# cmds: (rotate, 'x|y', pos, val)
commands = []
screen = {}
for i in range(6):
    row = deque(list([0]*50))
    screen[i] = row

file = open('input.txt', 'r')
for line in file:
    line = line.strip()

    if 'rect' in line:
        data = line.split()
        action = data[0]
        pos = data[1].split('x')
        cmd = (action, int(pos[0]), int(pos[1]))
        commands.append(cmd)
        continue

    data = line.split()
    val = int(line[line.rfind(' '):])
    pos = data[2].split('=')
    cmd = (data[0], pos[0], int(pos[1]), val)
    commands.append(cmd)

for cmd in commands:
    if cmd[0] == 'rect':
        for x in range(cmd[1]):
            for y in range(cmd[2]):
                screen[y][x] = 1
        continue

    if cmd[1] == 'y':
        screen[cmd[2]].rotate(cmd[3])
        continue

    collist = []
    for x in range(6):
        collist.append(screen[x][cmd[2]])
    col = deque(collist)
    col.rotate(cmd[3])
    for x in range(6):
        screen[x][cmd[2]] = col[x]

count = 0
for x in range(6):
    for y in range(50):
        if screen[x][y] == 1:
            count += 1

print(count)

