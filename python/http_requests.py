import requests

# Making a get request
res = requests.get('https://requests.readthedocs.io/en/master/')

# We can access the status code
print(res.status_code)

# The text of the request
# print(res.text)

# The encoding
print(res.encoding)

# And its headers
print(res.headers)

# Query parameters
# A query string is a convention for appending key-value pairs
# It is separated by a question mark sign ? from the URL

# Each key is separated from the value by an equality sign =
# The pairs are separated by an ampersand &

py_res = requests.get('http://python.org/search', params={
    'q': 'requests'
})


def google_search(query, num):
    r = requests.get('https://google.com/search',
                     params={'q': query, 'num': num})
    return r.url


# print(google_search('python', 1))



