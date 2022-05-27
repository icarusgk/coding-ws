from collections import namedtuple

# makes subtypes of tuples with named elements
person_template = namedtuple('Person', ['name', 'age', 'occupation'])


# We can create named tuple entities
mary = person_template('Mary', '25', 'doctor')
david = person_template(name='David', age='33', occupation='laywer')

print(mary.name)
print(david)
print(david[2])

# A new named tuple can also be created from a list:
susanne = person_template._make(['Susanne', '23', 'journalist'])
print(susanne)  # Person(name='Susanne', age='23', occupation='journalist')

# We can replace the field values with new ones
mary = mary._replace(age='26')
print(mary)          # Person(name='Mary', age='26', occupation='doctor')
print(mary._fields)  # ('name', 'age', 'occupation')


susanne_info = susanne._asdict()
print(susanne_info)
# OrderedDict([('name', 'Susanne'), ('age', '23'), ('occupation', 'journalist')])