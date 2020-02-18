print("Imported my_module")

test = 'Test string'

def find_index(to_search, target):
  for i, value in enumerate(to_search): #i is the index and value is the index respective value
    if value == target:
      return i
  return -1