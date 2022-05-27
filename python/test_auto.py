import unittest
from unittest import TestCase

import auto

class TestAuto(unittest.TestCase):
  def test_check_length(self):
    self.assertTrue(auto.check_length('a'*80))
    self.assertFalse(auto.check_length('b'*79))
    self.assertTrue(auto.check_length('c'*100))
    self.assertFalse(auto.check_length('d'*5))

  
  def test_check_indentation(self):
    self.assertTrue(auto.check_indentation('     print()'))
    self.assertFalse(auto.check_indentation('    print()'))
    self.assertFalse(auto.check_indentation('    '))
    self.assertTrue(auto.check_indentation('     def()'))
if __name__ == '__main__':
  unittest.main()