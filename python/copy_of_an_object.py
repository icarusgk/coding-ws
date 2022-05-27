# With mutable objects if you assign one variable to another and then modify an 
# object using any of these variables, it will affect both variables.
a = [1]
b = a
a.append(2)

print(b)  # The same value as a [1, 2] will be printed instead of [1]


# * Copy a mutable: shallow copy
# Mutable containers e.g. a list, store references to objects that store values
# With shallow copying, we can create a copy of a list that contains the same objects
# but the reference to a container will be new

# There are two ways to do this
# The universal way is to use the copy function from the copy module, 
# it works with any object

import copy
lst = [2, 3, 9]
new_lst = copy.copy(lst)

# Also some containers as list, set, and dict have the copy method which can be used
# instead of the copy function
built_in_lst = lst.copy()

# ? In both cases, a new list is created that stores references to the same objects
print(lst, id(lst))            # [2, 3, 9] 140619533293760
print(new_lst, id(new_lst))    # [2, 3, 9] 140619533293824

lst[2] = 0
print(lst, id(lst))

# the new list remains the same
print(new_lst, id(new_lst))


# * Dicts
# When we use shallow copying, the values stored in a dict are not copied
menu = {
   'breakfast': ['porridge'],
   'lunch': ['soup', 'main course', 'compote'],
   'dinner': ['main course', 'dessert', 'tea'],
}

copy_menu = menu.copy()
# a new container is created:
print(id(menu), id(copy_menu))                      # 4353003592 4353042040

# but the stored values are the same
print(id(menu['lunch']), id(copy_menu['lunch']))    # 4353060296 4353060296

# The thing is, when using shallow copying, only the container is duplicated (key)
# but the elements (values) remain the same

# * Copy a mutable: deep copy
# The deepcopy function from the copy module creates a clone that doesn't relate to the
# initial object

lst = [[5, 2], [2, 3, 9]]
new_lst = copy.deepcopy(lst)

my_list = [[1], [2, 1]]
list_copy = copy.deepcopy(my_list)
print(id(my_list[0][0]), id(list_copy[1][1]))

from statistics import median