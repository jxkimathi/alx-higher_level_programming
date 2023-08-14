#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element of a list in the copied string"""
    replace = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        replace[idx] = element
        return replace
