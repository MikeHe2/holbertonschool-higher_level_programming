#!/usr/bin/pthon3

def print_reversed_list_integer(my_list=[]):

    my_list.reverse() # reverse the list

    for i in range(len(my_list)):
        print(my_list[i])
