#!/usr/bin/python3
"""Module that provides a function to check indirect inheritance."""


def inherits_from(obj, a_class):
    """Return True if object inherits from a class indirectly.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited from a_class
        (directly or indirectly), False otherwise. Returns False if obj
        is directly an instance of a_class.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
