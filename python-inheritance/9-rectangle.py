#!/usr/bin/python3
"""Module that defines a Rectangle class with area calculation."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class with area calculation and string representation.

    This class represents a rectangle with width and height dimensions,
    and provides methods to calculate area and represent the rectangle
    as a formatted string.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width: The width of the rectangle (positive integer).
            height: The height of the rectangle (positive integer).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a formatted string representation of the rectangle.

        Returns:
            A string in the format "[Rectangle] <width>/<height>".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
