import sys
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
    seq = line[m_end + 1:end]
    beg = seq.find('(')
    if beg == -1:
        return chars * repeat, end

    total = 0
    pos = 0
    while beg != -1:
        chars, pos = get_length(seq, pos)
        total += chars
        beg = seq.find('(', pos)

    return total * repeat, end


bots = {}
cmds = []
outputs = []
file = open('input.txt', 'r')
for line in file:
    line = line.strip()

    if 'value' in line:
        data = line.split()
        val = int(data[1])
        bot_num = int(data[5])
        if bot_num not in bots:
            bots[bot_num] = []
        bots[bot_num].append(val)
        continue

    cmds.append(line)

while len(cmds) > 0:
    cur_cmds = []
    for cmd in cmds:
        data = cmd.split()
        bot_num = int(data[1])
        if bot_num not in bots:
            cur_cmds.append(cmd)
            continue

        if len(bots[bot_num]) < 2:
            cur_cmds.append(cmd)
            continue

        if min(bots[bot_num]) == 17 and max(bots[bot_num]) == 61:
            print(bot_num)
            #sys.exit()

        if 'bot' in data[5]:
            low_bot = int(data[6])
            if low_bot not in bots:
                bots[low_bot] = []
            bots[low_bot].append(min(bots[bot_num]))
        else:
            output = int(data[6])
            if output == 0 or output == 1 or output == 2:
                outputs.append(min(bots[bot_num]))

        if 'bot' in data[10]:
            high_bot = int(data[11])
            if high_bot not in bots:
                bots[high_bot] = []
            bots[high_bot].append(max(bots[bot_num]))
        else:
            output = int(data[11])
            if output == 0 or output == 1 or output == 2:
                outputs.append(min(bots[bot_num]))
        if len(outputs) == 3:
            print(outputs)
            sys.exit()

        bots[bot_num] = []

    cmds = cur_cmds

