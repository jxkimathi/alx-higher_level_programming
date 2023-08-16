#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    new = []
    sum = 0
    for number in my_list:
        if number not in new:
            sum = sum + number
            new.append(number)
    return (sum)
