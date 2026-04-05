#!/usr/bin/python3
"""
1-square.py - Square class with private size attribute

This module defines a Square class with a private size attribute.
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The private size of the square.
    """

    def __init__(self, size):
        """
        Initialize a Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
