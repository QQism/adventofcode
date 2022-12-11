import re

def part1():
  file = open('input10.txt')

  lines = file.readlines()

  queue = []
  x = 1

  for line in lines:
    line = line.strip()

    queue.append(None)

    m = re.match('addx (-*\d+)', line)

    if m:
      val = int(m.groups()[0])
      queue.append(val)

  trackedCycles = [20, 60, 100, 140, 180, 220]

  total = 0
  for i, instruction in enumerate(queue, start=1):
    # print(i, x, x * i, instruction)
    if i in trackedCycles:
      total += x * i

    if instruction:
      x += instruction

  print(total)
  return queue

canvas = (' ' * 40 + '\n') * 6

def part2():
  file = open('input10small.txt')

  lines = file.readlines()

  queue = []
  x = 1

  for line in lines:
    line = line.strip()

    queue.append(None)

    m = re.match('addx (-*\d+)', line)

    if m:
      val = int(m.groups()[0])
      queue.append(val)

  w = 40
  s = ''

  render('', refresh=False)

  for cycle, instruction in enumerate(queue, start=1):
    if x - 1 <= (cycle - 1) % w <= x + 1:
      s += '#'
    else:
      s += '.'

    if cycle % w == 0:
      s += '\n'

    if instruction:
      x += instruction

    render(s)

  return s

import sys, time

def render(s, refresh=True):
  if refresh:
    sys.stdout.write('\x1b[1A' * 7)

  content = ''
  n = len(s)
  for c in s:
    content += c

  for i in range(n, len(canvas)):
    content += canvas[i]

  time.sleep(0.04)
  print(content)

# print(part2())
part2()
