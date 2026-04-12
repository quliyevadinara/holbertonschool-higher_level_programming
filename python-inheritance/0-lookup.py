#!/usr/bin/python3
"""Module that provides a function to lookup object attributes and methods."""


def lookup(obj):
    """Return a list containing all attributes and methods of an object.

    Args:
        obj: Any Python object to inspect.

    Returns:
        A list of all attributes and methods of the given object.
    """
    return dir(obj)
