import random

random.seed(4)
print(random.random())

print(random.uniform(3, 100)) # Returns a random float

print(random.randint(35, 53)) # Returns a random integer

print(random.choice('roger')) # Returns a random element from a sequence

print(random.randrange(3, 100, 5))  # 18
print(random.randrange(1, 5))       # 2
print(random.randrange(100))        # 44


tiny_list = ['a', 'apple', 'b', 'banana', 'c', 'cat']
random.shuffle(tiny_list)
print(tiny_list)  # ['apple', 'banana', 'a', 'cat', 'b', 'c']

print(random.sample(range(100), 12))  # [24, 33, 91]