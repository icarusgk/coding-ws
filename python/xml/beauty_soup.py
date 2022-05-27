from bs4 import BeautifulSoup

file = open('example.xml', 'r').read()
soup = BeautifulSoup(file, 'xml')

print(soup.prettify())

# <?xml version="1.0" encoding="utf-8"?>
# <movie_library>
#  <movie>
#   <title year="1994">
#    Pulp Fiction
#   </title>
#   <director>
#    Quentin Tarantino
#   </director>
#  </movie>
#  <movie>
#   <title year="2001">
#    Mulholland Dr.
#   </title>
#   <director>
#    David Lynch
#   </director>
#  </movie>
# </movie_library>

# If the specified tags are not found, find() returns None;
# find_all() returns an empty list.

tag1 = soup.find('title')
print(tag1)  # <title year="1994">Pulp Fiction</title>

tag2 = soup.find_all("director")
print(tag2)
# [<director>Quentin Tarantino</director>, <director>David Lynch</director>]

# If a tag has an attribute, you can include it in the search
tag3 = soup.find("title", {"year": "1994"})
print(tag3)  # <title year="1994">Pulp Fiction</title>

# Alternative Way
# This will only return the first occurrence
print(soup.director)  # <director>Quentin Tarantino</director>

# You can also find out additional information about tags with
# main relationship types in XML files:

# * parent
print(tag3.parent)

# <movie>
# <title year="1994">Pulp Fiction</title>
# <director>Quentin Tarantino</director>
# </movie>

# * children
tag4 = soup.find("movie")
print(list(tag4.children))

# ['\n', <title year="1994">Pulp Fiction</title>, '\n',
# <director>Quentin Tarantino</director>, '\n']

# The .contents() method is similar to the children method, but it returns a list instead

print(tag4.contents)

# ['\n', <title year="1994">Pulp Fiction</title>, '\n',
# <director>Quentin Tarantino</director>, '\n']

# siblings() shows the tag that ar placed on the same level as the searched tag.
tag5 = soup.find("director")
print(tag5.previous_sibling)  # \n
print(list(tag5.previous_siblings))  # ['\n', <title year="1994">Pulp Fiction</title>, '\n']

tag3 = soup.find("title", {
    "year": "1994"
})
print(tag3.next_sibling)  # \n
print(list(tag3.next_siblings))  # ['\n', <director>Quentin Tarantino</director>, '\n']

# * Extracting information
# text method
tag2 = soup.find_all("director")

for t in tag2:
    print(t.text)

# Quentin Tarantino
# David Lynch

# Another helpful method is get()
tag1 = soup.find("title")
print(tag1.get("year"))  # 1994