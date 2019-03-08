import unittest
from fizzbuzz import FizzBuzz

class Testplay(unittest.TestCase):

    def test_return_fizz(self):
        f = FizzBuzz()
        self.assertEqual(f.play(3), "Fizz")

    def test_return_buzz(self):
        f = FizzBuzz()
        self.assertEqual(f.play(5), "Buzz")

    def test_return_fizzbuzz(self):
        f = FizzBuzz()
        self.assertEqual(f.play(15), "FizzBuzz")

    def test_return_num(self):
        f = FizzBuzz()
        self.assertEqual(f.play(2), 2)

if __name__ == '__main__':
	unittest.main()
