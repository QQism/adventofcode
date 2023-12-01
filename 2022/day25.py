import re, time, collections, sys, functools

def part1():
  file = open('input25small.txt')
  #file = open('input25.txt')

  lines = file.readlines()

  m = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
  }

  em = {
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '=',
  }

  def convert(line):
    tmp = 0

    n = len(line)

    for i in range(len(line)-1, -1, -1):
      power = 5 ** (n - i - 1)

      tmp += power * (m[line[i]])

    return tmp

  res = 0
  for line in lines:
    line = line.strip()
    res += convert(line)

  extract = []

  print(res)
  res = 12345
  i = 0
  while res > 0:
    rem = res % 5
    # print(res, rem, " >> ", em[rem], rem * (5 ** i))

    remain = 0
    if rem > 2:
      rem -= 5
      remain = 5 ** i

    if rem == 0 and i > 0:
      rem = 1
      remain = -5 ** i

    print(res, rem, " >> ", em[rem], rem * (5 ** i))

    extract.append(em[rem])
    res = (res + remain) // 5
    i += 1

  newRes = ''.join(reversed(extract))

  print(newRes, ' >>> ', convert(newRes))


part1()
