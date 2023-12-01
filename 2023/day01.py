import re, time, collections, sys, functools

def getLines(filename):
  file = open(filename)
  lines = file.readlines()

  res = []
  for line in lines:
    res.append(line.strip())

  return res

def part2():
  mapp = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
  }

  lines = getLines('input01p2.txt')
  # lines = getLines('input01p2small.txt')
  res = 0
  for line in lines:
    ss = []
    text = ''
    for c in line:
      if c.isdigit():
        text = ''
        ss.append(int(c))
      else:
        text += c
        n = len(text)
        for i in range(n):
          t = text[i:n]
          if t in mapp:
            ss.append(mapp[t])
            # text = ''
            # break

    print(res, line, '|', ss, '|', ss[0] * 10 + ss[-1])
    #if len(ss) > 1:
    res += ss[0] * 10 + ss[-1]
    #else:
    #  res += ss[0]

  print(res)

def part1():
  lines = getLines('input01.txt')
  # lines = getLines('input01small.txt')
  res = 0
  for line in lines:
    ss = []
    for c in line:
      if c.isdigit():
        ss.append(int(c))

    res += ss[0] * 10 + ss[-1]

  print(res)


# part1()
part2()
