import re, time, collections, sys, functools, copy

def part1():
  file = open('input16small.txt')
  # file = open('input16.txt')

  lines = file.readlines()

  adj = {}
  rates = {}
  nodes = set()
  # rateNodes = []

  for line in lines:
    line = line.strip()

    m = re.match('Valve (.+) has flow rate=(.+); tunnel[s]? lead[s]? to valve[s]? (.+)$', line)

    if m:
      node, rate, links = m.groups()

      links = links.split(', ')
      rate = int(rate)
      rates[node] = rate

      if node not in nodes:
        nodes.add(node)
      # rateNodes.append((node, rate))

      for link in links:
        if link not in adj:
          adj[link] = set()
        if node not in adj:
          adj[node] = set()

        if link not in adj[node]:
          adj[node].add(link)

        if node not in adj[link]:
          adj[link].add(node)

  # rateNodes.sort(key=lambda x: x[1], reverse=True)

  nodesToOpen = []

  for k, v in rates.items():
    if v == 0:
      nodesToOpen.append(k)

  def findShortestPath(source, target):
    steps = 0
    visited = set()
    queue = [(source, [])]

    while len(queue) > 0:
      m = len(queue)
      for _ in range(m):
        node, path = queue.pop()

        if node in visited:
          continue

        visited.add(node)

        if node == target:
          return steps, path

        for nextNode in adj[node]:
          queue.append((nextNode, path + [node]))

      steps += 1

  def getPressure(nodes):
    currentPressure = 0
    for node in nodes:
      currentPressure += rates[node]

    return currentPressure


  paths = {}
  for source in nodes:
    paths[source] = {}

    for target in nodes:
      if target == source:
        continue

      paths[source][target] = findShortestPath(source, target)

  cache = {}

  print(paths)

  # find permutations
  permutations = []

  def findPermutations(i, perm):
    print(i, perm)
    if len(perm) == len(nodesToOpen):
      permutations.append(copy.copy(perm))
      return

    if i == len(nodesToOpen):
      return findPermutations(0, perm)

    node = nodesToOpen[i]
    if node in perm:
      return findPermutations(i + 1, perm)

    perm.add(node)
    findPermutations(i + 1, perm)

    perm.remove(node)
    findPermutations(i + 1, perm)


  findPermutations(0, set())

  print(permutations)

  return adj

part1()
# print(part1())
