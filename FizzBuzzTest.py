import unittest
from FizzBuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):

  def test_regular_numbers(self):
    self.assertEqual(fizzbuzz(1), "1")

  def test_multiples_of_three(self):
    self.assertEqual(fizzbuzz(3), "Fizz")
    self.assertEqual(fizzbuzz(6), "Fizz")

  def test_multiples_of_five(self):
    self.assertEqual(fizzbuzz(5), "Buzz")
    self.assertEqual(fizzbuzz(10), "Buzz")

  def test_multiples_of_three_and_five(self):
    self.assertEqual(fizzbuzz(15), "FizzBuzz")
    self.assertEqual(fizzbuzz(30), "FizzBuzz")

if __name__ == '__main__':
  unittest.main()
