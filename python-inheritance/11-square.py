#!/usr/bin/python3
"""Module that defines a Square class with custom string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class with custom string representation.

    This class represents a square and overrides the string representation
    to display as [Square] instead of [Rectangle].
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

    def __str__(self):
        """Return a formatted string representation of the square.

        Returns:
            A string in the format "[Square] <size>/<size>".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
