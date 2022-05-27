x = 1
y = 2

print(f'x is {x}, y is {y}')
# Without a temporary variable
x, y = y, x
print(f'x is {x}, y is {y}')