# It is better to store tests in a separate file, and it
# is advisable to start the name of the file with test.

import unittest
from unittest import TestCase

import calculator


# * Time to test!
# A test case is a basic unit of testing, it checks that the tested unit
# prouces the right output when given various kinds of input.

# We create a test case by subclassing the general TestCase class
class TestCalculator(unittest.TestCase):
  # In this case, the tested unit is the whole module
  # In Python, the tested unit can be a class, a method, or a function

  # All tests will now be defined as methods inside this class.

  # The names of the methods must start with test. Otherwise, it is not going
  # to work properly

  # Note that inside one test we check several cases
  # It is important that we check all possible border cases and all cases
  # when something can go wrong.

  def test_add(self):
    # All assert methods accept a message argument that is used as the error
    # message if the test fails
    self.assertEqual(calculator.add(6, 4), 10, 'Error when adding two positive numbers')
    self.assertEqual(calculator.add(6, -4), 2)
    self.assertEqual(calculator.add(-6, 4), -2)
    self.assertEqual(calculator.add(-6, -4), -10)

  def test_divide(self):
    self.assertRaises(ValueError, calculator.divide, 5, 0)
    # Alternatively, we can use a context manager, within which we call the tested fn
    with self.assertRaises(ValueError):
      calculator.divide(9, 0)


# an easier way to run the tests right from the editor and get the message
if __name__ == '__main__':
  unittest.main()