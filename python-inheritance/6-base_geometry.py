#!/usr/bin/python3
"""
Module that defines a base class for geometry operations.
"""


class BaseGeometry:
    """
    Base class for geometry operations.
    """

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
