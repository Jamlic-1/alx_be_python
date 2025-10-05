import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 0.5), 3.0)
        self.assertEqual(self.calc.add(10**9, 10**9), 2 * 10**9)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 12345), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(10**6, 10**3), 10**9)

    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(-9, 3), -3.0)
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_precision(self):
        # check float precision behavior
        self.assertAlmostEqual(self.calc.divide(1, 3), 1/3)
        self.assertAlmostEqual(self.calc.divide(10**6 + 1, 10**3), (10**6 + 1) / 10**3)

if __name__ == "__main__":
    unittest.main()
