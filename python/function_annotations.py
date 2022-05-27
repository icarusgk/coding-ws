# Function annotations let you add arbitrary metadata to function arguments
# and a return value

# They can be associated with various function parts
# Python doesn't attack any meaning to these annotations by itself
def square_area(side: 'length of square side') -> 'result of side ** 2':
    return side ** 2

print(square_area.__annotations__)  # call annotations attribute

# {'side': 'length of square side', 'return': 'result of side ** 2'}


# * Importance of annotations
# - They improve the way you write your code - It becomes more concise
# - They encourage you to think outside of the box
# - They help you and other people to understand the code easier
# - They help you identify type-related issues

# * Syntax of annotations
# In function annotations, an expression is any valid Python expression
# from a string "Bob drives a nice car." to object types (str, dict, list, etc.)
# and mathematic expressions (5 + 2)

# ? Annotations for single parameters
# An argument is followed by: and an expression
# The default arguments are specified after the annotation expression.
def func(argument: "expression", default_argument: "expression"=5):
  pass


# ? Annotations for excess parameters
# The excess parameters like *args and **kwargs allow passing an arbitrary number of
# arguments in the function call. The syntax is very similar to the one with single
# parameters
def func(*args: "expression", **kwars: "expression"):
  pass


# ? Annotations for nested parameters
# In the case of nested parameters, the annotation comes after the variables
# not after the "tuple". You don't need to annotate all members of a nested parameter
def func(x, y: "expression", a: "expression", b:"expression"=(None, None)):
  pass


# ? Annotations for the return type
# Annotation of the return type is quite different from argument annotation
# The return value is annotated with -> followed by an annotation expression.
def func(argument: "expression") -> "expression":
  pass


# * Accessing annotations
# All annotations are stored in a dictionary named __annotations__ 
# that is an attribute of the function
def func(x:'annotating x', y: 'annotating y', z: int) -> float:
    return x + y + z

print(func.__annotations__)
# {'x': 'annotating x', 'y': 'annotating y', 'z': <class 'int'>, 'return': <class 'float'>}


# * Case studies
# You can move an arguemnt and a return value from a docstring
def multiplication(a, b):
  """Multiply a by b 
  args:
      a - the multiplicand
      b - the multiplier
  return:
      the result of multiplying a by b
  """
  return a * b
    
def multiplication(a: 'the multiplicand', b: 'the multiplier') -> 'the result of multiplying a by b':
  """Multiply a by b"""
  return a * b


# A benefit of annotations over docstrings is that you can specify different types of 
# metadata, such as tuples or dictionaries
# Let's say you want to annotate arguments and a return value with both type and a 
# description string. You can do that by annotating with a dict that has two keys: 
# type and description
def multiplication(
  a: dict(description='the multiplicand', type=int), 
  b: dict(description='the multiplier', type=int)) -> dict(description='the result of multiplying a by b', type=int):
  """Multiply a by b"""
  return a * b


print(multiplication.__annotations__)

#{'a': {'description': 'the multiplicand', 'type': <class 'int'>},
# 'b': {'description': 'the multiplier', 'type': <class 'int'>},
# 'return': {'description': 'the result of multiplying a by b',
#            'type': <class 'int'>}}


# Another case where function annotations can be helpful is optional typing.
# Even though Python is dynamically typed, and any object can be passed as 
# a function argument, there are many cases when functions require arguments
# of a specific type. With annotations, you can specify the type right next 
# to the argument in a very natural way:
def addition(a: int, b: float) -> float:
  return a + b

# Remember that solely specifying the type is not going to enforce it. 
# But still, even specifying the type in annotation can make the intent more
# READABLE

