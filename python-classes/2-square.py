#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:

    """
    A class to represent a square.

    Attributes
    ----------
    size : int
        The size of the square.

    Methods
    -------
    __init__(self, size=0):
        Initializes the Square with the given size.
    """
    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
        size : int, optional
            The size of the square (default is 0).

        Raises
        ------
        TypeError
            If the size is not an integer.
        ValueError
            If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
