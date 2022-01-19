import sys
from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = []
    self.graph = defaultdict(list)
    self.count = 0

  def addEdge(self, u, v):
    if v == 'start':
      print('Error')
    self.graph[u].append(v)

  def printAllPathsUtil(self, u, d, visited, counts, path):

    if u.islower():
      if counts[u] == 0:
        # if any other small cave is at to, mark this as visited
        if 2 in counts.values():
          visited[u] = True
        counts[u] += 1
      elif counts[u] == 1:
        counts[u] += 1
        # Set any other that is 1 to visited
        for key in counts.keys():
          if counts[key] == 1:
            visited[key] = True
        visited[u] = True
      elif counts[u] == 2:
        visited[u] = True

    path.append(u)

    # If current vertex is same as destination, then print
    # current path[]
    if u == d:
      self.count += 1
      print(path)
    else:
      # If current vertex is not destination
      # Recur for all the vertices adjacent to this vertex
      for i in self.graph[u]:
        if visited[i] == False:
          self.printAllPathsUtil(i, d, visited, counts, path)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    if u.islower():
      if counts[u] == 2:
        # Reset any nodes with count of 1 back to false
        for key in counts.keys():
          if counts[key] == 1:
            visited[key] = False
      counts[u] -= 1
    visited[u] = False

  # Prints all paths from 's' to 'd'
  def printAllPaths(self, s, d):

    # Mark all the vertices as not visited
    visited = {}
    for n in self.nodes:
      visited[n] = False

    counts = {}
    for n in self.nodes:
      counts[n] = 0

    # Create an array to store paths
    path = []

    # Call the recursive helper function to print all paths
    self.printAllPathsUtil(s, d, visited, counts, path)

file = open('input', 'r')

g = Graph()
nodes = set()

for line in file:
  line = line.strip()
  data = line.split('-')
  nodes.add(data[0])
  nodes.add(data[1])
  if 'start' in line:
    if 'start' == data[0]:
      g.addEdge(data[0], data[1])
    elif 'start' == data[1]:
      g.addEdge(data[1], data[0])
    else:
      print('start error')
      sys.exit()
    continue

  if 'end' in line:
    if 'end' == data[0]:
      g.addEdge(data[1], data[0])
    elif 'end' == data[1]:
      g.addEdge(data[0], data[1])
    else:
      print('End error')
      sys.exit()
    continue

  g.addEdge(data[0], data[1])
  g.addEdge(data[1], data[0])

for node in nodes:
  g.nodes.append(node)

print('Number of nodes is {}'.format(len(nodes)))
g.printAllPaths('start', 'end')
print('There are {} paths'.format(g.count))

