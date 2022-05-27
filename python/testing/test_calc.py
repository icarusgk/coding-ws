import unittest
import calc

class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.calc = calc.Calculator(5, 1)
    print('setUp method')
  
  def tearDown(self):
    print('tearDown method')

  def test_add(self):
    self.assertEqual(self.calc.add(), 6)
    self.calc.first = 8
    self.calc.second = 2
    self.assertEqual(self.calc.add(), 10)
    print('test_add method')

  def test_substract(self):
    self.assertEqual(self.calc.substract(), 4)
    self.calc.first = 8
    self.calc.second = 2
    self.assertEqual(self.calc.substract(), 6)
    print('test_substract method')

  
if __name__ == '__main__':
  unittest.main()