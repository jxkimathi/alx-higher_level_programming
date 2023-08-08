#!/usr/bin/python3
"""Prints string, removing the character at n"""


def remove_char_at(str, n):
    if n < 0:
        return (str)
    else:
        return (str[:n] + str[n+1:])
