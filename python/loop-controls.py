pets = ['dog', 'cat', 'parrot']

# * break
for pet in pets:
  print(pet)
  if pet == 'cat':
    break

# * continue
for pet in pets:
  if pet == 'dog':
    continue
  print(pet)

count = 0
while True:
  print("I am Infinite Loop")
  count += 1
  if count == 13:
    break

# * loop else clause
for pet in pets:
  print(pet)
else:
  print('We need a turtle!')


pancakes = 2
while pancakes > 0:
    print("I'm the happiest human being in the world!")
    pancakes -= 1
    if pancakes == 0:
        print("Now I have no pancakes!")
        break
else:
    print("No pancakes...")