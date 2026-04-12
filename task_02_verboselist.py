#!/usr/bin/env python3
"""
Module for VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """Custom list class that prints notifications for modifications."""

    def append(self, item):
        """
        Append an item to the list with a notification.

        Args:
            item: The item to append to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from an iterable with a notification.

        Args:
            iterable: An iterable of items to add to the list.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove an item from the list with a notification.

        Args:
            item: The item to remove from the list.
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
        Remove and return an item at the given index with a notification.

        Args:
            index: The index of the item to pop (default: -1 for last item).

        Returns:
            The item that was removed from the list.
        """
        item = self[index]
        super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
