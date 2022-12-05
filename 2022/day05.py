def part1():
  file = open('input5.txt')

  lines = file.readlines()

  stackData = []
  moveData = []
  stackEnded = False
  for line in lines:
    if len(line.strip()) == 0:
      stackEnded = True
      continue

    if stackEnded:
      moveData.append(line.strip())
    else:
      stackData.append(line)

  stackLine = stackData[-1].strip()
  stacks = [[] for i in range(int(stackLine[-1]))]

  for i, stack in enumerate(stacks):
    for j in range(len(stackData)-2, -1, -1):
      item = stackData[j][1+ (4 * i):1 + (4 * i) + 1].strip()

      if len(item) > 0:
        stack.append(item)

  import re

  for line in moveData:
    m = re.match("move (\d+) from (\d+) to (\d+)", line)
    move, fr, to = [int(s) for s in m.groups()]

    for i in range(move):
      item = stacks[fr-1].pop()
      stacks[to-1].append(item)

  print(''.join([stack[-1] for stack in stacks]))

def part2():
  file = open('input5.txt')

  lines = file.readlines()

  stackData = []
  moveData = []
  stackEnded = False
  for line in lines:
    if len(line.strip()) == 0:
      stackEnded = True
      continue

    if stackEnded:
      moveData.append(line.strip())
    else:
      stackData.append(line)

  stackLine = stackData[-1].strip()
  stacks = [[] for i in range(int(stackLine[-1]))]

  for i, stack in enumerate(stacks):
    for j in range(len(stackData)-2, -1, -1):
      item = stackData[j][1+ (4 * i):1 + (4 * i) + 1].strip()

      if len(item) > 0:
        stack.append(item)

  import re

  for line in moveData:
    m = re.match("move (\d+) from (\d+) to (\d+)", line)
    move, fr, to = [int(s) for s in m.groups()]

    temp = []
    for i in range(move):
      item = stacks[fr-1].pop()
      temp.append(item)

    stacks[to-1] += temp[::-1]

  print(''.join([stack[-1] for stack in stacks]))

print(part2())
