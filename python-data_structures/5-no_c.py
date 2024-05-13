#!/usr/bin/python3

def no_c(my_string):

    copy_my_string = list(my_string)
    j = 0

    for i in copy_my_string:
        if i == 'c' or i == 'C':
            copy_my_string[j] = ""
        j += 1
    return "".join(copy_my_string)
