import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for SimpleCalculator."""

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test SimpleCalculator.add with ints, floats, zero and large numbers."""
        cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (2.5, 0.5, 3.0),
            (10**9, 10**9, 2 * 10**9),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)

    def test_subtraction(self):
        """Test SimpleCalculator.subtract for normal and edge cases."""
        cases = [
            (5, 3, 2),
            (3, 5, -2),
            (0, 0, 0),
            (2.5, 1.2, 1.3),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                # Use almost equal for floats to avoid precision issues
                if isinstance(expected, float):
                    self.assertAlmostEqual(self.calc.subtract(a, b), expected, places=7)
                else:
                    self.assertEqual(self.calc.subtract(a, b), expected)

    def test_multiplication(self):
        """Test SimpleCalculator.multiply including zero, negatives and large values."""
        cases = [
            (4, 3, 12),
            (-2, 3, -6),
            (0, 12345, 0),
            (2.5, 4, 10.0),
            (10**6, 10**3, 10**9),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                if isinstance(expected, float):
                    self.assertAlmostEqual(self.calc.multiply(a, b), expected, places=7)
                else:
                    self.assertEqual(self.calc.multiply(a, b), expected)

    def test_division(self):
        """Test SimpleCalculator.divide for normal divisions (including floats)."""
        cases = [
            (6, 3, 2.0),
            (7, 2, 3.5),
            (-9, 3, -3.0),
            (0, 5, 0.0),
            (1, 3, 1.0/3.0),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                # Always compare floats for division
                result = self.calc.divide(a, b)
                self.assertIsNotNone(result)
                self.assertAlmostEqual(result, expected, places=7)

    def test_divide_by_zero(self):
        """Division by zero should return None as per the provided implementation."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()

