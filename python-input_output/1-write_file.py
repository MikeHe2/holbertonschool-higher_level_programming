#!/usr/bin/python3

"""This a module"""


def write_file(filename="", text=""):
    """
    Writes the given text to a file.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
