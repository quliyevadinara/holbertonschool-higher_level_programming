# Python - Test-driven Development

This project covers test-driven development in Python, writing doctests and unittests before and alongside implementing functions.

## Learning Objectives

- What is an interactive test
- Why tests are important
- How to write docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Tasks

### 0. Integers addition

**File:** `0-add_integer.py` | **Tests:** `tests/0-add_integer.txt`

Adds two integers or floats (floats are cast to int). Raises `TypeError` if either argument is not an integer or float.

### 1. Divide a matrix

**File:** `2-matrix_divided.py` | **Tests:** `tests/2-matrix_divided.txt`

Divides all elements of a matrix by `div`, rounded to 2 decimal places. Raises appropriate errors for invalid types, unequal row sizes, and division by zero.

### 2. Say my name

**File:** `3-say_my_name.py` | **Tests:** `tests/3-say_my_name.txt`

Prints `My name is <first name> <last name>`. Raises `TypeError` if either argument is not a string.

### 3. Print square

**File:** `4-print_square.py` | **Tests:** `tests/4-print_square.txt`

Prints a square of `#` characters. Raises `TypeError` if size is not an integer, and `ValueError` if size is less than 0.

### 4. Text indentation

**File:** `5-text_indentation.py` | **Tests:** `tests/5-text_indentation.txt`

Prints text with 2 new lines after each `.`, `?`, and `:`. No spaces at the beginning or end of each line.

### 5. Max integer - Unittest

**File:** `6-max_integer.py` | **Tests:** `tests/6-max_integer_test.py`

Unittests for the `max_integer` function using the `unittest` module. Run with:

```bash
python3 -m unittest tests.6-max_integer_test
```

## How to Run Doctests

```bash
python3 -m doctest tests/0-add_integer.txt
python3 -m doctest tests/2-matrix_divided.txt
python3 -m doctest tests/3-say_my_name.txt
python3 -m doctest tests/4-print_square.txt
python3 -m doctest tests/5-text_indentation.txt
```

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Code should use `pycodestyle` (version 2.7.\*)
- All files must be executable
- All modules, functions and classes must have documentation
