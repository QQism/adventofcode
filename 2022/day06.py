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
      newI = count[s[j]] + 1 # move to the new i
      del count[s[i]] # but first undo the i check
      i = newI
      count[s[j]] = j
    else:
      count[s[j]] = j

      if size == 4:
        return j+1

    j += 1

def part2():
  file = open('input6.txt')

  lines = file.readlines()
  s = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
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
      newI = count[s[j]] + 1 # move to the new i
      del count[s[i]] # but first undo the i check
      i = newI
      count[s[j]] = j
    else:
      count[s[j]] = j

      if size == 14:
        return j+1

    j += 1

print(part2())
