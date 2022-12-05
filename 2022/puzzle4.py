def part1():
  file = open('input4.txt')

  lines = file.readlines()

  count = 0
  def toInverval(s):
    return [int(sub) for sub in s.split('-')]

  for line in lines:
    one, two = line.strip().split(',')

    interval1 = toInverval(one)
    interval2 = toInverval(two)

    if interval1[0] <= interval2[0] <= interval1[1] and interval1[0] <= interval2[1] <= interval1[1]:
      count += 1
    elif interval2[0] <= interval1[0] <= interval2[1] and interval2[0] <= interval1[1] <= interval2[1]:
      count += 1

  return count

def part2():
  file = open('input4.txt')

  lines = file.readlines()

  count = 0
  def toInverval(s):
    return [int(sub) for sub in s.split('-')]

  for line in lines:
    one, two = line.strip().split(',')

    interval1 = toInverval(one)
    interval2 = toInverval(two)

    if interval1[0] > interval2[0]:
      interval1, interval2 = interval2, interval1

    if interval2[0] <= interval1[1]:
      count += 1

  return count

print(part2())
