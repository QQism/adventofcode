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
  # lines = getLines('input05small.txt')
  lines = getLines('input05.txt')

  seed2Soil = []
  soil2Fert = []
  fert2Water = []
  water2Light = []
  light2Temp = []
  temp2Humid = []
  humid2Loc = []

  mapps = [
    seed2Soil,
    soil2Fert,
    fert2Water,
    water2Light,
    light2Temp,
    temp2Humid,
    humid2Loc,
  ]

  currIdx = 0
  curr = mapps[currIdx]

  n = len(lines)
  first = lines[0]
  _, nums = first.split(':')
  nums = list(map(int, getItems(nums)))

  groups = []
  for idx in range(len(nums)):
    num = nums[idx]

    if idx % 2 == 0:
      groups.append([num])
    else:
      groups[-1].append(num)

  for idx in range(3, n):
    line = lines[idx]
    line.strip()

    if len(line) == 0:
      continue

    if line[-1] == ':':
      currIdx += 1
      curr = mapps[currIdx]
      continue

    dest, source, r = map(int, getItems(line))
    curr.append([dest, source, r])


  # res = math.inf
  # for s, ra in groups:
  #   for num in range(s, s + ra):
  #     arr = [num]
  #     for idx, mapp in enumerate(mapps):
  #       found = False
  #       for dest, source, r in mapp:
  #         if num >= source and num <= source + r - 1:
  #           num = dest + (num - source)
  #           arr.append(num)
  #           found = True
  #           break
  #       if not found:
  #         arr.append(num)

  #     print(arr)
  #     res = min(res, num)

  # print(res)

  curr = deque(groups)
  for i, mapp in enumerate(mapps):
    print(f'i: {i + 1}, curr: {curr}, mapp: {mapp}')
    nextCurr = deque()
    wait = set()
    toBeRemoved = set()
    while len(curr) > 0:
      s, ra = curr.popleft()
      for dest, source, r in mapp:
        if s >= source and s <= source + r - 1:
          # if i == 2:
          #   print(f's: {s}, ra: {ra}, source: {source}, r: {r}')
          if (s, ra) not in toBeRemoved:
            toBeRemoved.add((s, ra))

          nextS = dest + (s - source)
          remain = source + r - s

          nr = min(ra, remain)
          # if nextS == 53:
          #   print(f'remain: {remain}, ra: {ra}, r: {r}')
          nextCurr.append((nextS, nr))

          if nr < ra:
            val = (source + r, ra - nr)
            curr.append(val)
            wait.add(val)
          # else:
          break
        elif s < source and s + ra - 1 >= source:
          if (s, ra) not in toBeRemoved:
            toBeRemoved.add((s, ra))

          nr = source - s # - 1
          val = (s, nr)
          curr.append(val)
          wait.add(val)

          remain = ra - nr

          nr = min(remain, r)
          nextCurr.append((dest, nr))

          if nr < remain:
            val = (source + r, remain - nr)
            curr.append(val)
            wait.add(val)
          break
        else:
          if (s, ra) not in wait:
            wait.add((s, ra))

    for s, ra in wait:
      if (s, ra) not in toBeRemoved:
        nextCurr.append((s, ra))

    # print(nextCurr)
    curr = nextCurr
    # for s, ra in curr:
    #   found = False
    #   for dest, source, r in mapp:
    #     # print(f's: {s}, source: {source}, r: {r}')
    #     if s >= source and s <= source + r:
    #       # print('yes')
    #       nextS = dest + (s - source)
    #       nr = min(ra, r)
    #       nextCurr.append([nextS, nr])

    #       if nr < ra:
    #         nextCurr.append([nextS + nr + 1, ra - nr])
    #       found = True
    #       break

    #   if found:
    #     continue



    # print(nextCurr)
    # curr = nextCurr

  print(curr)
  print(min(curr)[0])

def part1():
  # lines = getLines('input05small.txt')
  lines = getLines('input05.txt')

  seed2Soil = []
  soil2Fert = []
  fert2Water = []
  water2Light = []
  light2Temp = []
  temp2Humid = []
  humid2Loc = []

  mapps = [
    seed2Soil,
    soil2Fert,
    fert2Water,
    water2Light,
    light2Temp,
    temp2Humid,
    humid2Loc,
  ]

  currIdx = 0
  curr = mapps[currIdx]

  n = len(lines)
  first = lines[0]
  _, nums = first.split(':')
  nums = list(map(int, getItems(nums)))

  for idx in range(3, n):
    line = lines[idx]
    line.strip()

    if len(line) == 0:
      continue

    if line[-1] == ':':
      currIdx += 1
      curr = mapps[currIdx]
      continue

    dest, source, r = map(int, getItems(line))
    curr.append([dest, source, r])

  currIdx = 0
  curr = mapps[currIdx]
  res = math.inf
  for num in nums:
    for mapp in mapps:
      for dest, source, r in mapp:
        if num >= source and num <= source + r:
          num = dest + (num - source)
          break

    res = min(res, num)
  print(res)

part2()
