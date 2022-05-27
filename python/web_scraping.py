import requests
from bs4 import BeautifulSoup

r = requests.get('https://wiki.archlinux.org/title/ASUS_GA401I#CPU_frequency')


# Then we use BeautifulSoup() class to create a parse tree of our page.
# r.content is the binary response

# html.parser is a parser included in the standard Python library.
soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.prettify())


# * find()
# returns the first occurrence of the tag in the tree
# suitable when searching a specific tag

# If not found returns None

title = soup.find('title')

# * find_all()
# returns the list of all the results or an empty list if not found
p = soup.find_all('p')

# We can also specify our tag using supplementary attributes
p3 = soup.find_all('p', {'style': 'text-align: justify;'})

# returns all the content between an opening tag and a closing tag
# print(soup.head)


paragraphs = soup.find_all('p')

# for p in paragraphs:
    # Each p.text returns a text paragraph from the page.
    # print(p.text.strip() + '\n')

links = soup.find_all('a')

for link in links:
    print(link.get('href'))



