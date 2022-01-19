import sys
lines = open('input', 'r').read().split('\n')[:-1]

points = list()
folds = list()
for l in lines:
    if (l.startswith('fold')):
        d,v = l[11:].split('=')
        folds.append((d,int(v)))
    elif (l != ''):
        x,y = l.split(',')
        points.append((int(x),int(y)))

def printPoints(points):
    maxY = max([p[1] for p in points])
    maxX = max([p[0] for p in points])
    print()
    for y in range(maxY+1):
        for x in range(maxX+1):
            if (x,y) in points:
                print('█',end='')
            else:
                print(' ',end='')
        print()
    print()

def foldPaper(points, fold):
    if (fold[0] == 'y'):
        for i in range(len(points)):
            if (points[i][1] > fold[1]):
                points[i] = (points[i][0], points[i][1] - 2 * (points[i][1] - fold[1]))
    elif (fold[0] == 'x'):
        for i in range(len(points)):
            if (points[i][0] > fold[1]):
                points[i] = (points[i][0] - 2 * (points[i][0] - fold[1]),points[i][1])
    return list(set(points))

for i in range(len(folds)):
    if (i == 1):
        print('Part 1:',len(points))
    points = foldPaper(points, folds[i])
print('Part 2:')
printPoints(points)
