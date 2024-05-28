#!/usr/bin/python3

"""This module write a function that returns the JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """
    Convert a Python object to a JSON string representation and save it
    to a file.

    Args:
        my_obj (Any): The Python object to be converted to JSON.
        filename (str): The name of the file to save the JSON string to.

    Returns:
        int: The number of characters written to the file.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        PermissionError: If the user does not have permission to write to
        the file.
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
