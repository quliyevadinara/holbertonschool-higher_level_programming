#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle.

    This class represents a square, which is a special case of a rectangle
    where width and height are equal. It is instantiated with a single
    size parameter.
    """

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size: The size of the square (positive integer).
                This value is used for both width and height.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
