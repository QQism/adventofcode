import re, time, collections, sys, functools

def part2():
  file = open('input14.txt')

  liness = file.readlines()

  # x - top - bottom
  # y - left - right
  init = (0, 500)

  maxH = 0
  maxW = 0

  lines = []

  # fill up lines in matrix
  for line in liness:
    points = line.strip().split(' -> ')
    n = len(points)
    for i in range(n-1):
      start = list(map(lambda x: int(x), points[i].split(',')))
      end = list(map(lambda x: int(x), points[i+1].split(',')))

      maxH = max(maxH, start[1], end[1])
      maxW = max(maxW, start[0], end[0])

      lines.append((start, end))

  w = maxW * 100
  # w = maxW * 5
  h = maxH + 3
  matrix = [['.' for cell in range(w)] for row in range(h)]

  for line in lines:
    start = line[0]
    end = line[1]
    if start[0] == end[0]:
      # same col, so it's vertical line
      ps = range(start[1], end[1] + 1) if start[1] < end[1] else range(end[1], start[1] + 1)

      for p in ps:
        matrix[p][start[0]] = '#'
    else:
      # same row, so it's horizon line
      ps = range(start[0], end[0] + 1) if start[0] < end[0] else range(end[0], start[0] + 1)

      for p in ps:
        matrix[start[1]][p] = '#'

  matrix[-1] = ['#' for _ in range(w)]

  stop = False
  count = 0
  while not stop:
    sand = [init[0], init[1]]

    if matrix[sand[0]][sand[1]] == 'o':
      break

    # while sand[0] <= maxH:
    while True:
      x, y = sand[0], sand[1]
      # check if it hits # or o

      if matrix[x + 1][y] not in '#o':
        sand[0] = x + 1
      elif matrix[x + 1][y - 1] not in '#o':
        # check dia left
        sand[0] = x + 1
        sand[1] = y - 1
      elif matrix[x + 1][y + 1] not in '#o':
        sand[0] = x + 1
        sand[1] = y + 1
      else:
        matrix[x][y] = 'o'
        break

    count += 1

  # for i in range(len(matrix)):
  #   print(''.join(matrix[i][-20:]))

  print(count)
  # return lines

print(part2())

def part1():
  file = open('input14.txt')

  liness = file.readlines()

  # x - top - bottom
  # y - left - right
  init = (0, 500)

  maxH = 0
  maxW = 0

  lines = []

  # fill up lines in matrix
  for line in liness:
    points = line.strip().split(' -> ')
    n = len(points)
    for i in range(n-1):
      start = list(map(lambda x: int(x), points[i].split(',')))
      end = list(map(lambda x: int(x), points[i+1].split(',')))

      maxH = max(maxH, start[1], end[1])
      maxW = max(maxW, start[0], end[0])

      lines.append((start, end))

  w = maxW + 1
  h = maxH + 1
  matrix = [['.' for cell in range(w)] for row in range(h)]

  for line in lines:
    start = line[0]
    end = line[1]
    if start[0] == end[0]:
      # same col, so it's vertical line
      ps = range(start[1], end[1] + 1) if start[1] < end[1] else range(end[1], start[1] + 1)

      for p in ps:
        matrix[p][start[0]] = '#'
    else:
      # same row, so it's horizon line
      ps = range(start[0], end[0] + 1) if start[0] < end[0] else range(end[0], start[0] + 1)

      for p in ps:
        matrix[start[1]][p] = '#'

  stop = False
  count = 0
  while not stop:
    sand = [init[0], init[1]]

    while sand[0] <= maxH:
      x, y = sand[0], sand[1]
      # check if it hits # or o

      if sand[0] == maxH:
        stop = True
        break

      if matrix[x + 1][y] not in '#o':
        sand[0] = x + 1
      elif matrix[x + 1][y - 1] not in '#o':
        # check dia left
        sand[0] = x + 1
        sand[1] = y - 1
      elif matrix[x + 1][y + 1] not in '#o':
        sand[0] = x + 1
        sand[1] = y + 1
      else:
        matrix[x][y] = 'o'
        break

    count += 1

  for i in range(len(matrix)):
    print(''.join(matrix[i][-20:]))

  print(count - 1)
  # return lines

# print(part1())
