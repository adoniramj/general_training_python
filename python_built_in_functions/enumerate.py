"""
enumerate allows to loop through a list and obtain the index and the value at the same time. 
Also works for tuples, sets
"""

cities = ['London', 'New York', ' Miami', 'Tokyo', 'San Jose']

for i, value in enumerate(cities):
  print('The index is %d and the city is %s' % (i, value))