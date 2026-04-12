#!/usr/bin/env python3
"""
Module for demonstrating mixins with SwimMixin, FlyMixin, and Dragon.
"""


class SwimMixin:
    """Mixin class that adds swimming capability."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that adds flying capability."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from SwimMixin and FlyMixin."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
