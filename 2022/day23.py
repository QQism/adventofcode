import re, time, collections, sys, functools


def render(grid, refresh=True, init=(0, 0), text=''):
  w = len(grid[0])
  h = len(grid)

  # data = [['s' if row == init[0] and col == init[1] else '.' for col in range(w)] for row in range(h)]

  if refresh:
    sys.stdout.write('\x1b[1A' * (h + 2))

  s = '\r'
  for row in grid:
    s += ''.join(row) + '\n'

  print(s)
  print(text)
  time.sleep(0.2)

class Elf:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

def part2():
  # file = open('input23small.txt')
  file = open('input23.txt')

  lines = file.readlines()

  elves = set()
  grid = {}

  def moveElf(elf, newPos):
    nonlocal grid

    x, y = elf.x, elf.y
    newX, newY = newPos

    if newY not in grid:
      grid[newY] = {}

    grid[newY][newX] = True

    grid[y][x] = None

    elf.x, elf.y = newX, newY

  def emptyCell(x, y):
    nonlocal grid

    if y not in grid:
      return True

    if x not in grid[y]:
      return True

    if not grid[y][x]:
      return True

  for j, line in enumerate(lines):
    line = line.strip()

    for i, c in enumerate(line):
      if c == '#':
        elves.add(Elf(i, j))

        if j in grid:
          grid[j][i] = True
        else:
          grid[j] = {i: True}

  dirs = ['T', 'B', 'L', 'R']
  steps = 0
  while True:
    proposed = {}
    for elf in elves:
      x, y = elf.x, elf.y

      checkTop = emptyCell(x, y-1) and emptyCell(x-1, y-1) and emptyCell(x+1, y-1)
      checkBottom = emptyCell(x, y+1) and emptyCell(x-1, y+1) and emptyCell(x+1, y+1)
      checkLeft = emptyCell(x-1, y) and emptyCell(x-1, y+1) and emptyCell(x-1, y-1)
      checkRight = emptyCell(x+1, y) and emptyCell(x+1, y+1) and emptyCell(x+1, y-1)

      if checkTop and checkBottom and checkLeft and checkRight:
        continue

      newPos = None
      for dir in dirs:
        if dir == 'T' and checkTop:
          newPos = (x, y-1)
          break
        elif dir == 'B' and checkBottom:
          newPos = (x, y+1)
          break
        elif dir == 'L' and checkLeft:
          newPos = (x-1, y)
          break
        elif dir == 'R' and checkRight:
          newPos = (x+1, y)
          break

      if newPos is None:
        continue

      if newPos not in proposed:
        proposed[newPos] = []

      proposed[newPos].append(elf)

    if len(proposed) == 0:
      print(steps + 1)
      return steps + 1

    for propose, candidates in proposed.items():
      if len(candidates) > 1:
        continue

      candidate = candidates[0]

      moveElf(candidate, propose)

    dirs = dirs[1:] + dirs[0:1]
    steps += 1

  topRow = float('inf')
  bottomRow  = -float('inf')
  leftCol = float('inf')
  rightCol = -float('inf')

  for row in grid:
    for col in grid[row]:
      if grid[row][col]:
        topRow = min(topRow, row)
        bottomRow = max(bottomRow, row)
        leftCol = min(leftCol, col)
        rightCol = max(rightCol, col)

  w = rightCol - leftCol + 1
  h = bottomRow - topRow + 1

  # print(w, h, grid)
  print(w, h)# grid)

  print(w * h - len(elves))


part2()

def part1():
  # file = open('input23small.txt')
  file = open('input23.txt')

  lines = file.readlines()

  elves = set()
  grid = {}

  def moveElf(elf, newPos):
    nonlocal grid

    x, y = elf.x, elf.y
    newX, newY = newPos

    if newY not in grid:
      grid[newY] = {}

    grid[newY][newX] = True

    grid[y][x] = None

    elf.x, elf.y = newX, newY

  def emptyCell(x, y):
    nonlocal grid

    if y not in grid:
      return True

    if x not in grid[y]:
      return True

    if not grid[y][x]:
      return True

  for j, line in enumerate(lines):
    line = line.strip()

    for i, c in enumerate(line):
      if c == '#':
        elves.add(Elf(i, j))

        if j in grid:
          grid[j][i] = True
        else:
          grid[j] = {i: True}

  dirs = ['T', 'B', 'L', 'R']
  for _ in range(10):
    proposed = {}
    for elf in elves:
      x, y = elf.x, elf.y

      checkTop = emptyCell(x, y-1) and emptyCell(x-1, y-1) and emptyCell(x+1, y-1)
      checkBottom = emptyCell(x, y+1) and emptyCell(x-1, y+1) and emptyCell(x+1, y+1)
      checkLeft = emptyCell(x-1, y) and emptyCell(x-1, y+1) and emptyCell(x-1, y-1)
      checkRight = emptyCell(x+1, y) and emptyCell(x+1, y+1) and emptyCell(x+1, y-1)

      if checkTop and checkBottom and checkLeft and checkRight:
        continue

      newPos = None
      for dir in dirs:
        if dir == 'T' and checkTop:
          newPos = (x, y-1)
          break
        elif dir == 'B' and checkBottom:
          newPos = (x, y+1)
          break
        elif dir == 'L' and checkLeft:
          newPos = (x-1, y)
          break
        elif dir == 'R' and checkRight:
          newPos = (x+1, y)
          break

      if newPos is None:
        continue

      if newPos not in proposed:
        proposed[newPos] = []

      proposed[newPos].append(elf)

    for propose, candidates in proposed.items():
      if len(candidates) > 1:
        continue

      candidate = candidates[0]

      moveElf(candidate, propose)

    dirs = dirs[1:] + dirs[0:1]

  topRow = float('inf')
  bottomRow  = -float('inf')
  leftCol = float('inf')
  rightCol = -float('inf')

  for row in grid:
    for col in grid[row]:
      if grid[row][col]:
        topRow = min(topRow, row)
        bottomRow = max(bottomRow, row)
        leftCol = min(leftCol, col)
        rightCol = max(rightCol, col)

  w = rightCol - leftCol + 1
  h = bottomRow - topRow + 1

  # print(w, h, grid)
  print(w, h)# grid)

  print(w * h - len(elves))


# part1()
