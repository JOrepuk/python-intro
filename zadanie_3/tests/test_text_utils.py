import unittest
from pyhelpers.text_utils import is_palindrome, count_vowels, normalize_text

class TestTextUtils(unittest.TestCase):

    def test_is_palindrome_true(self):
        """Test valid palindromes."""
        palindromes = [
            "kajak",
            "Level",
            "kobyła ma mały bok",
            "A man a plan a canal Panama"
        ]
        for text in palindromes:
            with self.subTest(text=text):
                self.assertTrue(is_palindrome(text))

    def test_is_palindrome_false(self):
        """Test non-palindromes."""
        non_palindromes = ["python", "hello world", "banana"]
        for text in non_palindromes:
            with self.subTest(text=text):
                self.assertFalse(is_palindrome(text))

    def test_is_palindrome_invalid(self):
        """Test is_palindrome with non-string input."""
        with self.assertRaises(TypeError):
            is_palindrome(123)

    def test_count_vowels_basic(self):
        """Test count_vowels with mixed-case strings."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_count_vowels_invalid(self):
        """Test count_vowels with non-string input."""
        with self.assertRaises(TypeError):
            count_vowels(["a", "e", "i"])

    def test_normalize_text_basic(self):
        """Test normalize_text with punctuation and case."""
        self.assertEqual(normalize_text("Hello, World!"), "hello world")
        self.assertEqual(normalize_text("Python. 3.11!"), "python 311")

    def test_normalize_text_empty(self):
        """Test normalize_text with empty string."""
        self.assertEqual(normalize_text(""), "")

    def test_normalize_text_invalid(self):
        """Test normalize_text with non-string input."""
        with self.assertRaises(TypeError):
            normalize_text(3.14)