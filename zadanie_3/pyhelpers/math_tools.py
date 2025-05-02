"""
Module containing basic mathematical utility functions.
"""

def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """
    Checks whether a number is a prime.

    Args:
        n (int): An integer greater than 1.

    Returns:
        bool: True if n is a prime number, False otherwise.

    Raises:
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer.")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a, b):
    """
    Computes the greatest common divisor (GCD) of two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Raises:
        TypeError: If either a or b is not an integer.
    """
    if not all(isinstance(x, int) for x in (a, b)):
        raise TypeError("Arguments must be integers.")
    while b != 0:
        a, b = b, a % b
    return abs(a)
