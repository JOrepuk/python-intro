import re

def is_valid_email(email):
    """Validates an email address using a professional regex."""
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$)"
    return re.match(pattern, email) is not None

def calculate_rectangle_area(width, height):
    """Calculates the area of a rectangle. Raises ValueError for negative dimensions, TypeError for invalid types."""
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numbers.")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return width * height

def filter_even_numbers(numbers):
    """Filters even numbers from a list. Raises TypeError if non-numeric values are found."""
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numbers.")
    return [num for num in numbers if num % 2 == 0]

def convert_date_format(date_str):
    """Converts a date from 'dd-mm-yyyy' format to 'yyyy/mm/dd'. Raises ValueError for invalid formats."""
    try:
        day, month, year = date_str.split("-")
        if len(day) != 2 or len(month) != 2 or len(year) != 4:
            raise ValueError("Invalid date format.")
        return f"{year}/{month}/{day}"
    except ValueError:
        raise ValueError("Invalid date format.")
    
def is_palindrome(text):
    """Checks if a text is a palindrome, ignoring spaces and letter case."""
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]