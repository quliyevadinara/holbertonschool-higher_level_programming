# Python - Everything is Object

## Description

This project explores one of Python's most fundamental concepts: **everything is an object**. Through a series of questions and exercises, we investigate how Python manages objects in memory, the difference between mutable and immutable types, how variable assignment and aliasing work, and how arguments are passed to functions.

## Learning Objectives

At the end of this project, you should be able to explain:

- What is an object
- The difference between a class and an instance of a class
- The difference between immutable and mutable objects
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (memory address)
- What is `id()` and `type()`
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How Python passes variables to functions

## Requirements

- Python 3.8+
- All answer files contain a single line
- All Python files start with `#!/usr/bin/python3`
- No external modules allowed

## Files

| File | Description |
|------|-------------|
| `0-answer.txt` | Function to print the type of an object |
| `1-answer.txt` | Function to get the variable identifier (memory address) |
| `2-answer.txt` | Do `a = 89` and `b = 100` point to the same object? |
| `3-answer.txt` | Do `a = 89` and `b = 89` point to the same object? |
| `4-answer.txt` | Do `a = 89` and `b = a` point to the same object? |
| `5-answer.txt` | Do `a = 89` and `b = a + 1` point to the same object? |
| `6-answer.txt` | What does `print(s1 == s2)` print when `s2 = s1`? |
| `7-answer.txt` | What does `print(s1 is s2)` print when `s2 = s1`? |
| `8-answer.txt` | What does `print(s1 == s2)` print for two equal string literals? |
| `9-answer.txt` | What does `print(s1 is s2)` print for two equal string literals? |
| `10-answer.txt` | What does `print(l1 == l2)` print for two equal list literals? |
| `11-answer.txt` | What does `print(l1 is l2)` print for two equal list literals? |
| `12-answer.txt` | What does `print(l1 == l2)` print when `l2 = l1`? |
| `13-answer.txt` | What does `print(l1 is l2)` print when `l2 = l1`? |
| `14-answer.txt` | What does `print(l2)` print after `l1.append(4)` with `l2 = l1`? |
| `15-answer.txt` | What does `print(l2)` print after `l1 = l1 + [4]` with `l2 = l1`? |
| `16-answer.txt` | What does `print(a)` print after passing an int to an increment function? |
| `17-answer.txt` | What does `print(l)` print after passing a list to an append function? |
| `18-answer.txt` | What does `print(l1)` print after `assign_value(l1, l2)`? |
| `19-copy_list.py` | Function that returns a copy of a list |
| `20-answer.txt` | Is `a = ()` a tuple? |
| `21-answer.txt` | Is `a = (1, 2)` a tuple? |
| `22-answer.txt` | Is `a = (1)` a tuple? |
| `23-answer.txt` | Is `a = (1, )` a tuple? |
| `24-answer.txt` | What does `a is b` print for `a = (1)` and `b = (1)`? |
| `25-answer.txt` | What does `a is b` print for `a = (1, 2)` and `b = (1, 2)`? |
| `26-answer.txt` | What does `a is b` print for `a = ()` and `b = ()`? |
| `27-answer.txt` | Will `id(a)` be the same after `a = a + [5]`? |
| `28-answer.txt` | Will `id(a)` be the same after `a += [4]`? |

## Key Concepts

### `type()` and `id()`
```python
a = 42
print(type(a))   # <class 'int'>
print(id(a))     # memory address, e.g. 140245876543120
```

### `==` vs `is`
- `==` compares **values**
- `is` compares **identity** (same object in memory)

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True
print(a is b)   # False
```

### Mutable vs Immutable

**Immutable** (cannot be changed in place): `int`, `float`, `str`, `tuple`, `bool`

**Mutable** (can be changed in place): `list`, `dict`, `set`

```python
# Immutable — creates a new object
a = "hello"
a += " world"   # new string object

# Mutable — modifies in place
l = [1, 2, 3]
l.append(4)     # same list object
```

### Small Integer Caching
CPython caches integers from **-5 to 256**, so variables assigned the same small integer share the same object:
```python
a = 89
b = 89
print(a is b)   # True — cached

a = 1000
b = 1000
print(a is b)   # False — not cached
```

### Function Argument Passing
Python passes arguments **by object reference**. Mutating a mutable object inside a function affects the caller; rebinding does not:

```python
def mutate(lst):
    lst.append(4)       # affects caller

def rebind(lst):
    lst = [9, 9, 9]    # does NOT affect caller
```

## Author

This project is part of the **Holberton School Higher Level Programming** curriculum.

## Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-everything_is_object`