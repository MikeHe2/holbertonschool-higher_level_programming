#!/usr/bin/python3
"""Defines a class called MyList."""


class MyList(list):
    """
    A subclass of list that provides an additional
    method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order without
        modifying the original list.
        """

        sorted_list = sorted(self)
        print(sorted_list)
