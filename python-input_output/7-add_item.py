#!/usr/bin/python3

"""This is a module"""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """
    Adds command line arguments to a list and saves it to a JSON file.

    If the JSON file already exists, the function loads the existing list
    from the file, appends the command line arguments to it, and then saves
    the updated list back to the file.  If the JSON file does not exist,
    the function creates a new list with the command line arguments
    and saves it to the file.

    Args:
        None

    Returns:
        None
    """
    try:
        my_list = load_from_json_file("add_item.json")
        my_list.extend(sys.argv[1:])
        save_to_json_file(my_list, "add_item.json")
    except Exception:
        my_list = sys.argv[1:]
        save_to_json_file(my_list, "add_item.json")
