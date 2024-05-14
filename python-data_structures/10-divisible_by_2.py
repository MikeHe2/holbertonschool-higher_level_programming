#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    newStr = []

    for i in my_list:
        if i % 2 == 0:
            newStr.append(True)
        else:
            newStr.append(False)

    return newStr
