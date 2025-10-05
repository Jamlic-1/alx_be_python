# === simple_calculator.py ===
class SimpleCalculator:
"""A simple calculator class that supports basic arithmetic operations."""


def add(self, a, b):
return a + b


def subtract(self, a, b):
return a - b


def multiply(self, a, b):
return a * b


def divide(self, a, b):
if b == 0:
return None
return a / b




# === test_simple_calculator.py ===
import unittest
from simple_calculator import SimpleCalculator




class TestSimpleCalculator(unittest.TestCase):


def setUp(self):
self.calc = SimpleCalculator()


def test_addition(self):
self.assertEqual(self.calc.add(2, 3), 5)
self.assertEqual(self.calc.add(-1, 1), 0)
self.assertAlmostEqual(self.calc.add(2.5, 0.5), 3.0)


def test_subtraction(self):
self.assertEqual(self.calc.subtract(5, 3), 2)
self.assertEqual(self.calc.subtract(3, 5), -2)


def test_multiplication(self):
self.assertEqual(self.calc.multiply(4, 5), 20)
self.assertEqual(self.calc.multiply(4, 0), 0)


def test_division_normal(self):
self.assertEqual(self.calc.divide(10, 2), 5)
self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)


def test_division_by_zero(self):
self.assertIsNone(self.calc.divide(10, 0))




if __name__ == "__main__":
unittest.main()
