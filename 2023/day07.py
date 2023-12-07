import re, time, collections, sys, functools, math
from collections import defaultdict, deque, Counter
import heapq

def getLines(filename):
  file = open(filename)
  lines = file.readlines()

  res = []
  for line in lines:
    res.append(line.strip())

  return res

def getItems(ss, sep=' '):
  res = []
  for num in list(map(lambda s: s.strip(), ss.strip().split(sep))):
    if num != '':
      res.append(num)

  return res

def part2():
  # lines = getLines('input07small.txt')
  lines = getLines('input07.txt')

  cards = []
  for line in lines:
    card, bid = getItems(line)

    cards.append(Card(card, bid))

  cards.sort()

  res = 0
  for idx, card in enumerate(cards):
    print(card.val, card._kind)
    res += (idx + 1) * card.bid

  print(res)

class Card:
  def __init__(self, val, bid):
    self.val = val
    self.bid = int(bid)
    self._kind = None
    self.map = {
      'A': 14,
      'K': 13,
      'Q': 12,
      # 'J': 11,
      'T': 10,
      '9': 9, '8': 8, '7': 7,
      '6': 6, '5': 5, '4': 4, '3': 3, '2': 2,
      'J': 1,
    }

    self.mapp = {
      '5k': 7,
      '4k': 6,
      'fh': 5,
      '3k': 4,
      '2p': 3,
      '1p': 2,
      'hc': 1
    }

  def kind(self):
    if self._kind is not None:
      return self._kind

    counter = Counter(self.val)
    jc = counter['J']

    maxxK = None
    maxx = 0
    for k in counter:
      if k != 'J':
        if counter[k] > maxx:
          maxxK = k
          maxx = counter[k]

    # if self.val == 'T55J5':
    #   print(counter)

    if maxxK:
      counter[maxxK] += jc
      del counter['J']

    # if self.val == 'T55J5':
    #   print(counter)

    s = set(counter)

    if len(s) == 1:
      # 5 kind
      self._kind = '5k'
    elif len(s) == 2:
      found = False

      for k in counter:
        if counter[k] == 4:
          # 4 kind
          self._kind = '4k'
          found = True

      if not found:
        # Full house
        self._kind = 'fh'
    elif len(s) == 3:
      # TTT98 vs 23423
      found = False
      for k in counter:
        if counter[k] == 3:
          # 3 kind
          self._kind = '3k'
          found = True

      if not found:
        # 2 pair
        self._kind = '2p'
    elif len(s) == 4:
      # 1 pair
      self._kind = '1p'
    else:
      # high5
      self._kind = 'hc'

    return self._kind

  def __lt__(self, other):
    if self.kind() != other.kind():
      return self.mapp[self.kind()] < self.mapp[other.kind()]

    for idx in range(5):
      if self.val[idx] == other.val[idx]:
        continue
      else:
        return self.map[self.val[idx]] < self.map[other.val[idx]]

def part1():
  # lines = getLines('input07small.txt')
  lines = getLines('input07.txt')

  cards = []
  for line in lines:
    card, bid = getItems(line)

    cards.append(Card(card, bid))

  cards.sort()

  res = 0
  for idx, card in enumerate(cards):
    print(card.val, card._kind)
    res += (idx + 1) * card.bid

  print(res)

part2()
