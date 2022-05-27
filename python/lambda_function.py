# Small functions
# anonymous
lambda x: 2 * x

# lambda arguments: expression 
lambda x: 'even' if x % 2 == 0 else 'odd'

# Invoking it
(lambda x, y: (x + y))(1, 5)

# assing it to a variable
say_name = lambda name: f'Hi there {name}'
print(say_name('icarus'))

# When is it useful?
def n_raiser(n):
  return lambda x: n * x

doubler = n_raiser(2)
tripler = n_raiser(3)

print(doubler(4))

sorted(['lion', 'cat', 'rhyno', 'leopard'], key=len, reverse=True)
['leopard', 'rhyno', 'lion', 'cat']