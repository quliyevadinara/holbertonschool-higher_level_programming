# Python - Exceptions

This project covers how to handle errors and exceptions in Python using `try`, `except`, `finally`, and how to raise exceptions.

## Learning Objectives

- What is the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What is the purpose of catching exceptions
- How to raise a built-in exception
- When do we need to implement a clean-up action after an exception

## Tasks

### 0. Safe list printing

**File:** `0-safe_print_list.py`

Prints `x` elements of a list on one line. Returns the real number of elements printed. Uses `try/except` without `len()`.

### 1. Safe printing of an integers list

**File:** `1-safe_print_integer.py`

Prints an integer using `"{:d}".format()`. Returns `True` if the value is an integer, `False` otherwise. Uses `try/except` without `type()`.

### 2. Print and count integers

**File:** `2-safe_print_list_integers.py`

Prints only integers from the first `x` elements of a list. Skips non-integers silently. Returns the count of integers printed.

### 3. Integers division with debug

**File:** `3-safe_print_division.py`

Divides two integers and always prints the result in the `finally` block. Returns the result or `None` if division by zero.

### 4. Divide a list

**File:** `4-list_division.py`

Divides two lists element by element. Handles wrong types, division by zero, and out-of-range indices, printing appropriate messages. Returns a new list of results.

### 5. Raise exception

**File:** `5-raise_exception.py`

Raises a `TypeError` exception.

### 6. Raise a message

**File:** `6-raise_exception_msg.py`

Raises a `NameError` exception with a custom message.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Code should use `pycodestyle` (version 2.7.\*)
- All files must be executable
    