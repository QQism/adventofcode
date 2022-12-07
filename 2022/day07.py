import bisect

class Dir:
  def __init__(self, name, parent):
    self.name = name
    self.subdir = {}
    self.parent = parent
    self.files = {}

  # need to cache it!
  def size(self):
    return sum([size for _, size in self.files.items()])

  # need to cache it!
  def totalSize(self):
    childTotal = sum([subdir.totalSize() for _, subdir in self.subdir.items()])
    return childTotal + self.size()

import re

def buildUpDirs(lines):
  root = Dir('/', None)
  dirs = set()
  cur = root
  for line in lines:
    # change directory
    m = re.match("\$ cd ([a-zA-Z0-9]+)", line)

    if m is not None:
      dirName = m.groups()

      if dirName not in cur.subdir:
        # Create a new dir
        newDir = Dir(dirName, cur)
        cur.subdir[dirName] = newDir
        if newDir not in dirs:
          dirs.add(newDir)

      cur = cur.subdir[dirName]
      continue

    # back to root
    m = re.match("\$ cd \/", line)

    if m is not None:
      cur = root
      continue

    m = re.match("\$ cd \.\.", line)

    if m is not None:
      cur = cur.parent
      continue

    m = re.match("(\d+) ([a-zA-Z0-9.]+)", line)

    if m is not None:
      size, filename = m.groups()
      if filename not in cur.files:
        cur.files[filename] = int(size)

  return dirs, root

def part1():
  file = open('input7small.txt')

  lines = file.readlines()

  dirs, root = buildUpDirs(lines)

  total = 0
  for dir in dirs:
    dirSize = dir.totalSize()
    if dirSize <= 100000:
      total += dirSize

  return total

def part2():
  file = open('input7.txt')

  lines = file.readlines()

  dirs, root = buildUpDirs(lines)

  totalSize = root.totalSize()
  maxSize = 70000000

  currentUsage = maxSize - totalSize

  mustFreeUp = 30000000 - currentUsage

  arr = []
  for dir in dirs:
    arr.append(dir.size())

  arr.sort()

  return arr[bisect.bisect_left(arr, mustFreeUp)]

print(part2())
