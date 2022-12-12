import re, math

class Monkey:
  def __init__(self) -> None:
    self.items = []
    self.op = ''
    self.comp = None
    self.test = None
    self.true = None
    self.false = None
    self.count = 0

def part1():
  file = open('input11small.txt')

  lines = file.readlines()

  monkeys = []
  for line in lines:
    line = line.strip()
    if re.match('Monkey .*:', line):
      monkeys.append(Monkey())

    monkey = monkeys[-1]

    m = re.match('Starting items: (.*)', line)

    if m:
      monkey.items = [int (i) for i in m.groups()[0].split(', ')]

    m = re.match('Operation: new = old ([\+\*]) (.*)', line)
    if m:
      monkey.op = m.groups()[0]
      monkey.comp = int(m.groups()[1]) if m.groups()[1] != 'old' else None

    m = re.match('Test: divisible by (.*)', line)
    if m:
      monkey.test = int(m.groups()[0])

    m = re.match('If true: throw to monkey (.*)', line)
    if m:
      monkey.true = int(m.groups()[0])

    m = re.match('If false: throw to monkey (.*)', line)
    if m:
      monkey.false = int(m.groups()[0])

  print(list(map(lambda m: m.items, monkeys)))
  print(list(map(lambda m: [m.op, m.comp], monkeys)))

  def round():
    nonlocal monkeys
    for monkey in monkeys:
      while len(monkey.items) > 0:
        monkey.count += 1
        item = monkey.items.pop()

        if monkey.op == '*':
          item = item * (monkey.comp if monkey.comp else item)
        elif monkey.op == '+':
          item = item + (monkey.comp if monkey.comp else item)

        item //= 3

        if item % monkey.test:
          monkeys[monkey.false].items.append(item)
        else:
          monkeys[monkey.true].items.append(item)

  for i in range(20):
    round()

  ranks = sorted(map(lambda m: m.count, monkeys))

  return ranks[-1] * ranks[-2]

class Item:
  def __init__(self, val) -> None:
    self.val = val
    self.mod = {}

def part2():
  file = open('input11.txt')

  lines = file.readlines()

  allMods = set()

  monkeys = []
  for line in lines:
    line = line.strip()
    if re.match('Monkey .*:', line):
      monkeys.append(Monkey())

    monkey = monkeys[-1]

    m = re.match('Starting items: (.*)', line)

    if m:
      monkey.items = [Item(int (i)) for i in m.groups()[0].split(', ')]

    m = re.match('Operation: new = old ([\+\*]) (.*)', line)
    if m:
      monkey.op = m.groups()[0]
      monkey.comp = int(m.groups()[1]) if m.groups()[1] != 'old' else None

    m = re.match('Test: divisible by (.*)', line)
    if m:
      monkey.test = int(m.groups()[0])
      allMods.add(monkey.test)

    m = re.match('If true: throw to monkey (.*)', line)
    if m:
      monkey.true = int(m.groups()[0])

    m = re.match('If false: throw to monkey (.*)', line)
    if m:
      monkey.false = int(m.groups()[0])

  print(list(map(lambda m: m.items, monkeys)))
  print(list(map(lambda m: [m.op, m.comp], monkeys)))

  for monkey in monkeys:
    for item in monkey.items:
      for mod in allMods:
        item.mod[mod] = item.val % mod

  def round():
    nonlocal monkeys, allMods
    for monkey in monkeys:
      while len(monkey.items) > 0:
        monkey.count += 1
        item = monkey.items.pop()

        if monkey.op == '*':
          if monkey.comp:
            for mod in allMods:
              item.mod[mod] *= monkey.comp
              item.mod[mod] %= mod
          else:
            for mod in allMods:
              item.mod[mod] *= item.mod[mod]
        elif monkey.op == '+':
          for mod in allMods:
            item.mod[mod] += monkey.comp

        # item //= 3

        if item.mod[monkey.test] % monkey.test:
          monkeys[monkey.false].items.append(item)
        else:
          monkeys[monkey.true].items.append(item)

  for i in range(10000):
    print('\rRound {round}'.format(round=i), end='\r')
    round()

  ranks = list(map(lambda m: m.count, monkeys))

  for i, monkey in enumerate(monkeys):
    print("Monkey {i}: {items}".format(i=i, items=len(monkey.items)))

  print(ranks)
  ranks.sort()
  return ranks[-1] * ranks[-2]

print(part2())
