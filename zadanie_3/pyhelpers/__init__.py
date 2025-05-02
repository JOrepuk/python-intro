"""
pyhelpers: A small utility library with math, text and data tools.
"""

from .math_tools import factorial, is_prime, gcd
from .text_utils import is_palindrome, count_vowels, normalize_text
from .data_utils import flatten_list, unique_elements

__all__ = [
    "factorial", "is_prime", "gcd",
    "is_palindrome", "count_vowels", "normalize_text",
    "flatten_list", "unique_elements"
]