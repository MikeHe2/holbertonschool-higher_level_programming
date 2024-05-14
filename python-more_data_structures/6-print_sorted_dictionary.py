#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sortDict = sorted(a_dictionary)

    for i in sortDict:
        print("{:s}: {}".format(i, a_dictionary[i]))
