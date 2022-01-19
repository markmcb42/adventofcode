import sys

import numpy
import numpy as np

file = open('input', 'r')
folds = []
dots = []
maxx = 0
maxy = 0
for line in file:

    line = line.strip()
    if len(line) == 0:
        continue

    if 'fold' in line:
        pos = line.find('=')
        fold = (line[pos-1:pos], int(line[pos+1:]))
        folds.append(fold)
    else:
        data = line.split(',')
        x = int(data[0])
        y = int(data[1])
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
        dot = (x,y)
        dots.append(dot)

for fold in folds:
    if fold[0] == 'y':
        new_dots = set()
        for dot in dots:
            if dot[1] > fold[1]:
                y = dot[1] - (2 * (dot[1] - fold[1]))
                new_dot = (dot[0], y)
                new_dots.add(new_dot)
            else:
                new_dots.add(dot)
        print('There are {} dots now'.format(len(new_dots)))
        dots = list(new_dots)

    elif fold[0] == 'x':
        new_dots = set()
        for dot in dots:
            if dot[0] > fold[1]:
                x = dot[0] - (2 * (dot[0] - fold[1]))
                new_dot = (x, dot[1])
                new_dots.add(new_dot)
            else:
                new_dots.add(dot)
        print('There are {} dots now'.format(len(new_dots)))

        dots = list(new_dots)



maxx += 1
maxy += 1
paper = np.zeros((maxy, maxx), dtype=int)
for dot in dots:
    paper[dot[1], dot[0]] = 1

print('There are {} dots in grid size {},{}'.format(len(dots), maxx, maxy))

for fold in folds:

    if fold[0] == 'y':
        foldy = fold[1]
        new_paper = np.zeros((foldy, maxx), dtype=int)

        for i in range(foldy):
            for x in range(maxx):
                if paper[i][x] == 1 or paper[maxy-1-i][x] == 1:
                    new_paper[i][x] = 1

        paper = new_paper
        maxy = foldy
    elif fold[0] == 'x':
        foldx = fold[1]
        new_paper = np.zeros((maxy,foldx), dtype=int)

        for i in range(foldx):
            for x in range(maxy):
                if paper[x][i] == 1 or paper[x][maxx-1-i] == 1:
                    new_paper[x][i] = 1

        maxx = foldx
        paper = new_paper

count = 0
for y in range(maxy):
    for x in range(maxx):
        if paper[y][x] == 1:
            count += 1

print('Number of dots is {}'.format(count))

