#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Prints all integers of a list"""
    for index in my_list:
        print("{}".format(my_list[index - 1]))
