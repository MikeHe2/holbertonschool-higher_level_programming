#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:

    """
    This class represents a square.

    Attributes
    ----------
    size : int
        The size of the square.

    Methods
    -------
    __init__(self, size=0):
        Initializes a new instance of the Square class.
    area(self):
        Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters
        ----------
        size : int, optional
            The size of the square (default is 0).

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size ** 2
