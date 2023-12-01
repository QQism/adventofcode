import re, time, collections, sys, functools

def part2():
  file = open('input22small.txt')
  # file = open('input22.txt')

  lines = file.readlines()

  grid = []

  maxLength = len(lines[0])

  cubeSize = 4
  # cubeSize = 50

  for i in range(len(lines)-2):
    line = lines[i]
    row = []

    for j in range(maxLength):
      if j >= len(line):
        row.append(' ')
      else:
        c = line[j]

        if c == '\n':
          continue
        else:
          row.append(c)

    grid.append(row)

  render(grid, refresh=False)

  instructions = re.split('([RL])', lines[-1].strip())

  start = (0, 0)
  foundStart = False
  for j, row in enumerate(grid):
    if foundStart:
      break

    for i, cell in enumerate(row):
      if cell == '.':
        start = (i, j)
        foundStart = True
        break

  print("Start: ", start)

  def move(pos, face, grid):
    x, y = pos
    newX, newY = x, y

    if face == 'R':
      newX = x + 1

      while newX == len(grid[0]) or grid[y][newX] == ' ':
        if newX == len(grid[0]):
          newX = 0
        else:
          newX += 1

      if grid[y][newX] == '#':
        return (x, y)
    elif face == 'L':
      newX = x - 1

      while newX < 0 or grid[y][newX] == ' ':
        if newX < 0:
          newX = len(grid[0])-1
        else:
          newX -= 1

      if grid[y][newX] == '#':
        return (x, y)
    elif face == 'T':
      newY = y - 1

      while newY < 0 or grid[newY][x] == ' ':
        if newY < 0:
          newY = len(grid)-1
        else:
          newY -= 1

      if grid[newY][x] == '#':
        return (x, y)

    elif face == 'B':
      newY = y + 1

      while newY == len(grid) or grid[newY][x] == ' ':
        if newY == len(grid):
          newY = 0
        else:
          newY += 1

      if grid[newY][x] == '#':
        return (x, y)

    return (newX, newY)

  # RLBT
  face = 'R'
  turnRight = {
    'T': 'R',
    'R': 'B',
    'B': 'L',
    'L': 'T',
  }

  turnLeft = {
    'T': 'L',
    'L': 'B',
    'B': 'R',
    'R': 'T',
  }
  currentPos = start
  for ins in instructions:
    if ins == 'R':
      face = turnRight[face]
    elif ins == 'L':
      face = turnLeft[face]
    else:
      steps = int(ins)

      for _ in range(steps):
        currentPos = move(currentPos, face, grid)

  print(currentPos, face)

  faceScore = {
    'R': 0,
    'L': 2,
    'B': 1,
    'T': 3
  }

  score =(currentPos[0] + 1) * 4 + (currentPos[1] + 1) * 1000 + faceScore[face]

  print(score)

part2()

def part1():
  # file = open('input22small.txt')
  file = open('input22.txt')

  lines = file.readlines()

  grid = []

  maxLength = len(lines[0])

  for i in range(len(lines)-2):
    line = lines[i]
    row = []

    for j in range(maxLength):
      if j >= len(line):
        row.append(' ')
      else:
        c = line[j]

        if c == '\n':
          continue
        else:
          row.append(c)

    grid.append(row)

  render(grid, refresh=False)

  instructions = re.split('([RL])', lines[-1].strip())

  start = (0, 0)
  foundStart = False
  for j, row in enumerate(grid):
    if foundStart:
      break

    for i, cell in enumerate(row):
      if cell == '.':
        start = (i, j)
        foundStart = True
        break

  print("Start: ", start)

  def move(pos, face, grid):
    x, y = pos
    newX, newY = x, y

    if face == 'R':
      newX = x + 1

      while newX == len(grid[0]) or grid[y][newX] == ' ':
        if newX == len(grid[0]):
          newX = 0
        else:
          newX += 1

      if grid[y][newX] == '#':
        return (x, y)
    elif face == 'L':
      newX = x - 1

      while newX < 0 or grid[y][newX] == ' ':
        if newX < 0:
          newX = len(grid[0])-1
        else:
          newX -= 1

      if grid[y][newX] == '#':
        return (x, y)
    elif face == 'T':
      newY = y - 1

      while newY < 0 or grid[newY][x] == ' ':
        if newY < 0:
          newY = len(grid)-1
        else:
          newY -= 1

      if grid[newY][x] == '#':
        return (x, y)

    elif face == 'B':
      newY = y + 1

      while newY == len(grid) or grid[newY][x] == ' ':
        if newY == len(grid):
          newY = 0
        else:
          newY += 1

      if grid[newY][x] == '#':
        return (x, y)

    return (newX, newY)

  # RLBT
  face = 'R'
  turnRight = {
    'T': 'R',
    'R': 'B',
    'B': 'L',
    'L': 'T',
  }

  turnLeft = {
    'T': 'L',
    'L': 'B',
    'B': 'R',
    'R': 'T',
  }
  currentPos = start
  for ins in instructions:
    if ins == 'R':
      face = turnRight[face]
    elif ins == 'L':
      face = turnLeft[face]
    else:
      steps = int(ins)

      for _ in range(steps):
        currentPos = move(currentPos, face, grid)

  print(currentPos, face)

  faceScore = {
    'R': 0,
    'L': 2,
    'B': 1,
    'T': 3
  }

  score =(currentPos[0] + 1) * 4 + (currentPos[1] + 1) * 1000 + faceScore[face]

  print(score)

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

# part1()
