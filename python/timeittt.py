import timeit

print(timeit.timeit(stmt="a=5;b=7;result=a+b"))
print(timeit.repeat(stmt="a=5;b=7;result=a+b", repeat=3))

# returns: 0.10849280000002182
timeit.timeit(stmt='math.sqrt(4)', setup='import math')

# the Timer class
snippet = '[x for x in range(1, 100)]'
t = timeit.Timer(stmt=snippet)
t.timeit(number=10000)  # returns: 0.05218779999995604


# The autorange method. It chooses the number of repetitions in the loop 
# automatically, aiming at total execution time >= 0.2 seconds.
snippet = '[x for x in range(1, 100)]'
t = timeit.Timer(stmt=snippet)
t.autorange()  # returns: (100000, 0.27417029999924125)

# The return value is tuple, where the first element is the number of repetitions,
# and the second one is the time measured in seconds.

cycle = """l = []
for num in range(1, 100):
    l.append(num)
"""
comprehension = "[num for num in range(1, 100)]"
a = timeit.timeit(cycle, number=100000)
b = timeit.timeit(comprehension, number=100000)
print(a, b)