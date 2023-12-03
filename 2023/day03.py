import re, time, collections, sys, functools

def getLines(filename):
  file = open(filename)
  lines = file.readlines()

  res = []
  for line in lines:
    res.append(line.strip())

  return res

def part2():
  # lines = getLines('input03small.txt')
  lines = getLines('input03.txt')

  n = len(lines)
  m = len(lines[0])

  grid = [[None for _ in range(m)] for _ in range(n)]

  dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
  ]
  res = 0

  def recordNums(num, count, row, col):
    for idx in range(col - count, col):
      grid[row][idx] = num

  for row in range(n):
    num = None
    count = 0

    for col in range(m+1):
      if col == m:
        if num is not None:
          recordNums(num, count, row, col)

        num = None
        count = 0
        continue

      c = lines[row][col]
      if c.isdigit():
        if num is None:
          num = 0

        num = num * 10 + int(c)
        count += 1

      else:
        if num is not None:
          recordNums(num, count, row, col)

        num = None
        count = 0

  for row in range(n):
    for col in range(m):
      c = lines[row][col]

      if c != '*':
        continue

      arr = []
      skips = []
      for x, y in dirs:
        adRow = row + x
        adCol = col + y

        if (adRow, adCol) in skips:
          continue

        if adRow >= n or adRow < 0 or adCol >= m or adCol < 0:
          continue

        nc = grid[adRow][adCol]
        if nc is not None:
          arr.append(nc)

          for idx in range(adCol + 1, m):
            if grid[adRow][idx] == None:
              break
            else:
              skips.append((adRow, idx))

      if len(arr) == 2:
        res += arr[0] * arr[1]

  print(res)

def part1():
  lines = getLines('input03small.txt')
  # lines = getLines('input03.txt')

  n = len(lines)
  m = len(lines[0])
  dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 1),
    (1, 0),
  ]
  res = 0
  for row in range(n):
    num = 0
    valid = False
    for col in range(m+1):
      if col == m:
        if valid:
          res += num
        valid = False
        num = 0
        continue

      c = lines[row][col]
      if c.isdigit():
        num = num * 10 + int(c)

        for x, y in dirs:
          adRow = row + x
          adCol = col + y

          if adRow >= n or adRow < 0 or adCol >= m or adCol < 0:
            continue

          nc = lines[adRow][adCol]
          if nc.isdigit() or nc == '.':
            continue
          else:
            valid = True
      else:
        if valid:
          res += num
        valid = False
        num = 0

  print(res)

part2()
