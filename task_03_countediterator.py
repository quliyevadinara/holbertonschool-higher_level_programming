#!/usr/bin/env python3
"""
Module for CountedIterator class that tracks iteration count.
"""


class CountedIterator:
    """Iterator class that counts the number of items iterated."""

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.

        Args:
            iterable: The iterable to wrap with counting functionality.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Returns:
            The next item from the wrapped iterator.

        Raises:
            StopIteration: When there are no more items to iterate.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Get the number of items iterated so far.

        Returns:
            The count of items that have been iterated.
        """
        return self.count
