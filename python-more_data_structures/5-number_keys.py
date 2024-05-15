#!/usr/bin/python3

def number_keys(a_dictionary):

    keyList = a_dictionary.keys()
    key = 0

    for i in keyList:
        key += 1

    return key

# Could solve this problem with just "return len(a_dictionary)"
