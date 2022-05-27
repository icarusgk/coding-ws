numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# * map() function syntax

doubled_numbers = map(lambda x: 2*x, numbers)

print(list(doubled_numbers))

x_list = [1, 2, 3] 
y_list = [4, 5, 6]
z_list = [7, 8, 9] 

s = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))

print(s)
# The output is [12, 15, 18]


# * filter() 
# filter() takes a Boolean function and a iterable

odd_numbers = filter(lambda x: x % 2, numbers)
print(list(odd_numbers))