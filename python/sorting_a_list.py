# Put items in the order I need
# Two different ways
# * list.sort() & sorted(list)

# They sort the list in ascending order
numbers = [3, 2, 5, 4, 1]
numbers.sort() # sorts the list in-place
print(numbers)  # [1, 2, 3, 4, 5]

# Invoking sorted(list)
numbers = [3, 2, 5, 4, 1] # doesn't modify the array, returns a new one
print(sorted(numbers))  # [1, 2, 3, 4, 5]

# list.sort() only works with lists
# sorted() can work with other collections (sets, dictionaries, tuples)

# ? Reversing a list in reverse order
print(sorted(numbers, reverse=True)) # [5, 4, 3, 2, 1]

numbers.sort(reverse=True)
print(numbers)

strings = ['aa', 'b', 'aaa', 'q', 'qq']
strings.sort()
print(strings)  # ['aa', 'aaa', 'b', 'q', 'qq']

# * The key
# You can pass the key function, this function will be applied to
# each element in the list, and the list will be sorted depending
# on the results. 

names = ['Mary', 'James', 'Tom', 'Katarina', 'John']
names.sort(key=len)
print(names) # ['Tom', 'Mary', 'John', 'James', 'Katarina']

nums = [7, 4, 1, 5]
print(sorted(nums, key=lambda x: x % 2))


# Custom functions
def my_sorted(x):
    return x - int(x)

numbers = [1.5, 3.2, 4.3]
print(sorted(numbers, key=my_sorted))  # [3.2, 4.3, 1.5]


# Invoking list.reverse() reverses the order of elements in the 
# list in-place.

initial_list = [1, 2, 3, 4, 5]
reversed_list = initial_list.reverse()
print(reversed_list)  # None
print(initial_list)   # [5, 4, 3, 2, 1]

# The function reversed() returns a reverse iterator
numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number) 