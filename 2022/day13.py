import re, time, collections, sys, functools

def parsePairs():
  file = open('input13small.txt')

  lines = file.readlines()

  s = ''.join(lines).strip()

  return list(
    map(lambda x:
      list(map(lambda y: eval(y), x.split('\n'))),
    s.split('\n\n')
    )
  )

def parse():
  file = open('input13.txt')

  lines = file.readlines()

  packets = []

  for line in lines:
    line = line.strip()

    if not len(line):
      continue

    packets.append(eval(line))

  return packets

def part2():
  pairs = parse()
  packet1 = [[2]]
  packet2 = [[6]]
  pairs.append(packet1)
  pairs.append(packet2)


  print(pairs, len(pairs))
  def compare(p1, p2):
    if type(p1) is int and type(p2) is int:
      if p1 < p2:
        return (True, True)
      elif p1 == p2:
        return (True, False)
      else:
        return (False, False)

    if type(p1) is int:
      p1 = [p1]

    if type(p2) is int:
      p2 = [p2]

    n = len(p1)
    m = len(p2)
    i = 0

    if m < n and m == 0:
      return False, False

    decided = False

    while i < max(n, m):
      if i < n and i == m:
        return False, False

      if i == n and i < m:
        return True, True

      res, decided = compare(p1[i], p2[i])

      if res and decided:
        return res, decided

      if not res:
        return (False, False)

      i+=1

    return (True, decided)

  def cmp(p1, p2):
    res, _ = compare(p1, p2)

    if res:
      return -1
    else:
      return 1

  ps = sorted(pairs, key=functools.cmp_to_key(cmp))

  i1 = 0
  i2 = 0
  for i, p in enumerate(ps, start=1):
    if p is packet1:
      i1 = i

    if p is packet2:
      i2 = i

  return i1 * i2

print(part2())

def part1():
  pairs = parsePairs()
  def compare(p1, p2):
    if type(p1) is int and type(p2) is int:
      if p1 < p2:
        return (True, True)
      elif p1 == p2:
        return (True, False)
      else:
        return (False, False)

    if type(p1) is int:
      p1 = [p1]

    if type(p2) is int:
      p2 = [p2]

    n = len(p1)
    m = len(p2)
    i = 0

    if m < n and m == 0:
      return False, False

    decided = False

    while i < max(n, m):
      if i < n and i == m:
        return False, False

      if i == n and i < m:
        return True, True

      res, decided = compare(p1[i], p2[i])

      if res and decided:
        return res, decided

      if not res:
        return (False, False)

      i+=1

    return (True, decided)

  total = 0
  for i, pair in enumerate(pairs, start=1):
    res, decided = compare(pair[0], pair[1])

    print(i, pair, res, decided)

    total += i if res else 0

  return total

# print(part1())
