import unittest
from fizzbuzz import FizzBuzz

class Testplay(unittest.TestCase):

    def test_return_fizz(self):
        f = FizzBuzz()
        self.assertEqual(f.play(3), "Fizz")
        self.assertEqual(f.play(9), "Fizz")

    def test_return_buzz(self):
        f = FizzBuzz()
        self.assertEqual(f.play(5), "Buzz")
        self.assertEqual(f.play(10), "Buzz")

    def test_return_fizzbuzz(self):
        f = FizzBuzz()
        self.assertEqual(f.play(15), "FizzBuzz")
        self.assertEqual(f.play(30), "FizzBuzz")

    def test_return_num(self):
        f = FizzBuzz()
        self.assertEqual(f.play(2), 2)
        self.assertEqual(f.play(4), 4)


if __name__ == '__main__':
	unittest.main()
