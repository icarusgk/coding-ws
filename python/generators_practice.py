def raise_to_4(n):
  yield n ** 4

def count():
  i = 0;
  while True:
    yield i
    i += 1

def multiply(n):
  for i in range(n):
    print("yielding", i)
    yield from raise_to_4(i)


multiples = multiply(6)

# print(next(multiples))
# print(next(multiples))
# print(next(multiples))

c = count()

print(next(c))
print(next(c))
print(next(c))



print(next(c))

# print(*multiples)
# for i in multiples:
#   print()
