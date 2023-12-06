import re, time, collections, sys, functools, math
from collections import defaultdict, deque

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
  # lines = getLines('input06small.txt')
  lines = getLines('input06.txt')
  _, times = getItems(lines[0], ': ')
  times = list(getItems(times, ' '))

  _, dists = getItems(lines[1], ': ')
  dists = list(getItems(dists, ' '))

  ti = int(''.join(times))
  dist = int(''.join(dists))

  x1 = math.floor((ti - math.sqrt(ti ** 2 - 4 * dist)) / 2)
  x2 = math.floor((ti + math.sqrt(ti ** 2 - 4 * dist)) / 2)

  print(x2 - x1)

def part1():
  # lines = getLines('input06small.txt')
  lines = getLines('input06.txt')
  _, times = getItems(lines[0], ': ')
  times = list(map(int, getItems(times, ' ')))

  _, dists = getItems(lines[1], ': ')
  dists = list(map(int, getItems(dists, ' ')))

  tracks = []
  for idx in range(len(times)):
    tracks.append((times[idx], dists[idx]))

  print(tracks)

  res = 0

  res = []
  for ti, dist in tracks:
    tmp = 0
    for t in range(ti + 1):
      # 1
      remain = ti - t
      if remain * t > dist:
        tmp += 1
    res.append(tmp)
    # break

  ress = 1
  for num in res:
    ress *= num
  print(ress)

part2()
