#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    my_list.reverse() # reverse the list

    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
