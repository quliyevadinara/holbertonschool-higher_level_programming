# Python Classes

This repository contains the `python-classes` project, which is part of the Holberton School Higher Level Programming curriculum. The goal of this project is to familiarize students with object-oriented programming in Python through various tasks related to classes and inheritance.

## Project Overview

The `python-classes` project includes six tasks based on the concept of a `Square`. Below are the descriptions of each task:

### Task 0: Square
- **Description**: Write a class `Square` that defines a square by its size.
- **Requirements**: The class should have a private attribute `size`, and a constructor to initialize it.

### Task 1: Square with Validation
- **Description**: Enhance the `Square` class to include validation for the size attribute. 
- **Requirements**: Ensure that `size` is an integer and greater than or equal to 0 when initializing.

### Task 2: Area of the Square
- **Description**: Implement a method in the `Square` class that calculates the area of the square.
- **Method**: `def area(self):` which returns the current square area.

### Task 3: String Representation
- **Description**: Provide a string representation for the `Square` class. 
- **Method**: Override the `__str__` method to customize the output format when printing the object.

### Task 4: Equality
- **Description**: Implement comparison methods in the `Square` class to compare size.
- **Methods**: Implement `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, and `__ge__` for comparing squares based on their sizes.

### Task 5: Square Dictionary
- **Description**: Implement a method to retrieve a dictionary representation of a `Square` instance.
- **Method**: `def to_dictionary(self):` that returns the dictionary representation of the square.

### Task 6: Save to JSON
- **Description**: Implement serialization and deserialization methods to save and load square objects in JSON format.
- **Methods**: `save_to_file()` and `load_from_file()` to handle file operations.

## Conclusion

This project aims to establish a solid foundation in Python classes and object-oriented programming principles. The `Square` class serves as an excellent example for understanding attributes, methods, and inheritance principles.

---

Date of Creation: 2026-04-05 18:18:54 UTC
