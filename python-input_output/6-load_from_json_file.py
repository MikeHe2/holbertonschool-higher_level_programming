#!/usr/bin/python3

""""This is a module"""


import json

def load_from_json_file(filename):
    """
    Load data from a JSON file and return the deserialized object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The deserialized object from the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())