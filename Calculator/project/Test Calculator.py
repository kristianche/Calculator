import unittest
from project.Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Calculator.add(2, 3), 5.0)
        self.assertEqual(Calculator.add(2, -3), -1.0)
        self.assertEqual(Calculator.add(-2, -3), -5.0)
        self.assertEqual(Calculator.add(0, 3), 3.0)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtract(20, 3), 17.0)
        self.assertEqual(Calculator.subtract(2, -3), 5.0)
        self.assertEqual(Calculator.subtract(0, -3), 3.0)
        self.assertEqual(Calculator.subtract(-2, -3), 1.0)

    def test_multiplication(self):
        self.assertEqual(Calculator.multiply(12, 12), 144.0)
        self.assertEqual(Calculator.multiply(0, 12), 0.0)
        self.assertEqual(Calculator.multiply(-3, -12), 36.0)
        self.assertEqual(Calculator.multiply(-12, 12), -144.0)

    def test_division(self):
        self.assertEqual(Calculator.division(0, 2), 0.0)
        self.assertEqual(Calculator.division(3, 0), "Cannot divide by zero!")
        self.assertEqual(Calculator.division(3, 2), 1.5)
        self.assertEqual(Calculator.division(-3, -2), 1.5)


if __name__ == '__main__':
    unittest.main()
