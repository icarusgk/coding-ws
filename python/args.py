# If you don't want to limit the number of arguments that your function might take
# use the following syntax

# This works for any variable name as long as there is a single asterisk * right before it.

def add(a, b, *args):
  total = a + b
  for n in args:
    total += n
  return total

# The length of `args` is 3
print(add(1, 2, 3, 4, 5))

# The length of `args` is 0
print(add(1, 2))

def recipe(*args, sep=" or "):
    return sep.join(args)


print(recipe("meat", "fish"))               # meat or fish
print(recipe("meat", "fish", sep=" and "))  # meat and fish


def add(*args):
    total = 0
    for n in args:
        total += n
    return total


small_numbers = [1, 2, 3]
large_numbers = [9999999, 1111111]

print(add(*small_numbers))  # 6
print(add(*large_numbers))  # 11111110