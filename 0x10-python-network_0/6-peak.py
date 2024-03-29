#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds the peak"""
    if list_of_integers == []:
        return None

    x = len(list_of_integers)
    if x == 1:
        return list_of_integers[0]
    elif x == 2:
        return max(list_of_integers)

    mi = int(x / 2)
    peak = list_of_integers[mi]

    if peak > list_of_integers[mi - 1] and peak > list_of_integers[mi + 1]:
        return peak
    elif peak < list_of_integers[mi - 1]:
        return find_peak(list_of_integers[:mi])
    else:
        return find_peak(list_of_integers[mi + 1:])
