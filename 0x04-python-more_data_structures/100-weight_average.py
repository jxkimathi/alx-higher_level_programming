#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple"""
    if not my_list:
        return 0
    num = 0
    dem = 0
    for tuple in my_list:
        num += (tuple[0] * tuple[1])
        dem += tuple[1]
    return (num / dem)
