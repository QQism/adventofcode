import re, time, collections, sys, functools
from collections import defaultdict

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
  # lines = getLines('input04small.txt')
  lines = getLines('input04.txt')

  res = 0
  counter = defaultdict(int)

  for idx, line in enumerate(lines):
    counter[idx + 1] += 1
    _, numbers = line.split(': ')

    p1, p2 = numbers.split(' | ')

    s1 = set()
    s1 = set(getItems(p1, ' '))
    s2 = set(getItems(p2, ' '))

    m = len(s1 & s2)
    if m == 0:
      continue

    for i in range(idx + 2, idx + m + 2):
      counter[i] += counter[idx + 1]

  # print(counter)

  for k in counter.keys():
    res += counter[k]

  print(res)

def part1():
  # lines = getLines('input04small.txt')
  lines = getLines('input04.txt')

  res = 0
  for line in lines:
    _, numbers = line.split(': ')

    p1, p2 = numbers.split(' | ')

    s1 = set()
    s1 = set(getItems(p1, ' '))
    s2 = set(getItems(p2, ' '))

    m = len(s1 & s2)
    if m > 0:
      res += 2 ** (m - 1)

  print(res)

part2()
