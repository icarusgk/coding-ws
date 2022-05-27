# Iterables and iterators
# any object we can loop over is an iterable

# * iter()
# __iter__() returns an iterator
# Iterators represent a stream of data
# They implement the __next__() method

# Example

my_list = [1, 2, 3]

# Create an iterator
my_iterator = iter(my_list)
print(my_iterator) # <list_iterator object at 0x7f0c06133c10>

print(next(my_iterator)) # 1
print(next(my_iterator)) # 2
print(next(my_iterator)) # 3
# print(next(my_iterator)) # StopIteration exception

# Python for loop will automatilcally create an iterator
# from a given iterable and get its elements one
# by one

# * zip()
# zip() takes several iterables and returns an iterator of tuples

first_names = ['John', 'Anna', 'Tom']
last_names = ['Smith', 'Williams', 'Davis']

for name, last_name in zip(first_names, last_names):
  print(name, last_name)

# John Smith
# Anna Williams
# Tom Davis

short_list = [1, 2, 3]
long_list = [10, 20, 30]
hi = [1, 2, 3]

for a, b, c in zip(short_list, long_list, hi):
    print(a, b, c + a, 'hi')

# 1 10
# 2 20
# 3 30

# zip has an optional strict parameter. When set a ValueError
# will be thrown when the values are exhausted

my_pets = ['Pistachio', 'Fluffy', 'Emperor']
your_pets = ['Claws', 'Grumpy', 'Mr. Cat', 'Naughty', 'Blue Paws']

for pet1, pet2 in zip(my_pets, your_pets):
    print(pet1, pet2)

# Pistachio Claws
# Fluffy Grumpy
# Emperor Mr. Cat

for pet1, pet2 in zip(my_pets, your_pets):
    print(pet1, pet2)

# Pistachio Claws
# Fluffy Grumpy
# Emperor Mr. Cat

# Traceback (most recent call last):
#    File "<pyshell#4>", line 1, in <module>
#      for pet1, pet2 in zip(my_pets, your_pets, strict=True):
#  ValueError: zip() argument 2 is longer than argument 1


# * enumerate()
# Takes an iterable and returs its elements one by one along
# with their indexes

months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for n, month in enumerate(months_list, start=1):
    print(n, month)

# 1 Jan
# 2 Feb
# 3 Mar
# 4 Apr
# 5 May
# 6 Jun
# etc.