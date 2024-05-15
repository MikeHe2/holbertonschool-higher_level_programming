#!/usr/bin/python3

def uniq_add(my_list=[]):

    newList = set(my_list)
    sumNums = 0

    for i in newList:
        sumNums += i

    return sumNums
