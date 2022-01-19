from collections import Counter
from collections import deque
import hashlib

def get_length(line, pos):
    m_end = line.find(')', pos)
    marker = line[pos + 1:m_end]
    data = marker.split('x')
    chars = int(data[0])
    repeat = int(data[1])
    end = m_end + 1 + chars
    seq = line[m_end+1:end]
    beg = seq.find('(')
    if beg == -1:
        return chars*repeat, end

    total = 0
    pos = 0
    while beg != -1:
        chars, pos = get_length(seq, pos)
        total += chars
        beg = seq.find('(', pos)

    return total*repeat, end


result = ''
count = 0
file = open('input.txt', 'r')
for line in file:
    line = line.strip()

    pos = 0
    while True:
        pos = line.find('(', pos)
        if pos == -1:
            break

        length, pos = get_length(line, pos)
        count += length


print(count)
