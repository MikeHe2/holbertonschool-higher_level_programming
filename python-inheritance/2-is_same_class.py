#!/usr/bin/python3
"""
Module that provides a function to check if an object is exactly an
instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the
        specified class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
