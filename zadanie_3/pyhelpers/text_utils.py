"""
Module providing helper functions for text processing.
"""

import string

def is_palindrome(text):
    """
    Checks whether the given text is a palindrome.

    The comparison ignores spaces and is case-insensitive.

    Args:
        text (str): The text to check.

    Returns:
        bool: True if text is a palindrome, False otherwise.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """
    Counts the number of vowels in the given text.

    Args:
        text (str): The input string.

    Returns:
        int: Number of vowels in the text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def normalize_text(text):
    """
    Normalizes text by converting it to lowercase and removing punctuation.

    Args:
        text (str): The text to normalize.

    Returns:
        str: Normalized text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    return ''.join(char.lower() for char in text if char not in string.punctuation)
