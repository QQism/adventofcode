import re, time, collections, sys, functools

def part2():
  # file = open('input15small.txt')
  file = open('input15.txt')

  lines = file.readlines()

  minX = float('inf')
  minY = float('inf')
  maxX = -float('inf')
  maxY = -float('inf')

  sensors = set()
  beacons = set()
  sensorMinDistance = {}

  def getDistance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

  for line in lines:
    line = line.strip()
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    m = re.match('Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)', line)

    if m:
      sx, sy, bx, by = [int(n) for n in m.groups()]

      sensor = (sx, sy)
      beacon = (bx, by)
      sensors.add(sensor)
      beacons.add(beacon)

      distance = getDistance(sensor, beacon)

      sensorMinDistance[sensor] = distance

      minX = min(minX, bx, sx - distance)
      minY = min(minY, by, sy - distance)
      maxX = max(maxX, bx, sx + distance)
      maxY = max(maxY, by, sy + distance)

  # print('minX', minX, 'maxX', maxX, 'minY', minY, 'maxY', maxY)
  minX = int(minX)
  maxX = int(maxX)
  print('minX', minX, 'maxX', maxX, 'minY', minY, 'maxY', maxY)

  print(len(sensors))
  print(len(beacons))
  print(sensorMinDistance)

  # size = 20 + 1
  size = 4000000 + 1
  print("==========")

  def outsideAllSensors(pos):
    res = True

    if pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size:
      return False

    for sensor in sensors:
      d = getDistance(pos, sensor)
      if d <= sensorMinDistance[sensor]:
        return False

    print(pos)
    print([(getDistance(pos, sensor), sensor) for sensor in sensors])
    return res

  def calculateRes(pos):
    return pos[0] * 4000000 + pos[1]

  d = 1
  excluded = set()
  while True:
    print(d, end="\r")
    for sensor in sensors:
      # clockwise
      pos = (sensor[0] - sensorMinDistance[sensor] - d, sensor[1])
      print(pos)
      # top left
      while pos[0] <= sensor[0]:
        if outsideAllSensors(pos):
          return pos, calculateRes(pos)
        else:
          excluded.add(pos)
          pos = (pos[0]+1, pos[1]-1)
      # top right
      while pos[1] <= sensor[1]:
        if outsideAllSensors(pos):
          return pos, calculateRes(pos)
        else:
          excluded.add(pos)
          pos = (pos[0]+1, pos[1]+1)
      # bottom right
      while pos[0] >= sensor[0]:
        if outsideAllSensors(pos):
          return pos, calculateRes(pos)
        else:
          excluded.add(pos)
          pos = (pos[0]-1, pos[1]+1)
      # bottom left
      while pos[1] >= sensor[1]:
        if outsideAllSensors(pos):
          return pos, calculateRes(pos)
        else:
          excluded.add(pos)
          pos = (pos[0]-1, pos[1]-1)
    d += 1

# print(part2())

def part1():
  file = open('input15small.txt')
  # file = open('input15.txt')

  lines = file.readlines()

  minX = float('inf')
  minY = float('inf')
  maxX = -float('inf')
  maxY = -float('inf')

  sensors = set()
  beacons = set()
  sensorMinDistance = {}

  def getDistance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

  for line in lines:
    line = line.strip()
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    m = re.match('Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)', line)

    if m:
      sx, sy, bx, by = [int(n) for n in m.groups()]

      sensor = (sx, sy)
      beacon = (bx, by)
      sensors.add(sensor)
      beacons.add(beacon)

      distance = getDistance(sensor, beacon)

      sensorMinDistance[sensor] = distance

      minX = min(minX, bx, sx - distance)
      minY = min(minY, by, sy - distance)
      maxX = max(maxX, bx, sx + distance)
      maxY = max(maxY, by, sy + distance)


  # y = 2000000
  y = 10

  count = 0
  minX = int(minX)
  maxX = int(maxX)
  print('minX', minX, 'maxX', maxX)

  print(len(sensors))
  print(len(beacons))

  for x in range(minX-4, maxX+1):
    pos = (x, y)

    if pos in beacons:
      continue

    # Find the closest sensor
    for sensor in sensors:
      d = getDistance(pos, sensor)

      if d <= sensorMinDistance[sensor]:
        count += 1
        print(pos)
        break

  print(count)

part1()
