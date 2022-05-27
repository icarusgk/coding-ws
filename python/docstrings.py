# To briefly describe the object's functionality and how to 
# use it, you can provide a general description via a docstring

# * What is a docstring?
# A docstring is a string literal. It is written as the first statement 
# in the definition of a module, a class, a method, a function, etc.

# PEP 257: each line in a docstring should be no longer than 72 characters.

# Importantly, we can access docstrings without reading the source code itself:
# for example, by using the __doc__ attribute:

print(str.count.__doc__)

# * Types of docstrings
# The two main types of documentation strings in Python are one-liners and multi-liners.

# One-line docstrings are a sort of quick summary for your object, 
# it is the shortest description

# Generally, it is better to provide a multi-line description, but in some obvious cases 
# that don't require further explanation, one-liners can be acceptable.

# * One-line docstring
def count_factorial(num):
  # Under PEP 257, you should follow the next conventions for docstrings
  # - The opening and the closing quotes should be on the same line.

  # - There should be no empty strings either before or after the docstring

  # - Your description should be imperative, that's why we need the wording 
  #   "Return the factorial" or "Return the number" instead of "Returns the number"

  # - The description is not a scheme that repeats the object's parameters and return
  #   values, like
  #   "count_factorial(num) -> int"
  """Return the factorial of the number."""
  if num == 0:
    return 1
  else:
    return num * count_factorial(num - 1)


print(count_factorial.__doc__)

# * Multi-line docstring
def c2ount_factorial(num):
  # - The summary is separated from the detailed description using a blank line.
  # - The detailed description starts at the same position as the first quote of 
  #   the first docstring line — there's no indent.
  """Return the factorial of the number
  
  Arguments:
  num -- an integer to count the factorial of.
  Return values:
  The integer factorial of the number
  """
  if num == 0:
    return 1
  else:
    return num * count_factorial(num - 1)

# * Classes and Modules
# Module docstrings should also provide a brief one-line description. 
# After that, it is recommended to specify all classes, methods, functions, 
# or any other of the module's objects.

# In class docstrings, apart from the general purpose of the class, you should 
# indicate the information about methods, instance variables, attributes, and so forth

# information.py module
"""The functionality for manipulating the user-related information."""

class Person:
  """The creation of the Person object and the related functionality."""

  def __init__(self, name, surname, birthdate):
    """The initializer for the class.
    
    Arguments:
    name -- a string representing the person's name.
    surname -- a string representing the person's surname.
    birthdate -- a string representing the person's birthdate.
    """
    self.name = name
    self.surname = surname
    self.birthdate = birthdate

  def calculate_age(self):
    """Return the current age of the person."""
    return 28


print(help(Person))