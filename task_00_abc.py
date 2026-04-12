#!/usr/bin/env python3
"""
Module for abstract Animal class and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """Dog class that implements the sound method."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Cat class that implements the sound method."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
