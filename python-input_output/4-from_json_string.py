#!/usr/bin/python3

"""This module write a function that returns the JSON representation """

import json


def from_json_string(my_str):
    """
    Convert a Python object to a JSON string representation.

    Args:
        my_obj (Any): The Python object to be converted.

    Returns:
        str: A JSON string representation of the input object.
    """
    return json.loads(my_str)
