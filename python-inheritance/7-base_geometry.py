#!/usr/bin/python3
"""
Module that defines a base class for geometry operations.
"""


class BaseGeometry:
    """
    Base class for geometry operations.
    """

    def integer_validator(self, name, value):
        """
        Validate that a parameter is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value of the parameter to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """
        Calculate the area of a geometric shape.

        This method should be overridden by subclasses to provide
        the specific area calculation.

        Raises:
            Exception: Always raises an exception indicating that
            the method is not implemented.
        """
        raise Exception("area() is not implemented")
