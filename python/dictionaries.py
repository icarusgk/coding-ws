# from_keys
planets = {'Venus', 'Earth', 'Jupiter'}

planets_dict = dict.fromkeys(planets)
print(planets_dict) # {'Jupiter': None, 'Venus': None, 'Earth': None}

value = 'planet'
planets_dict = dict.fromkeys(planets, value)
print(planets_dict)  # {'Earth': 'planet', 'Venus': 'planet', 'Jupiter': 'planet'}

satellites = ['Moon', 'Io', 'Europa']
planets_dict = dict.fromkeys(planets, [])
print(planets_dict) # {'Jupiter': [], 'Venus': [], 'Earth': []}

planets_dict['Earth'].append('hi')
planets_dict['Jupiter'].append('there')
planets_dict['Jupiter'].append('you')
print(planets_dict) 
# {'Venus': ['hi', 'there', 'you'], 'Earth': ['hi', 'there', 'you'], 'Jupiter': ['hi', 'there', 'you']}

planets_dict = {key: [] for key in planets}
planets_dict['Earth'].append('hi')
planets_dict['Venus'].append('there')
planets_dict['Jupiter'].append('you')
# {'Earth': ['hi'], 'Venus': ['there'], 'Jupiter': ['you']}
print(planets_dict)


# * Adding items
testable = {'September': '16°C', 'December': '-10°C'}
another_dictionary = {'June': '21°C'}

# adding items from another dictionary
testable.update(another_dictionary)
print(testable) # {'September': '16°C', 'December': '-10°C', 'June': '21°C'}

testable.update(October='10°C')
print(testable) # {'September': '16°C', 'December': '-10°C', 'June': '21°C', 'October': '10°C'}

# * Remove the key from a dictionary
return_value = testable.pop('December', 'no temperature')
print('return value: ', return_value)
print(testable)

# * Cleaning the dictionary
testable = {'September': '16°C', 'December': '-10°C', 'July': '23°C'}

# this will remove both the key and the value from dictionary object
del testable['September']

# deletes the whole dictionary
del testable

# 2. Remove all the items and return an empty dictionary
testable = {'September': '16°C', 'December': '-10°C', 'July': '23°C'}
testable.clear()
print(testable) # {}


