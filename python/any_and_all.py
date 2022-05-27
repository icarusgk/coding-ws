# These functions work only with iterable objects
# e.g. strings and lists.

# * any() -> bool
# It returns True if an element or a group of elements in an iterable object
# are evaluated True. Otherwise, it returns False.
# I.e. Jam and Andy, got test results in the form of a list of True or False
# values. The test is passed if at least one answer is correct. Now you need to
# check if you and your friend passes that test.
your_results = [True, False, False]
print(any(your_results))  # True

andy_results = [False, False, False]
print(any(andy_results))  # False

jam_results = []
print(any(jam_results))  # False

# any() takes a list as an argument, then evaluates all the elements of this
# list to find at least one True, if so returns True, otherwise, False.


# * all() -> bool
# Works similar to any() but all() checks if all the elements of an iterable
# are True or False.

your_results = [True, False, False]
print(all(your_results))  # False

andy_results = [True, True, True]
print(all(andy_results))  # True

jam_results = []
print(all(jam_results))  # True. No False values result in True


scores = [1, 2, 3, 4]
boolean_scores = [score >= 3 for score in scores]  # [False, False, True, True]
print(any(boolean_scores))  # True
print(all(boolean_scores))  # False


# * Conditions
# any() and all() are used in conditions. It helps to check the elements
# of iterable objects quickly and to avoid complex constructions.

# Even amount of candies for valentines
box = [10, 20, 33]

if any([candy % 2 for candy in box]):
    print("It is not a proper gift.")
else:
    print("Perfect!")