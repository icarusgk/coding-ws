democrats = {'Kennedy', 'Obama'}
republicans = {'Trump', 'Lincoln'}
presidents = democrats.union(republicans)
print(presidents)  # {'Kennedy', 'Obama', 'Lincoln', 'Trump'}

democrats = {'Kennedy', 'Obama'}
republicans = {'Trump', 'Lincoln'}
# operator
presidents = democrats | republicans
# method
also_presidents = democrats.union(republicans)
# let's compare
print(presidents == also_presidents)
# The output is True

# * Intersection
light_side = {'Obi-Wan', 'Anakin'}
dark_side = {'Palpatine', 'Anakin'}
both_sides = light_side.intersection(dark_side)
print(both_sides)
# The output is {'Anakin'}
print(light_side & dark_side)
# The output is {'Anakin'}

# * Intersection Update
creatures = {'human', 'rabbit', 'cat'}
pets = {'rabbit', 'cat'}
creatures.intersection_update(pets)
print(creatures)
# The output is {'rabbit', 'cat'}
beasts = {'crocodile', 'cat'}
creatures &= beasts
print(creatures)
# The output is {'cat'}


# * Difference

painters = {'Klimt', 'Michelangelo', 'Picasso'}
ninja_turtles = {'Michelangelo', 'Leonardo'}
print(painters.difference(ninja_turtles))
# The output is {'Klimt', 'Picasso'}
print(painters - ninja_turtles)
# The output is {'Klimt', 'Picasso'}

# * Difference Update

criminals = {'Al Capone', 'Blackbeard', 'Bonnie and Clyde'}
gangsters = {'Al Capone'}
pirates = {'Blackbeard'}

criminals.difference_update(gangsters)
criminals -= pirates
print(criminals)
# The output is {'Bonnie and Clyde'}


# sets are within a container
languages = [{'Bourbon Street', 'Pilotow Street', 'Prospekt Avenue'}, {'Sunset Boulevard', 'Sesame Street'}, {'Sunset Boulevard', 'Elm Street'}]
the_best = set.intersection(*languages)
print(the_best)
# The output is {'python'}