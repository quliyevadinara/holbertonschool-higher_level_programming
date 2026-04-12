#!/usr/bin/python3
"""Module that defines BaseGeometry with validation methods."""


class BaseGeometry:
    """A base class for geometry with validation capabilities.

    This class provides an area method and validation for geometric
    parameters such as integer values for dimensions.
    """

    def area(self):
        """Calculate the area of the geometric shape.

        This method should be implemented by subclasses for specific
        shapes. Raises an exception if called on the base class.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name: The name of the parameter being validated (string).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
