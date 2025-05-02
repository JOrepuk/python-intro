# pyhelpers – Python utility library

**pyhelpers** is a simple and modular Python library that provides utility functions for:

- basic mathematical operations
- text processing
- working with data structures

The library was created as part of Lab 3 in the course *Programowanie Zaawansowane*.

---

## 📦 Modules and Functions

### `math_tools.py`

- `factorial(n)` – calculates factorial of a non-negative integer
- `is_prime(n)` – checks if a number is prime
- `gcd(a, b)` – returns the greatest common divisor

### `text_utils.py`

- `is_palindrome(text)` – checks if a string is a palindrome (case-insensitive, ignores spaces)
- `count_vowels(text)` – counts vowels in a string
- `normalize_text(text)` – converts text to lowercase and removes punctuation

### `data_utils.py`

- `flatten_list(nested_list)` – flattens a nested list into a single list
- `unique_elements(lst)` – returns unique elements while preserving original order

---

## ✅ Features

- 3 modules, 8 documented utility functions
- 100% test coverage (checked with `coverage.py`)
- Unit tests for each function using Python's `unittest`
- Code follows PEP 8 standards
- MIT License

---

## 🔧 Installation

If using in development mode:

```
pip install -e .
```

Requirements: Python 3.8+

---

## 🧪 Running tests

```
python -m unittest discover tests
```

Or with test coverage:

```
python -m coverage run -m unittest discover tests
python -m coverage report -m
```

---

## 📝 License

MIT © 2025 Jakub Orepuk