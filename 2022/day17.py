import re, time, collections, sys, functools, math, copy

LIMIT = 7

class Rock:
  def __init__(self) -> None:
    self.pos = (0, 0)
    self.w = 0
    self.h = 0

  def hit(self, grid):
    pass

  def rest(self, grid):
    pass

  def move(self, grid, dir):
    pass

  def topY(self):
    pass

  def render(self, grid):
    pass

class Horizon(Rock):
  '''
  ####
    ^
  '''
  def __init__(self) -> None:
    super()
    self.w = 4
    self.h = 1

  def move(self, grid, dir):
    x, y = self.pos

    newX, newY = x + dir[0], y + dir[1]

    # hit the left and right, do nothing
    if newX - 2 < 0 or newX + 1 >= LIMIT:
      return

    if newY >= len(grid):
      return

    if newX - 2 >= 0 and grid[newY][newX-2] != '.':
      return

    if newX + 1 < LIMIT and grid[newY][newX+1] != '.':
      return

    if (grid[newY][newX] != '.' or \
        grid[newY][newX - 1] != '.' or \
        grid[newY][newX - 2] != '.' or \
        grid[newY][newX + 1] != '.'):
      return

    self.pos = (newX, newY)

  def rest(self, grid):
    x, y = self.pos

    return y + 1 >= len(grid) or grid[y + 1][x - 1] != '.' or grid[y + 1][x] != '.' or grid[y + 1][x + 1] != '.'

  def topY(self):
    return self.pos[1]

  def render(self, grid):
    x, y = self.pos

    grid[y][x] = '#'
    grid[y][x-1] = '#'
    grid[y][x-2] = '#'
    grid[y][x+1] = '#'

class Plus:
  '''
    #
   ###
    #
  '''
  def __init__(self) -> None:
    super()
    self.w = 3
    self.h = 3

class El:
  '''
    #
    #
  ###
  '''
  def __init__(self) -> None:
    super()
    self.w = 3
    self.h = 3

class Vertical:
  '''
  #
  #
  #
  #
  '''
  def __init__(self) -> None:
    super()
    self.w = 1
    self.h = 4

class Square:
  '''
  ##
  ##
  '''
  def __init__(self) -> None:
    super()
    self.w = 2
    self.h = 2

def part1():
  file = open('input17small.txt')
  # file = open('input17.txt')

  lines = file.readlines()

  instructions = lines[0].strip()

  instructionMap = {
    '>': (1, 0),
    '<': (-1, 0),
  }

  instructionIdx = 0
  def nextInstruction():
    nonlocal instructionIdx

    if instructionIdx == len(instructions):
      instructionIdx = 0

    res = instructionMap[instructions[instructionIdx]]

    instructionIdx += 1

    return res

  rockIdx = 0
  # rockTypes = [Horizon, Plus, El, Vertical, Square]
  rockTypes = [Horizon]
  def nextRock() -> Rock:
    nonlocal rockIdx

    if rockIdx == len(rockTypes):
      rockIdx = 0

    res = rockTypes[rockIdx]()

    rockIdx += 1

    return res

  w = 7
  # h = 4 * 2023
  h = 20 # 4 * 2023
  blankGrid = [['.' for _ in range(w)] for _ in range(h)]

  grid = copy.deepcopy(blankGrid)

  count = 0
  lastTipRockPos = h
  render(blankGrid, refresh=False)
  rocks = []
  while True:
    #print(lastTipRockPos)
    rock = nextRock()
    #print(rock)

    rock.pos = (2 + (rock.w // 2), lastTipRockPos - 3)
    rocks.append(rock)
    #print(rock.pos)

    count += 1

    while True:
      #grid = copy.deepcopy(blankGrid)

      #for r in rocks:
      #  r.render(grid)

      instruction = nextInstruction()

      rock.move(grid, (0, 1))
      # print(rock.pos, rock.topY())

      rock.move(grid, instruction)

      if rock.rest(grid):
        lastTipRockPos = rock.topY()
        rock.render(grid)
        break

      # render(grid, refresh=True, text=f"{str(rock.pos[0]), str(rock.pos[1])}")
    render(grid, refresh=True, text=f"{str(rock.pos[0]), str(rock.pos[1])}")
    if count == 3:
      break

  # print(lastTipRockPos)
  print([str(rock.pos) for rock in rocks])

def render(grid, text='', refresh=True):
  w = len(grid[0])
  h = len(grid)

  if refresh:
    sys.stdout.write('\x1b[1A' * (h + 1))

  for row in grid:
    print(''.join(row))

  print(text)

  time.sleep(0.5)
part1()
