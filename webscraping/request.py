import requests

res = requests.get('https://randomuser.me/api/?results=10')

data = res.json()

for user in data['results']:
  print(user['name']['first'])
