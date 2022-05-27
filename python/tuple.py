empty_tuple = ()
print(type(empty_tuple)) # <class 'tuple'>

#  It's actually a comma that makes a tuple, not parentheses.
now_a_tuple = ('a',)
print(now_a_tuple) # <class 'tuple'>

# In fact, even if your tuple contains more than one element, 
# separating items with commas will be enough:
weekend = 'Saturday', 'Sunday'
print(weekend)        # ('Saturday', 'Sunday')
print(type(weekend))  # <class 'tuple'>

# The built-in function tuple() turns strings, lists and other 
# iterables into a tuple.

bakers_dozen = tuple([12, 1])
print(bakers_dozen) # (12, 1)

sound = tuple('meow')
print(sound) # # ('m', 'e', 'o', 'w')


# WHAT CAN WE DO WITH TUPLES???

empty_tuple = ()
print(empty_tuple[0])  # IndexError

# Both lists and tuples are ordered
# Tuples are also indifferent to the nature of data stored in them, 
# so you can duplicate values or mix different data types:
tiny_tuple = (0, 1, 0, 'panda', 'sloth')

print(len(tiny_tuple))  # 5
print(tiny_tuple)       # (0, 1, 0, 'panda', 'sloth')

# Just like lists, tuples support indexing.
numbers = (0, 1, 2)
print(numbers[0])   # 0
print(numbers[1])   # 1
print(numbers[2])   # 2
print(numbers[3])   # IndexError

# And here the first distinctive feature of tuples comes into play. 
# What they don't support is item assignment.
# ex-capitals
capitals = ['Philadelphia', 'Rio de Janeiro', 'Saint Petersburg']

capitals[0] = 'Washington, D.C.'
capitals[1] = 'Brasília'
capitals[2] = 'Moscow'
print(capitals)  # ['Washington, D.C.', 'Brasília', 'Moscow']

former_capitals = tuple(capitals)
former_capitals[0] = 'Washington, D.C.'  # TypeError

