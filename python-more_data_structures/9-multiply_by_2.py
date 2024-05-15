#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    multDict = a_dictionary.copy()
    keysList = list(multDict.keys())

    for i in keysList:
        multDict[i] = multDict[i] * 2

    return multDict
