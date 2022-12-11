def getDistance(pos1, pos2):
  return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def move(pos, dir):
  return (pos[0] + dir[0], pos[1] + dir[1])

def adjacent(pos1, pos2):
  distance = getDistance(pos1, pos2)
  return (pos1 == pos2) or (distance == 1) or (distance == 2 and pos1[0] != pos2[0] and pos1[1] != pos2[1])

def unitVector(pos1, pos2):
    diff = [pos1[0] - pos2[0], pos1[1] - pos2[1]]
    return (
      int(diff[0] / abs(diff[0])) if diff[0] != 0 else 0,
      int(diff[1] / abs(diff[1])) if diff[1] != 0 else 0,
      )

dirs = {
  'U': (1, 0),
  'D': (-1, 0),
  'L': (0, -1),
  'R': (0, 1),
}

reverseDirs = {
  'U': dirs['D'],
  'L': dirs['R'],
  'D': dirs['U'],
  'R': dirs['L'],
}

def part1():
  file = open('input9small.txt')

  lines = file.readlines()

  head = tail = (0, 0)
  visited = set()
  visited.add(tail)
  for line in lines:
    # head moving
    letter, steps = line.strip().split(' ')

    dir = [di * int(steps) for di in dirs[letter]]

    newHead = move(head, dir)

    distance = getDistance(newHead, tail)

    if (newHead == tail) or (distance == 1) or (distance == 2 and newHead[0] != tail[0] and newHead[1] != tail[1]):
      head = newHead
      continue

    # one step back, this is the pos tail ended up
    newTail = move(newHead, reverseDirs[letter])
    back = newTail

    while True :
      if back not in visited:
        visited.add(back)

      distance = getDistance(back, tail)
      print(back, tail, dir, reverseDirs[letter], distance)

      if distance == 1 and (back[0] == tail[0] or back[1] == tail[1]):
        break

      if distance == 2 and back[0] != tail[0] and back[1] != tail[1]:
        break

      back = move(back, reverseDirs[letter])

    head = newHead
    tail = newTail

  return len(visited)

class Node:
  def __init__(self, name, pos) -> None:
    self.name = name
    self.pos = pos
    self.next = None
    self.visited = set()
    self.visited.add(pos)

  def recordPos(self):
    if self.pos not in self.visited:
      # if self.name == 9: print(self.pos)
      self.visited.add(self.pos)

  def move(self, dir, moved=False):
    if not moved:
      self.pos = move(self.pos, dir)

    tail = self.next

    if adjacent(self.pos, tail.pos):
      return

    if self.pos[0] != tail.pos[0] or self.pos[1] != tail.pos[1]:
      tail.pos = move(tail.pos, unitVector(self.pos, tail.pos))

    tail.recordPos()

    if tail.next:
      tail.move(dir, True)

def part1new():
  file = open('input9.txt')

  lines = file.readlines()

  head = Node((0, 0))

  tail = Node((0, 0))
  head.next = tail

  for line in lines:
    # head moving
    letter, steps = line.strip().split(' ')

    steps = int(steps)

    dir = dirs[letter]

    for _ in range(steps):
      head.move(dir)

  return len(tail.visited)

def part2():
  file = open('input9small.txt')

  lines = file.readlines()

  init = (5, 11)

  head = Node('H', init)
  nodes = set()
  nodes.add(head)

  node = head

  render([], refresh=False, init=init)

  for i in range(1, 10):
    node.next = Node(i, init)
    node = node.next
    nodes.add(node)

  tail = node

  for line in lines:
    # head moving
    letter, steps = line.strip().split(' ')

    steps = int(steps)

    dir = dirs[letter]

    for _ in range(steps):
      head.move(dir)
      render(nodes, init=init, text=', '.join(['{name}:{pos}'.format(name=node.name, pos=node.pos) for node in nodes]))

  return len(tail.visited)

import time
import sys
import keyboard

def render(nodes, refresh=True, init=(0, 0), text=''):
  size = 30 # * 2
  w = 50
  h = size

  data = [['s' if row == init[0] and col == init[1] else '.' for col in range(w)] for row in range(h)]

  for node in nodes:
    cur = data[node.pos[0]][node.pos[1]]
    data[node.pos[0]][node.pos[1]] = str(node.name) if cur == '.' else cur

  if refresh:
    sys.stdout.write('\x1b[1A' * (h + 2))

  s = '\r'
  for row in data[::-1]:
    s += ''.join(row) + '\n'

  print(s)
  print(text)
  time.sleep(0.2)

  # keyboard.wait('space', suppress=True)

print(part2())
