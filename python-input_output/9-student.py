#!/usr/bin/python3

"""This is a module"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Convert a Python object to a dictionary representation.

        Args:
            obj: The object to be converted.

        Returns:
            A dictionary representation of the object.
        """
        return self.__dict__
