#!/usr/bin/python3

"""This is a module"""


def class_to_json(obj):
    """
    Convert a Python object to a dictionary representation.

    Args:
        obj: The object to be converted.

    Returns:
        A dictionary representation of the object.
    """
    return obj.__dict__
