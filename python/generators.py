# def multiples(a, n):
#     i = 1
#     result = []
#     while i <= n:
#         result.append(a * i)
#         i += 1
#     return result


# print(multiples(3, 5))
# # Outputs [3, 6, 9, 12, 15]

# print(multiples(2, 3))
# # Outputs [2, 4, 6]


# A custom generator can be declared in the same way as a regular function 
# with a single difference: the return keyword gets replaced with yield.

def multiples(a, n):
  i = 1
  while i <= n:
    yield a*i
    i += 1

# Calling a generator doesn't immediately execute it. 
# Instead, a generator object is returned that can be iterated over:

multiples_of_three = multiples(3, 5)

for n in multiples_of_three:
  print(f'multiple of 3: {n}')
print()

# * Generator Expressions
# () for defining a generator
numbers = [1, 2, 3]

my_generator = (n ** 2 for n in numbers)

for i in my_generator:
  print("i:", i, end=" ")
print()