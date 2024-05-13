#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    copy_myList = my_list

    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy_myList[idx] = element
    return(copy_myList)
