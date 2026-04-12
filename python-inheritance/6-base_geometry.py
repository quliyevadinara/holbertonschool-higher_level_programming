#!/usr/bin/python3
"""Module that defines BaseGeometry class with area method."""


class BaseGeometry:
    """A base class for geometry-related classes.

    This class provides a foundation for geometry classes with a
    method to calculate area that must be implemented by subclasses.
    """

    def area(self):
        """Calculate the area of the geometric shape.

        This method should be implemented by subclasses for specific
        shapes. Raises an exception if called on the base class.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
