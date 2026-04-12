#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """A list subclass with a method to print sorted contents.

    This class extends the built-in list class and adds functionality
    to print the list contents in sorted order without modifying
    the original list.
    """

    def print_sorted(self):
        """Print the list sorted in ascending order.

        Prints the list elements sorted in ascending order.
        The original list remains unchanged.
        """
        print(sorted(self))
