import re, time, collections, sys, functools

def getLines(filename):
  file = open(filename)
  lines = file.readlines()

  res = []
  for line in lines:
    res.append(line.strip())

  return res

def part2():
  lines = getLines('input02.txt')

  res = 0

  for line in lines:
    m = re.match('Game (.*): (.*)', line)
    groups = m.groups()
    id = int(groups[0])
    turns = groups[1].split(';')
    valid = True
    maxx = {
      'red': 0,
      'green': 0,
      'blue': 0
    }
    for turn in turns:
      turn = turn.strip()
      cubes = turn.split(',')
      for cube in cubes:
        cube = cube.strip()
        num, color = cube.split(' ')
        num = int(num)

        maxx[color] = max(maxx[color], num)


    res += maxx['blue'] * maxx['red'] * maxx['green']
  print(res)

def part1():
  lines = getLines('input02.txt')

  all = {
    'red': 12,
    'green': 13,
    'blue': 14,
  }

  res = 0

  for line in lines:
    m = re.match('Game (.*): (.*)', line)
    groups = m.groups()
    id = int(groups[0])
    turns = groups[1].split(';')
    valid = True
    for turn in turns:
      turn = turn.strip()
      cubes = turn.split(',')
      for cube in cubes:
        cube = cube.strip()
        num, color = cube.split(' ')
        num = int(num)

        if color in all and all[color] - num >= 0:
          pass
        else:
          valid = False
          break

      if not valid:
        break

    if valid:
      res += id

  print(res)

part2()
