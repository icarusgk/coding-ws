import json

# encoding to json format is called serialization
# The key difference between these two methods is the type we're serializing to: 
# json.dump() writes to a file-like object, and json.dumps() creates a string.

movie_dict = {
  "movies": [
    {
      "title": "Inception",
      "director": "Christopher Nolan",
      "year": 2010
    },
    {
      "title": "The Lord of the Rings: The Fellowship of the Ring",
      "director": "Peter Jackson",
      "year": 2001
    },
    {
      "title": "Parasite",
      "director": "Bong Joon Ho",
      "year": 2019
    }
  ]
}

with open('movies.json', 'w') as json_file:
  json.dump(movie_dict, json_file)

years = {2020: "leap year", 2021: "regular year", 2022: "regular year",
         2023: "regular year", 2024: "leap year"}

years = json.dumps(years, indent=4)
print(years)

credentials = {
  'login': 'icarus',
  'password': ''
}

credentials_to_json = json.dumps(credentials)
print(credentials_to_json)