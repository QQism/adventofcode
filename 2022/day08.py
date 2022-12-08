def part1():
  file = open('input8.txt')

  lines = file.readlines()
  matrix = [[c for c in row.strip()] for row in lines]

  w = len(matrix[0])
  h = len(matrix)
  outsideCount = (w * 2) + ((h - 2) * 2)

  # Top, left, bottom, right
  maxData = [[[0, 0, 0, 0] for _ in row.strip()] for row in lines]

  # Fill up boundary
  for row in range(h):
    for col in range(w):
      if row == 0:
        maxData[row][col][0] = matrix[row][col]

      if row == (h-1):
        maxData[row][col][2] = matrix[row][col]

      if col == 0:
        maxData[row][col][1] = matrix[row][col]

      if col == (w-1):
        maxData[row][col][3] = matrix[row][col]

  visible = set()
  # Check for the top and left
  for row in range(1, h-1):
    for col in range(1, w-1):
      val = matrix[row][col]

      pos = (row, col)

      # Check for the top
      if maxData[row-1][col][0] < val and pos not in visible:
        visible.add(pos)

      # check for the left
      if maxData[row][col-1][1] < val and pos not in visible:
        visible.add(pos)

      maxData[row][col][0] = max(val, maxData[row-1][col][0])
      maxData[row][col][1] = max(val, maxData[row][col-1][1])

  # Check for the bottom right
  for row in range(h-2, 0, -1):
    for col in range(h-2, 0, -1):
      val = matrix[row][col]

      pos = (row, col)

      # Check for the bottom
      if maxData[row+1][col][2] < val and pos not in visible:
        visible.add(pos)

      # check for the left
      if maxData[row][col+1][3] < val and pos not in visible:
        visible.add(pos)

      maxData[row][col][2] = max(val, maxData[row+1][col][2])
      maxData[row][col][3] = max(val, maxData[row][col+1][3])

  return len(visible) + outsideCount

def part2():
  file = open('input8.txt')

  lines = file.readlines()
  matrix = [[c for c in row.strip()] for row in lines]

  w = len(matrix[0])
  h = len(matrix)
  outsideCount = (w * 2) + ((h - 2) * 2)

  def lookTop(pos, val):
    row, col = pos

    count = 0
    while (row-1) >= 0:
      if matrix[row-1][col] >= val:
        count +=1
        break

      count += 1
      row -= 1

    return count

  def lookLeft(pos, val):
    row, col = pos

    count = 0
    while col-1 >= 0:
      if matrix[row][col-1] >= val:
        count +=1
        break

      count += 1
      col -= 1

    return count

  def lookBottom(pos, val):
    nonlocal h
    row, col = pos

    count = 0
    while row+1 < h:
      if matrix[row+1][col] >= val:
        count +=1
        break

      count += 1
      row += 1

    return count

  def lookRight(pos, val):
    nonlocal w
    row, col = pos

    count = 0
    while col+1 < w:
      if matrix[row][col+1] >= val:
        count +=1
        break

      count += 1
      col += 1

    return count

  maxScore = 0
  for row in range(1, h-1):
    for col in range(1, w-1):
      pos = (row, col)
      # top
      top = lookTop(pos, matrix[row][col])
      # left
      left = lookLeft(pos, matrix[row][col])
      # bottom
      bottom = lookBottom(pos, matrix[row][col])
      # right
      right = lookRight(pos, matrix[row][col])

      maxScore = max(maxScore, top * left * bottom * right)

  return maxScore

print(part2())
