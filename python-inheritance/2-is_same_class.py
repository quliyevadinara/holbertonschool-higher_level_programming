#!/usr/bin/python3
"""Module that provides a function to check exact class type."""


def is_same_class(obj, a_class):
    """Return True if object is exactly an instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
