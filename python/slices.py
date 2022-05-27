planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[2:7:2])  # ['Earth', 'Jupiter', 'Uranus']

name = 'roger'
print(name[:2]) # ro
print(name[2:]) # ger
print(name[:]) # the full copy of the sequence
print(name[::2]) # rgr

my_other_name = name[:] # roger

pets = ['dog', 'cat', 'parrot', 'gecko']

print(pets[-2:])   # ['parrot', 'gecko']
print(pets[:-2])   # ['dog', 'cat']
print(pets[::-1])  # ['gecko', 'parrot', 'cat', 'dog']
print(pets[::-2])  # ['gecko', 'cat']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[7:2:-1])  # [8, 7, 6, 5, 4]