import unittest
from fizzbuzz import FizzBuzz

class TestSum(unittest.TestCase):

    def test_play(self):
        f = FizzBuzz()
        self.assertEqual(f.play([3]) == "Fizz", "Should return Fizz")

    def test_play(self):
        f = FizzBuzz()
        self.assertEqual(f.play([2]) == 2, "Should return 2")

if __name__ == "__main__":
    unittest.main()
