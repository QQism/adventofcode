
def part1():
  file = open('input3.txt')

  lines = file.readlines()

  def getPriority(c):
    res = ord(c) - 96

    return res if res > 0 else res + 58

  total = 0
  for line in lines:
    length = len(line)
    mid = length // 2
    freq = {}

    for i in range(length):
      compartment = i // mid
      if line[i] not in freq:
        freq[line[i]] = compartment
      else:
        if freq[line[i]] != compartment:
          total += getPriority(line[i])
          break

  return total

def part2():
  file = open('input3.txt')

  lines = file.readlines()

  def getPriority(c):
    res = ord(c) - 96

    return res if res > 0 else res + 58

  global total
  total = 0
  count = 0
  freq = {}

  def wrapUp(freq):
    global total
    for k, v in freq.items():
      one, two, three = v
      if k != '\n' and one > 0 and two > 0 and three > 0:
        total += getPriority(k)

  for line in lines:
    for c in line:
      if c not in freq:
        freq[c] = [0, 0, 0]

      freq[c][count % 3] += 1

    if count % 3 == 2:
      wrapUp(freq)
      # Reset freq
      freq = {}

    count += 1

  return total

print(part2())
