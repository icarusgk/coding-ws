from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.nature.com/articles/d41586-020-03621-6')

soup = BeautifulSoup(res.content, 'html.parser')

p = soup.find_all('p')

print(p)