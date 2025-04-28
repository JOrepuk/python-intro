import unittest
from app import is_valid_email, calculate_rectangle_area, filter_even_numbers, convert_date_format, is_palindrome

class TestApp(unittest.TestCase):
    def setUp(self):
        """Prepare common data for tests."""
        self.valid_emails = ["example@test.com", "user.name@domain.co"]
        self.invalid_emails = ["exampletest.com", "example@com", "", "@."]
        self.rectangle_dimensions = [(5, 10, 50), (3.5, 2, 7.0)]
        self.palindromes = ["kajak", "Level", "kobyła ma mały bok"]
        self.non_palindromes = ["hello", "world"]

    # Tests for is_valid_email
    def test_is_valid_email_valid(self):
        """Test that valid emails return True."""
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_is_valid_email_invalid(self):
        """Test that invalid emails return False."""
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    # Tests for calculate_rectangle_area
    def test_calculate_rectangle_area_valid(self):
        """Test rectangle area calculation with positive numbers."""
        for width, height, expected_area in self.rectangle_dimensions:
            with self.subTest(width=width, height=height):
                self.assertEqual(calculate_rectangle_area(width, height), expected_area)

    def test_calculate_rectangle_area_zero(self):
        """Test rectangle area when one side is zero."""
        self.assertEqual(calculate_rectangle_area(0, 5), 0)
        self.assertEqual(calculate_rectangle_area(5, 0), 0)

    def test_calculate_rectangle_area_invalid(self):
        """Test rectangle area with negative values and wrong types."""
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-5, 10)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(5, -10)
        with self.assertRaises(TypeError):
            calculate_rectangle_area("a", 5)

    # Tests for filter_even_numbers
    def test_filter_even_numbers_basic(self):
        """Test filtering even numbers from a typical list."""
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_even_numbers([0, 7, 8, 10]), [0, 8, 10])

    def test_filter_even_numbers_empty(self):
        """Test filtering even numbers from an empty or odd-only list."""
        self.assertEqual(filter_even_numbers([]), [])
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])

    def test_filter_even_numbers_invalid_input(self):
        """Test that non-numeric values raise TypeError."""
        with self.assertRaises(TypeError):
            filter_even_numbers([2, "a", 4])
        with self.assertRaises(TypeError):
            filter_even_numbers(["one", "two"])

    # Tests for convert_date_format
    def test_convert_date_format_valid(self):
        """Test correct conversion of date format."""
        self.assertEqual(convert_date_format("28-04-2025"), "2025/04/28")
        self.assertEqual(convert_date_format("01-01-2000"), "2000/01/01")

    def test_convert_date_format_invalid(self):
        """Test invalid date formats raising ValueError."""
        with self.assertRaises(ValueError):
            convert_date_format("2025-04-28")
        with self.assertRaises(ValueError):
            convert_date_format("28/04/2025")
        with self.assertRaises(ValueError):
            convert_date_format("invalid-date")

    # Tests for is_palindrome
    def test_is_palindrome_basic(self):
        """Test that known palindromes return True."""
        for text in self.palindromes:
            with self.subTest(text=text):
                self.assertTrue(is_palindrome(text))

    def test_is_palindrome_not_palindrome(self):
        """Test that non-palindromes return False."""
        for text in self.non_palindromes:
            with self.subTest(text=text):
                self.assertFalse(is_palindrome(text))

    def test_is_palindrome_edge_cases(self):
        """Test that empty string and single space are palindromes."""
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome(" "))

if __name__ == '__main__':
    unittest.main()
