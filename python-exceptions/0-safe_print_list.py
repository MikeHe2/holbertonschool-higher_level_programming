#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:

        numIterates = 0

        for i in range (x):
            print("{:d}".format(my_list[i]), end='')
            numIterates += 1
        print()
        return numIterates

    except IndexError:

        print()
        return numIterates
