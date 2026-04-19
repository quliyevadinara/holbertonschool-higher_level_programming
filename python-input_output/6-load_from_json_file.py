#!/usr/bin/python3
"""Module for loading objects from JSON files."""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename (str): The name of the file to load from.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
