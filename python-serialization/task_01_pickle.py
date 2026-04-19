#!/usr/bin/python3
"""
Module for pickling and unpickling custom Python objects.
"""

import pickle


class CustomObject:
    """
    A custom Python class with name, age, and is_student attributes.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The filename to save the serialized object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.

        Args:
            filename (str): The filename to load the serialized object.

        Returns:
            CustomObject: A CustomObject instance, or None if error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
