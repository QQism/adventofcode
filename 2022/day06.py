def part1():
  file = open('input6.txt')

  lines = file.readlines()
  s = lines[0]
  n = len(s)

  count = {}
  i = 0
  j = 0

  # sliding window
  while j < n:
    size = j - i + 1

    if s[j] in count and count[s[j]] >= i:
      i = count[s[j]] + 1 # move to the new i
    elif size == 4:
      return j+1
    count[s[j]] = j

    j += 1

def part2():
  file = open('input6.txt')

  lines = file.readlines()
  s = lines[0]
  n = len(s)

  print(s)

  count = {}
  i = 0
  j = 0

  # sliding window
  while j < n:
    size = j - i + 1

    if s[j] in count and count[s[j]] >= i:
      i = count[s[j]] + 1 # move to the new i
    elif size == 14:
      return j+1

    count[s[j]] = j

    j += 1

print(part2())
