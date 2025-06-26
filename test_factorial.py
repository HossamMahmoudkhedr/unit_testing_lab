from factorial import Calc
import unittest

class TestFactorial(unittest.TestCase):
    def test_fac(self):
        self.assertEqual(Calc.factorial(0), 1)
        self.assertEqual(Calc.factorial(1), 1)
        self.assertEqual(Calc.factorial(5), 120)
        self.assertEqual(Calc.factorial(-3), None)
        self.assertEqual(Calc.factorial(1.5), None)
        self.assertEqual(Calc.factorial(False), None)
        self.assertEqual(Calc.factorial('abc'), None)

if __name__ == '__main__':
    unittest.main()