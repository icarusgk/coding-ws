a = [1, 2, 3]
b = [1, 2, 3]
c = a

a[0] = 5

print(a)  # [5, 2, 3] - changed
print(b)  # [1, 2, 3] - didn't change
print(c)  # [5, 2, 3] - also changed

a = [5, 6]
print(c)