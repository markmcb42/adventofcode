
import sys
import numpy as np
from itertools import permutations

def getTripDistance(start, end, trips):

  for trip in trips:
    if start in trip and end in trip:
      return trip[2]
    
file = open('input', 'r')

cities = set()
trips = []

for line in file:

  # Save the unique cities
  data = line.split()
  cities.add(data[0])
  cities.add(data[2])

  # create list of tuples for each trip
  trip = (data[0], data[2], int(data[4]))
  trips.append(trip)
  
print('There are {} cities and {} trips'.format(len(cities), len(trips)))
print(cities)

routes = list(permutations(cities))
print('There are {} possible routes'.format(len(routes)))

final = 0
for route in routes:

  dist = 0 
  for i in range(len(route) -1):
    start = route[i]
    end = route[i+1]

    # Get trip distance
    dist += getTripDistance(start, end, trips) 

  if dist > final:
    final = dist

print('The longest distance is {}'.format(final))
