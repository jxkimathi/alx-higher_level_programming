#!/usr/bin/python3

def print_square(size):
    """Prints a square with the character '#'"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(size):
        [print("#", end="") for columns in range(size)]
        print()
