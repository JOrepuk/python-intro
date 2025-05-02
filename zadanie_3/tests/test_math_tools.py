import unittest
from pyhelpers.math_tools import factorial, is_prime, gcd

class TestMathTools(unittest.TestCase):

    def test_factorial_valid(self):
        """Test correct factorial values."""
        test_cases = [(0, 1), (1, 1), (5, 120), (7, 5040)]
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(factorial(n), expected)

    def test_factorial_invalid(self):
        """Test factorial with invalid input (negative or non-integer)."""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial("abc")

    def test_is_prime_true(self):
        """Test known prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        for n in primes:
            with self.subTest(n=n):
                self.assertTrue(is_prime(n))

    def test_is_prime_false(self):
        """Test known non-prime numbers."""
        non_primes = [0, 1, 4, 6, 8, 9, 15, 21, 49, 121]
        for n in non_primes:
            with self.subTest(n=n):
                self.assertFalse(is_prime(n))
                

    def test_is_prime_invalid(self):
        """Test is_prime with invalid input."""
        with self.assertRaises(TypeError):
            is_prime(2.5)
        with self.assertRaises(TypeError):
            is_prime("eleven")

    def test_gcd_valid(self):
        """Test GCD with valid integer pairs."""
        test_cases = [(10, 5, 5), (21, 14, 7), (100, 25, 25), (17, 13, 1)]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(gcd(a, b), expected)

    def test_gcd_invalid(self):
        """Test GCD with non-integer input."""
        with self.assertRaises(TypeError):
            gcd(10, "five")
        with self.assertRaises(TypeError):
            gcd("ten", 5)
        with self.assertRaises(TypeError):
            gcd(3.5, 2)

    def test_gcd_with_zero(self):
        """Test GCD when one argument is zero."""
        self.assertEqual(gcd(42, 0), 42)
        self.assertEqual(gcd(0, 42), 42)
