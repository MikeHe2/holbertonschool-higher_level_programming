#!/usr/bin/python3

"""This is a module"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): List of attributes to include in the dictionary
            representation. If None, all attributes are included.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            if isinstance(attrs, list) and all(isinstance(attr, str)
                for attr in attrs):

                return {attr: self.__dict__.get(attr) for attr in attrs
                    if attr in self.__dict__}
            else:
                return self.__dict__
