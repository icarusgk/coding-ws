import csv
from cs50 import get_string

 open('phonebook.csv', 'a')

name = get_string('Name: ')
number = get_string('Number: ')

# Expects a file as an argument
writer = csv.writer(file)

# Write a row
writer.writerow([name, number])

file.close()