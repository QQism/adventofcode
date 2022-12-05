
def totalScore():
  f = open('input2.txt')

  mapScore = {
    'X': 1, # A. Rock
    'Y': 2, # B. Paper
    'Z': 3, # C. Scissors
  }

  drawLetter = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
  }

  winLetter = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B',
  }
  def compete(other, you):
    if drawLetter[you] == other:
      return 3
    return 6 if winLetter[you] == other else 0

  score = 0
  for line in f.readlines():
    line = line.strip()

    if len(line) == 0:
      continue

    other, you = line.split(' ')
    score += mapScore[you] + compete(other, you)

  print(score)

def totalScorePart2():
  f = open('input2small.txt')

  # X lose
  # Y draw
  # Z win
  mapScore = {
    'X': 1, # A. Rock
    'Y': 2, # B. Paper
    'Z': 3, # C. Scissors
  }

  drawLetter = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
  }

  loseLetter = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
  }

  winLetter = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
  }

  score = 0
  for line in f.readlines():
    line = line.strip()

    if len(line) == 0:
      continue

    other, decision = line.split(' ')

    if decision == 'X': # lose
      option = loseLetter[other]
    elif decision == 'Y': # draw
      option = drawLetter[other]
      score += 3
    else:
      option = winLetter[other]
      score += 6

    score += mapScore[option]

  print(score)
totalScorePart2()
