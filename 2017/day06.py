import sys
import numpy as np
from collections import Counter

data_in = [0, 2, 7, 0]
data_in= [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
banks = {}
index = 0
for i in data_in:
    banks[index] = i
    index += 1

states = [tuple(data_in)]

count = 0
while True:
    count += 1
    max_bank = 0
    num_blocks = 0
    for bank, blocks in banks.items():
        if blocks > num_blocks:
            max_bank = bank
            num_blocks = blocks

    banks[max_bank] = 0
    for i in range(num_blocks):
        max_bank += 1
        if max_bank >= len(banks):
            max_bank = 0
        banks[max_bank] += 1

    state = tuple(list(banks.values()))
    if state in states:
        for i in range(len(states)):
            if states[i] == state:
                print(count - i)
        break
    else:
        states.append(state)

print(count)


