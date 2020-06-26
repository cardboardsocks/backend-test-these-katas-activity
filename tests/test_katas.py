import unittest
import katas
from katas import add, factorial, multiply, power, fibonacci

class TestKatas(unittest.TestCase):

    def test_add(self):
         self.assertEqual(add(4, 7), 11)

    def test_multiply(self):
        self.assertEqual(multiply(3, 6), 18)

    def test_power(self):
        self.assertEqual(power(4, 4), 256)
        

    def test_factorial(self):
        self.assertEqual(
            [factorial(n) for n in range(6)], [1, 1, 2, 6, 24, 120])

    def test_fibonacci(self):
        # dont know 
        pass



if __name__ == '__main__':
    unittest.main()
