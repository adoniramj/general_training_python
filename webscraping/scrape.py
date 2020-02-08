import requests
from bs4 import BeautifulSoup

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'html.parser')

articles = soup.find_all('article')
print(articles[0])
article = soup.find('article')
#print(article.prettify())
#headline = article.h2.a.text 
#summary = article.find('div', class_="entry-content").p.text

# for article in articles:
#   print(article.h2.a.text)
#   print('x'*30)
#   print(article.find('div', class_="entry-content").p.text)
#   print('x'*30)