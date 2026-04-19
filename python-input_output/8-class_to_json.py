#!/usr/bin/python3
"""Module for converting class instances to dictionaries."""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for
    JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__
