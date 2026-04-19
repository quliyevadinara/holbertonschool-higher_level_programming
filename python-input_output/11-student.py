#!/usr/bin/python3
"""Module for Student class with reload functionality."""


class Student:
    """
    Class that defines a student.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): Optional list of attribute names to include.

        Returns:
            dict: The dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary with public attribute names as keys.
        """
        for key, value in json.items():
            setattr(self, key, value)
