import itertools

# * chain()
# The  itertools module implements other useful combinatorial functions, 
# such as product() and combinations().
students_maths = ['Ann', 'Kate', 'Tom']
students_english = ['Tim', 'Carl', 'Dean']
students_history = ['Jane', 'Mike']

for student in itertools.chain(students_maths, students_english, students_history):
    print(student)
# Ann
# Kate
# Tom
# Tim
# Carl
# Dean
# Jane
# Mike

# * product()
# takes several iterables and returns the elements of their 
# Cartesian product one by one.
first_list = ['Hi', 'Bye', 'How are you']
second_list = ['Jane', 'Anton']

for first, second in itertools.product(first_list, second_list):
    print(first, second)

# Hi Jane
# Hi Anton
# Bye Jane
# Bye Anton
# How are you Jane
# How are you Anton

# Trying to create a list containing 10^12 elements will result in a 
# memory error:
# too_long_list = list(itertools.product(range(1000000), range(1000000)))

# However, works with iterators:
my_iterator = itertools.product(range(1000000), range(1000000))
for i in range(5):
    print(next(my_iterator))

# (0, 0)
# (0, 1
# (0, 2) 
# (0, 3)
# (0, 4)

# * combinations()
my_iter = itertools.combinations(range(1, 1000000), 3)

for i in range(5):
    print(next(my_iter))

# (1, 2, 3)
# (1, 2, 4)
# (1, 2, 5)
# (1, 2, 6)
# (1, 2, 7)