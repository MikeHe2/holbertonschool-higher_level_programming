#!/usr/bin/python3

def search_replace(my_list, search, replace):

    newList = list(map(lambda act: replace if act == search else act, my_list))

    return newList
