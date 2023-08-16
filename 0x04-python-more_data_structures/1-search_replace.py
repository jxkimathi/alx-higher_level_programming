#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list"""
    new = []
    for element in my_list:
        if element == search:
            new.append(replace)
        else:
            new.append(element)
    return new
