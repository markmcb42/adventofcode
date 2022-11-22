
import sys
import numpy as np
from datetime import datetime
from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
import copy


def get_code(cur_map):
  for key, val in cur_map.items():
    if len(val) == 1:
      return key, val[0]

  return '', -1


def remove_val(cur_map, value):
  for k, v in cur_map.items():
    if value in v:
      v.remove(value)
  return cur_map


def run_cmd(register, cur_cmd, opcode):
  if opcode == 'addr':
    register[cur_cmd[3]] = register[cur_cmd[1]] + register[cur_cmd[2]]
  elif opcode == 'addi':
    register[cur_cmd[3]] = register[cur_cmd[1]] + cur_cmd[2]
  elif opcode == 'mulr':
    register[cur_cmd[3]] = register[cur_cmd[1]] * register[cur_cmd[2]]
  elif opcode == 'muli':
    register[cur_cmd[3]] = register[cur_cmd[1]] * cur_cmd[2]
  elif opcode == 'banr':
    register[cur_cmd[3]] = register[cur_cmd[1]] & register[cur_cmd[2]]
  elif opcode == 'bani':
    register[cur_cmd[3]] = register[cur_cmd[1]] & cur_cmd[2]
  elif opcode == 'borr':
    register[cur_cmd[3]] = register[cur_cmd[1]] | register[cur_cmd[2]]
  elif opcode == 'bori':
    register[cur_cmd[3]] = register[cur_cmd[1]] | cur_cmd[2]
  elif opcode == 'setr':
    register[cur_cmd[3]] = register[cur_cmd[1]]
  elif opcode == 'seti':
    register[cur_cmd[3]] = cur_cmd[1]

  elif opcode == 'gtir':
    if cur_cmd[1] > register[cur_cmd[2]]:
      register[cur_cmd[3]] = 1
    else:
      register[cur_cmd[3]] = 0
  elif opcode == 'gtri':
    if register[cur_cmd[1]] > cur_cmd[2]:
      register[cur_cmd[3]] = 1
    else:
      register[cur_cmd[3]] = 0
  elif opcode == 'gtrr':
    if register[cur_cmd[1]] > register[cur_cmd[2]]:
      register[cur_cmd[3]] = 1
    else:
      register[cur_cmd[3]] = 0

  elif opcode == 'eqir':
    if cur_cmd[1] == register[cur_cmd[2]]:
      register[cur_cmd[3]] = 1
    else:
      register[cur_cmd[3]] = 0
  elif opcode == 'eqri':
    if register[cur_cmd[1]] == cur_cmd[2]:
      register[cur_cmd[3]] = 1
    else:
      register[cur_cmd[3]] = 0
  elif opcode == 'eqrr':
    if register[cur_cmd[1]] == register[cur_cmd[2]]:
      register[cur_cmd[3]] = 1
    else:
      register[cur_cmd[3]] = 0

  return register


lines = []
file = open('input16.txt', 'r')
before = []
ins = []
after = []
cmds = []
program = []
blank_count = 0
for line in file:
  line = line.strip()
  if len(line.strip()) == 0:
    blank_count += 1
    continue

  if blank_count <= 1:
    blank_count = 0
    if 'Before' in line:
      before = [int(c) for c in line.split('[')[1][:-1].split(',')]
    elif 'After' in line:
      after = [int(c) for c in line.split('[')[1][:-1].split(',')]
      cmds.append((before, ins, after))
      before = []
      ins = []
      after = []
    else:
      ins = [int(c) for c in line.split(' ')]
  else:
    ins = [int(c) for c in line.split(' ')]
    program.append(ins)


codes = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
         'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']
total = 0
cmap = {}
for c in cmds:
  correct = 0
  code = c[1]
  matches = []
  for opcode in codes:
    result = copy.copy(c[0])
    result = run_cmd(result, code, opcode)

    if result == c[2]:
      correct += 1
      matches.append(opcode)

  if correct >= 3:
    total += 1

  num_code = c[1][0]
  for m in matches:
    if m not in cmap:
      cmap[m] = []
    if num_code not in cmap[m]:
      cmap[m].append(num_code)

final_map = {}

while True:
  key, val = get_code(cmap)
  if val == -1:
    break
  final_map[val] = key
  cmap = remove_val(cmap, val)


print('Part 1: {} '.format(total))

register = [0,0,0,0]
for p in program:
  register = run_cmd(register, p, final_map[p[0]])


print('Part 2: {}'.format(register[0]))



