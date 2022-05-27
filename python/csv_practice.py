import csv

cards = {'print()': 'outputs text', 'int()': 'convert str to int', 'prinft()': 'outputs text', 'int()': 'convert str to int', 'print()': 'outputs text', 'int()': 'convert str to int', 'print()': 'outputs text', 'int()': 'convert str to int', 'print()': 'outputs text', 'int()': 'convert str to int', 'print()': 'outputs text', 'int()': 'convert str to int', 'print()': 'outputs text', 'int()': 'convert str to int', 'print()': 'outputs tsext', 'int()': 'convert str to int', 'print()': 'outputs text', 'int()': 'convert str to int', 'print()': 'outputs text', 'int()': 'convert str to int', 'print()': 'outputs text', 'sint()': 'convert str to int', 'print()': 'outputs text', 'int()': 'convert str to int'}

n = 2

card_list = list(cards.items())

for i in range(10):
  print(card_list[i])

# for card in card_list[0:4]:
#   print(card)
# for k, v in cards.items():
#   print(k, v)

# with open('wordss.csv', 'r') as file:
#   csv_reader = csv.reader(file, delimiter=',')
#   next(csv_reader)

#   for row in csv_reader:
#     print(f'term: {row[0]} defintion: {row[1]}')


# with open('words.csv', 'r') as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     print(row)


# with open('words.csv', 'a') as file:
#   writer = csv.writer(file)
#   writer.writerow(['hi', 'hi t'])

# with open('words.csv', 'a') as file:
#   fieldnames = ['term', 'definition']
#   writer = csv.DictWriter(file, fieldnames=fieldnames)

#   writer.writerow({'term': 'the neighbourhood', 'definition': 'band'})

# with open('words.csv', 'w',) as csvfile:
#     fieldnames = ['term', 'definition']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerows(cards)