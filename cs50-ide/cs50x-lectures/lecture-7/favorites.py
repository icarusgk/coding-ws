import csv
from cs50 import SQL

# Creates the file
open ('shows.db', 'w').close()

# Opens the empty file as a sqlite database
db = SQL('sqlite:///shows.db')

# Use SQL inside of Python
# Creates tables
db.execute('CREATE TABLE shows (id INTEGER, title TEXT, PRIMARY KEY(id))')
db.execute('CREATE TABLE genres (show_id INTEGER, genre TEXT, FOREIGN KEY(show_id) REFERENCES shows(id)')

with open('Favorite TV Shows - Form Responses 1.csv', 'r') as file:
  reader = csv.DictReader(file)
  for row in reader:
    title = row['title'].strip().upper()

    # ? is a placeholder
    db.execute('INSERT INTO (title) VALUES(?)', title)