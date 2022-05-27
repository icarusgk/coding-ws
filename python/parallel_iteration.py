# The zip function can take any number of iterable and then return an iterator
# of tuples

numbers = [1, 2, 3]
words = ['one', 'two', 'three']
zip_iterator = zip(numbers, words)

# [(1, 'one'), (2, 'two'), (3, 'three')]


# Convert the zip object (iterator) into a list
print(list(zip_iterator))


# You can pass any iterable to zip()
my_string = 'AFK'
my_tuple = ('Away', 'From', 'Keyboard')
zip_iterator = zip(my_string, my_tuple)  # Returns an iterator
print(list(zip_iterator))

# [('A', 'Away'), ('F', 'From'), ('K', 'Keyboard')]


# If you pass iterables of different lenghts to zip(), the numbers
# of the resulting tuples will always be equal to the shortest
# iterable. Any remaining data will be discarded.
shortest = {'this', 'is', 'a', 'set'}
longest = [True, True, True, True, False, False]
zip_iterator = zip(shortest, longest)
print(list(zip_iterator))

# [('a', True), ('set', True), ('this', True), ('is', True)]
# The order is different because of the iterable being a set

# You can pass only one iterable to zip().
# The resulting iterator will contain single element tuples.
solo_string = 'Han Solo'
zip_iterator = zip(solo_string)
print(list(zip_iterator))

# [('H',), ('a',), ('n',), (' ',), ('S',), ('o',), ('l',), ('o',)]


# * zip() in loops
# One of the most common uses of zip() is to loop over multiple
# iterables simultaneously. It is called # ? Parallel iteration

planets = ['Earth', 'The Moon', 'Mars']
colors = ['blue', 'gray', 'red']
visited = [True, True, False]

for planet, color, visit in zip(planets, colors, visited):
  print(f'{planet} is {color}')
  print(f'Visited = {visit}')

# Earth is blue
# Visited = True
# The Moon is gray
# Visited = True
# Mars is red
# Visited = False


# * Parallel iteration with dictionaries
hero = {
  'name': 'Peter',
  'age': 13
}

villain = {
  'name': 'Hook',
  'age': 41
}

zipped = zip(hero.items(), villain.items())
print(list(zipped))

# [(('name', 'Peter'), ('name', 'Hook')), (('age', 13), ('age', 41))]

zipped = zip(hero.items(), villain.items())
for (hero_key, hero_value), (villain_key, villain_value) in zipped:
  print(f"The hero's {hero_key} is {hero_value}")
  print(f"The villain's {villain_key} is {villain_value}")


# * Unzipping
# Unzipping a sequence is as simple as adding an unpacking operator to an
# iterable provided to zip()
phrase = [('A', 'Away'), ('F', 'From'), ('K', 'Keyboard')]
unzipped = zip(*phrase)
print(list(unzipped))

# [('A', 'F', 'K'), ('Away', 'From', 'Keyboard')]
