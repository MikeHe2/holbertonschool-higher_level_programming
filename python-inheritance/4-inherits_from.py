#!/usr/bin/python3
"""
Module that provides a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or
    indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited from the
        specified class, False otherwise.
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
