#!/usr/bin/python3
"""Module that provides a function to check class instance or inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if object is instance of or inherits from a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
