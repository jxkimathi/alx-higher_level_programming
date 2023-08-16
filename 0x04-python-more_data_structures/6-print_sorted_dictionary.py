#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    keys = list(a_dictionary.keys())
    keys.sort
    for sorted_keys in keys:
        print("{}: {}".format(sorted_keys, a_dictionary[sorted_keys]))
