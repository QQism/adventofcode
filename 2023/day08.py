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

def loadData(example: True):
  print(__file__)
  file = __file__.split('/')[-1]
  print(re.match('day(.+)\.py', file).groups)

# [13207, 19951, 14893, 12083, 20513, 22199]
# 21591777820373117801460521
def part2():
  # lines = getLines('input08small.txt')
  lines = getLines('input08.txt')

  insts = lines[0]
  n = len(lines)

  mapps = {}

  starts = []
  for idx in range(2, n):
    line = lines[idx].strip()
    src, dst = getItems(line, ' = ')
    left, right = getItems(dst, ',')
    left = left[1:]
    right = right[:-1]
    mapps[src] = (left, right)

    if src[-1] == 'A':
      starts.append(src)

  print(mapps)
  res = 0
  idx = 0

  print(starts)
  nn = len(starts)
  found = [None for _ in range(nn)]
  while True:
    res += 1
    mv = insts[idx]
    nStarts = []

    count = 0

    for idxx, curr in enumerate(starts):
      if mv == 'L':
        curr = mapps[curr][0]
      if mv == 'R':
        curr = mapps[curr][1]

      nStarts.append(curr)

      if curr[-1] == 'Z':
        if found[idxx] is None:
          # print(curr, res)
          found[idxx] = res

    idx = (idx + 1) % len(insts)

    breakk = True
    for f in found:
      if f is None:
        breakk = False

    if breakk:
      break

    # print(nStarts, count)
    starts = nStarts

  print(found)
  # Find the least common multiple of `found`

def part1():
  # lines = getLines('input08small.txt')
  lines = getLines('input08.txt')

  insts = lines[0]
  n = len(lines)

  mapps = {}
  for idx in range(2, n):
    line = lines[idx].strip()
    src, dst = getItems(line, ' = ')
    left, right = getItems(dst, ',')
    left = left[1:]
    right = right[:-1]
    mapps[src] = (left, right)

  print(mapps)
  curr = 'AAA'
  res = 0
  idx = 0

  while True:
    mv = insts[idx]

    if curr == 'ZZZ':
      break

    if mv == 'L':
      curr = mapps[curr][0]
    if mv == 'R':
      curr = mapps[curr][1]

    res += 1

    idx = (idx + 1) % len(insts)

  print(res)
  # loadData(True)
part2()
