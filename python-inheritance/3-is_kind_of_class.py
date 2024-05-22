#!/usr/bin/python3
"""
Module that provides a function to check if an object is an instance or
an instance of a subclass of a given class.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance or an instance of a subclass of the
    specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance or an instance of a subclass of
        the specified class, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
