import sys
import ctypes
import bitarray
import struct
import numpy
import numpy as np


class Packet:

  def __init__(self):
    self.version = 0
    self.type = 0
    self.literal = bitarray.bitarray()
    self.sub_pkt_len = 0
    self.sub_pkt_num = 0
    self.sub_packets = []

  def get_version_total(self):
    total = self.version
    for p in self.sub_packets:
      total += p.get_version_total()
    return total

  def get_value(self):
    total = 0
    if self.type == 0:
      for p in self.sub_packets:
        total += p.get_value()
    elif self.type == 1:
      total = 1
      for p in self.sub_packets:
        total *= p.get_value()
    elif self.type == 2:
      vals = []
      for p in self.sub_packets:
        vals.append(p.get_value())
      total = min(vals)
    elif self.type == 3:
      vals = []
      for p in self.sub_packets:
        vals.append(p.get_value())
      total = max(vals)
    elif self.type == 4:
      total = get_int(self.literal)
    elif self.type == 5:
      if self.sub_packets[0].get_value() > self.sub_packets[1].get_value():
        total = 1
      else:
        total = 0
    elif self.type == 6:
      if self.sub_packets[0].get_value() < self.sub_packets[1].get_value():
        total = 1
      else:
        total = 0
    elif self.type == 7:
      if self.sub_packets[0].get_value() == self.sub_packets[1].get_value():
        total = 1
      else:
        total = 0

    return total


  def parse(self, pos, data):

    self.version = get_int(data[pos:pos + 3])
    pos += 3
    self.type = get_int(data[pos:pos + 3])
    pos += 3

    if self.type == 4:
      while data[pos]:
        pos += 1
        self.literal.extend(data[pos:pos + 4])
        pos += 4
      pos += 1
      self.literal.extend(data[pos:pos + 4])
      pos += 4
    else:
      if data[pos]:
        pos += 1
        self.sub_pkt_num = get_int(data[pos:pos+11])
        pos += 11
        for i in range(self.sub_pkt_num):
          pos, p = get_packet(pos, data)
          self.sub_packets.append(p)
      else:
        pos += 1
        self.sub_pkt_len = get_int(data[pos:pos+15])
        pos += 15
        end = pos + self.sub_pkt_len
        while pos < end:
          pos, p = get_packet(pos, data)
          self.sub_packets.append(p)

    return pos


def get_packet(pos, data):
  p = Packet()
  index = p.parse(pos, data)
  return index, p


def get_int(val):
  i = 0
  for bit in val:
    i = (i << 1) | bit
  return i


file = open('input', 'r')

ba = bitarray.bitarray()
for line in file:

  line = line.strip()
  ba.frombytes(bytes(bytearray.fromhex(line)))

pos = 0
packets = []
while pos != -1:

  pos, p = get_packet(pos, ba)
  packets.append(p)
  if len(ba) - pos < 8:
    pos = -1

v_sum = 0
value = 0
for p in packets:
  v_sum += p.get_version_total()
  value += p.get_value()

print('There are {} packets sum {} value {}'.format(len(packets), v_sum, value))