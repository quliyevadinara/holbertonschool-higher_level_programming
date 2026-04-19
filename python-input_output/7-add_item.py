#!/usr/bin/python3
"""Module for adding items to a JSON file."""

import sys
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Adds all arguments to a Python list, and then saves them to a file.
    """
    filename = "add_item.json"

    # Load existing list or create new one
    if Path(filename).exists():
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Add all command line arguments to the list
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    # Save the list back to the file
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
