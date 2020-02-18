import os
import random
import sys
#import antigravity

from my_module import find_index, test

cities = ['London', 'New York', 'Miami', 'Tokyo', 'San Jose']

index = find_index(cities, 'London')

print(index)
print(test)

print(sys.path) #shows the paths python searches to import module

random_course  = random.choice(cities)

print(random_course)

print(os.getcwd()) # returns the path of the root directory
print(os.__file__) # prints the location of the os module. In this case notice that os is inside envs_gtp