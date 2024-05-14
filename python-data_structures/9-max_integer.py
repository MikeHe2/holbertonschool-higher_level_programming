#!/usr/bin/python3

def max_integer(my_list=[]):


    lenght = len(my_list)

    if lenght == 0:
        return None

    maxNum = my_list[0]

    for i in range(1, lenght):
        if my_list[i] > maxNum:
            maxNum = my_list[i]

    return maxNum

