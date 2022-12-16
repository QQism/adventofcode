import re, time, collections, sys

def climb(start, end, matrix):
  h = len(matrix)
  w = len(matrix[0])

  def validClimb(pos1, pos2):
    nonlocal matrix, h, w

    if pos2[0] < 0 or pos2[0] >= h or pos2[1] < 0 or pos2[1] >= w:
      return False

    h1 = matrix[pos1[0]][pos1[1]]
    h2 = matrix[pos2[0]][pos2[1]]

    return ord(h2) - ord(h1) <= 1

  q = collections.deque()

  q.appendleft((start, []))
  toBeVisted = set()

  steps = 0

  render(toBeVisted, (h, w), refresh=False, init=start, text=steps)
  while len(q) > 0:
    n = len(q)
    for _ in range(n):
      pos, path = q.popleft()

      row, col = pos

      if pos == end:
        # print("Found", end)
        render(toBeVisted, (h, w), refresh=True, init=start, text=path)
        # print(path)
        return steps

      for dir in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        if validClimb(pos, dir) and dir not in toBeVisted:
          q.append((dir, path + [dir]))
          toBeVisted.add(dir)
          render(toBeVisted, (h, w), refresh=True, init=start, text=steps)
    steps += 1

  return float('inf')

def part2():
  file = open('input12.txt')

  lines = file.readlines()

  matrix = [[c for c in row.strip()] for row in lines]

  h = len(matrix)
  w = len(matrix[0])
  # Find S
  starts = []
  for row in range(h):
    for cell in range(w):
      if matrix[row][cell] == 'S':
        matrix[row][cell] = 'a'
      if matrix[row][cell] == 'a':
        starts.append((row, cell))

  end = (0, 0)
  for row in range(h):
    for cell in range(w):
      if matrix[row][cell] == 'E':
        end = (row, cell)
        matrix[row][cell] = 'z'
        break

  print("Number of starts: ", len(starts))
  minn = float('inf')
  for start in starts:
    res = climb(start, end, matrix)

    if res < minn:
      minn = res

  return minn

def part1():
  file = open('input12.txt')

  lines = file.readlines()

  matrix = [[c for c in row.strip()] for row in lines]

  h = len(matrix)
  w = len(matrix[0])
  # Find S
  start = (0, 0)
  for row in range(h):
    for cell in range(w):
      if matrix[row][cell] == 'S':
        start = (row, cell)
        matrix[row][cell] = 'a'
        break

  end = (0, 0)
  for row in range(h):
    for cell in range(w):
      if matrix[row][cell] == 'E':
        end = (row, cell)
        matrix[row][cell] = 'z'
        break

  return climb(start, end, matrix)

def render(nodes, size, refresh=True, init=(0, 0), text=''):
  return
  w = size[1]
  h = size[0]

  data = [['s' if row == init[0] and col == init[1] else '.' for col in range(w)] for row in range(h)]

  for node in nodes:
    data[node[0]][node[1]] = '>'

  if refresh:
    sys.stdout.write('\x1b[1A' * (h + 2))

  s = '\r'
  for row in data:
    s += ''.join(row) + '\n'

  print(s)
  print(text)
  time.sleep(0.2)

# print(part1())
print(part2())
